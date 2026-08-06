from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Mapping

from .base_catalog import validate_base_binding
from .canonical import (
    canonical_json_bytes,
    canonical_sha256,
    require_exact_keys,
    require_nonempty_string,
    require_rfc3339_utc,
    strict_json_loads,
)
from .enums import (
    EVENT_SCHEMA_VERSION,
    LEDGER_SCHEMA_VERSION,
    PROJECT_ID,
    PROJECTION_SCHEMA_VERSION,
)
from .errors import ManifestValidationError
from .models import BaseCatalogAdapter


MANIFEST_FILENAME = "ledger_manifest.json"
EVENTS_FILENAME = "events.jsonl"
LOCK_FILENAME = "events.jsonl.lock"
MANIFEST_FIELDS = frozenset(
    {
        "ledger_id",
        "ledger_schema_version",
        "event_schema_version",
        "projection_schema_version",
        "project_id",
        "base_catalog",
        "created_by",
        "created_at",
    }
)
BASE_BINDING_FIELDS = frozenset(
    {
        "package_filename",
        "package_bytes",
        "package_sha256",
        "record_count",
        "record_schema_version",
        "base_catalog_hash",
    }
)


def derive_ledger_id(manifest_without_id: Mapping[str, Any]) -> str:
    return "RL-LEDGER-" + canonical_sha256(dict(manifest_without_id))[:24].upper()


def build_manifest(
    adapter: BaseCatalogAdapter,
    *,
    created_by: str,
    created_at: str,
) -> dict[str, Any]:
    require_nonempty_string(created_by, field="created_by")
    require_rfc3339_utc(created_at, field="created_at")
    body: dict[str, Any] = {
        "ledger_schema_version": LEDGER_SCHEMA_VERSION,
        "event_schema_version": EVENT_SCHEMA_VERSION,
        "projection_schema_version": PROJECTION_SCHEMA_VERSION,
        "project_id": PROJECT_ID,
        "base_catalog": adapter.binding.to_dict(),
        "created_by": created_by,
        "created_at": created_at,
    }
    return {"ledger_id": derive_ledger_id(body), **body}


def validate_manifest(
    value: Any,
    *,
    adapter: BaseCatalogAdapter | None = None,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestValidationError("ledger manifest must be an object")
    try:
        require_exact_keys(value, MANIFEST_FIELDS, field="manifest")
        if value["ledger_schema_version"] != LEDGER_SCHEMA_VERSION:
            raise ManifestValidationError("unsupported ledger schema version")
        if value["event_schema_version"] != EVENT_SCHEMA_VERSION:
            raise ManifestValidationError("unsupported event schema version")
        if value["projection_schema_version"] != PROJECTION_SCHEMA_VERSION:
            raise ManifestValidationError("unsupported projection schema version")
        if value["project_id"] != PROJECT_ID:
            raise ManifestValidationError("project ID does not match")
        require_nonempty_string(value["created_by"], field="created_by")
        require_rfc3339_utc(value["created_at"], field="created_at")
        if not isinstance(value["base_catalog"], dict):
            raise ManifestValidationError("base_catalog must be an object")
        require_exact_keys(
            value["base_catalog"], BASE_BINDING_FIELDS, field="base_catalog"
        )
        body = {key: child for key, child in value.items() if key != "ledger_id"}
        if value["ledger_id"] != derive_ledger_id(body):
            raise ManifestValidationError("ledger ID does not match manifest body")
        if adapter is not None:
            validate_base_binding(value["base_catalog"], adapter)
    except ManifestValidationError:
        raise
    except Exception as error:
        raise ManifestValidationError(str(error)) from error
    return value


def read_manifest(
    ledger_dir: str | Path,
    *,
    adapter: BaseCatalogAdapter | None = None,
) -> dict[str, Any]:
    path = Path(ledger_dir) / MANIFEST_FILENAME
    if path.is_symlink() or not path.is_file():
        raise ManifestValidationError("ledger manifest is absent or not regular")
    raw = path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise ManifestValidationError("manifest must have exactly one terminal LF")
    value = strict_json_loads(raw)
    validate_manifest(value, adapter=adapter)
    if raw != canonical_json_bytes(value) + b"\n":
        raise ManifestValidationError("manifest is not canonical JSON")
    return value


def _write_all(descriptor: int, data: bytes) -> None:
    view = memoryview(data)
    written = 0
    while written < len(view):
        count = os.write(descriptor, view[written:])
        if count <= 0:
            raise OSError("manifest write made no progress")
        written += count


def initialize_manifest(
    ledger_dir: str | Path,
    adapter: BaseCatalogAdapter,
    *,
    created_by: str,
    created_at: str,
) -> dict[str, Any]:
    root = Path(ledger_dir)
    root.mkdir(parents=True, exist_ok=True)
    manifest_path = root / MANIFEST_FILENAME
    manifest = build_manifest(adapter, created_by=created_by, created_at=created_at)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    descriptor = os.open(manifest_path, flags, 0o600)
    try:
        _write_all(descriptor, canonical_json_bytes(manifest) + b"\n")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    read_manifest(root, adapter=adapter)
    return manifest
