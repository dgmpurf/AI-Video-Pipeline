from __future__ import annotations


class EventLedgerV2Error(RuntimeError):
    code = "EVENT_LEDGER_V2_ERROR"


class CanonicalizationError(EventLedgerV2Error, ValueError):
    code = "CANONICALIZATION_ERROR"


class SchemaValidationError(EventLedgerV2Error, ValueError):
    code = "SCHEMA_VALIDATION_ERROR"


class AuthorityMismatchError(SchemaValidationError):
    code = "AUTHORITY_CLASS_MISMATCH"


class BaseBridgeError(EventLedgerV2Error, ValueError):
    code = "V0_1_BASE_BRIDGE_ERROR"


class ManifestValidationError(EventLedgerV2Error, ValueError):
    code = "MANIFEST_VALIDATION_ERROR"


class LedgerValidationError(EventLedgerV2Error, ValueError):
    code = "LEDGER_VALIDATION_ERROR"


class DuplicateEventError(EventLedgerV2Error):
    code = "DUPLICATE_EVENT_ID"


class EventCollisionError(EventLedgerV2Error):
    code = "EVENT_ID_COLLISION_OR_TAMPER"


class ProjectionError(EventLedgerV2Error, ValueError):
    code = "PROJECTION_ERROR"


class PreconditionError(ProjectionError):
    code = "PROJECTION_PRECONDITION_FAILED"


class CheckpointError(ProjectionError):
    code = "CHECKPOINT_VALIDATION_FAILED"
