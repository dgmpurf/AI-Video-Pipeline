from __future__ import annotations

import copy
from typing import Any, Mapping

from .enums import EventType
from .errors import ProjectionError
from .schema import unordered_member_pairs


def _require_empty(value: list[str], *, field: str, event_type: str) -> None:
    if value:
        raise ProjectionError(f"{event_type} requires empty {field}")


def _require_one(value: list[str], *, field: str, event_type: str) -> str:
    if len(value) != 1:
        raise ProjectionError(f"{event_type} requires exactly one {field}")
    return value[0]


def _history_record(
    event: Mapping[str, Any],
    position: int,
    *,
    active: bool = True,
    current: bool = True,
) -> dict[str, Any]:
    return {
        "event": copy.deepcopy(dict(event)),
        "ledger_position": position,
        "active": active,
        "current": current,
        "superseded_by_event_id": None,
        "retracted_by_event_id": None,
    }


def _append_history(
    state: dict[str, Any],
    bucket: str,
    event: Mapping[str, Any],
    position: int,
    *,
    active: bool = True,
    current: bool = True,
) -> dict[str, Any]:
    record = _history_record(event, position, active=active, current=current)
    state[bucket].append(record)
    state["event_index"][event["event_id"]] = {
        "bucket": bucket,
        "index": len(state[bucket]) - 1,
        "event_type": event["event_type"],
        "aggregate_type": event["aggregate_type"],
        "aggregate_id": event["aggregate_id"],
        "active": active,
        "current": current,
        "superseded_by_event_id": None,
        "retracted_by_event_id": None,
        "event": copy.deepcopy(dict(event)),
    }
    return record


def _prior(
    state: Mapping[str, Any],
    event_id: str,
    *,
    allowed_types: set[str],
    active: bool | None = True,
    current: bool | None = None,
) -> Mapping[str, Any]:
    prior = state["event_index"].get(event_id)
    if prior is None:
        raise ProjectionError(f"referenced event does not exist: {event_id}")
    if prior["event_type"] not in allowed_types:
        raise ProjectionError(f"referenced event has incompatible type: {event_id}")
    if active is not None and prior["active"] is not active:
        raise ProjectionError(f"referenced event active state differs: {event_id}")
    if current is not None and prior["current"] is not current:
        raise ProjectionError(f"referenced event current state differs: {event_id}")
    return prior


def _mark_prior(
    state: dict[str, Any],
    event_id: str,
    *,
    superseded_by: str | None = None,
    retracted_by: str | None = None,
) -> None:
    indexed = state["event_index"][event_id]
    indexed["active"] = False
    indexed["current"] = False
    record = state[indexed["bucket"]][indexed["index"]]
    record["active"] = False
    record["current"] = False
    if superseded_by is not None:
        indexed["superseded_by_event_id"] = superseded_by
        record["superseded_by_event_id"] = superseded_by
    if retracted_by is not None:
        indexed["retracted_by_event_id"] = retracted_by
        record["retracted_by_event_id"] = retracted_by


def _same_fields(
    first: Mapping[str, Any], second: Mapping[str, Any], fields: tuple[str, ...]
) -> bool:
    return all(first.get(field) == second.get(field) for field in fields)


def _require_pair_compatibility(prior: Mapping[str, Any], payload: Mapping[str, Any]) -> None:
    if not _same_fields(
        prior["event"]["payload"],
        payload,
        ("pair_id", "evidence_domain", "member_ids"),
    ):
        raise ProjectionError("referenced pair event is not compatible")


def _require_cluster_compatibility(
    prior: Mapping[str, Any], payload: Mapping[str, Any]
) -> None:
    if not _same_fields(
        prior["event"]["payload"],
        payload,
        ("cluster_snapshot_id",),
    ):
        raise ProjectionError("referenced cluster event is not compatible")


def _proposal_key(payload: Mapping[str, Any]) -> str:
    return f"{payload['cluster_snapshot_id']}::{payload['representative_role']}"


def _require_representative_compatibility(
    prior: Mapping[str, Any], payload: Mapping[str, Any]
) -> None:
    if _proposal_key(prior["event"]["payload"]) != _proposal_key(payload):
        raise ProjectionError("referenced representative event is not compatible")


def _validate_all_pair_basis(
    state: Mapping[str, Any], payload: Mapping[str, Any]
) -> None:
    references = payload["basis_evidence"]["pair_decision_event_ids"]
    observed_pairs: set[tuple[str, str]] = set()
    for event_id in references:
        prior = _prior(
            state,
            event_id,
            allowed_types={EventType.PAIR_RELATION_DECISION_RECORDED.value},
            active=True,
            current=True,
        )
        prior_payload = prior["event"]["payload"]
        if prior_payload["decision"] != "ACCEPT":
            raise ProjectionError("all-pair basis requires current human ACCEPT decisions")
        if prior_payload["evidence_domain"] != payload["cluster_kind"]:
            raise ProjectionError("all-pair basis evidence domain differs from cluster kind")
        observed_pairs.add(tuple(prior_payload["member_ids"]))
    required_pairs = set(unordered_member_pairs(payload["member_ids"]))
    if observed_pairs != required_pairs or len(references) != len(required_pairs):
        raise ProjectionError("all-pair basis does not provide complete exact coverage")


def _validate_representative_decision_binding(
    state: Mapping[str, Any], payload: Mapping[str, Any]
) -> Mapping[str, Any]:
    proposal = _prior(
        state,
        payload["representative_proposal_event_id"],
        allowed_types={
            EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
            EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
        },
        active=True,
        current=True,
    )
    proposal_event = proposal["event"]
    proposal_payload = proposal_event["payload"]
    if proposal_event["event_body_hash"] != payload["representative_proposal_body_hash"]:
        raise ProjectionError("representative proposal body hash differs")
    bindings = (
        "cluster_snapshot_id",
        "representative_role",
        "member_ids",
        "candidate_ids",
        "proposed_member_id",
        "policy_id",
        "policy_version",
    )
    if not _same_fields(proposal_payload, payload, bindings):
        raise ProjectionError("representative decision does not bind the exact proposal")
    if proposal_event["precondition_v0_2_checkpoint_id"] != payload["pinned_v0_2_checkpoint_id"]:
        raise ProjectionError("representative decision checkpoint pin differs")
    if proposal_event["precondition_v0_2_projection_hash"] != payload["pinned_v0_2_projection_hash"]:
        raise ProjectionError("representative decision projection pin differs")
    return proposal


def evaluate_execution_eligibility(
    state: Mapping[str, Any],
    *,
    decision_event_id: str,
    proposal_event_id: str,
) -> dict[str, Any]:
    reasons: list[str] = []
    decision = state["event_index"].get(decision_event_id)
    proposal = state["event_index"].get(proposal_event_id)
    if decision is None or decision["event_type"] != EventType.REPRESENTATIVE_DECISION_RECORDED.value:
        reasons.append("representative_decision_absent")
    elif not decision["current"] or not decision["active"] or decision["event"]["payload"]["decision"] != "ACCEPT":
        reasons.append("human_decision_not_current_active_unrevoked_accept")
    if proposal is None or proposal["event_type"] not in {
        EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
        EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
    }:
        reasons.append("representative_proposal_absent")
    elif not proposal["current"] or not proposal["active"]:
        reasons.append("representative_proposal_not_current_active_unsuperseded_unretracted")
    if reasons:
        return {"eligible": False, "reasons": reasons}
    decision_payload = decision["event"]["payload"]
    proposal_event = proposal["event"]
    if decision_payload["representative_proposal_event_id"] != proposal_event_id:
        reasons.append("decision_proposal_event_mismatch")
    if decision_payload["representative_proposal_body_hash"] != proposal_event["event_body_hash"]:
        reasons.append("decision_proposal_body_hash_mismatch")
    proposed_member = proposal_event["payload"]["proposed_member_id"]
    context = state["member_context"].get(proposed_member)
    if context is None:
        reasons.append("proposed_member_context_absent")
    else:
        if context.get("generation_input_allowed") not in (True, 1):
            reasons.append("rights_generation_input_not_allowed")
        if context.get("publication_allowed") not in (True, "TRUE"):
            reasons.append("rights_publication_not_allowed")
        if context.get("availability") not in ("AVAILABLE", "PRESENT"):
            reasons.append("member_not_available")
        if context.get("lifecycle") not in ("ACTIVE", "CURRENT"):
            reasons.append("member_lifecycle_not_active")
        rights_ref = proposal_event["payload"]["rights_snapshot_refs"][proposed_member]
        lifecycle_ref = proposal_event["payload"]["lifecycle_snapshot_refs"][proposed_member]
        if context.get("rights_snapshot_ref") != rights_ref:
            reasons.append("rights_snapshot_ref_stale")
        if context.get("lifecycle_snapshot_ref") != lifecycle_ref:
            reasons.append("lifecycle_snapshot_ref_stale")
    return {"eligible": not reasons, "reasons": reasons}


def apply_reducer(state: dict[str, Any], event: dict[str, Any], position: int) -> None:
    event_type = event["event_type"]
    payload = event["payload"]
    supersedes = event["supersedes_event_ids"]
    retracts = event["retracts_event_ids"]

    if event_type == EventType.DUPLICATE_EVIDENCE_ADDED.value:
        _append_history(state, "duplicate_evidence_history", event, position)
    elif event_type == EventType.DUPLICATE_EVIDENCE_RETRACTED.value:
        prior_id = _require_one(retracts, field="retracts_event_ids", event_type=event_type)
        prior = _prior(
            state, prior_id,
            allowed_types={EventType.DUPLICATE_EVIDENCE_ADDED.value},
            active=True,
        )
        if prior["event"]["payload"]["evidence_id"] != payload["evidence_id"]:
            raise ProjectionError("evidence retraction ID differs")
        _mark_prior(state, prior_id, retracted_by=event["event_id"])
        _append_history(state, "duplicate_evidence_history", event, position, active=False, current=False)
    elif event_type == EventType.PAIR_RELATION_PROPOSAL_ADDED.value:
        if supersedes:
            prior_id = supersedes[0]
            prior = _prior(
                state, prior_id,
                allowed_types={EventType.PAIR_RELATION_PROPOSAL_ADDED.value},
                active=True, current=True,
            )
            _require_pair_compatibility(prior, payload)
            _mark_prior(state, prior_id, superseded_by=event["event_id"])
        _append_history(state, "pair_relation_history", event, position)
    elif event_type == EventType.PAIR_RELATION_DECISION_RECORDED.value:
        if supersedes:
            prior_id = supersedes[0]
            prior = _prior(
                state, prior_id,
                allowed_types={EventType.PAIR_RELATION_DECISION_RECORDED.value},
                active=True, current=True,
            )
            _require_pair_compatibility(prior, payload)
            _mark_prior(state, prior_id, superseded_by=event["event_id"])
        for proposal_id in payload["proposal_event_ids"]:
            proposal = _prior(
                state, proposal_id,
                allowed_types={EventType.PAIR_RELATION_PROPOSAL_ADDED.value},
                active=None, current=None,
            )
            _require_pair_compatibility(proposal, payload)
        _append_history(state, "pair_relation_history", event, position)
    elif event_type == EventType.CLUSTER_PROPOSAL_ADDED.value:
        snapshot_id = payload["cluster_snapshot_id"]
        existing = state["cluster_snapshots"].get(snapshot_id)
        snapshot = {
            "cluster_snapshot_id": snapshot_id,
            "cluster_kind": payload["cluster_kind"],
            "member_ids": copy.deepcopy(payload["member_ids"]),
            "proposal_event_id": event["event_id"],
            "policy_id": payload["policy_id"],
            "policy_version": payload["policy_version"],
            "pinned_checkpoint_id": event["precondition_v0_2_checkpoint_id"],
            "pinned_projection_hash": event["precondition_v0_2_projection_hash"],
            "created_ledger_position": position,
        }
        if existing is not None and {
            key: existing[key] for key in ("cluster_snapshot_id", "cluster_kind", "member_ids", "pinned_checkpoint_id", "pinned_projection_hash")
        } != {
            key: snapshot[key] for key in ("cluster_snapshot_id", "cluster_kind", "member_ids", "pinned_checkpoint_id", "pinned_projection_hash")
        }:
            raise ProjectionError("cluster snapshot identity collision")
        state["cluster_snapshots"].setdefault(snapshot_id, snapshot)
        if supersedes:
            prior_id = supersedes[0]
            prior = _prior(
                state, prior_id,
                allowed_types={EventType.CLUSTER_PROPOSAL_ADDED.value},
                active=True, current=True,
            )
            _require_cluster_compatibility(prior, payload)
            _mark_prior(state, prior_id, superseded_by=event["event_id"])
        _append_history(state, "cluster_proposal_history", event, position)
    elif event_type == EventType.CLUSTER_CONFIRMATION_RECORDED.value:
        snapshot = state["cluster_snapshots"].get(payload["cluster_snapshot_id"])
        if snapshot is None or snapshot["member_ids"] != payload["member_ids"] or snapshot["cluster_kind"] != payload["cluster_kind"]:
            raise ProjectionError("cluster confirmation does not match an immutable snapshot")
        if payload["basis_evidence"]["kind"] == "ALL_PAIR_HUMAN_CONFIRMED_SUPPORT":
            _validate_all_pair_basis(state, payload)
        if supersedes:
            prior_id = supersedes[0]
            prior = _prior(
                state, prior_id,
                allowed_types={EventType.CLUSTER_CONFIRMATION_RECORDED.value},
                active=True, current=True,
            )
            _require_cluster_compatibility(prior, payload)
            _mark_prior(state, prior_id, superseded_by=event["event_id"])
        _append_history(state, "cluster_confirmation_history", event, position)
    elif event_type == EventType.CLUSTER_CONFIRMATION_RETRACTED.value:
        prior_id = _require_one(retracts, field="retracts_event_ids", event_type=event_type)
        prior = _prior(
            state, prior_id,
            allowed_types={EventType.CLUSTER_CONFIRMATION_RECORDED.value},
            active=True, current=True,
        )
        _require_cluster_compatibility(prior, payload)
        _mark_prior(state, prior_id, retracted_by=event["event_id"])
        _append_history(state, "cluster_confirmation_history", event, position, active=False, current=False)
    elif event_type == EventType.REPRESENTATIVE_PROPOSAL_ADDED.value:
        key = _proposal_key(payload)
        if any(
            item["current"] and _proposal_key(item["event"]["payload"]) == key
            for item in state["representative_proposal_history"]
        ):
            raise ProjectionError("an initial current proposal already exists for snapshot and role")
        _append_history(state, "representative_proposal_history", event, position)
    elif event_type == EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value:
        prior_id = _require_one(supersedes, field="supersedes_event_ids", event_type=event_type)
        prior = _prior(
            state, prior_id,
            allowed_types={
                EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
                EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
            },
            active=True, current=True,
        )
        _require_representative_compatibility(prior, payload)
        _mark_prior(state, prior_id, superseded_by=event["event_id"])
        _append_history(state, "representative_proposal_history", event, position)
    elif event_type == EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value:
        prior_id = _require_one(retracts, field="retracts_event_ids", event_type=event_type)
        prior = _prior(
            state, prior_id,
            allowed_types={
                EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
                EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
            },
            active=True, current=True,
        )
        _require_representative_compatibility(prior, payload)
        if prior["event"]["payload"]["representative_proposal_id"] != payload["representative_proposal_id"]:
            raise ProjectionError("representative proposal retraction identity differs")
        _mark_prior(state, prior_id, retracted_by=event["event_id"])
        _append_history(state, "representative_proposal_history", event, position, active=False, current=False)
    elif event_type == EventType.REPRESENTATIVE_DECISION_RECORDED.value:
        if payload["decision"] == "REVOKE":
            prior_id = _require_one(supersedes, field="supersedes_event_ids", event_type=event_type)
            prior = _prior(
                state, prior_id,
                allowed_types={EventType.REPRESENTATIVE_DECISION_RECORDED.value},
                active=True, current=True,
            )
            if prior["event"]["payload"]["decision"] != "ACCEPT":
                raise ProjectionError("representative REVOKE requires a current ACCEPT decision")
            if not _same_fields(
                prior["event"]["payload"], payload,
                ("representative_proposal_event_id", "cluster_snapshot_id", "representative_role"),
            ):
                raise ProjectionError("representative REVOKE is not compatible")
            _mark_prior(state, prior_id, superseded_by=event["event_id"])
        else:
            _validate_representative_decision_binding(state, payload)
            if supersedes:
                prior_id = supersedes[0]
                prior = _prior(
                    state, prior_id,
                    allowed_types={EventType.REPRESENTATIVE_DECISION_RECORDED.value},
                    active=True, current=True,
                )
                if not _same_fields(
                    prior["event"]["payload"], payload,
                    ("cluster_snapshot_id", "representative_role"),
                ):
                    raise ProjectionError("representative decision supersession is incompatible")
                _mark_prior(state, prior_id, superseded_by=event["event_id"])
        _append_history(state, "representative_decision_history", event, position)
    elif event_type == EventType.WORKFLOW_EXECUTION_AUDIT_RECORDED.value:
        decision = _prior(
            state, payload["representative_decision_event_id"],
            allowed_types={EventType.REPRESENTATIVE_DECISION_RECORDED.value},
            active=None, current=None,
        )
        proposal = _prior(
            state, payload["representative_proposal_event_id"],
            allowed_types={
                EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
                EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
            },
            active=None, current=None,
        )
        if decision["event"]["event_body_hash"] != payload["representative_decision_body_hash"]:
            raise ProjectionError("execution decision body hash differs")
        if proposal["event"]["event_body_hash"] != payload["representative_proposal_body_hash"]:
            raise ProjectionError("execution proposal body hash differs")
        eligibility = evaluate_execution_eligibility(
            state,
            decision_event_id=payload["representative_decision_event_id"],
            proposal_event_id=payload["representative_proposal_event_id"],
        )
        if not eligibility["eligible"]:
            raise ProjectionError(
                "workflow execution is not eligible: " + ",".join(eligibility["reasons"])
            )
        _append_history(state, "workflow_execution_receipt_history", event, position)
    else:
        raise ProjectionError(f"no V0.2 reducer for event type: {event_type}")

    state["event_history"].append(copy.deepcopy(state["event_index"][event["event_id"]]))
