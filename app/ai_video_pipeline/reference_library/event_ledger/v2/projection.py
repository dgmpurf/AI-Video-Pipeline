from __future__ import annotations

import copy
from typing import Any, Iterable, Mapping

from .base_bridge import validate_base_binding
from .canonical import canonical_sha256
from .enums import PROJECTION_SCHEMA_VERSION
from .errors import PreconditionError, ProjectionError
from .models import BaseV01Snapshot, LedgerEntry, ProjectionResult
from .reducers import apply_reducer


ZERO_HASH = "0" * 64


def _projection_hash(state: Mapping[str, Any]) -> str:
    body = copy.deepcopy(dict(state))
    body.pop("accepted_checkpoints", None)
    body.pop("current_checkpoint_id", None)
    return canonical_sha256(body)


def initial_projection(
    manifest: Mapping[str, Any],
    base: BaseV01Snapshot,
    *,
    accepted_checkpoints: Iterable[Mapping[str, Any]] = (),
) -> ProjectionResult:
    validate_base_binding(manifest["base_v0_1"])
    if manifest["base_v0_1"] != base.binding.to_dict():
        raise ProjectionError("manifest base binding differs from validated V0.1 snapshot")
    accepted_checkpoint_values = tuple(accepted_checkpoints)
    checkpoints = {
        str(item["checkpoint_id"]): copy.deepcopy(dict(item))
        for item in accepted_checkpoint_values
    }
    if len(checkpoints) != len(accepted_checkpoint_values):
        raise ProjectionError("accepted V0.2 checkpoint IDs must be unique")
    state: dict[str, Any] = {
        "projection_schema_version": PROJECTION_SCHEMA_VERSION,
        "ledger_id": manifest["ledger_id"],
        "base_v0_1": base.binding.to_dict(),
        "through_position": 0,
        "through_entry_hash": ZERO_HASH,
        "event_count": 0,
        "current_checkpoint_id": None,
        "member_context": base.member_context_copy(),
        "accepted_checkpoints": checkpoints,
        "event_history": [],
        "event_index": {},
        "duplicate_evidence_history": [],
        "pair_relation_history": [],
        "cluster_proposal_history": [],
        "cluster_snapshots": {},
        "cluster_confirmation_history": [],
        "representative_proposal_history": [],
        "representative_decision_history": [],
        "workflow_execution_receipt_history": [],
    }
    if checkpoints:
        current = max(
            checkpoints.values(), key=lambda item: int(item["through_position"])
        )
        state["current_checkpoint_id"] = current["checkpoint_id"]
    return ProjectionResult(state, _projection_hash(state))


def _validate_preconditions(event: Mapping[str, Any], projection: ProjectionResult) -> None:
    state = projection.to_dict()
    if event["base_v0_1_checkpoint_id"] != state["base_v0_1"]["base_v0_1_checkpoint_id"]:
        raise PreconditionError("event V0.1 checkpoint binding differs")
    if event["base_v0_1_projection_hash"] != state["base_v0_1"]["base_v0_1_projection_hash"]:
        raise PreconditionError("event V0.1 projection binding differs")
    checkpoint_id = event["precondition_v0_2_checkpoint_id"]
    projection_hash = event["precondition_v0_2_projection_hash"]
    if checkpoint_id is not None:
        checkpoint = state["accepted_checkpoints"].get(checkpoint_id)
        if checkpoint is None:
            raise PreconditionError("event V0.2 checkpoint is not accepted")
        if checkpoint["projection_hash"] != projection_hash:
            raise PreconditionError("checkpoint and projection preconditions differ")
        if projection_hash != projection.projection_hash:
            raise PreconditionError("event projection hash precondition is stale")


def apply_projected_event(
    projection: ProjectionResult,
    entry: LedgerEntry,
) -> ProjectionResult:
    event = entry.event.to_dict()
    _validate_preconditions(event, projection)
    state = projection.to_dict()
    if entry.position != state["through_position"] + 1:
        raise ProjectionError("projection entry position is not consecutive")
    apply_reducer(state, event, entry.position)
    state["through_position"] = entry.position
    state["through_entry_hash"] = entry.entry_hash
    state["event_count"] += 1
    return ProjectionResult(state, _projection_hash(state))


def replay_entries(
    manifest: Mapping[str, Any],
    base: BaseV01Snapshot,
    entries: Iterable[LedgerEntry],
    *,
    accepted_checkpoints: Iterable[Mapping[str, Any]] = (),
    through_position: int | None = None,
) -> ProjectionResult:
    selected = tuple(entries)
    if through_position is not None and not 0 <= through_position <= len(selected):
        raise ProjectionError("replay position is outside the ledger")
    projection = initial_projection(
        manifest, base, accepted_checkpoints=tuple(accepted_checkpoints)
    )
    for entry in selected:
        if through_position is not None and entry.position > through_position:
            break
        projection = apply_projected_event(projection, entry)
    return projection
