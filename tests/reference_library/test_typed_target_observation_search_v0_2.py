from __future__ import annotations

import copy
import hashlib
import json
import sqlite3
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import (
    EVENT_SCHEMA_VERSION,
    EVENT_TYPE_REGISTRY,
    append_event,
    append_successor_event_candidate,
    build_inventory_identity_registry,
    build_parent_binding,
    build_successor_manifest,
    build_target_identity,
    initialize_manifest,
    load_base_catalog,
    load_validated_ledger,
    replay_entries,
    replay_parent_and_successor,
    replay_successor_entries,
    validate_inventory_identity_registry,
    validate_target_identity,
)
from app.ai_video_pipeline.reference_library.event_ledger.successor import (
    REVIEW_OBSERVATION_CORRECTED,
    SUCCESSOR_EVENT_SCHEMA_VERSION,
    SuccessorValidationError,
)
from app.ai_video_pipeline.reference_library.event_ledger.typed_targets import (
    TARGET_IDENTITY_SCHEMA_VERSION,
    TARGET_KIND_INVENTORY_ASSET,
    TARGET_KIND_PILOT_CLIP,
    TypedTargetValidationError,
)
from app.ai_video_pipeline.reference_library.persistent_index import (
    TypedObservationQuery,
    TypedObservationRows,
    build_typed_observation_generation,
    map_projection,
    map_successor_observations,
    query_typed_observations,
    verify_typed_generation,
)
from app.ai_video_pipeline.reference_library.persistent_index.builder import (
    RuntimeStateProtectionPolicy,
)
from app.ai_video_pipeline.reference_library.persistent_index.typed_observation import (
    TypedObservationIndexError,
    _canonical,
    _row_seal_body,
)


PROJECT_ROOT = Path(__file__).parents[2]
FIXTURE_PATH = (
    PROJECT_ROOT
    / "tests"
    / "reference_library"
    / "fixtures"
    / "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_CANDIDATE_V0_1.zip"
)
INVENTORY_IDS = tuple(f"G01A-F-{index:032X}" for index in range(1, 13))
PACKAGE_FILENAME = "AI_VIDEO_PURCHASED_MATERIALS_G01A_FILESYSTEM_INVENTORY_V0_1.zip"
PACKAGE_BYTES = 4754
PACKAGE_SHA256 = "18123374e871d9123827b27185adc75476ded8244388429a5d58b00e7b41e08c"


def _v1_event(projection_hash: str | None = None) -> dict:
    return {
        "event_type": "REVIEW_OBSERVATION_ADDED",
        "event_schema_version": EVENT_SCHEMA_VERSION,
        "pilot_clip_id": "G01D-CLIP-001",
        "target_ids": ["G01D-CLIP-001"],
        "actor": {
            "actor_id": "CODEX-B24-TEST",
            "actor_type": "CODEX",
            "model_name": "SYNTHETIC",
            "model_version": "V0_1",
        },
        "authority_class": EVENT_TYPE_REGISTRY["REVIEW_OBSERVATION_ADDED"],
        "occurred_at": "2026-08-24T00:00:00Z",
        "recorded_at": "2026-08-24T00:00:01Z",
        "source_trace_ids": ["TRACE-B24-PARENT"],
        "precondition_checkpoint_id": None,
        "precondition_projection_hash": projection_hash,
        "supersedes_event_ids": [],
        "retracts_event_ids": [],
        "payload": {
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": "unchanged V0.1 parent observation",
        },
    }


def _payload(index: int, *, unknown: bool = False) -> dict:
    return {
        "observation_type": "B21_REVIEWED_PUBLIC_ANCHOR_OBSERVATION_V0_1",
        "statement": f"anchor C{index:03d} typed observation action signal",
        "b21_anchor_code": f"C{index:03d}",
        "inventory_file_id": INVENTORY_IDS[index - 1],
        "accepted_review_role": "HARD_NEGATIVE" if index % 2 else "POSITIVE_REFERENCE",
        "review_evidence_class": "HARD_NEGATIVE" if index % 2 else "POSITIVE",
        "negative_guards": ["NOT_PURSUIT"] if index % 2 else [],
        "causal_family_relation": {
            "CF1_CONTACT_FORCE_REACTION": "UNKNOWN_NOT_RECORDED" if unknown else "NOT_ASSESSED",
            "CF2_WEAPON_CLASH_GUARD": "DOES_NOT_SUPPORT" if index % 2 else "NOT_ASSESSED",
            "CF3_PURSUIT_CHASE": "AMBIGUOUS" if index == 1 else "NOT_ASSESSED",
        },
        "reference_use_surface": {
            "action_grammar_reference": "AMBIGUOUS" if index == 1 else False,
            "spatial_choreography_reference": index % 2 == 0,
            "hard_negative_guard_reference": index % 2 == 1,
            "destruction_or_effect_reference": False,
            "locomotion_reference": False,
        },
        "source_evidence": ["B21-SYNTHETIC-BOUND"],
        "uncertainty": ["UNKNOWN_NOT_RECORDED"] if unknown else ["NONE_RECORDED"],
        "human_correction_status": "NONE_REQUIRED",
        "contact_force_reaction_positive_claim": "UNKNOWN_NOT_RECORDED",
        "weapon_clash_positive_claim": "UNKNOWN_NOT_RECORDED",
        "rights_status": "UNKNOWN_NOT_RECORDED",
        "active_generation_input_allowed": False,
    }


def _successor_draft(
    manifest: dict,
    projection_hash: str,
    inventory_id: str,
    payload: dict,
    *,
    event_type: str = "REVIEW_OBSERVATION_ADDED",
    supersedes: tuple[str, ...] = (),
    target_kind: str = TARGET_KIND_INVENTORY_ASSET,
    sequence: int = 1,
) -> dict:
    return {
        "event_type": event_type,
        "event_schema_version": SUCCESSOR_EVENT_SCHEMA_VERSION,
        "target_identity": build_target_identity(target_kind, inventory_id),
        "actor": {
            "actor_id": "CODEX-B24-TEST",
            "actor_type": "CODEX",
            "model_name": "SYNTHETIC",
            "model_version": "V0_2",
        },
        "authority_class": "OBSERVATION_ONLY",
        "occurred_at": f"2026-08-24T00:00:{sequence:02d}Z",
        "recorded_at": f"2026-08-24T00:01:{sequence:02d}Z",
        "source_trace_ids": [f"TRACE-B24-{sequence:03d}"],
        "precondition_projection_hash": projection_hash,
        "supersedes_event_ids": sorted(supersedes),
        "payload": payload,
    }


def _parent(tmp_path: Path, *, with_event: bool = True):
    adapter = load_base_catalog(FIXTURE_PATH)
    ledger = tmp_path / "parent-ledger"
    initialize_manifest(
        ledger,
        adapter,
        created_by="CODEX_B24_TEST",
        created_at="2026-08-24T00:00:00Z",
    )
    if with_event:
        append_event(ledger, adapter, _v1_event())
    manifest, entries = load_validated_ledger(ledger, adapter)
    projection = replay_entries(manifest, adapter, entries)
    return adapter, ledger, manifest, entries, projection


def _successor_context(tmp_path: Path, *, count: int = 2, unknown: bool = False):
    adapter, ledger, parent_manifest, parent_entries, parent_projection = _parent(tmp_path)
    registry = build_inventory_identity_registry(
        INVENTORY_IDS,
        package_filename=PACKAGE_FILENAME,
        package_bytes=PACKAGE_BYTES,
        package_sha256=PACKAGE_SHA256,
        source_evidence_identities=["B21-EXACT12", "G01A-INVENTORY-BOUND"],
    )
    parent_binding = build_parent_binding(parent_manifest, parent_entries, parent_projection)
    successor_manifest = build_successor_manifest(
        parent_binding,
        registry,
        created_by="CODEX_B24_TEST",
        created_at="2026-08-24T00:02:00Z",
    )
    pilots = tuple(sorted(parent_projection.to_dict()["records"]))
    successor_entries = ()
    for index in range(1, count + 1):
        current = replay_successor_entries(
            successor_manifest, successor_entries, known_pilot_clip_ids=pilots
        )
        draft = _successor_draft(
            successor_manifest,
            current.projection_hash,
            INVENTORY_IDS[index - 1],
            _payload(index, unknown=unknown and index == 1),
            sequence=index,
        )
        successor_entries = append_successor_event_candidate(
            successor_manifest,
            successor_entries,
            draft,
            known_pilot_clip_ids=pilots,
        )
    mixed = replay_parent_and_successor(
        parent_manifest,
        adapter,
        parent_entries,
        successor_manifest,
        successor_entries,
    )
    parent_mapped = map_projection(
        adapter,
        parent_manifest,
        parent_entries,
        parent_projection,
        builder_source_identity="c" * 64,
    )
    typed_rows = map_successor_observations(
        parent_manifest,
        adapter,
        parent_entries,
        successor_manifest,
        successor_entries,
    )
    return {
        "adapter": adapter,
        "ledger": ledger,
        "parent_manifest": parent_manifest,
        "parent_entries": parent_entries,
        "parent_projection": parent_projection,
        "successor_manifest": successor_manifest,
        "successor_entries": successor_entries,
        "successor_projection": mixed.successor_projection,
        "pilots": pilots,
        "parent_mapped": parent_mapped,
        "typed_rows": typed_rows,
    }


def _policy(tmp_path: Path) -> RuntimeStateProtectionPolicy:
    return RuntimeStateProtectionPolicy(
        repository_root=tmp_path / "protected-repository",
        source_root=tmp_path / "protected-source",
        media_roots=(tmp_path / "protected-media",),
    )


def _build(tmp_path: Path, context: dict, name: str = "typed-state"):
    return build_typed_observation_generation(
        tmp_path / name,
        context["parent_mapped"],
        context["typed_rows"],
        protection_policy=_policy(tmp_path),
        parent_manifest=context["parent_manifest"],
        adapter=context["adapter"],
        parent_entries=context["parent_entries"],
        successor_manifest=context["successor_manifest"],
        successor_entries=context["successor_entries"],
    )


def test_b23_t01_old_v0_1_ledger_bytes_and_hash_identity(tmp_path: Path):
    context = _successor_context(tmp_path)
    before = (context["ledger"] / "events.jsonl").read_bytes()
    before_hash = context["parent_entries"][-1].entry_hash
    replay_parent_and_successor(
        context["parent_manifest"],
        context["adapter"],
        context["parent_entries"],
        context["successor_manifest"],
        context["successor_entries"],
    )
    assert (context["ledger"] / "events.jsonl").read_bytes() == before
    assert context["parent_entries"][-1].entry_hash == before_hash


def test_b23_t02_old_v0_1_replay_is_reproducible(tmp_path: Path):
    context = _successor_context(tmp_path)
    replayed = replay_entries(
        context["parent_manifest"], context["adapter"], context["parent_entries"]
    )
    assert replayed.projection_hash == context["parent_projection"].projection_hash


def test_b23_t03_successor_parent_binding_fails_closed(tmp_path: Path):
    context = _successor_context(tmp_path)
    wrong = copy.deepcopy(context["successor_manifest"]["parent_binding"])
    wrong["parent_projection_hash"] = "f" * 64
    wrong_manifest = build_successor_manifest(
        wrong,
        context["successor_manifest"]["inventory_identity_registry"],
        created_by="CODEX_B24_TEST",
        created_at="2026-08-24T00:02:00Z",
    )
    with pytest.raises(SuccessorValidationError):
        replay_parent_and_successor(
            context["parent_manifest"],
            context["adapter"],
            context["parent_entries"],
            wrong_manifest,
            (),
        )


def test_b23_t04_target_kind_namespaces_are_not_collapsed():
    with pytest.raises(TypedTargetValidationError):
        validate_target_identity(
            {
                "target_schema_version": TARGET_IDENTITY_SCHEMA_VERSION,
                "target_kind": TARGET_KIND_PILOT_CLIP,
                "target_id": INVENTORY_IDS[0],
            }
        )
    with pytest.raises(TypedTargetValidationError):
        validate_target_identity(
            {
                "target_schema_version": TARGET_IDENTITY_SCHEMA_VERSION,
                "target_kind": "UNKNOWN_KIND",
                "target_id": INVENTORY_IDS[0],
            }
        )


def test_b23_t05_unbound_inventory_target_is_rejected(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    current = replay_successor_entries(
        context["successor_manifest"], (), known_pilot_clip_ids=context["pilots"]
    )
    unknown_id = "G01A-F-FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    draft = _successor_draft(
        context["successor_manifest"], current.projection_hash, unknown_id, _payload(1)
    )
    with pytest.raises(TypedTargetValidationError):
        append_successor_event_candidate(
            context["successor_manifest"],
            (),
            draft,
            known_pilot_clip_ids=context["pilots"],
        )


def test_b23_t06_exact12_registry_coverage_is_unique():
    registry = build_inventory_identity_registry(
        INVENTORY_IDS,
        package_filename=PACKAGE_FILENAME,
        package_bytes=PACKAGE_BYTES,
        package_sha256=PACKAGE_SHA256,
        source_evidence_identities=["B21-EXACT12"],
    )
    assert registry["record_count"] == 12
    assert [row["inventory_file_id"] for row in registry["records"]] == sorted(
        INVENTORY_IDS
    )


def test_b23_t07_mixed_parent_successor_replay_is_deterministic(tmp_path: Path):
    context = _successor_context(tmp_path)
    first = replay_parent_and_successor(
        context["parent_manifest"],
        context["adapter"],
        context["parent_entries"],
        context["successor_manifest"],
        context["successor_entries"],
    )
    second = replay_parent_and_successor(
        context["parent_manifest"],
        context["adapter"],
        context["parent_entries"],
        context["successor_manifest"],
        context["successor_entries"],
    )
    assert first.parent_projection.projection_hash == second.parent_projection.projection_hash
    assert first.successor_projection.projection_hash == second.successor_projection.projection_hash


def test_b23_t08_correction_supersedes_same_target_and_rejects_cross_kind(tmp_path: Path):
    context = _successor_context(tmp_path, count=1)
    current = context["successor_projection"]
    prior_id = context["successor_entries"][0].event["event_id"]
    corrected = _payload(1)
    corrected["statement"] = "corrected inventory observation"
    draft = _successor_draft(
        context["successor_manifest"],
        current.projection_hash,
        INVENTORY_IDS[0],
        corrected,
        event_type=REVIEW_OBSERVATION_CORRECTED,
        supersedes=(prior_id,),
        sequence=2,
    )
    entries = append_successor_event_candidate(
        context["successor_manifest"],
        context["successor_entries"],
        draft,
        known_pilot_clip_ids=context["pilots"],
    )
    projection = replay_successor_entries(
        context["successor_manifest"], entries, known_pilot_clip_ids=context["pilots"]
    )
    assert projection.to_dict()["event_index"][prior_id]["active"] is False

    pilot = context["pilots"][0]
    bad = _successor_draft(
        context["successor_manifest"],
        current.projection_hash,
        pilot,
        corrected,
        event_type=REVIEW_OBSERVATION_CORRECTED,
        supersedes=(prior_id,),
        target_kind=TARGET_KIND_PILOT_CLIP,
        sequence=3,
    )
    with pytest.raises(SuccessorValidationError):
        append_successor_event_candidate(
            context["successor_manifest"],
            context["successor_entries"],
            bad,
            known_pilot_clip_ids=context["pilots"],
        )


def test_b23_t09_unknown_semantics_survive_projection_and_index(tmp_path: Path):
    context = _successor_context(tmp_path, count=1, unknown=True)
    result = _build(tmp_path, context)
    rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(inventory_file_ids=(INVENTORY_IDS[0],)),
    )
    payload = json.loads(rows[0]["payload_json"])
    assert payload["rights_status"] == "UNKNOWN_NOT_RECORDED"
    assert payload["causal_family_relation"]["CF1_CONTACT_FORCE_REACTION"] == "UNKNOWN_NOT_RECORDED"
    assert payload["active_generation_input_allowed"] is False


def test_b23_t10_twelve_payloads_round_trip_losslessly(tmp_path: Path):
    context = _successor_context(tmp_path, count=12)
    mapped_payloads = {
        json.loads(row[-1])["inventory_file_id"]: json.loads(row[-1])
        for row in context["typed_rows"].observations
        if row[6] is not None
    }
    assert mapped_payloads == {INVENTORY_IDS[index - 1]: _payload(index) for index in range(1, 13)}


def test_b23_t11_old_rl_p2_mapping_is_reproducible(tmp_path: Path):
    context = _successor_context(tmp_path)
    second = map_projection(
        context["adapter"],
        context["parent_manifest"],
        context["parent_entries"],
        context["parent_projection"],
        builder_source_identity="c" * 64,
    )
    assert second.materialization_generation_id == context["parent_mapped"].materialization_generation_id
    assert second.rows == context["parent_mapped"].rows


def test_b23_t12_typed_full_rebuild_is_deterministic(tmp_path: Path):
    context = _successor_context(tmp_path)
    first = _build(tmp_path, context, "typed-a")
    second = _build(tmp_path, context, "typed-b")
    assert first.materialization_generation_id == second.materialization_generation_id
    assert first.logical_content_hash == second.logical_content_hash
    assert verify_typed_generation(first.generation_path)["valid"] is True


def test_b23_t13_inventory_exact_lookup(tmp_path: Path):
    context = _successor_context(tmp_path)
    result = _build(tmp_path, context)
    rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(inventory_file_ids=(INVENTORY_IDS[1],)),
    )
    assert [row["inventory_file_id"] for row in rows] == [INVENTORY_IDS[1]]


def test_b23_t14_role_class_and_guard_exact_facets(tmp_path: Path):
    context = _successor_context(tmp_path)
    result = _build(tmp_path, context)
    rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(
            accepted_review_roles=("HARD_NEGATIVE",),
            review_evidence_classes=("HARD_NEGATIVE",),
            exact_attributes=(("negative_guards[]", "NOT_PURSUIT"),),
        ),
    )
    assert len(rows) == 1
    assert rows[0]["anchor_code"] == "C001"


def test_b23_t15_current_and_history_retrieval(tmp_path: Path):
    context = _successor_context(tmp_path, count=1)
    prior_id = context["successor_entries"][0].event["event_id"]
    corrected = _payload(1)
    corrected["statement"] = "corrected current statement"
    draft = _successor_draft(
        context["successor_manifest"],
        context["successor_projection"].projection_hash,
        INVENTORY_IDS[0],
        corrected,
        event_type=REVIEW_OBSERVATION_CORRECTED,
        supersedes=(prior_id,),
        sequence=2,
    )
    entries = append_successor_event_candidate(
        context["successor_manifest"],
        context["successor_entries"],
        draft,
        known_pilot_clip_ids=context["pilots"],
    )
    projection = replay_successor_entries(
        context["successor_manifest"], entries, known_pilot_clip_ids=context["pilots"]
    )
    typed_rows = map_successor_observations(
        context["parent_manifest"],
        context["adapter"],
        context["parent_entries"],
        context["successor_manifest"],
        entries,
    )
    updated = dict(context)
    updated["typed_rows"] = typed_rows
    updated["successor_entries"] = entries
    result = _build(tmp_path, updated)
    current = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(
            scope="CURRENT", inventory_file_ids=(INVENTORY_IDS[0],)
        ),
    )
    history = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(
            scope="HISTORY", inventory_file_ids=(INVENTORY_IDS[0],)
        ),
    )
    assert len(current) == 1
    assert current[0]["statement"] == "corrected current statement"
    assert len(history) == 2


def test_b23_t16_direct_b21_to_rl_p2_bypass_is_rejected(tmp_path: Path):
    context = _successor_context(tmp_path)
    with pytest.raises(TypedObservationIndexError):
        build_typed_observation_generation(
            tmp_path / "typed-state",
            context["parent_mapped"],
            {"B21": "direct bypass"},
            protection_policy=_policy(tmp_path),
        )


def test_b23_t17_search_surface_does_not_create_authority(tmp_path: Path):
    context = _successor_context(tmp_path, count=1, unknown=True)
    result = _build(tmp_path, context)
    connection = sqlite3.connect(result.generation_path)
    try:
        columns = {
            row[1] for row in connection.execute("PRAGMA table_info(inventory_asset_record)")
        }
        assert "rights_provenance" not in columns
        assert "generation_input_allowed" not in columns
        assert connection.execute(
            "SELECT authority_class FROM typed_review_observation_history"
        ).fetchone()[0] == "OBSERVATION_ONLY"
    finally:
        connection.close()


def test_b23_t18_failed_build_is_atomic_and_cleans_temporary_state(tmp_path: Path):
    context = _successor_context(tmp_path)
    original = context["typed_rows"]
    malformed = object.__new__(TypedObservationRows)
    for slot in TypedObservationRows.__slots__:
        object.__setattr__(malformed, slot, getattr(original, slot))
    object.__setattr__(malformed, "_observations", (("too-short",),))
    root = tmp_path / "typed-failure"
    with pytest.raises((sqlite3.Error, TypedObservationIndexError)):
        build_typed_observation_generation(
            root,
            context["parent_mapped"],
            malformed,
            protection_policy=_policy(tmp_path),
        )
    assert not list(root.glob("*.sqlite3"))
    assert not list(root.glob("*.lock"))


def _package_registry(**overrides):
    values = {
        "package_filename": PACKAGE_FILENAME,
        "package_bytes": PACKAGE_BYTES,
        "package_sha256": PACKAGE_SHA256,
    }
    values.update(overrides)
    return build_inventory_identity_registry(
        INVENTORY_IDS,
        **values,
        source_evidence_identities=["B21-EXACT12", "G01A-INVENTORY-BOUND"],
    )


def _append_target_event(
    context: dict,
    entries: tuple,
    *,
    target_kind: str,
    target_id: str,
    payload: dict,
    sequence: int,
):
    current = replay_successor_entries(
        context["successor_manifest"],
        entries,
        known_pilot_clip_ids=context["pilots"],
    )
    draft = _successor_draft(
        context["successor_manifest"],
        current.projection_hash,
        target_id,
        payload,
        target_kind=target_kind,
        sequence=sequence,
    )
    return append_successor_event_candidate(
        context["successor_manifest"],
        entries,
        draft,
        known_pilot_clip_ids=context["pilots"],
    )


def _map_context_entries(context: dict, entries: tuple):
    return map_successor_observations(
        context["parent_manifest"],
        context["adapter"],
        context["parent_entries"],
        context["successor_manifest"],
        entries,
    )


def _pilot_payload(statement: str) -> dict:
    return {
        "observation_type": "PILOT_REVIEW_OBSERVATION_V0_2",
        "statement": statement,
        "negative_guards": [],
        "causal_family_relation": {},
        "reference_use_surface": {},
    }


def test_b25_r01_exact_canonical_package_identity_accepts():
    registry = _package_registry()
    assert registry["package_filename"] == PACKAGE_FILENAME
    assert registry["package_bytes"] == PACKAGE_BYTES
    assert registry["package_sha256"] == PACKAGE_SHA256
    assert validate_inventory_identity_registry(registry) == registry


def test_b25_r02_canonical_package_filename_mismatch_rejects():
    with pytest.raises(TypedTargetValidationError):
        _package_registry(package_filename="other.zip")


def test_b25_r03_canonical_package_bytes_mismatch_rejects():
    with pytest.raises(TypedTargetValidationError):
        _package_registry(package_bytes=PACKAGE_BYTES + 1)


def test_b25_r04_canonical_package_sha256_mismatch_rejects():
    with pytest.raises(TypedTargetValidationError):
        _package_registry(package_sha256="0" * 64)


def test_b25_r05_first_successor_event_uses_exact_parent_projection(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    empty = replay_successor_entries(
        context["successor_manifest"], (), known_pilot_clip_ids=context["pilots"]
    )
    assert empty.projection_hash == context["parent_projection"].projection_hash
    entries = _append_target_event(
        context,
        (),
        target_kind=TARGET_KIND_INVENTORY_ASSET,
        target_id=INVENTORY_IDS[0],
        payload=_payload(1),
        sequence=1,
    )
    assert len(entries) == 1


def test_b25_r06_missing_parent_projection_hash_rejects(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    parent_binding = copy.deepcopy(context["successor_manifest"]["parent_binding"])
    parent_binding.pop("parent_projection_hash")
    with pytest.raises(SuccessorValidationError):
        build_successor_manifest(
            parent_binding,
            context["successor_manifest"]["inventory_identity_registry"],
            created_by="CODEX_B26_TEST",
            created_at="2026-08-24T00:03:00Z",
        )


def test_b25_r07_wrong_parent_projection_hash_rejects_replay(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    parent_binding = copy.deepcopy(context["successor_manifest"]["parent_binding"])
    parent_binding["parent_projection_hash"] = "f" * 64
    manifest = build_successor_manifest(
        parent_binding,
        context["successor_manifest"]["inventory_identity_registry"],
        created_by="CODEX_B26_TEST",
        created_at="2026-08-24T00:03:00Z",
    )
    with pytest.raises(SuccessorValidationError):
        replay_parent_and_successor(
            context["parent_manifest"],
            context["adapter"],
            context["parent_entries"],
            manifest,
            (),
        )


def test_b25_r08_parent_tail_projection_cross_mismatch_rejects(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    parent_binding = copy.deepcopy(context["successor_manifest"]["parent_binding"])
    parent_binding["parent_tail_entry_hash"] = "e" * 64
    manifest = build_successor_manifest(
        parent_binding,
        context["successor_manifest"]["inventory_identity_registry"],
        created_by="CODEX_B26_TEST",
        created_at="2026-08-24T00:03:00Z",
    )
    with pytest.raises(SuccessorValidationError):
        replay_parent_and_successor(
            context["parent_manifest"],
            context["adapter"],
            context["parent_entries"],
            manifest,
            (),
        )


def test_b25_r09_raw_dict_cannot_be_trusted_rows(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    with pytest.raises(TypedObservationIndexError):
        build_typed_observation_generation(
            tmp_path / "dict-bypass",
            context["parent_mapped"],
            {"trusted": True},
            protection_policy=_policy(tmp_path),
        )


def test_b25_r10_raw_list_cannot_be_trusted_rows(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    with pytest.raises(TypedObservationIndexError):
        build_typed_observation_generation(
            tmp_path / "list-bypass",
            context["parent_mapped"],
            [],
            protection_policy=_policy(tmp_path),
        )


def test_b25_r11_arbitrary_preconstructed_rows_object_rejects(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    forged = object.__new__(TypedObservationRows)
    with pytest.raises(TypedObservationIndexError):
        build_typed_observation_generation(
            tmp_path / "object-bypass",
            context["parent_mapped"],
            forged,
            protection_policy=_policy(tmp_path),
        )


def test_b25_r12_verified_replay_creates_sealed_rows_and_provenance(tmp_path: Path):
    context = _successor_context(tmp_path, count=1)
    rows = context["typed_rows"]
    assert type(rows) is TypedObservationRows
    assert rows.provenance["parent_projection_hash"] == context[
        "parent_projection"
    ].projection_hash
    assert rows.provenance["inventory_registry_hash"] == context[
        "successor_manifest"
    ]["inventory_identity_registry"]["canonical_registry_hash"]
    result = _build(tmp_path, context)
    assert verify_typed_generation(result.generation_path)[
        "verified_provenance_sha256"
    ] == rows.provenance_sha256
    parent = context["parent_mapped"]
    mismatched_tables = dict(parent.rows)
    mismatched_meta = list(mismatched_tables["read_model_meta"][0])
    mismatched_meta[18] = "f" * 64
    mismatched_tables["read_model_meta"] = (tuple(mismatched_meta),)
    mismatched_parent = type(parent)(
        mismatched_tables, parent.materialization_generation_id
    )
    with pytest.raises(TypedObservationIndexError):
        build_typed_observation_generation(
            tmp_path / "mismatched-parent",
            mismatched_parent,
            rows,
            protection_policy=_policy(tmp_path),
            parent_manifest=context["parent_manifest"],
            adapter=context["adapter"],
            parent_entries=context["parent_entries"],
            successor_manifest=context["successor_manifest"],
            successor_entries=context["successor_entries"],
        )


def test_b27_r01_fully_populated_recomputed_seal_forgery_rejects(tmp_path: Path):
    context = _successor_context(tmp_path, count=1)
    original = context["typed_rows"]
    forged = object.__new__(TypedObservationRows)
    for slot in TypedObservationRows.__slots__:
        object.__setattr__(forged, slot, getattr(original, slot))

    forged_provenance = dict(original.provenance)
    forged_provenance["successor_manifest_sha256"] = "d" * 64
    forged_provenance["successor_projection_hash"] = "e" * 64
    object.__setattr__(forged, "_successor_projection_hash", "e" * 64)
    object.__setattr__(forged, "_provenance", forged_provenance)
    object.__setattr__(
        forged,
        "_seal",
        hashlib.sha256(_canonical(_row_seal_body(forged)).encode("utf-8")).hexdigest(),
    )

    with pytest.raises(TypedObservationIndexError):
        build_typed_observation_generation(
            tmp_path / "fully-populated-forged-seal",
            context["parent_mapped"],
            forged,
            protection_policy=_policy(tmp_path),
            parent_manifest=context["parent_manifest"],
            adapter=context["adapter"],
            parent_entries=context["parent_entries"],
            successor_manifest=context["successor_manifest"],
            successor_entries=context["successor_entries"],
        )


def test_b25_r13_successor_pilot_observation_projects(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    pilot = context["pilots"][0]
    entries = _append_target_event(
        context,
        (),
        target_kind=TARGET_KIND_PILOT_CLIP,
        target_id=pilot,
        payload=_pilot_payload("successor pilot observation"),
        sequence=1,
    )
    updated = dict(
        context,
        successor_entries=entries,
        typed_rows=_map_context_entries(context, entries),
    )
    result = _build(tmp_path, updated)
    rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(target_kinds=(TARGET_KIND_PILOT_CLIP,)),
    )
    assert "successor pilot observation" in {row["statement"] for row in rows}
    assert all(row["inventory_file_id"] is None for row in rows)


def test_b25_r14_successor_inventory_observation_projects(tmp_path: Path):
    context = _successor_context(tmp_path, count=1)
    result = _build(tmp_path, context)
    rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(target_kinds=(TARGET_KIND_INVENTORY_ASSET,)),
    )
    assert [row["inventory_file_id"] for row in rows] == [INVENTORY_IDS[0]]
    assert rows[0]["pilot_clip_id"] is None


def test_b25_r15_mixed_pilot_and_inventory_successor_replay(tmp_path: Path):
    context = _successor_context(tmp_path, count=0)
    entries = _append_target_event(
        context,
        (),
        target_kind=TARGET_KIND_PILOT_CLIP,
        target_id=context["pilots"][0],
        payload=_pilot_payload("mixed pilot observation"),
        sequence=1,
    )
    entries = _append_target_event(
        context,
        entries,
        target_kind=TARGET_KIND_INVENTORY_ASSET,
        target_id=INVENTORY_IDS[0],
        payload=_payload(1),
        sequence=2,
    )
    updated = dict(
        context,
        successor_entries=entries,
        typed_rows=_map_context_entries(context, entries),
    )
    result = _build(tmp_path, updated)
    rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(
            target_kinds=(TARGET_KIND_PILOT_CLIP, TARGET_KIND_INVENTORY_ASSET)
        ),
    )
    assert {row["target_kind"] for row in rows} == {
        TARGET_KIND_PILOT_CLIP,
        TARGET_KIND_INVENTORY_ASSET,
    }


def test_b25_r16_target_kind_filter_and_conditional_nullable_semantics(tmp_path: Path):
    context = _successor_context(tmp_path, count=1)
    result = _build(tmp_path, context)
    pilot_rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(target_kinds=(TARGET_KIND_PILOT_CLIP,)),
    )
    inventory_rows = query_typed_observations(
        result.generation_path,
        TypedObservationQuery(target_kinds=(TARGET_KIND_INVENTORY_ASSET,)),
    )
    assert pilot_rows and inventory_rows
    assert all(
        row["pilot_clip_id"] is not None and row["inventory_file_id"] is None
        for row in pilot_rows
    )
    assert all(
        row["pilot_clip_id"] is None and row["inventory_file_id"] is not None
        for row in inventory_rows
    )
