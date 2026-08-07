from __future__ import annotations

import sqlite3
from collections.abc import Iterable, Mapping
from typing import Any

from .enums import LOGICAL_HASH_REGISTRY_VERSION, READ_MODEL_SCHEMA_VERSION
from .errors import SchemaError
from .identity import LOGICAL_REGISTRY


INTEGER_COLUMNS = frozenset(
    {
        "meta_id", "rl_p0_package_bytes", "rl_p0_record_count", "through_position",
        "artifact_bytes", "current_proxy_count", "current_proxy_bytes",
        "current_segment_count", "current_segment_bytes", "current_total_bytes",
        "historical_deleted_bytes", "ledger_position", "active",
        "score_is_decision_gate", "executed", "operation_success",
        "external_operation_count", "generation_input_allowed",
        "generation_input_allowed_change", "prefix_position",
        "record_count", "event_count", "proposal_count", "decision_count",
        "receipt_count", "media_operation_count",
    }
)


PRIMARY_KEYS: Mapping[str, tuple[str, ...]] = {
    "read_model_meta": ("meta_id",),
    "reference_record": ("pilot_clip_id",),
    "reference_duty": ("pilot_clip_id", "duty"),
    "reference_duty_extension": ("pilot_clip_id", "extension"),
    "artifact": ("artifact_id",),
    "artifact_storage_current": ("pilot_clip_id",),
    "review_observation_history": ("event_id",),
    "score_record_history": ("event_id",),
    "storage_proposal_history": ("event_id",),
    "human_decision_history": ("event_id",),
    "human_decision_proposal": ("decision_event_id", "proposal_event_id"),
    "execution_receipt_history": ("event_id",),
    "execution_receipt_decision": ("receipt_event_id", "decision_event_id"),
    "relationship_assertion_history": ("event_id",),
    "relationship_target": ("event_id", "target_pilot_clip_id"),
    "rights_evidence_history": ("event_id",),
    "rights_decision_history": ("event_id",),
    "rights_decision_evidence": ("decision_event_id", "evidence_event_id"),
    "rights_current": ("pilot_clip_id",),
    "taxonomy_binding_history": ("event_id",),
    "checkpoint_history": ("checkpoint_id",),
    "ledger_event_provenance": ("event_id",),
    "search_document": ("document_id",),
}


NULLABLE_COLUMNS = frozenset(
    {
        "checkpoint_id", "source_event_id", "superseded_by_event_id",
        "retracted_by_event_id", "observation_type", "statement", "score_name",
        "score_value_json", "proposal_id", "action", "decision_domain", "decision",
        "reason", "authorization_id", "before_identity_json", "after_identity_json",
        "possible_family_json", "possible_overlap_json", "exact_duplicate_status",
        "evidence_type", "generation_input_allowed_change",
        "publication_allowed_change",
        "taxonomy_snapshot_id", "taxonomy_version", "actor_class", "actor_id",
        "occurred_at", "recorded_at",
    }
)


TABLE_CONSTRAINTS: Mapping[str, tuple[str, ...]] = {
    "read_model_meta": (
        "CHECK(meta_id = 1)",
        f"CHECK(read_model_schema_version = '{READ_MODEL_SCHEMA_VERSION}')",
        f"CHECK(logical_hash_registry_version = '{LOGICAL_HASH_REGISTRY_VERSION}')",
        "CHECK(through_position >= 0)",
    ),
    "artifact": ("CHECK(artifact_bytes >= 0)",),
    "artifact_storage_current": (
        "CHECK(current_proxy_count >= 0 AND current_proxy_bytes >= 0)",
        "CHECK(current_segment_count >= 0 AND current_segment_bytes >= 0)",
        "CHECK(current_total_bytes = current_proxy_bytes + current_segment_bytes)",
        "CHECK(historical_deleted_bytes >= 0)",
    ),
    "review_observation_history": ("CHECK(active IN (0,1))", "UNIQUE(ledger_id, ledger_position)"),
    "score_record_history": ("CHECK(score_is_decision_gate = 0)", "CHECK(active IN (0,1))", "UNIQUE(ledger_id, ledger_position)"),
    "storage_proposal_history": ("CHECK(executed = 0)", "CHECK(active IN (0,1))", "UNIQUE(ledger_id, ledger_position)"),
    "human_decision_history": ("UNIQUE(ledger_id, ledger_position)",),
    "execution_receipt_history": ("CHECK(operation_success IN (0,1))", "CHECK(external_operation_count >= 0)", "UNIQUE(ledger_id, ledger_position)"),
    "relationship_assertion_history": ("CHECK(active IN (0,1))", "UNIQUE(ledger_id, ledger_position)"),
    "rights_evidence_history": ("UNIQUE(ledger_id, ledger_position)",),
    "rights_decision_history": ("UNIQUE(ledger_id, ledger_position)",),
    "rights_current": ("CHECK(generation_input_allowed IN (0,1))", "CHECK(publication_allowed IN ('TRUE','FALSE','UNKNOWN'))"),
    "taxonomy_binding_history": ("UNIQUE(ledger_id, ledger_position)",),
    "checkpoint_history": ("UNIQUE(event_id)", "UNIQUE(ledger_id, ledger_position)"),
    "ledger_event_provenance": ("UNIQUE(ledger_id, ledger_position)", "UNIQUE(event_body_hash)"),
}


FOREIGN_KEYS: Mapping[str, tuple[str, ...]] = {
    "reference_duty": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "reference_duty_extension": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "artifact": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "artifact_storage_current": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "review_observation_history": (
        "FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",
        "FOREIGN KEY(superseded_by_event_id) REFERENCES review_observation_history(event_id) DEFERRABLE INITIALLY DEFERRED",
        "FOREIGN KEY(retracted_by_event_id) REFERENCES review_observation_history(event_id) DEFERRABLE INITIALLY DEFERRED",
    ),
    "score_record_history": (
        "FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",
        "FOREIGN KEY(superseded_by_event_id) REFERENCES score_record_history(event_id) DEFERRABLE INITIALLY DEFERRED",
        "FOREIGN KEY(retracted_by_event_id) REFERENCES score_record_history(event_id) DEFERRABLE INITIALLY DEFERRED",
    ),
    "storage_proposal_history": (
        "FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",
        "FOREIGN KEY(superseded_by_event_id) REFERENCES storage_proposal_history(event_id) DEFERRABLE INITIALLY DEFERRED",
        "FOREIGN KEY(retracted_by_event_id) REFERENCES storage_proposal_history(event_id) DEFERRABLE INITIALLY DEFERRED",
    ),
    "human_decision_history": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "human_decision_proposal": (
        "FOREIGN KEY(decision_event_id) REFERENCES human_decision_history(event_id)",
        "FOREIGN KEY(proposal_event_id) REFERENCES storage_proposal_history(event_id)",
    ),
    "execution_receipt_history": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "execution_receipt_decision": (
        "FOREIGN KEY(receipt_event_id) REFERENCES execution_receipt_history(event_id)",
        "FOREIGN KEY(decision_event_id) REFERENCES human_decision_history(event_id)",
    ),
    "relationship_assertion_history": (
        "FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",
        "FOREIGN KEY(retracted_by_event_id) REFERENCES relationship_assertion_history(event_id) DEFERRABLE INITIALLY DEFERRED",
    ),
    "relationship_target": ("FOREIGN KEY(event_id) REFERENCES relationship_assertion_history(event_id)", "FOREIGN KEY(target_pilot_clip_id) REFERENCES reference_record(pilot_clip_id)"),
    "rights_evidence_history": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "rights_decision_history": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "rights_decision_evidence": ("FOREIGN KEY(decision_event_id) REFERENCES rights_decision_history(event_id)", "FOREIGN KEY(evidence_event_id) REFERENCES rights_evidence_history(event_id)"),
    "rights_current": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "taxonomy_binding_history": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "ledger_event_provenance": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
    "search_document": ("FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id)",),
}


INDEX_STATEMENTS = (
    "CREATE UNIQUE INDEX ux_reference_record_record_id ON reference_record(record_id)",
    "CREATE INDEX ix_reference_record_family ON reference_record(primary_family,pilot_clip_id)",
    "CREATE INDEX ix_reference_record_scope ON reference_record(content_scope,pilot_clip_id)",
    "CREATE INDEX ix_reference_record_taxonomy ON reference_record(taxonomy_status,pilot_clip_id)",
    "CREATE INDEX ix_reference_duty_duty ON reference_duty(duty,pilot_clip_id)",
    "CREATE INDEX ix_artifact_status ON artifact(technical_status,pilot_clip_id)",
    "CREATE INDEX ix_artifact_availability ON artifact(availability,pilot_clip_id)",
    "CREATE INDEX ix_artifact_lifecycle ON artifact(lifecycle,pilot_clip_id)",
    "CREATE INDEX ix_storage_total ON artifact_storage_current(current_total_bytes,pilot_clip_id)",
    "CREATE INDEX ix_observation_current ON review_observation_history(pilot_clip_id,active,ledger_position)",
    "CREATE INDEX ix_score_current ON score_record_history(pilot_clip_id,active,score_name,ledger_position)",
    "CREATE INDEX ix_proposal_current ON storage_proposal_history(pilot_clip_id,active,action,ledger_position)",
    "CREATE INDEX ix_human_decision_domain ON human_decision_history(pilot_clip_id,decision_domain,ledger_position)",
    "CREATE INDEX ix_receipt_operation ON execution_receipt_history(pilot_clip_id,operation_type,ledger_position)",
    "CREATE INDEX ix_relationship_current ON relationship_assertion_history(pilot_clip_id,active,ledger_position)",
    "CREATE INDEX ix_relationship_target ON relationship_target(target_pilot_clip_id,event_id)",
    "CREATE INDEX ix_rights_evidence ON rights_evidence_history(pilot_clip_id,evidence_type,ledger_position)",
    "CREATE INDEX ix_rights_decision ON rights_decision_history(pilot_clip_id,ledger_position)",
    "CREATE INDEX ix_rights_current ON rights_current(rights_provenance,generation_input_allowed,publication_allowed,pilot_clip_id)",
    "CREATE INDEX ix_taxonomy_binding ON taxonomy_binding_history(taxonomy_snapshot_id,taxonomy_version,pilot_clip_id)",
    "CREATE INDEX ix_checkpoint_prefix ON checkpoint_history(prefix_position,projection_hash)",
    "CREATE INDEX ix_event_type ON ledger_event_provenance(event_type,ledger_position)",
    "CREATE INDEX ix_event_authority ON ledger_event_provenance(authority_class,ledger_position)",
    "CREATE INDEX ix_search_record ON search_document(pilot_clip_id,active_state,document_kind,document_id)",
)


def _column_sql(name: str, primary: bool) -> str:
    affinity = "INTEGER" if name in INTEGER_COLUMNS else "TEXT COLLATE BINARY"
    nullable = name in NULLABLE_COLUMNS
    parts = [f'"{name}"', affinity]
    if not nullable:
        parts.append("NOT NULL")
    if primary:
        parts.append("PRIMARY KEY")
    return " ".join(parts)


def create_schema(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = DELETE")
    connection.execute("PRAGMA synchronous = FULL")
    for entry in LOGICAL_REGISTRY:
        primary_key = PRIMARY_KEYS[entry.table]
        inline_primary = len(primary_key) == 1
        definitions = [
            _column_sql(column, inline_primary and column == primary_key[0])
            for column in entry.columns
        ]
        if entry.table == "read_model_meta":
            definitions.append('"logical_content_hash" TEXT COLLATE BINARY')
        if len(primary_key) > 1:
            definitions.append("PRIMARY KEY(" + ",".join(f'"{value}"' for value in primary_key) + ")")
        definitions.extend(TABLE_CONSTRAINTS.get(entry.table, ()))
        definitions.extend(FOREIGN_KEYS.get(entry.table, ()))
        sql = f'CREATE TABLE "{entry.table}" (' + ",".join(definitions) + ") WITHOUT ROWID"
        connection.execute(sql)
    for statement in INDEX_STATEMENTS:
        connection.execute(statement)
    connection.execute(
        "CREATE VIRTUAL TABLE search_current_fts USING fts5("
        "document_id UNINDEXED,pilot_clip_id UNINDEXED,document_kind UNINDEXED,"
        "description_text,observation_text,taxonomy_text,duty_text,bounded_notes_text,"
        "prepared_tokens,tokenize='unicode61')"
    )
    connection.execute(
        "CREATE VIRTUAL TABLE search_history_fts USING fts5("
        "document_id UNINDEXED,pilot_clip_id UNINDEXED,document_kind UNINDEXED,"
        "description_text,observation_text,taxonomy_text,duty_text,bounded_notes_text,"
        "prepared_tokens,tokenize='unicode61')"
    )
    connection.execute(
        "CREATE VIEW review_observation_current AS SELECT * FROM review_observation_history WHERE active=1"
    )
    connection.execute(
        "CREATE VIEW score_record_current AS SELECT * FROM score_record_history WHERE active=1"
    )
    connection.execute(
        "CREATE VIEW storage_proposal_current AS SELECT * FROM storage_proposal_history WHERE active=1"
    )
    connection.execute(
        "CREATE VIEW relationship_assertion_current AS SELECT * FROM relationship_assertion_history WHERE active=1"
    )
    connection.execute(
        "CREATE VIEW taxonomy_binding_current AS "
        "SELECT t.* FROM taxonomy_binding_history t WHERE t.ledger_position=("
        "SELECT max(t2.ledger_position) FROM taxonomy_binding_history t2 "
        "WHERE t2.pilot_clip_id=t.pilot_clip_id)"
    )


def insert_rows(connection: sqlite3.Connection, rows: Mapping[str, Iterable[tuple[Any, ...]]]) -> None:
    expected = {entry.table for entry in LOGICAL_REGISTRY}
    if set(rows) != expected:
        raise SchemaError("mapped table set differs from the closed logical registry")
    for entry in LOGICAL_REGISTRY:
        placeholders = ",".join("?" for _ in entry.columns)
        columns = ",".join(f'"{column}"' for column in entry.columns)
        values = list(rows[entry.table])
        if any(len(row) != len(entry.columns) for row in values):
            raise SchemaError(f"mapped row width differs for {entry.table}")
        connection.executemany(
            f'INSERT INTO "{entry.table}" ({columns}) VALUES ({placeholders})', values
        )


def populate_fts(connection: sqlite3.Connection) -> None:
    fields = (
        "document_id,pilot_clip_id,document_kind,description_text,observation_text,"
        "taxonomy_text,duty_text,bounded_notes_text,prepared_tokens"
    )
    connection.execute(
        f"INSERT INTO search_current_fts ({fields}) SELECT {fields} FROM search_document WHERE active_state='CURRENT' ORDER BY document_id COLLATE BINARY"
    )
    connection.execute(
        f"INSERT INTO search_history_fts ({fields}) SELECT {fields} FROM search_document WHERE active_state='HISTORY' ORDER BY document_id COLLATE BINARY"
    )


def require_fts5(connection: sqlite3.Connection) -> None:
    try:
        connection.execute("CREATE VIRTUAL TABLE temp.rl_p2_fts_probe USING fts5(body, tokenize='unicode61')")
        connection.execute("INSERT INTO temp.rl_p2_fts_probe(body) VALUES (?)", ("alpha beta",))
        row = connection.execute(
            "SELECT body,bm25(rl_p2_fts_probe) FROM rl_p2_fts_probe WHERE rl_p2_fts_probe MATCH ?",
            ("alpha",),
        ).fetchone()
    except sqlite3.Error as error:
        raise SchemaError("required FTS5/unicode61/bm25 capability is unavailable") from error
    if row is None or row[0] != "alpha beta":
        raise SchemaError("FTS5 capability probe returned an unexpected row")


def validate_fts_parity(connection: sqlite3.Connection) -> None:
    expected_current = connection.execute("SELECT count(*) FROM search_document WHERE active_state='CURRENT'").fetchone()[0]
    expected_history = connection.execute("SELECT count(*) FROM search_document WHERE active_state='HISTORY'").fetchone()[0]
    actual_current = connection.execute("SELECT count(*) FROM search_current_fts").fetchone()[0]
    actual_history = connection.execute("SELECT count(*) FROM search_history_fts").fetchone()[0]
    if (expected_current, expected_history) != (actual_current, actual_history):
        raise SchemaError("FTS current/history content differs from search_document")
    fields = (
        "document_id,pilot_clip_id,document_kind,description_text,observation_text,"
        "taxonomy_text,duty_text,bounded_notes_text,prepared_tokens"
    )
    for table, state in (("search_current_fts", "CURRENT"), ("search_history_fts", "HISTORY")):
        missing = connection.execute(
            f"SELECT {fields} FROM search_document WHERE active_state=? "
            f"EXCEPT SELECT {fields} FROM {table}",
            (state,),
        ).fetchone()
        extra = connection.execute(
            f"SELECT {fields} FROM {table} EXCEPT "
            f"SELECT {fields} FROM search_document WHERE active_state=?",
            (state,),
        ).fetchone()
        if missing is not None or extra is not None:
            raise SchemaError(f"{table} row content differs from search_document")
