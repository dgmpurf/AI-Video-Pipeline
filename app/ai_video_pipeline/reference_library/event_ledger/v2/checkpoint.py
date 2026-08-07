from __future__ import annotations

from typing import Any, Iterable, Mapping

from .canonical import canonical_sha256, require_exact_keys
from .enums import CHECKPOINT_SCHEMA_VERSION
from .errors import CheckpointError
from .models import LedgerEntry, ProjectionResult


CHECKPOINT_FIELDS = frozenset(
    {
        "checkpoint_schema_version",
        "checkpoint_id",
        "ledger_id",
        "base_v0_1_checkpoint_id",
        "base_v0_1_projection_hash",
        "through_position",
        "through_entry_hash",
        "ledger_prefix_hash",
        "projection_hash",
        "event_count",
        "state_counts",
        "validation_errors",
    }
)


def _body(
    projection: ProjectionResult, entries: Iterable[LedgerEntry]
) -> dict[str, Any]:
    selected = tuple(entries)
    state = projection.to_dict()
    if len(selected) != state["through_position"]:
        raise CheckpointError("checkpoint entry count differs from projection tail")
    return {
        "checkpoint_schema_version": CHECKPOINT_SCHEMA_VERSION,
        "ledger_id": state["ledger_id"],
        "base_v0_1_checkpoint_id": state["base_v0_1"]["base_v0_1_checkpoint_id"],
        "base_v0_1_projection_hash": state["base_v0_1"]["base_v0_1_projection_hash"],
        "through_position": state["through_position"],
        "through_entry_hash": state["through_entry_hash"],
        "ledger_prefix_hash": canonical_sha256(
            [entry.entry_hash for entry in selected]
        ),
        "projection_hash": projection.projection_hash,
        "event_count": state["event_count"],
        "state_counts": {
            "duplicate_evidence_history": len(state["duplicate_evidence_history"]),
            "pair_relation_history": len(state["pair_relation_history"]),
            "cluster_snapshot": len(state["cluster_snapshots"]),
            "cluster_confirmation_history": len(state["cluster_confirmation_history"]),
            "representative_proposal_history": len(state["representative_proposal_history"]),
            "representative_decision_history": len(state["representative_decision_history"]),
            "workflow_execution_receipt_history": len(state["workflow_execution_receipt_history"]),
        },
        "validation_errors": [],
    }


def build_checkpoint_payload(
    projection: ProjectionResult, entries: Iterable[LedgerEntry]
) -> dict[str, Any]:
    body = _body(projection, entries)
    return {"checkpoint_id": "RL2-CHK-" + canonical_sha256(body)[:24].upper(), **body}


def validate_checkpoint_payload(
    payload: Any,
    projection: ProjectionResult,
    entries: Iterable[LedgerEntry],
) -> None:
    if not isinstance(payload, dict):
        raise CheckpointError("checkpoint payload must be an object")
    try:
        require_exact_keys(payload, CHECKPOINT_FIELDS, field="checkpoint payload")
    except Exception as error:
        raise CheckpointError(str(error)) from error
    if payload != build_checkpoint_payload(projection, entries):
        raise CheckpointError("checkpoint payload does not match projection prefix")
