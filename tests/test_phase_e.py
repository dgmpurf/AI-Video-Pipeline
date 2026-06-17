from __future__ import annotations

import csv
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.ai_video_pipeline.assets.registry import AssetRegistry
from app.ai_video_pipeline.core.manifest import MANIFEST_FIELDS, parse_manifest_csv
from app.ai_video_pipeline.core.manifest_writer import read_task_manifest, write_task_manifest
from app.ai_video_pipeline.core.models import (
    AssetRecord,
    AssetStatus,
    AssetType,
    ProviderName,
    ReviewStatus,
    RunMode,
    ShotRecord,
    ShotStatus,
    TaskType,
)
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.execution.task_compiler import compile_prompt_to_task
from app.ai_video_pipeline.path_policy import PathPolicy, PathPolicyError
from app.ai_video_pipeline.prompts.prompt_record import PromptRecord
from app.ai_video_pipeline.prompts.prompt_validation import PromptValidationError, validate_prompt_record

ROOT = Path(__file__).resolve().parents[1]
TEST_PRODUCTION_ID = "test_production"


def _init_workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    (workspace / "mock_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "live_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / TEST_PRODUCTION_ID / "manifests").mkdir(parents=True, exist_ok=True)
    (workspace / "refs").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    return workspace


def _shot(required_asset_ids: list[str] | None = None) -> ShotRecord:
    return ShotRecord.from_dict(
        {
            "shot_id": "SHOT-001",
            "production_id": TEST_PRODUCTION_ID,
            "sequence_id": "SEQ-01",
            "scene_id": "SCENE-01",
            "shot_index": 1,
            "title": "Phase E shot",
            "shot_type": "establishing",
            "duration_seconds": 5,
            "story_beat": "beat",
            "visual_goal": "visual target",
            "action_goal": "walk forward",
            "camera_goal": "slow push",
            "required_asset_ids": required_asset_ids or [],
            "previous_shot_id": None,
            "next_shot_id": None,
            "status": ShotStatus.draft.value,
            "review_status": "pending_review",
            "notes": "",
        }
    )


def _prompt(
    prompt_type: str,
    reference_ids: list[str] | None = None,
    reference_roles: list[dict] | None = None,
    prompt_id: str = "PROMPT-001",
) -> PromptRecord:
    return PromptRecord.from_dict(
        {
            "prompt_id": prompt_id,
            "production_id": TEST_PRODUCTION_ID,
            "shot_id": "SHOT-001",
            "asset_id": None,
            "prompt_type": prompt_type,
            "version": "v1",
            "prompt_text": "compiled prompt text",
            "negative_prompt": "no text",
            "reference_ids": reference_ids or [],
            "reference_roles": reference_roles or [],
            "source_shot_id": "SHOT-001",
            "status": "draft",
            "notes": "phase e test",
            "created_at": "2026-06-13T00:00:00+00:00",
            "updated_at": "2026-06-13T00:00:00+00:00",
        }
    )


def _role(order: int, logical_id: str, lock_strength: str = "medium") -> dict:
    return {
        "order": order,
        "logical_id": logical_id,
        "role_type": "character_subject",
        "role_description": f"role {logical_id}",
        "lock_strength": lock_strength,
        "allowed_drift": "low",
    }


def _asset(logical_id: str, status: AssetStatus = AssetStatus.candidate, tags: list[str] | None = None) -> AssetRecord:
    return AssetRecord(
        logical_id=logical_id,
        candidate_id="A",
        asset_type=AssetType.image,
        relative_path=Path(f"refs/{logical_id}.txt"),
        status=status,
        review_status=ReviewStatus.pending_review,
        tags=tags or [],
    )


def test_01_keyframe_prompt_compiles_to_image2image() -> None:
    task = compile_prompt_to_task(_prompt("keyframe_image", ["ref-a"]), _shot(), {})
    assert task.task_type == TaskType.image2image
    assert task.provider == ProviderName.dreamina_cli
    assert task.model_version == "5.0"


def test_02_video_prompt_compiles_to_multimodal2video() -> None:
    task = compile_prompt_to_task(_prompt("video", ["kf-a"]), _shot(), {})
    assert task.task_type == TaskType.multimodal2video
    assert task.model_version == "seedance2.0fast_vip"
    assert task.duration == 5
    assert task.video_resolution == "720p"


def test_03_asset_image_without_reference_compiles_to_text2image() -> None:
    assert compile_prompt_to_task(_prompt("asset_image"), _shot(), {}).task_type == TaskType.text2image


def test_04_asset_image_with_reference_compiles_to_image2image() -> None:
    assert compile_prompt_to_task(_prompt("asset_image", ["ref-a"]), _shot(), {}).task_type == TaskType.image2image


def test_05_reference_id_order_is_preserved() -> None:
    task = compile_prompt_to_task(_prompt("keyframe_image", ["a", "b", "c"]), _shot(), {})
    assert task.reference_ids == ["a", "b", "c"]


def test_06_manifest_writer_joins_reference_ids_with_pipe(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    task = compile_prompt_to_task(_prompt("keyframe_image", ["a", "b"]), _shot(), {})
    manifest_path = write_task_manifest([task], workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "compiled.csv", policy)
    row = list(csv.DictReader(manifest_path.open("r", encoding="utf-8", newline="")))[0]
    assert row["reference_ids"] == "a|b"


def test_07_manifest_writer_uses_deterministic_field_order(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    task = compile_prompt_to_task(_prompt("asset_image"), _shot(), {})
    manifest_path = write_task_manifest([task], workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "compiled.csv", policy)
    header = manifest_path.read_text(encoding="utf-8").splitlines()[0].split(",")
    assert header == MANIFEST_FIELDS


def test_08_missing_prompt_id_fails() -> None:
    with pytest.raises(ValueError, match="prompt_id is required"):
        PromptRecord.from_dict(_prompt("asset_image").asdict() | {"prompt_id": ""})


def test_09_missing_prompt_text_fails() -> None:
    with pytest.raises(ValueError, match="prompt_text is required"):
        PromptRecord.from_dict(_prompt("asset_image").asdict() | {"prompt_text": ""})


def test_10_unknown_prompt_type_fails() -> None:
    prompt = _prompt("asset_image")
    prompt.prompt_type = "unknown"
    with pytest.raises(PromptValidationError, match="unknown prompt_type"):
        validate_prompt_record(prompt, _shot())


def test_11_reference_role_count_mismatch_fails() -> None:
    with pytest.raises(ValueError, match="reference_ids count must match reference_roles count"):
        _prompt("keyframe_image", ["a", "b"], [_role(1, "a")])


def test_12_rejected_asset_cannot_be_used_as_reference(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    registry = AssetRegistry(workspace / "asset_registry.json", PathPolicy(workspace))
    registry.add_asset(_asset("ref-a", AssetStatus.rejected))
    with pytest.raises(PromptValidationError, match="rejected asset"):
        validate_prompt_record(_prompt("keyframe_image", ["ref-a"]), _shot(), registry)


def test_13_archived_asset_cannot_be_used_by_default(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    registry = AssetRegistry(workspace / "asset_registry.json", PathPolicy(workspace))
    registry.add_asset(_asset("ref-a", AssetStatus.archived))
    with pytest.raises(PromptValidationError, match="archived asset"):
        validate_prompt_record(_prompt("keyframe_image", ["ref-a"]), _shot(), registry)


def test_14_mock_asset_cannot_be_used_as_locked_reference(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    registry = AssetRegistry(workspace / "asset_registry.json", PathPolicy(workspace))
    registry.add_asset(_asset("ref-a", tags=["mock"]))
    prompt = _prompt("keyframe_image", ["ref-a"], [_role(1, "ref-a", lock_strength="high")])
    with pytest.raises(PromptValidationError, match="mock asset"):
        validate_prompt_record(prompt, _shot(), registry)


def test_15_compiled_manifest_can_be_loaded_by_existing_parser(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    task = compile_prompt_to_task(_prompt("asset_image"), _shot(), {})
    manifest_path = write_task_manifest([task], workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "compiled.csv", policy)
    assert parse_manifest_csv(manifest_path)[0].task_id == task.task_id
    assert read_task_manifest(manifest_path, policy)[0].task_type == TaskType.text2image


def test_16_compiled_manifest_can_run_dry_run_only(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = {}
    for name in ["a", "b", "c"]:
        path = workspace / "refs" / f"{name}.txt"
        path.write_text(f"dummy {name}", encoding="utf-8")
        refs[name] = str(path.relative_to(workspace))
    task = compile_prompt_to_task(_prompt("keyframe_image", ["a", "b", "c"]), _shot(), {})
    manifest_path = write_task_manifest(
        [task],
        workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "compiled.csv",
        PathPolicy(workspace),
    )
    artifacts = PipelineRunner(workspace, reference_registry=refs).dry_run(
        production_id=TEST_PRODUCTION_ID,
        manifest_paths=[manifest_path],
        task_or_batch_name="phase-e",
    )
    assert artifacts.provider_requests_jsonl.exists()
    assert artifacts.command_preview_csv.exists()
    assert artifacts.job_store_json.exists()
    assert artifacts.run_root.is_relative_to(workspace)


def test_17_dry_run_does_not_call_dreamina(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    workspace = _init_workspace(tmp_path)
    calls: list[tuple] = []
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: calls.append((args, kwargs)))
    task = compile_prompt_to_task(_prompt("asset_image"), _shot(), {})
    PipelineRunner(workspace).dry_run([task], production_id=TEST_PRODUCTION_ID, task_or_batch_name="phase-e")
    assert calls == []


def test_18_live_run_remains_disabled(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False
    with pytest.raises(RuntimeError, match="Live run is disabled"):
        runner.execute(RunMode.live, [compile_prompt_to_task(_prompt("asset_image"), _shot(), {})], production_id=TEST_PRODUCTION_ID)


def test_19_output_paths_stay_inside_workspace(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    task = compile_prompt_to_task(_prompt("asset_image"), _shot(), {})
    output = write_task_manifest([task], workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "compiled.csv", policy)
    assert output.is_relative_to(workspace)
    with pytest.raises(PathPolicyError):
        write_task_manifest([task], workspace.parent / "outside.csv", policy)


def test_20_reports_do_not_contain_question_mark_artifacts() -> None:
    text = (ROOT / "reports" / "PHASE_E_TASK_COMPILER_REPORT.md").read_text(encoding="utf-8")
    assert "????" not in text


def test_21_reports_do_not_contain_false_true_artifact() -> None:
    text = (ROOT / "reports" / "PHASE_E_TASK_COMPILER_REPORT.md").read_text(encoding="utf-8")
    assert "false?True" not in text


def test_22_phase_e_sample_compiled_manifest_exists_and_loads() -> None:
    manifest_path = ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "sample_compiled_manifest.phase_e.csv"
    tasks = parse_manifest_csv(manifest_path)
    assert [task.task_id for task in tasks] == ["SHOT-001-KF", "SHOT-001-VIDEO"]
    assert tasks[0].reference_ids == ["CHAR-A-SUBJECT", "CHAR-B-SUBJECT", "SCENE-TEMPLE"]
