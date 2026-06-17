from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "A-CH-B-SUBJECT-001"
SUBMIT_ID = "b381e6d4-c559-4689-a09c-03289ac63319"
RUN_DIR = ROOT / "productions" / PRODUCTION_ID / "runs" / "live" / "20260614_055254_A-CH-B-SUBJECT-001"
REPORT = ROOT / "reports" / "PHASE_G4_1_EXISTING_SUBMIT_QUERY_REPORT.md"
OUTPUT = RUN_DIR / "output" / "A-CH-B-SUBJECT-001_shuangji_full_body_subject.png"


def test_01_g4_1_report_has_existing_submit_id_only() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert TASK_ID in text
    assert SUBMIT_ID in text
    assert "PHASE_G4_1_SUCCESS_DOWNLOADED" in text


def test_02_raw_query_response_saved_under_existing_run_dir() -> None:
    path = RUN_DIR / "raw_responses" / "query_response_g4_1.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["argv"] == ["C:/Users/msjpurf/bin/dreamina.exe", "query_result", "--submit_id", SUBMIT_ID]
    assert payload["returncode"] == 0


def test_03_downloaded_output_exists_and_is_inside_workspace() -> None:
    assert OUTPUT.exists()
    assert OUTPUT.stat().st_size > 10 * 1024
    assert OUTPUT.resolve().is_relative_to(ROOT)


def test_04_downloaded_files_csv_records_renamed_output() -> None:
    text = (RUN_DIR / "downloaded_files.csv").read_text(encoding="utf-8")
    assert SUBMIT_ID in text
    assert "A-CH-B-SUBJECT-001_shuangji_full_body_subject.png" in text
    assert "f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a" in text


def test_05_job_store_is_completed_for_existing_submit() -> None:
    payload = json.loads((RUN_DIR / "job_store.json").read_text(encoding="utf-8"))
    job = payload["jobs"][0]
    assert job["task_id"] == TASK_ID
    assert job["status"] == "completed"
    assert job["submit_id"] == SUBMIT_ID
    assert job["last_event"] == "g4_1_success_downloaded"


def test_06_execution_log_records_no_retry() -> None:
    text = (RUN_DIR / "execution_log.txt").read_text(encoding="utf-8")
    assert "phase=G4.1" in text
    assert "status=success" in text
    assert "retry=false" in text


def test_07_providers_json_remains_allow_live_run_false() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert payload["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_08_report_has_no_question_mark_artifact() -> None:
    assert "????" not in REPORT.read_text(encoding="utf-8")


def test_09_report_has_no_false_true_artifact() -> None:
    assert "false?True" not in REPORT.read_text(encoding="utf-8")
