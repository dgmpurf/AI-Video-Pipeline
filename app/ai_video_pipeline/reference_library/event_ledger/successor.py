from __future__ import annotations

import copy
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

from .canonical import (
    canonical_sha256,
    require_exact_keys,
    require_nonempty_string,
    require_rfc3339_utc,
    require_sha256,
)
from .enums import AuthorityClass, EVENT_SCHEMA_VERSION, PROJECTION_SCHEMA_VERSION
from .models import BaseCatalogAdapter, LedgerEntry, ProjectionResult
from .projection import replay_entries
from .typed_targets import (
    TARGET_KIND_INVENTORY_ASSET,
    TARGET_KIND_PILOT_CLIP,
    inventory_registry_ids,
    validate_inventory_identity_registry,
    validate_target_identity,
)


SUCCESSOR_SEGMENT_SCHEMA_VERSION = "RL_LEDGER_SUCCESSOR_SEGMENT_V0_2"
SUCCESSOR_EVENT_SCHEMA_VERSION = "RL_EVENT_V0_2"
SUCCESSOR_PROJECTION_SCHEMA_VERSION = "RL_PROJECTION_V0_2"
SUCCESSOR_EVENT_REGISTRY_VERSION = "RL_EVENT_REGISTRY_V0_2"

REVIEW_OBSERVATION_ADDED = "REVIEW_OBSERVATION_ADDED"
REVIEW_OBSERVATION_CORRECTED = "REVIEW_OBSERVATION_CORRECTED"
SUCCESSOR_EVENT_TYPES = frozenset(
    {REVIEW_OBSERVATION_ADDED, REVIEW_OBSERVATION_CORRECTED}
)

ZERO_HASH = "0" * 64

PARENT_BINDING_FIELDS = frozenset(
    {
        "parent_ledger_id",
        "parent_manifest_sha256",
        "parent_tail_position",
        "parent_tail_entry_hash",
        "parent_projection_hash",
        "parent_checkpoint_id",
        "parent_event_schema_version",
        "parent_projection_schema_version",
    }
)
MANIFEST_FIELDS = frozenset(
    {
        "segment_id",
        "segment_schema_version",
        "event_schema_version",
        "projection_schema_version",
        "event_registry_version",
        "parent_binding",
        "inventory_identity_registry",
        "created_by",
        "created_at",
    }
)
EVENT_DRAFT_FIELDS = frozenset(
    {
        "event_type",
        "event_schema_version",
        "target_identity",
        "actor",
        "authority_class",
        "occurred_at",
        "recorded_at",
        "source_trace_ids",
        "precondition_projection_hash",
        "supersedes_event_ids",
        "payload",
    }
)
ACTOR_FIELDS = frozenset({"actor_id", "actor_type", "model_name", "model_version"})
ACTOR_TYPES = frozenset({"HUMAN", "CHATGPT", "CODEX", "SYSTEM", "EXTERNAL_OPERATOR"})
STORED_EVENT_FIELDS = EVENT_DRAFT_FIELDS | {"event_id", "event_body_hash"}
ENTRY_FIELDS = frozenset(
    {
        "segment_schema_version",
        "segment_id",
        "ledger_position",
        "previous_entry_hash",
        "event",
        "entry_hash",
    }
)


class SuccessorValidationError(ValueError):
    pass


@dataclass(frozen=True)
class SuccessorEntry:
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
    def event(self) -> Mapping[str, Any]:
        return copy.deepcopy(dict(self._value["event"]))


@dataclass(frozen=True)
class SuccessorProjection:
    _value: Mapping[str, Any]
    projection_hash: str

    def to_dict(self) -> dict[str, Any]:
        return copy.deepcopy(dict(self._value))


@dataclass(frozen=True)
class MixedReplayResult:
    parent_projection: ProjectionResult
    successor_projection: SuccessorProjection


def _sorted_unique_strings(value: Any, *, field: str) -> list[str]:
    if not isinstance(value, list):
        raise SuccessorValidationError(f"{field} must be a list")
    if any(not isinstance(item, str) or not item for item in value):
        raise SuccessorValidationError(f"{field} must contain nonempty strings")
    if value != sorted(value) or len(value) != len(set(value)):
        raise SuccessorValidationError(f"{field} must be sorted and unique")
    return list(value)


def _latest_checkpoint_id(projection: ProjectionResult) -> str | None:
    checkpoints = projection.to_dict().get("checkpoints", {})
    if not checkpoints:
        return None
    return max(
        checkpoints,
        key=lambda key: int(checkpoints[key]["ledger_position"]),
    )


def build_parent_binding(
    parent_manifest: Mapping[str, Any],
    parent_entries: Iterable[LedgerEntry],
    parent_projection: ProjectionResult,
) -> dict[str, Any]:
    entries = tuple(parent_entries)
    tail_hash = entries[-1].entry_hash if entries else ZERO_HASH
    return validate_parent_binding(
        {
            "parent_ledger_id": parent_manifest["ledger_id"],
            "parent_manifest_sha256": canonical_sha256(dict(parent_manifest)),
            "parent_tail_position": len(entries),
            "parent_tail_entry_hash": tail_hash,
            "parent_projection_hash": parent_projection.projection_hash,
            "parent_checkpoint_id": _latest_checkpoint_id(parent_projection),
            "parent_event_schema_version": parent_manifest["event_schema_version"],
            "parent_projection_schema_version": parent_manifest[
                "projection_schema_version"
            ],
        }
    )


def validate_parent_binding(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SuccessorValidationError("parent binding must be an object")
    try:
        require_exact_keys(value, PARENT_BINDING_FIELDS, field="parent binding")
        require_nonempty_string(value["parent_ledger_id"], field="parent_ledger_id")
        for field in (
            "parent_manifest_sha256",
            "parent_tail_entry_hash",
            "parent_projection_hash",
        ):
            require_sha256(value[field], field=field)
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    position = value["parent_tail_position"]
    if not isinstance(position, int) or isinstance(position, bool) or position < 0:
        raise SuccessorValidationError("parent_tail_position must be nonnegative")
    checkpoint = value["parent_checkpoint_id"]
    if checkpoint is not None and (not isinstance(checkpoint, str) or not checkpoint):
        raise SuccessorValidationError("parent_checkpoint_id must be string or null")
    if value["parent_event_schema_version"] != EVENT_SCHEMA_VERSION:
        raise SuccessorValidationError("parent event schema version differs")
    if value["parent_projection_schema_version"] != PROJECTION_SCHEMA_VERSION:
        raise SuccessorValidationError("parent projection schema version differs")
    return copy.deepcopy(value)


def _segment_id(body: Mapping[str, Any]) -> str:
    return "RL-SEGMENT-" + canonical_sha256(dict(body))[:24].upper()


def build_successor_manifest(
    parent_binding: Mapping[str, Any],
    inventory_identity_registry: Mapping[str, Any],
    *,
    created_by: str,
    created_at: str,
) -> dict[str, Any]:
    try:
        require_nonempty_string(created_by, field="created_by")
        require_rfc3339_utc(created_at, field="created_at")
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    body = {
        "segment_schema_version": SUCCESSOR_SEGMENT_SCHEMA_VERSION,
        "event_schema_version": SUCCESSOR_EVENT_SCHEMA_VERSION,
        "projection_schema_version": SUCCESSOR_PROJECTION_SCHEMA_VERSION,
        "event_registry_version": SUCCESSOR_EVENT_REGISTRY_VERSION,
        "parent_binding": validate_parent_binding(dict(parent_binding)),
        "inventory_identity_registry": validate_inventory_identity_registry(
            dict(inventory_identity_registry)
        ),
        "created_by": created_by,
        "created_at": created_at,
    }
    return validate_successor_manifest({"segment_id": _segment_id(body), **body})


def validate_successor_manifest(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SuccessorValidationError("successor manifest must be an object")
    try:
        require_exact_keys(value, MANIFEST_FIELDS, field="successor manifest")
        require_nonempty_string(value["created_by"], field="created_by")
        require_rfc3339_utc(value["created_at"], field="created_at")
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    expected_versions = {
        "segment_schema_version": SUCCESSOR_SEGMENT_SCHEMA_VERSION,
        "event_schema_version": SUCCESSOR_EVENT_SCHEMA_VERSION,
        "projection_schema_version": SUCCESSOR_PROJECTION_SCHEMA_VERSION,
        "event_registry_version": SUCCESSOR_EVENT_REGISTRY_VERSION,
    }
    if any(value[field] != expected for field, expected in expected_versions.items()):
        raise SuccessorValidationError("successor schema version differs")
    parent = validate_parent_binding(value["parent_binding"])
    registry = validate_inventory_identity_registry(value["inventory_identity_registry"])
    body = {key: child for key, child in value.items() if key != "segment_id"}
    if value["segment_id"] != _segment_id(body):
        raise SuccessorValidationError("successor segment ID differs")
    return {**copy.deepcopy(value), "parent_binding": parent, "inventory_identity_registry": registry}


def _validate_actor(actor: Any) -> None:
    if not isinstance(actor, dict):
        raise SuccessorValidationError("actor must be an object")
    try:
        require_exact_keys(actor, ACTOR_FIELDS, field="actor")
        require_nonempty_string(actor["actor_id"], field="actor.actor_id")
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    if actor["actor_type"] not in ACTOR_TYPES:
        raise SuccessorValidationError("actor type is unsupported")
    for field in ("model_name", "model_version"):
        if actor[field] is not None and not isinstance(actor[field], str):
            raise SuccessorValidationError(f"actor.{field} must be string or null")


def validate_successor_event_draft(
    value: Any,
    *,
    manifest: Mapping[str, Any],
    known_pilot_clip_ids: Iterable[str] = (),
) -> dict[str, Any]:
    manifest_value = validate_successor_manifest(dict(manifest))
    if not isinstance(value, dict):
        raise SuccessorValidationError("successor event draft must be an object")
    try:
        require_exact_keys(value, EVENT_DRAFT_FIELDS, field="successor event draft")
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    if value["event_schema_version"] != SUCCESSOR_EVENT_SCHEMA_VERSION:
        raise SuccessorValidationError("successor event schema version differs")
    if value["event_type"] not in SUCCESSOR_EVENT_TYPES:
        raise SuccessorValidationError("unsupported successor event type")
    if value["authority_class"] != AuthorityClass.OBSERVATION_ONLY.value:
        raise SuccessorValidationError("review observation must remain observation-only")
    validate_target_identity(
        value["target_identity"],
        inventory_registry=manifest_value["inventory_identity_registry"],
        known_pilot_clip_ids=known_pilot_clip_ids,
    )
    _validate_actor(value["actor"])
    try:
        require_rfc3339_utc(value["occurred_at"], field="occurred_at")
        require_rfc3339_utc(value["recorded_at"], field="recorded_at")
        require_sha256(
            value["precondition_projection_hash"],
            field="precondition_projection_hash",
        )
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    _sorted_unique_strings(value["source_trace_ids"], field="source_trace_ids")
    supersedes = _sorted_unique_strings(
        value["supersedes_event_ids"], field="supersedes_event_ids"
    )
    if value["event_type"] == REVIEW_OBSERVATION_ADDED and supersedes:
        raise SuccessorValidationError("added observation may not supersede an event")
    if value["event_type"] == REVIEW_OBSERVATION_CORRECTED and len(supersedes) != 1:
        raise SuccessorValidationError("corrected observation must supersede exactly one event")
    payload = value["payload"]
    if not isinstance(payload, dict):
        raise SuccessorValidationError("payload must be an object")
    canonical_sha256(payload)
    for field in ("observation_type", "statement"):
        try:
            require_nonempty_string(payload.get(field), field=f"payload.{field}")
        except Exception as error:
            raise SuccessorValidationError(str(error)) from error
    return copy.deepcopy(value)


def finalize_successor_event(
    event_draft: Mapping[str, Any],
    *,
    manifest: Mapping[str, Any],
    known_pilot_clip_ids: Iterable[str] = (),
) -> dict[str, Any]:
    body = validate_successor_event_draft(
        dict(event_draft),
        manifest=manifest,
        known_pilot_clip_ids=known_pilot_clip_ids,
    )
    body_hash = canonical_sha256(body)
    return {**body, "event_id": "RL-EVT-" + body_hash[:24].upper(), "event_body_hash": body_hash}


def validate_stored_successor_event(
    value: Any,
    *,
    manifest: Mapping[str, Any],
    known_pilot_clip_ids: Iterable[str] = (),
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SuccessorValidationError("stored successor event must be an object")
    try:
        require_exact_keys(value, STORED_EVENT_FIELDS, field="stored successor event")
    except Exception as error:
        raise SuccessorValidationError(str(error)) from error
    draft = {key: child for key, child in value.items() if key not in {"event_id", "event_body_hash"}}
    expected = finalize_successor_event(
        draft,
        manifest=manifest,
        known_pilot_clip_ids=known_pilot_clip_ids,
    )
    if value != expected:
        raise SuccessorValidationError("stored successor event identity differs")
    return copy.deepcopy(value)


def build_successor_entry(
    manifest: Mapping[str, Any],
    event: Mapping[str, Any],
    *,
    position: int,
    previous_entry_hash: str,
) -> SuccessorEntry:
    manifest_value = validate_successor_manifest(dict(manifest))
    require_sha256(previous_entry_hash, field="previous_entry_hash")
    body = {
        "segment_schema_version": SUCCESSOR_SEGMENT_SCHEMA_VERSION,
        "segment_id": manifest_value["segment_id"],
        "ledger_position": position,
        "previous_entry_hash": previous_entry_hash,
        "event": copy.deepcopy(dict(event)),
    }
    return SuccessorEntry({**body, "entry_hash": canonical_sha256(body)})


def _initial_projection(
    manifest: Mapping[str, Any],
    known_pilot_clip_ids: Iterable[str],
) -> SuccessorProjection:
    manifest_value = validate_successor_manifest(dict(manifest))
    pilots = sorted(set(known_pilot_clip_ids))
    for pilot in pilots:
        validate_target_identity(
            {
                "target_schema_version": "RL_TYPED_TARGET_IDENTITY_V0_2",
                "target_kind": TARGET_KIND_PILOT_CLIP,
                "target_id": pilot,
            },
            known_pilot_clip_ids=pilots,
        )
    inventory_ids = sorted(inventory_registry_ids(manifest_value["inventory_identity_registry"]))
    state = {
        "projection_schema_version": SUCCESSOR_PROJECTION_SCHEMA_VERSION,
        "segment_id": manifest_value["segment_id"],
        "parent_binding": copy.deepcopy(manifest_value["parent_binding"]),
        "inventory_registry_hash": manifest_value["inventory_identity_registry"][
            "canonical_registry_hash"
        ],
        "through_position": manifest_value["parent_binding"]["parent_tail_position"],
        "through_entry_hash": manifest_value["parent_binding"]["parent_tail_entry_hash"],
        "event_count": 0,
        "target_records": {
            TARGET_KIND_PILOT_CLIP: {
                pilot: {"review_observations": []} for pilot in pilots
            },
            TARGET_KIND_INVENTORY_ASSET: {
                identifier: {"review_observations": []} for identifier in inventory_ids
            },
        },
        "event_index": {},
    }
    # The empty successor segment is the exact governed parent projection.
    # Only after the first accepted successor event does the V0.2 state acquire
    # its own projection hash.
    return SuccessorProjection(
        state, manifest_value["parent_binding"]["parent_projection_hash"]
    )


def replay_successor_entries(
    manifest: Mapping[str, Any],
    entries: Iterable[SuccessorEntry],
    *,
    known_pilot_clip_ids: Iterable[str] = (),
) -> SuccessorProjection:
    manifest_value = validate_successor_manifest(dict(manifest))
    pilots = tuple(sorted(set(known_pilot_clip_ids)))
    projection = _initial_projection(manifest_value, pilots)
    state = projection.to_dict()
    current_projection_hash = projection.projection_hash
    expected_position = int(state["through_position"]) + 1
    previous_hash = str(state["through_entry_hash"])
    for entry in entries:
        value = entry.to_dict() if isinstance(entry, SuccessorEntry) else copy.deepcopy(dict(entry))
        try:
            require_exact_keys(value, ENTRY_FIELDS, field="successor entry")
        except Exception as error:
            raise SuccessorValidationError(str(error)) from error
        if value["segment_schema_version"] != SUCCESSOR_SEGMENT_SCHEMA_VERSION:
            raise SuccessorValidationError("successor entry schema differs")
        if value["segment_id"] != manifest_value["segment_id"]:
            raise SuccessorValidationError("successor entry segment differs")
        if value["ledger_position"] != expected_position:
            raise SuccessorValidationError("successor ledger position is not consecutive")
        if value["previous_entry_hash"] != previous_hash:
            raise SuccessorValidationError("successor hash chain is broken")
        event = validate_stored_successor_event(
            value["event"], manifest=manifest_value, known_pilot_clip_ids=pilots
        )
        entry_body = {key: child for key, child in value.items() if key != "entry_hash"}
        if value["entry_hash"] != canonical_sha256(entry_body):
            raise SuccessorValidationError("successor entry hash differs")
        if event["precondition_projection_hash"] != current_projection_hash:
            raise SuccessorValidationError("successor projection precondition differs")
        if event["event_id"] in state["event_index"]:
            raise SuccessorValidationError("duplicate successor event ID")
        target = event["target_identity"]
        kind = target["target_kind"]
        target_id = target["target_id"]
        records = state["target_records"][kind]
        if target_id not in records:
            raise SuccessorValidationError("successor event targets an unbound identity")
        observation = {
            "event_id": event["event_id"],
            "ledger_position": value["ledger_position"],
            "target_identity": copy.deepcopy(target),
            "payload": copy.deepcopy(event["payload"]),
            "source_trace_ids": copy.deepcopy(event["source_trace_ids"]),
            "active": True,
            "superseded_by": None,
        }
        if event["event_type"] == REVIEW_OBSERVATION_CORRECTED:
            prior_id = event["supersedes_event_ids"][0]
            prior = state["event_index"].get(prior_id)
            if prior is None or not prior["active"]:
                raise SuccessorValidationError("corrected observation prior is absent or inactive")
            if prior["target_identity"] != target:
                raise SuccessorValidationError("cross-target or cross-kind supersession is forbidden")
            prior["active"] = False
            prior["superseded_by"] = event["event_id"]
            for recorded in records[target_id]["review_observations"]:
                if recorded["event_id"] == prior_id:
                    recorded["active"] = False
                    recorded["superseded_by"] = event["event_id"]
                    break
        records[target_id]["review_observations"].append(observation)
        state["event_index"][event["event_id"]] = copy.deepcopy(observation)
        state["through_position"] = value["ledger_position"]
        state["through_entry_hash"] = value["entry_hash"]
        state["event_count"] += 1
        current_projection_hash = canonical_sha256(state)
        expected_position += 1
        previous_hash = value["entry_hash"]
    return SuccessorProjection(state, current_projection_hash)


def append_successor_event_candidate(
    manifest: Mapping[str, Any],
    existing_entries: Iterable[SuccessorEntry],
    event_draft: Mapping[str, Any],
    *,
    known_pilot_clip_ids: Iterable[str] = (),
) -> tuple[SuccessorEntry, ...]:
    entries = tuple(existing_entries)
    current = replay_successor_entries(
        manifest, entries, known_pilot_clip_ids=known_pilot_clip_ids
    )
    event = finalize_successor_event(
        event_draft,
        manifest=manifest,
        known_pilot_clip_ids=known_pilot_clip_ids,
    )
    if event["precondition_projection_hash"] != current.projection_hash:
        raise SuccessorValidationError("candidate event precondition differs")
    position = current.to_dict()["through_position"] + 1
    previous = current.to_dict()["through_entry_hash"]
    candidate = build_successor_entry(
        manifest, event, position=position, previous_entry_hash=previous
    )
    replay_successor_entries(
        manifest,
        (*entries, candidate),
        known_pilot_clip_ids=known_pilot_clip_ids,
    )
    return (*entries, candidate)


def replay_parent_and_successor(
    parent_manifest: Mapping[str, Any],
    adapter: BaseCatalogAdapter,
    parent_entries: Iterable[LedgerEntry],
    successor_manifest: Mapping[str, Any],
    successor_entries: Iterable[SuccessorEntry],
) -> MixedReplayResult:
    parent_values = tuple(parent_entries)
    parent_projection = replay_entries(parent_manifest, adapter, parent_values)
    expected_binding = build_parent_binding(
        parent_manifest, parent_values, parent_projection
    )
    successor_manifest_value = validate_successor_manifest(dict(successor_manifest))
    if successor_manifest_value["parent_binding"] != expected_binding:
        raise SuccessorValidationError("successor parent binding differs")
    pilots = tuple(sorted(parent_projection.to_dict()["records"]))
    successor_projection = replay_successor_entries(
        successor_manifest_value,
        successor_entries,
        known_pilot_clip_ids=pilots,
    )
    return MixedReplayResult(parent_projection, successor_projection)
