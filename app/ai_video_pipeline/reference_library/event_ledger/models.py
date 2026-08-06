from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


@dataclass(frozen=True)
class BaseCatalogBinding:
    package_filename: str
    package_bytes: int
    package_sha256: str
    record_count: int
    record_schema_version: str
    base_catalog_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "package_filename": self.package_filename,
            "package_bytes": self.package_bytes,
            "package_sha256": self.package_sha256,
            "record_count": self.record_count,
            "record_schema_version": self.record_schema_version,
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
    records: tuple[Mapping[str, Any], ...]
    validation: Mapping[str, Any]

    def record_map(self) -> dict[str, Mapping[str, Any]]:
        return {
            str(record["record_identity"]["pilot_clip_id"]): copy.deepcopy(record)
            for record in self.records
        }
