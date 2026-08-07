import pytest

from app.ai_video_pipeline.reference_library.duplicate_workflow.errors import MappingError
from app.ai_video_pipeline.reference_library.duplicate_workflow.registry import REGISTRY_BY_TABLE

from conftest import mapped_from_scenario, rich_scenario


def _row(table, row):
    return dict(zip(REGISTRY_BY_TABLE[table].columns, row))


def test_unknown_rights_round_trip_without_false_coercion():
    scenario, *_ = rich_scenario(unknown_member="MEMBER-B")
    mapped = mapped_from_scenario(scenario)
    rows = [_row("member_context_snapshot", row) for row in mapped.rows["member_context_snapshot"]]
    member = next(row for row in rows if row["member_id"] == "MEMBER-B")
    assert member["rights_provenance"] == "UNKNOWN"
    assert member["generation_input_allowed"] == "UNKNOWN"
    assert member["publication_allowed"] == "UNKNOWN"


def test_audit_links_cover_execution_decision_and_proposal(mapped_model):
    links = {_row("audit_link", row)["link_type"] for row in mapped_model.rows["audit_link"]}
    assert {"RECEIPT_DECISION", "RECEIPT_PROPOSAL"} <= links


def test_unverified_rl_p2_context_is_rejected(scenario_bundle):
    with pytest.raises(MappingError):
        mapped_from_scenario(
            scenario_bundle[0],
            rl_p2_context={
                "verified": False,
                "generation_filename": "generation.sqlite3",
                "materialization_generation_id": "1" * 64,
                "logical_content_hash": "2" * 64,
            },
        )
