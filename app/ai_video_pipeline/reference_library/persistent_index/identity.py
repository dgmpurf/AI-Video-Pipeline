from __future__ import annotations

import hashlib
import json
import math
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from .enums import (
    BUILDER_CONTRACT_VERSION,
    LOGICAL_HASH_REGISTRY_VERSION,
    POINTER_SCHEMA_VERSION,
    READ_MODEL_SCHEMA_VERSION,
)
from .errors import IdentityError, SchemaError


SHA256_RE = re.compile(r"^[0-9a-f]{64}$", flags=re.ASCII)
GENERATION_RE = re.compile(
    r"^rl_p2--(?P<schema>[A-Za-z0-9_]+)--"
    r"(?P<generation>[0-9a-f]{64})--sha256-(?P<logical>[0-9a-f]{64})\.sqlite3$",
    flags=re.ASCII,
)


@dataclass(frozen=True)
class RegistryEntry:
    table: str
    columns: tuple[str, ...]
    row_key: tuple[str, ...]


def _entry(table: str, columns: str, row_key: str) -> RegistryEntry:
    return RegistryEntry(table, tuple(columns.split()), tuple(row_key.split()))


LOGICAL_REGISTRY: tuple[RegistryEntry, ...] = (
    _entry("read_model_meta", "meta_id read_model_schema_version logical_hash_registry_version builder_contract_version builder_source_identity rl_p0_commit rl_p0_package_filename rl_p0_package_bytes rl_p0_package_sha256 rl_p0_record_schema_version rl_p0_record_count base_catalog_hash ledger_id ledger_schema_version event_schema_version projection_schema_version through_position through_entry_hash projection_hash checkpoint_id tokenizer_contract_version build_mode materialization_generation_id", "meta_id"),
    _entry("reference_record", "pilot_clip_id record_id record_schema_version record_revision primary_family content_scope description taxonomy_status canonical_base_record_json canonical_base_record_sha256", "pilot_clip_id"),
    _entry("reference_duty", "pilot_clip_id duty", "pilot_clip_id duty"),
    _entry("reference_duty_extension", "pilot_clip_id extension taxonomy_status", "pilot_clip_id extension"),
    _entry("artifact", "artifact_id pilot_clip_id artifact_type tier role technical_status availability lifecycle artifact_bytes sha256 sha256_status execution_history_json", "artifact_id"),
    _entry("artifact_storage_current", "pilot_clip_id current_proxy_count current_proxy_bytes current_segment_count current_segment_bytes current_total_bytes historical_deleted_bytes arithmetic_status canonical_tier_map_json canonical_segment_map_json", "pilot_clip_id"),
    _entry("review_observation_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class observation_type statement active superseded_by_event_id retracted_by_event_id source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("score_record_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class score_name score_value_json score_is_decision_gate active superseded_by_event_id retracted_by_event_id source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("storage_proposal_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class proposal_id action executed active superseded_by_event_id retracted_by_event_id source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("human_decision_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class decision_domain decision reason authorization_trace_json proposal_event_json source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("human_decision_proposal", "decision_event_id proposal_event_id", "decision_event_id proposal_event_id"),
    _entry("execution_receipt_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class operation_type authorization_id operation_success external_operation_count before_identity_json after_identity_json receipt_traces_json source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("execution_receipt_decision", "receipt_event_id decision_event_id", "receipt_event_id decision_event_id"),
    _entry("relationship_assertion_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class possible_family_json possible_overlap_json exact_duplicate_status active retracted_by_event_id source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("relationship_target", "event_id target_pilot_clip_id", "event_id target_pilot_clip_id"),
    _entry("rights_evidence_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class evidence_type statement source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("rights_decision_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class reason authorization_traces_json rights_changes_json generation_input_allowed_change publication_allowed_change source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("rights_decision_evidence", "decision_event_id evidence_event_id", "decision_event_id evidence_event_id"),
    _entry("rights_current", "pilot_clip_id rights_provenance generation_input_allowed publication_allowed source_decision_event_id through_position", "pilot_clip_id"),
    _entry("taxonomy_binding_history", "event_id ledger_id ledger_position pilot_clip_id event_type authority_class taxonomy_snapshot_id taxonomy_version source_trace_json payload_json", "ledger_id ledger_position event_id"),
    _entry("checkpoint_history", "checkpoint_id event_id ledger_id ledger_position prefix_position prefix_entry_hash ledger_prefix_hash projection_hash base_identity_json record_count event_count unknown_distribution_json rights_distribution_json proposal_count decision_count receipt_count media_operation_count validation_errors_json source_trace_json payload_json", "ledger_id ledger_position checkpoint_id"),
    _entry("ledger_event_provenance", "event_id ledger_id ledger_position event_body_hash previous_entry_hash entry_hash event_type authority_class pilot_clip_id actor_class actor_id occurred_at recorded_at target_ids_json source_trace_json supersedes_event_ids_json retracts_event_ids_json preconditions_json payload_json", "ledger_id ledger_position event_id"),
    _entry("search_document", "document_id pilot_clip_id document_kind source_event_id active_state authority_class description_text observation_text taxonomy_text duty_text bounded_notes_text prepared_tokens source_field_path through_position", "document_id"),
)

LOGICAL_TABLE_NAMES = tuple(item.table for item in LOGICAL_REGISTRY)
_FTS_PREFIXES = ("search_current_fts", "search_history_fts")


def _validate_json(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value) or (value == 0 and math.copysign(1.0, value) < 0):
            raise IdentityError(f"non-canonical number at {path}")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            _validate_json(child, f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise IdentityError(f"non-string JSON key at {path}")
            _validate_json(child, f"{path}.{key}")
        return
    raise IdentityError(f"unsupported JSON value at {path}: {type(value).__name__}")


def canonical_json_text(value: Any, *, terminal_lf: bool = False) -> str:
    _validate_json(value)
    text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return text + ("\n" if terminal_lf else "")


def canonical_json_bytes(value: Any, *, terminal_lf: bool = False) -> bytes:
    return canonical_json_text(value, terminal_lf=terminal_lf).encode("utf-8")


def sha256_hex(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonicalize_bounded_json(value: Any) -> str:
    if isinstance(value, str):
        def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            result: dict[str, Any] = {}
            for key, child in pairs:
                if key in result:
                    raise IdentityError(f"duplicate bounded JSON key: {key}")
                result[key] = child
            return result

        try:
            parsed = json.loads(
                value,
                object_pairs_hook=strict_object,
                parse_constant=lambda token: (_ for _ in ()).throw(
                    IdentityError(f"non-finite bounded JSON number: {token}")
                ),
            )
        except (json.JSONDecodeError, IdentityError) as error:
            raise IdentityError("bounded JSON text is invalid") from error
    else:
        parsed = value
    return canonical_json_text(parsed)


def _binary_key(value: Any) -> tuple[int, Any]:
    if value is None:
        return (0, 0)
    if isinstance(value, int):
        return (1, value)
    if isinstance(value, str):
        return (2, value.encode("utf-8"))
    raise IdentityError(f"unsupported row-key type: {type(value).__name__}")


def validate_registry_schema(connection: sqlite3.Connection) -> None:
    physical = {
        str(row[0])
        for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
        if not str(row[0]).startswith("sqlite_")
    }
    extras = {
        name
        for name in physical - set(LOGICAL_TABLE_NAMES)
        if not any(name == prefix or name.startswith(prefix + "_") for prefix in _FTS_PREFIXES)
    }
    missing = set(LOGICAL_TABLE_NAMES) - physical
    if missing or extras:
        raise SchemaError(f"logical table registry differs; missing={sorted(missing)}, extra={sorted(extras)}")
    for entry in LOGICAL_REGISTRY:
        actual = tuple(str(row[1]) for row in connection.execute(f'PRAGMA table_info("{entry.table}")'))
        if entry.table == "read_model_meta":
            allowed = entry.columns + ("logical_content_hash",)
            if actual != allowed:
                raise SchemaError(f"column registry differs for {entry.table}: {actual}")
        elif actual != entry.columns:
            raise SchemaError(f"column registry differs for {entry.table}: {actual}")


def logical_export(connection: sqlite3.Connection) -> list[Any]:
    validate_registry_schema(connection)
    meta_rows = connection.execute("SELECT read_model_schema_version FROM read_model_meta").fetchall()
    if len(meta_rows) != 1:
        raise IdentityError("read_model_meta must contain exactly one row")
    tables: list[Any] = []
    for entry in LOGICAL_REGISTRY:
        select_columns = ",".join(f'"{column}"' for column in entry.columns)
        rows = [list(row) for row in connection.execute(f'SELECT {select_columns} FROM "{entry.table}"')]
        key_indexes = tuple(entry.columns.index(column) for column in entry.row_key)
        rows.sort(key=lambda row: tuple(_binary_key(row[index]) for index in key_indexes))
        seen: set[tuple[Any, ...]] = set()
        for row in rows:
            key = tuple(row[index] for index in key_indexes)
            if key in seen:
                raise IdentityError(f"duplicate logical row key in {entry.table}: {key}")
            seen.add(key)
            for index, column in enumerate(entry.columns):
                value = row[index]
                if value is not None and (
                    column.endswith("_json") or column == "canonical_base_record_json"
                ):
                    if not isinstance(value, str) or canonicalize_bounded_json(value) != value:
                        raise IdentityError(
                            f"non-canonical bounded JSON in {entry.table}.{column}"
                        )
            if entry.table == "reference_record":
                json_index = entry.columns.index("canonical_base_record_json")
                hash_index = entry.columns.index("canonical_base_record_sha256")
                if sha256_hex(str(row[json_index]).encode("utf-8")) != row[hash_index]:
                    raise IdentityError("canonical base-record hash differs")
        tables.append([entry.table, list(entry.columns), rows])
    return [LOGICAL_HASH_REGISTRY_VERSION, str(meta_rows[0][0]), tables]


def logical_export_bytes(connection: sqlite3.Connection) -> bytes:
    return canonical_json_bytes(logical_export(connection))


def logical_content_hash(connection: sqlite3.Connection) -> str:
    return sha256_hex(logical_export_bytes(connection))


def materialization_generation_id(identity: Mapping[str, Any]) -> str:
    body = dict(identity)
    body["read_model_schema_version"] = READ_MODEL_SCHEMA_VERSION
    body["logical_hash_registry_version"] = LOGICAL_HASH_REGISTRY_VERSION
    body["builder_contract_version"] = BUILDER_CONTRACT_VERSION
    return sha256_hex(canonical_json_bytes(body))


def generation_filename(generation_id: str, logical_hash: str) -> str:
    for name, value in (("generation_id", generation_id), ("logical_hash", logical_hash)):
        if SHA256_RE.fullmatch(value) is None:
            raise IdentityError(f"{name} must be full lowercase SHA-256")
    return f"rl_p2--{READ_MODEL_SCHEMA_VERSION}--{generation_id}--sha256-{logical_hash}.sqlite3"


def parse_generation_filename(path: str | Path) -> dict[str, str]:
    match = GENERATION_RE.fullmatch(Path(path).name)
    if match is None:
        raise IdentityError("generation filename does not match the full-hash contract")
    return match.groupdict()


POINTER_FIELDS = frozenset(
    {
        "pointer_schema_version", "generation_filename", "logical_content_hash",
        "read_model_schema_version", "logical_hash_registry_version",
        "materialization_generation_id", "rl_p0_commit", "rl_p0_package_filename",
        "rl_p0_package_bytes", "rl_p0_package_sha256", "rl_p0_record_schema_version",
        "rl_p0_record_count", "base_catalog_hash", "ledger_id", "ledger_schema_version",
        "event_schema_version", "projection_schema_version", "through_position",
        "through_entry_hash", "projection_hash", "checkpoint_id",
    }
)


def pointer_from_meta(meta: Mapping[str, Any], filename: str) -> dict[str, Any]:
    result = {key: meta[key] for key in POINTER_FIELDS if key not in {"pointer_schema_version", "generation_filename"}}
    result["pointer_schema_version"] = POINTER_SCHEMA_VERSION
    result["generation_filename"] = filename
    validate_pointer(result)
    return result


def validate_pointer(value: Mapping[str, Any]) -> None:
    if set(value) != POINTER_FIELDS:
        raise IdentityError("pointer fields differ from the closed schema")
    if value["pointer_schema_version"] != POINTER_SCHEMA_VERSION:
        raise IdentityError("unsupported pointer schema")
    if value["read_model_schema_version"] != READ_MODEL_SCHEMA_VERSION:
        raise IdentityError("unsupported read-model schema")
    if value["logical_hash_registry_version"] != LOGICAL_HASH_REGISTRY_VERSION:
        raise IdentityError("unsupported logical-hash registry")
    filename = str(value["generation_filename"])
    if Path(filename).name != filename or "/" in filename or "\\" in filename:
        raise IdentityError("pointer generation filename must be one basename")
    parsed = parse_generation_filename(filename)
    if parsed["logical"] != value["logical_content_hash"]:
        raise IdentityError("pointer and filename logical hashes differ")
    if parsed["generation"] != value["materialization_generation_id"]:
        raise IdentityError("pointer and filename generation IDs differ")
    for field in ("logical_content_hash", "materialization_generation_id", "rl_p0_package_sha256", "base_catalog_hash", "through_entry_hash", "projection_hash"):
        if SHA256_RE.fullmatch(str(value[field])) is None:
            raise IdentityError(f"{field} must be lowercase SHA-256")
