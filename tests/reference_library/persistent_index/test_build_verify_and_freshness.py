from __future__ import annotations

import os
import shutil
import sqlite3
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index.builder import (
    LOCK_FILENAME,
    build_generation,
)
from app.ai_video_pipeline.reference_library.persistent_index.enums import GenerationState
from app.ai_video_pipeline.reference_library.persistent_index.errors import BuildError
from app.ai_video_pipeline.reference_library.persistent_index.promotion import POINTER_FILENAME
from app.ai_video_pipeline.reference_library.persistent_index.verify import verify_generation


def test_repeated_full_rebuilds_have_same_logical_identity(tmp_path: Path, mapped_empty):
    first = build_generation(tmp_path / "first", mapped_empty)
    second = build_generation(tmp_path / "second", mapped_empty)
    assert first.logical_content_hash == second.logical_content_hash
    assert first.materialization_generation_id == second.materialization_generation_id
    assert first.generation_path.name == second.generation_path.name
    assert first.verification.valid and second.verification.valid


def test_valid_older_prefix_is_stale_not_corrupt(built_generation):
    current_position = int(built_generation.verification.metadata["through_position"])
    result = verify_generation(
        built_generation.generation_path,
        expected_upstream={"through_position": current_position + 1},
    )
    assert result.state == GenerationState.STALE_GENERATION
    assert result.logical_content_hash == built_generation.logical_content_hash


def test_divergent_or_incomplete_upstream_identity_is_incompatible(built_generation):
    divergent = verify_generation(
        built_generation.generation_path,
        expected_upstream={"base_catalog_hash": "0" * 64},
    )
    missing = verify_generation(
        built_generation.generation_path,
        expected_upstream={"unregistered_identity_field": "value"},
    )
    assert divergent.state == GenerationState.INCOMPATIBLE_GENERATION
    assert missing.state == GenerationState.INCOMPATIBLE_GENERATION


def test_generation_collision_never_creates_or_changes_pointer(tmp_path: Path, mapped_empty):
    state = tmp_path / "state"
    first = build_generation(state, mapped_empty)
    with pytest.raises(BuildError, match="immutable generation filename collision"):
        build_generation(state, mapped_empty)
    assert first.generation_path.exists()
    assert not (state / POINTER_FILENAME).exists()
    assert (state / LOCK_FILENAME).exists()


def test_truncated_database_is_corrupt(tmp_path: Path, built_generation):
    truncated = tmp_path / built_generation.generation_path.name
    raw = built_generation.generation_path.read_bytes()
    truncated.write_bytes(raw[: max(1, len(raw) // 3)])
    result = verify_generation(truncated)
    assert result.state == GenerationState.CORRUPT_OR_TAMPERED_GENERATION


@pytest.mark.parametrize(
    "field,value,diagnostic",
    (
        ("read_model_schema_version", "UNSUPPORTED", "read-model schema"),
        ("logical_hash_registry_version", "UNSUPPORTED", "logical-hash registry"),
        ("builder_contract_version", "UNSUPPORTED", "builder contract"),
        ("tokenizer_contract_version", "UNSUPPORTED", "tokenizer contract"),
    ),
)
def test_unsupported_contract_identity_is_incompatible(
    built_generation, field, value, diagnostic
):
    with sqlite3.connect(built_generation.generation_path) as connection:
        connection.execute("PRAGMA ignore_check_constraints=ON")
        connection.execute(f"UPDATE read_model_meta SET {field}=? WHERE meta_id=1", (value,))
        connection.commit()
    result = verify_generation(built_generation.generation_path)
    assert result.state == GenerationState.INCOMPATIBLE_GENERATION
    assert diagnostic in " ".join(result.diagnostics)


def test_fts_physical_index_tamper_is_detected(built_generation):
    with sqlite3.connect(built_generation.generation_path) as connection:
        connection.execute(
            "DELETE FROM search_current_fts WHERE document_id='record:G01D-CLIP-001:description'"
        )
        connection.commit()
    result = verify_generation(built_generation.generation_path)
    assert result.state == GenerationState.CORRUPT_OR_TAMPERED_GENERATION
    assert "FTS current/history" in " ".join(result.diagnostics) or "row content" in " ".join(result.diagnostics)
