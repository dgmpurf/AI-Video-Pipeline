from __future__ import annotations


class PersistentIndexError(RuntimeError):
    """Base error for the derived RL-P2 read model."""


class IdentityError(PersistentIndexError):
    pass


class SchemaError(PersistentIndexError):
    pass


class MappingError(PersistentIndexError):
    pass


class BuildError(PersistentIndexError):
    pass


class VerificationError(PersistentIndexError):
    pass


class PromotionError(PersistentIndexError):
    pass


class QueryError(PersistentIndexError):
    pass


class UnsafePathError(PersistentIndexError):
    pass
