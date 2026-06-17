from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.ai_video_pipeline.core.models import ProviderName, RunMode, TaskSpec, TaskType
from app.ai_video_pipeline.execution.job_store import JobRecord
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.execution.resume_state import ResumeDecision, decide_resume_action, load_job_store
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
TEST_PRODUCTION_ID = "test_production"


def _init_workspace(tmp_path: Path, *, fake_live: bool = False) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    (workspace / "mock_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "live_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / TEST_PRODUCTION_ID / "manifests").mkdir(parents=True, exist_ok=True)
    (workspace / "refs").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    if fake_live:
        config = json.loads((workspace / "configs" / "providers.json").read_text(encoding="utf-8"))
        config["providers"]["fake_live_provider"] = {
            "enabled": True,
            "mode": "fake_live",
            "allow_live_run": True,
            "test_context": True,
            "fake_query_status": "querying",
        }
        (workspace / "configs" / "providers.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    return workspace


def _task(task_id: str = "TASK-F0", refs: list[str] | None = None) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        phase="phaseF0",
        task_type=TaskType.text2image if not refs else TaskType.image2image,
        provider=ProviderName.fake_live_provider,
        model_version="5.0",
        ratio="16:9",
        resolution_type="2k",
        duration=None,
        video_resolution=None,
        prompt="phase F0 gated prompt",
        reference_ids=refs or [],
        output_name=f"{task_id}_output",
    )


def _request(workspace: Path, *, confirmed: bool = True, fs_plan: Path | None = None, dry_run_id: str = "dry-run-ok") -> LiveRunRequest:
    return LiveRunRequest(
        production_id=TEST_PRODUCTION_ID,
        task_id="TASK-F0",
        run_mode=RunMode.live,
        provider=ProviderName.fake_live_provider.value,
        manifest_path=None,
        reference_registry_path=None,
        fs_write_plan_path=fs_plan,
        user_confirmed=confirmed,
        allow_single_task_only=True,
        dry_run_id=dry_run_id,
        notes="test request",
    )


def _approved_plan(workspace: Path, *, approved: bool = True, external: bool = False) -> Path:
    plan = workspace / "productions" / TEST_PRODUCTION_ID / "runs" / "fs_write_plan.json"
    plan.parent.mkdir(parents=True, exist_ok=True)
    planned_file = workspace.parent / "outside.txt" if external else workspace / "productions" / TEST_PRODUCTION_ID / "runs" / "live" / "out.txt"
    plan.write_text(json.dumps({"approved": approved, "planned_files": [str(planned_file)]}), encoding="utf-8")
    return plan


def _provider_config(allow: bool, *, fake: bool = False) -> dict:
    return {
        "providers": {
            "fake_live_provider": {
                "enabled": True,
                "mode": "fake_live" if fake else "cli",
                "allow_live_run": allow,
                "test_context": fake,
            }
        }
    }


def test_01_live_run_denied_when_provider_allow_live_run_false(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task()], _provider_config(False), PathPolicy(workspace))
    assert decision.allowed is False
    assert "enable provider allow_live_run" in decision.required_actions


def test_02_live_run_denied_without_user_confirmation(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, confirmed=False, fs_plan=_approved_plan(workspace)), [_task()], _provider_config(True), PathPolicy(workspace))
    assert "collect explicit user confirmation" in decision.required_actions


def test_03_live_run_denied_for_multiple_tasks(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task(), _task("TASK-F0-B")], _provider_config(True), PathPolicy(workspace))
    assert "provide exactly one task" in decision.required_actions


def test_04_live_run_denied_without_dry_run_proof(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace), dry_run_id=""), [_task()], _provider_config(True), PathPolicy(workspace))
    assert "complete dry-run first" in decision.required_actions


def test_05_live_run_denied_without_fs_write_plan(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace), [_task()], _provider_config(True), PathPolicy(workspace))
    assert "provide fs_write_plan" in decision.required_actions


def test_06_live_run_denied_if_fs_write_plan_not_approved(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace, approved=False)), [_task()], _provider_config(True), PathPolicy(workspace))
    assert "approve fs_write_plan" in decision.required_actions


def test_07_live_run_denied_if_staged_media_missing(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task(refs=["ref-a"])], _provider_config(True), PathPolicy(workspace))
    assert "stage media before live-run" in decision.required_actions


def test_08_live_run_allowed_for_fake_provider_with_all_gates_satisfied(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref-a.txt"
    staged.write_text("dummy", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task(refs=["ref-a"])], _provider_config(True, fake=True), PathPolicy(workspace), staged_media_paths=[staged])
    assert decision.allowed is True


def test_09_fake_submit_writes_submitted_tasks_csv_immediately(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path, fake_live=True)
    artifacts = PipelineRunner(workspace).live_run(
        [_task()],
        production_id=TEST_PRODUCTION_ID,
        fs_write_plan_path=_approved_plan(workspace),
        user_confirmed=True,
        dry_run_id="dry-run-ok",
        stop_after_submit=True,
    )
    assert "submitted" in artifacts.submitted_tasks_csv.read_text(encoding="utf-8")


def test_10_fake_submit_writes_job_store_json_immediately(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path, fake_live=True)
    artifacts = PipelineRunner(workspace).live_run(
        [_task()],
        production_id=TEST_PRODUCTION_ID,
        fs_write_plan_path=_approved_plan(workspace),
        user_confirmed=True,
        dry_run_id="dry-run-ok",
        stop_after_submit=True,
    )
    store = load_job_store(artifacts.job_store_json, PathPolicy(workspace), allow_missing=False)
    assert store.jobs[0].submit_id == "fake-submit-TASK-F0"
    assert decide_resume_action(store.jobs[0]) == ResumeDecision.submitted_query_only


def test_11_interrupted_after_submit_resume_decision_is_submitted_query_only() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="submitted", provider_task_id="provider-id", submit_id="submit-id")) == ResumeDecision.submitted_query_only


def test_12_querying_state_resumes_query_only() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="querying", provider_task_id="provider-id", submit_id="submit-id")) == ResumeDecision.querying_query_only


def test_13_success_state_resumes_download_only() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="success", provider_task_id="provider-id", submit_id="submit-id")) == ResumeDecision.success_download_only


def test_14_completed_state_skips() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="completed", provider_task_id="provider-id")) == ResumeDecision.completed_skip


def test_15_failed_state_requires_user_decision() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="failed", provider_task_id="provider-id")) == ResumeDecision.failed_requires_user_decision


def test_16_dreamina_cli_live_run_remains_disabled(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False
    with pytest.raises(RuntimeError, match="live-run denied"):
        runner.live_run(
            [_task()],
            production_id=TEST_PRODUCTION_ID,
            fs_write_plan_path=_approved_plan(workspace),
            user_confirmed=True,
            dry_run_id="dry-run-ok",
            stop_after_submit=True,
        )


def test_17_no_dreamina_subprocess_is_called(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    workspace = _init_workspace(tmp_path, fake_live=True)
    calls: list[tuple] = []
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: calls.append((args, kwargs)))
    PipelineRunner(workspace).live_run(
        [_task()],
        production_id=TEST_PRODUCTION_ID,
        fs_write_plan_path=_approved_plan(workspace),
        user_confirmed=True,
        dry_run_id="dry-run-ok",
        stop_after_submit=True,
    )
    assert calls == []


def test_18_no_external_path_write_is_allowed(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace, external=True)), [_task()], _provider_config(True), PathPolicy(workspace))
    assert "keep planned output paths inside workspace" in decision.required_actions


def test_19_report_does_not_contain_question_mark_artifact() -> None:
    text = (ROOT / "reports" / "PHASE_F0_LIVE_GATE_REPORT.md").read_text(encoding="utf-8")
    assert "????" not in text


def test_20_report_does_not_contain_false_true_artifact() -> None:
    text = (ROOT / "reports" / "PHASE_F0_LIVE_GATE_REPORT.md").read_text(encoding="utf-8")
    assert "false?True" not in text


def test_21_phase_f0_report_does_not_contain_stale_phase_e_labels() -> None:
    text = (ROOT / "reports" / "PHASE_F0_LIVE_GATE_REPORT.md").read_text(encoding="utf-8")
    assert "PHASE_E_ACCEPTED" not in text
    assert "PHASE_E_TASK_COMPILER_REPORT.md" not in text
    assert "PHASE_F0_ACCEPTED" in text


def test_22_phase_f0_1_report_quality_and_live_run_disabled(tmp_path: Path) -> None:
    text = (ROOT / "reports" / "PHASE_F0_1_REPORT_CONSISTENCY_AUDIT.md").read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text
    assert "PHASE_F0_REPORT_CONSISTENCY_ACCEPTED" in text
    assert PipelineRunner(_init_workspace(tmp_path)).can_run_live() is False
