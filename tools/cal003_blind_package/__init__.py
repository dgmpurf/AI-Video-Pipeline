"""Bounded sealed-ZIP persistence helpers for CAL-003."""

from .durability import (
    atomic_publish_verified_zip,
    cleanup_task_created_paths,
    flush_file_durable,
    validate_zip_archive,
)
from .failure_state import (
    FailurePhase,
    OperationCode,
    PhaseTracker,
    SanitizedFailure,
    sanitize_exception,
)
from .runner import BlindPackagePersistenceRunner, RunnerResult

CAL003_BLIND_PACKAGE_WINDOWS_DURABILITY_V0_1 = (
    "CAL003_BLIND_PACKAGE_WINDOWS_DURABILITY_V0_1"
)

__all__ = [
    "CAL003_BLIND_PACKAGE_WINDOWS_DURABILITY_V0_1",
    "FailurePhase",
    "OperationCode",
    "PhaseTracker",
    "SanitizedFailure",
    "sanitize_exception",
    "flush_file_durable",
    "validate_zip_archive",
    "atomic_publish_verified_zip",
    "cleanup_task_created_paths",
    "BlindPackagePersistenceRunner",
    "RunnerResult",
]
