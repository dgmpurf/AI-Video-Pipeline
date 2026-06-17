from __future__ import annotations

import csv
import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import RunMode
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "SHOT-01-KF-001"

MANIFEST_PATH = ROOT / "productions" / PRODUCTION_ID / "manifests" / "production_image2image_SHOT-01-KF-001.csv"
PROMPT_PATH = ROOT / "productions" / PRODUCTION_ID / "prompts" / "shot_01_keyframe_prompt_SHOT-01-KF-001.json"
SHOT_PATH = ROOT / "productions" / PRODUCTION_ID / "shots" / "shot_01_keyframe_record.json"
SUMMARY_PATH = ROOT / "reports" / "SHOT-01-KF-001_readiness_summary.json"
FS_PLAN_PATH = ROOT / "reports" / "SHOT-01-KF-001_fs_write_plan.json"
CHECKLIST_PATH = ROOT / "reports" / "SHOT-01-KF-001_LIVE_APPROVAL_CHECKLIST.json"
REPORT_PATH = ROOT / "reports" / "PHASE_H1_SHOT01_KEYFRAME_READINESS_REPORT.md"


def _summary() -> dict:
    return json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))


def _run_dir() -> Path:
    return Path(_summary()["dry_run_run_dir"])


def _provider_request() -> list[dict]:
    request_file = _run_dir() / "provider_requests.jsonl"
    rows = [json.loads(line) for line in request_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 1
    return rows


def test_01_manifest_has_single_h1_image2image_task() -> None:
    tasks = parse_manifest_csv(MANIFEST_PATH)
    assert len(tasks) == 1
    task = tasks[0]
    assert task.task_id == TASK_ID
    assert task.phase == "shot_keyframe"
    assert task.task_type.value == "image2image"
    assert task.provider.value == "dreamina_cli"
    assert task.reference_ids == [
        "A-SC-TEMPLE-COURTYARD-001",
        "A-CH-A-SUBJECT-001",
        "A-CH-B-SUBJECT-001",
    ]


def test_02_prompt_record_reference_roles_match_manifest_order() -> None:
    prompt = json.loads(PROMPT_PATH.read_text(encoding="utf-8"))
    roles = prompt.get("reference_roles", [])
    assert prompt["prompt_id"] == TASK_ID
    assert [r["order"] for r in roles] == [1, 2, 3]
    assert [r["logical_id"] for r in roles] == [
        "A-SC-TEMPLE-COURTYARD-001",
        "A-CH-A-SUBJECT-001",
        "A-CH-B-SUBJECT-001",
    ]
    assert prompt["reference_ids"] == [r["logical_id"] for r in roles]


def test_03_shot_record_contains_expected_assets_for_h1() -> None:
    shot_payload = json.loads(SHOT_PATH.read_text(encoding="utf-8"))
    shots = shot_payload.get("shots", [])
    assert len(shots) == 1
    shot = shots[0]
    assert shot["shot_id"] == TASK_ID
    assert shot["shot_index"] == 1
    assert shot["required_asset_ids"] == [
        "A-SC-TEMPLE-COURTYARD-001",
        "A-CH-A-SUBJECT-001",
        "A-CH-B-SUBJECT-001",
    ]


def test_04_dry_run_argv_is_image2image_and_has_required_arguments() -> None:
    argv = _provider_request()[0]["command_argv"]
    assert argv[0] == "C:/Users/msjpurf/bin/dreamina.exe"
    assert argv[1] == "image2image"
    assert argv[argv.index("--model_version") + 1] == "5.0"
    assert argv[argv.index("--ratio") + 1] == "16:9"
    assert argv[argv.index("--resolution_type") + 1] == "2k"
    assert argv.count("--images") == 3
    assert "--prompt" in argv


def test_05_dry_run_argv_contains_no_forbidden_pipeline_fields() -> None:
    argv = _provider_request()[0]["command_argv"]
    joined = " ".join(argv)
    assert "--output_name" not in argv
    assert "--output_dir" not in joined
    assert "output_dir" not in joined
    assert "query_result" not in argv
    assert "--download_dir" not in argv
    assert "--image" not in argv


def test_06_dry_run_provider_request_prepared_status() -> None:
    request = _provider_request()[0]
    assert request["status"] == "prepared"
    assert request["task_id"] == TASK_ID
    assert request["provider"] == "dreamina_cli"
    assert request["task_type"] == "image2image"


def test_07_fs_write_plan_targets_are_well_formed_and_not_executed() -> None:
    payload = json.loads(FS_PLAN_PATH.read_text(encoding="utf-8"))
    assert payload["approved"] is False
    assert payload["task_id"] == TASK_ID
    assert payload["workspace_root"] == str(ROOT)
    assert all(item["executed"] is False for item in payload["planned_operations"])
    assert all("<future_run_id>/" in item["target"] for item in payload["planned_operations"])
    assert not any("<future_run_id/" in item["target"] for item in payload["planned_operations"])


def test_08_readiness_summary_default_gate_and_hypothetical_are_blocked() -> None:
    payload = _summary()
    default_gate = payload["default_live_gate"]
    hypo = payload["hypothetical_readiness"]
    assert default_gate["allowed"] is False
    assert hypo["allowed"] is False
    assert "dreamina_cli live-run disabled by provider config" in default_gate["required_actions"]
    assert "dreamina_cli live-run disabled by provider config" in hypo["required_actions"]
    assert "approve fs_write_plan" in default_gate["required_actions"]
    assert "approve fs_write_plan" in hypo["required_actions"]
    assert "create fs_write_plan" not in default_gate["required_actions"]
    assert "create fs_write_plan" not in hypo["required_actions"]
    assert payload["providers_json_allow_live_run"] is False
    assert payload["submit_query_download_happened"] is False
    assert payload["external_path_touched"] is False
    assert hypo["blocked_until_provider_live_run_enabled"] is True
    assert hypo["readiness_package_prepared"] is True


def test_09_readiness_and_artifacts_are_within_workspace() -> None:
    payload = _summary()
    run_dir = Path(payload["dry_run_run_dir"])
    assert run_dir.is_relative_to(ROOT)
    assert run_dir.name == payload["dry_run_run_id"]
    for key in ["command_preview_path", "provider_requests_path", "job_store_path"]:
        assert Path(payload[key]).is_relative_to(ROOT)
    for path in [run_dir / "command_preview.csv", run_dir / "provider_requests.jsonl", run_dir / "job_store.json", run_dir / "run_plan.json"]:
        assert path.exists()


def test_10_live_run_is_hard_disabled_by_config() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False


def test_11_approval_checklist_marks_default_readiness_flags() -> None:
    checklist = json.loads(CHECKLIST_PATH.read_text(encoding="utf-8"))
    assert checklist["task_id"] == TASK_ID
    assert checklist["production_id"] == PRODUCTION_ID
    assert checklist["user_approved_live_run"] is False
    assert checklist["provider_live_run_enabled"] is False
    assert checklist["allow_batch"] is False
    assert checklist["allow_parallel"] is False
    assert checklist["allow_auto_continue"] is False
    assert checklist["allow_retry"] is False
    assert checklist["dry_run_passed"] is True
    assert checklist["fs_write_plan_reviewed"] is False


def test_12_no_dreamina_submit_query_download_happened() -> None:
    request = _provider_request()[0]
    assert request["status"] == "prepared"
    run_dir = _run_dir()
    command_preview = list(csv.DictReader((run_dir / "command_preview.csv").open(encoding="utf-8", newline="")))[0]["command"]
    assert "query_result" not in command_preview
    assert "download_dir" not in command_preview
    assert "submit_id" not in request
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert providers["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_13_live_gate_decision_requires_approval_and_staging_for_multi_ref_task() -> None:
    task = parse_manifest_csv(MANIFEST_PATH)[0]
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    policy = PathPolicy(ROOT)
    decision = validate_live_run_request(
        LiveRunRequest(
            production_id=PRODUCTION_ID,
            task_id=TASK_ID,
            run_mode="live",
            provider=task.provider.value,
            manifest_path=MANIFEST_PATH,
            reference_registry_path=None,
            fs_write_plan_path=FS_PLAN_PATH,
            user_confirmed=True,
            allow_single_task_only=True,
            dry_run_id=_summary()["dry_run_run_id"],
            notes="H1 readiness check",
        ),
        [task],
        providers,
        policy,
    )
    assert decision.allowed is False
    assert "approve fs_write_plan" in decision.required_actions
    assert "stage media before live-run" in decision.required_actions
    assert "dreamina_cli live-run disabled by provider config" in decision.required_actions


def test_14_phase_h1_report_and_inputs_do_not_contain_garbled_tokens() -> None:
    text = REPORT_PATH.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text
    assert "PHASE_H1_ACCEPTED" in text
    for path in [SUMMARY_PATH, FS_PLAN_PATH, CHECKLIST_PATH, PROMPT_PATH, SHOT_PATH, MANIFEST_PATH]:
        content = Path(path).read_text(encoding="utf-8")
        assert "????" not in content
        assert "false?True" not in content
