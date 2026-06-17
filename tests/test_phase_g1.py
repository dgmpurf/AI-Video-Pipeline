from __future__ import annotations

import csv
import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import TaskType
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "A-CH-A-SUBJECT-001"
MANIFEST = ROOT / "productions" / PRODUCTION_ID / "manifests" / "production_text2image_A-CH-A-SUBJECT-001.csv"
PROMPT_RECORD = ROOT / "productions" / PRODUCTION_ID / "prompts" / "production_character_subject_prompt_A-CH-A-SUBJECT-001.json"
FS_PLAN = ROOT / "reports" / "A-CH-A-SUBJECT-001_fs_write_plan.json"
CHECKLIST = ROOT / "reports" / "A-CH-A-SUBJECT-001_LIVE_APPROVAL_CHECKLIST.json"
REPORT = ROOT / "reports" / "PHASE_G1_CHARACTER_SUBJECT_READINESS_REPORT.md"


def _task() -> tuple:
    tasks = parse_manifest_csv(MANIFEST)
    assert len(tasks) == 1
    return tasks[0]


def _dry_run_dir() -> Path:
    runs_root = ROOT / "productions" / PRODUCTION_ID / "runs" / "dry_run"
    candidates = sorted([item for item in runs_root.iterdir() if item.is_dir() and TASK_ID in item.name])
    if not candidates:
        raise RuntimeError("no G1 dry-run directory found")
    return candidates[-1]


def _provider_requests() -> list[dict]:
    provider_requests_path = _dry_run_dir() / "provider_requests.jsonl"
    return [json.loads(line) for line in provider_requests_path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _argv() -> list[str]:
    payload = _provider_requests()
    assert payload
    return list(payload[0]["command_argv"])


def _command_preview() -> str:
    command_preview_path = _dry_run_dir() / "command_preview.csv"
    with command_preview_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return ""
    return rows[0]["command"]


def test_01_candidate_manifest_has_exactly_one_task() -> None:
    assert len(parse_manifest_csv(MANIFEST)) == 1


def test_02_task_id_is_expected_character_subject_task() -> None:
    assert _task().task_id == TASK_ID


def test_03_task_type_is_text2image() -> None:
    assert _task().task_type == TaskType.text2image


def test_04_dry_run_argv_uses_text2image() -> None:
    assert _argv()[1] == "text2image"


def test_05_dry_run_argv_includes_prompt() -> None:
    assert "--prompt" in _argv()


def test_06_dry_run_argv_includes_model_version_5() -> None:
    argv = _argv()
    assert argv[argv.index("--model_version") + 1] == "5.0"


def test_07_dry_run_argv_includes_ratio_9_16() -> None:
    argv = _argv()
    assert argv[argv.index("--ratio") + 1] == "9:16"


def test_08_dry_run_argv_includes_resolution_type_2k() -> None:
    argv = _argv()
    assert argv[argv.index("--resolution_type") + 1] == "2k"


def test_09_dry_run_argv_does_not_include_output_name_or_output_dir() -> None:
    argv = _argv()
    joined = " ".join(argv)
    assert "--output_name" not in joined
    assert "output_dir" not in joined


def test_10_dry_run_argv_does_not_include_submit_query_or_download_tokens() -> None:
    joined = " ".join(_argv())
    assert "query_result" not in joined
    assert "submit_id" not in joined
    assert "download_dir" not in joined


def test_11_dry_run_argv_does_not_include_image_reference_flags() -> None:
    argv = _argv()
    assert "--image" not in argv
    assert "--images" not in argv
    assert "--refs" not in argv
    assert "--ref_strength" not in argv


def test_12_approval_checklist_has_user_approval_flags_false() -> None:
    payload = json.loads(CHECKLIST.read_text(encoding="utf-8"))
    assert payload["user_approved_live_run"] is False
    assert payload["provider_live_run_enabled"] is False
    assert payload["allow_batch"] is False
    assert payload["allow_parallel"] is False
    assert payload["allow_auto_continue"] is False
    assert payload["allow_retry"] is False


def test_13_fs_write_plan_executed_values_are_all_false() -> None:
    payload = json.loads(FS_PLAN.read_text(encoding="utf-8"))
    assert payload["approved"] is False
    assert all(item["executed"] is False for item in payload["planned_operations"])


def test_14_providers_json_remains_allow_live_run_false() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert payload["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_15_no_submit_query_download_happened_in_g1_dry_run() -> None:
    requests = _provider_requests()
    assert len(requests) == 1
    assert requests[0]["status"] == "prepared"
    assert "query_result" not in _command_preview()
    assert "download_dir" not in _command_preview()
    assert "submit" not in _command_preview()


def test_16_g1_prompt_record_exists() -> None:
    payload = json.loads(PROMPT_RECORD.read_text(encoding="utf-8"))
    assert payload["prompt_id"] == TASK_ID


def test_17_run_artifacts_are_inside_workspace() -> None:
    run_dir = _dry_run_dir()
    assert run_dir.is_relative_to(ROOT)
    assert (run_dir / "command_preview.csv").is_relative_to(ROOT)
    assert (run_dir / "provider_requests.jsonl").is_relative_to(ROOT)
    assert (run_dir / "job_store.json").is_relative_to(ROOT)


def test_18_reports_do_not_contain_question_mark_artifact() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert "????" not in text


def test_19_reports_do_not_contain_false_true_artifact() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert "false?True" not in text


def test_20_default_live_gate_denied_without_user_confirmation_or_dry_run() -> None:
    task = _task()
    policy = PathPolicy(ROOT)
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    decision = validate_live_run_request(
        LiveRunRequest(
            production_id=PRODUCTION_ID,
            task_id=TASK_ID,
            run_mode="live",
            provider=task.provider.value,
            manifest_path=MANIFEST,
            reference_registry_path=None,
            fs_write_plan_path=FS_PLAN,
            user_confirmed=False,
            allow_single_task_only=True,
            dry_run_id="",
            notes="test",
        ),
        [task],
        providers,
        policy,
    )
    assert decision.allowed is False
    assert "collect explicit user confirmation" in decision.required_actions
    assert "complete dry-run first" in decision.required_actions
    assert "approve fs_write_plan" in decision.required_actions
