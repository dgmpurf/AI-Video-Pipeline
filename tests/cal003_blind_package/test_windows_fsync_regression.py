from __future__ import annotations

import hashlib
import inspect
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.cal003_blind_package import (
    FailurePhase,
    OperationCode,
    PhaseTracker,
    flush_file_durable,
)


def _test_root() -> Path:
    root = Path(os.environ["CAL003_REPAIR_TEMP_ROOT"])
    root.mkdir(parents=True, exist_ok=True)
    return root


class WindowsFsyncRegressionTests(unittest.TestCase):
    def test_legacy_read_only_fsync_is_reproduced_or_simulated(self) -> None:
        with tempfile.TemporaryDirectory(dir=_test_root()) as directory:
            path = Path(directory) / "legacy.bin"
            path.write_bytes(b"synthetic-legacy")
            if os.name == "nt":
                with path.open("rb") as handle:
                    with self.assertRaises(OSError) as captured:
                        os.fsync(handle.fileno())
                self.assertEqual(captured.exception.errno, 9)
            else:
                captured_error = OSError(9, "synthetic legacy failure")
                self.assertEqual(captured_error.errno, 9)

    def test_writable_helper_preserves_bytes_and_sha256(self) -> None:
        with tempfile.TemporaryDirectory(dir=_test_root()) as directory:
            path = Path(directory) / "durable.bin"
            original = b"deterministic-durable-bytes"
            path.write_bytes(original)
            before = hashlib.sha256(path.read_bytes()).hexdigest()
            tracker = PhaseTracker()
            flush_file_durable(
                path,
                tracker=tracker,
                phase=FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
                operation=OperationCode.FLUSH_PARTIAL_ZIP,
            )
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), before)

    def test_helper_opens_exact_r_plus_b_mode(self) -> None:
        with tempfile.TemporaryDirectory(dir=_test_root()) as directory:
            path = Path(directory) / "mode.bin"
            path.write_bytes(b"mode")
            handle = mock.MagicMock()
            handle.__enter__.return_value = handle
            handle.fileno.return_value = 41
            with (
                mock.patch.object(Path, "open", return_value=handle) as opened,
                mock.patch("tools.cal003_blind_package.durability.os.fsync"),
            ):
                flush_file_durable(
                    path,
                    tracker=PhaseTracker(),
                    phase=FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
                    operation=OperationCode.FLUSH_PARTIAL_ZIP,
                )
            opened.assert_called_once_with("r+b")

    def test_flush_precedes_fsync(self) -> None:
        with tempfile.TemporaryDirectory(dir=_test_root()) as directory:
            path = Path(directory) / "order.bin"
            path.write_bytes(b"order")
            events: list[str] = []
            handle = mock.MagicMock()
            handle.__enter__.return_value = handle
            handle.flush.side_effect = lambda: events.append("flush")
            handle.fileno.side_effect = lambda: events.append("fileno") or 42
            with (
                mock.patch.object(Path, "open", return_value=handle),
                mock.patch(
                    "tools.cal003_blind_package.durability.os.fsync",
                    side_effect=lambda _: events.append("fsync"),
                ),
            ):
                flush_file_durable(
                    path,
                    tracker=PhaseTracker(),
                    phase=FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
                    operation=OperationCode.FLUSH_PARTIAL_ZIP,
                )
            self.assertLess(events.index("flush"), events.index("fsync"))

    def test_helper_records_explicit_phase_and_operation(self) -> None:
        with tempfile.TemporaryDirectory(dir=_test_root()) as directory:
            path = Path(directory) / "phase.bin"
            path.write_bytes(b"phase")
            tracker = PhaseTracker()
            flush_file_durable(
                path,
                tracker=tracker,
                phase=FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
                operation=OperationCode.FLUSH_PARTIAL_ZIP,
            )
            self.assertEqual(tracker.phase, FailurePhase.SEALED_PACKAGE_FILE_FLUSH)
            self.assertEqual(tracker.operation, OperationCode.FLUSH_PARTIAL_ZIP)

    def test_symlink_is_rejected_before_open(self) -> None:
        path = _test_root() / "synthetic-link"
        with mock.patch.object(Path, "is_symlink", return_value=True):
            with self.assertRaises(ValueError):
                flush_file_durable(
                    path,
                    tracker=PhaseTracker(),
                    phase=FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
                    operation=OperationCode.FLUSH_PARTIAL_ZIP,
                )

    def test_helper_source_contains_no_read_only_open(self) -> None:
        source = inspect.getsource(flush_file_durable)
        self.assertIn('path.open("r+b")', source)
        self.assertNotIn('path.open("rb")', source)


if __name__ == "__main__":
    unittest.main()
