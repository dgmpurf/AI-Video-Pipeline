from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import (
    EVENT_SCHEMA_VERSION,
    EVENT_TYPE_REGISTRY,
    initialize_manifest,
    load_base_catalog,
)


PROJECT_ROOT = Path(__file__).parents[3]
FIXTURE_PATH = (
    PROJECT_ROOT
    / "tests"
    / "reference_library"
    / "fixtures"
    / "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_CANDIDATE_V0_1.zip"
)


def payload_for(event_type: str) -> dict[str, Any]:
    values: dict[str, dict[str, Any]] = {
        "REVIEW_OBSERVATION_ADDED": {
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": "bounded synthetic observation",
        },
        "REVIEW_OBSERVATION_CORRECTED": {
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": "bounded corrected observation",
        },
        "SCORE_RECORD_ADDED": {
            "score_name": "action_value",
            "score_value": "UNKNOWN",
            "score_is_decision_gate": False,
        },
        "SCORE_RECORD_SUPERSEDED": {
            "reason": "superseded by a later model proposal"
        },
        "STORAGE_PROPOSAL_ADDED": {
            "proposal_id": "SYNTHETIC-PROPOSAL-001",
            "action": "KEEP",
            "executed": False,
        },
        "STORAGE_PROPOSAL_SUPERSEDED": {
            "reason": "superseded by a later proposal"
        },
        "HUMAN_DECISION_RECORDED": {
            "decision_domain": "storage",
            "decision": "ACCEPT",
            "proposal_event_ids": [],
            "reason": "bounded synthetic human decision",
            "authorization_trace_ids": ["AUTH-SYNTHETIC-001"],
        },
        "EXECUTION_AUDIT_RECORDED": {
            "operation_type": "SYNTHETIC_NOOP",
            "authorization_id": "AUTH-SYNTHETIC-001",
            "decision_event_ids": [],
            "operation_success": True,
            "before_identity": {"state": "before"},
            "after_identity": {"state": "after"},
            "receipt_trace_ids": ["RECEIPT-SYNTHETIC-001"],
            "external_operation_count": 0,
        },
        "RELATIONSHIP_ASSERTION_ADDED": {
            "possible_same_family": ["G01D-CLIP-002"],
            "possible_upstream_overlap": [],
            "exact_duplicate_status": "UNKNOWN",
        },
        "RELATIONSHIP_ASSERTION_RETRACTED": {
            "reason": "bounded synthetic retraction"
        },
        "RIGHTS_EVIDENCE_ADDED": {
            "evidence_type": "LICENSE_TEXT_OBSERVATION",
            "statement": "synthetic evidence only",
        },
        "RIGHTS_DECISION_RECORDED": {
            "evidence_event_ids": [],
            "rights_changes": {"publication_allowed": False},
            "reason": "bounded synthetic rights decision",
            "authorization_trace_ids": ["AUTH-SYNTHETIC-RIGHTS-001"],
        },
        "TAXONOMY_SNAPSHOT_BOUND": {
            "taxonomy_snapshot_id": "TAXONOMY-SYNTHETIC-001",
            "taxonomy_version": "V0_1",
        },
    }
    return dict(values.get(event_type, {}))


@pytest.fixture(scope="session")
def base_adapter():
    return load_base_catalog(FIXTURE_PATH)


@pytest.fixture
def initialized_ledger(tmp_path: Path, base_adapter):
    root = tmp_path / "ledger"
    initialize_manifest(
        root,
        base_adapter,
        created_by="CODEX_SYNTHETIC_TEST",
        created_at="2026-08-07T00:00:00Z",
    )
    return root


@pytest.fixture
def make_event() -> Callable[..., dict[str, Any]]:
    def factory(
        event_type: str = "REVIEW_OBSERVATION_ADDED",
        *,
        pilot_clip_id: str = "G01D-CLIP-001",
        payload: dict[str, Any] | None = None,
        target_ids: list[str] | None = None,
        source_trace_ids: list[str] | None = None,
        supersedes_event_ids: list[str] | None = None,
        retracts_event_ids: list[str] | None = None,
        precondition_projection_hash: str | None = None,
        precondition_checkpoint_id: str | None = None,
        occurred_at: str = "2026-08-07T00:00:00Z",
        recorded_at: str = "2026-08-07T00:00:01Z",
    ) -> dict[str, Any]:
        return {
            "event_type": event_type,
            "event_schema_version": EVENT_SCHEMA_VERSION,
            "pilot_clip_id": pilot_clip_id,
            "target_ids": sorted(
                target_ids if target_ids is not None else [pilot_clip_id]
            ),
            "actor": {
                "actor_id": "CODEX-SYNTHETIC-TEST",
                "actor_type": "CODEX",
                "model_name": "SYNTHETIC",
                "model_version": "V0_1",
            },
            "authority_class": EVENT_TYPE_REGISTRY[event_type],
            "occurred_at": occurred_at,
            "recorded_at": recorded_at,
            "source_trace_ids": sorted(
                source_trace_ids
                if source_trace_ids is not None
                else ["TRACE-SYNTHETIC-001"]
            ),
            "precondition_checkpoint_id": precondition_checkpoint_id,
            "precondition_projection_hash": precondition_projection_hash,
            "supersedes_event_ids": sorted(supersedes_event_ids or []),
            "retracts_event_ids": sorted(retracts_event_ids or []),
            "payload": payload if payload is not None else payload_for(event_type),
        }

    return factory
