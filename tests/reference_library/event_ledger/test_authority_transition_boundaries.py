from __future__ import annotations

import copy

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import (
    append_event,
    load_validated_ledger,
    replay_entries,
)
from app.ai_video_pipeline.reference_library.event_ledger.enums import EventType
from app.ai_video_pipeline.reference_library.event_ledger.errors import ProjectionError
from app.ai_video_pipeline.reference_library.event_ledger.manifest import EVENTS_FILENAME
from app.ai_video_pipeline.reference_library.event_ledger.query import projection_record


def _project(ledger, adapter):
    manifest, entries = load_validated_ledger(ledger, adapter)
    return replay_entries(manifest, adapter, entries)


def test_model_score_does_not_create_decision_or_execution(
    initialized_ledger, base_adapter, make_event
) -> None:
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(EventType.SCORE_RECORD_ADDED.value),
    )
    record = projection_record(_project(initialized_ledger, base_adapter), "G01D-CLIP-001")
    assert len(record["score_records"]) == 1
    assert record["human_decisions"] == []
    assert record["execution_receipts"] == []


def test_human_decision_and_execution_receipt_remain_separate(
    initialized_ledger, base_adapter, make_event
) -> None:
    proposal = append_event(
        initialized_ledger,
        base_adapter,
        make_event(EventType.STORAGE_PROPOSAL_ADDED.value),
    )
    decision_payload = {
        "decision_domain": "storage",
        "decision": "ACCEPT",
        "proposal_event_ids": [proposal.event.event_id],
        "reason": "synthetic human decision",
        "authorization_trace_ids": ["AUTH-SYNTHETIC-001"],
    }
    decision = append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.HUMAN_DECISION_RECORDED.value,
            payload=decision_payload,
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    before_execution = projection_record(
        _project(initialized_ledger, base_adapter), "G01D-CLIP-001"
    )
    assert len(before_execution["human_decisions"]) == 1
    assert before_execution["execution_receipts"] == []
    execution_payload = {
        "operation_type": "SYNTHETIC_NOOP",
        "authorization_id": "AUTH-SYNTHETIC-001",
        "decision_event_ids": [decision.event.event_id],
        "operation_success": True,
        "before_identity": {"state": "before"},
        "after_identity": {"state": "after"},
        "receipt_trace_ids": ["RECEIPT-SYNTHETIC-001"],
        "external_operation_count": 0,
    }
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.EXECUTION_AUDIT_RECORDED.value,
            payload=execution_payload,
            occurred_at="2026-08-07T00:00:04Z",
            recorded_at="2026-08-07T00:00:05Z",
        ),
    )
    after_execution = projection_record(
        _project(initialized_ledger, base_adapter), "G01D-CLIP-001"
    )
    assert after_execution["human_decisions"] == before_execution["human_decisions"]
    assert len(after_execution["execution_receipts"]) == 1


def test_rights_evidence_cannot_change_rights_without_human_decision(
    initialized_ledger, base_adapter, make_event
) -> None:
    initial_rights = copy.deepcopy(
        projection_record(_project(initialized_ledger, base_adapter), "G01D-CLIP-001")[
            "rights"
        ]
    )
    evidence = append_event(
        initialized_ledger,
        base_adapter,
        make_event(EventType.RIGHTS_EVIDENCE_ADDED.value),
    )
    after_evidence = projection_record(
        _project(initialized_ledger, base_adapter), "G01D-CLIP-001"
    )
    assert after_evidence["rights"] == initial_rights
    payload = {
        "evidence_event_ids": [evidence.event.event_id],
        "rights_changes": {
            "active_generation_input_allowed": False,
            "publication_allowed": False,
        },
        "reason": "synthetic human rights decision",
        "authorization_trace_ids": ["AUTH-SYNTHETIC-RIGHTS-001"],
    }
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.RIGHTS_DECISION_RECORDED.value,
            payload=payload,
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    after_decision = projection_record(
        _project(initialized_ledger, base_adapter), "G01D-CLIP-001"
    )
    assert after_decision["rights"]["rights_provenance"] == (
        "purchased_unverified_license"
    )
    assert after_decision["rights"]["active_generation_input_allowed"] is False
    assert after_decision["rights"]["publication_allowed"] is False


def test_unknown_is_preserved_until_specific_authorized_transition(
    initialized_ledger, base_adapter, make_event
) -> None:
    initial = projection_record(_project(initialized_ledger, base_adapter), "G01D-CLIP-001")
    assert initial["rights"]["publication_allowed"] == "UNKNOWN"
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(EventType.SCORE_RECORD_ADDED.value),
    )
    scored = projection_record(_project(initialized_ledger, base_adapter), "G01D-CLIP-001")
    assert scored["rights"]["publication_allowed"] == "UNKNOWN"


def test_taxonomy_binding_does_not_create_rights_or_human_approval(
    initialized_ledger, base_adapter, make_event
) -> None:
    initial = projection_record(_project(initialized_ledger, base_adapter), "G01D-CLIP-001")
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(EventType.TAXONOMY_SNAPSHOT_BOUND.value),
    )
    final = projection_record(_project(initialized_ledger, base_adapter), "G01D-CLIP-001")
    assert len(final["taxonomy_bindings"]) == 1
    assert final["rights"] == initial["rights"]
    assert final["human_decisions"] == []


def test_incompatible_supersession_is_rejected_with_no_write(
    initialized_ledger, base_adapter, make_event
) -> None:
    score = append_event(
        initialized_ledger,
        base_adapter,
        make_event(EventType.SCORE_RECORD_ADDED.value),
    )
    before = (initialized_ledger / EVENTS_FILENAME).read_bytes()
    with pytest.raises(ProjectionError, match="incompatible"):
        append_event(
            initialized_ledger,
            base_adapter,
            make_event(
                EventType.REVIEW_OBSERVATION_CORRECTED.value,
                supersedes_event_ids=[score.event.event_id],
                occurred_at="2026-08-07T00:00:02Z",
                recorded_at="2026-08-07T00:00:03Z",
            ),
        )
    assert (initialized_ledger / EVENTS_FILENAME).read_bytes() == before


def test_rights_decision_requires_existing_rights_evidence(
    initialized_ledger, base_adapter, make_event
) -> None:
    payload = {
        "evidence_event_ids": ["RL-EVT-000000000000000000000000"],
        "rights_changes": {"publication_allowed": False},
        "reason": "synthetic decision",
        "authorization_trace_ids": ["AUTH-SYNTHETIC-RIGHTS-001"],
    }
    with pytest.raises(ProjectionError, match="does not exist"):
        append_event(
            initialized_ledger,
            base_adapter,
            make_event(EventType.RIGHTS_DECISION_RECORDED.value, payload=payload),
        )
