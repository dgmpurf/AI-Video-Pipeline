from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping


@dataclass(frozen=True)
class RegistryEntry:
    table: str
    columns: tuple[str, ...]
    row_key: tuple[str, ...]
    role: str
    logical_export_exclude: tuple[str, ...] = ()

    @property
    def logical_columns(self) -> tuple[str, ...]:
        excluded = set(self.logical_export_exclude)
        return tuple(column for column in self.columns if column not in excluded)


def _entry(
    table: str,
    columns: str,
    row_key: str,
    role: str,
    *,
    exclude: str = "",
) -> RegistryEntry:
    return RegistryEntry(
        table,
        tuple(columns.split()),
        tuple(row_key.split()),
        role,
        tuple(exclude.split()) if exclude else (),
    )


LOGICAL_REGISTRY: tuple[RegistryEntry, ...] = (
    _entry(
        "read_model_meta",
        "meta_id read_model_schema_version logical_hash_registry_version pointer_schema_version builder_contract_version build_mode rl_p0_commit rl_p0_package_filename rl_p0_package_bytes rl_p0_package_sha256 rl_p0_record_schema_version rl_p0_record_count base_v0_1_ledger_id base_v0_1_checkpoint_id base_v0_1_checkpoint_event_id base_v0_1_through_position base_v0_1_through_entry_hash base_v0_1_projection_hash v0_2_ledger_id v0_2_ledger_schema_version v0_2_event_schema_version v0_2_projection_schema_version v0_2_checkpoint_id v0_2_through_position v0_2_through_entry_hash v0_2_projection_hash rl_p2_context_generation_filename rl_p2_context_generation_id rl_p2_context_logical_hash materialization_generation_id logical_content_hash",
        "meta_id",
        "VERSION_AND_UPSTREAM_IDENTITY",
        exclude="logical_content_hash",
    ),
    _entry(
        "member_context_snapshot",
        "member_id pilot_clip_id record_id lifecycle availability rights_provenance generation_input_allowed publication_allowed artifact_context_json source_projection_hash through_position",
        "member_id",
        "DERIVED_MEMBER_CONTEXT_NOT_AUTHORITY",
    ),
    _entry(
        "duplicate_evidence_history",
        "event_id event_body_hash ledger_id ledger_position evidence_id evidence_domain evidence_kind observation_state technical_exact_equality measurement_trace_ids_json evidence_value_json limitations_json authority_class active retracted_by_event_id source_trace_ids_json payload_json",
        "ledger_id ledger_position event_id",
        "GOVERNED_EVIDENCE_HISTORY",
    ),
    _entry(
        "duplicate_evidence_member",
        "evidence_event_id evidence_id member_id",
        "evidence_event_id member_id",
        "EVIDENCE_TO_MEMBER_LINK",
    ),
    _entry(
        "pair_relation_history",
        "event_id event_body_hash ledger_id ledger_position record_kind pair_relation_id pair_id evidence_domain member_a_id member_b_id proposed_relation decision authority_class active superseded_by_event_id retracted_by_event_id source_trace_ids_json payload_json",
        "ledger_id ledger_position event_id",
        "PAIR_PROPOSAL_AND_DECISION_HISTORY",
    ),
    _entry(
        "pair_relation_evidence",
        "pair_event_id evidence_event_id evidence_id",
        "pair_event_id evidence_event_id",
        "PAIR_TO_EVIDENCE_LINK",
    ),
    _entry(
        "cluster_snapshot",
        "cluster_snapshot_id cluster_kind member_count proposal_event_id policy_id policy_version pinned_checkpoint_id pinned_projection_hash canonical_member_ids_json created_ledger_position source_trace_ids_json",
        "cluster_snapshot_id",
        "IMMUTABLE_CLUSTER_SNAPSHOT",
    ),
    _entry(
        "cluster_member",
        "cluster_snapshot_id member_id member_ordinal",
        "cluster_snapshot_id member_ordinal member_id",
        "IMMUTABLE_CLUSTER_MEMBERSHIP",
    ),
    _entry(
        "cluster_confirmation_history",
        "event_id event_body_hash ledger_id ledger_position cluster_confirmation_id cluster_snapshot_id cluster_kind decision confirmation_basis cluster_scope_decision_ref authority_class active superseded_by_event_id retracted_by_event_id authorization_trace_ids_json source_trace_ids_json payload_json",
        "ledger_id ledger_position event_id",
        "E1_CLUSTER_SCOPE_CONFIRMATION_HISTORY",
    ),
    _entry(
        "cluster_confirmation_pair_support",
        "confirmation_event_id pair_decision_event_id pair_id member_a_id member_b_id",
        "confirmation_event_id pair_id pair_decision_event_id",
        "ALL_PAIR_BASIS_PROVENANCE_ONLY",
    ),
    _entry(
        "representative_proposal_history",
        "event_id event_body_hash ledger_id ledger_position proposal_kind representative_proposal_id cluster_snapshot_id representative_role proposed_member_id policy_id policy_version pinned_checkpoint_id pinned_projection_hash prior_proposal_event_id current active superseded_by_event_id retracted_by_event_id ranking_facts_json rights_snapshot_refs_json lifecycle_snapshot_refs_json source_trace_ids_json payload_json",
        "ledger_id ledger_position event_id",
        "ROLE_SPECIFIC_PROPOSAL_HISTORY",
    ),
    _entry(
        "representative_proposal_candidate",
        "proposal_event_id candidate_member_id candidate_ordinal is_proposed_member",
        "proposal_event_id candidate_ordinal candidate_member_id",
        "PROPOSAL_CANDIDATE_AND_RANKING_FACTS",
    ),
    _entry(
        "representative_decision_history",
        "event_id event_body_hash ledger_id ledger_position representative_decision_id representative_proposal_event_id representative_proposal_body_hash cluster_snapshot_id representative_role proposed_member_id decision authority_class current active superseded_by_event_id retracted_by_event_id pinned_checkpoint_id pinned_projection_hash authorization_trace_ids_json source_trace_ids_json payload_json",
        "ledger_id ledger_position event_id",
        "HUMAN_REPRESENTATIVE_DECISION_HISTORY",
    ),
    _entry(
        "workflow_execution_receipt_history",
        "event_id event_body_hash ledger_id ledger_position operation_type authorization_id representative_decision_event_id representative_decision_body_hash representative_proposal_event_id representative_proposal_body_hash cluster_snapshot_id representative_role operation_success external_operation_count before_identity_json after_identity_json receipt_trace_ids_json source_trace_ids_json payload_json",
        "ledger_id ledger_position event_id",
        "EXTERNAL_RECEIPT_HISTORY_ONLY",
    ),
    _entry(
        "audit_link",
        "from_domain from_id to_domain to_id link_type source_event_id",
        "from_domain from_id to_domain to_id link_type source_event_id",
        "DETERMINISTIC_CROSS_DOMAIN_TRACEABILITY",
    ),
)

LOGICAL_TABLE_NAMES = tuple(entry.table for entry in LOGICAL_REGISTRY)
REGISTRY_BY_TABLE: Mapping[str, RegistryEntry] = MappingProxyType(
    {entry.table: entry for entry in LOGICAL_REGISTRY}
)


def registry_document() -> dict[str, object]:
    return {
        "registry_closed": True,
        "logical_table_count": len(LOGICAL_REGISTRY),
        "fts_table_count": 0,
        "tables": [
            {
                "table": entry.table,
                "columns": list(entry.columns),
                "logical_export_columns_exclude": list(entry.logical_export_exclude),
                "row_key": list(entry.row_key),
                "role": entry.role,
            }
            for entry in LOGICAL_REGISTRY
        ],
    }
