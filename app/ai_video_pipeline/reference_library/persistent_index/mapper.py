from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping

from app.ai_video_pipeline.reference_library.event_ledger.models import (
    BaseCatalogAdapter,
    LedgerEntry,
    ProjectionResult,
)

from .enums import (
    BUILD_MODE,
    BUILDER_CONTRACT_VERSION,
    LOGICAL_HASH_REGISTRY_VERSION,
    READ_MODEL_SCHEMA_VERSION,
    TOKENIZER_CONTRACT_VERSION,
)
from .errors import MappingError
from .identity import (
    LOGICAL_REGISTRY,
    canonical_json_text,
    materialization_generation_id,
    sha256_hex,
)
from .tokenize import prepare_document


EXPECTED_BUCKETS = frozenset(
    {
        "base_record_id", "artifact_storage", "review_observations",
        "score_records", "storage_proposals", "human_decisions",
        "execution_receipts", "relationship_assertions", "rights_evidence",
        "rights_decisions", "taxonomy_bindings", "rights",
    }
)


@dataclass(frozen=True)
class MappedReadModel:
    rows: Mapping[str, tuple[tuple[Any, ...], ...]]
    materialization_generation_id: str

    def table(self, name: str) -> tuple[tuple[Any, ...], ...]:
        try:
            return self.rows[name]
        except KeyError as error:
            raise MappingError(f"unknown mapped table: {name}") from error


def _json(value: Any) -> str:
    return canonical_json_text(value)


def _bool(value: Any) -> int:
    if value is True:
        return 1
    if value is False:
        return 0
    raise MappingError(f"expected a boolean, got {value!r}")


def _publication(value: Any) -> str:
    if value is True or value == "TRUE":
        return "TRUE"
    if value is False or value == "FALSE":
        return "FALSE"
    if value == "UNKNOWN":
        return "UNKNOWN"
    raise MappingError(f"invalid publication rights value: {value!r}")


def _empty_rows() -> dict[str, list[tuple[Any, ...]]]:
    return {entry.table: [] for entry in LOGICAL_REGISTRY}


def _checkpoint_id(state: Mapping[str, Any]) -> str | None:
    values = state.get("checkpoints", {})
    if not values:
        return None
    return max(values, key=lambda key: int(values[key]["ledger_position"]))


def _meta_values(
    adapter: BaseCatalogAdapter,
    manifest: Mapping[str, Any],
    state: Mapping[str, Any],
    projection_hash: str,
    builder_source_identity: str,
) -> tuple[tuple[Any, ...], str]:
    binding = adapter.binding
    identity = {
        "builder_source_identity": builder_source_identity,
        "rl_p0_commit": binding.rl_p0_commit,
        "rl_p0_package_filename": binding.package_filename,
        "rl_p0_package_bytes": binding.package_bytes,
        "rl_p0_package_sha256": binding.package_sha256,
        "rl_p0_record_schema_version": binding.record_schema_version,
        "rl_p0_record_count": binding.record_count,
        "base_catalog_hash": binding.base_catalog_hash,
        "ledger_id": manifest["ledger_id"],
        "ledger_schema_version": manifest["ledger_schema_version"],
        "event_schema_version": manifest["event_schema_version"],
        "projection_schema_version": manifest["projection_schema_version"],
        "through_position": int(state["through_position"]),
        "through_entry_hash": state["through_entry_hash"],
        "projection_hash": projection_hash,
        "checkpoint_id": _checkpoint_id(state),
        "tokenizer_contract_version": TOKENIZER_CONTRACT_VERSION,
        "build_mode": BUILD_MODE,
    }
    generation_id = materialization_generation_id(identity)
    row = (
        1, READ_MODEL_SCHEMA_VERSION, LOGICAL_HASH_REGISTRY_VERSION,
        BUILDER_CONTRACT_VERSION, builder_source_identity, binding.rl_p0_commit,
        binding.package_filename, binding.package_bytes, binding.package_sha256,
        binding.record_schema_version, binding.record_count, binding.base_catalog_hash,
        manifest["ledger_id"], manifest["ledger_schema_version"],
        manifest["event_schema_version"], manifest["projection_schema_version"],
        int(state["through_position"]), state["through_entry_hash"], projection_hash,
        identity["checkpoint_id"], TOKENIZER_CONTRACT_VERSION, BUILD_MODE, generation_id,
    )
    return row, generation_id


def _map_base_record(
    rows: dict[str, list[tuple[Any, ...]]],
    record: Mapping[str, Any],
    projected: Mapping[str, Any],
    through_position: int,
) -> None:
    identity = record["record_identity"]
    pilot = str(identity["pilot_clip_id"])
    if set(projected) != EXPECTED_BUCKETS:
        raise MappingError(f"projection bucket set differs for {pilot}")
    content = record["content"]
    profile = record["reference_profile"]
    canonical_record = _json(record)
    rows["reference_record"].append(
        (
            pilot, str(identity["record_id"]), str(identity["schema_version"]),
            str(identity["record_revision"]), str(content["content_family"]["primary"]),
            str(content["content_scope"]), str(content["plain_language_description"]),
            str(profile["reference_taxonomy_status"]), canonical_record,
            sha256_hex(canonical_record.encode("utf-8")),
        )
    )
    for duty in profile["reference_duties"]:
        rows["reference_duty"].append((pilot, str(duty)))
    for extension in profile["reference_duty_extensions"]:
        rows["reference_duty_extension"].append(
            (pilot, str(extension), str(profile["reference_taxonomy_status"]))
        )
    for artifact in record["artifacts"]:
        rows["artifact"].append(
            (
                str(artifact["artifact_id"]), pilot, str(artifact["artifact_type"]),
                str(artifact["tier"]), str(artifact["artifact_role"]),
                str(artifact["technical_validation_status"]),
                str(artifact["artifact_availability"]), str(artifact["artifact_lifecycle"]),
                int(artifact["artifact_bytes"]), str(artifact["sha256"]),
                str(artifact["sha256_status"]), _json(artifact["execution_history"]),
            )
        )
    storage = projected["artifact_storage"]
    current_total = int(storage["current_total_derived_media_bytes"])
    if current_total != int(storage["current_proxy_bytes"]) + int(storage["current_segment_bytes"]):
        raise MappingError(f"storage arithmetic differs for {pilot}")
    rows["artifact_storage_current"].append(
        (
            pilot, int(storage["current_proxy_file_count"]), int(storage["current_proxy_bytes"]),
            int(storage["current_segment_count"]), int(storage["current_segment_bytes"]),
            current_total, int(storage["historical_deleted_bytes"]),
            str(storage["arithmetic_status"]), _json(storage["artifact_bytes_by_tier"]),
            _json(storage["segment_bytes_by_id"]),
        )
    )
    rights = projected["rights"]
    rights_decisions = projected["rights_decisions"]
    source_decision = rights_decisions[-1]["event_id"] if rights_decisions else "RL_P0_BASE"
    rows["rights_current"].append(
        (
            pilot, str(rights["rights_provenance"]),
            _bool(rights["active_generation_input_allowed"]),
            _publication(rights["publication_allowed"]), source_decision,
            int(through_position),
        )
    )
    taxonomy = " ".join(
        [str(content["content_family"]["primary"])]
        + [str(value) for value in content["content_family"].get("secondary", [])]
    )
    duties = " ".join(str(value) for value in profile["reference_duties"])
    notes_values = record.get("human_gate_reasons", [])
    notes = " ".join(str(value) for value in notes_values)
    description = str(content["plain_language_description"])
    observation = str(record.get("review_observation", {}).get("statement", ""))
    prepared = prepare_document(
        " ".join((description, observation, taxonomy, duties, notes))
    )
    rows["search_document"].append(
        (
            f"record:{pilot}:description", pilot, "BASE_RECORD", "RL_P0_BASE",
            "CURRENT", "RL_P0_BASE", description, observation, taxonomy, duties, notes,
            prepared, "$.content.plain_language_description", int(through_position),
        )
    )


def _event_common(
    manifest: Mapping[str, Any],
    entry: Mapping[str, Any],
    state: Mapping[str, Any],
) -> dict[str, Any]:
    event = entry["event"]
    indexed = state["event_index"][event["event_id"]]
    return {
        "event": event,
        "event_id": event["event_id"],
        "ledger_id": manifest["ledger_id"],
        "position": int(entry["ledger_position"]),
        "pilot": event["pilot_clip_id"],
        "event_type": event["event_type"],
        "authority": event["authority_class"],
        "payload": event["payload"],
        "payload_json": _json(event["payload"]),
        "source_json": _json(event["source_trace_ids"]),
        "active": _bool(indexed["active"]),
        "superseded": indexed["superseded_by"],
        "retracted": indexed["retracted_by"],
    }


def _map_event(
    rows: dict[str, list[tuple[Any, ...]]],
    manifest: Mapping[str, Any],
    entry: Mapping[str, Any],
    state: Mapping[str, Any],
) -> None:
    common = _event_common(manifest, entry, state)
    event = common["event"]
    payload = common["payload"]
    prefix = (
        common["event_id"], common["ledger_id"], common["position"], common["pilot"],
        common["event_type"], common["authority"],
    )
    suffix = (common["source_json"], common["payload_json"])
    event_type = common["event_type"]
    if event_type in {"REVIEW_OBSERVATION_ADDED", "REVIEW_OBSERVATION_CORRECTED"}:
        rows["review_observation_history"].append(
            prefix + (
                payload.get("observation_type"), payload.get("statement"), common["active"],
                common["superseded"], common["retracted"],
            ) + suffix
        )
        statement = str(payload.get("statement", ""))
        active_state = "CURRENT" if common["active"] else "HISTORY"
        rows["search_document"].append(
            (
                f"event:{common['event_id']}:observation", common["pilot"],
                "REVIEW_OBSERVATION", common["event_id"], active_state,
                common["authority"], "", statement, "", "", "",
                prepare_document(statement), "$.payload.statement", common["position"],
            )
        )
    elif event_type in {"SCORE_RECORD_ADDED", "SCORE_RECORD_SUPERSEDED"}:
        rows["score_record_history"].append(
            prefix + (
                payload.get("score_name"),
                _json(payload["score_value"]) if "score_value" in payload else None,
                _bool(payload.get("score_is_decision_gate", False)), common["active"],
                common["superseded"], common["retracted"],
            ) + suffix
        )
    elif event_type in {"STORAGE_PROPOSAL_ADDED", "STORAGE_PROPOSAL_SUPERSEDED"}:
        rows["storage_proposal_history"].append(
            prefix + (
                payload.get("proposal_id"), payload.get("action"),
                _bool(payload.get("executed", False)), common["active"],
                common["superseded"], common["retracted"],
            ) + suffix
        )
    elif event_type == "HUMAN_DECISION_RECORDED":
        proposals = payload.get("proposal_event_ids", [])
        rows["human_decision_history"].append(
            prefix + (
                payload["decision_domain"], payload["decision"], payload["reason"],
                _json(payload["authorization_trace_ids"]), _json(proposals),
            ) + suffix
        )
        rows["human_decision_proposal"].extend(
            (common["event_id"], str(proposal)) for proposal in proposals
        )
    elif event_type == "EXECUTION_AUDIT_RECORDED":
        decisions = payload.get("decision_event_ids", [])
        rows["execution_receipt_history"].append(
            prefix + (
                payload["operation_type"], payload["authorization_id"],
                _bool(payload["operation_success"]), int(payload["external_operation_count"]),
                _json(payload["before_identity"]), _json(payload["after_identity"]),
                _json(payload["receipt_trace_ids"]),
            ) + suffix
        )
        rows["execution_receipt_decision"].extend(
            (common["event_id"], str(decision)) for decision in decisions
        )
    elif event_type in {"RELATIONSHIP_ASSERTION_ADDED", "RELATIONSHIP_ASSERTION_RETRACTED"}:
        rows["relationship_assertion_history"].append(
            prefix + (
                _json(payload["possible_same_family"]) if "possible_same_family" in payload else None,
                _json(payload["possible_upstream_overlap"]) if "possible_upstream_overlap" in payload else None,
                payload.get("exact_duplicate_status"), common["active"], common["retracted"],
            ) + suffix
        )
        rows["relationship_target"].extend(
            (common["event_id"], str(target)) for target in event["target_ids"]
            if target in state["records"]
        )
    elif event_type == "RIGHTS_EVIDENCE_ADDED":
        rows["rights_evidence_history"].append(
            prefix + (payload.get("evidence_type"), payload.get("statement")) + suffix
        )
    elif event_type == "RIGHTS_DECISION_RECORDED":
        changes = payload["rights_changes"]
        evidence = payload.get("evidence_event_ids", [])
        generation_change = changes.get("active_generation_input_allowed")
        publication_change = changes.get("publication_allowed")
        rows["rights_decision_history"].append(
            prefix + (
                payload["reason"], _json(payload["authorization_trace_ids"]), _json(changes),
                None if generation_change is None else _bool(generation_change),
                None if publication_change is None else _publication(publication_change),
            ) + suffix
        )
        rows["rights_decision_evidence"].extend(
            (common["event_id"], str(item)) for item in evidence
        )
    elif event_type == "TAXONOMY_SNAPSHOT_BOUND":
        rows["taxonomy_binding_history"].append(
            prefix + (payload["taxonomy_snapshot_id"], payload["taxonomy_version"]) + suffix
        )
        taxonomy_text = f"{payload['taxonomy_snapshot_id']} {payload['taxonomy_version']}"
        bindings = state["records"][common["pilot"]]["taxonomy_bindings"]
        active_state = (
            "CURRENT"
            if bindings and bindings[-1]["event_id"] == common["event_id"]
            else "HISTORY"
        )
        rows["search_document"].append(
            (
                f"event:{common['event_id']}:taxonomy", common["pilot"], "TAXONOMY_BINDING",
                common["event_id"], active_state, common["authority"], "", "", taxonomy_text,
                "", "", prepare_document(taxonomy_text), "$.payload", common["position"],
            )
        )
    elif event_type == "CHECKPOINT_CREATED":
        rows["checkpoint_history"].append(
            (
                payload["checkpoint_id"], common["event_id"], common["ledger_id"],
                common["position"], int(payload["prefix_position"]), payload["prefix_entry_hash"],
                payload["ledger_prefix_hash"], payload["projection_hash"],
                _json(payload["base_catalog_identity"]), int(payload["record_count"]),
                int(payload["event_count"]), _json(payload["unknown_preservation_counts"]),
                _json(payload["rights_distribution"]), int(payload["open_proposal_count"]),
                int(payload["human_decision_count"]), int(payload["execution_receipt_count"]),
                int(payload["media_operation_count"]), _json(payload["validation_errors"]),
                common["source_json"], common["payload_json"],
            )
        )
    else:
        raise MappingError(f"unregistered projection event type: {event_type}")
    actor = event["actor"]
    rows["ledger_event_provenance"].append(
        (
            common["event_id"], common["ledger_id"], common["position"], event["event_body_hash"],
            entry["previous_entry_hash"], entry["entry_hash"], event_type, common["authority"],
            common["pilot"], actor.get("actor_type"), actor.get("actor_id"),
            event.get("occurred_at"), event.get("recorded_at"), _json(event["target_ids"]),
            common["source_json"], _json(event["supersedes_event_ids"]),
            _json(event["retracts_event_ids"]),
            _json(
                {
                    "checkpoint_id": event.get("precondition_checkpoint_id"),
                    "projection_hash": event.get("precondition_projection_hash"),
                }
            ),
            common["payload_json"],
        )
    )


def map_projection(
    adapter: BaseCatalogAdapter,
    manifest: Mapping[str, Any],
    entries: Iterable[LedgerEntry],
    projection: ProjectionResult,
    *,
    builder_source_identity: str,
) -> MappedReadModel:
    state = projection.to_dict()
    if state["base_catalog"] != adapter.binding.to_dict():
        raise MappingError("projection base binding differs from the accepted catalog")
    base_records = adapter.records
    if len(base_records) != adapter.binding.record_count:
        raise MappingError("base record count differs from its binding")
    if set(state["records"]) != {
        str(record["record_identity"]["pilot_clip_id"]) for record in base_records
    }:
        raise MappingError("projection record coverage differs from the base catalog")
    rows = _empty_rows()
    meta, generation_id = _meta_values(
        adapter, manifest, state, projection.projection_hash, builder_source_identity
    )
    rows["read_model_meta"].append(meta)
    for record in base_records:
        pilot = str(record["record_identity"]["pilot_clip_id"])
        _map_base_record(rows, record, state["records"][pilot], int(state["through_position"]))
    entry_values = tuple(entry.to_dict() for entry in entries)
    if len(entry_values) != int(state["event_count"]):
        raise MappingError("entry count differs from projection event count")
    for entry in entry_values:
        _map_event(rows, manifest, entry, state)
    frozen = {name: tuple(values) for name, values in rows.items()}
    if set(frozen) != {entry.table for entry in LOGICAL_REGISTRY}:
        raise MappingError("mapped tables differ from the closed registry")
    return MappedReadModel(frozen, generation_id)
