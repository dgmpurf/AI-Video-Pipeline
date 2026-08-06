from __future__ import annotations


class EventLedgerError(RuntimeError):
    code = "EVENT_LEDGER_ERROR"

    def __init__(self, message: str) -> None:
        super().__init__(message)


class CanonicalizationError(EventLedgerError, ValueError):
    code = "CANONICALIZATION_ERROR"


class SchemaValidationError(EventLedgerError, ValueError):
    code = "SCHEMA_VALIDATION_ERROR"


class AuthorityMismatchError(SchemaValidationError):
    code = "AUTHORITY_CLASS_MISMATCH"


class ManifestValidationError(EventLedgerError, ValueError):
    code = "MANIFEST_VALIDATION_ERROR"


class LedgerValidationError(EventLedgerError, ValueError):
    code = "LEDGER_VALIDATION_ERROR"


class LedgerLockedError(EventLedgerError, FileExistsError):
    code = "LEDGER_LOCK_ALREADY_EXISTS"


class DuplicateEventError(EventLedgerError):
    code = "DUPLICATE_EVENT_ID"


class EventCollisionError(EventLedgerError):
    code = "EVENT_ID_COLLISION_OR_TAMPER"


class ProjectionError(EventLedgerError, ValueError):
    code = "PROJECTION_ERROR"


class PreconditionError(ProjectionError):
    code = "PROJECTION_PRECONDITION_FAILED"


class CheckpointError(ProjectionError):
    code = "CHECKPOINT_VALIDATION_FAILED"


class UnsafeLedgerPathError(EventLedgerError, ValueError):
    code = "UNSAFE_LEDGER_PATH"
