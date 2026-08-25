from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
from collections import Counter
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from ..event_ledger import (
    SUCCESSOR_EVENT_SCHEMA_VERSION,
    SuccessorEntry,
    append_successor_event_candidate,
    build_inventory_identity_registry,
    build_parent_binding,
    build_successor_manifest,
    build_target_identity,
    load_base_catalog,
    load_validated_ledger,
    replay_entries,
    replay_parent_and_successor,
    replay_successor_entries,
)
from ..event_ledger.canonical import (
    canonical_json_bytes,
    canonical_sha256,
    require_exact_keys,
    require_nonempty_string,
    strict_json_loads,
)
from ..event_ledger.successor import REVIEW_OBSERVATION_ADDED
from ..event_ledger.typed_targets import TARGET_KIND_INVENTORY_ASSET
from . import (
    TypedObservationQuery,
    build_typed_observation_generation,
    map_projection,
    map_successor_observations,
    query_typed_observations,
    verify_typed_generation,
)
from .builder import (
    RuntimeStateProtectionPolicy,
    validate_state_root,
)


INGEST_RECEIPT_SCHEMA_VERSION = "RL_BOUNDED_B21_INGEST_RECEIPT_V0_1"
INPUT_BINDING_SCHEMA_VERSION = "RL_BOUNDED_B21_INPUT_BINDING_V0_1"
LOGICAL_SOURCE_IDENTITY_SCHEMA_VERSION = (
    "B21_BOUNDED_INGEST_LOGICAL_SOURCE_IDENTITY_V0_1"
)
OBSERVATION_TYPE = "B21_REVIEWED_PUBLIC_ANCHOR_OBSERVATION_V0_1"
B040_INVENTORY_FILE_ID = "G01A-F-D7C621BD1DA755E8813DCD0994B7A1D3"

CATALOG_FIELDS = frozenset(
    {
        "accepted_review_role",
        "active_generation_input_allowed",
        "anchor_code",
        "causal_family_relation",
        "contact_force_reaction_positive_claim",
        "human_correction_status",
        "inventory_file_id",
        "negative_guards",
        "reference_use_surface",
        "review_evidence_class",
        "rights_status",
        "source_evidence",
        "uncertainty",
        "weapon_clash_positive_claim",
    }
)
GUARD_FIELDS = frozenset(
    {
        "active_generation_input_allowed",
        "anchor_code",
        "causal_family_relation",
        "inventory_file_id",
        "negative_guard_status",
        "negative_guards",
        "reference_use_surface",
        "review_evidence_class",
        "rights_status",
    }
)
CAUSAL_FIELDS = frozenset(
    {
        "CF1_CONTACT_FORCE_REACTION",
        "CF2_WEAPON_CLASH_GUARD",
        "CF3_PURSUIT_CHASE",
    }
)
REFERENCE_FIELDS = frozenset(
    {
        "action_grammar_reference",
        "spatial_choreography_reference",
        "hard_negative_guard_reference",
        "destruction_or_effect_reference",
        "locomotion_reference",
    }
)
EXPECTED_CLASS_COUNTS = {
    "POSITIVE": 4,
    "PARTIAL_OR_AMBIGUOUS": 1,
    "HARD_NEGATIVE": 5,
    "NON_CAUSAL_REFERENCE": 2,
}


class BoundedB21IngestError(ValueError):
    pass


def _is_reparse_point(path: Path) -> bool:
    flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    attributes = getattr(os.lstat(path), "st_file_attributes", 0)
    return bool(flag and attributes & flag)


def _require_regular_file(value: str | Path, *, role: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        raise BoundedB21IngestError(f"{role} must be an explicit absolute path")
    if path.is_symlink() or not path.exists() or not path.is_file():
        raise BoundedB21IngestError(f"{role} must be an existing regular file")
    if _is_reparse_point(path):
        raise BoundedB21IngestError(f"{role} may not be a reparse point")
    return path.resolve(strict=True)


def _file_identity(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": str(path),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def _optional_file_identity(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "exists": False, "bytes": 0, "sha256": None}
    identity = _file_identity(_require_regular_file(path, role=path.name))
    return {**identity, "exists": True}


def _logical_file_identity(identity: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "bytes": identity["bytes"],
        "sha256": identity["sha256"],
    }


def _logical_source_identity(input_bindings: Mapping[str, Any]) -> dict[str, Any]:
    parent_members = {
        "schema_version": "B21_GOVERNED_PARENT_LEDGER_LOGICAL_IDENTITY_V0_1",
        "parent_catalog": _logical_file_identity(input_bindings["parent_catalog"]),
        "parent_ledger_manifest": _logical_file_identity(
            input_bindings["parent_ledger_manifest"]
        ),
        "parent_ledger_events": {
            "exists": input_bindings["parent_ledger_events"]["exists"],
            **_logical_file_identity(input_bindings["parent_ledger_events"]),
        },
    }
    parent_bytes = sum(
        member["bytes"]
        for member in (
            parent_members["parent_catalog"],
            parent_members["parent_ledger_manifest"],
            parent_members["parent_ledger_events"],
        )
    )
    return {
        "schema_version": LOGICAL_SOURCE_IDENTITY_SCHEMA_VERSION,
        "inputs": [
            {
                "role": "B21_CATALOG",
                **_logical_file_identity(input_bindings["catalog"]),
            },
            {
                "role": "B21_GUARD_REUSE",
                **_logical_file_identity(input_bindings["guard_reuse"]),
            },
            {
                "role": "GOVERNED_PARENT_LEDGER",
                "bytes": parent_bytes,
                "sha256": canonical_sha256(parent_members),
            },
        ],
        "canonical_inventory_package": dict(
            input_bindings["canonical_g01a_package"]
        ),
    }


def _read_jsonl(path: Path, *, role: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise BoundedB21IngestError(f"{role} must not contain a UTF-8 BOM")
    if not raw or not raw.endswith(b"\n"):
        raise BoundedB21IngestError(f"{role} must be nonempty and end with LF")
    records: list[dict[str, Any]] = []
    for number, line in enumerate(raw.splitlines(), start=1):
        if not line:
            raise BoundedB21IngestError(f"{role} contains blank line {number}")
        try:
            value = strict_json_loads(line)
        except Exception as error:
            raise BoundedB21IngestError(
                f"{role} line {number} is not strict JSON: {error}"
            ) from error
        if not isinstance(value, dict):
            raise BoundedB21IngestError(f"{role} line {number} must be an object")
        records.append(value)
    return records, {
        "path": str(path),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "record_count": len(records),
    }


def _require_string_list(value: Any, *, field: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(child, str) or not child for child in value
    ):
        raise BoundedB21IngestError(f"{field} must be a list of nonempty strings")
    if len(value) != len(set(value)):
        raise BoundedB21IngestError(f"{field} must not contain duplicates")
    return list(value)


def _require_attribute_map(
    value: Any, *, field: str, expected_keys: frozenset[str]
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise BoundedB21IngestError(f"{field} must be an object")
    try:
        require_exact_keys(value, expected_keys, field=field)
    except Exception as error:
        raise BoundedB21IngestError(str(error)) from error
    if any(
        child is not True
        and child is not False
        and (not isinstance(child, str) or not child)
        for child in value.values()
    ):
        raise BoundedB21IngestError(
            f"{field} values must be booleans or nonempty strings"
        )
    return dict(value)


def _validate_catalog_record(value: dict[str, Any], *, index: int) -> dict[str, Any]:
    field = f"catalog[{index}]"
    try:
        require_exact_keys(value, CATALOG_FIELDS, field=field)
        for name in (
            "accepted_review_role",
            "anchor_code",
            "human_correction_status",
            "inventory_file_id",
            "review_evidence_class",
            "rights_status",
        ):
            require_nonempty_string(value[name], field=f"{field}.{name}")
    except Exception as error:
        raise BoundedB21IngestError(str(error)) from error
    if not isinstance(value["active_generation_input_allowed"], bool):
        raise BoundedB21IngestError(
            f"{field}.active_generation_input_allowed must be boolean"
        )
    _require_string_list(value["negative_guards"], field=f"{field}.negative_guards")
    _require_string_list(value["source_evidence"], field=f"{field}.source_evidence")
    _require_string_list(value["uncertainty"], field=f"{field}.uncertainty")
    _require_attribute_map(
        value["causal_family_relation"],
        field=f"{field}.causal_family_relation",
        expected_keys=CAUSAL_FIELDS,
    )
    _require_attribute_map(
        value["reference_use_surface"],
        field=f"{field}.reference_use_surface",
        expected_keys=REFERENCE_FIELDS,
    )
    for name in (
        "contact_force_reaction_positive_claim",
        "weapon_clash_positive_claim",
    ):
        child = value[name]
        if child is not True and child is not False and (
            not isinstance(child, str) or not child
        ):
            raise BoundedB21IngestError(
                f"{field}.{name} must be boolean or nonempty string"
            )
    return json.loads(canonical_json_bytes(value).decode("utf-8"))


def _validate_guard_record(value: dict[str, Any], *, index: int) -> dict[str, Any]:
    field = f"guard_reuse[{index}]"
    try:
        require_exact_keys(value, GUARD_FIELDS, field=field)
        for name in (
            "anchor_code",
            "inventory_file_id",
            "negative_guard_status",
            "review_evidence_class",
            "rights_status",
        ):
            require_nonempty_string(value[name], field=f"{field}.{name}")
    except Exception as error:
        raise BoundedB21IngestError(str(error)) from error
    if not isinstance(value["active_generation_input_allowed"], bool):
        raise BoundedB21IngestError(
            f"{field}.active_generation_input_allowed must be boolean"
        )
    _require_string_list(value["negative_guards"], field=f"{field}.negative_guards")
    _require_attribute_map(
        value["causal_family_relation"],
        field=f"{field}.causal_family_relation",
        expected_keys=CAUSAL_FIELDS,
    )
    _require_attribute_map(
        value["reference_use_surface"],
        field=f"{field}.reference_use_surface",
        expected_keys=REFERENCE_FIELDS,
    )
    return json.loads(canonical_json_bytes(value).decode("utf-8"))


def _validate_b21_inputs(
    catalog_values: Sequence[dict[str, Any]],
    guard_values: Sequence[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    if len(catalog_values) != 12:
        raise BoundedB21IngestError("B21 catalog must contain exactly 12 records")
    if len(guard_values) != 12:
        raise BoundedB21IngestError("B21 guard/reuse file must contain exactly 12 records")
    catalog = [
        _validate_catalog_record(dict(value), index=index)
        for index, value in enumerate(catalog_values, start=1)
    ]
    guards = [
        _validate_guard_record(dict(value), index=index)
        for index, value in enumerate(guard_values, start=1)
    ]
    catalog_ids = [row["inventory_file_id"] for row in catalog]
    guard_ids = [row["inventory_file_id"] for row in guards]
    anchors = [row["anchor_code"] for row in catalog]
    if len(catalog_ids) != len(set(catalog_ids)):
        raise BoundedB21IngestError("B21 catalog inventory targets must be unique")
    if len(guard_ids) != len(set(guard_ids)):
        raise BoundedB21IngestError("B21 guard/reuse inventory targets must be unique")
    if len(anchors) != len(set(anchors)):
        raise BoundedB21IngestError("B21 catalog anchor codes must be unique")
    if set(catalog_ids) != set(guard_ids):
        raise BoundedB21IngestError("B21 catalog and guard/reuse target coverage differs")
    guard_by_id = {row["inventory_file_id"]: row for row in guards}
    shared_fields = (
        "anchor_code",
        "active_generation_input_allowed",
        "causal_family_relation",
        "negative_guards",
        "reference_use_surface",
        "review_evidence_class",
        "rights_status",
    )
    for row in catalog:
        guard = guard_by_id[row["inventory_file_id"]]
        if any(row[field] != guard[field] for field in shared_fields):
            raise BoundedB21IngestError(
                f"B21 catalog/guard join differs for {row['inventory_file_id']}"
            )
    observed_classes = Counter(row["review_evidence_class"] for row in catalog)
    if dict(observed_classes) != EXPECTED_CLASS_COUNTS:
        raise BoundedB21IngestError("B21 review evidence class distribution differs")
    if sum(bool(row["negative_guards"]) for row in catalog) != 6:
        raise BoundedB21IngestError("B21 guarded-row count must equal 6")
    if any(row["rights_status"] != "UNKNOWN_NOT_RECORDED" for row in catalog):
        raise BoundedB21IngestError("B21 rights must remain UNKNOWN_NOT_RECORDED")
    if any(row["active_generation_input_allowed"] is not False for row in catalog):
        raise BoundedB21IngestError("B21 active generation input must remain denied")
    b040 = [row for row in catalog if row["anchor_code"] == "B040"]
    if len(b040) != 1 or b040[0]["inventory_file_id"] != B040_INVENTORY_FILE_ID:
        raise BoundedB21IngestError("B040 identity binding differs")
    b040_row = b040[0]
    if (
        b040_row["review_evidence_class"] != "POSITIVE"
        or b040_row["reference_use_surface"]["spatial_choreography_reference"]
        is not True
        or b040_row["contact_force_reaction_positive_claim"] is not False
        or b040_row["weapon_clash_positive_claim"] is not False
    ):
        raise BoundedB21IngestError("B040 bounded semantics differ")
    return catalog, guard_by_id


def _payload(row: Mapping[str, Any], guard: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "observation_type": OBSERVATION_TYPE,
        "statement": (
            f"B21 reviewed public anchor {row['anchor_code']} "
            f"{row['accepted_review_role']} {row['review_evidence_class']}"
        ),
        "b21_anchor_code": row["anchor_code"],
        "inventory_file_id": row["inventory_file_id"],
        "accepted_review_role": row["accepted_review_role"],
        "review_evidence_class": row["review_evidence_class"],
        "negative_guards": row["negative_guards"],
        "negative_guard_status": guard["negative_guard_status"],
        "causal_family_relation": row["causal_family_relation"],
        "reference_use_surface": row["reference_use_surface"],
        "source_evidence": row["source_evidence"],
        "uncertainty": row["uncertainty"],
        "human_correction_status": row["human_correction_status"],
        "contact_force_reaction_positive_claim": row[
            "contact_force_reaction_positive_claim"
        ],
        "weapon_clash_positive_claim": row["weapon_clash_positive_claim"],
        "rights_status": row["rights_status"],
        "active_generation_input_allowed": row[
            "active_generation_input_allowed"
        ],
    }


def _write_exclusive(path: Path, data: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    descriptor = os.open(path, flags, 0o600)
    try:
        view = memoryview(data)
        written = 0
        while written < len(view):
            count = os.write(descriptor, view[written:])
            if count <= 0:
                raise OSError("durable B21 write made no progress")
            written += count
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    _write_exclusive(path, canonical_json_bytes(dict(value)) + b"\n")


def _write_entries(path: Path, entries: Sequence[SuccessorEntry]) -> None:
    raw = b"".join(canonical_json_bytes(entry.to_dict()) + b"\n" for entry in entries)
    _write_exclusive(path, raw)


def _read_canonical_json(path: Path, *, role: str) -> dict[str, Any]:
    raw = path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise BoundedB21IngestError(f"{role} must have exactly one terminal LF")
    value = strict_json_loads(raw)
    if not isinstance(value, dict) or raw != canonical_json_bytes(value) + b"\n":
        raise BoundedB21IngestError(f"{role} is not canonical JSON")
    return value


def _reload_successor_bundle(
    staging_root: Path,
) -> tuple[dict[str, Any], dict[str, Any], tuple[SuccessorEntry, ...]]:
    successor_root = staging_root / "successor"
    parent_binding = _read_canonical_json(
        successor_root / "parent_binding.json", role="durable parent binding"
    )
    successor_manifest = _read_canonical_json(
        successor_root / "successor_manifest.json", role="durable successor manifest"
    )
    raw = (successor_root / "successor_entries.jsonl").read_bytes()
    if not raw or not raw.endswith(b"\n"):
        raise BoundedB21IngestError("durable successor entries must end with LF")
    entries: list[SuccessorEntry] = []
    for number, line in enumerate(raw.splitlines(), start=1):
        if not line:
            raise BoundedB21IngestError(
                f"durable successor entries contain blank line {number}"
            )
        value = strict_json_loads(line)
        if not isinstance(value, dict) or line != canonical_json_bytes(value):
            raise BoundedB21IngestError(
                f"durable successor entry {number} is not canonical JSON"
            )
        entries.append(SuccessorEntry(value))
    return parent_binding, successor_manifest, tuple(entries)


def _verify_queries(
    generation_path: Path,
    catalog: Sequence[dict[str, Any]],
    guard_by_id: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    expected_payloads = {
        row["inventory_file_id"]: _payload(row, guard_by_id[row["inventory_file_id"]])
        for row in catalog
    }
    exact_lookup_verified = True
    payload_reconstruction_pass = True
    authority_leakage_count = 0
    observed_by_id: dict[str, dict[str, Any]] = {}
    for inventory_id, expected_payload in expected_payloads.items():
        rows = query_typed_observations(
            generation_path,
            TypedObservationQuery(inventory_file_ids=(inventory_id,)),
        )
        if len(rows) != 1:
            exact_lookup_verified = False
            continue
        row = rows[0]
        observed_by_id[inventory_id] = row
        if row["authority_class"] != "OBSERVATION_ONLY":
            authority_leakage_count += 1
        try:
            observed_payload = strict_json_loads(row["payload_json"])
        except Exception:
            payload_reconstruction_pass = False
            continue
        if observed_payload != expected_payload:
            payload_reconstruction_pass = False

    class_facets = {
        evidence_class: len(
            query_typed_observations(
                generation_path,
                TypedObservationQuery(
                    target_kinds=(TARGET_KIND_INVENTORY_ASSET,),
                    review_evidence_classes=(evidence_class,),
                ),
            )
        )
        for evidence_class in EXPECTED_CLASS_COUNTS
    }
    role_counts = Counter(row["accepted_review_role"] for row in catalog)
    role_facets = {
        role: len(
            query_typed_observations(
                generation_path,
                TypedObservationQuery(
                    target_kinds=(TARGET_KIND_INVENTORY_ASSET,),
                    accepted_review_roles=(role,),
                ),
            )
        )
        for role in sorted(role_counts)
    }
    anchor_facets = {
        row["anchor_code"]: len(
            query_typed_observations(
                generation_path,
                TypedObservationQuery(
                    target_kinds=(TARGET_KIND_INVENTORY_ASSET,),
                    anchor_codes=(row["anchor_code"],),
                ),
            )
        )
        for row in catalog
    }
    expected_guard_ids: dict[str, set[str]] = {}
    for row in catalog:
        for guard in row["negative_guards"]:
            expected_guard_ids.setdefault(guard, set()).add(row["inventory_file_id"])
    guard_facets: dict[str, int] = {}
    negative_guard_verified = True
    for guard, expected_ids in sorted(expected_guard_ids.items()):
        rows = query_typed_observations(
            generation_path,
            TypedObservationQuery(
                target_kinds=(TARGET_KIND_INVENTORY_ASSET,),
                exact_attributes=(("negative_guards[]", guard),)
            ),
        )
        guard_facets[guard] = len(rows)
        if {row["inventory_file_id"] for row in rows} != expected_ids:
            negative_guard_verified = False
    fts_rows = query_typed_observations(
        generation_path,
        TypedObservationQuery(
            target_kinds=(TARGET_KIND_INVENTORY_ASSET,), text="B21"
        ),
    )
    b040_payload = None
    if B040_INVENTORY_FILE_ID in observed_by_id:
        b040_payload = strict_json_loads(
            observed_by_id[B040_INVENTORY_FILE_ID]["payload_json"]
        )
    b040_pass = bool(
        b040_payload
        and b040_payload["review_evidence_class"] == "POSITIVE"
        and b040_payload["reference_use_surface"][
            "spatial_choreography_reference"
        ]
        is True
        and b040_payload["contact_force_reaction_positive_claim"] is False
        and b040_payload["weapon_clash_positive_claim"] is False
        and b040_payload["rights_status"] == "UNKNOWN_NOT_RECORDED"
    )
    rights_unknown_count = sum(
        payload["rights_status"] == "UNKNOWN_NOT_RECORDED"
        for payload in expected_payloads.values()
    )
    active_generation_allowed_count = sum(
        payload["active_generation_input_allowed"] is True
        for payload in expected_payloads.values()
    )
    evidence_class_verified = class_facets == EXPECTED_CLASS_COUNTS
    role_facet_verified = role_facets == dict(sorted(role_counts.items()))
    anchor_facet_verified = all(value == 1 for value in anchor_facets.values())
    fts_verified = len(fts_rows) == 12
    result = {
        "exact_lookup_verified": exact_lookup_verified,
        "role_facet_verified": role_facet_verified,
        "evidence_class_verified": evidence_class_verified,
        "anchor_facet_verified": anchor_facet_verified,
        "class_facets": class_facets,
        "role_facets": role_facets,
        "anchor_facets": anchor_facets,
        "negative_guard_verified": negative_guard_verified,
        "guard_facets": guard_facets,
        "fts_verified": fts_verified,
        "fts_result_count": len(fts_rows),
        "semantic_reconstruction_pass": payload_reconstruction_pass,
        "rights_unknown_count": rights_unknown_count,
        "active_generation_allowed_count": active_generation_allowed_count,
        "authority_leakage_count": authority_leakage_count,
        "b040_verification_pass": b040_pass,
    }
    required = (
        result["exact_lookup_verified"],
        result["role_facet_verified"],
        result["evidence_class_verified"],
        result["anchor_facet_verified"],
        result["negative_guard_verified"],
        result["fts_verified"],
        result["semantic_reconstruction_pass"],
        result["rights_unknown_count"] == 12,
        result["active_generation_allowed_count"] == 0,
        result["authority_leakage_count"] == 0,
        result["b040_verification_pass"],
    )
    if not all(required):
        raise BoundedB21IngestError("typed B21 query verification failed")
    return result


def run_bounded_b21_ingest(
    *,
    catalog_path: str | Path,
    guard_reuse_path: str | Path,
    parent_catalog_path: str | Path,
    parent_ledger_path: str | Path,
    package_filename: str,
    package_bytes: int,
    package_sha256: str,
    output_root: str | Path,
    protection_policy: RuntimeStateProtectionPolicy,
    created_by: str,
    created_at: str,
    actor: Mapping[str, Any],
    occurred_at: str,
    recorded_at: str,
) -> dict[str, Any]:
    """Ingest the exact governed B21 12-row surface into one immutable generation."""

    catalog_file = _require_regular_file(catalog_path, role="B21 catalog")
    guard_file = _require_regular_file(guard_reuse_path, role="B21 guard/reuse")
    parent_catalog_file = _require_regular_file(
        parent_catalog_path, role="parent catalog package"
    )
    parent_ledger = Path(parent_ledger_path)
    if not parent_ledger.is_absolute() or not parent_ledger.is_dir():
        raise BoundedB21IngestError(
            "parent ledger must be an explicit existing directory"
        )
    if parent_ledger.is_symlink() or _is_reparse_point(parent_ledger):
        raise BoundedB21IngestError("parent ledger may not be a link or reparse point")
    final_root = validate_state_root(output_root, protection_policy=protection_policy)
    staging_root = validate_state_root(
        final_root.with_name(final_root.name + ".partial"),
        protection_policy=protection_policy,
    )
    if final_root.exists():
        raise BoundedB21IngestError("bounded B21 output root already exists")
    if staging_root.exists():
        raise BoundedB21IngestError("bounded B21 staging root already exists")

    catalog_values, catalog_identity = _read_jsonl(catalog_file, role="B21 catalog")
    guard_values, guard_identity = _read_jsonl(
        guard_file, role="B21 guard/reuse"
    )
    catalog, guard_by_id = _validate_b21_inputs(catalog_values, guard_values)
    inventory_ids = [row["inventory_file_id"] for row in catalog]
    registry = build_inventory_identity_registry(
        inventory_ids,
        package_filename=package_filename,
        package_bytes=package_bytes,
        package_sha256=package_sha256,
        source_evidence_identities=sorted(
            {
                f"B21-CATALOG-SHA256:{catalog_identity['sha256']}",
                f"B21-GUARD-REUSE-SHA256:{guard_identity['sha256']}",
                f"G01A-PACKAGE-SHA256:{package_sha256}",
            }
        ),
    )

    adapter = load_base_catalog(parent_catalog_file)
    parent_manifest, parent_entries = load_validated_ledger(parent_ledger, adapter)
    parent_projection = replay_entries(parent_manifest, adapter, parent_entries)
    parent_binding = build_parent_binding(
        parent_manifest, parent_entries, parent_projection
    )
    successor_manifest = build_successor_manifest(
        parent_binding,
        registry,
        created_by=created_by,
        created_at=created_at,
    )
    known_pilots = tuple(sorted(parent_projection.to_dict()["records"]))
    successor_entries: tuple[SuccessorEntry, ...] = ()
    actor_value = dict(actor)
    for row in catalog:
        current = replay_successor_entries(
            successor_manifest,
            successor_entries,
            known_pilot_clip_ids=known_pilots,
        )
        source_trace_ids = sorted(
            set(row["source_evidence"])
            | {
                f"B21-CATALOG-SHA256:{catalog_identity['sha256']}",
                f"B21-GUARD-REUSE-SHA256:{guard_identity['sha256']}",
            }
        )
        draft = {
            "event_type": REVIEW_OBSERVATION_ADDED,
            "event_schema_version": SUCCESSOR_EVENT_SCHEMA_VERSION,
            "target_identity": build_target_identity(
                TARGET_KIND_INVENTORY_ASSET, row["inventory_file_id"]
            ),
            "actor": actor_value,
            "authority_class": "OBSERVATION_ONLY",
            "occurred_at": occurred_at,
            "recorded_at": recorded_at,
            "source_trace_ids": source_trace_ids,
            "precondition_projection_hash": current.projection_hash,
            "supersedes_event_ids": [],
            "payload": _payload(row, guard_by_id[row["inventory_file_id"]]),
        }
        successor_entries = append_successor_event_candidate(
            successor_manifest,
            successor_entries,
            draft,
            known_pilot_clip_ids=known_pilots,
        )

    parent_manifest_path = parent_ledger.resolve(strict=True) / "ledger_manifest.json"
    parent_events_path = parent_ledger.resolve(strict=True) / "events.jsonl"
    input_bindings = {
        "schema_version": INPUT_BINDING_SCHEMA_VERSION,
        "catalog": catalog_identity,
        "guard_reuse": guard_identity,
        "parent_catalog": _file_identity(parent_catalog_file),
        "parent_ledger_manifest": _file_identity(
            _require_regular_file(parent_manifest_path, role="parent ledger manifest")
        ),
        "parent_ledger_events": _optional_file_identity(parent_events_path),
        "canonical_g01a_package": {
            "filename": package_filename,
            "bytes": package_bytes,
            "sha256": package_sha256,
        },
        "catalog_record_count": len(catalog),
        "guard_record_count": len(guard_by_id),
        "inventory_target_count": len(inventory_ids),
        "class_counts": dict(Counter(row["review_evidence_class"] for row in catalog)),
        "guarded_row_count": sum(bool(row["negative_guards"]) for row in catalog),
    }
    logical_source_identity = _logical_source_identity(input_bindings)
    builder_source_identity = canonical_sha256(logical_source_identity)

    finalized = False
    try:
        staging_root.mkdir(parents=True, exist_ok=False)
        successor_root = staging_root / "successor"
        successor_root.mkdir()
        _write_json(staging_root / "input_bindings.json", input_bindings)
        _write_json(successor_root / "parent_binding.json", parent_binding)
        _write_json(
            successor_root / "successor_manifest.json", successor_manifest
        )
        _write_entries(
            successor_root / "successor_entries.jsonl", successor_entries
        )

        expected_parent_binding = parent_binding
        expected_entry_count = len(successor_entries)
        del parent_binding
        del successor_manifest
        del successor_entries

        (
            durable_parent_binding,
            durable_successor_manifest,
            durable_successor_entries,
        ) = _reload_successor_bundle(staging_root)
        if durable_parent_binding != expected_parent_binding:
            raise BoundedB21IngestError("durable parent binding differs")
        if durable_successor_manifest.get("parent_binding") != durable_parent_binding:
            raise BoundedB21IngestError("durable successor parent binding differs")
        if len(durable_successor_entries) != expected_entry_count:
            raise BoundedB21IngestError("durable successor entry count differs")
        replay_successor_entries(
            durable_successor_manifest,
            durable_successor_entries,
            known_pilot_clip_ids=known_pilots,
        )
        mixed = replay_parent_and_successor(
            parent_manifest,
            adapter,
            parent_entries,
            durable_successor_manifest,
            durable_successor_entries,
        )
        if mixed.successor_projection.to_dict()["event_count"] != 12:
            raise BoundedB21IngestError("durable successor replay count differs")

        parent_mapped = map_projection(
            adapter,
            parent_manifest,
            parent_entries,
            parent_projection,
            builder_source_identity=builder_source_identity,
        )
        typed_rows = map_successor_observations(
            parent_manifest,
            adapter,
            parent_entries,
            durable_successor_manifest,
            durable_successor_entries,
        )
        typed_result = build_typed_observation_generation(
            staging_root / "typed_state",
            parent_mapped,
            typed_rows,
            protection_policy=protection_policy,
            parent_manifest=parent_manifest,
            adapter=adapter,
            parent_entries=parent_entries,
            successor_manifest=durable_successor_manifest,
            successor_entries=durable_successor_entries,
        )
        typed_verification = verify_typed_generation(typed_result.generation_path)
        query_verification = _verify_queries(
            typed_result.generation_path, catalog, guard_by_id
        )
        final_generation_path = (
            final_root / "typed_state" / typed_result.generation_path.name
        )
        receipt = {
            "schema_version": INGEST_RECEIPT_SCHEMA_VERSION,
            "catalog_parent_identity": catalog_identity,
            "guard_reuse_parent_identity": guard_identity,
            "governed_parent_ledger_identity": {
                "manifest": input_bindings["parent_ledger_manifest"],
                "events": input_bindings["parent_ledger_events"],
            },
            "canonical_g01a_package": input_bindings["canonical_g01a_package"],
            "logical_source_identity": logical_source_identity,
            "builder_source_identity": builder_source_identity,
            "catalog_record_count": 12,
            "guard_reuse_record_count": 12,
            "inventory_target_count": 12,
            "successor_event_count": 12,
            "durable_replay_verified": True,
            "typed_inventory_asset_count": typed_verification[
                "inventory_asset_count"
            ],
            "typed_observation_count": typed_verification["observation_count"],
            "generation_path": str(final_generation_path),
            "logical_content_hash": typed_result.logical_content_hash,
            "materialization_generation_id": (
                typed_result.materialization_generation_id
            ),
            "exact_lookup_verified": query_verification[
                "exact_lookup_verified"
            ],
            "role_facet_verified": query_verification["role_facet_verified"],
            "evidence_class_verified": query_verification[
                "evidence_class_verified"
            ],
            "negative_guard_verified": query_verification[
                "negative_guard_verified"
            ],
            "fts_verified": query_verification["fts_verified"],
            "semantic_reconstruction_pass": query_verification[
                "semantic_reconstruction_pass"
            ],
            "rights_unknown_count": query_verification["rights_unknown_count"],
            "active_generation_allowed_count": query_verification[
                "active_generation_allowed_count"
            ],
            "authority_leakage_count": query_verification[
                "authority_leakage_count"
            ],
            "b040_verification_pass": query_verification[
                "b040_verification_pass"
            ],
            "query_verification": query_verification,
            "pointer_created": False,
            "promotion_performed": False,
        }
        _write_json(staging_root / "ingest_receipt.json", receipt)
        os.rename(staging_root, final_root)
        finalized = True
        return receipt
    except Exception:
        if not finalized and staging_root.exists():
            shutil.rmtree(staging_root)
        raise


__all__ = [
    "B040_INVENTORY_FILE_ID",
    "BoundedB21IngestError",
    "INGEST_RECEIPT_SCHEMA_VERSION",
    "run_bounded_b21_ingest",
]
