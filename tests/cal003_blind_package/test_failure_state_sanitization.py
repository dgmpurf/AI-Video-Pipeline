from __future__ import annotations

import json
import unittest

from tools.cal003_blind_package import (
    FailurePhase,
    OperationCode,
    PhaseTracker,
    sanitize_exception,
)


class FailureStateSanitizationTests(unittest.TestCase):
    def test_initial_state_is_startup(self) -> None:
        tracker = PhaseTracker()
        self.assertEqual(tracker.phase, FailurePhase.STARTUP)
        self.assertIsNone(tracker.operation)

    def test_all_pipeline_phases_persist_in_order(self) -> None:
        tracker = PhaseTracker()
        transitions = [
            (FailurePhase.SEALED_ZIP_WRITE, OperationCode.WRITE_PARTIAL_ZIP),
            (
                FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
                OperationCode.FLUSH_PARTIAL_ZIP,
            ),
            (FailurePhase.SEALED_ZIP_INTEGRITY, OperationCode.VERIFY_PARTIAL_ZIP),
            (FailurePhase.ATOMIC_RENAME, OperationCode.ATOMIC_REPLACE),
            (
                FailurePhase.FINAL_PACKAGE_FILE_FLUSH,
                OperationCode.FLUSH_FINAL_ZIP,
            ),
            (FailurePhase.FINAL_ZIP_INTEGRITY, OperationCode.VERIFY_FINAL_ZIP),
            (FailurePhase.COMPLETE, OperationCode.VERIFY_FINAL_ZIP),
        ]
        for phase, operation in transitions:
            tracker.transition(phase, operation)
        self.assertEqual(
            [phase for phase, _ in tracker.history[1:]],
            [phase for phase, _ in transitions],
        )

    def test_cleanup_is_permitted_after_activated_failure(self) -> None:
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_ZIP_INTEGRITY,
            OperationCode.VERIFY_PARTIAL_ZIP,
        )
        tracker.transition(
            FailurePhase.CLEANUP,
            OperationCode.CLEANUP_TASK_CREATED_PATHS,
        )
        self.assertEqual(tracker.phase, FailurePhase.CLEANUP)

    def test_startup_cannot_be_reentered(self) -> None:
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_ZIP_WRITE,
            OperationCode.WRITE_PARTIAL_ZIP,
        )
        with self.assertRaises(ValueError):
            tracker.transition(
                FailurePhase.STARTUP,
                OperationCode.WRITE_PARTIAL_ZIP,
            )

    def test_complete_requires_final_verification(self) -> None:
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            tracker.transition(
                FailurePhase.COMPLETE,
                OperationCode.VERIFY_FINAL_ZIP,
            )

    def test_phase_and_operation_must_match(self) -> None:
        tracker = PhaseTracker()
        with self.assertRaises(ValueError):
            tracker.transition(
                FailurePhase.ATOMIC_RENAME,
                OperationCode.FLUSH_FINAL_ZIP,
            )

    def test_exception_is_sanitized_without_raw_text(self) -> None:
        tracker = PhaseTracker()
        tracker.transition(
            FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
            OperationCode.FLUSH_PARTIAL_ZIP,
        )
        secret = "C:/synthetic/private/path token=SENSITIVE"
        exc = OSError(9, secret)
        try:
            exc.winerror = 123
        except AttributeError:
            pass
        failure = sanitize_exception(exc, tracker)
        encoded = json.dumps(failure.as_dict(), sort_keys=True)
        self.assertEqual(failure.exception_class, "OSError")
        self.assertEqual(failure.errno, 9)
        if hasattr(exc, "winerror"):
            self.assertEqual(failure.winerror, 123)
        self.assertNotIn(secret, encoded)
        self.assertNotIn("SENSITIVE", encoded)
        self.assertNotIn("traceback", encoded.lower())
        self.assertNotIn("args", encoded.lower())

    def test_unsafe_numeric_values_are_excluded(self) -> None:
        class SyntheticFailure(Exception):
            errno = True
            winerror = 2**40

        failure = sanitize_exception(SyntheticFailure(), PhaseTracker())
        self.assertIsNone(failure.errno)
        self.assertIsNone(failure.winerror)

    def test_sanitized_model_has_exact_fields(self) -> None:
        failure = sanitize_exception(OSError(5, "hidden"), PhaseTracker())
        self.assertEqual(
            set(failure.as_dict()),
            {
                "errno",
                "exception_class",
                "failure_phase",
                "operation_code",
                "winerror",
            },
        )


if __name__ == "__main__":
    unittest.main()
