from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from .reference_roles import ReferenceRole, validate_reference_roles


@dataclass
class PromptRecord:
    prompt_id: str
    production_id: str
    shot_id: str | None
    asset_id: str | None
    prompt_type: str
    version: str
    prompt_text: str
    negative_prompt: str
    reference_ids: List[str]
    reference_roles: List[dict]
    source_shot_id: str | None
    status: str
    notes: str
    created_at: str
    updated_at: str

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "PromptRecord":
        prompt = cls(
            prompt_id=_ensure_text(raw.get("prompt_id"), "prompt_id"),
            production_id=_ensure_text(raw.get("production_id"), "production_id"),
            shot_id=raw.get("shot_id"),
            asset_id=raw.get("asset_id"),
            prompt_type=_ensure_text(raw.get("prompt_type"), "prompt_type"),
            version=_ensure_text(raw.get("version"), "version"),
            prompt_text=_ensure_text(raw.get("prompt_text"), "prompt_text"),
            negative_prompt=str(raw.get("negative_prompt", "")).strip(),
            reference_ids=_ensure_string_list(raw.get("reference_ids", []), "reference_ids"),
            reference_roles=_ensure_role_list(raw.get("reference_roles", []), "reference_roles"),
            source_shot_id=raw.get("source_shot_id"),
            status=_ensure_text(raw.get("status"), "status"),
            notes=str(raw.get("notes", "")).strip(),
            created_at=_ensure_text(raw.get("created_at"), "created_at"),
            updated_at=_ensure_text(raw.get("updated_at"), "updated_at"),
        )
        prompt.validate()
        return prompt

    def validate(self) -> None:
        if self.reference_ids and self.reference_roles:
            validate_reference_roles(self.reference_roles, self.reference_ids)

    def asdict(self) -> Dict[str, Any]:
        return {
            "prompt_id": self.prompt_id,
            "production_id": self.production_id,
            "shot_id": self.shot_id,
            "asset_id": self.asset_id,
            "prompt_type": self.prompt_type,
            "version": self.version,
            "prompt_text": self.prompt_text,
            "negative_prompt": self.negative_prompt,
            "reference_ids": list(self.reference_ids),
            "reference_roles": list(self.reference_roles),
            "source_shot_id": self.source_shot_id,
            "status": self.status,
            "notes": self.notes,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


def _ensure_text(raw: Any, field_name: str) -> str:
    text = "" if raw is None else str(raw).strip()
    if not text:
        raise ValueError(f"{field_name} is required")
    return text


def _ensure_string_list(raw: Any, field_name: str) -> List[str]:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise ValueError(f"{field_name} must be a list")
    result: List[str] = []
    for item in raw:
        text = _ensure_text(item, f"{field_name} item")
        result.append(text)
    return result


def _ensure_role_list(raw: Any, field_name: str) -> List[dict]:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise ValueError(f"{field_name} must be a list")
    prepared: List[dict] = []
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError(f"{field_name} entries must be objects")
        prepared.append(item)
    return prepared