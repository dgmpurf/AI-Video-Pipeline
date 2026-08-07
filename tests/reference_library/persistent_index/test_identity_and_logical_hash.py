from __future__ import annotations

import shutil
import sqlite3
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index.enums import (
    LOGICAL_HASH_REGISTRY_VERSION,
    GenerationState,
)
from app.ai_video_pipeline.reference_library.persistent_index.identity import (
    LOGICAL_REGISTRY,
    canonical_json_bytes,
    canonicalize_bounded_json,
    logical_content_hash,
    logical_export,
    parse_generation_filename,
)
from app.ai_video_pipeline.reference_library.persistent_index.schema import (
    create_schema,
    insert_rows,
    populate_fts,
)
from app.ai_video_pipeline.reference_library.persistent_index.verify import (
    verify_generation,
)


def _logical_database(path: Path, rows, *, reverse: bool, page_size: int) -> str:
    connection = sqlite3.connect(path)
    try:
        connection.execute(f"PRAGMA page_size={page_size}")
        create_schema(connection)
        values = {
            name: tuple(reversed(table_rows)) if reverse else table_rows
            for name, table_rows in rows.items()
        }
        insert_rows(connection, values)
        populate_fts(connection)
        connection.commit()
        return logical_content_hash(connection)
    finally:
        connection.close()


def test_closed_registry_has_exact_23_tables():
    assert len(LOGICAL_REGISTRY) == 23
    assert len({entry.table for entry in LOGICAL_REGISTRY}) == 23
    assert LOGICAL_HASH_REGISTRY_VERSION == "RL_P2_LOGICAL_HASH_REGISTRY_V0_1R1"


def test_canonical_json_is_stable_and_rejects_negative_zero():
    assert canonical_json_bytes({"z": 1, "a": ["原神", None, False]}) == (
        b'{"a":["\xe5\x8e\x9f\xe7\xa5\x9e",null,false],"z":1}'
    )
    with pytest.raises(Exception, match="non-canonical number"):
        canonical_json_bytes({"value": -0.0})
    assert canonicalize_bounded_json('{"z":1,"a":2}') == '{"a":2,"z":1}'
    with pytest.raises(Exception, match="bounded JSON text is invalid"):
        canonicalize_bounded_json('{"a":1,"a":2}')


def test_logical_hash_ignores_insertion_order_and_physical_layout(
    tmp_path: Path, mapped_empty
):
    first = _logical_database(tmp_path / "a.sqlite3", mapped_empty.rows, reverse=False, page_size=4096)
    second = _logical_database(tmp_path / "b.sqlite3", mapped_empty.rows, reverse=True, page_size=8192)
    assert first == second
    with sqlite3.connect(tmp_path / "a.sqlite3") as connection:
        exported = logical_export(connection)
    assert exported[0] == LOGICAL_HASH_REGISTRY_VERSION
    assert len(exported[2]) == 23


def test_stored_hash_is_excluded_from_preimage_but_mismatch_fails(built_generation):
    expected = built_generation.logical_content_hash
    with sqlite3.connect(built_generation.generation_path) as connection:
        connection.execute(
            "UPDATE read_model_meta SET logical_content_hash=? WHERE meta_id=1",
            ("0" * 64,),
        )
        connection.commit()
    result = verify_generation(built_generation.generation_path)
    assert result.state == GenerationState.CORRUPT_OR_TAMPERED_GENERATION
    assert result.logical_content_hash == expected
    assert result.stored_logical_content_hash == "0" * 64


def test_included_logical_mutation_fails_verification(built_generation):
    with sqlite3.connect(built_generation.generation_path) as connection:
        connection.execute(
            "UPDATE reference_record SET description=description || ' changed' "
            "WHERE pilot_clip_id='G01D-CLIP-001'"
        )
        connection.commit()
    result = verify_generation(built_generation.generation_path)
    assert result.state == GenerationState.CORRUPT_OR_TAMPERED_GENERATION
    assert "stored and recomputed" in " ".join(result.diagnostics)


def test_schema_drift_fails_closed(built_generation):
    with sqlite3.connect(built_generation.generation_path) as connection:
        connection.execute("ALTER TABLE reference_record ADD COLUMN unregistered TEXT")
        connection.commit()
    result = verify_generation(built_generation.generation_path)
    assert result.state == GenerationState.INCOMPATIBLE_GENERATION
    assert "column registry differs" in " ".join(result.diagnostics)


def test_full_filename_hash_and_generation_identity_are_enforced(
    tmp_path: Path, built_generation
):
    parsed = parse_generation_filename(built_generation.generation_path)
    assert parsed["generation"] == built_generation.materialization_generation_id
    wrong = tmp_path / (
        "rl_p2--RL_P2_READ_MODEL_V0_1R1--"
        + built_generation.materialization_generation_id
        + "--sha256-"
        + "f" * 64
        + ".sqlite3"
    )
    shutil.copy2(built_generation.generation_path, wrong)
    result = verify_generation(wrong)
    assert result.state == GenerationState.CORRUPT_OR_TAMPERED_GENERATION
    assert "filename hash differs" in " ".join(result.diagnostics)
