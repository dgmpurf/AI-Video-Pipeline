from __future__ import annotations

from typing import Any, Iterable, Mapping, Sequence

from app.ai_video_pipeline.reference_library.event_ledger.v2.enums import EventType
from app.ai_video_pipeline.reference_library.event_ledger.v2.models import (
    BaseV01Snapshot,
    LedgerEntry,
    ProjectionResult,
)

from .canonical import canonical_json_text
from .enums import (
    BUILD_MODE,
    BUILDER_CONTRACT_VERSION,
    LOGICAL_HASH_REGISTRY_VERSION,
    POINTER_SCHEMA_VERSION,
    READ_MODEL_SCHEMA_VERSION,
)
from .errors import MappingError
from .identity import materialization_generation_id
from .models import MappedReadModel
from .registry import LOGICAL_REGISTRY


def _json(value: Any) -> str:
    return canonical_json_text(value)


def _bool(value: Any) -> int:
    if value is True:
        return 1
    if value is False:
        return 0
    raise MappingError(f"expected boolean, got {value!r}")


def _truth_state(value: Any) -> str:
    if value is True or value == "TRUE":
        return "TRUE"
    if value is False or value == "FALSE":
        return "FALSE"
    if value == "UNKNOWN" or value is None:
        return "UNKNOWN"
    raise MappingError(f"invalid three-state value: {value!r}")


def _empty_rows() -> dict[str, list[tuple[Any, ...]]]:
    return {entry.table: [] for entry in LOGICAL_REGISTRY}


def _rl_p2_context(value: Mapping[str, Any] | None) -> tuple[Any, Any, Any]:
    if value is None:
        return None, None, None
    required = {
        "verified",
        "generation_filename",
        "materialization_generation_id",
        "logical_content_hash",
    }
    if set(value) != required or value["verified"] is not True:
        raise MappingError("RL-P2 context must be independently verified and exact")
    return (
        value["generation_filename"],
        value["materialization_generation_id"],
        value["logical_content_hash"],
    )


def _meta_row(
    base: BaseV01Snapshot,
    manifest: Mapping[str, Any],
    state: Mapping[str, Any],
    projection_hash: str,
    rl_p2_context: Mapping[str, Any] | None,
) -> tuple[tuple[Any, ...], str, dict[str, Any]]:
    catalog = base.base_catalog_identity
    rl_p2_filename, rl_p2_generation, rl_p2_hash = _rl_p2_context(rl_p2_context)
    checkpoint_id = state.get("current_checkpoint_id")
    if not isinstance(checkpoint_id, str) or not checkpoint_id:
        raise MappingError("RL-P3 materialization requires one accepted V0.2 checkpoint")
    identity = {
        "rl_p0_commit": catalog["rl_p0_commit"],
        "rl_p0_package_filename": catalog["package_filename"],
        "rl_p0_package_bytes": int(catalog["package_bytes"]),
        "rl_p0_package_sha256": catalog["package_sha256"],
        "rl_p0_record_schema_version": catalog["record_schema_version"],
        "rl_p0_record_count": int(catalog["record_count"]),
        **base.binding.to_dict(),
        "v0_2_ledger_id": manifest["ledger_id"],
        "v0_2_ledger_schema_version": manifest["ledger_schema_version"],
        "v0_2_event_schema_version": manifest["event_schema_version"],
        "v0_2_projection_schema_version": manifest["projection_schema_version"],
        "v0_2_checkpoint_id": checkpoint_id,
        "v0_2_through_position": int(state["through_position"]),
        "v0_2_through_entry_hash": state["through_entry_hash"],
        "v0_2_projection_hash": projection_hash,
        "rl_p2_context_generation_filename": rl_p2_filename,
        "rl_p2_context_generation_id": rl_p2_generation,
        "rl_p2_context_logical_hash": rl_p2_hash,
    }
    generation_id = materialization_generation_id(identity)
    row = (
        1,
        READ_MODEL_SCHEMA_VERSION,
        LOGICAL_HASH_REGISTRY_VERSION,
        POINTER_SCHEMA_VERSION,
        BUILDER_CONTRACT_VERSION,
        BUILD_MODE,
        identity["rl_p0_commit"],
        identity["rl_p0_package_filename"],
        identity["rl_p0_package_bytes"],
        identity["rl_p0_package_sha256"],
        identity["rl_p0_record_schema_version"],
        identity["rl_p0_record_count"],
        identity["base_v0_1_ledger_id"],
        identity["base_v0_1_checkpoint_id"],
        identity["base_v0_1_checkpoint_event_id"],
        identity["base_v0_1_through_position"],
        identity["base_v0_1_through_entry_hash"],
        identity["base_v0_1_projection_hash"],
        identity["v0_2_ledger_id"],
        identity["v0_2_ledger_schema_version"],
        identity["v0_2_event_schema_version"],
        identity["v0_2_projection_schema_version"],
        identity["v0_2_checkpoint_id"],
        identity["v0_2_through_position"],
        identity["v0_2_through_entry_hash"],
        identity["v0_2_projection_hash"],
        rl_p2_filename,
        rl_p2_generation,
        rl_p2_hash,
        generation_id,
        None,
    )
    return row, generation_id, identity


def _member_rows(
    rows: dict[str, list[tuple[Any, ...]]],
    state: Mapping[str, Any],
) -> None:
    for member_id in sorted(state["member_context"], key=lambda value: value.encode("utf-8")):
        value = state["member_context"][member_id]
        if value.get("member_id", member_id) != member_id:
            raise MappingError("member context key differs from member_id")
        rows["member_context_snapshot"].append(
            (
                member_id,
                value.get("pilot_clip_id"),
                value.get("record_id"),
                str(value.get("lifecycle", "UNKNOWN")),
                str(value.get("availability", "UNKNOWN")),
                str(value.get("rights_provenance", "UNKNOWN")),
                _truth_state(value.get("generation_input_allowed", "UNKNOWN")),
                _truth_state(value.get("publication_allowed", "UNKNOWN")),
                _json(value.get("artifact_context", {})),
                state["base_v0_1"]["base_v0_1_projection_hash"],
                int(state["through_position"]),
            )
        )


def _status(state: Mapping[str, Any], event_id: str) -> Mapping[str, Any]:
    try:
        return state["event_index"][event_id]
    except KeyError as error:
        raise MappingError(f"projection event index is missing {event_id}") from error


def _referenced_event(state: Mapping[str, Any], event_id: str) -> Mapping[str, Any]:
    return _status(state, event_id)["event"]


def _add_link(
    links: set[tuple[str, str, str, str, str, str]],
    *,
    from_domain: str,
    from_id: str,
    to_domain: str,
    to_id: str,
    link_type: str,
    source_event_id: str,
) -> None:
    links.add((from_domain, from_id, to_domain, to_id, link_type, source_event_id))


def _map_event(
    rows: dict[str, list[tuple[Any, ...]]],
    links: set[tuple[str, str, str, str, str, str]],
    manifest: Mapping[str, Any],
    entry: Mapping[str, Any],
    state: Mapping[str, Any],
) -> None:
    event = entry["event"]
    event_id = event["event_id"]
    event_type = event["event_type"]
    payload = event["payload"]
    status = _status(state, event_id)
    ledger_id = manifest["ledger_id"]
    position = int(entry["ledger_position"])
    common = (
        event_id,
        event["event_body_hash"],
        ledger_id,
        position,
    )
    source_json = _json(event["source_trace_ids"])
    payload_json = _json(payload)

    if event_type in {
        EventType.DUPLICATE_EVIDENCE_ADDED.value,
        EventType.DUPLICATE_EVIDENCE_RETRACTED.value,
    }:
        source_event = event
        if event_type == EventType.DUPLICATE_EVIDENCE_RETRACTED.value:
            source_event = _referenced_event(state, payload["evidence_event_id"])
        source_payload = source_event["payload"]
        rows["duplicate_evidence_history"].append(
            common
            + (
                source_payload["evidence_id"],
                source_payload.get("evidence_domain", "RETRACTION"),
                source_payload.get("evidence_kind", "RETRACTION"),
                source_payload.get("observation_state", "RETRACTED"),
                _bool(source_payload.get("technical_exact_equality", False)),
                _json(source_payload.get("measurement_trace_ids", [])),
                _json(source_payload.get("evidence_value", {})),
                _json(source_payload.get("limitations", [])),
                event["authority_class"],
                _bool(status["active"]),
                status["retracted_by_event_id"],
                source_json,
                payload_json,
            )
        )
        for member_id in source_payload.get("member_ids", source_event["target_member_ids"]):
            rows["duplicate_evidence_member"].append(
                (event_id, source_payload["evidence_id"], member_id)
            )
            _add_link(
                links,
                from_domain="DUPLICATE_EVIDENCE",
                from_id=event_id,
                to_domain="MEMBER",
                to_id=member_id,
                link_type="EVIDENCE_MEMBER",
                source_event_id=event_id,
            )
    elif event_type in {
        EventType.PAIR_RELATION_PROPOSAL_ADDED.value,
        EventType.PAIR_RELATION_DECISION_RECORDED.value,
    }:
        is_proposal = event_type == EventType.PAIR_RELATION_PROPOSAL_ADDED.value
        relation_id = (
            payload["pair_relation_proposal_id"]
            if is_proposal
            else payload["pair_decision_id"]
        )
        rows["pair_relation_history"].append(
            common
            + (
                "PROPOSAL" if is_proposal else "DECISION",
                relation_id,
                payload["pair_id"],
                payload["evidence_domain"],
                payload["member_ids"][0],
                payload["member_ids"][1],
                payload.get("proposed_relation"),
                payload.get("decision"),
                event["authority_class"],
                _bool(status["active"]),
                status["superseded_by_event_id"],
                status["retracted_by_event_id"],
                source_json,
                payload_json,
            )
        )
        if is_proposal:
            for evidence_event_id in payload["evidence_event_ids"]:
                evidence = _referenced_event(state, evidence_event_id)
                rows["pair_relation_evidence"].append(
                    (event_id, evidence_event_id, evidence["payload"]["evidence_id"])
                )
                _add_link(
                    links,
                    from_domain="PAIR_EVENT",
                    from_id=event_id,
                    to_domain="DUPLICATE_EVIDENCE",
                    to_id=evidence_event_id,
                    link_type="PAIR_EVIDENCE",
                    source_event_id=event_id,
                )
    elif event_type == EventType.CLUSTER_PROPOSAL_ADDED.value:
        if payload["cluster_snapshot_id"] not in {
            row[0] for row in rows["cluster_snapshot"]
        }:
            rows["cluster_snapshot"].append(
                (
                    payload["cluster_snapshot_id"],
                    payload["cluster_kind"],
                    len(payload["member_ids"]),
                    event_id,
                    payload["policy_id"],
                    payload["policy_version"],
                    event["precondition_v0_2_checkpoint_id"],
                    event["precondition_v0_2_projection_hash"],
                    _json(payload["member_ids"]),
                    position,
                    source_json,
                )
            )
            for ordinal, member_id in enumerate(payload["member_ids"], start=1):
                rows["cluster_member"].append(
                    (payload["cluster_snapshot_id"], member_id, ordinal)
                )
                _add_link(
                    links,
                    from_domain="CLUSTER_SNAPSHOT",
                    from_id=payload["cluster_snapshot_id"],
                    to_domain="MEMBER",
                    to_id=member_id,
                    link_type="CLUSTER_MEMBER",
                    source_event_id=event_id,
                )
    elif event_type in {
        EventType.CLUSTER_CONFIRMATION_RECORDED.value,
        EventType.CLUSTER_CONFIRMATION_RETRACTED.value,
    }:
        source_event = event
        if event_type == EventType.CLUSTER_CONFIRMATION_RETRACTED.value:
            source_event = _referenced_event(
                state, payload["cluster_confirmation_event_id"]
            )
        source_payload = source_event["payload"]
        basis = source_payload.get("basis_evidence", {"kind": "RETRACTED"})
        rows["cluster_confirmation_history"].append(
            common
            + (
                source_payload["cluster_confirmation_id"],
                source_payload["cluster_snapshot_id"],
                source_payload.get("cluster_kind", "RETRACTED"),
                source_payload.get("decision", "RETRACTED"),
                basis["kind"],
                basis.get("cluster_scope_decision_ref"),
                event["authority_class"],
                _bool(status["active"]),
                status["superseded_by_event_id"],
                status["retracted_by_event_id"],
                _json(payload.get("authorization_trace_ids", [])),
                source_json,
                payload_json,
            )
        )
        if event_type == EventType.CLUSTER_CONFIRMATION_RECORDED.value and basis["kind"] == "ALL_PAIR_HUMAN_CONFIRMED_SUPPORT":
            for pair_event_id in basis["pair_decision_event_ids"]:
                pair_event = _referenced_event(state, pair_event_id)
                pair_payload = pair_event["payload"]
                rows["cluster_confirmation_pair_support"].append(
                    (
                        event_id,
                        pair_event_id,
                        pair_payload["pair_id"],
                        pair_payload["member_ids"][0],
                        pair_payload["member_ids"][1],
                    )
                )
                _add_link(
                    links,
                    from_domain="CLUSTER_CONFIRMATION",
                    from_id=event_id,
                    to_domain="PAIR_DECISION",
                    to_id=pair_event_id,
                    link_type="ALL_PAIR_BASIS",
                    source_event_id=event_id,
                )
    elif event_type in {
        EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
        EventType.REPRESENTATIVE_PROPOSAL_SUPERSEDED.value,
        EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value,
    }:
        source_event = event
        if event_type == EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value:
            source_event = _referenced_event(
                state, payload["representative_proposal_event_id"]
            )
        source_payload = source_event["payload"]
        rows["representative_proposal_history"].append(
            common
            + (
                event_type,
                source_payload["representative_proposal_id"],
                source_payload["cluster_snapshot_id"],
                source_payload["representative_role"],
                source_payload.get("proposed_member_id", "UNKNOWN"),
                source_payload.get("policy_id", "UNKNOWN"),
                source_payload.get("policy_version", "UNKNOWN"),
                source_event.get("precondition_v0_2_checkpoint_id"),
                source_event.get("precondition_v0_2_projection_hash"),
                source_payload.get("prior_proposal_event_id"),
                _bool(status["current"]),
                _bool(status["active"]),
                status["superseded_by_event_id"],
                status["retracted_by_event_id"],
                _json(source_payload.get("ranking_facts", {})),
                _json(source_payload.get("rights_snapshot_refs", {})),
                _json(source_payload.get("lifecycle_snapshot_refs", {})),
                source_json,
                payload_json,
            )
        )
        if event_type != EventType.REPRESENTATIVE_PROPOSAL_RETRACTED.value:
            for ordinal, member_id in enumerate(source_payload["candidate_ids"], start=1):
                rows["representative_proposal_candidate"].append(
                    (
                        event_id,
                        member_id,
                        ordinal,
                        _bool(member_id == source_payload["proposed_member_id"]),
                    )
                )
                _add_link(
                    links,
                    from_domain="REPRESENTATIVE_PROPOSAL",
                    from_id=event_id,
                    to_domain="MEMBER",
                    to_id=member_id,
                    link_type="PROPOSAL_CANDIDATE",
                    source_event_id=event_id,
                )
    elif event_type == EventType.REPRESENTATIVE_DECISION_RECORDED.value:
        rows["representative_decision_history"].append(
            common
            + (
                payload["representative_decision_id"],
                payload["representative_proposal_event_id"],
                payload["representative_proposal_body_hash"],
                payload["cluster_snapshot_id"],
                payload["representative_role"],
                payload["proposed_member_id"],
                payload["decision"],
                event["authority_class"],
                _bool(status["current"]),
                _bool(status["active"]),
                status["superseded_by_event_id"],
                status["retracted_by_event_id"],
                payload["pinned_v0_2_checkpoint_id"],
                payload["pinned_v0_2_projection_hash"],
                _json(payload["authorization_trace_ids"]),
                source_json,
                payload_json,
            )
        )
        _add_link(
            links,
            from_domain="REPRESENTATIVE_DECISION",
            from_id=event_id,
            to_domain="REPRESENTATIVE_PROPOSAL",
            to_id=payload["representative_proposal_event_id"],
            link_type="DECISION_PROPOSAL",
            source_event_id=event_id,
        )
    elif event_type == EventType.WORKFLOW_EXECUTION_AUDIT_RECORDED.value:
        rows["workflow_execution_receipt_history"].append(
            common
            + (
                payload["operation_type"],
                payload["authorization_id"],
                payload["representative_decision_event_id"],
                payload["representative_decision_body_hash"],
                payload["representative_proposal_event_id"],
                payload["representative_proposal_body_hash"],
                payload["cluster_snapshot_id"],
                payload["representative_role"],
                _bool(payload["operation_success"]),
                int(payload["external_operation_count"]),
                _json(payload["before_identity"]),
                _json(payload["after_identity"]),
                _json(payload["receipt_trace_ids"]),
                source_json,
                payload_json,
            )
        )
        for domain, reference, link_type in (
            ("REPRESENTATIVE_DECISION", payload["representative_decision_event_id"], "RECEIPT_DECISION"),
            ("REPRESENTATIVE_PROPOSAL", payload["representative_proposal_event_id"], "RECEIPT_PROPOSAL"),
        ):
            _add_link(
                links,
                from_domain="WORKFLOW_EXECUTION_RECEIPT",
                from_id=event_id,
                to_domain=domain,
                to_id=reference,
                link_type=link_type,
                source_event_id=event_id,
            )
    else:
        raise MappingError(f"unregistered V0.2 event type: {event_type}")


def map_projection(
    base: BaseV01Snapshot,
    manifest: Mapping[str, Any],
    entries: Iterable[LedgerEntry],
    projection: ProjectionResult,
    *,
    rl_p2_context: Mapping[str, Any] | None = None,
) -> MappedReadModel:
    state = projection.to_dict()
    if state["base_v0_1"] != base.binding.to_dict():
        raise MappingError("projection base binding differs from validated V0.1 base")
    entry_values = tuple(entry.to_dict() for entry in entries)
    if len(entry_values) != int(state["event_count"]):
        raise MappingError("entry count differs from projection event count")
    if set(state["event_index"]) != {
        entry["event"]["event_id"] for entry in entry_values
    }:
        raise MappingError("projection event coverage differs from ledger")
    rows = _empty_rows()
    meta, generation_id, identity = _meta_row(
        base, manifest, state, projection.projection_hash, rl_p2_context
    )
    rows["read_model_meta"].append(meta)
    _member_rows(rows, state)
    links: set[tuple[str, str, str, str, str, str]] = set()
    for entry in entry_values:
        _map_event(rows, links, manifest, entry, state)
    rows["audit_link"].extend(sorted(links, key=lambda row: tuple(value.encode("utf-8") for value in row)))
    frozen = {name: tuple(values) for name, values in rows.items()}
    if set(frozen) != {entry.table for entry in LOGICAL_REGISTRY}:
        raise MappingError("mapped tables differ from the closed registry")
    return MappedReadModel(frozen, generation_id, identity)


def plan_scale_shape(
    record_count: int,
    candidate_edges: Sequence[tuple[str, str]],
    *,
    partition_size: int = 1000,
) -> dict[str, Any]:
    """Describe a deterministic explicit-edge-only scale shape without all-pairs work."""

    if isinstance(record_count, bool) or not isinstance(record_count, int) or record_count < 0:
        raise MappingError("record_count must be a nonnegative integer")
    if isinstance(partition_size, bool) or not isinstance(partition_size, int) or partition_size <= 0:
        raise MappingError("partition_size must be positive")
    normalized: list[tuple[str, str]] = []
    for edge in candidate_edges:
        if len(edge) != 2 or edge[0] == edge[1]:
            raise MappingError("candidate edge must contain two different members")
        normalized.append(tuple(sorted(edge, key=lambda value: value.encode("utf-8"))))
    normalized = sorted(set(normalized), key=lambda edge: (edge[0].encode("utf-8"), edge[1].encode("utf-8")))
    partitions = [
        {"start": start, "end": min(record_count, start + partition_size)}
        for start in range(0, record_count, partition_size)
    ]
    return {
        "record_count": record_count,
        "candidate_edge_count": len(normalized),
        "candidate_edges": [list(edge) for edge in normalized],
        "partition_size": partition_size,
        "partitions": partitions,
        "all_pairs_enumerated": False,
        "strategy": "EXPLICIT_BOUNDED_CANDIDATE_EDGES_ONLY",
    }
