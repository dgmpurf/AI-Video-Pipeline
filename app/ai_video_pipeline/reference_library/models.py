from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Mapping


UNKNOWN = "UNKNOWN"


def stable_json_text(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def json_clone(value: Any) -> Any:
    return json.loads(stable_json_text(value))


@dataclass(frozen=True)
class ReferenceRecord:
    """Immutable JSON-backed view of one normalized candidate record."""

    _canonical_json: str

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "ReferenceRecord":
        if not isinstance(value, Mapping):
            raise TypeError("reference record must be a mapping")
        return cls(stable_json_text(dict(value)))

    @property
    def canonical_json(self) -> str:
        return self._canonical_json

    def to_dict(self) -> dict[str, Any]:
        return json.loads(self._canonical_json)

    @property
    def pilot_clip_id(self) -> str:
        return self.to_dict()["record_identity"]["pilot_clip_id"]

    @property
    def record_id(self) -> str:
        return self.to_dict()["record_identity"]["record_id"]

    @property
    def content_family_primary(self) -> str:
        return self.to_dict()["content"]["content_family"]["primary"]

    @property
    def content_scope(self) -> str:
        return self.to_dict()["content"]["content_scope"]

    @property
    def plain_language_description(self) -> str:
        return self.to_dict()["content"]["plain_language_description"]

    @property
    def reference_duties(self) -> tuple[str, ...]:
        values = self.to_dict()["reference_profile"]["reference_duties"]
        return tuple(values)

    @property
    def reference_duty_extensions(self) -> tuple[str, ...]:
        values = self.to_dict()["reference_profile"][
            "reference_duty_extensions"
        ]
        return tuple(values)

    @property
    def reference_taxonomy_status(self) -> str:
        return self.to_dict()["reference_profile"]["reference_taxonomy_status"]

    @property
    def artifacts(self) -> tuple[dict[str, Any], ...]:
        return tuple(self.to_dict()["artifacts"])

    @property
    def rights(self) -> dict[str, Any]:
        return self.to_dict()["rights"]

    @property
    def current_proxy_bytes(self) -> int:
        return int(self.to_dict()["artifact_storage"]["current_proxy_bytes"])

    @property
    def current_segment_bytes(self) -> int:
        return int(self.to_dict()["artifact_storage"]["current_segment_bytes"])

    @property
    def current_total_derived_media_bytes(self) -> int:
        return int(
            self.to_dict()["artifact_storage"][
                "current_total_derived_media_bytes"
            ]
        )

    @property
    def technical_validation_statuses(self) -> tuple[str, ...]:
        return tuple(
            artifact["technical_validation_status"]
            for artifact in self.to_dict()["artifacts"]
        )

    @property
    def artifact_availabilities(self) -> tuple[str, ...]:
        return tuple(
            artifact["artifact_availability"]
            for artifact in self.to_dict()["artifacts"]
        )

    @property
    def artifact_lifecycles(self) -> tuple[str, ...]:
        return tuple(
            artifact["artifact_lifecycle"]
            for artifact in self.to_dict()["artifacts"]
        )
