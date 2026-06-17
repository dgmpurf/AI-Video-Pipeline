from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.ai_video_pipeline.assets.registry import AssetRecord, AssetRegistry
from app.ai_video_pipeline.core.models import (
    AssetRole,
    AssetStatus,
    AssetType,
    ProviderName,
    ReviewStatus,
    RunMode,
    ShotRecord,
    ShotStatus,
    TaskSpec,
    TaskType,
)
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy
from app.ai_video_pipeline.prompts.negative_rules import DEFAULT_NEGATIVE_RULE_SETS
from app.ai_video_pipeline.prompts.prompt_factory import PromptFactory
from app.ai_video_pipeline.prompts.prompt_record import PromptRecord
from app.ai_video_pipeline.prompts.reference_roles import ReferenceRole, validate_reference_roles
from app.ai_video_pipeline.shots.shot_registry import ShotRegistry, ShotRegistryError

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
    return workspace


def _registry_path(workspace: Path) -> Path:
    return workspace / "productions" / TEST_PRODUCTION_ID / "shots" / "shot_registry.json"


def _shot_payload(index: int, shot_id: str, shot_type: str = "establishing", action_goal: str = "") -> dict:
    return {
        "shot_id": shot_id,
        "production_id": TEST_PRODUCTION_ID,
        "sequence_id": "SEQ-01",
        "scene_id": "SCENE-01",
        "shot_index": index,
        "title": f"Shot {index}",
        "shot_type": shot_type,
        "duration_seconds": 4.0,
        "story_beat": "beat",
        "visual_goal": "visual target",
        "action_goal": action_goal,
        "camera_goal": "camera plan",
        "required_asset_ids": [],
        "previous_shot_id": None,
        "next_shot_id": None,
        "status": ShotStatus.draft.value,
        "review_status": "pending_review",
        "notes": "",
    }


def _new_asset(logical_id: str, candidate_id: str) -> AssetRecord:
    return AssetRecord(
        logical_id=logical_id,
        candidate_id=candidate_id,
        asset_type=AssetType.image,
        role=AssetRole.source,
        relative_path=Path(f"assets/{logical_id}_{candidate_id}.png"),
        source_path=Path(f"tests/fixtures/media/{logical_id}_{candidate_id}.png"),
        status=AssetStatus.candidate,
        review_status=ReviewStatus.pending_review,
    )


def _new_task(task_id: str = "task-d", provider: ProviderName = ProviderName.dreamina_cli) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        phase="phaseD",
        task_type=TaskType.text2image,
        provider=provider,
        model_version="5.0",
        ratio="16:9",
        resolution_type="2k",
        duration=None,
        video_resolution="720p",
        prompt="phase D test",
        reference_ids=[],
        output_name=task_id,
        status=None,
        review_status=None,
        notes=None,
    )


def test_01_shot_registry_add_and_get(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    registry = ShotRegistry(_registry_path(workspace), policy)
    shot = ShotRecord.from_dict(_shot_payload(1, "SHOT-001"))
    registry.add_shot(shot)
    assert registry.get_by_shot_id("SHOT-001") == shot


def test_02_shot_registry_validates_continuity_links(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    registry = ShotRegistry(_registry_path(workspace), policy)

    first = ShotRecord.from_dict(_shot_payload(1, "SHOT-001"))
    second = ShotRecord.from_dict(_shot_payload(2, "SHOT-002"))
    third = ShotRecord.from_dict(_shot_payload(3, "SHOT-003"))

    first.next_shot_id = "SHOT-002"
    second.previous_shot_id = "SHOT-001"
    second.next_shot_id = "SHOT-003"
    third.previous_shot_id = "SHOT-002"

    registry.add_shot(first)
    registry.add_shot(second)
    registry.add_shot(third)
    registry.validate_continuity()

    bad = ShotRecord.from_dict(_shot_payload(4, "SHOT-004"))
    bad.previous_shot_id = "MISSING"
    with pytest.raises(ShotRegistryError, match="Missing previous shot"):
        registry.add_shot(bad)


def test_03_shot_registry_requires_assets_when_asset_registry_exists(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    asset_registry = AssetRegistry(workspace / "productions" / TEST_PRODUCTION_ID / "assets" / "asset_registry.json", policy)
    registry = ShotRegistry(
        _registry_path(workspace),
        policy,
        asset_registry=asset_registry,
    )
    shot = ShotRecord.from_dict(
        _shot_payload(1, "SHOT-REQ") | {
            "required_asset_ids": ["fixture-001:A"],
        }
    )
    with pytest.raises(ShotRegistryError, match="Missing required asset"):
        registry.add_shot(shot)

    asset_registry.add_asset(_new_asset("fixture-001", "A"))
    registry.add_shot(shot)
    assert registry.get_by_shot_id("SHOT-REQ") is not None


def test_04_prompt_record_requires_prompt_id() -> None:
    with pytest.raises(ValueError, match="prompt_id is required"):
        PromptRecord.from_dict(json.loads(
            ROOT.joinpath("tests/fixtures/shot_prompt/sample_prompt_record.json").read_text(encoding="utf-8")
        ) | {"prompt_id": ""})


def test_05_prompt_record_requires_prompt_text() -> None:
    with pytest.raises(ValueError, match="prompt_text is required"):
        PromptRecord.from_dict({
            "prompt_id": "PROMPT-ERR",
            "production_id": TEST_PRODUCTION_ID,
            "shot_id": None,
            "asset_id": None,
            "prompt_type": "asset_image",
            "version": "v1",
            "prompt_text": "",
            "negative_prompt": "",
            "reference_ids": [],
            "reference_roles": [],
            "source_shot_id": None,
            "status": "draft",
            "notes": "",
            "created_at": "2026-06-13T00:00:00+00:00",
            "updated_at": "2026-06-13T00:00:00+00:00",
        })


def test_06_reference_ids_order_must_match_reference_roles() -> None:
    fixture = json.loads(ROOT.joinpath("tests/fixtures/shot_prompt/sample_prompt_record.json").read_text(encoding="utf-8"))
    with pytest.raises(ValueError, match="reference_ids must match reference_roles order"):
        PromptRecord.from_dict(fixture | {"reference_ids": ["fixture-002", "fixture-001"]})


def test_07_reference_role_order_starts_at_one() -> None:
    with pytest.raises(ValueError, match="ReferenceRole order must start at 1"):
        validate_reference_roles([
            ReferenceRole(
                order=2,
                logical_id="logic-2",
                role_type="character_subject",
                role_description="subject",
                lock_strength="high",
                allowed_drift="low",
            )
        ], ["logic-2"])


def test_08_duplicate_reference_role_order_fails() -> None:
    with pytest.raises(ValueError, match="Duplicate ReferenceRole order"):
        validate_reference_roles(
            [
                ReferenceRole(
                    order=1,
                    logical_id="logic-1",
                    role_type="character_subject",
                    role_description="one",
                    lock_strength="high",
                    allowed_drift="low",
                ),
                ReferenceRole(
                    order=1,
                    logical_id="logic-2",
                    role_type="scene_environment",
                    role_description="two",
                    lock_strength="high",
                    allowed_drift="low",
                ),
            ],
            ["logic-1", "logic-2"],
        )


def test_09_prompt_factory_reference_roles_block_is_deterministic() -> None:
    role_block = PromptFactory.build_reference_role_block([
        {
            "order": 2,
            "logical_id": "second",
            "role_type": "prop",
            "role_description": "second",
            "lock_strength": "low",
            "allowed_drift": "low",
        },
        {
            "order": 1,
            "logical_id": "first",
            "role_type": "character_subject",
            "role_description": "first",
            "lock_strength": "high",
            "allowed_drift": "low",
        },
    ])
    lines = role_block.splitlines()
    assert lines[0].startswith("1.")
    assert lines[0].startswith("1. first")


def test_10_prompt_factory_keyframe_prompt_includes_visual_goal() -> None:
    shot = ShotRecord.from_dict(_shot_payload(1, "SHOT-KF"))
    prompt = PromptFactory.build_keyframe_prompt(shot, [], {"style_goal": "clean cinematic"}, ["no_text", "no_watermark"])
    assert "Visual goal: visual target" in prompt


def test_11_prompt_factory_video_prompt_includes_action_and_camera_goal() -> None:
    shot = ShotRecord.from_dict(_shot_payload(2, "SHOT-VA", shot_type="action", action_goal="character jumps forward"))
    prompt = PromptFactory.build_video_prompt(
        shot,
        [],
        motion_plan="lunge and rotate",
        camera_plan="low dolly push",
        negative_rules=["no_text", "no_watermark"],
    )
    assert "Action goal: character jumps forward" in prompt
    assert "Camera goal: camera plan" in prompt


def test_12_negative_rules_include_no_text_and_no_watermark() -> None:
    for prompt_type in ["asset_image", "keyframe_image", "video"]:
        names = set(DEFAULT_NEGATIVE_RULE_SETS[prompt_type])
        assert "no_text" in names
        assert "no_watermark" in names


def test_13_action_prompt_flags_vague_action_words() -> None:
    assert PromptFactory.contains_vague_action_language("The character is preparing to attack")
    assert PromptFactory.contains_vague_action_language("about to raise the sword")
    assert PromptFactory.contains_vague_action_language("wait before the action")
    assert not PromptFactory.contains_vague_action_language("The character lunges and lands")


def test_14_production_templates_are_ascii_safe() -> None:
    template_files = [
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_REGISTRY_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "shot_registry.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_RECORD_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "prompt_record.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "reference_roles.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "negative_rules.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_DESIGN_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_FACTORY_USAGE.md",
    ]
    for path in template_files:
        text = path.read_text(encoding="utf-8")
        assert "????" not in text


def test_15_production_templates_do_not_contain_false_true_mixed_token() -> None:
    template_files = [
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_REGISTRY_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_RECORD_TEMPLATE.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "reference_roles.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "negative_rules.template.json",
        ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_DESIGN_TEMPLATE.md",
        ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_FACTORY_USAGE.md",
    ]
    for path in template_files:
        text = path.read_text(encoding="utf-8")
        assert "false?True" not in text


def test_16_phase_d_report_is_ascii_safe(tmp_path: Path) -> None:
    report = ROOT / "reports" / "PHASE_D_SHOT_PROMPT_REPORT.md"
    assert report.exists()
    text = report.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text


def test_17_no_external_path_written_for_shot_registry(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    registry = ShotRegistry(_registry_path(workspace), policy)
    shot = ShotRecord.from_dict(_shot_payload(1, "SHOT-EXT"))
    registry.add_shot(shot)
    assert registry.path.is_relative_to(workspace)


def test_18_live_run_is_disabled_in_phase_d(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False
    with pytest.raises(RuntimeError):
        runner.execute(
            RunMode.live,
            tasks=[_new_task(task_id="TASK-LIVE")],
            production_id=TEST_PRODUCTION_ID,
            task_or_batch_name="RUN-LIVE",
        )


def test_19_no_dreamina_command_execution_in_phase_d_workflow(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    calls: list[list] = []

    def _run(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        calls.append(list(args))
        return subprocess.CompletedProcess(args=args, returncode=0)

    monkeypatch.setattr(subprocess, "run", _run)
    runner.dry_run(
        [_new_task(task_id="TASK-NO-CMD")],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-D",
    )
    runner.mock_run(
        [_new_task(task_id="TASK-NO-CMD-2")],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-D",
    )
    assert calls == []


def test_20_tests_use_test_production_and_not_legacy(tmp_path: Path) -> None:
    assert TEST_PRODUCTION_ID == "test_production"
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert not (workspace / "productions" / "legacy").exists()
