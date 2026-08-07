from __future__ import annotations

import base64
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from .enums import SearchScope
from .errors import QueryError
from .identity import canonical_json_bytes, sha256_hex
from .promotion import resolve_current
from .tokenize import prepare_match_query
from .verify import VerificationResult, open_read_only, require_valid_generation


QUERY_CONTRACT_VERSION = "RL_P2_QUERY_V0_1R1"
CURSOR_CONTRACT_VERSION = "RL_P2_CURSOR_V0_1R1"
MAX_PAGE_SIZE = 200
MAX_FILTER_VALUES = 100
MAX_FTS_OFFSET = 10_000

FACET_SORTS: Mapping[str, tuple[str, str]] = {
    "pilot_clip_id": ("r.pilot_clip_id COLLATE BINARY", "pilot_clip_id"),
    "record_id": ("r.record_id COLLATE BINARY", "record_id"),
    "primary_family": ("r.primary_family COLLATE BINARY", "primary_family"),
    "content_scope": ("r.content_scope COLLATE BINARY", "content_scope"),
    "current_total_bytes": ("s.current_total_bytes", "current_total_bytes"),
}


def _validated_values(values: Sequence[str], field_name: str) -> tuple[str, ...]:
    result = tuple(values)
    if len(result) > MAX_FILTER_VALUES:
        raise QueryError(f"{field_name} contains too many values")
    if any(not isinstance(value, str) or not value for value in result):
        raise QueryError(f"{field_name} must contain nonempty strings")
    if len(set(result)) != len(result):
        raise QueryError(f"{field_name} contains duplicate values")
    return tuple(sorted(result, key=lambda value: value.encode("utf-8")))


def _validate_page_size(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= MAX_PAGE_SIZE:
        raise QueryError(f"page_size must be between 1 and {MAX_PAGE_SIZE}")


def _encode_cursor(value: Mapping[str, Any]) -> str:
    raw = canonical_json_bytes(value)
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def _decode_cursor(value: str) -> Mapping[str, Any]:
    if not isinstance(value, str) or not value:
        raise QueryError("cursor must be a nonempty string")
    try:
        padded = value + "=" * (-len(value) % 4)
        raw = base64.urlsafe_b64decode(padded.encode("ascii"))
        import json

        decoded = json.loads(raw.decode("utf-8"))
    except Exception as error:
        raise QueryError("cursor is not canonical base64url JSON") from error
    if not isinstance(decoded, dict) or raw != canonical_json_bytes(decoded):
        raise QueryError("cursor is not canonical base64url JSON")
    return decoded


@dataclass(frozen=True)
class FacetQuery:
    pilot_clip_ids: tuple[str, ...] = ()
    content_families: tuple[str, ...] = ()
    content_scopes: tuple[str, ...] = ()
    reference_duties: tuple[str, ...] = ()
    technical_statuses: tuple[str, ...] = ()
    artifact_availabilities: tuple[str, ...] = ()
    artifact_lifecycles: tuple[str, ...] = ()
    taxonomy_statuses: tuple[str, ...] = ()
    rights_provenances: tuple[str, ...] = ()
    generation_input_allowed: bool | None = None
    publication_allowed: str | None = None
    sort_by: str = "pilot_clip_id"
    descending: bool = False
    page_size: int = 50
    cursor: str | None = None

    def __post_init__(self) -> None:
        for name in (
            "pilot_clip_ids", "content_families", "content_scopes",
            "reference_duties", "technical_statuses", "artifact_availabilities",
            "artifact_lifecycles", "taxonomy_statuses", "rights_provenances",
        ):
            object.__setattr__(self, name, _validated_values(getattr(self, name), name))
        if self.sort_by not in FACET_SORTS:
            raise QueryError(f"unsupported facet sort: {self.sort_by}")
        if self.generation_input_allowed is not None and not isinstance(
            self.generation_input_allowed, bool
        ):
            raise QueryError("generation_input_allowed must be boolean or null")
        if self.publication_allowed not in {None, "TRUE", "FALSE", "UNKNOWN"}:
            raise QueryError("publication_allowed must be TRUE, FALSE, UNKNOWN, or null")
        _validate_page_size(self.page_size)

    def normalized(self) -> dict[str, Any]:
        return {
            "query_contract_version": QUERY_CONTRACT_VERSION,
            "mode": "FACET",
            "filters": {
                "pilot_clip_ids": list(self.pilot_clip_ids),
                "content_families": list(self.content_families),
                "content_scopes": list(self.content_scopes),
                "reference_duties": list(self.reference_duties),
                "technical_statuses": list(self.technical_statuses),
                "artifact_availabilities": list(self.artifact_availabilities),
                "artifact_lifecycles": list(self.artifact_lifecycles),
                "taxonomy_statuses": list(self.taxonomy_statuses),
                "rights_provenances": list(self.rights_provenances),
                "generation_input_allowed": self.generation_input_allowed,
                "publication_allowed": self.publication_allowed,
            },
            "sort_by": self.sort_by,
            "descending": self.descending,
            "page_size": self.page_size,
        }


@dataclass(frozen=True)
class SearchQuery:
    text: str
    scope: SearchScope = SearchScope.CURRENT
    pilot_clip_ids: tuple[str, ...] = ()
    authority_classes: tuple[str, ...] = ()
    rights_provenances: tuple[str, ...] = ()
    generation_input_allowed: bool | None = None
    publication_allowed: str | None = None
    page_size: int = 50
    cursor: str | None = None

    def __post_init__(self) -> None:
        if isinstance(self.scope, str):
            try:
                object.__setattr__(self, "scope", SearchScope(self.scope))
            except ValueError as error:
                raise QueryError("search scope must be CURRENT or HISTORY") from error
        for name in ("pilot_clip_ids", "authority_classes", "rights_provenances"):
            object.__setattr__(self, name, _validated_values(getattr(self, name), name))
        if self.generation_input_allowed is not None and not isinstance(
            self.generation_input_allowed, bool
        ):
            raise QueryError("generation_input_allowed must be boolean or null")
        if self.publication_allowed not in {None, "TRUE", "FALSE", "UNKNOWN"}:
            raise QueryError("publication_allowed must be TRUE, FALSE, UNKNOWN, or null")
        _validate_page_size(self.page_size)
        prepare_match_query(self.text)

    def normalized(self) -> dict[str, Any]:
        return {
            "query_contract_version": QUERY_CONTRACT_VERSION,
            "mode": "FTS",
            "text": self.text,
            "search_text_sha256": sha256_hex(self.text.encode("utf-8")),
            "scope": self.scope.value,
            "filters": {
                "pilot_clip_ids": list(self.pilot_clip_ids),
                "authority_classes": list(self.authority_classes),
                "rights_provenances": list(self.rights_provenances),
                "generation_input_allowed": self.generation_input_allowed,
                "publication_allowed": self.publication_allowed,
            },
            "sort_by": "SEARCH_RELEVANCE_THEN_BINARY_IDENTITY",
            "page_size": self.page_size,
        }


@dataclass(frozen=True)
class QueryPage:
    request_hash: str
    request: Mapping[str, Any]
    generation: Mapping[str, Any]
    rows: tuple[Mapping[str, Any], ...]
    next_cursor: str | None
    page_offset: int = 0
    warnings: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query_contract_version": QUERY_CONTRACT_VERSION,
            "request_hash": self.request_hash,
            "request": dict(self.request),
            "generation": dict(self.generation),
            "freshness_verdict": "VALID_CURRENT_GENERATION",
            "page_offset": self.page_offset,
            "row_count": len(self.rows),
            "rows": [dict(row) for row in self.rows],
            "next_cursor": self.next_cursor,
            "warnings": list(self.warnings),
        }


class ReadModel:
    """Pinned, verified, read-only access to one immutable RL-P2 generation."""

    def __init__(
        self,
        generation_path: Path,
        verification: VerificationResult,
        connection: sqlite3.Connection,
    ) -> None:
        self.generation_path = generation_path
        self.verification = verification
        self.connection = connection

    @classmethod
    def open_generation(
        cls,
        generation_path: str | Path,
        *,
        pointer: Mapping[str, Any] | str | Path | None = None,
        expected_upstream: Mapping[str, Any] | None = None,
    ) -> "ReadModel":
        path = Path(generation_path).resolve(strict=True)
        verification = require_valid_generation(
            path, pointer=pointer, expected_upstream=expected_upstream
        )
        return cls(path, verification, open_read_only(path))

    @classmethod
    def open_current(
        cls,
        state_root: str | Path,
        *,
        expected_upstream: Mapping[str, Any] | None = None,
    ) -> "ReadModel":
        generation, pointer = resolve_current(state_root)
        return cls.open_generation(
            generation, pointer=pointer, expected_upstream=expected_upstream
        )

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "ReadModel":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _generation_envelope(self) -> dict[str, Any]:
        meta = self.verification.metadata
        return {
            "generation_filename": self.generation_path.name,
            "materialization_generation_id": meta["materialization_generation_id"],
            "read_model_schema_version": meta["read_model_schema_version"],
            "logical_hash_registry_version": meta["logical_hash_registry_version"],
            "logical_content_hash": self.verification.logical_content_hash,
            "rl_p0_commit": meta["rl_p0_commit"],
            "rl_p0_package_sha256": meta["rl_p0_package_sha256"],
            "base_catalog_hash": meta["base_catalog_hash"],
            "ledger_id": meta["ledger_id"],
            "through_position": meta["through_position"],
            "through_entry_hash": meta["through_entry_hash"],
            "projection_hash": meta["projection_hash"],
        }

    def facet(self, request: FacetQuery) -> QueryPage:
        normalized = request.normalized()
        request_hash = sha256_hex(canonical_json_bytes(normalized))
        generation_id = str(self.verification.metadata["materialization_generation_id"])
        where: list[str] = []
        parameters: list[Any] = []

        def add_in(expression: str, values: Sequence[str]) -> None:
            if values:
                where.append(expression + " IN (" + ",".join("?" for _ in values) + ")")
                parameters.extend(values)

        add_in("r.pilot_clip_id", request.pilot_clip_ids)
        add_in("r.primary_family", request.content_families)
        add_in("r.content_scope", request.content_scopes)
        add_in("r.taxonomy_status", request.taxonomy_statuses)
        add_in("g.rights_provenance", request.rights_provenances)
        for duty in request.reference_duties:
            where.append(
                "EXISTS (SELECT 1 FROM reference_duty d WHERE d.pilot_clip_id=r.pilot_clip_id AND d.duty=?)"
            )
            parameters.append(duty)
        for expression, values in (
            ("a.technical_status", request.technical_statuses),
            ("a.availability", request.artifact_availabilities),
            ("a.lifecycle", request.artifact_lifecycles),
        ):
            if values:
                where.append(
                    "EXISTS (SELECT 1 FROM artifact a WHERE a.pilot_clip_id=r.pilot_clip_id AND "
                    + expression
                    + " IN ("
                    + ",".join("?" for _ in values)
                    + "))"
                )
                parameters.extend(values)
        if request.generation_input_allowed is not None:
            where.append("g.generation_input_allowed=?")
            parameters.append(int(request.generation_input_allowed))
        if request.publication_allowed is not None:
            where.append("g.publication_allowed=?")
            parameters.append(request.publication_allowed)

        sort_expression, sort_field = FACET_SORTS[request.sort_by]
        if request.cursor is not None:
            cursor = _decode_cursor(request.cursor)
            required = {
                "cursor_contract_version", "mode", "materialization_generation_id",
                "request_hash", "sort_value", "pilot_clip_id",
            }
            if set(cursor) != required or cursor.get("cursor_contract_version") != CURSOR_CONTRACT_VERSION:
                raise QueryError("facet cursor schema differs")
            if cursor.get("mode") != "FACET" or cursor.get("materialization_generation_id") != generation_id:
                raise QueryError("facet cursor generation or mode differs")
            if cursor.get("request_hash") != request_hash:
                raise QueryError("facet cursor request differs")
            if request.sort_by == "pilot_clip_id":
                operator = "<" if request.descending else ">"
                where.append(f"r.pilot_clip_id COLLATE BINARY {operator} ?")
                parameters.append(cursor["pilot_clip_id"])
            else:
                operator = "<" if request.descending else ">"
                where.append(
                    f"({sort_expression} {operator} ? OR "
                    f"({sort_expression} = ? AND r.pilot_clip_id COLLATE BINARY > ?))"
                )
                parameters.extend(
                    [cursor["sort_value"], cursor["sort_value"], cursor["pilot_clip_id"]]
                )

        sql = (
            "SELECT r.pilot_clip_id,r.record_id,r.primary_family,r.content_scope,"
            "r.description,r.taxonomy_status,s.current_proxy_count,s.current_proxy_bytes,"
            "s.current_segment_count,s.current_segment_bytes,s.current_total_bytes,"
            "g.rights_provenance,g.generation_input_allowed,g.publication_allowed,"
            f"{sort_expression} AS _sort_value "
            "FROM reference_record r "
            "JOIN artifact_storage_current s ON s.pilot_clip_id=r.pilot_clip_id "
            "JOIN rights_current g ON g.pilot_clip_id=r.pilot_clip_id"
        )
        if where:
            sql += " WHERE " + " AND ".join(where)
        direction = "DESC" if request.descending else "ASC"
        sql += f" ORDER BY {sort_expression} {direction},r.pilot_clip_id COLLATE BINARY ASC LIMIT ?"
        parameters.append(request.page_size + 1)
        fetched = self.connection.execute(sql, parameters).fetchall()
        has_more = len(fetched) > request.page_size
        selected = fetched[: request.page_size]
        rows = tuple({key: row[key] for key in row.keys() if key != "_sort_value"} for row in selected)
        next_cursor = None
        if has_more and selected:
            last = selected[-1]
            next_cursor = _encode_cursor(
                {
                    "cursor_contract_version": CURSOR_CONTRACT_VERSION,
                    "mode": "FACET",
                    "materialization_generation_id": generation_id,
                    "request_hash": request_hash,
                    "sort_value": last["_sort_value"],
                    "pilot_clip_id": last["pilot_clip_id"],
                }
            )
        return QueryPage(
            request_hash, normalized, self._generation_envelope(), rows, next_cursor
        )

    def search(self, request: SearchQuery) -> QueryPage:
        normalized = request.normalized()
        request_hash = sha256_hex(canonical_json_bytes(normalized))
        generation_id = str(self.verification.metadata["materialization_generation_id"])
        offset = 0
        if request.cursor is not None:
            cursor = _decode_cursor(request.cursor)
            required = {
                "cursor_contract_version", "mode", "materialization_generation_id",
                "request_hash", "next_offset",
            }
            if set(cursor) != required or cursor.get("cursor_contract_version") != CURSOR_CONTRACT_VERSION:
                raise QueryError("FTS cursor schema differs")
            if cursor.get("mode") != "FTS" or cursor.get("materialization_generation_id") != generation_id:
                raise QueryError("FTS cursor generation or mode differs")
            if cursor.get("request_hash") != request_hash:
                raise QueryError("FTS cursor request differs")
            offset = cursor.get("next_offset")
            if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
                raise QueryError("FTS cursor offset is invalid")
        if offset > MAX_FTS_OFFSET:
            raise QueryError("FTS cursor exceeds the bounded offset limit")

        table = (
            "search_current_fts"
            if request.scope == SearchScope.CURRENT
            else "search_history_fts"
        )
        where = [f"{table} MATCH ?"]
        parameters: list[Any] = [prepare_match_query(request.text)]

        def add_in(expression: str, values: Sequence[str]) -> None:
            if values:
                where.append(expression + " IN (" + ",".join("?" for _ in values) + ")")
                parameters.extend(values)

        add_in("d.pilot_clip_id", request.pilot_clip_ids)
        add_in("d.authority_class", request.authority_classes)
        add_in("g.rights_provenance", request.rights_provenances)
        if request.generation_input_allowed is not None:
            where.append("g.generation_input_allowed=?")
            parameters.append(int(request.generation_input_allowed))
        if request.publication_allowed is not None:
            where.append("g.publication_allowed=?")
            parameters.append(request.publication_allowed)
        sql = (
            f"SELECT d.document_id,d.pilot_clip_id,d.document_kind,d.source_event_id,"
            "d.active_state,d.authority_class,d.description_text,d.observation_text,"
            "d.taxonomy_text,d.duty_text,d.bounded_notes_text,d.source_field_path,"
            "d.through_position,g.rights_provenance,g.generation_input_allowed,"
            f"g.publication_allowed,bm25({table},0,0,0,5,3,2,2,1,1) AS search_relevance "
            f"FROM {table} JOIN search_document d ON d.document_id={table}.document_id "
            "JOIN rights_current g ON g.pilot_clip_id=d.pilot_clip_id "
            "WHERE " + " AND ".join(where) +
            " ORDER BY search_relevance ASC,d.pilot_clip_id COLLATE BINARY ASC,"
            "d.document_kind COLLATE BINARY ASC,d.document_id COLLATE BINARY ASC LIMIT ? OFFSET ?"
        )
        parameters.extend([request.page_size + 1, offset])
        fetched = self.connection.execute(sql, parameters).fetchall()
        has_more = len(fetched) > request.page_size
        selected = fetched[: request.page_size]
        rows = tuple(dict(row) for row in selected)
        next_offset = offset + len(selected)
        warnings: tuple[str, ...] = ()
        next_cursor = None
        if has_more:
            if next_offset <= MAX_FTS_OFFSET:
                next_cursor = _encode_cursor(
                    {
                        "cursor_contract_version": CURSOR_CONTRACT_VERSION,
                        "mode": "FTS",
                        "materialization_generation_id": generation_id,
                        "request_hash": request_hash,
                        "next_offset": next_offset,
                    }
                )
            else:
                warnings = ("FTS_BOUNDED_OFFSET_LIMIT_REACHED",)
        return QueryPage(
            request_hash,
            normalized,
            self._generation_envelope(),
            rows,
            next_cursor,
            page_offset=offset,
            warnings=warnings,
        )
