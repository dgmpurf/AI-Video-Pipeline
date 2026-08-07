from app.ai_video_pipeline.reference_library.event_ledger.v2.checkpoint import (
    build_checkpoint_payload,
    validate_checkpoint_payload,
)


def test_replay_is_deterministic_and_checkpoint_bound(scenario):
    scenario.evidence()
    first = scenario.projection()
    second = scenario.projection()
    assert first.projection_hash == second.projection_hash
    checkpoint = build_checkpoint_payload(first, scenario.entries)
    validate_checkpoint_payload(checkpoint, second, scenario.entries)
    assert checkpoint["through_position"] == 1


def test_evidence_retraction_preserves_history(scenario):
    evidence = scenario.evidence()
    scenario.add(
        "DUPLICATE_EVIDENCE_RETRACTED",
        evidence.event.to_dict()["aggregate_id"],
        ["MEMBER-A", "MEMBER-B"],
        {
            "evidence_event_id": evidence.event.event_id,
            "evidence_id": "EVIDENCE-MEMBER-A-MEMBER-B",
            "reason": "synthetic correction",
            "authorization_trace_ids": ["AUTH-RETRACT"],
        },
        retracts=[evidence.event.event_id],
    )
    state = scenario.projection().to_dict()
    assert len(state["duplicate_evidence_history"]) == 2
    assert state["event_index"][evidence.event.event_id]["active"] is False
