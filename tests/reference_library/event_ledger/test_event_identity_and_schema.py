from __future__ import annotations

import copy

import pytest

from app.ai_video_pipeline.reference_library.event_ledger.canonical import (
    canonical_json_bytes,
    strict_json_loads,
)
from app.ai_video_pipeline.reference_library.event_ledger.enums import (
    AuthorityClass,
    EventType,
)
from app.ai_video_pipeline.reference_library.event_ledger.errors import (
    AuthorityMismatchError,
    CanonicalizationError,
    SchemaValidationError,
)
from app.ai_video_pipeline.reference_library.event_ledger.registry import (
    EVENT_TYPE_REGISTRY,
    registry_document,
)
from app.ai_video_pipeline.reference_library.event_ledger.schema import (
    finalize_event,
    validate_event_draft,
    validate_stored_event,
)


EXPECTED_REGISTRY = {
    "CHECKPOINT_CREATED": "SYSTEM_PROJECTION",
    "EXECUTION_AUDIT_RECORDED": "EXTERNAL_EXECUTION_RECEIPT",
    "HUMAN_DECISION_RECORDED": "HUMAN_DECISION",
    "RELATIONSHIP_ASSERTION_ADDED": "OBSERVATION_ONLY",
    "RELATIONSHIP_ASSERTION_RETRACTED": "OBSERVATION_ONLY",
    "REVIEW_OBSERVATION_ADDED": "OBSERVATION_ONLY",
    "REVIEW_OBSERVATION_CORRECTED": "OBSERVATION_ONLY",
    "RIGHTS_DECISION_RECORDED": "HUMAN_DECISION",
    "RIGHTS_EVIDENCE_ADDED": "OBSERVATION_ONLY",
    "SCORE_RECORD_ADDED": "MODEL_PROPOSAL",
    "SCORE_RECORD_SUPERSEDED": "MODEL_PROPOSAL",
    "STORAGE_PROPOSAL_ADDED": "MODEL_PROPOSAL",
    "STORAGE_PROPOSAL_SUPERSEDED": "MODEL_PROPOSAL",
    "TAXONOMY_SNAPSHOT_BOUND": "OBSERVATION_ONLY",
}


def test_exact_fourteen_event_registry() -> None:
    assert dict(EVENT_TYPE_REGISTRY) == EXPECTED_REGISTRY
    assert registry_document() == {
        "registry_version": "RL_EVENT_REGISTRY_V0_1",
        "events": EXPECTED_REGISTRY,
    }


def test_canonical_json_is_sorted_compact_utf8_without_lf() -> None:
    value = {"z": "中文", "a": [2, 1], "nested": {"b": True, "a": None}}
    assert canonical_json_bytes(value) == (
        b'{"a":[2,1],"nested":{"a":null,"b":true},"z":"\xe4\xb8\xad\xe6\x96\x87"}'
    )
    assert not canonical_json_bytes(value).endswith(b"\n")


@pytest.mark.parametrize(
    "raw",
    [
        b"\xef\xbb\xbf{}",
        b'{"a":1,"a":2}',
        b'{"a":NaN}',
        b'{"a":Infinity}',
        b"\xff",
    ],
)
def test_strict_json_rejects_unsafe_inputs(raw: bytes) -> None:
    with pytest.raises(CanonicalizationError):
        strict_json_loads(raw)


def test_event_identity_is_deterministic_and_full_hash_verified(make_event) -> None:
    draft = make_event()
    first = finalize_event(draft)
    second = finalize_event(copy.deepcopy(draft))
    assert first == second
    assert first["event_id"] == "RL-EVT-" + first["event_body_hash"][:24].upper()
    assert len(first["event_body_hash"]) == 64
    validate_stored_event(first)
    first["payload"]["statement"] = "tampered"
    with pytest.raises(SchemaValidationError, match="hash"):
        validate_stored_event(first)


def test_event_draft_does_not_insert_time_or_random_identity(make_event) -> None:
    draft = make_event()
    validated = validate_event_draft(draft)
    assert validated == draft
    assert "event_id" not in validated
    assert validated["recorded_at"] == "2026-08-07T00:00:01Z"


def test_authority_class_mismatch_is_rejected(make_event) -> None:
    draft = make_event(EventType.HUMAN_DECISION_RECORDED.value)
    draft["authority_class"] = AuthorityClass.MODEL_PROPOSAL.value
    with pytest.raises(AuthorityMismatchError):
        validate_event_draft(draft)


@pytest.mark.parametrize(
    "field,value",
    [
        ("target_ids", ["B", "A"]),
        ("source_trace_ids", ["TRACE-A", "TRACE-A"]),
        ("supersedes_event_ids", ["RL-EVT-B", "RL-EVT-A"]),
        ("retracts_event_ids", ["RL-EVT-A", "RL-EVT-A"]),
    ],
)
def test_identity_arrays_must_be_sorted_and_unique(make_event, field, value) -> None:
    draft = make_event()
    draft[field] = value
    with pytest.raises(SchemaValidationError):
        validate_event_draft(draft)


def test_unknown_event_and_unknown_field_are_rejected(make_event) -> None:
    draft = make_event()
    draft["event_type"] = "UNKNOWN_EVENT"
    with pytest.raises(SchemaValidationError, match="unknown event"):
        validate_event_draft(draft)
    draft = make_event()
    draft["unexpected"] = True
    with pytest.raises(SchemaValidationError, match="keys differ"):
        validate_event_draft(draft)


def test_timestamp_must_be_explicit_valid_utc(make_event) -> None:
    for value in ("2026-08-07T00:00:00+00:00", "2026-13-07T00:00:00Z", ""):
        draft = make_event(recorded_at=value)
        with pytest.raises(SchemaValidationError):
            validate_event_draft(draft)


def test_possible_overlap_cannot_assert_exact_duplicate(make_event) -> None:
    payload = {
        "possible_same_family": ["G01D-CLIP-002"],
        "possible_upstream_overlap": ["G01D-CLIP-003"],
        "exact_duplicate_status": True,
    }
    with pytest.raises(SchemaValidationError, match="exact duplicate"):
        validate_event_draft(
            make_event(EventType.RELATIONSHIP_ASSERTION_ADDED.value, payload=payload)
        )
