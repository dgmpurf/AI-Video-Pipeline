from __future__ import annotations

import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "A-CH-B-SUBJECT-001"
MANIFEST = ROOT / "productions" / PRODUCTION_ID / "manifests" / "production_text2image_A-CH-B-SUBJECT-001.csv"
PROMPT_RECORD = ROOT / "productions" / PRODUCTION_ID / "prompts" / "production_character_subject_prompt_A-CH-B-SUBJECT-001.json"
FS_PLAN = ROOT / "reports" / "A-CH-B-SUBJECT-001_fs_write_plan.json"
CHECKLIST = ROOT / "reports" / "A-CH-B-SUBJECT-001_LIVE_APPROVAL_CHECKLIST.json"
SUMMARY = ROOT / "reports" / "A-CH-B-SUBJECT-001_readiness_summary.json"
REPORT = ROOT / "reports" / "PHASE_G3_SHUANGJI_CHARACTER_SUBJECT_READINESS_REPORT.md"


def _latest_dry_run_dir() -> Path:
    runs_root = ROOT / "productions" / PRODUCTION_ID / "runs" / "dry_run"
    candidates = [item for item in runs_root.iterdir() if item.is_dir() and TASK_ID in item.name]
    assert candidates, "no G3 dry-run directory found"
    return sorted(candidates)[-1]


def _latest_provider_request() -> dict:
    provider_requests = _latest_dry_run_dir() / "provider_requests.jsonl"
    payload = [json.loads(item) for item in provider_requests.read_text(encoding="utf-8").splitlines() if item.strip()]
    assert len(payload) == 1
    return payload[0]


def test_01_production_manifest_has_exactly_one_task() -> None:
    assert len(parse_manifest_csv(MANIFEST)) == 1


def test_02_task_id_is_expected_subject_task() -> None:
    task = parse_manifest_csv(MANIFEST)[0]
    assert task.task_id == TASK_ID


def test_03_task_type_is_text2image() -> None:
    task = parse_manifest_csv(MANIFEST)[0]
    assert task.task_type.value == "text2image"


def test_04_dry_run_argv_uses_text2image() -> None:
    argv = _latest_provider_request()["command_argv"]
    assert argv[1] == "text2image"


def test_05_dry_run_argv_includes_prompt_and_model_version_ratio_resolution() -> None:
    argv = _latest_provider_request()["command_argv"]
    assert "--prompt" in argv
    assert argv[argv.index("--model_version") + 1] == "5.0"
    assert argv[argv.index("--ratio") + 1] == "9:16"
    assert argv[argv.index("--resolution_type") + 1] == "2k"


def test_06_dry_run_argv_does_not_include_forbidden_fields() -> None:
    argv = _latest_provider_request()["command_argv"]
    joined = " ".join(argv)
    assert "--output_name" not in argv
    assert "output_dir" not in joined
    assert "query_result" not in joined
    assert "--image" not in argv
    assert "--images" not in argv
    assert "--refs" not in argv
    assert "--ref_strength" not in argv


def test_07_live_run_gate_denied_by_dreamina_provider_config() -> None:
    task = parse_manifest_csv(MANIFEST)[0]
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    run_dir = _latest_dry_run_dir()
    policy = PathPolicy(ROOT)
    decision = validate_live_run_request(
        LiveRunRequest(
            production_id=PRODUCTION_ID,
            task_id=TASK_ID,
            run_mode="live",
            provider=task.provider.value,
            manifest_path=MANIFEST,
            reference_registry_path=None,
            fs_write_plan_path=FS_PLAN,
            user_confirmed=True,
            allow_single_task_only=True,
            dry_run_id=run_dir.name,
            notes="g3 readiness check",
        ),
        [task],
        providers,
        policy,
    )
    assert decision.allowed is False
    assert "dreamina_cli live-run disabled by provider config" in decision.required_actions
    assert "approve fs_write_plan" in decision.required_actions
    assert "live-run denied by safety gate" in decision.reason or "safety gate" in decision.reason


def test_08_hypothetical_readiness_result_matches_expected_flags() -> None:
    payload = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert payload["dry_run_run_id"] == _latest_dry_run_dir().name
    readiness = payload["hypothetical_readiness"]
    assert payload["default_live_gate"]["allowed"] is False
    assert readiness["allowed"] is False
    assert readiness["readiness_package_prepared"] is True
    assert readiness["blocked_until_provider_live_run_enabled"] is True
    assert readiness["blocked_until_fs_write_plan_reviewed"] is True


def test_09_approval_checklist_stays_unapproved() -> None:
    payload = json.loads(CHECKLIST.read_text(encoding="utf-8"))
    assert payload["user_approved_live_run"] is False
    assert payload["provider_live_run_enabled"] is False
    assert payload["allow_single_task_only"] is True
    assert payload["allow_batch"] is False
    assert payload["allow_parallel"] is False
    assert payload["allow_auto_continue"] is False
    assert payload["allow_retry"] is False
    assert payload["dry_run_passed"] is True
    assert payload["fs_write_plan_reviewed"] is False


def test_10_fs_write_plan_executed_values_are_all_false() -> None:
    payload = json.loads(FS_PLAN.read_text(encoding="utf-8"))
    assert payload["approved"] is False
    for item in payload["planned_operations"]:
        assert item["executed"] is False


def test_11_providers_json_still_disables_live_run() -> None:
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert providers["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_12_no_submit_query_download_happened() -> None:
    payload = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert payload["submit_query_download_happened"] is False
    run_dir = _latest_dry_run_dir()
    command_preview = (run_dir / "command_preview.csv").read_text(encoding="utf-8")
    assert "query_result" not in command_preview
    assert "download_dir" not in command_preview
    request = _latest_provider_request()
    assert request["status"] == "prepared"


def test_13_reports_and_generated_files_do_not_contain_garbled_tokens() -> None:
    for path in [SUMMARY, REPORT, FS_PLAN, CHECKLIST, PROMPT_RECORD]:
        text = Path(path).read_text(encoding="utf-8")
        assert "????" not in text
        assert "false?True" not in text


def test_14_prompt_record_exists_for_A_CH_B_task() -> None:
    payload = json.loads(PROMPT_RECORD.read_text(encoding="utf-8"))
    assert payload["prompt_id"] == TASK_ID
    assert payload["asset_scope"] == "production_character_subject"
