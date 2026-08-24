from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from typing import Any

from .canonical import (
    canonical_sha256,
    require_exact_keys,
    require_nonempty_string,
    require_sha256,
)


TARGET_IDENTITY_SCHEMA_VERSION = "RL_TYPED_TARGET_IDENTITY_V0_2"
INVENTORY_REGISTRY_SCHEMA_VERSION = "RL_INVENTORY_IDENTITY_REGISTRY_V0_1"

CANONICAL_INVENTORY_PACKAGE_FILENAME = (
    "AI_VIDEO_PURCHASED_MATERIALS_G01A_FILESYSTEM_INVENTORY_V0_1.zip"
)
CANONICAL_INVENTORY_PACKAGE_BYTES = 4754
CANONICAL_INVENTORY_PACKAGE_SHA256 = (
    "18123374e871d9123827b27185adc75476ded8244388429a5d58b00e7b41e08c"
)

TARGET_KIND_PILOT_CLIP = "PILOT_CLIP"
TARGET_KIND_INVENTORY_ASSET = "INVENTORY_ASSET"
TARGET_KINDS = frozenset({TARGET_KIND_PILOT_CLIP, TARGET_KIND_INVENTORY_ASSET})

PILOT_CLIP_ID_RE = re.compile(r"^G01D-CLIP-[0-9]{3}$", flags=re.ASCII)
INVENTORY_FILE_ID_RE = re.compile(r"^G01A-F-[0-9A-F]{32}$", flags=re.ASCII)

TARGET_IDENTITY_FIELDS = frozenset(
    {"target_schema_version", "target_kind", "target_id"}
)
REGISTRY_FIELDS = frozenset(
    {
        "registry_schema_version",
        "target_kind",
        "package_filename",
        "package_bytes",
        "package_sha256",
        "source_evidence_identities",
        "record_count",
        "records",
        "canonical_registry_hash",
    }
)
REGISTRY_RECORD_FIELDS = frozenset({"target_kind", "inventory_file_id"})


class TypedTargetValidationError(ValueError):
    pass


def _sorted_unique_strings(values: Any, *, field: str, nonempty: bool = False) -> list[str]:
    if not isinstance(values, list):
        raise TypedTargetValidationError(f"{field} must be a list")
    result = []
    for index, value in enumerate(values):
        try:
            result.append(require_nonempty_string(value, field=f"{field}[{index}]"))
        except Exception as error:
            raise TypedTargetValidationError(str(error)) from error
    if result != sorted(result) or len(result) != len(set(result)):
        raise TypedTargetValidationError(f"{field} must be sorted and unique")
    if nonempty and not result:
        raise TypedTargetValidationError(f"{field} must not be empty")
    return result


def validate_inventory_file_id(value: Any) -> str:
    try:
        identifier = require_nonempty_string(value, field="inventory_file_id")
    except Exception as error:
        raise TypedTargetValidationError(str(error)) from error
    if INVENTORY_FILE_ID_RE.fullmatch(identifier) is None:
        raise TypedTargetValidationError(
            "inventory_file_id does not match G01A-F-<32 uppercase hex>"
        )
    return identifier


def build_inventory_identity_registry(
    inventory_file_ids: Iterable[str],
    *,
    package_filename: str,
    package_bytes: int,
    package_sha256: str,
    source_evidence_identities: Iterable[str],
) -> dict[str, Any]:
    raw_ids = list(inventory_file_ids)
    if len(raw_ids) != len(set(raw_ids)):
        raise TypedTargetValidationError("duplicate inventory identity is forbidden")
    identifiers = sorted(validate_inventory_file_id(value) for value in raw_ids)
    if not identifiers:
        raise TypedTargetValidationError("inventory registry must not be empty")
    source_identities = sorted(source_evidence_identities)
    _sorted_unique_strings(
        source_identities,
        field="source_evidence_identities",
        nonempty=True,
    )
    validated_package = _validate_package_identity(
        package_filename, package_bytes, package_sha256
    )
    body = {
        "registry_schema_version": INVENTORY_REGISTRY_SCHEMA_VERSION,
        "target_kind": TARGET_KIND_INVENTORY_ASSET,
        **validated_package,
        "source_evidence_identities": source_identities,
        "record_count": len(identifiers),
        "records": [
            {
                "target_kind": TARGET_KIND_INVENTORY_ASSET,
                "inventory_file_id": identifier,
            }
            for identifier in identifiers
        ],
    }
    registry = {**body, "canonical_registry_hash": canonical_sha256(body)}
    return validate_inventory_identity_registry(registry)


def _validate_package_identity(
    package_filename: Any, package_bytes: Any, package_sha256: Any
) -> dict[str, Any]:
    try:
        filename = require_nonempty_string(package_filename, field="package_filename")
        require_sha256(package_sha256, field="package_sha256")
        digest = package_sha256
    except Exception as error:
        raise TypedTargetValidationError(str(error)) from error
    if "/" in filename or "\\" in filename or filename in {".", ".."}:
        raise TypedTargetValidationError("package_filename must be an exact basename")
    if (
        not isinstance(package_bytes, int)
        or isinstance(package_bytes, bool)
        or package_bytes <= 0
    ):
        raise TypedTargetValidationError("package_bytes must be a positive integer")
    expected = (
        CANONICAL_INVENTORY_PACKAGE_FILENAME,
        CANONICAL_INVENTORY_PACKAGE_BYTES,
        CANONICAL_INVENTORY_PACKAGE_SHA256,
    )
    if (filename, package_bytes, digest) != expected:
        raise TypedTargetValidationError(
            "inventory package identity differs from the canonical G01A package"
        )
    return {
        "package_filename": filename,
        "package_bytes": package_bytes,
        "package_sha256": digest,
    }


def validate_inventory_identity_registry(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypedTargetValidationError("inventory registry must be an object")
    try:
        require_exact_keys(value, REGISTRY_FIELDS, field="inventory registry")
    except Exception as error:
        raise TypedTargetValidationError(str(error)) from error
    if value["registry_schema_version"] != INVENTORY_REGISTRY_SCHEMA_VERSION:
        raise TypedTargetValidationError("unsupported inventory registry schema")
    if value["target_kind"] != TARGET_KIND_INVENTORY_ASSET:
        raise TypedTargetValidationError("inventory registry target kind differs")
    _validate_package_identity(
        value["package_filename"], value["package_bytes"], value["package_sha256"]
    )
    _sorted_unique_strings(
        value["source_evidence_identities"],
        field="source_evidence_identities",
        nonempty=True,
    )
    if not isinstance(value["records"], list) or not value["records"]:
        raise TypedTargetValidationError("inventory registry records must not be empty")
    identifiers = []
    for index, record in enumerate(value["records"]):
        if not isinstance(record, dict):
            raise TypedTargetValidationError(f"registry record {index} is not an object")
        try:
            require_exact_keys(record, REGISTRY_RECORD_FIELDS, field="registry record")
        except Exception as error:
            raise TypedTargetValidationError(str(error)) from error
        if record["target_kind"] != TARGET_KIND_INVENTORY_ASSET:
            raise TypedTargetValidationError("registry record target kind differs")
        identifiers.append(validate_inventory_file_id(record["inventory_file_id"]))
    if identifiers != sorted(identifiers) or len(identifiers) != len(set(identifiers)):
        raise TypedTargetValidationError(
            "inventory registry records must be sorted and unique"
        )
    if value["record_count"] != len(identifiers):
        raise TypedTargetValidationError("inventory registry record count differs")
    body = {key: child for key, child in value.items() if key != "canonical_registry_hash"}
    if value["canonical_registry_hash"] != canonical_sha256(body):
        raise TypedTargetValidationError("inventory registry hash differs")
    return dict(value)


def inventory_registry_ids(registry: Mapping[str, Any]) -> frozenset[str]:
    validated = validate_inventory_identity_registry(dict(registry))
    return frozenset(record["inventory_file_id"] for record in validated["records"])


def build_target_identity(target_kind: str, target_id: str) -> dict[str, str]:
    value = {
        "target_schema_version": TARGET_IDENTITY_SCHEMA_VERSION,
        "target_kind": target_kind,
        "target_id": target_id,
    }
    return validate_target_identity(value)


def validate_target_identity(
    value: Any,
    *,
    inventory_registry: Mapping[str, Any] | None = None,
    known_pilot_clip_ids: Iterable[str] | None = None,
) -> dict[str, str]:
    if not isinstance(value, dict):
        raise TypedTargetValidationError("typed target must be an object")
    try:
        require_exact_keys(value, TARGET_IDENTITY_FIELDS, field="typed target")
    except Exception as error:
        raise TypedTargetValidationError(str(error)) from error
    if value["target_schema_version"] != TARGET_IDENTITY_SCHEMA_VERSION:
        raise TypedTargetValidationError("unsupported typed-target schema")
    kind = require_nonempty_string(value["target_kind"], field="target_kind")
    identifier = require_nonempty_string(value["target_id"], field="target_id")
    if kind not in TARGET_KINDS:
        raise TypedTargetValidationError("unknown target kind")
    if kind == TARGET_KIND_PILOT_CLIP:
        if PILOT_CLIP_ID_RE.fullmatch(identifier) is None:
            raise TypedTargetValidationError("PILOT_CLIP target has a non-pilot identity")
        if known_pilot_clip_ids is not None and identifier not in set(known_pilot_clip_ids):
            raise TypedTargetValidationError("PILOT_CLIP target is absent from parent projection")
    else:
        validate_inventory_file_id(identifier)
        if inventory_registry is not None and identifier not in inventory_registry_ids(
            inventory_registry
        ):
            raise TypedTargetValidationError(
                "INVENTORY_ASSET target is absent from the bound registry"
            )
    return {
        "target_schema_version": TARGET_IDENTITY_SCHEMA_VERSION,
        "target_kind": kind,
        "target_id": identifier,
    }
