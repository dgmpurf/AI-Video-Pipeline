from __future__ import annotations

import copy
from collections import Counter
from typing import Any, Iterable

from .canonical import canonical_sha256, require_exact_keys
from .enums import CHECKPOINT_SCHEMA_VERSION
from .errors import CheckpointError
from .models import LedgerEntry, ProjectionResult


CHECKPOINT_FIELDS = frozenset(
    {
        "checkpoint_schema_version",
        "checkpoint_id",
        "prefix_position",
        "prefix_entry_hash",
        "base_catalog_identity",
        "ledger_prefix_hash",
        "projection_hash",
        "record_count",
        "event_count",
        "technical_failure_count",
        "current_proxy_count",
        "current_proxy_bytes",
        "current_segment_count",
        "current_segment_bytes",
        "unknown_preservation_counts",
        "rights_distribution",
        "open_proposal_count",
        "human_decision_count",
        "execution_receipt_count",
        "media_operation_count",
        "validation_errors",
    }
)


def _count_unknown(value: Any) -> int:
    if value == "UNKNOWN":
        return 1
    if isinstance(value, dict):
        return sum(_count_unknown(child) for child in value.values())
    if isinstance(value, list):
        return sum(_count_unknown(child) for child in value)
    return 0


def _checkpoint_body(
    projection: ProjectionResult, entries: Iterable[LedgerEntry]
) -> dict[str, Any]:
    selected = tuple(entries)
    state = projection.to_dict()
    records = tuple(state["records"].values())
    rights_provenance = Counter(record["rights"]["rights_provenance"] for record in records)
    publication = Counter(str(record["rights"]["publication_allowed"]) for record in records)
    generation = Counter(
        str(record["rights"]["active_generation_input_allowed"]) for record in records
    )
    execution_receipts = [
        item
        for record in records
        for item in record["execution_receipts"]
    ]
    body: dict[str, Any] = {
        "checkpoint_schema_version": CHECKPOINT_SCHEMA_VERSION,
        "prefix_position": selected[-1].position if selected else 0,
        "prefix_entry_hash": selected[-1].entry_hash if selected else "0" * 64,
        "base_catalog_identity": copy.deepcopy(state["base_catalog"]),
        "ledger_prefix_hash": canonical_sha256(
            [entry.entry_hash for entry in selected]
        ),
        "projection_hash": projection.projection_hash,
        "record_count": len(records),
        "event_count": state["event_count"],
        "technical_failure_count": sum(
            item["payload"].get("operation_success") is False
            for item in execution_receipts
        ),
        "current_proxy_count": sum(
            record["artifact_storage"]["current_proxy_file_count"]
            for record in records
        ),
        "current_proxy_bytes": sum(
            record["artifact_storage"]["current_proxy_bytes"] for record in records
        ),
        "current_segment_count": sum(
            record["artifact_storage"]["current_segment_count"] for record in records
        ),
        "current_segment_bytes": sum(
            record["artifact_storage"]["current_segment_bytes"] for record in records
        ),
        "unknown_preservation_counts": {
            "total_unknown_values": sum(_count_unknown(record) for record in records)
        },
        "rights_distribution": {
            "rights_provenance": dict(sorted(rights_provenance.items())),
            "publication_allowed": dict(sorted(publication.items())),
            "active_generation_input_allowed": dict(sorted(generation.items())),
        },
        "open_proposal_count": sum(
            item["active"]
            for record in records
            for bucket in ("score_records", "storage_proposals")
            for item in record[bucket]
        ),
        "human_decision_count": sum(
            len(record["human_decisions"]) for record in records
        ),
        "execution_receipt_count": len(execution_receipts),
        "media_operation_count": sum(
            int(item["payload"].get("external_operation_count", 0))
            for item in execution_receipts
        ),
        "validation_errors": [],
    }
    return body


def build_checkpoint_payload(
    projection: ProjectionResult, entries: Iterable[LedgerEntry]
) -> dict[str, Any]:
    body = _checkpoint_body(projection, entries)
    checkpoint_id = "RL-CHK-" + canonical_sha256(body)[:24].upper()
    return {"checkpoint_id": checkpoint_id, **body}


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
    expected = build_checkpoint_payload(projection, entries)
    if payload != expected:
        raise CheckpointError("checkpoint payload does not match preceding prefix")
