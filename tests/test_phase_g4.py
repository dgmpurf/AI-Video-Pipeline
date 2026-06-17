from __future__ import annotations

import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import RunMode
from app.ai_video_pipeline.execution.runner import PipelineRunner

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "A-CH-B-SUBJECT-001"
MANIFEST = ROOT / "productions" / PRODUCTION_ID / "manifests" / "production_text2image_A-CH-B-SUBJECT-001.csv"
REPORT = ROOT / "reports" / "PHASE_G4_SHUANGJI_SUBJECT_TEXT2IMAGE_LIVE_RUN_REPORT.md"


def _latest_g4_run_dir() -> Path:
    runs_root = ROOT / "productions" / PRODUCTION_ID / "runs" / "live"
    candidates = [item for item in runs_root.iterdir() if item.is_dir() and TASK_ID in item.name]
    assert candidates, "no G4 live run directory found"
    return sorted(candidates)[-1]


def _provider_request() -> dict:
    path = _latest_g4_run_dir() / "provider_requests.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 1
    return rows[0]


def _authorization() -> dict:
    return json.loads((_latest_g4_run_dir() / "reports" / "one_shot_live_authorization.json").read_text(encoding="utf-8"))


def test_01_one_shot_authorization_applies_only_to_exact_task_id() -> None:
    auth = _authorization()
    assert auth["task_id"] == TASK_ID
    assert auth["provider"] == "dreamina_cli"
    assert auth["task_type"] == "text2image"
    assert auth["allow_single_task_only"] is True
    assert auth["allow_batch"] is False


def test_02_authorization_is_consumed_after_submit() -> None:
    assert _authorization()["consumed"] is True


def test_03_shuangji_subject_live_argv_excludes_pipeline_only_fields() -> None:
    argv = _provider_request()["command_argv"]
    joined = " ".join(argv)
    assert "--output_name" not in argv
    assert "output_dir" not in joined
    assert "query_result" not in joined
    assert "submit_id" not in joined


def test_04_download_dir_is_not_used_before_download_stage() -> None:
    argv = _provider_request()["command_argv"]
    query_payload = json.loads((_latest_g4_run_dir() / "raw_responses" / "query_response.json").read_text(encoding="utf-8"))
    assert "download_dir" not in " ".join(argv)
    assert "--download_dir" not in query_payload["argv"]


def test_05_submit_id_persistence_happened_before_query() -> None:
    log = (_latest_g4_run_dir() / "execution_log.txt").read_text(encoding="utf-8")
    assert "submit_persisted_before_query=true" in log
    assert log.index("submit_persisted_before_query=true") < log.index("status=querying")


def test_06_querying_state_stops_without_download() -> None:
    run_dir = _latest_g4_run_dir()
    log = (run_dir / "execution_log.txt").read_text(encoding="utf-8")
    assert (run_dir / "querying_tasks.csv").read_text(encoding="utf-8")
    assert "phase=G4" in log
    assert "status=querying" in log
    assert "download=false" in log


def test_07_providers_json_remains_allow_live_run_false() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert payload["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_08_general_runner_still_denies_live_run() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False


def test_09_no_batch_parallel_retry_or_auto_continue_allowed() -> None:
    auth = _authorization()
    assert auth["allow_batch"] is False
    assert auth["allow_parallel"] is False
    assert auth["allow_retry"] is False
    assert auth["allow_auto_continue"] is False


def test_10_manifest_remains_one_exact_text2image_task() -> None:
    tasks = parse_manifest_csv(MANIFEST)
    assert len(tasks) == 1
    assert tasks[0].task_id == TASK_ID
    assert tasks[0].task_type.value == "text2image"


def test_11_report_does_not_contain_question_mark_artifact() -> None:
    assert "????" not in REPORT.read_text(encoding="utf-8")


def test_12_report_does_not_contain_false_true_artifact() -> None:
    assert "false?True" not in REPORT.read_text(encoding="utf-8")
