from __future__ import annotations

import hashlib
import inspect
import os
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from unittest import mock

from tools.cal003_blind_package import (
    FailurePhase,
    OperationCode,
    PhaseTracker,
    atomic_publish_verified_zip,
    cleanup_task_created_paths,
    validate_zip_archive,
)


def _global_test_root() -> Path:
    root = Path(os.environ["CAL003_REPAIR_TEMP_ROOT"])
    root.mkdir(parents=True, exist_ok=True)
    return root


class AtomicZipPersistenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory(dir=_global_test_root())
        self.root = Path(self._temporary.name)
        self.partial = self.root / "synthetic.partial"
        self.final = self.root / "synthetic.zip"
        self.members = {
            "fixture_alpha.txt": b"alpha",
            "fixture_beta.json": b'{"beta":true}\n',
            "fixture_manifest.txt": b"manifest\n",
        }
        self.hashes = {
            name: hashlib.sha256(data).hexdigest()
            for name, data in self.members.items()
        }

    def tearDown(self) -> None:
        self._temporary.cleanup()

    def _write_zip(self, members: dict[str, bytes] | None = None) -> None:
        with zipfile.ZipFile(self.partial, "w", zipfile.ZIP_STORED) as archive:
            for name, data in (members or self.members).items():
                archive.writestr(name, data)

    def _publish(self, tracker: PhaseTracker | None = None) -> PhaseTracker:
        active_tracker = tracker or PhaseTracker()
        active_tracker.transition(
            FailurePhase.SEALED_ZIP_WRITE,
            OperationCode.WRITE_PARTIAL_ZIP,
        )
        atomic_publish_verified_zip(
            self.partial,
            self.final,
            expected_members=set(self.members),
            expected_member_hashes=self.hashes,
            commitment_verifier=lambda _: True,
            tracker=active_tracker,
        )
        return active_tracker

    def test_valid_zip_is_atomically_published(self) -> None:
        self._write_zip()
        tracker = self._publish()
        self.assertFalse(self.partial.exists())
        self.assertTrue(self.final.exists())
        self.assertEqual(tracker.phase, FailurePhase.COMPLETE)

    def test_final_bytes_are_unchanged_by_durability_flush(self) -> None:
        self._write_zip()
        before = self.partial.read_bytes()
        self._publish()
        self.assertEqual(self.final.read_bytes(), before)

    def test_wrong_member_set_blocks_before_rename(self) -> None:
        self._write_zip()
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_ZIP_WRITE,
            OperationCode.WRITE_PARTIAL_ZIP,
        )
        with self.assertRaises(ValueError):
            atomic_publish_verified_zip(
                self.partial,
                self.final,
                expected_members={"fixture_alpha.txt"},
                expected_member_hashes={
                    "fixture_alpha.txt": self.hashes["fixture_alpha.txt"]
                },
                commitment_verifier=lambda _: True,
                tracker=tracker,
            )
        self.assertTrue(self.partial.exists())
        self.assertFalse(self.final.exists())

    def test_duplicate_member_blocks(self) -> None:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(self.partial, "w", zipfile.ZIP_STORED) as archive:
                archive.writestr("fixture_alpha.txt", b"alpha")
                archive.writestr("fixture_alpha.txt", b"alpha")
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            validate_zip_archive(
                self.partial,
                expected_members={"fixture_alpha.txt"},
                expected_member_hashes={
                    "fixture_alpha.txt": hashlib.sha256(b"alpha").hexdigest()
                },
                commitment_verifier=lambda _: True,
                tracker=tracker,
                phase=FailurePhase.SEALED_ZIP_INTEGRITY,
                operation=OperationCode.VERIFY_PARTIAL_ZIP,
            )

    def test_wrong_member_hash_blocks(self) -> None:
        self._write_zip()
        wrong = dict(self.hashes)
        wrong["fixture_alpha.txt"] = "0" * 64
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            validate_zip_archive(
                self.partial,
                expected_members=set(self.members),
                expected_member_hashes=wrong,
                commitment_verifier=lambda _: True,
                tracker=tracker,
                phase=FailurePhase.SEALED_ZIP_INTEGRITY,
                operation=OperationCode.VERIFY_PARTIAL_ZIP,
            )

    def test_commitment_false_blocks(self) -> None:
        self._write_zip()
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            validate_zip_archive(
                self.partial,
                expected_members=set(self.members),
                expected_member_hashes=self.hashes,
                commitment_verifier=lambda _: False,
                tracker=tracker,
                phase=FailurePhase.SEALED_ZIP_INTEGRITY,
                operation=OperationCode.VERIFY_PARTIAL_ZIP,
            )

    def test_cross_volume_is_rejected_deterministically(self) -> None:
        self._write_zip()
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_ZIP_WRITE,
            OperationCode.WRITE_PARTIAL_ZIP,
        )
        with mock.patch(
            "tools.cal003_blind_package.durability._volume_identity",
            side_effect=[("drive", "a:"), ("drive", "b:")],
        ):
            with self.assertRaises(ValueError):
                atomic_publish_verified_zip(
                    self.partial,
                    self.final,
                    expected_members=set(self.members),
                    expected_member_hashes=self.hashes,
                    commitment_verifier=lambda _: True,
                    tracker=tracker,
                )

    def test_existing_final_is_rejected(self) -> None:
        self._write_zip()
        self.final.write_bytes(b"existing")
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_ZIP_WRITE,
            OperationCode.WRITE_PARTIAL_ZIP,
        )
        with self.assertRaises(FileExistsError):
            atomic_publish_verified_zip(
                self.partial,
                self.final,
                expected_members=set(self.members),
                expected_member_hashes=self.hashes,
                commitment_verifier=lambda _: True,
                tracker=tracker,
            )

    def test_replace_is_called_once_without_retry(self) -> None:
        self._write_zip()
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_ZIP_WRITE,
            OperationCode.WRITE_PARTIAL_ZIP,
        )
        with mock.patch(
            "tools.cal003_blind_package.durability.os.replace",
            side_effect=OSError(5, "synthetic replace failure"),
        ) as replaced:
            with self.assertRaises(OSError):
                atomic_publish_verified_zip(
                    self.partial,
                    self.final,
                    expected_members=set(self.members),
                    expected_member_hashes=self.hashes,
                    commitment_verifier=lambda _: True,
                    tracker=tracker,
                )
        replaced.assert_called_once_with(self.partial, self.final)

    def test_pipeline_history_contains_both_flush_phases(self) -> None:
        self._write_zip()
        tracker = self._publish()
        phases = [phase for phase, _ in tracker.history]
        self.assertIn(FailurePhase.SEALED_PACKAGE_FILE_FLUSH, phases)
        self.assertIn(FailurePhase.FINAL_PACKAGE_FILE_FLUSH, phases)
        self.assertIn(FailurePhase.FINAL_ZIP_INTEGRITY, phases)

    def test_cleanup_removes_only_explicit_files(self) -> None:
        self.partial.write_bytes(b"partial")
        self.final.write_bytes(b"final")
        summary = cleanup_task_created_paths(
            [self.partial, self.final],
            allowed_root=self.root,
            tracker=PhaseTracker(),
        )
        self.assertEqual(summary, {"already_absent": 0, "removed": 2, "requested": 2})

    def test_cleanup_tolerates_absent_path(self) -> None:
        summary = cleanup_task_created_paths(
            [self.partial],
            allowed_root=self.root,
            tracker=PhaseTracker(),
        )
        self.assertEqual(summary["already_absent"], 1)

    def test_cleanup_rejects_escape(self) -> None:
        outside = self.root.parent / f"{self.root.name}_outside.bin"
        outside.write_bytes(b"outside")
        try:
            with self.assertRaises(ValueError):
                cleanup_task_created_paths(
                    [outside],
                    allowed_root=self.root,
                    tracker=PhaseTracker(),
                )
        finally:
            outside.unlink()

    def test_cleanup_rejects_repository_paths(self) -> None:
        self.partial.write_bytes(b"protected")
        with self.assertRaises(ValueError):
            cleanup_task_created_paths(
                [self.partial],
                allowed_root=self.root,
                repository_root=self.root,
                tracker=PhaseTracker(),
            )

    def test_traversal_member_is_rejected(self) -> None:
        self._write_zip({"../escape.txt": b"escape"})
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            validate_zip_archive(
                self.partial,
                expected_members={"../escape.txt"},
                expected_member_hashes={
                    "../escape.txt": hashlib.sha256(b"escape").hexdigest()
                },
                commitment_verifier=lambda _: True,
                tracker=tracker,
                phase=FailurePhase.SEALED_ZIP_INTEGRITY,
                operation=OperationCode.VERIFY_PARTIAL_ZIP,
            )

    def test_absolute_member_is_rejected(self) -> None:
        self._write_zip({"/absolute.txt": b"absolute"})
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            validate_zip_archive(
                self.partial,
                expected_members={"/absolute.txt"},
                expected_member_hashes={
                    "/absolute.txt": hashlib.sha256(b"absolute").hexdigest()
                },
                commitment_verifier=lambda _: True,
                tracker=tracker,
                phase=FailurePhase.SEALED_ZIP_INTEGRITY,
                operation=OperationCode.VERIFY_PARTIAL_ZIP,
            )

    def test_atomic_helper_contains_no_directory_fsync(self) -> None:
        source = inspect.getsource(atomic_publish_verified_zip)
        self.assertNotIn("os.fsync", source)
        self.assertNotIn("copy", source)


if __name__ == "__main__":
    unittest.main()
