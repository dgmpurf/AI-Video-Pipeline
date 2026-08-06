from __future__ import annotations

import copy
from typing import Any, Iterable

from .base_catalog import validate_base_binding
from .canonical import canonical_sha256
from .enums import EventType, PROJECTION_SCHEMA_VERSION
from .errors import PreconditionError, ProjectionError
from .models import BaseCatalogAdapter, LedgerEntry, ProjectionResult
from .reducers import apply_reducer


ZERO_HASH = "0" * 64


def initial_projection(
    manifest: dict[str, Any], adapter: BaseCatalogAdapter
) -> ProjectionResult:
    validate_base_binding(manifest["base_catalog"], adapter)
    records: dict[str, Any] = {}
    base_records = adapter.records
    for base_record in base_records:
        pilot_clip_id = str(base_record["record_identity"]["pilot_clip_id"])
        records[pilot_clip_id] = {
            "base_record_id": base_record["record_identity"]["record_id"],
            "artifact_storage": copy.deepcopy(base_record["artifact_storage"]),
            "review_observations": [],
            "score_records": [],
            "storage_proposals": [],
            "human_decisions": [],
            "execution_receipts": [],
            "relationship_assertions": [],
            "rights_evidence": [],
            "rights_decisions": [],
            "taxonomy_bindings": [],
            "rights": copy.deepcopy(base_record["rights"]),
        }
    value = {
        "projection_schema_version": PROJECTION_SCHEMA_VERSION,
        "ledger_id": manifest["ledger_id"],
        "base_catalog": adapter.binding.to_dict(),
        "through_position": 0,
        "through_entry_hash": ZERO_HASH,
        "event_count": 0,
        "records": records,
        "checkpoints": {},
        "event_index": {},
    }
    return ProjectionResult(value, canonical_sha256(value))


def _validate_preconditions(
    event: dict[str, Any], projection: ProjectionResult
) -> None:
    expected_hash = event["precondition_projection_hash"]
    if expected_hash is not None and expected_hash != projection.projection_hash:
        raise PreconditionError("event projection hash precondition does not match")
    checkpoint_id = event["precondition_checkpoint_id"]
    if checkpoint_id is not None:
        checkpoints = projection.to_dict()["checkpoints"]
        if checkpoint_id not in checkpoints:
            raise PreconditionError("event checkpoint precondition is not accepted")


def apply_projected_event(
    projection: ProjectionResult,
    entry: LedgerEntry,
    *,
    prefix_entries: Iterable[LedgerEntry],
) -> ProjectionResult:
    event = entry.event.to_dict()
    _validate_preconditions(event, projection)
    if event["event_type"] == EventType.CHECKPOINT_CREATED.value:
        from .checkpoint import validate_checkpoint_payload

        validate_checkpoint_payload(event["payload"], projection, prefix_entries)
    state = projection.to_dict()
    if entry.position != state["through_position"] + 1:
        raise ProjectionError("projection entry position is not consecutive")
    apply_reducer(state, event, entry.position)
    state["through_position"] = entry.position
    state["through_entry_hash"] = entry.entry_hash
    state["event_count"] += 1
    return ProjectionResult(state, canonical_sha256(state))


def replay_entries(
    manifest: dict[str, Any],
    adapter: BaseCatalogAdapter,
    entries: Iterable[LedgerEntry],
    *,
    through_position: int | None = None,
    through_entry_hash: str | None = None,
    through_checkpoint_id: str | None = None,
) -> ProjectionResult:
    selectors = sum(
        value is not None
        for value in (through_position, through_entry_hash, through_checkpoint_id)
    )
    if selectors > 1:
        raise ProjectionError("only one replay boundary may be selected")
    selected = tuple(entries)
    stop_position: int | None = None
    if through_position is not None:
        if through_position < 0 or through_position > len(selected):
            raise ProjectionError("replay position is outside the ledger")
        stop_position = through_position
    elif through_entry_hash is not None:
        matches = [entry.position for entry in selected if entry.entry_hash == through_entry_hash]
        if len(matches) != 1:
            raise ProjectionError("replay entry hash is not unique and present")
        stop_position = matches[0]
    elif through_checkpoint_id is not None:
        matches = [
            entry.position
            for entry in selected
            if entry.event.event_type == EventType.CHECKPOINT_CREATED.value
            and entry.event.to_dict()["payload"].get("checkpoint_id")
            == through_checkpoint_id
        ]
        if len(matches) != 1:
            raise ProjectionError("checkpoint ID is not unique and present")
        stop_position = matches[0]

    projection = initial_projection(manifest, adapter)
    applied: list[LedgerEntry] = []
    for entry in selected:
        if stop_position is not None and entry.position > stop_position:
            break
        projection = apply_projected_event(
            projection, entry, prefix_entries=tuple(applied)
        )
        applied.append(entry)
    return projection
