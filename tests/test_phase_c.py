from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import pytest

from app.ai_video_pipeline.assets.registry import AssetRegistry
from app.ai_video_pipeline.core.models import (
    AssetRecord,
    AssetRelationshipType,
    AssetRole,
    AssetStatus,
    AssetType,
    ReviewStatus,
    RunMode,
)
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy
from app.ai_video_pipeline.review import ReviewDecision, ReviewLocker

ROOT = Path(__file__).resolve().parents[1]
TEST_PRODUCTION_ID = "test_production"


def _init_workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    (workspace / "mock_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "live_outputs").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    (workspace / "productions" / TEST_PRODUCTION_ID / "assets").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / TEST_PRODUCTION_ID / "reviews").mkdir(parents=True, exist_ok=True)
    return workspace


def _registry_path(workspace: Path) -> Path:
    return workspace / "productions" / TEST_PRODUCTION_ID / "assets" / "asset_registry.json"


def _new_asset(logical_id: str, candidate_id: str, status: AssetStatus | None = None) -> AssetRecord:
    return AssetRecord(
        logical_id=logical_id,
        candidate_id=candidate_id,
        asset_type=AssetType.image,
        role=AssetRole.source,
        relative_path=Path(f"assets/{logical_id}_{candidate_id}.png"),
        source_path=Path(f"tests/fixtures/media/{logical_id}_{candidate_id}.png"),
        status=status or AssetStatus.candidate,
        review_status=ReviewStatus.pending_review,
    )


def _new_tester(tmp_path: Path) -> tuple[Path, PathPolicy, AssetRegistry, ReviewLocker]:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    registry = AssetRegistry(_registry_path(workspace), policy)
    review = ReviewLocker(registry, workspace / "productions" / TEST_PRODUCTION_ID, policy)
    return workspace, policy, registry, review


def test_01_asset_registry_add_and_get(tmp_path: Path) -> None:
    workspace, _, registry, _ = _new_tester(tmp_path)
    registry.add_asset(_new_asset("shot-001", "cand-001"))
    results = registry.get_by_logical_id("shot-001", "cand-001")
    assert len(results) == 1
    assert results[0].logical_id == "shot-001"
    assert results[0].candidate_id == "cand-001"
    assert registry.load()
    assert (workspace / "productions" / TEST_PRODUCTION_ID / "assets" / "asset_registry.json").exists()


def test_02_asset_registry_list_by_status(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    registry.add_asset(_new_asset("s1", "c1", status=AssetStatus.candidate))
    registry.add_asset(_new_asset("s2", "c2", status=AssetStatus.rejected))
    registry.add_asset(_new_asset("s3", "c3", status=AssetStatus.archived))
    assert len(registry.list_by_status(AssetStatus.candidate)) == 1
    assert len(registry.list_by_status("rejected")) == 1
    assert len(registry.list_by_status("archived")) == 1


def test_03_candidate_id_is_required(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    with pytest.raises(ValueError, match="candidate_id is required"):
        registry.add_asset(_new_asset("s4", ""))


def test_04_logical_id_duplicate_with_different_candidate_id_is_allowed(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    registry.add_asset(_new_asset("dup-001", "cA"))
    registry.add_asset(_new_asset("dup-001", "cB"))
    entries = registry.get_by_logical_id("dup-001")
    assert len(entries) == 2
    assert sorted(item.candidate_id for item in entries) == ["cA", "cB"]


def test_05_exact_duplicate_relationship_marks_canonical(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    first = _new_asset("dup-img", "cA")
    second = _new_asset("dup-img", "cB")
    first.sha256 = "same-hash"
    second.sha256 = "same-hash"
    registry.add_asset(first)
    registry.add_asset(second)
    relation = registry.add_exact_duplicate(("dup-img", "cA"), ("dup-img", "cB"))
    assert relation.relationship_type == AssetRelationshipType.exact_duplicate
    assert relation.is_canonical is True
    assert relation.logical_id == "dup-img"
    assert relation.candidate_id == "cA"
    assert registry.get_canonical_for_exact_duplicate("dup-img", "cB") == ("dup-img", "cA")


def test_06_near_duplicate_variant_is_not_rejected(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    registry.add_asset(_new_asset("v1", "c1"))
    registry.add_asset(_new_asset("v1", "c2"))
    relation = registry.mark_near_duplicate_variant(("v1", "c1"), ("v1", "c2"))
    assert relation.relationship_type == AssetRelationshipType.near_duplicate_variant
    entries = registry.get_by_logical_id("v1")
    assert all(item.status == AssetStatus.candidate for item in entries)


def test_07_continuity_pair_is_not_deduplicated(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    registry.add_asset(_new_asset("cont-1", "c1"))
    registry.add_asset(_new_asset("cont-1", "c2"))
    relation = registry.mark_continuity_pair(("cont-1", "c1"), ("cont-1", "c2"))
    assert relation.relationship_type == AssetRelationshipType.continuity_pair
    assert registry.get_canonical_for_exact_duplicate("cont-1", "c2") is None


def test_08_lock_asset_requires_user_decision(tmp_path: Path) -> None:
    _, policy, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("shot-lock", "c1"))
    with pytest.raises(ValueError, match="cannot auto-lock"):
        review.lock_asset("shot-lock", "c1", reviewer="system", source_path="real_source.png")
    review.lock_asset("shot-lock", "c1", reviewer="user", source_path="real_source.png")
    found = registry.get_by_logical_id("shot-lock", "c1")[0]
    assert found.status == AssetStatus.locked_after_human_review


def test_09_system_reviewer_cannot_final_lock_production_asset(tmp_path: Path) -> None:
    _, _, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("shot-system", "c1"))
    with pytest.raises(ValueError, match="cannot auto-lock"):
        review.approve_candidate("shot-system", "c1", reviewer="system", source_path="real_source.png")


def test_10_reject_asset_requires_reason(tmp_path: Path) -> None:
    _, _, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("reject-001", "c1"))
    with pytest.raises(ValueError, match="reject must include reason"):
        review.reject_asset("reject-001", "c1", reason="")
    decision = review.reject_asset("reject-001", "c1", reason="too noisy")
    assert decision.decision == ReviewDecision.reject
    assert registry.get_by_logical_id("reject-001", "c1")[0].status == AssetStatus.rejected


def test_11_request_rerun_requires_reason(tmp_path: Path) -> None:
    _, _, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("rerun-001", "c1"))
    with pytest.raises(ValueError, match="needs_rerun must include rerun_reason"):
        review.request_rerun("rerun-001", "c1", rerun_reason="")
    decision = review.request_rerun("rerun-001", "c1", rerun_reason="motion blur")
    assert decision.decision == ReviewDecision.needs_rerun


def test_12_review_record_written_on_state_changes(tmp_path: Path) -> None:
    _, _, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("record-approve", "c1"))
    registry.add_asset(_new_asset("record-reject", "c1"))
    review.approve_candidate("record-approve", "c1", reviewer="user", source_path="asset.png")
    review.reject_asset("record-reject", "c1", reason="bad")
    lines = review.record_path.read_text(encoding="utf-8").splitlines()
    parsed = [json.loads(line) for line in lines]
    decisions = {item["decision"] for item in parsed}
    assert "approve" in decisions
    assert "reject" in decisions
    assert len(parsed) == 2

def test_13_mock_output_cannot_be_locked(tmp_path: Path) -> None:
    _, _, registry, review = _new_tester(tmp_path)
    mock_asset = _new_asset("mock-001", "c1")
    mock_asset.source_path = Path("workspace/mock_outputs/sample.png")
    registry.add_asset(mock_asset)
    with pytest.raises(ValueError, match="mock output cannot be locked"):
        review.approve_candidate("mock-001", "c1", reviewer="user", source_path="mock_outputs/sample.png")


def test_14_rejected_asset_cannot_be_used_as_reference(tmp_path: Path) -> None:
    _, _, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("ref-001", "c1"))
    review.reject_asset("ref-001", "c1", reason="invalid framing")
    assert registry.can_be_reference("ref-001", "c1") is False


def test_15_archived_asset_cannot_be_used_by_default(tmp_path: Path) -> None:
    _, _, registry, _ = _new_tester(tmp_path)
    registry.add_asset(_new_asset("archive-001", "c1"))
    registry.archive_asset("archive-001", "c1")
    assert registry.can_be_reference("archive-001", "c1") is False


def test_16_templates_are_ascii_safe(tmp_path: Path) -> None:
    template_files = [
        ROOT / "productions" / "chi_yan_tian_qiong" / "assets" / "asset_registry.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "review_records.template.jsonl",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "IMAGE_REVIEW_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "VIDEO_REVIEW_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "RERUN_REASON_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_REGISTRY_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_RECORD_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "MANIFEST_TEMPLATE.csv",
    ]
    for path in template_files:
        text = path.read_text(encoding="utf-8")
        assert "????" not in text
        assert path.exists()


def test_17_templates_do_not_contain_false_true_mixed_token(tmp_path: Path) -> None:
    template_files = [
        ROOT / "productions" / "chi_yan_tian_qiong" / "assets" / "asset_registry.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "review_records.template.jsonl",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "IMAGE_REVIEW_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "VIDEO_REVIEW_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "RERUN_REASON_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_REGISTRY_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_RECORD_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "MANIFEST_TEMPLATE.csv",
    ]
    for path in template_files:
        text = path.read_text(encoding="utf-8")
        assert "false?True" not in text


def test_18_no_external_path_writes_in_registry_or_review_records(tmp_path: Path) -> None:
    workspace, _, registry, review = _new_tester(tmp_path)
    registry.add_asset(_new_asset("safe", "c1"))
    review.approve_candidate("safe", "c1", reviewer="user", source_path="source.png")
    assert registry.path.is_relative_to(workspace)
    assert review.record_path.is_relative_to(workspace)


def test_19_live_run_remains_disabled(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False
    with pytest.raises(RuntimeError):
        runner.execute(RunMode.live, tasks=[], task_or_batch_name="LIVE-BLOCKED")

def test_20_no_dreamina_command_execution_in_phase_c_checks(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    task_id = "TASK-CHECK"
    call_log: list[Any] = []
    def _run(*args: Any, **kwargs: Any) -> int:
        call_log.append((args, kwargs))
        return 0

    monkeypatch.setattr("subprocess.run", _run)
    runner.dry_run(
        [_new_task(task_id)],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-CHECK",
    )
    runner.mock_run(
        [_new_task(task_id + "B")],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-CHECK-MOCK",
    )
    assert call_log == []


def _new_task(task_id: str = "task-c") -> Any:
    from app.ai_video_pipeline.core.models import ProviderName, TaskSpec, TaskType

    return TaskSpec(
        task_id=task_id,
        phase="phaseC",
        task_type=TaskType.text2image,
        provider=ProviderName.dreamina_cli,
        model_version="5.0",
        ratio="16:9",
        resolution_type="2k",
        duration=None,
        video_resolution="720p",
        prompt="phase C test",
        reference_ids=[],
        output_name=task_id,
        status=None,
        review_status=None,
        notes=None,
    )
