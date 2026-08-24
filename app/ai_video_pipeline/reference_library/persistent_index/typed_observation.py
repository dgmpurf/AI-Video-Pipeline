from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.ai_video_pipeline.reference_library.event_ledger.successor import (
    SuccessorEntry,
    replay_parent_and_successor,
    validate_successor_manifest,
)
from app.ai_video_pipeline.reference_library.event_ledger.typed_targets import (
    TARGET_KINDS,
    TARGET_KIND_INVENTORY_ASSET,
    TARGET_KIND_PILOT_CLIP,
)
from app.ai_video_pipeline.reference_library.event_ledger.models import (
    BaseCatalogAdapter,
    LedgerEntry,
)

from .builder import RuntimeStateProtectionPolicy, validate_state_root
from .identity import canonical_json_text, logical_content_hash, sha256_hex
from .mapper import MappedReadModel
from .schema import create_schema, insert_rows, populate_fts, require_fts5
from .tokenize import prepare_document


TYPED_READ_MODEL_SCHEMA_VERSION = "RL_P2_TYPED_OBSERVATION_READ_MODEL_V0_2"
TYPED_LOGICAL_HASH_REGISTRY_VERSION = "RL_P2_TYPED_LOGICAL_HASH_V0_2"
TYPED_BUILDER_CONTRACT_VERSION = "RL_P2_TYPED_BUILDER_V0_2"

EXACT_ATTRIBUTE_PATHS = frozenset(
    {
        "negative_guards[]",
        "causal_family_relation.CF1_CONTACT_FORCE_REACTION",
        "causal_family_relation.CF2_WEAPON_CLASH_GUARD",
        "causal_family_relation.CF3_PURSUIT_CHASE",
        "reference_use_surface.action_grammar_reference",
        "reference_use_surface.spatial_choreography_reference",
        "reference_use_surface.hard_negative_guard_reference",
        "reference_use_surface.destruction_or_effect_reference",
        "reference_use_surface.locomotion_reference",
    }
)


class TypedObservationIndexError(ValueError):
    pass


class TypedObservationRows:
    __slots__ = (
        "_inventory_assets",
        "_observations",
        "_exact_attributes",
        "_search_documents",
        "_segment_id",
        "_through_position",
        "_through_entry_hash",
        "_successor_projection_hash",
        "_provenance",
        "_seal",
    )

    def __init__(self, *_: Any, **__: Any) -> None:
        raise TypedObservationIndexError(
            "typed observation rows require verified parent-plus-successor replay"
        )

    @property
    def inventory_assets(self) -> tuple[tuple[Any, ...], ...]:
        return self._inventory_assets

    @property
    def observations(self) -> tuple[tuple[Any, ...], ...]:
        return self._observations

    @property
    def exact_attributes(self) -> tuple[tuple[Any, ...], ...]:
        return self._exact_attributes

    @property
    def search_documents(self) -> tuple[tuple[Any, ...], ...]:
        return self._search_documents

    @property
    def segment_id(self) -> str:
        return self._segment_id

    @property
    def through_position(self) -> int:
        return self._through_position

    @property
    def through_entry_hash(self) -> str:
        return self._through_entry_hash

    @property
    def successor_projection_hash(self) -> str:
        return self._successor_projection_hash

    @property
    def provenance(self) -> Mapping[str, Any]:
        return json.loads(_canonical(self._provenance))

    @property
    def provenance_sha256(self) -> str:
        return sha256_hex(_canonical(self._provenance).encode("utf-8"))


@dataclass(frozen=True)
class TypedObservationBuildResult:
    generation_path: Path
    logical_content_hash: str
    materialization_generation_id: str


@dataclass(frozen=True)
class TypedObservationQuery:
    scope: str = "CURRENT"
    target_kinds: tuple[str, ...] = ()
    inventory_file_ids: tuple[str, ...] = ()
    anchor_codes: tuple[str, ...] = ()
    accepted_review_roles: tuple[str, ...] = ()
    review_evidence_classes: tuple[str, ...] = ()
    exact_attributes: tuple[tuple[str, str], ...] = ()
    text: str | None = None


def _canonical(value: Any) -> str:
    return canonical_json_text(value)


def _row_seal_body(rows: TypedObservationRows) -> dict[str, Any]:
    return {
        "inventory_assets": [list(row) for row in rows.inventory_assets],
        "observations": [list(row) for row in rows.observations],
        "exact_attributes": [list(row) for row in rows.exact_attributes],
        "search_documents": [list(row) for row in rows.search_documents],
        "segment_id": rows.segment_id,
        "through_position": rows.through_position,
        "through_entry_hash": rows.through_entry_hash,
        "successor_projection_hash": rows.successor_projection_hash,
        "verified_provenance_sha256": rows.provenance_sha256,
        "provenance": rows.provenance,
    }


def _create_verified_rows(
    *,
    inventory_assets: tuple[tuple[Any, ...], ...],
    observations: tuple[tuple[Any, ...], ...],
    exact_attributes: tuple[tuple[Any, ...], ...],
    search_documents: tuple[tuple[Any, ...], ...],
    segment_id: str,
    through_position: int,
    through_entry_hash: str,
    successor_projection_hash: str,
    provenance: Mapping[str, Any],
) -> TypedObservationRows:
    value = object.__new__(TypedObservationRows)
    object.__setattr__(value, "_inventory_assets", inventory_assets)
    object.__setattr__(value, "_observations", observations)
    object.__setattr__(value, "_exact_attributes", exact_attributes)
    object.__setattr__(value, "_search_documents", search_documents)
    object.__setattr__(value, "_segment_id", segment_id)
    object.__setattr__(value, "_through_position", through_position)
    object.__setattr__(value, "_through_entry_hash", through_entry_hash)
    object.__setattr__(value, "_successor_projection_hash", successor_projection_hash)
    object.__setattr__(value, "_provenance", json.loads(_canonical(provenance)))
    object.__setattr__(
        value, "_seal", sha256_hex(_canonical(_row_seal_body(value)).encode("utf-8"))
    )
    return value


def _validate_verified_rows(value: Any) -> TypedObservationRows:
    if type(value) is not TypedObservationRows:
        raise TypedObservationIndexError(
            "typed generation requires rows from verified parent-plus-successor replay"
        )
    try:
        observed = value._seal
        expected = sha256_hex(_canonical(_row_seal_body(value)).encode("utf-8"))
    except Exception as error:
        raise TypedObservationIndexError(
            "typed observation provenance seal is absent or malformed"
        ) from error
    if observed != expected:
        raise TypedObservationIndexError("typed observation provenance seal differs")
    provenance = value.provenance
    required = {
        "parent_manifest_sha256",
        "parent_projection_hash",
        "parent_tail_entry_hash",
        "successor_manifest_sha256",
        "successor_segment_id",
        "successor_entry_hashes",
        "successor_projection_hash",
        "inventory_registry_hash",
    }
    if set(provenance) != required:
        raise TypedObservationIndexError("typed observation provenance fields differ")
    for field in required - {"successor_segment_id", "successor_entry_hashes"}:
        child = provenance[field]
        if not isinstance(child, str) or len(child) != 64:
            raise TypedObservationIndexError("typed observation provenance hash differs")
    hashes = provenance["successor_entry_hashes"]
    if not isinstance(hashes, list) or any(
        not isinstance(child, str) or len(child) != 64 for child in hashes
    ):
        raise TypedObservationIndexError("typed successor entry provenance differs")
    if not isinstance(provenance["successor_segment_id"], str):
        raise TypedObservationIndexError("typed successor segment provenance differs")
    return value


def _revalidate_rows_against_successor_replay(
    value: TypedObservationRows,
    *,
    parent_manifest: Mapping[str, Any] | None,
    adapter: BaseCatalogAdapter | None,
    parent_entries: Iterable[LedgerEntry] | None,
    successor_manifest: Mapping[str, Any] | None,
    successor_entries: Iterable[SuccessorEntry] | None,
) -> TypedObservationRows:
    if (
        parent_manifest is None
        or adapter is None
        or parent_entries is None
        or successor_manifest is None
        or successor_entries is None
    ):
        raise TypedObservationIndexError(
            "typed generation requires independently verified successor replay context"
        )
    replay_rows = map_successor_observations(
        parent_manifest,
        adapter,
        parent_entries,
        successor_manifest,
        successor_entries,
    )
    if _canonical(_row_seal_body(value)) != _canonical(_row_seal_body(replay_rows)):
        raise TypedObservationIndexError(
            "typed observation rows differ from verified successor replay"
        )
    return replay_rows


def _validate_parent_read_model_binding(
    parent: MappedReadModel, rows: TypedObservationRows
) -> None:
    meta_rows = parent.table("read_model_meta")
    if len(meta_rows) != 1 or len(meta_rows[0]) < 19:
        raise TypedObservationIndexError("parent read-model metadata differs")
    meta = meta_rows[0]
    provenance = rows.provenance
    if meta[17] != provenance["parent_tail_entry_hash"]:
        raise TypedObservationIndexError("typed rows parent tail binding differs")
    if meta[18] != provenance["parent_projection_hash"]:
        raise TypedObservationIndexError("typed rows parent projection binding differs")


def _attribute_value(value: Any) -> tuple[str, str]:
    if value is True:
        return "BOOLEAN", "true"
    if value is False:
        return "BOOLEAN", "false"
    if isinstance(value, str) and value:
        return "STRING", value
    raise TypedObservationIndexError(
        "exact observation attributes must be booleans or nonempty strings"
    )


def _extract_exact_attributes(
    event_id: str, payload: Mapping[str, Any]
) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    guards = payload.get("negative_guards", [])
    if not isinstance(guards, list) or any(
        not isinstance(value, str) or not value for value in guards
    ):
        raise TypedObservationIndexError("negative_guards must contain strings")
    for value in guards:
        value_type, value_text = _attribute_value(value)
        rows.append((event_id, "negative_guards[]", value_type, value_text))
    causal = payload.get("causal_family_relation", {})
    if not isinstance(causal, dict):
        raise TypedObservationIndexError("causal_family_relation must be an object")
    for key in (
        "CF1_CONTACT_FORCE_REACTION",
        "CF2_WEAPON_CLASH_GUARD",
        "CF3_PURSUIT_CHASE",
    ):
        if key in causal:
            value_type, value_text = _attribute_value(causal[key])
            rows.append(
                (event_id, f"causal_family_relation.{key}", value_type, value_text)
            )
    reuse = payload.get("reference_use_surface", {})
    if not isinstance(reuse, dict):
        raise TypedObservationIndexError("reference_use_surface must be an object")
    for key in (
        "action_grammar_reference",
        "spatial_choreography_reference",
        "hard_negative_guard_reference",
        "destruction_or_effect_reference",
        "locomotion_reference",
    ):
        if key in reuse:
            value_type, value_text = _attribute_value(reuse[key])
            rows.append(
                (event_id, f"reference_use_surface.{key}", value_type, value_text)
            )
    if any(row[1] not in EXACT_ATTRIBUTE_PATHS for row in rows):
        raise TypedObservationIndexError("unapproved exact attribute path")
    return sorted(set(rows))


def _append_observation_rows(
    observations: list[tuple[Any, ...]],
    attributes: list[tuple[str, str, str, str]],
    search_documents: list[tuple[Any, ...]],
    *,
    segment_id: str,
    ledger_position: int,
    event: Mapping[str, Any],
    target_kind: str,
    target_id: str,
    active_record: Mapping[str, Any],
) -> None:
    pilot_clip_id = target_id if target_kind == TARGET_KIND_PILOT_CLIP else None
    inventory_file_id = (
        target_id if target_kind == TARGET_KIND_INVENTORY_ASSET else None
    )
    payload = event["payload"]
    active = 1 if active_record["active"] else 0
    statement = payload["statement"]
    observations.append(
        (
            event["event_id"],
            segment_id,
            ledger_position,
            target_kind,
            target_id,
            pilot_clip_id,
            inventory_file_id,
            event["event_type"],
            event["authority_class"],
            payload["observation_type"],
            statement,
            payload.get("b21_anchor_code"),
            payload.get("accepted_review_role"),
            payload.get("review_evidence_class"),
            active,
            active_record["superseded_by"],
            _canonical(event["source_trace_ids"]),
            _canonical(payload),
        )
    )
    attributes.extend(_extract_exact_attributes(event["event_id"], payload))
    search_documents.append(
        (
            f"typed-event:{event['event_id']}:observation",
            target_kind,
            target_id,
            pilot_clip_id,
            inventory_file_id,
            "REVIEW_OBSERVATION",
            event["event_id"],
            "CURRENT" if active else "HISTORY",
            event["authority_class"],
            statement,
            prepare_document(statement),
            ledger_position,
        )
    )


def map_successor_observations(
    parent_manifest: Mapping[str, Any],
    adapter: BaseCatalogAdapter,
    parent_entries: Iterable[LedgerEntry],
    successor_manifest: Mapping[str, Any],
    successor_entries: Iterable[SuccessorEntry],
) -> TypedObservationRows:
    parent_values = tuple(parent_entries)
    successor_values = tuple(successor_entries)
    mixed = replay_parent_and_successor(
        parent_manifest,
        adapter,
        parent_values,
        successor_manifest,
        successor_values,
    )
    manifest = validate_successor_manifest(dict(successor_manifest))
    parent_state = mixed.parent_projection.to_dict()
    successor_state = mixed.successor_projection.to_dict()
    if successor_state["event_count"] != len(successor_values):
        raise TypedObservationIndexError("successor projection event count differs")

    registry = manifest["inventory_identity_registry"]
    inventory_assets = tuple(
        (
            record["inventory_file_id"],
            record["target_kind"],
            _canonical(record),
            sha256_hex(_canonical(record).encode("utf-8")),
            registry["canonical_registry_hash"],
            registry["package_filename"],
            registry["package_bytes"],
            registry["package_sha256"],
        )
        for record in registry["records"]
    )
    observations: list[tuple[Any, ...]] = []
    attributes: list[tuple[str, str, str, str]] = []
    search_documents: list[tuple[Any, ...]] = []

    for entry in parent_values:
        value = entry.to_dict()
        event = value["event"]
        if event["event_type"] not in {
            "REVIEW_OBSERVATION_ADDED",
            "REVIEW_OBSERVATION_CORRECTED",
        }:
            continue
        _append_observation_rows(
            observations,
            attributes,
            search_documents,
            segment_id=parent_manifest["ledger_id"],
            ledger_position=value["ledger_position"],
            event=event,
            target_kind=TARGET_KIND_PILOT_CLIP,
            target_id=event["pilot_clip_id"],
            active_record=parent_state["event_index"][event["event_id"]],
        )

    for entry in successor_values:
        value = entry.to_dict()
        event = value["event"]
        target = event["target_identity"]
        _append_observation_rows(
            observations,
            attributes,
            search_documents,
            segment_id=manifest["segment_id"],
            ledger_position=value["ledger_position"],
            event=event,
            target_kind=target["target_kind"],
            target_id=target["target_id"],
            active_record=successor_state["event_index"][event["event_id"]],
        )

    observations.sort(key=lambda row: (row[2], row[1], row[0]))
    attributes.sort()
    search_documents.sort()
    provenance = {
        "parent_manifest_sha256": sha256_hex(
            _canonical(dict(parent_manifest)).encode("utf-8")
        ),
        "parent_projection_hash": mixed.parent_projection.projection_hash,
        "parent_tail_entry_hash": manifest["parent_binding"][
            "parent_tail_entry_hash"
        ],
        "successor_manifest_sha256": sha256_hex(
            _canonical(manifest).encode("utf-8")
        ),
        "successor_segment_id": manifest["segment_id"],
        "successor_entry_hashes": [entry.entry_hash for entry in successor_values],
        "successor_projection_hash": mixed.successor_projection.projection_hash,
        "inventory_registry_hash": registry["canonical_registry_hash"],
    }
    return _create_verified_rows(
        inventory_assets=inventory_assets,
        observations=tuple(observations),
        exact_attributes=tuple(attributes),
        search_documents=tuple(search_documents),
        segment_id=manifest["segment_id"],
        through_position=int(successor_state["through_position"]),
        through_entry_hash=str(successor_state["through_entry_hash"]),
        successor_projection_hash=mixed.successor_projection.projection_hash,
        provenance=provenance,
    )


def _create_typed_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        CREATE TABLE typed_read_model_meta(
          meta_id INTEGER PRIMARY KEY CHECK(meta_id=1),
          read_model_schema_version TEXT NOT NULL COLLATE BINARY,
          logical_hash_registry_version TEXT NOT NULL COLLATE BINARY,
          builder_contract_version TEXT NOT NULL COLLATE BINARY,
          parent_materialization_generation_id TEXT NOT NULL COLLATE BINARY,
          parent_logical_content_hash TEXT NOT NULL COLLATE BINARY,
          segment_id TEXT NOT NULL COLLATE BINARY,
          through_position INTEGER NOT NULL,
          through_entry_hash TEXT NOT NULL COLLATE BINARY,
          successor_projection_hash TEXT NOT NULL COLLATE BINARY,
          verified_provenance_sha256 TEXT NOT NULL COLLATE BINARY,
          materialization_generation_id TEXT NOT NULL COLLATE BINARY,
          logical_content_hash TEXT COLLATE BINARY
        ) WITHOUT ROWID;
        CREATE TABLE inventory_asset_record(
          inventory_file_id TEXT PRIMARY KEY COLLATE BINARY,
          target_kind TEXT NOT NULL COLLATE BINARY CHECK(target_kind='INVENTORY_ASSET'),
          canonical_identity_json TEXT NOT NULL COLLATE BINARY,
          canonical_identity_sha256 TEXT NOT NULL COLLATE BINARY,
          registry_hash TEXT NOT NULL COLLATE BINARY,
          registry_package_filename TEXT NOT NULL COLLATE BINARY,
          registry_package_bytes INTEGER NOT NULL CHECK(registry_package_bytes>0),
          registry_package_sha256 TEXT NOT NULL COLLATE BINARY
        ) WITHOUT ROWID;
        CREATE TABLE typed_review_observation_history(
          event_id TEXT PRIMARY KEY COLLATE BINARY,
          segment_id TEXT NOT NULL COLLATE BINARY,
          ledger_position INTEGER NOT NULL,
          target_kind TEXT NOT NULL COLLATE BINARY CHECK(target_kind IN ('PILOT_CLIP','INVENTORY_ASSET')),
          target_id TEXT NOT NULL COLLATE BINARY,
          pilot_clip_id TEXT COLLATE BINARY,
          inventory_file_id TEXT COLLATE BINARY,
          event_type TEXT NOT NULL COLLATE BINARY,
          authority_class TEXT NOT NULL COLLATE BINARY CHECK(authority_class='OBSERVATION_ONLY'),
          observation_type TEXT NOT NULL COLLATE BINARY,
          statement TEXT NOT NULL COLLATE BINARY,
          anchor_code TEXT COLLATE BINARY,
          accepted_review_role TEXT COLLATE BINARY,
          review_evidence_class TEXT COLLATE BINARY,
          active INTEGER NOT NULL CHECK(active IN (0,1)),
          superseded_by_event_id TEXT COLLATE BINARY,
          source_trace_json TEXT NOT NULL COLLATE BINARY,
          payload_json TEXT NOT NULL COLLATE BINARY,
          UNIQUE(segment_id,ledger_position),
          CHECK(
            (target_kind='PILOT_CLIP' AND pilot_clip_id IS NOT NULL AND inventory_file_id IS NULL AND target_id=pilot_clip_id)
            OR
            (target_kind='INVENTORY_ASSET' AND pilot_clip_id IS NULL AND inventory_file_id IS NOT NULL AND target_id=inventory_file_id)
          ),
          FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id),
          FOREIGN KEY(inventory_file_id) REFERENCES inventory_asset_record(inventory_file_id),
          FOREIGN KEY(superseded_by_event_id) REFERENCES typed_review_observation_history(event_id)
            DEFERRABLE INITIALLY DEFERRED
        ) WITHOUT ROWID;
        CREATE TABLE typed_review_observation_exact_attribute(
          event_id TEXT NOT NULL COLLATE BINARY,
          attribute_path TEXT NOT NULL COLLATE BINARY,
          value_type TEXT NOT NULL COLLATE BINARY CHECK(value_type IN ('BOOLEAN','STRING')),
          value_text TEXT NOT NULL COLLATE BINARY,
          PRIMARY KEY(event_id,attribute_path,value_text),
          FOREIGN KEY(event_id) REFERENCES typed_review_observation_history(event_id)
        ) WITHOUT ROWID;
        CREATE TABLE typed_search_document(
          document_id TEXT PRIMARY KEY COLLATE BINARY,
          target_kind TEXT NOT NULL COLLATE BINARY,
          target_id TEXT NOT NULL COLLATE BINARY,
          pilot_clip_id TEXT COLLATE BINARY,
          inventory_file_id TEXT COLLATE BINARY,
          document_kind TEXT NOT NULL COLLATE BINARY,
          source_event_id TEXT NOT NULL COLLATE BINARY,
          active_state TEXT NOT NULL COLLATE BINARY CHECK(active_state IN ('CURRENT','HISTORY')),
          authority_class TEXT NOT NULL COLLATE BINARY,
          observation_text TEXT NOT NULL COLLATE BINARY,
          prepared_tokens TEXT NOT NULL COLLATE BINARY,
          through_position INTEGER NOT NULL,
          CHECK(
            (target_kind='PILOT_CLIP' AND pilot_clip_id IS NOT NULL AND inventory_file_id IS NULL AND target_id=pilot_clip_id)
            OR
            (target_kind='INVENTORY_ASSET' AND pilot_clip_id IS NULL AND inventory_file_id IS NOT NULL AND target_id=inventory_file_id)
          ),
          FOREIGN KEY(pilot_clip_id) REFERENCES reference_record(pilot_clip_id),
          FOREIGN KEY(inventory_file_id) REFERENCES inventory_asset_record(inventory_file_id),
          FOREIGN KEY(source_event_id) REFERENCES typed_review_observation_history(event_id)
        ) WITHOUT ROWID;
        CREATE UNIQUE INDEX ux_typed_inventory_target
          ON inventory_asset_record(target_kind,inventory_file_id);
        CREATE INDEX ix_typed_observation_inventory_current
          ON typed_review_observation_history(inventory_file_id,active,ledger_position);
        CREATE INDEX ix_typed_observation_pilot_current
          ON typed_review_observation_history(pilot_clip_id,active,ledger_position);
        CREATE INDEX ix_typed_observation_kind_current
          ON typed_review_observation_history(target_kind,active,ledger_position);
        CREATE INDEX ix_typed_observation_anchor
          ON typed_review_observation_history(anchor_code,active,event_id);
        CREATE INDEX ix_typed_observation_role
          ON typed_review_observation_history(accepted_review_role,active,event_id);
        CREATE INDEX ix_typed_observation_evidence_class
          ON typed_review_observation_history(review_evidence_class,active,event_id);
        CREATE INDEX ix_typed_observation_attribute
          ON typed_review_observation_exact_attribute(attribute_path,value_text,event_id);
        CREATE VIRTUAL TABLE typed_search_current_fts USING fts5(
          document_id UNINDEXED,target_kind UNINDEXED,target_id UNINDEXED,
          pilot_clip_id UNINDEXED,inventory_file_id UNINDEXED,observation_text,prepared_tokens,
          tokenize='unicode61'
        );
        CREATE VIRTUAL TABLE typed_search_history_fts USING fts5(
          document_id UNINDEXED,target_kind UNINDEXED,target_id UNINDEXED,
          pilot_clip_id UNINDEXED,inventory_file_id UNINDEXED,observation_text,prepared_tokens,
          tokenize='unicode61'
        );
        CREATE VIEW typed_review_observation_current AS
          SELECT * FROM typed_review_observation_history WHERE active=1;
        """
    )


def _generation_identity(parent: MappedReadModel, rows: TypedObservationRows) -> str:
    body = {
        "read_model_schema_version": TYPED_READ_MODEL_SCHEMA_VERSION,
        "logical_hash_registry_version": TYPED_LOGICAL_HASH_REGISTRY_VERSION,
        "builder_contract_version": TYPED_BUILDER_CONTRACT_VERSION,
        "parent_materialization_generation_id": parent.materialization_generation_id,
        "segment_id": rows.segment_id,
        "through_position": rows.through_position,
        "through_entry_hash": rows.through_entry_hash,
        "successor_projection_hash": rows.successor_projection_hash,
        "verified_provenance_sha256": rows.provenance_sha256,
    }
    return sha256_hex(_canonical(body).encode("utf-8"))


def _typed_logical_hash(
    connection: sqlite3.Connection,
    parent_logical_hash: str,
    verified_provenance_sha256: str,
) -> str:
    tables = []
    definitions = (
        ("inventory_asset_record", "inventory_file_id,target_kind,canonical_identity_json,canonical_identity_sha256,registry_hash,registry_package_filename,registry_package_bytes,registry_package_sha256", "inventory_file_id"),
        ("typed_review_observation_history", "event_id,segment_id,ledger_position,target_kind,target_id,pilot_clip_id,inventory_file_id,event_type,authority_class,observation_type,statement,anchor_code,accepted_review_role,review_evidence_class,active,superseded_by_event_id,source_trace_json,payload_json", "ledger_position,event_id"),
        ("typed_review_observation_exact_attribute", "event_id,attribute_path,value_type,value_text", "event_id,attribute_path,value_text"),
        ("typed_search_document", "document_id,target_kind,target_id,pilot_clip_id,inventory_file_id,document_kind,source_event_id,active_state,authority_class,observation_text,prepared_tokens,through_position", "document_id"),
    )
    for table, columns, order in definitions:
        rows = [list(row) for row in connection.execute(
            f"SELECT {columns} FROM {table} ORDER BY {order} COLLATE BINARY"
        )]
        tables.append([table, columns.split(","), rows])
    body = [
        TYPED_LOGICAL_HASH_REGISTRY_VERSION,
        TYPED_READ_MODEL_SCHEMA_VERSION,
        parent_logical_hash,
        verified_provenance_sha256,
        tables,
    ]
    return sha256_hex(_canonical(body).encode("utf-8"))


def _populate_typed(
    connection: sqlite3.Connection,
    parent: MappedReadModel,
    rows: TypedObservationRows,
    parent_logical_hash: str,
) -> tuple[str, str]:
    generation_id = _generation_identity(parent, rows)
    connection.execute(
        "INSERT INTO typed_read_model_meta VALUES (1,?,?,?,?,?,?,?,?,?,?,?,NULL)",
        (
            TYPED_READ_MODEL_SCHEMA_VERSION,
            TYPED_LOGICAL_HASH_REGISTRY_VERSION,
            TYPED_BUILDER_CONTRACT_VERSION,
            parent.materialization_generation_id,
            parent_logical_hash,
            rows.segment_id,
            rows.through_position,
            rows.through_entry_hash,
            rows.successor_projection_hash,
            rows.provenance_sha256,
            generation_id,
        ),
    )
    connection.executemany(
        "INSERT INTO inventory_asset_record VALUES (?,?,?,?,?,?,?,?)", rows.inventory_assets
    )
    connection.executemany(
        "INSERT INTO typed_review_observation_history VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        rows.observations,
    )
    connection.executemany(
        "INSERT INTO typed_review_observation_exact_attribute VALUES (?,?,?,?)",
        rows.exact_attributes,
    )
    connection.executemany(
        "INSERT INTO typed_search_document VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        rows.search_documents,
    )
    connection.execute(
        "INSERT INTO typed_search_current_fts "
        "SELECT document_id,target_kind,target_id,pilot_clip_id,inventory_file_id,observation_text,prepared_tokens "
        "FROM typed_search_document WHERE active_state='CURRENT' ORDER BY document_id"
    )
    connection.execute(
        "INSERT INTO typed_search_history_fts "
        "SELECT document_id,target_kind,target_id,pilot_clip_id,inventory_file_id,observation_text,prepared_tokens "
        "FROM typed_search_document ORDER BY document_id"
    )
    typed_hash = _typed_logical_hash(
        connection, parent_logical_hash, rows.provenance_sha256
    )
    connection.execute(
        "UPDATE typed_read_model_meta SET logical_content_hash=? WHERE meta_id=1",
        (typed_hash,),
    )
    return generation_id, typed_hash


def verify_typed_generation(path: str | Path) -> dict[str, Any]:
    target = Path(path)
    connection = sqlite3.connect(f"file:{target.as_posix()}?mode=ro", uri=True)
    try:
        meta = connection.execute(
            "SELECT read_model_schema_version,logical_hash_registry_version,"
            "builder_contract_version,parent_logical_content_hash,"
            "verified_provenance_sha256,materialization_generation_id,logical_content_hash "
            "FROM typed_read_model_meta WHERE meta_id=1"
        ).fetchone()
        if meta is None or meta[:3] != (
            TYPED_READ_MODEL_SCHEMA_VERSION,
            TYPED_LOGICAL_HASH_REGISTRY_VERSION,
            TYPED_BUILDER_CONTRACT_VERSION,
        ):
            raise TypedObservationIndexError("typed generation metadata differs")
        foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
        if foreign_keys:
            raise TypedObservationIndexError("typed generation foreign-key check failed")
        current_docs = connection.execute(
            "SELECT count(*) FROM typed_search_document WHERE active_state='CURRENT'"
        ).fetchone()[0]
        history_docs = connection.execute(
            "SELECT count(*) FROM typed_search_document"
        ).fetchone()[0]
        if connection.execute("SELECT count(*) FROM typed_search_current_fts").fetchone()[0] != current_docs:
            raise TypedObservationIndexError("typed current FTS parity differs")
        if connection.execute("SELECT count(*) FROM typed_search_history_fts").fetchone()[0] != history_docs:
            raise TypedObservationIndexError("typed history FTS parity differs")
        parent_meta_hash = connection.execute(
            "SELECT logical_content_hash FROM read_model_meta WHERE meta_id=1"
        ).fetchone()[0]
        if meta[3] != parent_meta_hash:
            raise TypedObservationIndexError("parent logical content hash differs")
        expected_hash = _typed_logical_hash(connection, meta[3], meta[4])
        if meta[6] != expected_hash:
            raise TypedObservationIndexError("typed logical content hash differs")
        return {
            "valid": True,
            "verified_provenance_sha256": meta[4],
            "materialization_generation_id": meta[5],
            "logical_content_hash": meta[6],
            "inventory_asset_count": connection.execute(
                "SELECT count(*) FROM inventory_asset_record"
            ).fetchone()[0],
            "observation_count": connection.execute(
                "SELECT count(*) FROM typed_review_observation_history"
            ).fetchone()[0],
        }
    finally:
        connection.close()


def build_typed_observation_generation(
    state_root: str | Path,
    parent_mapped: MappedReadModel,
    typed_rows: TypedObservationRows,
    *,
    protection_policy: RuntimeStateProtectionPolicy,
    parent_manifest: Mapping[str, Any] | None = None,
    adapter: BaseCatalogAdapter | None = None,
    parent_entries: Iterable[LedgerEntry] | None = None,
    successor_manifest: Mapping[str, Any] | None = None,
    successor_entries: Iterable[SuccessorEntry] | None = None,
) -> TypedObservationBuildResult:
    if not isinstance(parent_mapped, MappedReadModel):
        raise TypedObservationIndexError(
            "typed generation requires a governed RL-P2 parent mapping"
        )
    typed_rows = _validate_verified_rows(typed_rows)
    typed_rows = _revalidate_rows_against_successor_replay(
        typed_rows,
        parent_manifest=parent_manifest,
        adapter=adapter,
        parent_entries=parent_entries,
        successor_manifest=successor_manifest,
        successor_entries=successor_entries,
    )
    _validate_parent_read_model_binding(parent_mapped, typed_rows)
    root = validate_state_root(state_root, protection_policy=protection_policy)
    root.mkdir(parents=True, exist_ok=True)
    generation_id = _generation_identity(parent_mapped, typed_rows)
    staging = root / f"rl_p2--{TYPED_READ_MODEL_SCHEMA_VERSION}--{generation_id}.partial.sqlite3"
    if staging.exists():
        raise TypedObservationIndexError("typed staging path already exists")
    lock = root / "rl_p2_typed_builder.lock"
    descriptor = os.open(
        lock,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0),
        0o600,
    )
    success = False
    try:
        connection = sqlite3.connect(staging)
        try:
            create_schema(connection)
            require_fts5(connection)
            insert_rows(connection, parent_mapped.rows)
            populate_fts(connection)
            connection.commit()
            base_hash = logical_content_hash(connection)
            connection.execute(
                "UPDATE read_model_meta SET logical_content_hash=? WHERE meta_id=1",
                (base_hash,),
            )
            _create_typed_schema(connection)
            observed_generation_id, typed_hash = _populate_typed(
                connection, parent_mapped, typed_rows, base_hash
            )
            if observed_generation_id != generation_id:
                raise TypedObservationIndexError("typed generation identity differs")
            connection.commit()
        finally:
            connection.close()
        verification = verify_typed_generation(staging)
        if not verification["valid"] or verification["logical_content_hash"] != typed_hash:
            raise TypedObservationIndexError("typed staging verification failed")
        final = root / (
            f"rl_p2--{TYPED_READ_MODEL_SCHEMA_VERSION}--{generation_id}--"
            f"sha256-{typed_hash}.sqlite3"
        )
        if final.exists():
            raise TypedObservationIndexError("immutable typed generation collision")
        os.rename(staging, final)
        verify_typed_generation(final)
        success = True
        return TypedObservationBuildResult(final, typed_hash, generation_id)
    finally:
        os.close(descriptor)
        if lock.exists():
            lock.unlink()
        if not success and staging.exists():
            staging.unlink()


def query_typed_observations(
    generation_path: str | Path,
    query: TypedObservationQuery,
) -> list[dict[str, Any]]:
    if query.scope not in {"CURRENT", "HISTORY"}:
        raise TypedObservationIndexError("query scope must be CURRENT or HISTORY")
    if any(kind not in TARGET_KINDS for kind in query.target_kinds):
        raise TypedObservationIndexError("query target kind is not allowed")
    for path, _ in query.exact_attributes:
        if path not in EXACT_ATTRIBUTE_PATHS:
            raise TypedObservationIndexError("query exact attribute path is not allowed")
    connection = sqlite3.connect(
        f"file:{Path(generation_path).as_posix()}?mode=ro", uri=True
    )
    connection.row_factory = sqlite3.Row
    try:
        where = []
        parameters: list[Any] = []
        if query.scope == "CURRENT":
            where.append("o.active=1")
        filters = (
            ("o.target_kind", query.target_kinds),
            ("o.inventory_file_id", query.inventory_file_ids),
            ("o.anchor_code", query.anchor_codes),
            ("o.accepted_review_role", query.accepted_review_roles),
            ("o.review_evidence_class", query.review_evidence_classes),
        )
        for column, values in filters:
            if values:
                where.append(f"{column} IN ({','.join('?' for _ in values)})")
                parameters.extend(values)
        for path, value in query.exact_attributes:
            where.append(
                "EXISTS (SELECT 1 FROM typed_review_observation_exact_attribute a "
                "WHERE a.event_id=o.event_id AND a.attribute_path=? AND a.value_text=?)"
            )
            parameters.extend((path, value))
        join = ""
        if query.text:
            fts = (
                "typed_search_current_fts"
                if query.scope == "CURRENT"
                else "typed_search_history_fts"
            )
            join = (
                f" JOIN {fts} f ON f.document_id="
                "('typed-event:' || o.event_id || ':observation')"
            )
            where.append(f"{fts} MATCH ?")
            parameters.append(query.text)
        sql = "SELECT o.* FROM typed_review_observation_history o" + join
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY o.ledger_position,o.event_id"
        return [dict(row) for row in connection.execute(sql, parameters)]
    finally:
        connection.close()
