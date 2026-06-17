from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ROLE_TYPES = {
    "character_subject",
    "character_face",
    "character_body",
    "scene_environment",
    "previous_keyframe",
    "prop",
    "style_reference",
}


@dataclass(frozen=True)
class ReferenceRole:
    order: int
    logical_id: str
    role_type: str
    role_description: str
    lock_strength: str
    allowed_drift: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ReferenceRole":
        return cls(
            order=int(raw.get("order", 0)),
            logical_id=_ensure_text(raw.get("logical_id"), "logical_id"),
            role_type=str(raw.get("role_type", "")).strip(),
            role_description=str(raw.get("role_description", "")).strip(),
            lock_strength=str(raw.get("lock_strength", "")).strip(),
            allowed_drift=str(raw.get("allowed_drift", "")).strip(),
        )

    def asdict(self) -> dict[str, Any]:
        return {
            "order": self.order,
            "logical_id": self.logical_id,
            "role_type": self.role_type,
            "role_description": self.role_description,
            "lock_strength": self.lock_strength,
            "allowed_drift": self.allowed_drift,
        }


def validate_reference_roles(
    reference_roles: list[dict] | list[ReferenceRole],
    reference_ids: list[str],
    *,
    allow_duplicate_logical_id: bool = False,
) -> None:
    if not reference_roles and not reference_ids:
        return

    parsed = [_to_reference_role(item) for item in reference_roles]
    validate_reference_roles_structure(parsed)
    ordered = sorted(parsed, key=lambda item: item.order)

    if [role.order for role in ordered] != list(range(1, len(ordered) + 1)):
        raise ValueError("ReferenceRole order must start at 1 and be sequential")

    if not allow_duplicate_logical_id:
        logical_ids = [role.logical_id for role in ordered]
        if len(logical_ids) != len(set(logical_ids)):
            raise ValueError("Duplicate logical_id is not allowed")

    if len(ordered) != len(reference_ids):
        raise ValueError("reference_ids count must match reference_roles count")

    ordered_ids = [role.logical_id for role in ordered]
    if ordered_ids != list(reference_ids):
        raise ValueError("reference_ids must match reference_roles order")


def validate_reference_roles_structure(roles: list[ReferenceRole]) -> None:
    seen_orders = set()
    for role in roles:
        if role.order < 1:
            raise ValueError("ReferenceRole order must start at 1")
        if role.order in seen_orders:
            raise ValueError("Duplicate ReferenceRole order")
        seen_orders.add(role.order)
        if role.role_type and role.role_type not in ROLE_TYPES:
            raise ValueError(f"Unsupported role_type: {role.role_type}")
        if not role.role_description:
            raise ValueError("role_description is required")


def _to_reference_role(raw: dict | ReferenceRole) -> ReferenceRole:
    if isinstance(raw, ReferenceRole):
        return raw
    if not isinstance(raw, dict):
        raise ValueError("reference_role item must be an object")
    return ReferenceRole.from_dict(raw)


def _ensure_text(raw: Any, field_name: str) -> str:
    text = "" if raw is None else str(raw).strip()
    if not text:
        raise ValueError(f"{field_name} is required")
    return text