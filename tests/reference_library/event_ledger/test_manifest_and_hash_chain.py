from __future__ import annotations

import copy
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import (
    append_event,
    initialize_manifest,
    read_manifest,
)
from app.ai_video_pipeline.reference_library.event_ledger.canonical import (
    canonical_json_bytes,
    canonical_sha256,
    strict_json_loads,
)
from app.ai_video_pipeline.reference_library.event_ledger.errors import (
    DuplicateEventError,
    EventCollisionError,
    LedgerValidationError,
    ManifestValidationError,
)
from app.ai_video_pipeline.reference_library.event_ledger.ledger import (
    read_ledger_entries,
)
from app.ai_video_pipeline.reference_library.event_ledger.manifest import (
    EVENTS_FILENAME,
    MANIFEST_FILENAME,
    build_manifest,
    derive_ledger_id,
    validate_manifest,
)
from app.ai_video_pipeline.reference_library.event_ledger.models import RL_P0_COMMIT


def test_manifest_and_ledger_ids_are_deterministic(tmp_path: Path, base_adapter) -> None:
    first = initialize_manifest(
        tmp_path / "first",
        base_adapter,
        created_by="CODEX_SYNTHETIC_TEST",
        created_at="2026-08-07T00:00:00Z",
    )
    second = initialize_manifest(
        tmp_path / "second",
        base_adapter,
        created_by="CODEX_SYNTHETIC_TEST",
        created_at="2026-08-07T00:00:00Z",
    )
    assert first == second
    assert first["ledger_id"].startswith("RL-LEDGER-")
    assert first["base_catalog"] == base_adapter.binding.to_dict()
    assert first["base_catalog"]["rl_p0_commit"] == RL_P0_COMMIT


def test_base_catalog_hash_explicitly_binds_rl_p0_commit(base_adapter) -> None:
    binding = base_adapter.binding
    expected_input = {
        "package_filename": binding.package_filename,
        "package_bytes": binding.package_bytes,
        "package_sha256": binding.package_sha256,
        "record_count": binding.record_count,
        "record_schema_version": binding.record_schema_version,
        "rl_p0_commit": RL_P0_COMMIT,
        "records": list(base_adapter.records),
    }
    assert binding.rl_p0_commit == RL_P0_COMMIT
    assert binding.base_catalog_hash == canonical_sha256(expected_input)
    expected_input.pop("rl_p0_commit")
    assert binding.base_catalog_hash != canonical_sha256(expected_input)


def _refresh_ledger_id(manifest: dict) -> None:
    body = {key: value for key, value in manifest.items() if key != "ledger_id"}
    manifest["ledger_id"] = derive_ledger_id(body)


def test_manifest_rejects_missing_rl_p0_commit(base_adapter) -> None:
    manifest = build_manifest(
        base_adapter,
        created_by="CODEX_SYNTHETIC_TEST",
        created_at="2026-08-07T00:00:00Z",
    )
    del manifest["base_catalog"]["rl_p0_commit"]
    _refresh_ledger_id(manifest)
    with pytest.raises(ManifestValidationError):
        validate_manifest(manifest, adapter=base_adapter)


@pytest.mark.parametrize("commit", ["not-a-commit", "0" * 40])
def test_manifest_rejects_malformed_or_different_rl_p0_commit(
    base_adapter, commit
) -> None:
    manifest = build_manifest(
        base_adapter,
        created_by="CODEX_SYNTHETIC_TEST",
        created_at="2026-08-07T00:00:00Z",
    )
    manifest["base_catalog"]["rl_p0_commit"] = commit
    _refresh_ledger_id(manifest)
    with pytest.raises(ManifestValidationError, match="RL-P0 commit"):
        validate_manifest(manifest, adapter=base_adapter)


def test_manifest_is_canonical_and_immutable(initialized_ledger, base_adapter) -> None:
    path = initialized_ledger / MANIFEST_FILENAME
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    assert path.read_bytes() == canonical_json_bytes(manifest) + b"\n"
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        initialize_manifest(
            initialized_ledger,
            base_adapter,
            created_by="ANOTHER_ACTOR",
            created_at="2026-08-07T00:00:02Z",
        )
    assert path.read_bytes() == before


def test_manifest_tamper_is_rejected(initialized_ledger, base_adapter) -> None:
    path = initialized_ledger / MANIFEST_FILENAME
    manifest = strict_json_loads(path.read_bytes())
    manifest["base_catalog"]["record_count"] = 29
    path.write_bytes(canonical_json_bytes(manifest) + b"\n")
    with pytest.raises(ManifestValidationError):
        read_manifest(initialized_ledger, adapter=base_adapter)


def test_genesis_and_multi_entry_hash_chain(initialized_ledger, base_adapter, make_event) -> None:
    first = append_event(initialized_ledger, base_adapter, make_event())
    second = append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            pilot_clip_id="G01D-CLIP-002",
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    entries = read_ledger_entries(initialized_ledger, manifest=manifest)
    assert [entry.position for entry in entries] == [1, 2]
    assert first.to_dict()["previous_entry_hash"] == "0" * 64
    assert second.to_dict()["previous_entry_hash"] == first.entry_hash
    assert entries == (first, second)


def test_duplicate_event_is_no_write(initialized_ledger, base_adapter, make_event) -> None:
    draft = make_event()
    append_event(initialized_ledger, base_adapter, draft)
    path = initialized_ledger / EVENTS_FILENAME
    before = path.read_bytes()
    with pytest.raises(DuplicateEventError):
        append_event(initialized_ledger, base_adapter, copy.deepcopy(draft))
    assert path.read_bytes() == before


def test_event_prefix_collision_is_no_write(
    initialized_ledger, base_adapter, make_event, monkeypatch
) -> None:
    first = append_event(initialized_ledger, base_adapter, make_event())
    path = initialized_ledger / EVENTS_FILENAME
    before = path.read_bytes()
    collision = first.event.to_dict()
    collision["event_body_hash"] = "f" * 64
    collision["payload"] = {"statement": "different body"}
    monkeypatch.setattr(
        "app.ai_video_pipeline.reference_library.event_ledger.ledger.finalize_event",
        lambda _: collision,
    )
    with pytest.raises(EventCollisionError):
        append_event(initialized_ledger, base_adapter, make_event())
    assert path.read_bytes() == before


def _rewrite_entries(path: Path, mutator) -> None:
    values = [strict_json_loads(line) for line in path.read_bytes().splitlines()]
    mutator(values)
    path.write_bytes(b"\n".join(canonical_json_bytes(value) for value in values) + b"\n")


@pytest.mark.parametrize("field", ["previous_entry_hash", "entry_hash"])
def test_broken_hash_chain_is_rejected(
    initialized_ledger, base_adapter, make_event, field
) -> None:
    append_event(initialized_ledger, base_adapter, make_event())
    append_event(
        initialized_ledger,
        base_adapter,
        make_event(
            pilot_clip_id="G01D-CLIP-002",
            occurred_at="2026-08-07T00:00:02Z",
            recorded_at="2026-08-07T00:00:03Z",
        ),
    )
    path = initialized_ledger / EVENTS_FILENAME

    def mutate(values):
        values[-1][field] = "f" * 64

    _rewrite_entries(path, mutate)
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    with pytest.raises(LedgerValidationError):
        read_ledger_entries(initialized_ledger, manifest=manifest)


def test_duplicate_or_skipped_position_is_rejected(
    initialized_ledger, base_adapter, make_event
) -> None:
    append_event(initialized_ledger, base_adapter, make_event())
    path = initialized_ledger / EVENTS_FILENAME

    def mutate(values):
        values[0]["ledger_position"] = 2

    _rewrite_entries(path, mutate)
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    with pytest.raises(LedgerValidationError, match="position"):
        read_ledger_entries(initialized_ledger, manifest=manifest)


@pytest.mark.parametrize(
    "replacement",
    [
        b'{"broken":\n',
        b"\xff\n",
        b'{"partial":"\xe4\xb8"}\n',
        b'{"not":"canonical", "spacing":true}\n',
    ],
)
def test_malformed_json_utf8_and_noncanonical_lines_are_rejected(
    initialized_ledger, base_adapter, replacement
) -> None:
    (initialized_ledger / EVENTS_FILENAME).write_bytes(replacement)
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    with pytest.raises(LedgerValidationError):
        read_ledger_entries(initialized_ledger, manifest=manifest)


def test_missing_final_lf_is_rejected(initialized_ledger, base_adapter, make_event) -> None:
    append_event(initialized_ledger, base_adapter, make_event())
    path = initialized_ledger / EVENTS_FILENAME
    path.write_bytes(path.read_bytes().removesuffix(b"\n"))
    manifest = read_manifest(initialized_ledger, adapter=base_adapter)
    with pytest.raises(LedgerValidationError, match="final LF"):
        read_ledger_entries(initialized_ledger, manifest=manifest)
