from __future__ import annotations

import copy
import re
from itertools import combinations
from typing import Any, Mapping, Sequence

from .canonical import (
    binary_sorted,
    canonical_json_bytes,
    canonical_sha256,
    require_exact_keys,
    require_nonempty_string,
    require_rfc3339_utc,
    require_sha256,
    require_sorted_unique_strings,
    sha256_hex,
)
from .enums import EVENT_SCHEMA_VERSION, EventType
from .errors import SchemaValidationError
from .registry import validate_registered_authority


EVENT_ID_RE = re.compile(r"^RL2-EVT-[0-9A-F]{24}$", flags=re.ASCII)
EVENT_DRAFT_FIELDS = frozenset(
    {
        "event_schema_version",
        "event_type",
        "aggregate_type",
        "aggregate_id",
        "target_member_ids",
        "actor",
        "authority_class",
        "occurred_at",
        "recorded_at",
        "source_trace_ids",
        "base_v0_1_checkpoint_id",
        "base_v0_1_projection_hash",
        "precondition_v0_2_checkpoint_id",
        "precondition_v0_2_projection_hash",
        "supersedes_event_ids",
        "retracts_event_ids",
        "payload",
    }
)
STORED_EVENT_FIELDS = EVENT_DRAFT_FIELDS | {"event_id", "event_body_hash"}
ACTOR_FIELDS = frozenset({"actor_id", "actor_type", "model_name", "model_version"})
ACTOR_TYPES = frozenset({"HUMAN", "CHATGPT", "CODEX", "SYSTEM", "EXTERNAL_OPERATOR"})
DECISIONS = frozenset({"ACCEPT", "REJECT", "DEFER", "REVOKE"})
EXACT_BYTE_DOMAINS = frozenset({"EXACT_BYTES", "FULL_FILE_SHA256"})

PAYLOAD_FIELDS: Mapping[str, frozenset[str]] = {
    EventType.DUPLICATE_EVIDENCE_ADDED.value: frozenset(
        {
            "evidence_id", "evidence_domain", "evidence_kind", "member_ids",
            "observation_state", "technical_exact_equality", "measurement_trace_ids",
            "evidence_value", "limitations",
        }
    ),
    EventType.DUPLICATE_EVIDENCE_RETRACTED.value: frozenset(
        {"evidence_event_id", "evidence_id", "reason", "authorization_trace_ids"}
    ),
    EventType.PAIR_RELATION_PROPOSAL_ADDED.value: frozenset(
        {
            "pair_relation_proposal_id", "pair_id", "evidence_domain", "member_ids",
            "proposed_relation", "evidence_event_ids", "policy_id", "policy_version",
            "limitations",
        }
    ),
    EventType.PAIR_RELATION_DECISION_RECORDED.value: frozenset(
        {
            "pair_decision_id", "pair_id", "evidence_domain", "member_ids",
            "proposal_event_ids", "decision", "reason", "authorization_trace_ids",
        }
    ),
    EventType.CLUSTER_PROPOSAL_ADDED.value: frozenset(
        {
            "cluster_proposal_id", "cluster_snapshot_id", "cluster_kind", "member_ids",
            "supporting_pair_decision_event_ids", "policy_id", "policy_version",
            "limitations",
        }
    ),
    EventType.CLUSTER_CONFIRMATION_RECORDED.value: frozenset(
        {
            "cluster_confirmation_id", "cluster_snapshot_id", "cluster_kind",
            "member_ids", "decision", "basis_evidence", "reason",
            "authorization_trace_ids",
        }
    ),
    EventType.CLUSTER_CONFIRMATION_RETRACTED.value: frozenset(
        {
            "cluster_confirmation_event_id", "cluster_confirmation_id",
            "cluster_snapshot_id", "reason", "authorization_trace_ids",
        }
    ),
    EventType.REPRESENTATIVE_PROPOSAL_ADDED.value: frozenset(
        {
            "representative_proposal_id", "cluster_snapshot_id", "representative_role",
            "member_ids", "candidate_ids", "proposed_member_id", "policy_id",
            "policy_version", "ranking_facts", "rights_snapshot_refs",
            "lifecycle_snapshot_refs", "limitations",
        }
    ),
    EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value: frozenset(
        {
            "representative_proposal_id", "cluster_snapshot_id", "representative_role",
            "member_ids", "candidate_ids", "proposed_member_id", "policy_id",
            "policy_version", "ranking_facts", "rights_snapshot_refs",
            "lifecycle_snapshot_refs", "limitations", "prior_proposal_event_id",
            "supersession_reason",
        }
    ),
    EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value: frozenset(
        {
            "representative_proposal_event_id", "representative_proposal_id",
            "cluster_snapshot_id", "representative_role", "reason",
        }
    ),
    EventType.REPRESENTATIVE_DECISION_RECORDED.value: frozenset(
        {
            "representative_decision_id", "representative_proposal_event_id",
            "representative_proposal_body_hash", "cluster_snapshot_id",
            "representative_role", "member_ids", "candidate_ids", "proposed_member_id",
            "policy_id", "policy_version", "pinned_v0_2_checkpoint_id",
            "pinned_v0_2_projection_hash", "decision", "reason",
            "authorization_trace_ids",
        }
    ),
    EventType.WORKFLOW_EXECUTION_AUDIT_RECORDED.value: frozenset(
        {
            "operation_type", "authorization_id", "representative_decision_event_id",
            "representative_decision_body_hash", "representative_proposal_event_id",
            "representative_proposal_body_hash", "cluster_snapshot_id",
            "representative_role", "operation_success", "before_identity",
            "after_identity", "receipt_trace_ids", "external_operation_count",
        }
    ),
}


def derive_pair_id(evidence_domain: str, member_ids: Sequence[str]) -> str:
    members = binary_sorted(list(member_ids))
    if len(members) != 2 or len(set(members)) != 2:
        raise SchemaValidationError("pair identity requires two unique members")
    return canonical_sha256(
        {"identity_domain": "RL_PAIR_V0_1", "evidence_domain": evidence_domain, "member_ids": members}
    )


def derive_cluster_snapshot_id(
    cluster_kind: str,
    member_ids: Sequence[str],
    pinned_checkpoint_id: str,
    pinned_projection_hash: str,
) -> str:
    return canonical_sha256(
        {
            "identity_domain": "RL_CLUSTER_SNAPSHOT_V0_1",
            "cluster_kind": cluster_kind,
            "member_ids": binary_sorted(list(member_ids)),
            "pinned_v0_2_checkpoint_id": pinned_checkpoint_id,
            "pinned_v0_2_projection_hash": pinned_projection_hash,
        }
    )


def derive_representative_proposal_id(
    *,
    cluster_snapshot_id: str,
    representative_role: str,
    member_ids: Sequence[str],
    candidate_ids: Sequence[str],
    policy_id: str,
    policy_version: str,
    ranking_facts: Mapping[str, Any],
    pinned_checkpoint_id: str,
    pinned_projection_hash: str,
) -> str:
    return canonical_sha256(
        {
            "identity_domain": "RL_REPRESENTATIVE_PROPOSAL_V0_1",
            "cluster_snapshot_id": cluster_snapshot_id,
            "representative_role": representative_role,
            "member_ids": binary_sorted(list(member_ids)),
            "candidate_ids": binary_sorted(list(candidate_ids)),
            "policy_id": policy_id,
            "policy_version": policy_version,
            "ranking_facts": dict(ranking_facts),
            "pinned_v0_2_checkpoint_id": pinned_checkpoint_id,
            "pinned_v0_2_projection_hash": pinned_projection_hash,
        }
    )


def unordered_member_pairs(member_ids: Sequence[str]) -> tuple[tuple[str, str], ...]:
    members = binary_sorted(list(member_ids))
    return tuple(combinations(members, 2))


def _require_bool(value: Any, *, field: str) -> bool:
    if not isinstance(value, bool):
        raise SchemaValidationError(f"{field} must be boolean")
    return value


def _require_nonnegative_int(value: Any, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise SchemaValidationError(f"{field} must be a nonnegative integer")
    return value


def _validate_actor(value: Any) -> None:
    if not isinstance(value, dict):
        raise SchemaValidationError("actor must be an object")
    require_exact_keys(value, ACTOR_FIELDS, field="actor")
    require_nonempty_string(value["actor_id"], field="actor.actor_id")
    if value["actor_type"] not in ACTOR_TYPES:
        raise SchemaValidationError("actor.actor_type is unsupported")
    for field in ("model_name", "model_version"):
        if value[field] is not None and not isinstance(value[field], str):
            raise SchemaValidationError(f"actor.{field} must be string or null")


def _strings(payload: Mapping[str, Any], fields: Sequence[str]) -> None:
    for field in fields:
        require_nonempty_string(payload[field], field=f"payload.{field}")


def _limitations(value: Any) -> None:
    require_sorted_unique_strings(value, field="payload.limitations")


def _snapshot_refs(value: Any, candidates: Sequence[str], *, field: str) -> None:
    if not isinstance(value, dict) or set(value) != set(candidates):
        raise SchemaValidationError(f"payload.{field} must contain exactly one ref per candidate")
    for candidate, reference in value.items():
        require_nonempty_string(reference, field=f"payload.{field}.{candidate}")


def _validate_payload(event_type: str, payload: Any, event: Mapping[str, Any]) -> None:
    if not isinstance(payload, dict):
        raise SchemaValidationError("payload must be an object")
    require_exact_keys(payload, PAYLOAD_FIELDS[event_type], field=f"{event_type} payload")
    canonical_json_bytes(payload)
    supersedes = event["supersedes_event_ids"]
    retracts = event["retracts_event_ids"]

    if event_type == EventType.DUPLICATE_EVIDENCE_ADDED.value:
        _strings(payload, ("evidence_id", "evidence_domain", "evidence_kind", "observation_state"))
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", nonempty=True)
        require_sorted_unique_strings(payload["measurement_trace_ids"], field="payload.measurement_trace_ids")
        exact = _require_bool(payload["technical_exact_equality"], field="payload.technical_exact_equality")
        if exact and payload["evidence_domain"] not in EXACT_BYTE_DOMAINS:
            raise SchemaValidationError("technical exact equality requires an exact-byte evidence domain")
        _limitations(payload["limitations"])
        if list(members) != event["target_member_ids"]:
            raise SchemaValidationError("evidence member_ids must equal target_member_ids")
        if supersedes or retracts:
            raise SchemaValidationError("evidence-add event cannot supersede or retract")
    elif event_type == EventType.DUPLICATE_EVIDENCE_RETRACTED.value:
        _strings(payload, ("evidence_event_id", "evidence_id", "reason"))
        require_sorted_unique_strings(payload["authorization_trace_ids"], field="payload.authorization_trace_ids", nonempty=True)
        if supersedes or retracts != [payload["evidence_event_id"]]:
            raise SchemaValidationError("evidence retraction cross-reference differs")
    elif event_type == EventType.PAIR_RELATION_PROPOSAL_ADDED.value:
        _strings(payload, ("pair_relation_proposal_id", "pair_id", "evidence_domain", "proposed_relation", "policy_id", "policy_version"))
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", exact_length=2)
        require_sorted_unique_strings(payload["evidence_event_ids"], field="payload.evidence_event_ids", nonempty=True)
        _limitations(payload["limitations"])
        if payload["pair_id"] != derive_pair_id(payload["evidence_domain"], members):
            raise SchemaValidationError("pair_id does not match pair identity")
        if list(members) != event["target_member_ids"] or len(supersedes) > 1 or retracts:
            raise SchemaValidationError("pair proposal envelope cardinality differs")
    elif event_type == EventType.PAIR_RELATION_DECISION_RECORDED.value:
        _strings(payload, ("pair_decision_id", "pair_id", "evidence_domain", "reason"))
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", exact_length=2)
        require_sorted_unique_strings(payload["proposal_event_ids"], field="payload.proposal_event_ids")
        require_sorted_unique_strings(payload["authorization_trace_ids"], field="payload.authorization_trace_ids", nonempty=True)
        if payload["decision"] not in DECISIONS:
            raise SchemaValidationError("unsupported pair decision")
        if payload["pair_id"] != derive_pair_id(payload["evidence_domain"], members):
            raise SchemaValidationError("pair_id does not match pair identity")
        if list(members) != event["target_member_ids"] or len(supersedes) > 1 or retracts:
            raise SchemaValidationError("pair decision envelope cardinality differs")
        if payload["decision"] == "REVOKE" and len(supersedes) != 1:
            raise SchemaValidationError("REVOKE requires one current prior pair decision")
    elif event_type == EventType.CLUSTER_PROPOSAL_ADDED.value:
        _strings(payload, ("cluster_proposal_id", "cluster_snapshot_id", "cluster_kind", "policy_id", "policy_version"))
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", nonempty=True)
        if len(members) < 2:
            raise SchemaValidationError("cluster snapshot requires at least two members")
        require_sorted_unique_strings(payload["supporting_pair_decision_event_ids"], field="payload.supporting_pair_decision_event_ids")
        _limitations(payload["limitations"])
        checkpoint = require_nonempty_string(event["precondition_v0_2_checkpoint_id"], field="precondition_v0_2_checkpoint_id")
        projection_hash = event["precondition_v0_2_projection_hash"]
        require_sha256(projection_hash, field="precondition_v0_2_projection_hash")
        if payload["cluster_snapshot_id"] != derive_cluster_snapshot_id(payload["cluster_kind"], members, checkpoint, projection_hash):
            raise SchemaValidationError("cluster_snapshot_id does not match immutable snapshot")
        if list(members) != event["target_member_ids"] or len(supersedes) > 1 or retracts:
            raise SchemaValidationError("cluster proposal envelope cardinality differs")
    elif event_type == EventType.CLUSTER_CONFIRMATION_RECORDED.value:
        _strings(payload, ("cluster_confirmation_id", "cluster_snapshot_id", "cluster_kind", "reason"))
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", nonempty=True)
        if len(members) < 2 or list(members) != event["target_member_ids"]:
            raise SchemaValidationError("cluster confirmation members differ")
        if payload["decision"] not in DECISIONS:
            raise SchemaValidationError("unsupported cluster confirmation decision")
        require_sorted_unique_strings(payload["authorization_trace_ids"], field="payload.authorization_trace_ids", nonempty=True)
        basis = payload["basis_evidence"]
        if not isinstance(basis, dict) or basis.get("kind") not in {
            "ALL_PAIR_HUMAN_CONFIRMED_SUPPORT", "EXPLICIT_HUMAN_CLUSTER_LEVEL_DECISION"
        }:
            raise SchemaValidationError("cluster confirmation basis is unsupported")
        if basis["kind"] == "ALL_PAIR_HUMAN_CONFIRMED_SUPPORT":
            require_exact_keys(basis, {"kind", "pair_decision_event_ids"}, field="basis_evidence")
            require_sorted_unique_strings(basis["pair_decision_event_ids"], field="basis_evidence.pair_decision_event_ids", nonempty=True)
        else:
            require_exact_keys(basis, {"kind", "cluster_scope_decision_ref"}, field="basis_evidence")
            require_nonempty_string(basis["cluster_scope_decision_ref"], field="basis_evidence.cluster_scope_decision_ref")
        if len(supersedes) > 1 or retracts:
            raise SchemaValidationError("cluster confirmation envelope cardinality differs")
        if payload["decision"] == "REVOKE" and len(supersedes) != 1:
            raise SchemaValidationError("REVOKE requires one current prior cluster decision")
    elif event_type == EventType.CLUSTER_CONFIRMATION_RETRACTED.value:
        _strings(payload, ("cluster_confirmation_event_id", "cluster_confirmation_id", "cluster_snapshot_id", "reason"))
        require_sorted_unique_strings(payload["authorization_trace_ids"], field="payload.authorization_trace_ids", nonempty=True)
        if supersedes or retracts != [payload["cluster_confirmation_event_id"]]:
            raise SchemaValidationError("cluster retraction cross-reference differs")
    elif event_type in {
        EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
        EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
    }:
        _strings(payload, ("representative_proposal_id", "cluster_snapshot_id", "representative_role", "proposed_member_id", "policy_id", "policy_version"))
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", nonempty=True)
        candidates = require_sorted_unique_strings(payload["candidate_ids"], field="payload.candidate_ids", nonempty=True)
        if len(members) < 2 or not set(candidates).issubset(members) or payload["proposed_member_id"] not in candidates:
            raise SchemaValidationError("representative candidate/member relationship differs")
        if not isinstance(payload["ranking_facts"], dict):
            raise SchemaValidationError("ranking_facts must be an object")
        _snapshot_refs(payload["rights_snapshot_refs"], candidates, field="rights_snapshot_refs")
        _snapshot_refs(payload["lifecycle_snapshot_refs"], candidates, field="lifecycle_snapshot_refs")
        _limitations(payload["limitations"])
        checkpoint = require_nonempty_string(event["precondition_v0_2_checkpoint_id"], field="precondition_v0_2_checkpoint_id")
        projection_hash = event["precondition_v0_2_projection_hash"]
        require_sha256(projection_hash, field="precondition_v0_2_projection_hash")
        expected_id = derive_representative_proposal_id(
            cluster_snapshot_id=payload["cluster_snapshot_id"],
            representative_role=payload["representative_role"],
            member_ids=members,
            candidate_ids=candidates,
            policy_id=payload["policy_id"],
            policy_version=payload["policy_version"],
            ranking_facts=payload["ranking_facts"],
            pinned_checkpoint_id=checkpoint,
            pinned_projection_hash=projection_hash,
        )
        if payload["representative_proposal_id"] != expected_id:
            raise SchemaValidationError("representative proposal identity differs")
        if list(members) != event["target_member_ids"] or retracts:
            raise SchemaValidationError("representative proposal envelope differs")
        if event_type == EventType.REPRESENTATIVE_PROPOSAL_ADDED.value:
            if supersedes:
                raise SchemaValidationError("initial representative proposal cannot supersede")
        else:
            _strings(payload, ("prior_proposal_event_id", "supersession_reason"))
            if supersedes != [payload["prior_proposal_event_id"]]:
                raise SchemaValidationError("representative supersession cross-reference differs")
    elif event_type == EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value:
        _strings(payload, ("representative_proposal_event_id", "representative_proposal_id", "cluster_snapshot_id", "representative_role", "reason"))
        if supersedes or retracts != [payload["representative_proposal_event_id"]]:
            raise SchemaValidationError("representative retraction cross-reference differs")
    elif event_type == EventType.REPRESENTATIVE_DECISION_RECORDED.value:
        _strings(payload, ("representative_decision_id", "representative_proposal_event_id", "cluster_snapshot_id", "representative_role", "proposed_member_id", "policy_id", "policy_version", "pinned_v0_2_checkpoint_id", "reason"))
        require_sha256(payload["representative_proposal_body_hash"], field="payload.representative_proposal_body_hash")
        require_sha256(payload["pinned_v0_2_projection_hash"], field="payload.pinned_v0_2_projection_hash")
        members = require_sorted_unique_strings(payload["member_ids"], field="payload.member_ids", nonempty=True)
        candidates = require_sorted_unique_strings(payload["candidate_ids"], field="payload.candidate_ids", nonempty=True)
        if not set(candidates).issubset(members) or payload["proposed_member_id"] not in candidates:
            raise SchemaValidationError("representative decision candidate/member relationship differs")
        require_sorted_unique_strings(payload["authorization_trace_ids"], field="payload.authorization_trace_ids", nonempty=True)
        if payload["decision"] not in DECISIONS:
            raise SchemaValidationError("unsupported representative decision")
        if len(supersedes) > 1 or retracts:
            raise SchemaValidationError("representative decision envelope cardinality differs")
        if payload["decision"] == "REVOKE" and len(supersedes) != 1:
            raise SchemaValidationError("REVOKE requires one current prior representative decision")
    elif event_type == EventType.WORKFLOW_EXECUTION_AUDIT_RECORDED.value:
        _strings(payload, ("operation_type", "authorization_id", "representative_decision_event_id", "representative_proposal_event_id", "cluster_snapshot_id", "representative_role"))
        require_sha256(payload["representative_decision_body_hash"], field="payload.representative_decision_body_hash")
        require_sha256(payload["representative_proposal_body_hash"], field="payload.representative_proposal_body_hash")
        _require_bool(payload["operation_success"], field="payload.operation_success")
        if not isinstance(payload["before_identity"], dict) or not isinstance(payload["after_identity"], dict):
            raise SchemaValidationError("execution before/after identity must be objects")
        require_sorted_unique_strings(payload["receipt_trace_ids"], field="payload.receipt_trace_ids", nonempty=True)
        _require_nonnegative_int(payload["external_operation_count"], field="payload.external_operation_count")
        if supersedes or retracts:
            raise SchemaValidationError("execution audit cannot supersede or retract")


def validate_event_draft(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaValidationError("event draft must be an object")
    require_exact_keys(value, EVENT_DRAFT_FIELDS, field="event draft")
    if value["event_schema_version"] != EVENT_SCHEMA_VERSION:
        raise SchemaValidationError("unsupported event schema version")
    event_type = require_nonempty_string(value["event_type"], field="event_type")
    aggregate_type = require_nonempty_string(value["aggregate_type"], field="aggregate_type")
    require_nonempty_string(value["aggregate_id"], field="aggregate_id")
    authority = require_nonempty_string(value["authority_class"], field="authority_class")
    validate_registered_authority(event_type, authority, aggregate_type)
    _validate_actor(value["actor"])
    require_rfc3339_utc(value["occurred_at"], field="occurred_at")
    require_rfc3339_utc(value["recorded_at"], field="recorded_at")
    require_sorted_unique_strings(value["target_member_ids"], field="target_member_ids", nonempty=True)
    require_sorted_unique_strings(value["source_trace_ids"], field="source_trace_ids")
    require_nonempty_string(value["base_v0_1_checkpoint_id"], field="base_v0_1_checkpoint_id")
    require_sha256(value["base_v0_1_projection_hash"], field="base_v0_1_projection_hash")
    require_sorted_unique_strings(value["supersedes_event_ids"], field="supersedes_event_ids")
    require_sorted_unique_strings(value["retracts_event_ids"], field="retracts_event_ids")
    checkpoint = value["precondition_v0_2_checkpoint_id"]
    projection_hash = value["precondition_v0_2_projection_hash"]
    if (checkpoint is None) != (projection_hash is None):
        raise SchemaValidationError("V0.2 checkpoint/projection preconditions must be paired")
    if checkpoint is not None:
        require_nonempty_string(checkpoint, field="precondition_v0_2_checkpoint_id")
        require_sha256(projection_hash, field="precondition_v0_2_projection_hash")
    _validate_payload(event_type, value["payload"], value)
    return copy.deepcopy(value)


def event_body_hash(event_draft: Mapping[str, Any]) -> str:
    return sha256_hex(canonical_json_bytes(dict(event_draft)))


def event_id_from_hash(body_hash: str) -> str:
    require_sha256(body_hash, field="event body hash")
    return "RL2-EVT-" + body_hash[:24].upper()


def finalize_event(event_draft: Any) -> dict[str, Any]:
    body = validate_event_draft(event_draft)
    body_hash = event_body_hash(body)
    return {**body, "event_id": event_id_from_hash(body_hash), "event_body_hash": body_hash}


def validate_stored_event(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaValidationError("stored event must be an object")
    require_exact_keys(value, STORED_EVENT_FIELDS, field="stored event")
    if not isinstance(value["event_id"], str) or EVENT_ID_RE.fullmatch(value["event_id"]) is None:
        raise SchemaValidationError("stored event ID is invalid")
    require_sha256(value["event_body_hash"], field="event_body_hash")
    body = {key: value[key] for key in EVENT_DRAFT_FIELDS}
    validate_event_draft(body)
    expected_hash = event_body_hash(body)
    if value["event_body_hash"] != expected_hash or value["event_id"] != event_id_from_hash(expected_hash):
        raise SchemaValidationError("stored event identity does not match canonical body")
    return copy.deepcopy(value)
