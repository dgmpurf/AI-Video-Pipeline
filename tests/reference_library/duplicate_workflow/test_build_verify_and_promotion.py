from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.duplicate_workflow.builder import build_generation
from app.ai_video_pipeline.reference_library.duplicate_workflow.errors import PromotionError
from app.ai_video_pipeline.reference_library.duplicate_workflow.models import RuntimeStateProtectionPolicy
from app.ai_video_pipeline.reference_library.duplicate_workflow.promotion import (
    POINTER_FILENAME,
    promote_generation,
    resolve_current,
)
from app.ai_video_pipeline.reference_library.duplicate_workflow.verify import verify_generation


def _policy(tmp_path):
    return RuntimeStateProtectionPolicy(
        tmp_path / "repository",
        tmp_path / "source",
        (tmp_path / "media",),
    )


def test_build_verify_rebuild_and_atomic_promotion(tmp_path, mapped_model):
    policy = _policy(tmp_path)
    first = build_generation(tmp_path / "state-a", mapped_model, protection_policy=policy)
    second = build_generation(tmp_path / "state-b", mapped_model, protection_policy=policy)
    assert first.logical_content_hash == second.logical_content_hash
    assert first.generation_path.name == second.generation_path.name
    pointer = promote_generation(first.generation_path, protection_policy=policy)
    assert pointer["generation_filename"] == first.generation_path.name
    assert (tmp_path / "state-a" / POINTER_FILENAME).read_bytes().endswith(b"\n")
    resolved, observed = resolve_current(tmp_path / "state-a")
    assert resolved == first.generation_path
    assert observed == pointer
    assert verify_generation(resolved, pointer=observed).valid


def test_no_latest_by_time_fallback(tmp_path):
    root = tmp_path / "state"
    root.mkdir()
    (root / "unbound.sqlite3").write_bytes(b"not-a-store")
    with pytest.raises(PromotionError):
        resolve_current(root)
