from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.duplicate_workflow.mapper import map_projection


_HELPER_PATH = Path(__file__).parents[1] / "event_ledger_v2" / "conftest.py"
_SPEC = importlib.util.spec_from_file_location("_rl_p3_event_test_helpers", _HELPER_PATH)
assert _SPEC is not None and _SPEC.loader is not None
_HELPERS = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _HELPERS
_SPEC.loader.exec_module(_HELPERS)

EventScenario = _HELPERS.EventScenario
MEMBERS = _HELPERS.MEMBERS


def make_base():
    return _HELPERS.base_snapshot.__wrapped__()


def add_representative_accept(scenario, proposal, pinned):
    payload = proposal.event.to_dict()["payload"]
    return scenario.add(
        "REPRESENTATIVE_DECISION_RECORDED",
        proposal.event.to_dict()["aggregate_id"],
        list(payload["member_ids"]),
        {
            "representative_decision_id": "REP-DECISION-STORE-001",
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
            "reason": "store fixture acceptance",
            "authorization_trace_ids": ["AUTH-STORE"],
        },
        pinned=True,
    )


def rich_scenario(*, unknown_member: str | None = None):
    base = make_base()
    if unknown_member is not None:
        base.member_context[unknown_member]["generation_input_allowed"] = "UNKNOWN"
        base.member_context[unknown_member]["publication_allowed"] = "UNKNOWN"
        base.member_context[unknown_member]["rights_provenance"] = "UNKNOWN"
    scenario = EventScenario.create(base)
    scenario.pair_accept("MEMBER-A", "MEMBER-B")
    snapshot, _ = scenario.cluster()
    scenario.add(
        "CLUSTER_CONFIRMATION_RECORDED",
        snapshot,
        list(MEMBERS),
        {
            "cluster_confirmation_id": "CLUSTER-CONFIRM-STORE-001",
            "cluster_snapshot_id": snapshot,
            "cluster_kind": "FULL_FILE_SHA256",
            "member_ids": list(MEMBERS),
            "decision": "ACCEPT",
            "basis_evidence": {
                "kind": "EXPLICIT_HUMAN_CLUSTER_LEVEL_DECISION",
                "cluster_scope_decision_ref": "HUMAN-CLUSTER-STORE-001",
            },
            "reason": "cluster scope fixture",
            "authorization_trace_ids": ["AUTH-CLUSTER-STORE"],
        },
    )
    proposal, pinned = scenario.representative(snapshot)
    decision = add_representative_accept(scenario, proposal, pinned)
    scenario.add(
        "WORKFLOW_EXECUTION_AUDIT_RECORDED",
        proposal.event.to_dict()["aggregate_id"],
        list(MEMBERS),
        {
            "operation_type": "SYNTHETIC_NO_EXTERNAL_EFFECT",
            "authorization_id": "AUTH-EXEC-STORE",
            "representative_decision_event_id": decision.event.event_id,
            "representative_decision_body_hash": decision.event.event_body_hash,
            "representative_proposal_event_id": proposal.event.event_id,
            "representative_proposal_body_hash": proposal.event.event_body_hash,
            "cluster_snapshot_id": snapshot,
            "representative_role": "GENERATION_INPUT",
            "operation_success": True,
            "before_identity": {"state": "BEFORE"},
            "after_identity": {"state": "AFTER"},
            "receipt_trace_ids": ["RECEIPT-STORE"],
            "external_operation_count": 0,
        },
        pinned=True,
    )
    scenario.checkpoint()
    return scenario, snapshot, proposal, decision


def mapped_from_scenario(scenario, *, rl_p2_context=None):
    projection = scenario.projection()
    return map_projection(
        scenario.base,
        scenario.manifest,
        tuple(scenario.entries),
        projection,
        rl_p2_context=rl_p2_context,
    )


@pytest.fixture
def scenario_bundle():
    return rich_scenario()


@pytest.fixture
def mapped_model(scenario_bundle):
    return mapped_from_scenario(scenario_bundle[0])
