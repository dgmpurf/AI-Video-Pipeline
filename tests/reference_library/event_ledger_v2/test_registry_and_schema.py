import copy

import pytest

from app.ai_video_pipeline.reference_library.event_ledger.v2.enums import EventType
from app.ai_video_pipeline.reference_library.event_ledger.v2.errors import SchemaValidationError
from app.ai_video_pipeline.reference_library.event_ledger.v2.registry import EVENT_CONTRACTS
from app.ai_video_pipeline.reference_library.event_ledger.v2.schema import finalize_event


def test_closed_registry_has_exact_twelve_events():
    assert set(EVENT_CONTRACTS) == {event.value for event in EventType}
    assert len(EVENT_CONTRACTS) == 12


def test_unknown_payload_field_is_rejected(scenario):
    evidence = scenario.evidence().event.to_dict()
    draft = {key: value for key, value in evidence.items() if key not in {"event_id", "event_body_hash"}}
    draft = copy.deepcopy(draft)
    draft["payload"]["unknown"] = True
    with pytest.raises(SchemaValidationError):
        finalize_event(draft)


def test_ascii_unrevoked_contract_has_no_cyrillic_lookalike():
    contract = "human_decision_not_current_active_unrevoked_accept"
    assert "unrevoked" in contract
    assert "о" not in contract
