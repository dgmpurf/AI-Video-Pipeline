from __future__ import annotations

from types import MappingProxyType
from typing import Mapping

from .enums import AuthorityClass, EVENT_REGISTRY_VERSION, EventType
from .errors import AuthorityMismatchError, SchemaValidationError


_REGISTRY = {
    EventType.CHECKPOINT_CREATED.value: AuthorityClass.SYSTEM_PROJECTION.value,
    EventType.EXECUTION_AUDIT_RECORDED.value: AuthorityClass.EXTERNAL_EXECUTION_RECEIPT.value,
    EventType.HUMAN_DECISION_RECORDED.value: AuthorityClass.HUMAN_DECISION.value,
    EventType.RELATIONSHIP_ASSERTION_ADDED.value: AuthorityClass.OBSERVATION_ONLY.value,
    EventType.RELATIONSHIP_ASSERTION_RETRACTED.value: AuthorityClass.OBSERVATION_ONLY.value,
    EventType.REVIEW_OBSERVATION_ADDED.value: AuthorityClass.OBSERVATION_ONLY.value,
    EventType.REVIEW_OBSERVATION_CORRECTED.value: AuthorityClass.OBSERVATION_ONLY.value,
    EventType.RIGHTS_DECISION_RECORDED.value: AuthorityClass.HUMAN_DECISION.value,
    EventType.RIGHTS_EVIDENCE_ADDED.value: AuthorityClass.OBSERVATION_ONLY.value,
    EventType.SCORE_RECORD_ADDED.value: AuthorityClass.MODEL_PROPOSAL.value,
    EventType.SCORE_RECORD_SUPERSEDED.value: AuthorityClass.MODEL_PROPOSAL.value,
    EventType.STORAGE_PROPOSAL_ADDED.value: AuthorityClass.MODEL_PROPOSAL.value,
    EventType.STORAGE_PROPOSAL_SUPERSEDED.value: AuthorityClass.MODEL_PROPOSAL.value,
    EventType.TAXONOMY_SNAPSHOT_BOUND.value: AuthorityClass.OBSERVATION_ONLY.value,
}

EVENT_TYPE_REGISTRY: Mapping[str, str] = MappingProxyType(dict(sorted(_REGISTRY.items())))


def registry_document() -> dict[str, object]:
    return {
        "registry_version": EVENT_REGISTRY_VERSION,
        "events": dict(EVENT_TYPE_REGISTRY),
    }


def required_authority(event_type: str) -> str:
    try:
        return EVENT_TYPE_REGISTRY[event_type]
    except KeyError as error:
        raise SchemaValidationError(f"unknown event type: {event_type}") from error


def validate_registered_authority(event_type: str, authority_class: str) -> None:
    expected = required_authority(event_type)
    if authority_class != expected:
        raise AuthorityMismatchError(
            f"{event_type} requires {expected}, not {authority_class}"
        )
