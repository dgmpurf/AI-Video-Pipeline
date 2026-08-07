from __future__ import annotations


class DuplicateWorkflowError(RuntimeError):
    """Base error for the derived RL-P3 duplicate workflow."""


class IdentityError(DuplicateWorkflowError, ValueError):
    pass


class SchemaError(DuplicateWorkflowError, ValueError):
    pass


class MappingError(DuplicateWorkflowError, ValueError):
    pass


class BuildError(DuplicateWorkflowError):
    pass


class VerificationError(DuplicateWorkflowError):
    pass


class PromotionError(DuplicateWorkflowError):
    pass


class QueryError(DuplicateWorkflowError):
    pass


class UnsafePathError(DuplicateWorkflowError, ValueError):
    pass
