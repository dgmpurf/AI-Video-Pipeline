from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import (
    EVENT_SCHEMA_VERSION,
    EVENT_TYPE_REGISTRY,
    append_event,
    build_checkpoint_payload,
    initialize_manifest,
    load_base_catalog,
    load_validated_ledger,
    replay_entries,
)
from app.ai_video_pipeline.reference_library.persistent_index.builder import (
    BuildResult,
    build_generation,
)
from app.ai_video_pipeline.reference_library.persistent_index.mapper import (
    MappedReadModel,
    map_projection,
)


PROJECT_ROOT = Path(__file__).parents[3]
FIXTURE_PATH = (
    PROJECT_ROOT
    / "tests"
    / "reference_library"
    / "fixtures"
    / "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_CANDIDATE_V0_1.zip"
)
BUILDER_SOURCE_IDENTITY = "c" * 64


def default_payload(event_type: str) -> dict[str, Any]:
    values: dict[str, dict[str, Any]] = {
        "REVIEW_OBSERVATION_ADDED": {
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": "原神 action alpha bounded observation",
        },
        "REVIEW_OBSERVATION_CORRECTED": {
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": "原神 corrected bounded observation",
        },
        "SCORE_RECORD_ADDED": {
            "score_name": "action_value",
            "score_value": "UNKNOWN",
            "score_is_decision_gate": False,
        },
        "SCORE_RECORD_SUPERSEDED": {"reason": "superseded model proposal"},
        "STORAGE_PROPOSAL_ADDED": {
            "proposal_id": "SYNTHETIC-PROPOSAL-001",
            "action": "KEEP",
            "executed": False,
        },
        "STORAGE_PROPOSAL_SUPERSEDED": {"reason": "superseded proposal"},
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
        "RELATIONSHIP_ASSERTION_RETRACTED": {"reason": "bounded retraction"},
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
    return dict(values[event_type])


@dataclass
class LedgerHarness:
    root: Path
    adapter: Any
    counter: int = 0

    def append(
        self,
        event_type: str,
        *,
        pilot_clip_id: str = "G01D-CLIP-001",
        payload: dict[str, Any] | None = None,
        target_ids: tuple[str, ...] | None = None,
        supersedes: tuple[str, ...] = (),
        retracts: tuple[str, ...] = (),
    ):
        self.counter += 1
        second = self.counter % 60
        draft = {
            "event_type": event_type,
            "event_schema_version": EVENT_SCHEMA_VERSION,
            "pilot_clip_id": pilot_clip_id,
            "target_ids": sorted(target_ids or (pilot_clip_id,)),
            "actor": {
                "actor_id": "CODEX-SYNTHETIC-TEST",
                "actor_type": "CODEX",
                "model_name": "SYNTHETIC",
                "model_version": "V0_1",
            },
            "authority_class": EVENT_TYPE_REGISTRY[event_type],
            "occurred_at": f"2026-08-07T00:00:{second:02d}Z",
            "recorded_at": f"2026-08-07T00:01:{second:02d}Z",
            "source_trace_ids": [f"TRACE-SYNTHETIC-{self.counter:03d}"],
            "precondition_checkpoint_id": None,
            "precondition_projection_hash": None,
            "supersedes_event_ids": sorted(supersedes),
            "retracts_event_ids": sorted(retracts),
            "payload": payload if payload is not None else default_payload(event_type),
        }
        return append_event(self.root, self.adapter, draft)

    def append_checkpoint(self):
        manifest, entries = load_validated_ledger(self.root, self.adapter)
        projection = replay_entries(manifest, self.adapter, entries)
        payload = build_checkpoint_payload(projection, entries)
        return self.append("CHECKPOINT_CREATED", payload=payload)

    def mapped(self) -> MappedReadModel:
        manifest, entries = load_validated_ledger(self.root, self.adapter)
        projection = replay_entries(manifest, self.adapter, entries)
        return map_projection(
            self.adapter,
            manifest,
            entries,
            projection,
            builder_source_identity=BUILDER_SOURCE_IDENTITY,
        )


@pytest.fixture(scope="session")
def base_adapter():
    return load_base_catalog(FIXTURE_PATH)


@pytest.fixture
def ledger_harness(tmp_path: Path, base_adapter) -> LedgerHarness:
    root = tmp_path / "ledger"
    initialize_manifest(
        root,
        base_adapter,
        created_by="CODEX_SYNTHETIC_TEST",
        created_at="2026-08-07T00:00:00Z",
    )
    return LedgerHarness(root, base_adapter)


@pytest.fixture
def mapped_empty(ledger_harness: LedgerHarness) -> MappedReadModel:
    return ledger_harness.mapped()


@pytest.fixture
def built_generation(tmp_path: Path, mapped_empty: MappedReadModel) -> BuildResult:
    return build_generation(tmp_path / "state", mapped_empty)
