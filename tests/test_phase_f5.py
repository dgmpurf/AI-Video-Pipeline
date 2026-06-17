from __future__ import annotations

import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import TaskType

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "production_text2image_A-SC-TEMPLE-COURTYARD-001.csv"
PROMPT_RECORD = ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-001.json"
CHECKLIST = ROOT / "reports" / "A-SC-TEMPLE-COURTYARD-001_LIVE_APPROVAL_CHECKLIST.json"
FS_PLAN = ROOT / "reports" / "A-SC-TEMPLE-COURTYARD-001_fs_write_plan.json"
SUMMARY = ROOT / "reports" / "A-SC-TEMPLE-COURTYARD-001_readiness_summary.json"
REPORT = ROOT / "reports" / "PHASE_F5_PRODUCTION_TEXT2IMAGE_READINESS_REPORT.md"


def _task():
    return parse_manifest_csv(MANIFEST)[0]


def _summary() -> dict:
    return json.loads(SUMMARY.read_text(encoding="utf-8"))


def _argv() -> list[str]:
    return list(_summary()["dry_run_argv"])


def test_01_production_manifest_has_exactly_one_task() -> None:
    assert len(parse_manifest_csv(MANIFEST)) == 1


def test_02_task_id_is_expected_scene_asset_id() -> None:
    assert _task().task_id == "A-SC-TEMPLE-COURTYARD-001"


def test_03_task_type_is_text2image() -> None:
    assert _task().task_type == TaskType.text2image


def test_04_prompt_record_marks_scene_asset_not_shot_keyframe() -> None:
    payload = json.loads(PROMPT_RECORD.read_text(encoding="utf-8"))
    assert payload["asset_scope"] == "production_scene_asset"
    assert payload["shot_id"] is None
    assert payload["reference_ids"] == []


def test_05_dry_run_argv_uses_text2image() -> None:
    assert _argv()[1] == "text2image"


def test_06_dry_run_argv_includes_prompt() -> None:
    assert "--prompt" in _argv()


def test_07_dry_run_argv_includes_model_version_5() -> None:
    argv = _argv()
    assert argv[argv.index("--model_version") + 1] == "5.0"


def test_08_dry_run_argv_includes_ratio_16_9() -> None:
    argv = _argv()
    assert argv[argv.index("--ratio") + 1] == "16:9"


def test_09_dry_run_argv_includes_resolution_type_2k() -> None:
    argv = _argv()
    assert argv[argv.index("--resolution_type") + 1] == "2k"


def test_10_dry_run_argv_does_not_include_output_name_or_output_dir() -> None:
    joined = " ".join(_argv())
    assert "--output_name" not in _argv()
    assert "output_dir" not in joined


def test_11_dry_run_argv_does_not_include_query_result_or_submit_id() -> None:
    joined = " ".join(_argv())
    assert "query_result" not in joined
    assert "submit_id" not in joined


def test_12_dry_run_argv_does_not_include_image_reference_flags() -> None:
    argv = _argv()
    assert "--image" not in argv
    assert "--images" not in argv
    assert "--refs" not in argv
    assert "--ref_strength" not in argv


def test_13_approval_checklist_remains_unapproved() -> None:
    payload = json.loads(CHECKLIST.read_text(encoding="utf-8"))
    assert payload["user_approved_live_run"] is False
    assert payload["provider_live_run_enabled"] is False
    assert payload["allow_batch"] is False
    assert payload["allow_parallel"] is False
    assert payload["allow_auto_continue"] is False
    assert payload["allow_retry"] is False


def test_14_fs_write_plan_executed_values_are_all_false() -> None:
    payload = json.loads(FS_PLAN.read_text(encoding="utf-8"))
    assert payload["approved"] is False
    assert all(item["executed"] is False for item in payload["planned_operations"])


def test_15_providers_json_remains_allow_live_run_false() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert payload["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_16_no_submit_query_download_happened() -> None:
    summary = _summary()
    assert summary["submit_query_download_happened"] is False
    assert summary["default_live_gate"]["allowed"] is False
    assert "dreamina_cli live-run disabled by provider config" in summary["default_live_gate"]["required_actions"]


def test_17_dry_run_artifacts_are_inside_workspace() -> None:
    summary = _summary()
    for key in ["dry_run_run_dir", "command_preview_path", "provider_requests_path", "job_store_path"]:
        assert Path(summary[key]).is_relative_to(ROOT)


def test_18_reports_do_not_contain_question_mark_artifact() -> None:
    for path in [REPORT, SUMMARY, FS_PLAN, CHECKLIST]:
        assert "????" not in path.read_text(encoding="utf-8")


def test_19_reports_do_not_contain_false_true_artifact() -> None:
    for path in [REPORT, SUMMARY, FS_PLAN, CHECKLIST]:
        assert "false?True" not in path.read_text(encoding="utf-8")
