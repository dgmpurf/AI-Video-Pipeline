from __future__ import annotations

from app.ai_video_pipeline.reference_library.event_ledger import (
    append_event,
    build_checkpoint_payload,
    load_validated_ledger,
    read_manifest,
    replay_entries,
)
from app.ai_video_pipeline.reference_library.event_ledger.enums import EventType
from app.ai_video_pipeline.reference_library.event_ledger.errors import (
    CheckpointError,
    PreconditionError,
)
from app.ai_video_pipeline.reference_library.event_ledger.manifest import EVENTS_FILENAME
from app.ai_video_pipeline.reference_library.event_ledger.projection import (
    initial_projection,
)
from app.ai_video_pipeline.reference_library.event_ledger.query import (
    projection_record,
)


def test_replay_is_deterministic_and_has_exact_provenance(
    initialized_ledger, base_adapter, make_event
) -> None:
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(source_trace_ids=["TRACE-A", "TRACE-B"]),
    )
    manifest, entries = load_validated_ledger(initialized_ledger, base_adapter)
    first = replay_entries(manifest, base_adapter, entries)
    second = replay_entries(manifest, base_adapter, entries)
    assert first.to_dict() == second.to_dict()
    assert first.projection_hash == second.projection_hash
    observation = projection_record(first, "G01D-CLIP-001")["review_observations"][0]
    assert observation["source_event_ids"] == ["TRACE-A", "TRACE-B"]
    assert observation["event_id"] == entries[0].event.event_id


def test_correction_supersession_and_retraction_preserve_history(
    initialized_ledger, base_adapter, make_event
) -> None:
    observation = append_event(initialized_ledger, base_adapter, make_event())
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.REVIEW_OBSERVATION_CORRECTED.value,
            supersedes_event_ids=[observation.event.event_id],
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    score = append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.SCORE_RECORD_ADDED.value,
            occurred_at="2026-08-07T00:00:04Z",
            recorded_at="2026-08-07T00:00:05Z",
        ),
    )
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.SCORE_RECORD_SUPERSEDED.value,
            supersedes_event_ids=[score.event.event_id],
            occurred_at="2026-08-07T00:00:06Z",
            recorded_at="2026-08-07T00:00:07Z",
        ),
    )
    relationship = append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.RELATIONSHIP_ASSERTION_ADDED.value,
            occurred_at="2026-08-07T00:00:08Z",
            recorded_at="2026-08-07T00:00:09Z",
        ),
    )
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.RELATIONSHIP_ASSERTION_RETRACTED.value,
            retracts_event_ids=[relationship.event.event_id],
            occurred_at="2026-08-07T00:00:10Z",
            recorded_at="2026-08-07T00:00:11Z",
        ),
    )
    manifest, entries = load_validated_ledger(initialized_ledger, base_adapter)
    record = projection_record(
        replay_entries(manifest, base_adapter, entries), "G01D-CLIP-001"
    )
    assert len(record["review_observations"]) == 2
    assert record["review_observations"][0]["active"] is False
    assert record["review_observations"][1]["active"] is True
    assert len(record["score_records"]) == 2
    assert record["score_records"][0]["active"] is False
    assert len(record["relationship_assertions"]) == 2
    assert record["relationship_assertions"][0]["active"] is False
    assert record["relationship_assertions"][0]["retracted_by"] is not None


def test_projection_hash_precondition_is_checked_against_immediate_prefix(
    initialized_ledger, base_adapter, make_event
) -> None:
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    initial = initial_projection(manifest, base_adapter)
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(precondition_projection_hash=initial.projection_hash),
    )
    before = (initialized_ledger / EVENTS_FILENAME).read_bytes()
    try:
        append_event(
            initialized_ledger,
            base_adapter,
            make_event(
                pilot_clip_id="G01D-CLIP-002",
                precondition_projection_hash=initial.projection_hash,
                occurred_at="2026-08-07T00:00:02Z",
                recorded_at="2026-08-07T00:00:03Z",
            ),
        )
    except PreconditionError:
        pass
    else:
        raise AssertionError("stale projection precondition was accepted")
    assert (initialized_ledger / EVENTS_FILENAME).read_bytes() == before


def test_replay_through_position_and_entry_hash_is_read_only(
    initialized_ledger, base_adapter, make_event
) -> None:
    first = append_event(initialized_ledger, base_adapter, make_event())
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            pilot_clip_id="G01D-CLIP-002",
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    manifest, entries = load_validated_ledger(initialized_ledger, base_adapter)
    before = (initialized_ledger / EVENTS_FILENAME).read_bytes()
    by_position = replay_entries(
        manifest, base_adapter, entries, through_position=1
    )
    by_hash = replay_entries(
        manifest, base_adapter, entries, through_entry_hash=first.entry_hash
    )
    assert by_position.to_dict() == by_hash.to_dict()
    assert by_position.to_dict()["through_position"] == 1
    assert (initialized_ledger / EVENTS_FILENAME).read_bytes() == before


def test_checkpoint_summarizes_preceding_prefix_and_verifies_completely(
    initialized_ledger, base_adapter, make_event
) -> None:
    append_event(initialized_ledger, base_adapter, make_event())
    manifest, prefix = load_validated_ledger(initialized_ledger, base_adapter)
    projection = replay_entries(manifest, base_adapter, prefix)
    payload = build_checkpoint_payload(projection, prefix)
    checkpoint = append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            EventType.CHECKPOINT_CREATED.value,
            payload=payload,
            precondition_projection_hash=projection.projection_hash,
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    manifest, entries = load_validated_ledger(initialized_ledger, base_adapter)
    through_checkpoint = replay_entries(
        manifest,
        base_adapter,
        entries,
        through_checkpoint_id=payload["checkpoint_id"],
    )
    assert through_checkpoint.to_dict()["through_position"] == checkpoint.position
    assert payload["prefix_position"] == 1
    assert payload["event_count"] == 1
    assert payload["projection_hash"] == projection.projection_hash


def test_incorrect_checkpoint_payload_is_no_write(
    initialized_ledger, base_adapter, make_event
) -> None:
    append_event(initialized_ledger, base_adapter, make_event())
    manifest, prefix = load_validated_ledger(initialized_ledger, base_adapter)
    projection = replay_entries(manifest, base_adapter, prefix)
    payload = build_checkpoint_payload(projection, prefix)
    payload["record_count"] = 29
    before = (initialized_ledger / EVENTS_FILENAME).read_bytes()
    try:
        append_event(
            initialized_ledger,
            base_adapter,
            make_event(
                EventType.CHECKPOINT_CREATED.value,
                payload=payload,
                precondition_projection_hash=projection.projection_hash,
                occurred_at="2026-08-07T00:00:02Z",
                recorded_at="2026-08-07T00:00:03Z",
            ),
        )
    except CheckpointError:
        pass
    else:
        raise AssertionError("invalid checkpoint was accepted")
    assert (initialized_ledger / EVENTS_FILENAME).read_bytes() == before
