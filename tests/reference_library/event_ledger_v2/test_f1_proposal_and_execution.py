import copy

import pytest

from app.ai_video_pipeline.reference_library.event_ledger.v2.errors import ProjectionError
from app.ai_video_pipeline.reference_library.event_ledger.v2.reducers import evaluate_execution_eligibility


def _accept(scenario, proposal, pinned):
    payload = proposal.event.to_dict()["payload"]
    return scenario.add(
        "REPRESENTATIVE_DECISION_RECORDED",
        proposal.event.to_dict()["aggregate_id"],
        list(payload["member_ids"]),
        {
            "representative_decision_id": "REP-DECISION-001",
            "representative_proposal_event_id": proposal.event.event_id,
            "representative_proposal_body_hash": proposal.event.event_body_hash,
            "cluster_snapshot_id": payload["cluster_snapshot_id"],
            "representative_role": payload["representative_role"],
            "member_ids": payload["member_ids"],
            "candidate_ids": payload["candidate_ids"],
            "proposed_member_id": payload["proposed_member_id"],
            "policy_id": payload["policy_id"],
            "policy_version": payload["policy_version"],
            "pinned_v0_2_checkpoint_id": pinned["checkpoint_id"],
            "pinned_v0_2_projection_hash": pinned["projection_hash"],
            "decision": "ACCEPT",
            "reason": "human accepts current exact proposal",
            "authorization_trace_ids": ["AUTH-REP"],
        },
        pinned=True,
    )


def test_current_exact_proposal_and_accept_are_eligible(scenario):
    snapshot, _ = scenario.cluster()
    proposal, pinned = scenario.representative(snapshot)
    decision = _accept(scenario, proposal, pinned)
    result = evaluate_execution_eligibility(
        scenario.projection().to_dict(),
        decision_event_id=decision.event.event_id,
        proposal_event_id=proposal.event.event_id,
    )
    assert result == {"eligible": True, "reasons": []}


def test_retracted_proposal_rejects_execution_after_accept(scenario):
    snapshot, _ = scenario.cluster()
    proposal, pinned = scenario.representative(snapshot)
    decision = _accept(scenario, proposal, pinned)
    payload = proposal.event.to_dict()["payload"]
    scenario.add(
        "REPRESENTATIVE_PROPOSAL_RETRACTED",
        proposal.event.to_dict()["aggregate_id"],
        list(payload["member_ids"]),
        {
            "representative_proposal_event_id": proposal.event.event_id,
            "representative_proposal_id": payload["representative_proposal_id"],
            "cluster_snapshot_id": snapshot,
            "representative_role": payload["representative_role"],
            "reason": "proposal withdrawn",
        },
        retracts=[proposal.event.event_id],
    )
    result = evaluate_execution_eligibility(
        scenario.projection().to_dict(),
        decision_event_id=decision.event.event_id,
        proposal_event_id=proposal.event.event_id,
    )
    assert result["eligible"] is False
    assert "representative_proposal_not_current_active_unsuperseded_unretracted" in result["reasons"]


def test_decision_rejects_exact_binding_mismatch(scenario):
    snapshot, _ = scenario.cluster()
    proposal, pinned = scenario.representative(snapshot)
    payload = proposal.event.to_dict()["payload"]
    altered = copy.deepcopy(payload)
    altered["policy_version"] = "2"
    with pytest.raises(ProjectionError):
        scenario.add(
            "REPRESENTATIVE_DECISION_RECORDED",
            proposal.event.to_dict()["aggregate_id"],
            list(payload["member_ids"]),
            {
                "representative_decision_id": "REP-DECISION-MISMATCH",
                "representative_proposal_event_id": proposal.event.event_id,
                "representative_proposal_body_hash": proposal.event.event_body_hash,
                "cluster_snapshot_id": snapshot,
                "representative_role": payload["representative_role"],
                "member_ids": payload["member_ids"],
                "candidate_ids": payload["candidate_ids"],
                "proposed_member_id": payload["proposed_member_id"],
                "policy_id": payload["policy_id"],
                "policy_version": altered["policy_version"],
                "pinned_v0_2_checkpoint_id": pinned["checkpoint_id"],
                "pinned_v0_2_projection_hash": pinned["projection_hash"],
                "decision": "ACCEPT",
                "reason": "mismatch",
                "authorization_trace_ids": ["AUTH-REP"],
            },
            pinned=True,
        )
