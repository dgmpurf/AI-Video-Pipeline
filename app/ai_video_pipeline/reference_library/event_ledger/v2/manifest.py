from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Mapping

from .base_bridge import BASE_BINDING_FIELDS, validate_base_binding
from .canonical import (
    canonical_json_bytes,
    canonical_sha256,
    require_exact_keys,
    require_nonempty_string,
    require_rfc3339_utc,
    strict_json_loads,
)
from .enums import (
    EVENT_REGISTRY_VERSION,
    EVENT_SCHEMA_VERSION,
    LEDGER_SCHEMA_VERSION,
    PROJECT_ID,
    PROJECTION_SCHEMA_VERSION,
)
from .errors import ManifestValidationError
from .models import BaseV01Snapshot


MANIFEST_FILENAME = "ledger_manifest.json"
EVENTS_FILENAME = "events.jsonl"
LOCK_FILENAME = "events.jsonl.lock"
MANIFEST_FIELDS = frozenset(
    {
        "ledger_id",
        "ledger_schema_version",
        "event_schema_version",
        "projection_schema_version",
        "event_registry_version",
        "project_id",
        "base_v0_1",
        "created_by",
        "created_at",
    }
)


def derive_ledger_id(body: Mapping[str, Any]) -> str:
    return "RL2-LEDGER-" + canonical_sha256(dict(body))[:24].upper()


def build_manifest(
    base: BaseV01Snapshot,
    *,
    created_by: str,
    created_at: str,
) -> dict[str, Any]:
    require_nonempty_string(created_by, field="created_by")
    require_rfc3339_utc(created_at, field="created_at")
    body = {
        "ledger_schema_version": LEDGER_SCHEMA_VERSION,
        "event_schema_version": EVENT_SCHEMA_VERSION,
        "projection_schema_version": PROJECTION_SCHEMA_VERSION,
        "event_registry_version": EVENT_REGISTRY_VERSION,
        "project_id": PROJECT_ID,
        "base_v0_1": base.binding.to_dict(),
        "created_by": created_by,
        "created_at": created_at,
    }
    return {"ledger_id": derive_ledger_id(body), **body}


def validate_manifest(
    value: Any,
    *,
    base: BaseV01Snapshot | None = None,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestValidationError("V0.2 ledger manifest must be an object")
    try:
        require_exact_keys(value, MANIFEST_FIELDS, field="manifest")
        if value["ledger_schema_version"] != LEDGER_SCHEMA_VERSION:
            raise ManifestValidationError("unsupported ledger schema version")
        if value["event_schema_version"] != EVENT_SCHEMA_VERSION:
            raise ManifestValidationError("unsupported event schema version")
        if value["projection_schema_version"] != PROJECTION_SCHEMA_VERSION:
            raise ManifestValidationError("unsupported projection schema version")
        if value["event_registry_version"] != EVENT_REGISTRY_VERSION:
            raise ManifestValidationError("unsupported event registry version")
        if value["project_id"] != PROJECT_ID:
            raise ManifestValidationError("project ID differs")
        if not isinstance(value["base_v0_1"], dict):
            raise ManifestValidationError("base_v0_1 must be an object")
        require_exact_keys(value["base_v0_1"], BASE_BINDING_FIELDS, field="base_v0_1")
        validate_base_binding(value["base_v0_1"])
        require_nonempty_string(value["created_by"], field="created_by")
        require_rfc3339_utc(value["created_at"], field="created_at")
        body = {key: child for key, child in value.items() if key != "ledger_id"}
        if value["ledger_id"] != derive_ledger_id(body):
            raise ManifestValidationError("ledger ID does not match manifest body")
        if base is not None and value["base_v0_1"] != base.binding.to_dict():
            raise ManifestValidationError("manifest base differs from validated snapshot")
    except ManifestValidationError:
        raise
    except Exception as error:
        raise ManifestValidationError(str(error)) from error
    return value


def read_manifest(
    ledger_dir: str | Path,
    *,
    base: BaseV01Snapshot | None = None,
) -> dict[str, Any]:
    path = Path(ledger_dir) / MANIFEST_FILENAME
    if path.is_symlink() or not path.is_file():
        raise ManifestValidationError("V0.2 ledger manifest is absent or non-regular")
    raw = path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise ManifestValidationError("manifest must have exactly one terminal LF")
    value = strict_json_loads(raw)
    validate_manifest(value, base=base)
    if raw != canonical_json_bytes(value, terminal_lf=True):
        raise ManifestValidationError("manifest is not canonical JSON")
    return value


def initialize_manifest(
    ledger_dir: str | Path,
    base: BaseV01Snapshot,
    *,
    created_by: str,
    created_at: str,
) -> dict[str, Any]:
    root = Path(ledger_dir)
    root.mkdir(parents=True, exist_ok=True)
    path = root / MANIFEST_FILENAME
    manifest = build_manifest(base, created_by=created_by, created_at=created_at)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    descriptor = os.open(path, flags, 0o600)
    try:
        data = canonical_json_bytes(manifest, terminal_lf=True)
        written = 0
        while written < len(data):
            count = os.write(descriptor, data[written:])
            if count <= 0:
                raise OSError("manifest write made no progress")
            written += count
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    read_manifest(root, base=base)
    return manifest
