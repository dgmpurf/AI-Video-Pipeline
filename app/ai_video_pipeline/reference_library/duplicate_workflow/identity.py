from __future__ import annotations

import os
import re
import sqlite3
from pathlib import Path
from typing import Any, Mapping

from .canonical import canonical_json_bytes, canonicalize_bounded_json, sha256_hex
from .enums import (
    BUILD_MODE,
    BUILDER_CONTRACT_VERSION,
    LOGICAL_HASH_REGISTRY_VERSION,
    POINTER_SCHEMA_VERSION,
    READ_MODEL_SCHEMA_VERSION,
)
from .errors import IdentityError, SchemaError
from .registry import LOGICAL_REGISTRY, LOGICAL_TABLE_NAMES


SHA256_RE = re.compile(r"^[0-9a-f]{64}$", flags=re.ASCII)
GENERATION_RE = re.compile(
    r"^rl_p3--(?P<schema>[A-Za-z0-9_]+)--"
    r"(?P<generation>[0-9a-f]{64})--sha256-(?P<logical>[0-9a-f]{64})\.sqlite3$",
    flags=re.ASCII,
)


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
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        if not str(row[0]).startswith("sqlite_")
    }
    missing = set(LOGICAL_TABLE_NAMES) - physical
    extra = physical - set(LOGICAL_TABLE_NAMES)
    if missing or extra:
        raise SchemaError(
            f"closed logical table registry differs; missing={sorted(missing)}, extra={sorted(extra)}"
        )
    for entry in LOGICAL_REGISTRY:
        actual = tuple(
            str(row[1])
            for row in connection.execute(f'PRAGMA table_info("{entry.table}")')
        )
        if actual != entry.columns:
            raise SchemaError(f"column registry differs for {entry.table}: {actual}")


def logical_export(connection: sqlite3.Connection) -> list[Any]:
    validate_registry_schema(connection)
    meta_rows = connection.execute(
        "SELECT read_model_schema_version FROM read_model_meta"
    ).fetchall()
    if len(meta_rows) != 1:
        raise IdentityError("read_model_meta must contain exactly one row")
    tables: list[Any] = []
    for entry in LOGICAL_REGISTRY:
        columns = entry.logical_columns
        select_columns = ",".join(f'"{column}"' for column in columns)
        rows = [
            list(row)
            for row in connection.execute(
                f'SELECT {select_columns} FROM "{entry.table}"'
            )
        ]
        key_indexes = tuple(columns.index(column) for column in entry.row_key)
        rows.sort(key=lambda row: tuple(_binary_key(row[index]) for index in key_indexes))
        seen: set[tuple[Any, ...]] = set()
        for row in rows:
            key = tuple(row[index] for index in key_indexes)
            if key in seen:
                raise IdentityError(f"duplicate logical row key in {entry.table}: {key}")
            seen.add(key)
            for index, column in enumerate(columns):
                value = row[index]
                if value is not None and column.endswith("_json"):
                    if not isinstance(value, str) or canonicalize_bounded_json(value) != value:
                        raise IdentityError(
                            f"non-canonical bounded JSON in {entry.table}.{column}"
                        )
        tables.append([entry.table, list(columns), rows])
    return [
        LOGICAL_HASH_REGISTRY_VERSION,
        str(meta_rows[0][0]),
        tables,
    ]


def logical_export_bytes(connection: sqlite3.Connection) -> bytes:
    return canonical_json_bytes(logical_export(connection))


def logical_content_hash(connection: sqlite3.Connection) -> str:
    return sha256_hex(logical_export_bytes(connection))


def materialization_generation_id(upstream_identity: Mapping[str, Any]) -> str:
    body = dict(upstream_identity)
    body.update(
        {
            "read_model_schema_version": READ_MODEL_SCHEMA_VERSION,
            "logical_hash_registry_version": LOGICAL_HASH_REGISTRY_VERSION,
            "pointer_schema_version": POINTER_SCHEMA_VERSION,
            "builder_contract_version": BUILDER_CONTRACT_VERSION,
            "build_mode": BUILD_MODE,
        }
    )
    return sha256_hex(canonical_json_bytes(body))


def generation_filename(generation_id: str, logical_hash: str) -> str:
    for name, value in (("generation_id", generation_id), ("logical_hash", logical_hash)):
        if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
            raise IdentityError(f"{name} must be full lowercase SHA-256")
    return (
        f"rl_p3--{READ_MODEL_SCHEMA_VERSION}--{generation_id}--"
        f"sha256-{logical_hash}.sqlite3"
    )


def parse_generation_filename(path: str | Path) -> dict[str, str]:
    match = GENERATION_RE.fullmatch(Path(path).name)
    if match is None:
        raise IdentityError("generation filename does not match the full-hash contract")
    return match.groupdict()


POINTER_FIELDS = frozenset(
    {
        "pointer_schema_version",
        "generation_filename",
        "logical_content_hash",
        "read_model_schema_version",
        "logical_hash_registry_version",
        "builder_contract_version",
        "build_mode",
        "rl_p0_commit",
        "rl_p0_package_filename",
        "rl_p0_package_bytes",
        "rl_p0_package_sha256",
        "rl_p0_record_schema_version",
        "rl_p0_record_count",
        "base_v0_1_ledger_id",
        "base_v0_1_checkpoint_id",
        "base_v0_1_checkpoint_event_id",
        "base_v0_1_through_position",
        "base_v0_1_through_entry_hash",
        "base_v0_1_projection_hash",
        "v0_2_ledger_id",
        "v0_2_ledger_schema_version",
        "v0_2_event_schema_version",
        "v0_2_projection_schema_version",
        "v0_2_checkpoint_id",
        "v0_2_through_position",
        "v0_2_through_entry_hash",
        "v0_2_projection_hash",
        "rl_p2_context_generation_filename",
        "rl_p2_context_generation_id",
        "rl_p2_context_logical_hash",
        "materialization_generation_id",
    }
)


def pointer_from_meta(meta: Mapping[str, Any], filename: str) -> dict[str, Any]:
    result = {
        key: meta[key]
        for key in POINTER_FIELDS
        if key not in {"pointer_schema_version", "generation_filename"}
    }
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
    if value["builder_contract_version"] != BUILDER_CONTRACT_VERSION:
        raise IdentityError("unsupported builder contract")
    if value["build_mode"] != BUILD_MODE:
        raise IdentityError("unsupported build mode")
    filename = str(value["generation_filename"])
    if Path(filename).name != filename or "/" in filename or "\\" in filename:
        raise IdentityError("pointer generation filename must be one basename")
    parsed = parse_generation_filename(filename)
    if parsed["logical"] != value["logical_content_hash"]:
        raise IdentityError("pointer and filename logical hashes differ")
    if parsed["generation"] != value["materialization_generation_id"]:
        raise IdentityError("pointer and filename generation IDs differ")
    for field in (
        "logical_content_hash",
        "materialization_generation_id",
        "rl_p0_package_sha256",
        "base_v0_1_through_entry_hash",
        "base_v0_1_projection_hash",
        "v0_2_through_entry_hash",
        "v0_2_projection_hash",
    ):
        if SHA256_RE.fullmatch(str(value[field])) is None:
            raise IdentityError(f"{field} must be lowercase SHA-256")
    optional_hashes = (
        "rl_p2_context_generation_id",
        "rl_p2_context_logical_hash",
    )
    for field in optional_hashes:
        if value[field] is not None and SHA256_RE.fullmatch(str(value[field])) is None:
            raise IdentityError(f"{field} must be null or lowercase SHA-256")
    if value["rl_p2_context_generation_filename"] is not None:
        name = str(value["rl_p2_context_generation_filename"])
        if Path(name).name != name:
            raise IdentityError("RL-P2 context filename must be one basename")


def path_is_within(path: Path, boundary: Path) -> bool:
    try:
        return os.path.commonpath(
            (os.path.normcase(str(path)), os.path.normcase(str(boundary)))
        ) == os.path.normcase(str(boundary))
    except ValueError:
        return False
