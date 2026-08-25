from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index import (
    bounded_b21_ingest as bounded,
)
from app.ai_video_pipeline.reference_library.persistent_index.bounded_b21_ingest import (
    B040_INVENTORY_FILE_ID,
    BoundedB21IngestError,
    run_bounded_b21_ingest,
)
from app.ai_video_pipeline.reference_library.event_ledger import (
    initialize_manifest,
    load_base_catalog,
)
from app.ai_video_pipeline.reference_library.event_ledger.canonical import (
    canonical_json_bytes,
    strict_json_loads,
)
from app.ai_video_pipeline.reference_library.persistent_index import (
    TypedObservationQuery,
    TypedObservationRows,
    query_typed_observations,
)
from app.ai_video_pipeline.reference_library.persistent_index.builder import (
    RuntimeStateProtectionPolicy,
)
from app.ai_video_pipeline.reference_library.persistent_index.typed_observation import (
    TypedObservationIndexError,
)


PROJECT_ROOT = Path(__file__).parents[2]
FIXTURE_PATH = (
    PROJECT_ROOT
    / "tests"
    / "reference_library"
    / "fixtures"
    / "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_CANDIDATE_V0_1.zip"
)
PACKAGE_FILENAME = "AI_VIDEO_PURCHASED_MATERIALS_G01A_FILESYSTEM_INVENTORY_V0_1.zip"
PACKAGE_BYTES = 4754
PACKAGE_SHA256 = "18123374e871d9123827b27185adc75476ded8244388429a5d58b00e7b41e08c"


def _records() -> tuple[list[dict], list[dict]]:
    identifiers = [B040_INVENTORY_FILE_ID] + [
        f"G01A-F-{index:032X}" for index in range(1, 12)
    ]
    classes = (
        "POSITIVE",
        "POSITIVE",
        "POSITIVE",
        "POSITIVE",
        "PARTIAL_OR_AMBIGUOUS",
        "HARD_NEGATIVE",
        "HARD_NEGATIVE",
        "HARD_NEGATIVE",
        "HARD_NEGATIVE",
        "HARD_NEGATIVE",
        "NON_CAUSAL_REFERENCE",
        "NON_CAUSAL_REFERENCE",
    )
    catalog: list[dict] = []
    guards: list[dict] = []
    for index, (inventory_id, evidence_class) in enumerate(
        zip(identifiers, classes, strict=True)
    ):
        anchor = "B040" if index == 0 else f"T{index:03d}"
        negative_guards = [f"NOT_SYNTHETIC_{index:02d}"] if 5 <= index <= 10 else []
        causal = {
            "CF1_CONTACT_FORCE_REACTION": "AMBIGUOUS"
            if index == 0
            else "NOT_ASSESSED",
            "CF2_WEAPON_CLASH_GUARD": "NOT_ASSESSED",
            "CF3_PURSUIT_CHASE": "NOT_ASSESSED",
        }
        reference = {
            "action_grammar_reference": evidence_class == "POSITIVE" and index != 0,
            "spatial_choreography_reference": index == 0,
            "hard_negative_guard_reference": bool(negative_guards),
            "destruction_or_effect_reference": False,
            "locomotion_reference": False,
        }
        row = {
            "accepted_review_role": f"SYNTHETIC_ROLE_{index:02d}",
            "active_generation_input_allowed": False,
            "anchor_code": anchor,
            "causal_family_relation": causal,
            "contact_force_reaction_positive_claim": False
            if index == 0
            else "UNKNOWN_NOT_RECORDED",
            "human_correction_status": "NONE_REQUIRED",
            "inventory_file_id": inventory_id,
            "negative_guards": negative_guards,
            "reference_use_surface": reference,
            "review_evidence_class": evidence_class,
            "rights_status": "UNKNOWN_NOT_RECORDED",
            "source_evidence": ["SYNTHETIC-B21-BOUND"],
            "uncertainty": ["NONE_RECORDED"],
            "weapon_clash_positive_claim": False
            if index == 0
            else "UNKNOWN_NOT_RECORDED",
        }
        catalog.append(row)
        guards.append(
            {
                "active_generation_input_allowed": False,
                "anchor_code": anchor,
                "causal_family_relation": causal,
                "inventory_file_id": inventory_id,
                "negative_guard_status": "PRESENT"
                if negative_guards
                else "UNKNOWN_NOT_RECORDED",
                "negative_guards": negative_guards,
                "reference_use_surface": reference,
                "review_evidence_class": evidence_class,
                "rights_status": "UNKNOWN_NOT_RECORDED",
            }
        )
    return catalog, guards


def _write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_bytes(
        b"".join(canonical_json_bytes(record) + b"\n" for record in records)
    )


def _prepare(
    tmp_path: Path, *, parent_catalog_path: Path = FIXTURE_PATH
) -> dict:
    tmp_path.mkdir(parents=True, exist_ok=True)
    catalog, guards = _records()
    catalog_path = tmp_path / "catalog.jsonl"
    guard_path = tmp_path / "guard.jsonl"
    _write_jsonl(catalog_path, catalog)
    _write_jsonl(guard_path, guards)
    adapter = load_base_catalog(parent_catalog_path)
    ledger = tmp_path / "parent-ledger"
    initialize_manifest(
        ledger,
        adapter,
        created_by="CODEX_B21_TEST",
        created_at="2026-08-25T00:00:00Z",
    )
    policy = RuntimeStateProtectionPolicy(
        repository_root=PROJECT_ROOT,
        source_root=tmp_path / "protected-source",
        media_roots=(tmp_path / "protected-media",),
    )
    return {
        "catalog": catalog,
        "guards": guards,
        "catalog_path": catalog_path,
        "guard_path": guard_path,
        "parent_catalog_path": parent_catalog_path,
        "ledger": ledger,
        "output": tmp_path / "bounded-output",
        "policy": policy,
    }


def _run(context: dict, **overrides):
    values = {
        "catalog_path": context["catalog_path"],
        "guard_reuse_path": context["guard_path"],
        "parent_catalog_path": context["parent_catalog_path"],
        "parent_ledger_path": context["ledger"],
        "package_filename": PACKAGE_FILENAME,
        "package_bytes": PACKAGE_BYTES,
        "package_sha256": PACKAGE_SHA256,
        "output_root": context["output"],
        "protection_policy": context["policy"],
        "created_by": "CODEX_B21_TEST",
        "created_at": "2026-08-25T00:01:00Z",
        "actor": {
            "actor_id": "CODEX-B21-TEST",
            "actor_type": "CODEX",
            "model_name": "SYNTHETIC",
            "model_version": "V0_1",
        },
        "occurred_at": "2026-08-25T00:02:00Z",
        "recorded_at": "2026-08-25T00:03:00Z",
    }
    values.update(overrides)
    return run_bounded_b21_ingest(**values)


def test_b21_t01_valid_synthetic_exact12_route(tmp_path: Path):
    context = _prepare(tmp_path)
    receipt = _run(context)
    assert receipt["catalog_record_count"] == 12
    assert receipt["successor_event_count"] == 12
    assert receipt["durable_replay_verified"] is True
    assert receipt["typed_inventory_asset_count"] == 12
    assert receipt["rights_unknown_count"] == 12
    assert receipt["exact_lookup_verified"] is True
    assert receipt["role_facet_verified"] is True
    assert receipt["evidence_class_verified"] is True
    assert receipt["negative_guard_verified"] is True
    assert receipt["fts_verified"] is True
    assert receipt["active_generation_allowed_count"] == 0
    assert receipt["promotion_performed"] is False
    for retired_alias in (
        "exact_lookup_pass",
        "facet_pass",
        "guard_query_pass",
        "fts_pass",
        "active_generation_true_count",
        "promotion",
    ):
        assert retired_alias not in receipt
    assert Path(receipt["generation_path"]).is_file()
    assert (context["output"] / "successor" / "successor_entries.jsonl").is_file()


def test_b21_t02_bad_catalog_count_rejected_before_output(tmp_path: Path):
    context = _prepare(tmp_path)
    context["catalog"].pop()
    _write_jsonl(context["catalog_path"], context["catalog"])
    with pytest.raises(BoundedB21IngestError, match="exactly 12"):
        _run(context)
    assert not context["output"].exists()


def test_b21_t03_guard_target_mismatch_rejected(tmp_path: Path):
    context = _prepare(tmp_path)
    context["guards"][-1]["inventory_file_id"] = "G01A-F-FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    _write_jsonl(context["guard_path"], context["guards"])
    with pytest.raises(BoundedB21IngestError, match="target coverage differs"):
        _run(context)
    assert not context["output"].exists()


def test_b21_t04_duplicate_catalog_target_rejected(tmp_path: Path):
    context = _prepare(tmp_path)
    context["catalog"][1]["inventory_file_id"] = context["catalog"][0][
        "inventory_file_id"
    ]
    _write_jsonl(context["catalog_path"], context["catalog"])
    with pytest.raises(BoundedB21IngestError, match="targets must be unique"):
        _run(context)
    assert not context["output"].exists()


def test_b21_t05_wrong_canonical_package_identity_rejected(tmp_path: Path):
    context = _prepare(tmp_path)
    with pytest.raises(Exception, match="canonical G01A package"):
        _run(context, package_sha256="0" * 64)
    assert not context["output"].exists()


def test_b21_t06_rights_must_remain_unknown(tmp_path: Path):
    context = _prepare(tmp_path)
    context["catalog"][0]["rights_status"] = "KNOWN"
    context["guards"][0]["rights_status"] = "KNOWN"
    _write_jsonl(context["catalog_path"], context["catalog"])
    _write_jsonl(context["guard_path"], context["guards"])
    with pytest.raises(BoundedB21IngestError, match="rights must remain"):
        _run(context)
    assert not context["output"].exists()


def test_b21_t07_active_generation_must_remain_denied(tmp_path: Path):
    context = _prepare(tmp_path)
    context["catalog"][0]["active_generation_input_allowed"] = True
    context["guards"][0]["active_generation_input_allowed"] = True
    _write_jsonl(context["catalog_path"], context["catalog"])
    _write_jsonl(context["guard_path"], context["guards"])
    with pytest.raises(BoundedB21IngestError, match="must remain denied"):
        _run(context)
    assert not context["output"].exists()


def test_b21_t08_tampered_durable_successor_fails_before_typed_finalization(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    context = _prepare(tmp_path)
    original = bounded._reload_successor_bundle

    def tamper_then_reload(staging_root: Path):
        path = staging_root / "successor" / "successor_entries.jsonl"
        lines = path.read_bytes().splitlines()
        value = strict_json_loads(lines[0])
        value["event"]["payload"]["rights_status"] = "TAMPERED"
        lines[0] = canonical_json_bytes(value)
        path.write_bytes(b"\n".join(lines) + b"\n")
        return original(staging_root)

    monkeypatch.setattr(bounded, "_reload_successor_bundle", tamper_then_reload)
    with pytest.raises(Exception, match="identity differs|hash differs"):
        _run(context)
    assert not context["output"].exists()
    assert not context["output"].with_name(context["output"].name + ".partial").exists()


def test_b21_t09_existing_output_root_is_never_overwritten(tmp_path: Path):
    context = _prepare(tmp_path)
    context["output"].mkdir()
    marker = context["output"] / "keep.txt"
    marker.write_text("keep", encoding="ascii")
    with pytest.raises(BoundedB21IngestError, match="already exists"):
        _run(context)
    assert marker.read_text(encoding="ascii") == "keep"


def test_b21_t10_raw_unverified_typed_rows_bypass_is_impossible():
    with pytest.raises(TypedObservationIndexError, match="verified"):
        TypedObservationRows()


def test_b21_t11_no_pointer_or_promotion_artifact_created(tmp_path: Path):
    context = _prepare(tmp_path)
    receipt = _run(context)
    names = {path.name for path in context["output"].rglob("*")}
    assert receipt["pointer_created"] is False
    assert receipt["promotion_performed"] is False
    assert "current_read_model.json" not in names
    assert len(list((context["output"] / "typed_state").glob("*.sqlite3"))) == 1


def test_b21_t12_classes_guards_and_b040_survive_roundtrip(tmp_path: Path):
    context = _prepare(tmp_path)
    receipt = _run(context)
    generation = Path(receipt["generation_path"])
    positive = query_typed_observations(
        generation,
        TypedObservationQuery(review_evidence_classes=("POSITIVE",)),
    )
    guarded = query_typed_observations(
        generation,
        TypedObservationQuery(
            exact_attributes=(("negative_guards[]", "NOT_SYNTHETIC_05"),)
        ),
    )
    b040 = query_typed_observations(
        generation,
        TypedObservationQuery(inventory_file_ids=(B040_INVENTORY_FILE_ID,)),
    )
    payload = json.loads(b040[0]["payload_json"])
    assert len(positive) == 4
    assert len(guarded) == 1
    assert payload["review_evidence_class"] == "POSITIVE"
    assert payload["reference_use_surface"]["spatial_choreography_reference"] is True
    assert payload["contact_force_reaction_positive_claim"] is False
    assert payload["weapon_clash_positive_claim"] is False
    assert payload["rights_status"] == "UNKNOWN_NOT_RECORDED"


def test_b21_t13_import_origin_is_app_and_wrong_src_path_is_absent(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "app"))
    spec = importlib.util.find_spec(
        "ai_video_pipeline.reference_library.persistent_index.bounded_b21_ingest"
    )
    assert spec is not None and spec.origin is not None
    assert Path(spec.origin).resolve() == (
        PROJECT_ROOT
        / "app"
        / "ai_video_pipeline"
        / "reference_library"
        / "persistent_index"
        / "bounded_b21_ingest.py"
    ).resolve()
    assert not (
        PROJECT_ROOT
        / "src"
        / "ai_video_pipeline"
        / "reference_library"
        / "bounded_b21_ingest.py"
    ).exists()


def test_b21_t14_logical_identity_is_path_independent_and_content_sensitive(
    tmp_path: Path,
):
    contexts = []
    for location in ("location-a", "location-b", "location-content-change"):
        root = tmp_path / location
        root.mkdir()
        parent_catalog = root / FIXTURE_PATH.name
        parent_catalog.write_bytes(FIXTURE_PATH.read_bytes())
        contexts.append(_prepare(root, parent_catalog_path=parent_catalog))

    changed = contexts[2]
    changed["catalog"][1]["source_evidence"] = ["SYNTHETIC-B21-CONTENT-CHANGE"]
    _write_jsonl(changed["catalog_path"], changed["catalog"])

    receipt_a, receipt_b, receipt_changed = (_run(context) for context in contexts)
    assert receipt_a["builder_source_identity"] == receipt_b[
        "builder_source_identity"
    ]
    assert receipt_a["materialization_generation_id"] == receipt_b[
        "materialization_generation_id"
    ]
    assert receipt_a["logical_content_hash"] == receipt_b["logical_content_hash"]
    assert receipt_a["builder_source_identity"] != receipt_changed[
        "builder_source_identity"
    ]
    assert receipt_a["materialization_generation_id"] != receipt_changed[
        "materialization_generation_id"
    ]
    assert receipt_a["logical_content_hash"] != receipt_changed[
        "logical_content_hash"
    ]
    for receipt, context in zip(
        (receipt_a, receipt_b, receipt_changed), contexts, strict=True
    ):
        logical_text = json.dumps(receipt["logical_source_identity"], sort_keys=True)
        assert str(context["catalog_path"]) not in logical_text
        assert str(context["guard_path"]) not in logical_text
        assert str(context["ledger"]) not in logical_text
        assert str(context["output"]) not in logical_text
