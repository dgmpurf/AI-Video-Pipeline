from __future__ import annotations

import copy
import re
from typing import Any, Mapping

from .canonical import (
    canonical_json_bytes,
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


PILOT_CLIP_ID_RE = re.compile(r"^G01D-CLIP-[0-9]{3}$", flags=re.ASCII)
EVENT_ID_RE = re.compile(r"^RL-EVT-[0-9A-F]{24}$", flags=re.ASCII)
EVENT_DRAFT_FIELDS = frozenset(
    {
        "event_type",
        "event_schema_version",
        "pilot_clip_id",
        "target_ids",
        "actor",
        "authority_class",
        "occurred_at",
        "recorded_at",
        "source_trace_ids",
        "precondition_checkpoint_id",
        "precondition_projection_hash",
        "supersedes_event_ids",
        "retracts_event_ids",
        "payload",
    }
)
STORED_EVENT_FIELDS = EVENT_DRAFT_FIELDS | {"event_id", "event_body_hash"}
ACTOR_FIELDS = frozenset(
    {"actor_id", "actor_type", "model_name", "model_version"}
)
ACTOR_TYPES = frozenset(
    {"HUMAN", "CHATGPT", "CODEX", "SYSTEM", "EXTERNAL_OPERATOR"}
)
DECISIONS = frozenset({"ACCEPT", "REJECT", "DEFER", "REVOKE"})
DECISION_DOMAINS = frozenset(
    {"storage", "taxonomy", "relationship", "review", "other_bounded_domain"}
)


def _require_boolean(value: Any, *, field: str) -> bool:
    if not isinstance(value, bool):
        raise SchemaValidationError(f"{field} must be a boolean")
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


def _validate_human_decision_payload(payload: dict[str, Any]) -> None:
    required = {
        "decision_domain",
        "decision",
        "proposal_event_ids",
        "reason",
        "authorization_trace_ids",
    }
    missing = sorted(required - set(payload))
    if missing:
        raise SchemaValidationError(f"human decision payload missing: {missing}")
    if payload["decision_domain"] not in DECISION_DOMAINS:
        raise SchemaValidationError("unsupported decision_domain")
    if payload["decision"] not in DECISIONS:
        raise SchemaValidationError("unsupported decision")
    require_sorted_unique_strings(
        payload["proposal_event_ids"], field="payload.proposal_event_ids"
    )
    require_sorted_unique_strings(
        payload["authorization_trace_ids"],
        field="payload.authorization_trace_ids",
        nonempty=True,
    )
    require_nonempty_string(payload["reason"], field="payload.reason")


def _validate_execution_payload(payload: dict[str, Any]) -> None:
    required = {
        "operation_type",
        "authorization_id",
        "decision_event_ids",
        "operation_success",
        "before_identity",
        "after_identity",
        "receipt_trace_ids",
        "external_operation_count",
    }
    missing = sorted(required - set(payload))
    if missing:
        raise SchemaValidationError(f"execution payload missing: {missing}")
    require_nonempty_string(payload["operation_type"], field="payload.operation_type")
    require_nonempty_string(payload["authorization_id"], field="payload.authorization_id")
    require_sorted_unique_strings(
        payload["decision_event_ids"], field="payload.decision_event_ids"
    )
    require_sorted_unique_strings(
        payload["receipt_trace_ids"],
        field="payload.receipt_trace_ids",
        nonempty=True,
    )
    _require_boolean(payload["operation_success"], field="payload.operation_success")
    if not isinstance(payload["external_operation_count"], int) or isinstance(
        payload["external_operation_count"], bool
    ) or payload["external_operation_count"] < 0:
        raise SchemaValidationError(
            "payload.external_operation_count must be a nonnegative integer"
        )
    for field in ("before_identity", "after_identity"):
        if not isinstance(payload[field], dict):
            raise SchemaValidationError(f"payload.{field} must be an object")


def _validate_relationship_payload(payload: dict[str, Any]) -> None:
    required = {
        "possible_same_family",
        "possible_upstream_overlap",
        "exact_duplicate_status",
    }
    missing = sorted(required - set(payload))
    if missing:
        raise SchemaValidationError(f"relationship payload missing: {missing}")
    if payload["exact_duplicate_status"] not in ("UNKNOWN", False, None):
        raise SchemaValidationError(
            "observation-only relationship cannot establish exact duplicate status"
        )


def _validate_rights_decision_payload(payload: dict[str, Any]) -> None:
    required = {
        "evidence_event_ids",
        "rights_changes",
        "reason",
        "authorization_trace_ids",
    }
    missing = sorted(required - set(payload))
    if missing:
        raise SchemaValidationError(f"rights decision payload missing: {missing}")
    require_sorted_unique_strings(
        payload["evidence_event_ids"],
        field="payload.evidence_event_ids",
        nonempty=True,
    )
    require_sorted_unique_strings(
        payload["authorization_trace_ids"],
        field="payload.authorization_trace_ids",
        nonempty=True,
    )
    require_nonempty_string(payload["reason"], field="payload.reason")
    changes = payload["rights_changes"]
    if not isinstance(changes, dict) or not changes:
        raise SchemaValidationError("payload.rights_changes must be a nonempty object")
    allowed = {
        "rights_provenance",
        "active_generation_input_allowed",
        "publication_allowed",
    }
    if not set(changes).issubset(allowed):
        raise SchemaValidationError("payload.rights_changes contains an unknown field")
    if "rights_provenance" in changes:
        require_nonempty_string(
            changes["rights_provenance"], field="payload.rights_changes.rights_provenance"
        )
    if "active_generation_input_allowed" in changes:
        _require_boolean(
            changes["active_generation_input_allowed"],
            field="payload.rights_changes.active_generation_input_allowed",
        )
    if "publication_allowed" in changes and changes["publication_allowed"] not in (
        True,
        False,
        "UNKNOWN",
    ):
        raise SchemaValidationError("invalid publication_allowed transition")


def validate_payload(event_type: str, payload: Any) -> None:
    if not isinstance(payload, dict):
        raise SchemaValidationError("payload must be an object")
    canonical_json_bytes(payload)
    if event_type == EventType.HUMAN_DECISION_RECORDED.value:
        _validate_human_decision_payload(payload)
    elif event_type == EventType.EXECUTION_AUDIT_RECORDED.value:
        _validate_execution_payload(payload)
    elif event_type == EventType.RELATIONSHIP_ASSERTION_ADDED.value:
        _validate_relationship_payload(payload)
    elif event_type == EventType.RIGHTS_DECISION_RECORDED.value:
        _validate_rights_decision_payload(payload)
    elif event_type == EventType.TAXONOMY_SNAPSHOT_BOUND.value:
        for field in ("taxonomy_snapshot_id", "taxonomy_version"):
            if field not in payload:
                raise SchemaValidationError(f"taxonomy payload missing: {field}")
            require_nonempty_string(payload[field], field=f"payload.{field}")


def validate_event_draft(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaValidationError("event draft must be an object")
    require_exact_keys(value, EVENT_DRAFT_FIELDS, field="event draft")
    if value["event_schema_version"] != EVENT_SCHEMA_VERSION:
        raise SchemaValidationError("unsupported event schema version")
    event_type = require_nonempty_string(value["event_type"], field="event_type")
    authority_class = require_nonempty_string(
        value["authority_class"], field="authority_class"
    )
    validate_registered_authority(event_type, authority_class)
    pilot_clip_id = require_nonempty_string(
        value["pilot_clip_id"], field="pilot_clip_id"
    )
    if PILOT_CLIP_ID_RE.fullmatch(pilot_clip_id) is None:
        raise SchemaValidationError("pilot_clip_id does not match G01D-CLIP-NNN")
    _validate_actor(value["actor"])
    require_rfc3339_utc(value["occurred_at"], field="occurred_at")
    require_rfc3339_utc(value["recorded_at"], field="recorded_at")
    require_sorted_unique_strings(value["target_ids"], field="target_ids")
    require_sorted_unique_strings(
        value["source_trace_ids"], field="source_trace_ids"
    )
    require_sorted_unique_strings(
        value["supersedes_event_ids"], field="supersedes_event_ids"
    )
    require_sorted_unique_strings(
        value["retracts_event_ids"], field="retracts_event_ids"
    )
    checkpoint_id = value["precondition_checkpoint_id"]
    if checkpoint_id is not None:
        require_nonempty_string(
            checkpoint_id, field="precondition_checkpoint_id"
        )
    require_sha256(
        value["precondition_projection_hash"],
        field="precondition_projection_hash",
        nullable=True,
    )
    validate_payload(event_type, value["payload"])
    return copy.deepcopy(value)


def event_body_hash(event_draft: Mapping[str, Any]) -> str:
    return sha256_hex(canonical_json_bytes(dict(event_draft)))


def event_id_from_hash(body_hash: str) -> str:
    require_sha256(body_hash, field="event body hash")
    return "RL-EVT-" + body_hash[:24].upper()


def finalize_event(event_draft: Any) -> dict[str, Any]:
    body = validate_event_draft(event_draft)
    body_hash = event_body_hash(body)
    return {
        **body,
        "event_id": event_id_from_hash(body_hash),
        "event_body_hash": body_hash,
    }


def validate_stored_event(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SchemaValidationError("stored event must be an object")
    require_exact_keys(value, STORED_EVENT_FIELDS, field="stored event")
    event_id = value["event_id"]
    if not isinstance(event_id, str) or EVENT_ID_RE.fullmatch(event_id) is None:
        raise SchemaValidationError("stored event ID is invalid")
    require_sha256(value["event_body_hash"], field="event_body_hash")
    body = {key: child for key, child in value.items() if key in EVENT_DRAFT_FIELDS}
    validate_event_draft(body)
    expected_hash = event_body_hash(body)
    if value["event_body_hash"] != expected_hash:
        raise SchemaValidationError("event body hash does not match")
    if event_id != event_id_from_hash(expected_hash):
        raise SchemaValidationError("event ID does not match full body hash")
    return copy.deepcopy(value)
