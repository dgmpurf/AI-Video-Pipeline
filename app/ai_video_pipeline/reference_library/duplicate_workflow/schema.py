from __future__ import annotations

import sqlite3
from collections.abc import Iterable, Mapping
from typing import Any

from .enums import (
    BUILD_MODE,
    BUILDER_CONTRACT_VERSION,
    LOGICAL_HASH_REGISTRY_VERSION,
    POINTER_SCHEMA_VERSION,
    READ_MODEL_SCHEMA_VERSION,
)
from .errors import SchemaError
from .registry import LOGICAL_REGISTRY


INTEGER_COLUMNS = frozenset(
    {
        "meta_id", "rl_p0_package_bytes", "rl_p0_record_count",
        "base_v0_1_through_position", "v0_2_through_position", "through_position",
        "ledger_position", "technical_exact_equality", "active", "current",
        "member_count", "member_ordinal", "created_ledger_position",
        "candidate_ordinal", "is_proposed_member", "operation_success",
        "external_operation_count",
    }
)

NULLABLE_COLUMNS = frozenset(
    {
        "logical_content_hash", "rl_p2_context_generation_filename",
        "rl_p2_context_generation_id", "rl_p2_context_logical_hash",
        "pilot_clip_id", "record_id", "retracted_by_event_id",
        "superseded_by_event_id", "proposed_relation", "decision",
        "cluster_scope_decision_ref", "prior_proposal_event_id",
    }
)

TABLE_CONSTRAINTS: Mapping[str, tuple[str, ...]] = {
    "read_model_meta": (
        "CHECK(meta_id=1)",
        f"CHECK(read_model_schema_version='{READ_MODEL_SCHEMA_VERSION}')",
        f"CHECK(logical_hash_registry_version='{LOGICAL_HASH_REGISTRY_VERSION}')",
        f"CHECK(pointer_schema_version='{POINTER_SCHEMA_VERSION}')",
        f"CHECK(builder_contract_version='{BUILDER_CONTRACT_VERSION}')",
        f"CHECK(build_mode='{BUILD_MODE}')",
    ),
    "duplicate_evidence_history": (
        "CHECK(technical_exact_equality IN (0,1))",
        "CHECK(active IN (0,1))",
    ),
    "pair_relation_history": ("CHECK(active IN (0,1))",),
    "cluster_snapshot": ("CHECK(member_count>=2)",),
    "cluster_member": ("CHECK(member_ordinal>=1)",),
    "cluster_confirmation_history": ("CHECK(active IN (0,1))",),
    "representative_proposal_history": (
        "CHECK(current IN (0,1))", "CHECK(active IN (0,1))",
    ),
    "representative_proposal_candidate": (
        "CHECK(candidate_ordinal>=1)", "CHECK(is_proposed_member IN (0,1))",
    ),
    "representative_decision_history": (
        "CHECK(current IN (0,1))", "CHECK(active IN (0,1))",
    ),
    "workflow_execution_receipt_history": (
        "CHECK(operation_success IN (0,1))", "CHECK(external_operation_count>=0)",
    ),
}

FOREIGN_KEYS: Mapping[str, tuple[str, ...]] = {
    "duplicate_evidence_member": (
        "FOREIGN KEY(evidence_event_id) REFERENCES duplicate_evidence_history(event_id)",
        "FOREIGN KEY(member_id) REFERENCES member_context_snapshot(member_id)",
    ),
    "pair_relation_evidence": (
        "FOREIGN KEY(pair_event_id) REFERENCES pair_relation_history(event_id)",
        "FOREIGN KEY(evidence_event_id) REFERENCES duplicate_evidence_history(event_id)",
    ),
    "cluster_member": (
        "FOREIGN KEY(cluster_snapshot_id) REFERENCES cluster_snapshot(cluster_snapshot_id)",
        "FOREIGN KEY(member_id) REFERENCES member_context_snapshot(member_id)",
    ),
    "cluster_confirmation_history": (
        "FOREIGN KEY(cluster_snapshot_id) REFERENCES cluster_snapshot(cluster_snapshot_id)",
    ),
    "cluster_confirmation_pair_support": (
        "FOREIGN KEY(confirmation_event_id) REFERENCES cluster_confirmation_history(event_id)",
        "FOREIGN KEY(pair_decision_event_id) REFERENCES pair_relation_history(event_id)",
    ),
    "representative_proposal_history": (
        "FOREIGN KEY(cluster_snapshot_id) REFERENCES cluster_snapshot(cluster_snapshot_id)",
        "FOREIGN KEY(proposed_member_id) REFERENCES member_context_snapshot(member_id)",
    ),
    "representative_proposal_candidate": (
        "FOREIGN KEY(proposal_event_id) REFERENCES representative_proposal_history(event_id)",
        "FOREIGN KEY(candidate_member_id) REFERENCES member_context_snapshot(member_id)",
    ),
    "representative_decision_history": (
        "FOREIGN KEY(representative_proposal_event_id) REFERENCES representative_proposal_history(event_id)",
    ),
    "workflow_execution_receipt_history": (
        "FOREIGN KEY(representative_decision_event_id) REFERENCES representative_decision_history(event_id)",
        "FOREIGN KEY(representative_proposal_event_id) REFERENCES representative_proposal_history(event_id)",
    ),
}

INDEX_STATEMENTS = (
    "CREATE UNIQUE INDEX ux_evidence_event_id ON duplicate_evidence_history(event_id)",
    "CREATE UNIQUE INDEX ux_pair_event_id ON pair_relation_history(event_id)",
    "CREATE UNIQUE INDEX ux_cluster_confirmation_event_id ON cluster_confirmation_history(event_id)",
    "CREATE UNIQUE INDEX ux_representative_proposal_event_id ON representative_proposal_history(event_id)",
    "CREATE UNIQUE INDEX ux_representative_decision_event_id ON representative_decision_history(event_id)",
    "CREATE INDEX ix_evidence_id ON duplicate_evidence_history(evidence_id,ledger_position)",
    "CREATE INDEX ix_pair_id ON pair_relation_history(pair_id,active,ledger_position)",
    "CREATE INDEX ix_cluster_confirmation ON cluster_confirmation_history(cluster_snapshot_id,active,ledger_position)",
    "CREATE INDEX ix_representative_proposal ON representative_proposal_history(cluster_snapshot_id,representative_role,current,active,ledger_position)",
    "CREATE INDEX ix_representative_decision ON representative_decision_history(cluster_snapshot_id,representative_role,current,active,ledger_position)",
    "CREATE INDEX ix_receipt_decision ON workflow_execution_receipt_history(representative_decision_event_id,ledger_position)",
)


def _column_sql(name: str, *, inline_primary: bool) -> str:
    affinity = "INTEGER" if name in INTEGER_COLUMNS else "TEXT COLLATE BINARY"
    parts = [f'"{name}"', affinity]
    if name not in NULLABLE_COLUMNS:
        parts.append("NOT NULL")
    if inline_primary:
        parts.append("PRIMARY KEY")
    return " ".join(parts)


def create_schema(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA foreign_keys=ON")
    connection.execute("PRAGMA journal_mode=DELETE")
    connection.execute("PRAGMA synchronous=FULL")
    for entry in LOGICAL_REGISTRY:
        inline = len(entry.row_key) == 1
        definitions = [
            _column_sql(column, inline_primary=inline and column == entry.row_key[0])
            for column in entry.columns
        ]
        if len(entry.row_key) > 1:
            definitions.append(
                "PRIMARY KEY(" + ",".join(f'"{column}"' for column in entry.row_key) + ")"
            )
        definitions.extend(TABLE_CONSTRAINTS.get(entry.table, ()))
        definitions.extend(FOREIGN_KEYS.get(entry.table, ()))
        connection.execute(
            f'CREATE TABLE "{entry.table}" (' + ",".join(definitions) + ")"
        )
    for statement in INDEX_STATEMENTS:
        connection.execute(statement)


def insert_rows(
    connection: sqlite3.Connection,
    rows: Mapping[str, Iterable[tuple[Any, ...]]],
) -> None:
    expected = {entry.table for entry in LOGICAL_REGISTRY}
    if set(rows) != expected:
        raise SchemaError("mapped table set differs from the closed logical registry")
    for entry in LOGICAL_REGISTRY:
        values = list(rows[entry.table])
        if any(len(row) != len(entry.columns) for row in values):
            raise SchemaError(f"mapped row width differs for {entry.table}")
        placeholders = ",".join("?" for _ in entry.columns)
        columns = ",".join(f'"{column}"' for column in entry.columns)
        connection.executemany(
            f'INSERT INTO "{entry.table}" ({columns}) VALUES ({placeholders})',
            values,
        )
