from __future__ import annotations

import json
import re
from pathlib import Path

from app.ai_video_pipeline.core.models import RunMode
from app.ai_video_pipeline.execution.run_context import (
    create_run_dir,
    make_run_id,
    make_safe_run_label,
    strip_existing_timestamp_prefix,
)
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "reports" / "dreamina_preflight_text2image_001_readiness_summary.json"
F3_REPORT = ROOT / "reports" / "PHASE_F3_DREAMINA_SINGLE_TASK_READINESS_REPORT.md"
F3_1_REPORT = ROOT / "reports" / "PHASE_F3_1_SUBMIT_ARGV_PURITY_REPORT.md"
F3_2_REPORT = ROOT / "reports" / "PHASE_F3_2_RUN_ID_NAMING_REPORT.md"


def _timestamp_count(value: str) -> int:
    return len(re.findall(r"\d{8}_\d{6}", value))


def test_01_run_dir_basename_contains_exactly_one_timestamp(tmp_path: Path) -> None:
    workspace = tmp_path / "ws"
    context = create_run_dir(
        workspace,
        "prod",
        RunMode.dry_run,
        "20260613_133659_20260613_213659_batch",
        policy=PathPolicy(workspace),
    )
    assert _timestamp_count(context.run_root.name) == 1


def test_02_create_run_dir_strips_existing_timestamp_prefix_from_label(tmp_path: Path) -> None:
    workspace = tmp_path / "ws"
    context = create_run_dir(
        workspace,
        "prod",
        RunMode.dry_run,
        "ignored",
        run_id="20260613_133659_20260613_213659_dreamina_preflight_text2image_001",
        policy=PathPolicy(workspace),
    )
    assert _timestamp_count(context.run_dir_name) == 1
    assert context.run_dir_name.endswith("_dreamina_preflight_text2image_001")


def test_03_run_id_and_run_dir_basename_match(tmp_path: Path) -> None:
    workspace = tmp_path / "ws"
    context = create_run_dir(workspace, "prod", RunMode.live, "DREAMINA-PREFLIGHT-TEXT2IMAGE-001", policy=PathPolicy(workspace))
    assert context.run_dir_name == context.run_root.name


def test_04_helper_functions_normalize_timestamped_labels() -> None:
    assert strip_existing_timestamp_prefix("20260613_133659_20260613_213659_label") == "label"
    assert make_safe_run_label("20260613_213659_a label") == "a_label"
    assert make_run_id("20260613_213659", "20260613_133659_label") == "20260613_213659_label"


def test_05_f3_dry_run_run_dir_does_not_contain_double_timestamp() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    run_dir = Path(summary["dry_run_run_dir"])
    assert _timestamp_count(run_dir.name) == 1
    assert summary["dry_run_run_id"] == run_dir.name


def test_06_output_name_is_not_in_dreamina_submit_argv() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert "--output_name" not in summary["dry_run_argv"]


def test_07_live_run_remains_disabled() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False


def test_08_no_dreamina_submit_query_or_download_happened() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert summary["submit_query_download_happened"] is False
    assert summary["dreamina_command_executed"] is False
    assert "query_result" not in summary["dry_run_argv"]


def test_09_reports_do_not_contain_question_mark_artifact() -> None:
    for report in [F3_REPORT, F3_1_REPORT, F3_2_REPORT]:
        assert "????" not in report.read_text(encoding="utf-8")


def test_10_reports_do_not_contain_false_true_artifact() -> None:
    for report in [F3_REPORT, F3_1_REPORT, F3_2_REPORT]:
        assert "false?True" not in report.read_text(encoding="utf-8")
