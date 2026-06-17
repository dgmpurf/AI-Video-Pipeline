from __future__ import annotations

import builtins
import subprocess
from pathlib import Path

import pytest

from app.ai_video_pipeline.core.models import ShotRecord, ShotStatus
from app.ai_video_pipeline.prompts.prompt_factory import PromptFactory
from app.ai_video_pipeline.prompts.reference_roles import ReferenceRole, validate_reference_roles

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "PHASE_D1_TEMPLATE_PLACEMENT_AUDIT.md"

APP_TEMPLATE_PATHS = [
    ROOT / "app" / "ai_video_pipeline" / "shots" / "SHOT_REGISTRY_TEMPLATE.json",
    ROOT / "app" / "ai_video_pipeline" / "prompts" / "PROMPT_RECORD_TEMPLATE.json",
]

PRODUCTION_TEMPLATE_PATHS = [
    ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "SHOT_REGISTRY_TEMPLATE.json",
    ROOT / "productions" / "chi_yan_tian_qiong" / "shots" / "shot_registry.template.json",
    ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "PROMPT_RECORD_TEMPLATE.json",
    ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "prompt_record.template.json",
]

FORBIDDEN_OLD_PATH_TOKENS = [
    "G:\\AICODING\\AI\u89c6\u9891\u5de5\u4f5c\u6d41",
    "G:/AICODING/AI\u89c6\u9891\u5de5\u4f5c\u6d41",
    "G:\\AICODING\\dreamina_upload_staging",
    "G:/AICODING/dreamina_upload_staging",
    "DreaminaBatcher_v2_clean",
    "V8_validation",
    "APITEST",
    "CLI_md",
]


def _read_report() -> str:
    return REPORT_PATH.read_text(encoding="utf-8")


def _make_shot() -> ShotRecord:
    return ShotRecord.from_dict(
        {
            "shot_id": "SHOT-D1-01",
            "production_id": "test_production",
            "sequence_id": "SEQ-01",
            "scene_id": "SCENE-01",
            "shot_index": 1,
            "title": "Template audit shot",
            "shot_type": "establishing",
            "duration_seconds": 6.0,
            "story_beat": "Audit beat",
            "visual_goal": "Audit visual goal",
            "action_goal": "The hero steps forward",
            "camera_goal": "Steady wide shot",
            "required_asset_ids": [],
            "previous_shot_id": None,
            "next_shot_id": None,
            "status": ShotStatus.draft.value,
            "review_status": "pending_review",
            "notes": "",
        }
    )


def _scan_app_code_for_token(token: str) -> bool:
    for path in (ROOT / "app").rglob("*.py"):
        if not path.is_file():
            continue
        if token in path.read_text(encoding="utf-8", errors="replace"):
            return True
    return False


def test_01_production_templates_exist_and_live_under_productions() -> None:
    for path in PRODUCTION_TEMPLATE_PATHS:
        assert path.exists(), f"missing: {path}"
        assert path.relative_to(ROOT).parts[0] == "productions"


def test_02_app_level_template_status_is_audited_and_recorded() -> None:
    report = _read_report()
    for path in APP_TEMPLATE_PATHS:
        relative = path.relative_to(ROOT).as_posix()
        assert f"{relative} : missing (not present in app package)" in report
        if path.exists():
            assert "accidental duplicates" in report
            assert not _scan_app_code_for_token(path.name)
        else:
            assert "missing (not present in app package)" in report


def test_03_prompt_factory_uses_only_structured_inputs_and_no_subprocess_calls(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple] = []
    shot = _make_shot()

    def _blocked_open(*args: object, **kwargs: object) -> object:
        raise AssertionError("PromptFactory should not open filesystem files in prompt assembly")

    def _blocked_run(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        calls.append((args, kwargs))
        return subprocess.CompletedProcess(args=list(args), returncode=0)

    monkeypatch.setattr(builtins, "open", _blocked_open)
    monkeypatch.setattr(subprocess, "run", _blocked_run)

    PromptFactory.build_keyframe_prompt(shot, [], {"style_goal": "clean"}, ["no_text", "no_watermark"])
    PromptFactory.build_video_prompt(shot, [], "step sequence", "stable track", ["no_text", "no_watermark"])
    PromptFactory.build_reference_role_block([])

    assert calls == []


def test_04_prompt_layer_reference_order_and_vague_word_validation_remain_enforced() -> None:
    validate_reference_roles(
        [
            ReferenceRole(
                order=2,
                logical_id="b",
                role_type="prop",
                role_description="prop",
                lock_strength="low",
                allowed_drift="low",
            ),
            ReferenceRole(
                order=1,
                logical_id="a",
                role_type="character_subject",
                role_description="character",
                lock_strength="high",
                allowed_drift="low",
            ),
        ],
        ["a", "b"],
    )

    assert validate_reference_roles.__name__ == "validate_reference_roles"
    assert PromptFactory.contains_vague_action_language("about to jump") is True
    assert PromptFactory.contains_vague_action_language("the hero pivots and lands") is False


def test_05_phase_d1_and_phase_d_reports_do_not_contain_encoding_artifacts() -> None:
    for path in [ROOT / "reports" / "PHASE_D_SHOT_PROMPT_REPORT.md", REPORT_PATH]:
        text = path.read_text(encoding="utf-8")
        assert "????" not in text
        assert "false?True" not in text


def test_06_old_path_tokens_are_not_present_outside_historical_scan_definitions() -> None:
    allowed_match_files = {
        (ROOT / "app" / "ai_video_pipeline" / "tools" / "path_scan.py").resolve(),
        (ROOT / "reports" / "PHASE_A1_1_ENCODING_SAFE_PATH_SCAN.md").resolve(),
        (ROOT / "reports" / "PHASE_B1_1_GAP_CLOSURE_REPORT.md").resolve(),
        REPORT_PATH.resolve(),
        Path(__file__).resolve(),
    }
    blocked_matches: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name.lower().endswith(".pyc"):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".zip", ".tar", ".gz", ".exe", ".dll", ".so", ".pdf", ".npy", ".npz"}:
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in FORBIDDEN_OLD_PATH_TOKENS:
            if token in text and path.resolve() not in allowed_match_files:
                blocked_matches.append(f"{path}: {token}")

    assert blocked_matches == [], "forbidden legacy tokens found outside allowed scope:\n" + "\n".join(blocked_matches)
