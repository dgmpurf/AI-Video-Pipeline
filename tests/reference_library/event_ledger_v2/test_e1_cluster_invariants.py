import pytest

from app.ai_video_pipeline.reference_library.event_ledger.v2.errors import ProjectionError
from app.ai_video_pipeline.reference_library.event_ledger.v2.schema import derive_pair_id


def test_all_pair_basis_requires_complete_exact_coverage(scenario):
    ab = scenario.pair_accept("MEMBER-A", "MEMBER-B")
    bc = scenario.pair_accept("MEMBER-B", "MEMBER-C")
    snapshot, _ = scenario.cluster()
    with pytest.raises(ProjectionError):
        scenario.add(
            "CLUSTER_CONFIRMATION_RECORDED",
            snapshot,
            ["MEMBER-A", "MEMBER-B", "MEMBER-C"],
            {
                "cluster_confirmation_id": "CLUSTER-CONFIRM-001",
                "cluster_snapshot_id": snapshot,
                "cluster_kind": "FULL_FILE_SHA256",
                "member_ids": ["MEMBER-A", "MEMBER-B", "MEMBER-C"],
                "decision": "ACCEPT",
                "basis_evidence": {
                    "kind": "ALL_PAIR_HUMAN_CONFIRMED_SUPPORT",
                    "pair_decision_event_ids": sorted([ab.event.event_id, bc.event.event_id]),
                },
                "reason": "incomplete on purpose",
                "authorization_trace_ids": ["AUTH-CLUSTER"],
            },
        )


def test_explicit_cluster_confirmation_does_not_create_pair_state(scenario):
    snapshot, _ = scenario.cluster()
    scenario.add(
        "CLUSTER_CONFIRMATION_RECORDED",
        snapshot,
        ["MEMBER-A", "MEMBER-B", "MEMBER-C"],
        {
            "cluster_confirmation_id": "CLUSTER-CONFIRM-EXPLICIT",
            "cluster_snapshot_id": snapshot,
            "cluster_kind": "FULL_FILE_SHA256",
            "member_ids": ["MEMBER-A", "MEMBER-B", "MEMBER-C"],
            "decision": "ACCEPT",
            "basis_evidence": {
                "kind": "EXPLICIT_HUMAN_CLUSTER_LEVEL_DECISION",
                "cluster_scope_decision_ref": "HUMAN-CLUSTER-DECISION-001",
            },
            "reason": "cluster scope only",
            "authorization_trace_ids": ["AUTH-CLUSTER"],
        },
    )
    state = scenario.projection().to_dict()
    ac = derive_pair_id("FULL_FILE_SHA256", ["MEMBER-A", "MEMBER-C"])
    assert all(item["event"]["payload"].get("pair_id") != ac for item in state["pair_relation_history"])
