from __future__ import annotations

import copy
from typing import Any, Mapping

from app.ai_video_pipeline.reference_library.event_ledger.enums import (
    CHECKPOINT_SCHEMA_VERSION as V0_1_CHECKPOINT_SCHEMA_VERSION,
    EVENT_SCHEMA_VERSION as V0_1_EVENT_SCHEMA_VERSION,
    LEDGER_SCHEMA_VERSION as V0_1_LEDGER_SCHEMA_VERSION,
    PROJECTION_SCHEMA_VERSION as V0_1_PROJECTION_SCHEMA_VERSION,
)

from .canonical import (
    canonical_json_bytes,
    require_exact_keys,
    require_nonempty_string,
    require_sha256,
    sha256_hex,
)
from .errors import BaseBridgeError
from .models import BaseV01Binding, BaseV01Snapshot, ProjectionResult


BASE_BINDING_FIELDS = frozenset(
    {
        "base_v0_1_ledger_id",
        "base_v0_1_checkpoint_id",
        "base_v0_1_checkpoint_event_id",
        "base_v0_1_through_position",
        "base_v0_1_through_entry_hash",
        "base_v0_1_projection_hash",
        "base_v0_1_manifest_sha256",
        "base_v0_1_checkpoint_sha256",
    }
)


def _mapping(value: Mapping[str, Any] | ProjectionResult) -> tuple[dict[str, Any], str]:
    if isinstance(value, ProjectionResult):
        return value.to_dict(), value.projection_hash
    if hasattr(value, "to_dict") and hasattr(value, "projection_hash"):
        return copy.deepcopy(value.to_dict()), str(value.projection_hash)
    if isinstance(value, Mapping):
        result = copy.deepcopy(dict(value))
        return result, sha256_hex(canonical_json_bytes(result))
    raise BaseBridgeError("V0.1 projection must be a validated projection mapping")


def validate_base_binding(value: Mapping[str, Any]) -> BaseV01Binding:
    try:
        require_exact_keys(value, BASE_BINDING_FIELDS, field="base_v0_1")
        for field in (
            "base_v0_1_ledger_id",
            "base_v0_1_checkpoint_id",
            "base_v0_1_checkpoint_event_id",
        ):
            require_nonempty_string(value[field], field=field)
        position = value["base_v0_1_through_position"]
        if isinstance(position, bool) or not isinstance(position, int) or position < 0:
            raise BaseBridgeError("base V0.1 through position must be nonnegative")
        for field in (
            "base_v0_1_through_entry_hash",
            "base_v0_1_projection_hash",
            "base_v0_1_manifest_sha256",
            "base_v0_1_checkpoint_sha256",
        ):
            require_sha256(value[field], field=field)
    except BaseBridgeError:
        raise
    except Exception as error:
        raise BaseBridgeError(str(error)) from error
    return BaseV01Binding(**dict(value))


def bridge_v0_1_base(
    manifest: Mapping[str, Any],
    checkpoint: Mapping[str, Any],
    projection: Mapping[str, Any] | ProjectionResult,
    *,
    checkpoint_event_id: str,
    manifest_bytes: bytes | None = None,
    checkpoint_bytes: bytes | None = None,
    member_context: Mapping[str, Mapping[str, Any]] | None = None,
) -> BaseV01Snapshot:
    """Validate and bind an immutable V0.1 checkpoint/projection without rewriting it."""

    manifest_value = copy.deepcopy(dict(manifest))
    checkpoint_value = copy.deepcopy(dict(checkpoint))
    projection_value, projection_hash = _mapping(projection)
    try:
        if manifest_value.get("ledger_schema_version") != V0_1_LEDGER_SCHEMA_VERSION:
            raise BaseBridgeError("base ledger is not RL_LEDGER_V0_1")
        if manifest_value.get("event_schema_version") != V0_1_EVENT_SCHEMA_VERSION:
            raise BaseBridgeError("base event schema is not RL_EVENT_V0_1")
        if manifest_value.get("projection_schema_version") != V0_1_PROJECTION_SCHEMA_VERSION:
            raise BaseBridgeError("base projection schema is not RL_PROJECTION_V0_1")
        if checkpoint_value.get("checkpoint_schema_version") != V0_1_CHECKPOINT_SCHEMA_VERSION:
            raise BaseBridgeError("base checkpoint is not RL_CHECKPOINT_V0_1")
        if projection_value.get("projection_schema_version") != V0_1_PROJECTION_SCHEMA_VERSION:
            raise BaseBridgeError("base projection value has the wrong schema")
        ledger_id = require_nonempty_string(
            manifest_value.get("ledger_id"), field="base ledger_id"
        )
        if projection_value.get("ledger_id") != ledger_id:
            raise BaseBridgeError("base projection ledger ID differs from manifest")
        checkpoint_id = require_nonempty_string(
            checkpoint_value.get("checkpoint_id"), field="base checkpoint_id"
        )
        require_nonempty_string(checkpoint_event_id, field="checkpoint_event_id")
        if checkpoint_value.get("projection_hash") != projection_hash:
            raise BaseBridgeError("base checkpoint projection hash differs")
        if int(checkpoint_value.get("prefix_position", -1)) != int(
            projection_value.get("through_position", -2)
        ):
            raise BaseBridgeError("base checkpoint position differs from projection")
        if checkpoint_value.get("prefix_entry_hash") != projection_value.get(
            "through_entry_hash"
        ):
            raise BaseBridgeError("base checkpoint tail differs from projection")
        base_catalog = checkpoint_value.get("base_catalog_identity")
        if not isinstance(base_catalog, dict):
            raise BaseBridgeError("base checkpoint catalog identity is absent")
        manifest_raw = (
            manifest_bytes
            if manifest_bytes is not None
            else canonical_json_bytes(manifest_value, terminal_lf=True)
        )
        checkpoint_raw = (
            checkpoint_bytes
            if checkpoint_bytes is not None
            else canonical_json_bytes(checkpoint_value, terminal_lf=True)
        )
        binding = BaseV01Binding(
            base_v0_1_ledger_id=ledger_id,
            base_v0_1_checkpoint_id=checkpoint_id,
            base_v0_1_checkpoint_event_id=checkpoint_event_id,
            base_v0_1_through_position=int(checkpoint_value["prefix_position"]),
            base_v0_1_through_entry_hash=str(checkpoint_value["prefix_entry_hash"]),
            base_v0_1_projection_hash=projection_hash,
            base_v0_1_manifest_sha256=sha256_hex(bytes(manifest_raw)),
            base_v0_1_checkpoint_sha256=sha256_hex(bytes(checkpoint_raw)),
        )
        validate_base_binding(binding.to_dict())
        contexts = copy.deepcopy(dict(member_context or {}))
        if any(not isinstance(value, Mapping) for value in contexts.values()):
            raise BaseBridgeError("member context values must be objects")
        return BaseV01Snapshot(binding, copy.deepcopy(base_catalog), contexts)
    except BaseBridgeError:
        raise
    except Exception as error:
        raise BaseBridgeError(str(error)) from error
