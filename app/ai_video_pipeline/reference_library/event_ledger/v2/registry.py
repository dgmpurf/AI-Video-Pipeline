from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping

from .enums import AggregateType, AuthorityClass, EVENT_REGISTRY_VERSION, EventType
from .errors import AuthorityMismatchError, SchemaValidationError


@dataclass(frozen=True)
class EventContract:
    authority_class: str
    aggregate_types: tuple[str, ...]


_CONTRACTS = {
    EventType.DUPLICATE_EVIDENCE_ADDED.value: EventContract(
        AuthorityClass.OBSERVATION_ONLY.value,
        (AggregateType.PAIR.value, AggregateType.CLUSTER.value),
    ),
    EventType.DUPLICATE_EVIDENCE_RETRACTED.value: EventContract(
        AuthorityClass.OBSERVATION_ONLY.value,
        (AggregateType.PAIR.value, AggregateType.CLUSTER.value),
    ),
    EventType.PAIR_RELATION_PROPOSAL_ADDED.value: EventContract(
        AuthorityClass.MODEL_PROPOSAL.value, (AggregateType.PAIR.value,)
    ),
    EventType.PAIR_RELATION_DECISION_RECORDED.value: EventContract(
        AuthorityClass.HUMAN_DECISION.value, (AggregateType.PAIR.value,)
    ),
    EventType.CLUSTER_PROPOSAL_ADDED.value: EventContract(
        AuthorityClass.MODEL_PROPOSAL.value, (AggregateType.CLUSTER.value,)
    ),
    EventType.CLUSTER_CONFIRMATION_RECORDED.value: EventContract(
        AuthorityClass.HUMAN_DECISION.value, (AggregateType.CLUSTER.value,)
    ),
    EventType.CLUSTER_CONFIRMATION_RETRACTED.value: EventContract(
        AuthorityClass.HUMAN_DECISION.value, (AggregateType.CLUSTER.value,)
    ),
    EventType.REPRESENTATIVE_PROPOSAL_ADDED.value: EventContract(
        AuthorityClass.MODEL_PROPOSAL.value,
        (AggregateType.REPRESENTATIVE_WORKFLOW.value,),
    ),
    EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value: EventContract(
        AuthorityClass.MODEL_PROPOSAL.value,
        (AggregateType.REPRESENTATIVE_WORKFLOW.value,),
    ),
    EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value: EventContract(
        AuthorityClass.MODEL_PROPOSAL.value,
        (AggregateType.REPRESENTATIVE_WORKFLOW.value,),
    ),
    EventType.REPRESENTATIVE_DECISION_RECORDED.value: EventContract(
        AuthorityClass.HUMAN_DECISION.value,
        (AggregateType.REPRESENTATIVE_WORKFLOW.value,),
    ),
    EventType.WORKFLOW_EXECUTION_AUDIT_RECORDED.value: EventContract(
        AuthorityClass.EXTERNAL_EXECUTION_RECEIPT.value,
        (AggregateType.REPRESENTATIVE_WORKFLOW.value,),
    ),
}

EVENT_CONTRACTS: Mapping[str, EventContract] = MappingProxyType(
    dict(sorted(_CONTRACTS.items()))
)
EVENT_TYPE_REGISTRY: Mapping[str, str] = MappingProxyType(
    {key: contract.authority_class for key, contract in EVENT_CONTRACTS.items()}
)


def registry_document() -> dict[str, object]:
    return {
        "registry_version": EVENT_REGISTRY_VERSION,
        "event_count": len(EVENT_CONTRACTS),
        "events": {
            key: {
                "authority_class": contract.authority_class,
                "aggregate_types": list(contract.aggregate_types),
            }
            for key, contract in EVENT_CONTRACTS.items()
        },
    }


def event_contract(event_type: str) -> EventContract:
    try:
        return EVENT_CONTRACTS[event_type]
    except KeyError as error:
        raise SchemaValidationError(f"unknown event type: {event_type}") from error


def validate_registered_authority(
    event_type: str, authority_class: str, aggregate_type: str
) -> None:
    contract = event_contract(event_type)
    if authority_class != contract.authority_class:
        raise AuthorityMismatchError(
            f"{event_type} requires {contract.authority_class}, not {authority_class}"
        )
    if aggregate_type not in contract.aggregate_types:
        raise SchemaValidationError(
            f"{event_type} does not support aggregate type {aggregate_type}"
        )
