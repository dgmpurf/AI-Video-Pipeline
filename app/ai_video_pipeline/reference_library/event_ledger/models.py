from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


RL_P0_COMMIT = "1b86aae6ff08d74ce2993ef92721c9ef585854f8"


@dataclass(frozen=True)
class BaseCatalogBinding:
    package_filename: str
    package_bytes: int
    package_sha256: str
    record_count: int
    record_schema_version: str
    rl_p0_commit: str
    base_catalog_hash: str

    def __post_init__(self) -> None:
        if self.rl_p0_commit != RL_P0_COMMIT:
            raise ValueError("RL-P0 commit does not match the accepted base commit")

    def to_dict(self) -> dict[str, Any]:
        return {
            "package_filename": self.package_filename,
            "package_bytes": self.package_bytes,
            "package_sha256": self.package_sha256,
            "record_count": self.record_count,
            "record_schema_version": self.record_schema_version,
            "rl_p0_commit": self.rl_p0_commit,
            "base_catalog_hash": self.base_catalog_hash,
        }


@dataclass(frozen=True)
class StoredEvent:
    _value: Mapping[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return copy.deepcopy(dict(self._value))

    @property
    def event_id(self) -> str:
        return str(self._value["event_id"])

    @property
    def event_body_hash(self) -> str:
        return str(self._value["event_body_hash"])

    @property
    def event_type(self) -> str:
        return str(self._value["event_type"])


@dataclass(frozen=True)
class LedgerEntry:
    _value: Mapping[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return copy.deepcopy(dict(self._value))

    @property
    def position(self) -> int:
        return int(self._value["ledger_position"])

    @property
    def entry_hash(self) -> str:
        return str(self._value["entry_hash"])

    @property
    def event(self) -> StoredEvent:
        return StoredEvent(self._value["event"])


@dataclass(frozen=True)
class ProjectionResult:
    _value: Mapping[str, Any]
    projection_hash: str

    def to_dict(self) -> dict[str, Any]:
        return copy.deepcopy(dict(self._value))


@dataclass(frozen=True)
class BaseCatalogAdapter:
    package_path: Path
    binding: BaseCatalogBinding
    _record_bytes: tuple[bytes, ...]
    _validation_bytes: bytes

    @property
    def records(self) -> tuple[Mapping[str, Any], ...]:
        return tuple(json.loads(raw.decode("utf-8")) for raw in self._record_bytes)

    @property
    def validation(self) -> Mapping[str, Any]:
        return json.loads(self._validation_bytes.decode("utf-8"))

    @property
    def canonical_record_bytes(self) -> tuple[bytes, ...]:
        return self._record_bytes

    def record_map(self) -> dict[str, Mapping[str, Any]]:
        return {
            str(record["record_identity"]["pilot_clip_id"]): record
            for record in self.records
        }
