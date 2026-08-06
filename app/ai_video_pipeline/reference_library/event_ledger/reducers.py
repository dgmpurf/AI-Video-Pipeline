from __future__ import annotations

import copy
from typing import Any

from .enums import EventType
from .errors import ProjectionError


def _event_record(event: dict[str, Any], position: int) -> dict[str, Any]:
    return {
        "event_id": event["event_id"],
        "ledger_position": position,
        "payload": copy.deepcopy(event["payload"]),
        "source_event_ids": list(event["source_trace_ids"]),
        "active": True,
        "superseded_by": None,
        "retracted_by": None,
    }


def _require_empty(value: list[str], *, field: str, event_type: str) -> None:
    if value:
        raise ProjectionError(f"{event_type} requires empty {field}")


def _require_one(value: list[str], *, field: str, event_type: str) -> str:
    if len(value) != 1:
        raise ProjectionError(f"{event_type} requires exactly one {field}")
    return value[0]


def _prior_event(
    state: dict[str, Any],
    event_id: str,
    *,
    allowed_types: set[str],
    pilot_clip_id: str,
    active: bool = True,
) -> dict[str, Any]:
    prior = state["event_index"].get(event_id)
    if prior is None:
        raise ProjectionError(f"referenced event does not exist: {event_id}")
    if prior["event_type"] not in allowed_types:
        raise ProjectionError(f"referenced event has incompatible type: {event_id}")
    if prior["pilot_clip_id"] != pilot_clip_id:
        raise ProjectionError(f"referenced event targets another record: {event_id}")
    if active and prior["active"] is not True:
        raise ProjectionError(f"referenced event is not active: {event_id}")
    return prior


def _append_overlay(
    state: dict[str, Any],
    event: dict[str, Any],
    position: int,
    bucket: str,
) -> dict[str, Any]:
    record = _event_record(event, position)
    state["records"][event["pilot_clip_id"]][bucket].append(record)
    return record


def _mark_prior(
    state: dict[str, Any],
    event_id: str,
    *,
    field: str,
    by_event_id: str,
) -> None:
    indexed = state["event_index"][event_id]
    indexed["active"] = False
    indexed[field] = by_event_id
    overlay = indexed["overlay_record"]
    overlay["active"] = False
    overlay[field] = by_event_id


def apply_reducer(
    state: dict[str, Any], event: dict[str, Any], position: int
) -> None:
    event_type = event["event_type"]
    pilot_clip_id = event["pilot_clip_id"]
    if pilot_clip_id not in state["records"]:
        raise ProjectionError(f"event targets unknown pilot clip: {pilot_clip_id}")
    supersedes = event["supersedes_event_ids"]
    retracts = event["retracts_event_ids"]
    overlay_record: dict[str, Any] | None = None

    if event_type == EventType.REVIEW_OBSERVATION_ADDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _append_overlay(
            state, event, position, "review_observations"
        )
    elif event_type == EventType.REVIEW_OBSERVATION_CORRECTED.value:
        prior_id = _require_one(
            supersedes, field="supersedes_event_ids", event_type=event_type
        )
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        _prior_event(
            state,
            prior_id,
            allowed_types={
                EventType.REVIEW_OBSERVATION_ADDED.value,
                EventType.REVIEW_OBSERVATION_CORRECTED.value,
            },
            pilot_clip_id=pilot_clip_id,
        )
        overlay_record = _append_overlay(
            state, event, position, "review_observations"
        )
        _mark_prior(
            state,
            prior_id,
            field="superseded_by",
            by_event_id=event["event_id"],
        )
    elif event_type == EventType.SCORE_RECORD_ADDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _append_overlay(state, event, position, "score_records")
    elif event_type == EventType.SCORE_RECORD_SUPERSEDED.value:
        prior_id = _require_one(
            supersedes, field="supersedes_event_ids", event_type=event_type
        )
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        _prior_event(
            state,
            prior_id,
            allowed_types={EventType.SCORE_RECORD_ADDED.value},
            pilot_clip_id=pilot_clip_id,
        )
        overlay_record = _append_overlay(state, event, position, "score_records")
        _mark_prior(
            state,
            prior_id,
            field="superseded_by",
            by_event_id=event["event_id"],
        )
    elif event_type == EventType.STORAGE_PROPOSAL_ADDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _append_overlay(state, event, position, "storage_proposals")
    elif event_type == EventType.STORAGE_PROPOSAL_SUPERSEDED.value:
        prior_id = _require_one(
            supersedes, field="supersedes_event_ids", event_type=event_type
        )
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        _prior_event(
            state,
            prior_id,
            allowed_types={EventType.STORAGE_PROPOSAL_ADDED.value},
            pilot_clip_id=pilot_clip_id,
        )
        overlay_record = _append_overlay(state, event, position, "storage_proposals")
        _mark_prior(
            state,
            prior_id,
            field="superseded_by",
            by_event_id=event["event_id"],
        )
    elif event_type == EventType.HUMAN_DECISION_RECORDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        for proposal_id in event["payload"]["proposal_event_ids"]:
            _prior_event(
                state,
                proposal_id,
                allowed_types={EventType.STORAGE_PROPOSAL_ADDED.value},
                pilot_clip_id=pilot_clip_id,
                active=False,
            )
        overlay_record = _append_overlay(state, event, position, "human_decisions")
    elif event_type == EventType.EXECUTION_AUDIT_RECORDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        for decision_id in event["payload"]["decision_event_ids"]:
            _prior_event(
                state,
                decision_id,
                allowed_types={EventType.HUMAN_DECISION_RECORDED.value},
                pilot_clip_id=pilot_clip_id,
                active=False,
            )
        overlay_record = _append_overlay(state, event, position, "execution_receipts")
    elif event_type == EventType.RELATIONSHIP_ASSERTION_ADDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _append_overlay(
            state, event, position, "relationship_assertions"
        )
    elif event_type == EventType.RELATIONSHIP_ASSERTION_RETRACTED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        prior_id = _require_one(
            retracts, field="retracts_event_ids", event_type=event_type
        )
        _prior_event(
            state,
            prior_id,
            allowed_types={EventType.RELATIONSHIP_ASSERTION_ADDED.value},
            pilot_clip_id=pilot_clip_id,
        )
        overlay_record = _append_overlay(
            state, event, position, "relationship_assertions"
        )
        _mark_prior(
            state,
            prior_id,
            field="retracted_by",
            by_event_id=event["event_id"],
        )
    elif event_type == EventType.RIGHTS_EVIDENCE_ADDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _append_overlay(state, event, position, "rights_evidence")
    elif event_type == EventType.RIGHTS_DECISION_RECORDED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        for evidence_id in event["payload"]["evidence_event_ids"]:
            _prior_event(
                state,
                evidence_id,
                allowed_types={EventType.RIGHTS_EVIDENCE_ADDED.value},
                pilot_clip_id=pilot_clip_id,
                active=False,
            )
        overlay_record = _append_overlay(state, event, position, "rights_decisions")
        state["records"][pilot_clip_id]["rights"].update(
            copy.deepcopy(event["payload"]["rights_changes"])
        )
    elif event_type == EventType.TAXONOMY_SNAPSHOT_BOUND.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _append_overlay(state, event, position, "taxonomy_bindings")
    elif event_type == EventType.CHECKPOINT_CREATED.value:
        _require_empty(supersedes, field="supersedes_event_ids", event_type=event_type)
        _require_empty(retracts, field="retracts_event_ids", event_type=event_type)
        overlay_record = _event_record(event, position)
        checkpoint_id = event["payload"]["checkpoint_id"]
        if checkpoint_id in state["checkpoints"]:
            raise ProjectionError(f"duplicate checkpoint ID: {checkpoint_id}")
        state["checkpoints"][checkpoint_id] = overlay_record
    else:
        raise ProjectionError(f"no reducer for event type: {event_type}")

    state["event_index"][event["event_id"]] = {
        "event_type": event_type,
        "pilot_clip_id": pilot_clip_id,
        "ledger_position": position,
        "active": True,
        "superseded_by": None,
        "retracted_by": None,
        "overlay_record": overlay_record,
    }
