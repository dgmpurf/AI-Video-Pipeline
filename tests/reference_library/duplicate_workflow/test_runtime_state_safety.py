import pytest

from app.ai_video_pipeline.reference_library.duplicate_workflow.builder import (
    build_generation,
    validate_state_root,
)
from app.ai_video_pipeline.reference_library.duplicate_workflow.errors import UnsafePathError
from app.ai_video_pipeline.reference_library.duplicate_workflow.models import RuntimeStateProtectionPolicy


def test_missing_policy_rejects_before_root_creation(tmp_path, mapped_model):
    target = tmp_path / "must-not-exist"
    with pytest.raises(UnsafePathError):
        build_generation(target, mapped_model)
    assert not target.exists()


def test_relative_or_protected_state_root_is_rejected(tmp_path):
    policy = RuntimeStateProtectionPolicy(
        tmp_path / "repo", tmp_path / "source", (tmp_path / "media",)
    )
    with pytest.raises(UnsafePathError):
        validate_state_root("relative-state", protection_policy=policy)
    protected_target = tmp_path / "repo" / "runtime"
    with pytest.raises(UnsafePathError):
        validate_state_root(protected_target, protection_policy=policy)
    assert not protected_target.exists()
