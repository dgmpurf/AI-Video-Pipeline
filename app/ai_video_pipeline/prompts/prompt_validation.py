from __future__ import annotations

from dataclasses import dataclass

from ..assets.registry import AssetRegistry
from ..core.models import AssetRecord, AssetStatus, ShotRecord
from .prompt_record import PromptRecord
from .reference_roles import ReferenceRole, _to_reference_role, validate_reference_roles


KNOWN_PROMPT_TYPES = {"asset_image", "keyframe_image", "video"}


class PromptValidationError(ValueError):
    pass


@dataclass(frozen=True)
class PromptValidationOptions:
    allow_archived_assets: bool = False
    mock_tag: str = "mock"
    locked_strengths: tuple[str, ...] = ("high",)


def validate_prompt_record(
    prompt_record: PromptRecord,
    shot_record: ShotRecord | None = None,
    asset_registry: AssetRegistry | None = None,
    *,
    options: PromptValidationOptions | None = None,
) -> None:
    options = options or PromptValidationOptions()
    _ensure_text(prompt_record.prompt_id, "prompt_id")
    _ensure_text(prompt_record.prompt_text, "prompt_text")

    if prompt_record.prompt_type not in KNOWN_PROMPT_TYPES:
        raise PromptValidationError(f"unknown prompt_type: {prompt_record.prompt_type}")

    if prompt_record.reference_roles:
        validate_reference_roles(prompt_record.reference_roles, prompt_record.reference_ids)

    if asset_registry is not None:
        _validate_references_against_assets(prompt_record, asset_registry, options)
        if shot_record is not None:
            _validate_required_assets(shot_record, asset_registry, options)


def _validate_references_against_assets(
    prompt_record: PromptRecord,
    asset_registry: AssetRegistry,
    options: PromptValidationOptions,
) -> None:
    roles_by_id = {
        role.logical_id: role
        for role in [_to_reference_role(item) for item in prompt_record.reference_roles]
    }
    for reference_id in prompt_record.reference_ids:
        assets = _find_assets(asset_registry, reference_id)
        if not assets:
            continue
        for asset in assets:
            _validate_asset_status(reference_id, asset, options)
            role = roles_by_id.get(reference_id)
            if role is not None:
                _validate_mock_lock(reference_id, asset, role, options)


def _validate_required_assets(
    shot_record: ShotRecord,
    asset_registry: AssetRegistry,
    options: PromptValidationOptions,
) -> None:
    for reference in shot_record.required_asset_ids:
        assets = _find_assets(asset_registry, reference)
        if not assets:
            raise PromptValidationError(f"missing required asset: {reference}")
        for asset in assets:
            _validate_asset_status(reference, asset, options)


def _find_assets(asset_registry: AssetRegistry, reference: str) -> list[AssetRecord]:
    logical_id, candidate_id = _split_asset_reference(reference)
    return asset_registry.get_by_logical_id(logical_id, candidate_id)


def _split_asset_reference(reference: str) -> tuple[str, str | None]:
    if ":" not in reference:
        return reference.strip(), None
    logical_id, candidate_id = reference.split(":", 1)
    return logical_id.strip(), candidate_id.strip() or None


def _validate_asset_status(reference: str, asset: AssetRecord, options: PromptValidationOptions) -> None:
    if asset.status == AssetStatus.rejected:
        raise PromptValidationError(f"rejected asset cannot be used as reference: {reference}")
    if asset.status == AssetStatus.archived and not options.allow_archived_assets:
        raise PromptValidationError(f"archived asset cannot be used as reference: {reference}")


def _validate_mock_lock(
    reference: str,
    asset: AssetRecord,
    role: ReferenceRole,
    options: PromptValidationOptions,
) -> None:
    if role.lock_strength.lower() not in options.locked_strengths:
        return
    if options.mock_tag in {tag.lower() for tag in asset.tags}:
        raise PromptValidationError(f"mock asset cannot be used as locked reference: {reference}")


def _ensure_text(value: str | None, field_name: str) -> str:
    text = "" if value is None else str(value).strip()
    if not text:
        raise PromptValidationError(f"{field_name} is required")
    return text
