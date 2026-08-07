from __future__ import annotations

import sqlite3

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import (
    load_validated_ledger,
    replay_entries,
)
from app.ai_video_pipeline.reference_library.event_ledger.models import ProjectionResult
from app.ai_video_pipeline.reference_library.persistent_index.errors import MappingError
from app.ai_video_pipeline.reference_library.persistent_index.builder import build_generation
from app.ai_video_pipeline.reference_library.persistent_index.identity import (
    LOGICAL_REGISTRY,
)
from app.ai_video_pipeline.reference_library.persistent_index.mapper import map_projection
from app.ai_video_pipeline.reference_library.persistent_index.verify import open_read_only

def test_rl_p0_mapping_parity_and_closed_table_coverage(base_adapter, mapped_empty):
    assert set(mapped_empty.rows) == {entry.table for entry in LOGICAL_REGISTRY}
    assert len(mapped_empty.table("reference_record")) == base_adapter.binding.record_count == 30
    assert len(mapped_empty.table("artifact_storage_current")) == 30
    assert len(mapped_empty.table("rights_current")) == 30
    assert len(mapped_empty.table("artifact")) == sum(
        len(record["artifacts"]) for record in base_adapter.records
    )
    mapped_ids = {row[0] for row in mapped_empty.table("reference_record")}
    source_ids = {
        record["record_identity"]["pilot_clip_id"] for record in base_adapter.records
    }
    assert mapped_ids == source_ids


def test_rl_p1_history_current_and_checkpoint_mapping(tmp_path, ledger_harness):
    first = ledger_harness.append("REVIEW_OBSERVATION_ADDED")
    ledger_harness.append(
        "REVIEW_OBSERVATION_CORRECTED",
        supersedes=(first.event.event_id,),
    )
    ledger_harness.append("SCORE_RECORD_ADDED")
    ledger_harness.append("STORAGE_PROPOSAL_ADDED")
    evidence = ledger_harness.append("RIGHTS_EVIDENCE_ADDED")
    rights_payload = {
        "evidence_event_ids": [evidence.event.event_id],
        "rights_changes": {
            "active_generation_input_allowed": True,
            "publication_allowed": "UNKNOWN",
        },
        "reason": "bounded human rights decision",
        "authorization_trace_ids": ["AUTH-SYNTHETIC-RIGHTS-002"],
    }
    ledger_harness.append("RIGHTS_DECISION_RECORDED", payload=rights_payload)
    ledger_harness.append_checkpoint()
    mapped = ledger_harness.mapped()

    observations = mapped.table("review_observation_history")
    assert len(observations) == 2
    assert [row[8] for row in observations] == [0, 1]
    assert observations[0][9] == observations[1][0]
    assert len(mapped.table("score_record_history")) == 1
    assert mapped.table("score_record_history")[0][8] == 0
    assert len(mapped.table("storage_proposal_history")) == 1
    assert mapped.table("storage_proposal_history")[0][8] == 0
    assert len(mapped.table("rights_evidence_history")) == 1
    assert len(mapped.table("rights_decision_history")) == 1
    current_rights = {
        row[0]: row for row in mapped.table("rights_current")
    }["G01D-CLIP-001"]
    assert current_rights[2:4] == (1, "UNKNOWN")
    checkpoint = mapped.table("checkpoint_history")[0]
    assert "total_unknown_values" in checkpoint[11]
    assert len(mapped.table("ledger_event_provenance")) == 7
    assert build_generation(tmp_path / "state", mapped).verification.valid


def test_physical_schema_constraints_and_fts_parity(built_generation):
    with open_read_only(built_generation.generation_path) as connection:
        assert connection.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
            )
        }
        assert {entry.table for entry in LOGICAL_REGISTRY}.issubset(tables)
        assert connection.execute("SELECT count(*) FROM search_current_fts").fetchone()[0] == 30
        assert connection.execute("SELECT count(*) FROM search_history_fts").fetchone()[0] == 0
        assert tuple(connection.execute(
            "SELECT generation_input_allowed,publication_allowed FROM rights_current "
            "WHERE pilot_clip_id='G01D-CLIP-001'"
        ).fetchone()) == (0, "UNKNOWN")


def test_unknown_projection_bucket_fails_mapping(ledger_harness):
    manifest, entries = load_validated_ledger(ledger_harness.root, ledger_harness.adapter)
    projection = replay_entries(manifest, ledger_harness.adapter, entries)
    state = projection.to_dict()
    state["records"]["G01D-CLIP-001"]["unregistered_bucket"] = []
    changed = ProjectionResult(state, projection.projection_hash)
    with pytest.raises(MappingError, match="bucket set differs"):
        map_projection(
            ledger_harness.adapter,
            manifest,
            entries,
            changed,
            builder_source_identity="c" * 64,
        )
