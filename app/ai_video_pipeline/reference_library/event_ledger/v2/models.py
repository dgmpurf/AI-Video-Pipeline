from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class BaseV01Binding:
    base_v0_1_ledger_id: str
    base_v0_1_checkpoint_id: str
    base_v0_1_checkpoint_event_id: str
    base_v0_1_through_position: int
    base_v0_1_through_entry_hash: str
    base_v0_1_projection_hash: str
    base_v0_1_manifest_sha256: str
    base_v0_1_checkpoint_sha256: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "base_v0_1_ledger_id": self.base_v0_1_ledger_id,
            "base_v0_1_checkpoint_id": self.base_v0_1_checkpoint_id,
            "base_v0_1_checkpoint_event_id": self.base_v0_1_checkpoint_event_id,
            "base_v0_1_through_position": self.base_v0_1_through_position,
            "base_v0_1_through_entry_hash": self.base_v0_1_through_entry_hash,
            "base_v0_1_projection_hash": self.base_v0_1_projection_hash,
            "base_v0_1_manifest_sha256": self.base_v0_1_manifest_sha256,
            "base_v0_1_checkpoint_sha256": self.base_v0_1_checkpoint_sha256,
        }


@dataclass(frozen=True)
class BaseV01Snapshot:
    binding: BaseV01Binding
    base_catalog_identity: Mapping[str, Any]
    member_context: Mapping[str, Mapping[str, Any]]

    def member_context_copy(self) -> dict[str, dict[str, Any]]:
        return copy.deepcopy({key: dict(value) for key, value in self.member_context.items()})


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
