from __future__ import annotations

from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index.builder import build_generation
from app.ai_video_pipeline.reference_library.persistent_index.enums import GenerationState
from app.ai_video_pipeline.reference_library.persistent_index.errors import PromotionError
from app.ai_video_pipeline.reference_library.persistent_index.promotion import (
    POINTER_FILENAME,
    POINTER_TEMP_FILENAME,
    promote_generation,
    read_pointer,
    resolve_current,
)
from app.ai_video_pipeline.reference_library.persistent_index.verify import (
    open_read_only,
    verify_generation,
)


def _two_generations(tmp_path: Path, ledger_harness, runtime_state_policy):
    state = tmp_path / "state"
    first = build_generation(
        state, ledger_harness.mapped(), protection_policy=runtime_state_policy
    )
    ledger_harness.append("REVIEW_OBSERVATION_ADDED")
    second = build_generation(
        state, ledger_harness.mapped(), protection_policy=runtime_state_policy
    )
    return state, first, second


def test_initial_pointer_creation_and_immediate_reopen(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    state = tmp_path / "state"
    generation = build_generation(
        state, ledger_harness.mapped(), protection_policy=runtime_state_policy
    )
    pointer = promote_generation(
        generation.generation_path, protection_policy=runtime_state_policy
    )
    observed = read_pointer(state / POINTER_FILENAME)
    resolved, resolved_pointer = resolve_current(state)
    assert observed == pointer == resolved_pointer
    assert resolved == generation.generation_path
    assert pointer["logical_content_hash"] == generation.logical_content_hash
    assert pointer["generation_filename"] == generation.generation_path.name


def test_reader_holding_old_generation_survives_pointer_replacement(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    state, first, second = _two_generations(
        tmp_path, ledger_harness, runtime_state_policy
    )
    promote_generation(first.generation_path, protection_policy=runtime_state_policy)
    old_reader = open_read_only(first.generation_path)
    try:
        promote_generation(
            second.generation_path, protection_policy=runtime_state_policy
        )
        assert old_reader.execute("SELECT count(*) FROM reference_record").fetchone()[0] == 30
    finally:
        old_reader.close()
    current, _ = resolve_current(state)
    assert current == second.generation_path
    assert first.generation_path.exists()


def test_failed_pointer_replace_preserves_prior_pointer(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    state, first, second = _two_generations(
        tmp_path, ledger_harness, runtime_state_policy
    )
    promote_generation(first.generation_path, protection_policy=runtime_state_policy)
    before = (state / POINTER_FILENAME).read_bytes()

    def fail_replace(*_):
        raise OSError("synthetic replace failure")

    with pytest.raises(PromotionError, match="atomic pointer promotion failed"):
        promote_generation(
            second.generation_path,
            protection_policy=runtime_state_policy,
            replace_operation=fail_replace,
        )
    assert (state / POINTER_FILENAME).read_bytes() == before
    assert (state / POINTER_TEMP_FILENAME).exists()
    current, _ = resolve_current(state)
    assert current == first.generation_path


def test_pointer_hash_mismatch_fails_closed(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    state = tmp_path / "state"
    generation = build_generation(
        state, ledger_harness.mapped(), protection_policy=runtime_state_policy
    )
    pointer = dict(
        promote_generation(
            generation.generation_path, protection_policy=runtime_state_policy
        )
    )
    pointer["logical_content_hash"] = "0" * 64
    result = verify_generation(generation.generation_path, pointer=pointer)
    assert result.state == GenerationState.CORRUPT_OR_TAMPERED_GENERATION


def test_full_pointer_filename_stored_and_recomputed_hashes_agree(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    state = tmp_path / "state"
    generation = build_generation(
        state, ledger_harness.mapped(), protection_policy=runtime_state_policy
    )
    pointer = promote_generation(
        generation.generation_path, protection_policy=runtime_state_policy
    )
    verified = verify_generation(generation.generation_path, pointer=pointer)
    assert verified.valid
    assert {
        pointer["logical_content_hash"],
        verified.stored_logical_content_hash,
        verified.logical_content_hash,
        generation.logical_content_hash,
    } == {generation.logical_content_hash}
