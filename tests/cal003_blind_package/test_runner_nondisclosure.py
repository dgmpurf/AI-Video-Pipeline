from __future__ import annotations

import ast
import dataclasses
import hashlib
import inspect
import os
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

import tools.cal003_blind_package.runner as runner_module
from tools.cal003_blind_package import (
    BlindPackagePersistenceRunner,
    FailurePhase,
    PhaseTracker,
    RunnerResult,
)


def _global_test_root() -> Path:
    root = Path(os.environ["CAL003_REPAIR_TEMP_ROOT"])
    root.mkdir(parents=True, exist_ok=True)
    return root


class RunnerNondisclosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory(dir=_global_test_root())
        self.root = Path(self._temporary.name)
        self.partial = self.root / "fixture.partial"
        self.final = self.root / "fixture.zip"
        self.members = {
            "fixture_alpha.txt": b"alpha",
            "fixture_beta.json": b'{"beta":true}\n',
        }
        self.hashes = {
            name: hashlib.sha256(data).hexdigest()
            for name, data in self.members.items()
        }
        self._write_zip()

    def tearDown(self) -> None:
        self._temporary.cleanup()

    def _write_zip(self) -> None:
        with zipfile.ZipFile(self.partial, "w", zipfile.ZIP_STORED) as archive:
            for name, data in self.members.items():
                archive.writestr(name, data)

    def _runner(
        self,
        *,
        verifier=lambda _: True,
        tracker: PhaseTracker | None = None,
    ) -> BlindPackagePersistenceRunner:
        return BlindPackagePersistenceRunner(
            partial_path=self.partial,
            final_path=self.final,
            expected_members=set(self.members),
            expected_member_hashes=self.hashes,
            commitment_verifier=verifier,
            cleanup_paths=[self.partial, self.final],
            cleanup_root=self.root,
            tracker=tracker,
        )

    def test_success_returns_only_bounded_facts(self) -> None:
        result = self._runner().run()
        self.assertTrue(result.success)
        self.assertEqual(result.failure_phase, FailurePhase.COMPLETE.value)
        self.assertIsNone(result.failure)

    def test_failure_contains_sanitized_evidence_only(self) -> None:
        secret = "C:/synthetic/private/path token=SENSITIVE"

        def fail(_: Path) -> bool:
            raise OSError(9, secret)

        result = self._runner(verifier=fail).run()
        self.assertFalse(result.success)
        self.assertIsNotNone(result.failure)
        serialized = repr(result)
        self.assertNotIn(secret, serialized)
        self.assertNotIn("SENSITIVE", serialized)

    def test_failure_invokes_cleanup(self) -> None:
        tracker = PhaseTracker()
        result = self._runner(verifier=lambda _: False, tracker=tracker).run()
        self.assertFalse(result.success)
        self.assertFalse(self.partial.exists())
        self.assertFalse(self.final.exists())
        self.assertEqual(tracker.phase, FailurePhase.CLEANUP)

    def test_runner_does_not_retry_publication(self) -> None:
        with mock.patch.object(
            runner_module,
            "atomic_publish_verified_zip",
            side_effect=OSError(5, "synthetic"),
        ) as publish:
            result = self._runner().run()
        self.assertFalse(result.success)
        self.assertEqual(publish.call_count, 1)

    def test_runner_module_has_no_forbidden_import_surface(self) -> None:
        source = inspect.getsource(runner_module)
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        self.assertTrue({"random", "secrets", "subprocess"}.isdisjoint(imported))
        self.assertNotIn("dreamina", source.lower())
        self.assertNotIn("provider", source.lower())

    def test_result_model_has_no_identity_disclosure_fields(self) -> None:
        field_names = {field.name for field in dataclasses.fields(RunnerResult)}
        self.assertNotIn("mapping", field_names)
        self.assertNotIn("salt", field_names)
        self.assertNotIn("source_to_alias", field_names)
        self.assertNotIn("raw_exception_text", field_names)

    def test_all_synthetic_paths_are_confined_and_cleaned(self) -> None:
        result = self._runner(verifier=lambda _: False).run()
        self.assertFalse(result.success)
        self.assertEqual(result.cleanup_requested, 2)
        self.assertFalse(self.partial.exists())
        self.assertFalse(self.final.exists())
        self.assertEqual(os.path.commonpath([self.root, self.partial]), str(self.root))


if __name__ == "__main__":
    unittest.main()
