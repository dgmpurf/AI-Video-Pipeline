from __future__ import annotations

import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import RunMode, TaskType
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "dreamina_preflight_text2image_001.csv"
SUMMARY = ROOT / "reports" / "dreamina_preflight_text2image_001_readiness_summary.json"
FS_PLAN = ROOT / "reports" / "dreamina_preflight_text2image_001_fs_write_plan.json"
CHECKLIST = ROOT / "reports" / "DREAMINA_PREFLIGHT_TEXT2IMAGE_001_LIVE_APPROVAL_CHECKLIST.json"
REPORT = ROOT / "reports" / "PHASE_F3_DREAMINA_SINGLE_TASK_READINESS_REPORT.md"


def _summary() -> dict:
    return json.loads(SUMMARY.read_text(encoding="utf-8"))


def _argv() -> list[str]:
    return list(_summary()["dry_run_argv"])


def test_01_candidate_manifest_has_exactly_one_task() -> None:
    tasks = parse_manifest_csv(MANIFEST)
    assert len(tasks) == 1
    assert tasks[0].task_id == "DREAMINA-PREFLIGHT-TEXT2IMAGE-001"


def test_02_candidate_task_is_text2image() -> None:
    assert parse_manifest_csv(MANIFEST)[0].task_type == TaskType.text2image


def test_03_dry_run_argv_uses_text2image() -> None:
    assert _argv()[1] == "text2image"


def test_04_dry_run_argv_includes_prompt() -> None:
    assert "--prompt" in _argv()


def test_05_dry_run_argv_includes_model_version_5() -> None:
    argv = _argv()
    assert argv[argv.index("--model_version") + 1] == "5.0"


def test_06_dry_run_argv_includes_ratio_16_9() -> None:
    argv = _argv()
    assert argv[argv.index("--ratio") + 1] == "16:9"


def test_07_dry_run_argv_includes_resolution_type_2k() -> None:
    argv = _argv()
    assert argv[argv.index("--resolution_type") + 1] == "2k"


def test_08_dry_run_argv_does_not_contain_output_dir() -> None:
    joined = " ".join(_argv())
    assert "output_dir" not in joined
    assert "--output_name" not in _argv()


def test_09_dry_run_argv_does_not_contain_query_result() -> None:
    assert "query_result" not in _argv()


def test_10_dry_run_argv_does_not_contain_submit_id_or_download_dir() -> None:
    joined = " ".join(_argv())
    assert "submit_id" not in joined
    assert "download_dir" not in joined
    assert "--image" not in _argv()
    assert "--images" not in _argv()


def test_11_default_live_gate_denies_dreamina_cli_allow_live_false() -> None:
    data = _summary()
    assert data["default_gate"]["allowed"] is False
    assert "dreamina_cli live-run disabled by provider config" in data["default_gate"]["required_actions"]


def test_12_hypothetical_readiness_passes_without_modifying_providers_json() -> None:
    data = _summary()
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert data["hypothetical_readiness"]["readiness_package_valid"] is True
    assert providers["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_13_fs_write_plan_executed_values_are_all_false() -> None:
    plan = json.loads(FS_PLAN.read_text(encoding="utf-8"))
    assert plan["approved"] is True
    assert all(item["executed"] is False for item in plan["planned_operations"])


def test_14_approval_checklist_user_approved_live_run_false() -> None:
    checklist = json.loads(CHECKLIST.read_text(encoding="utf-8"))
    assert checklist["user_approved_live_run"] is False


def test_15_approval_checklist_provider_live_run_enabled_false() -> None:
    checklist = json.loads(CHECKLIST.read_text(encoding="utf-8"))
    assert checklist["provider_live_run_enabled"] is False


def test_16_no_submit_query_download_happened() -> None:
    data = _summary()
    assert data["submit_query_download_happened"] is False
    provider_requests = Path(data["provider_requests_path"]).read_text(encoding="utf-8")
    assert '"status": "prepared"' in provider_requests


def test_17_no_external_path_write() -> None:
    data = _summary()
    assert data["external_path_touched"] is False
    for key in ["manifest_path", "dry_run_run_dir", "command_preview_path", "provider_requests_path", "fs_write_plan_path", "approval_checklist_path"]:
        assert Path(data[key]).is_relative_to(ROOT)


def test_18_reports_do_not_contain_question_mark_artifact() -> None:
    assert "????" not in REPORT.read_text(encoding="utf-8")


def test_19_reports_do_not_contain_false_true_artifact() -> None:
    assert "false?True" not in REPORT.read_text(encoding="utf-8")


def test_20_live_run_remains_disabled_in_runner() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False


def test_21_hypothetical_gate_can_be_recomputed_from_package() -> None:
    task = parse_manifest_csv(MANIFEST)[0]
    data = _summary()
    request = LiveRunRequest(
        production_id="chi_yan_tian_qiong",
        task_id=task.task_id,
        run_mode=RunMode.live,
        provider=task.provider.value,
        manifest_path=MANIFEST,
        reference_registry_path=None,
        fs_write_plan_path=FS_PLAN,
        user_confirmed=True,
        allow_single_task_only=True,
        dry_run_id=data["dry_run_run_id"],
        notes="test recompute only",
    )
    hypothetical = {
        "providers": {
            "dreamina_cli": {
                "enabled": True,
                "mode": "cli",
                "executable": "C:/Users/msjpurf/bin/dreamina.exe",
                "allow_live_run": True,
            }
        }
    }
    decision = validate_live_run_request(request, [task], hypothetical, PathPolicy(ROOT))
    assert decision.allowed is True
