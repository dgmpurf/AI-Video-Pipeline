"""Explicit failure phases and non-revealing exception evidence."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


class FailurePhase(str, Enum):
    STARTUP = "STARTUP"
    SEALED_ZIP_WRITE = "SEALED_ZIP_WRITE"
    SEALED_PACKAGE_FILE_FLUSH = "SEALED_PACKAGE_FILE_FLUSH"
    SEALED_ZIP_INTEGRITY = "SEALED_ZIP_INTEGRITY"
    ATOMIC_RENAME = "ATOMIC_RENAME"
    FINAL_PACKAGE_FILE_FLUSH = "FINAL_PACKAGE_FILE_FLUSH"
    FINAL_ZIP_INTEGRITY = "FINAL_ZIP_INTEGRITY"
    CLEANUP = "CLEANUP"
    COMPLETE = "COMPLETE"


class OperationCode(str, Enum):
    WRITE_PARTIAL_ZIP = "WRITE_PARTIAL_ZIP"
    FLUSH_PARTIAL_ZIP = "FLUSH_PARTIAL_ZIP"
    VERIFY_PARTIAL_ZIP = "VERIFY_PARTIAL_ZIP"
    ATOMIC_REPLACE = "ATOMIC_REPLACE"
    FLUSH_FINAL_ZIP = "FLUSH_FINAL_ZIP"
    VERIFY_FINAL_ZIP = "VERIFY_FINAL_ZIP"
    CLEANUP_TASK_CREATED_PATHS = "CLEANUP_TASK_CREATED_PATHS"


_PHASE_OPERATIONS = {
    FailurePhase.SEALED_ZIP_WRITE: OperationCode.WRITE_PARTIAL_ZIP,
    FailurePhase.SEALED_PACKAGE_FILE_FLUSH: OperationCode.FLUSH_PARTIAL_ZIP,
    FailurePhase.SEALED_ZIP_INTEGRITY: OperationCode.VERIFY_PARTIAL_ZIP,
    FailurePhase.ATOMIC_RENAME: OperationCode.ATOMIC_REPLACE,
    FailurePhase.FINAL_PACKAGE_FILE_FLUSH: OperationCode.FLUSH_FINAL_ZIP,
    FailurePhase.FINAL_ZIP_INTEGRITY: OperationCode.VERIFY_FINAL_ZIP,
    FailurePhase.CLEANUP: OperationCode.CLEANUP_TASK_CREATED_PATHS,
}


@dataclass(frozen=True)
class SanitizedFailure:
    exception_class: str
    errno: Optional[int]
    winerror: Optional[int]
    failure_phase: str
    operation_code: Optional[str]

    def as_dict(self) -> dict[str, object]:
        return {
            "errno": self.errno,
            "exception_class": self.exception_class,
            "failure_phase": self.failure_phase,
            "operation_code": self.operation_code,
            "winerror": self.winerror,
        }


class PhaseTracker:
    """Tracks explicit persistence transitions without implicit reset."""

    def __init__(self) -> None:
        self._phase = FailurePhase.STARTUP
        self._operation: Optional[OperationCode] = None
        self._history: list[Tuple[FailurePhase, Optional[OperationCode]]] = [
            (self._phase, self._operation)
        ]

    @property
    def phase(self) -> FailurePhase:
        return self._phase

    @property
    def operation(self) -> Optional[OperationCode]:
        return self._operation

    @property
    def history(self) -> Tuple[Tuple[FailurePhase, Optional[OperationCode]], ...]:
        return tuple(self._history)

    def transition(
        self,
        phase: FailurePhase,
        operation: OperationCode,
    ) -> None:
        if not isinstance(phase, FailurePhase):
            raise TypeError("phase must be a FailurePhase")
        if not isinstance(operation, OperationCode):
            raise TypeError("operation must be an OperationCode")
        if self._phase is FailurePhase.COMPLETE:
            raise ValueError("no transition is permitted after COMPLETE")
        if phase is FailurePhase.STARTUP:
            raise ValueError("STARTUP cannot be re-entered")
        if phase is FailurePhase.COMPLETE:
            if (
                self._phase is not FailurePhase.FINAL_ZIP_INTEGRITY
                or self._operation is not OperationCode.VERIFY_FINAL_ZIP
                or operation is not OperationCode.VERIFY_FINAL_ZIP
            ):
                raise ValueError("COMPLETE requires verified final ZIP state")
        else:
            expected = _PHASE_OPERATIONS.get(phase)
            if expected is not operation:
                raise ValueError("phase and operation do not match")
        self._phase = phase
        self._operation = operation
        self._history.append((phase, operation))


def _safe_integer(value: object) -> Optional[int]:
    if (
        isinstance(value, int)
        and not isinstance(value, bool)
        and -(2**31) <= value <= (2**31 - 1)
    ):
        return value
    return None


def sanitize_exception(
    exc: BaseException,
    tracker: PhaseTracker,
) -> SanitizedFailure:
    """Return only bounded numeric and explicit state evidence."""

    operation = tracker.operation.value if tracker.operation is not None else None
    return SanitizedFailure(
        exception_class=type(exc).__name__,
        errno=_safe_integer(getattr(exc, "errno", None)),
        winerror=_safe_integer(getattr(exc, "winerror", None)),
        failure_phase=tracker.phase.value,
        operation_code=operation,
    )
