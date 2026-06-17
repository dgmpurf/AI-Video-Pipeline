from __future__ import annotations

import csv
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import ProviderName, RunMode, TaskSpec, TaskType
from app.ai_video_pipeline.execution.job_store import JobRecord
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.execution.resume_state import ResumeDecision, decide_resume_action, load_job_store
from app.ai_video_pipeline.execution.runner import PipelineRunner, RunArtifacts
from app.ai_video_pipeline.path_policy import PathPolicy
from app.ai_video_pipeline.providers.fake_live_provider import FakeLiveProvider

ROOT = Path(__file__).resolve().parents[1]
TEST_PRODUCTION_ID = "test_production"


def _init_workspace(tmp_path: Path, *, scenario: str = "submit_then_querying") -> Path:
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
    config = json.loads((workspace / "configs" / "providers.json").read_text(encoding="utf-8"))
    config["providers"]["fake_live_provider"] = {
        "enabled": True,
        "mode": "fake_live",
        "allow_live_run": True,
        "test_context": True,
        "fake_scenario": scenario,
    }
    (workspace / "configs" / "providers.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    return workspace


def _task(refs: list[str] | None = None) -> TaskSpec:
    return TaskSpec(
        task_id="FAKE-LIVE-I2I",
        phase="phaseF1",
        task_type=TaskType.image2image,
        provider=ProviderName.fake_live_provider,
        model_version="fake-model",
        ratio="16:9",
        resolution_type="2k",
        prompt="fake live test prompt",
        reference_ids=refs or ["ref_a", "ref_b", "scene"],
        output_name="FAKE-LIVE-I2I_output",
    )


def _write_refs(workspace: Path) -> dict[str, str]:
    refs: dict[str, str] = {}
    for name in ["ref_a", "ref_b", "scene"]:
        path = workspace / "refs" / f"{name}.txt"
        path.write_text(f"fake fixture {name}", encoding="utf-8")
        refs[name] = str(path.relative_to(workspace))
    return refs


def _approved_plan(workspace: Path, *, approved: bool = True, external: bool = False) -> Path:
    plan = workspace / "productions" / TEST_PRODUCTION_ID / "runs" / "fs_write_plan.json"
    plan.parent.mkdir(parents=True, exist_ok=True)
    planned = workspace.parent / "outside.txt" if external else workspace / "productions" / TEST_PRODUCTION_ID / "runs" / "live" / "planned.txt"
    plan.write_text(json.dumps({"approved": approved, "planned_files": [str(planned)]}), encoding="utf-8")
    return plan


def _request(workspace: Path, *, confirmed: bool = True, dry_run_id: str = "dry-ok", fs_plan: Path | None = None) -> LiveRunRequest:
    return LiveRunRequest(
        production_id=TEST_PRODUCTION_ID,
        task_id="FAKE-LIVE-I2I",
        run_mode=RunMode.live,
        provider=ProviderName.fake_live_provider.value,
        manifest_path=None,
        reference_registry_path=None,
        fs_write_plan_path=fs_plan,
        user_confirmed=confirmed,
        allow_single_task_only=True,
        dry_run_id=dry_run_id,
        notes="phase f1 test",
    )


def _provider_config() -> dict:
    return {
        "providers": {
            "fake_live_provider": {
                "enabled": True,
                "mode": "fake_live",
                "allow_live_run": True,
                "test_context": True,
            }
        }
    }


def _run_fake_live(tmp_path: Path, *, scenario: str = "submit_then_success_download", stop_after_submit: bool = False) -> tuple[Path, RunArtifacts]:
    workspace = _init_workspace(tmp_path, scenario=scenario)
    refs = _write_refs(workspace)
    artifacts = PipelineRunner(workspace, reference_registry=refs).live_run(
        [_task()],
        production_id=TEST_PRODUCTION_ID,
        fs_write_plan_path=_approved_plan(workspace),
        user_confirmed=True,
        dry_run_id="dry-ok",
        stop_after_submit=stop_after_submit,
    )
    return workspace, artifacts


def test_01_fake_live_denied_without_user_confirmation(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, confirmed=False, fs_plan=_approved_plan(workspace)), [_task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[workspace / "staging"])
    assert "collect explicit user confirmation" in decision.required_actions


def test_02_fake_live_denied_with_multiple_tasks(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref.txt"
    staged.write_text("x", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task(), _task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[staged])
    assert "provide exactly one task" in decision.required_actions


def test_03_fake_live_denied_without_dry_run_proof(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref.txt"
    staged.write_text("x", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace, dry_run_id="", fs_plan=_approved_plan(workspace)), [_task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[staged])
    assert "complete dry-run first" in decision.required_actions


def test_04_fake_live_denied_without_fs_write_plan(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref.txt"
    staged.write_text("x", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace), [_task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[staged])
    assert "provide fs_write_plan" in decision.required_actions


def test_05_fake_live_denied_if_fs_write_plan_not_approved(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref.txt"
    staged.write_text("x", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace, approved=False)), [_task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[staged])
    assert "approve fs_write_plan" in decision.required_actions


def test_06_fake_live_denied_if_staged_media_missing(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task()], _provider_config(), PathPolicy(workspace))
    assert "stage media before live-run" in decision.required_actions


def test_07_fake_live_allowed_when_all_gates_pass(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref.txt"
    staged.write_text("x", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace)), [_task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[staged])
    assert decision.allowed is True


def test_08_fake_submit_writes_submitted_tasks_csv_immediately(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path, scenario="submit_interrupted_before_query", stop_after_submit=True)
    assert "submitted" in artifacts.submitted_tasks_csv.read_text(encoding="utf-8")
    assert "fake-submit-FAKE-LIVE-I2I" in artifacts.provider_responses_jsonl.read_text(encoding="utf-8")
    assert "submit_id_persisted_before_query=true" in artifacts.execution_log_txt.read_text(encoding="utf-8")


def test_09_fake_submit_writes_job_store_json_immediately(tmp_path: Path) -> None:
    workspace, artifacts = _run_fake_live(tmp_path, scenario="submit_interrupted_before_query", stop_after_submit=True)
    store = load_job_store(artifacts.job_store_json, PathPolicy(workspace), allow_missing=False)
    assert store.jobs[0].submit_id == "fake-submit-FAKE-LIVE-I2I"


def test_10_fake_interrupted_before_query_resumes_as_submitted_query_only(tmp_path: Path) -> None:
    workspace, artifacts = _run_fake_live(tmp_path, scenario="submit_interrupted_before_query", stop_after_submit=True)
    store = load_job_store(artifacts.job_store_json, PathPolicy(workspace), allow_missing=False)
    assert decide_resume_action(store.jobs[0]) == ResumeDecision.submitted_query_only


def test_11_querying_resumes_as_querying_query_only() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="querying", provider_task_id="id")) == ResumeDecision.querying_query_only


def test_12_success_resumes_as_success_download_only() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="success", provider_task_id="id")) == ResumeDecision.success_download_only


def test_13_downloaded_resumes_as_downloaded_rename_only() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="downloaded", provider_task_id="id")) == ResumeDecision.downloaded_rename_only


def test_14_completed_resumes_as_completed_skip() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="completed", provider_task_id="id")) == ResumeDecision.completed_skip


def test_15_failed_resumes_as_failed_requires_user_decision() -> None:
    assert decide_resume_action(JobRecord(task_id="x", status="failed", provider_task_id="id")) == ResumeDecision.failed_requires_user_decision


def test_16_fake_success_path_writes_completed_tasks_csv(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path)
    assert "completed" in artifacts.completed_tasks_csv.read_text(encoding="utf-8")


def test_17_fake_success_path_writes_downloaded_files_csv(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path)
    assert "downloaded" in artifacts.downloaded_files_csv.read_text(encoding="utf-8")


def test_18_fake_output_is_renamed_to_output_name(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path)
    output = artifacts.run_root / "output" / "FAKE-LIVE-I2I_output.txt"
    assert output.exists()
    assert output.read_text(encoding="utf-8") == "fake live output for FAKE-LIVE-I2I\n"


def test_19_fake_output_stays_inside_workspace(tmp_path: Path) -> None:
    workspace, artifacts = _run_fake_live(tmp_path)
    assert (artifacts.run_root / "output" / "FAKE-LIVE-I2I_output.txt").is_relative_to(workspace)


def test_20_fake_output_does_not_enter_locked_refs(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path)
    output = artifacts.run_root / "output" / "FAKE-LIVE-I2I_output.txt"
    assert "locked_refs" not in output.parts


def test_21_dreamina_cli_live_run_remains_disabled(tmp_path: Path) -> None:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    assert PipelineRunner(workspace).can_run_live() is False


def test_22_no_dreamina_subprocess_is_called(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple] = []
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: calls.append((args, kwargs)))
    _run_fake_live(tmp_path)
    assert calls == []


def test_23_no_external_path_write(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    staged = workspace / "staging" / "ref.txt"
    staged.write_text("x", encoding="utf-8")
    decision = validate_live_run_request(_request(workspace, fs_plan=_approved_plan(workspace, external=True)), [_task()], _provider_config(), PathPolicy(workspace), staged_media_paths=[staged])
    assert "keep planned output paths inside workspace" in decision.required_actions


def test_24_report_does_not_contain_question_mark_artifact() -> None:
    assert "????" not in (ROOT / "reports" / "PHASE_F1_FAKE_LIVE_FULL_LOOP_REPORT.md").read_text(encoding="utf-8")


def test_25_report_does_not_contain_false_true_artifact() -> None:
    assert "false?True" not in (ROOT / "reports" / "PHASE_F1_FAKE_LIVE_FULL_LOOP_REPORT.md").read_text(encoding="utf-8")


def test_26_fake_live_manifest_has_one_fake_provider_task() -> None:
    tasks = parse_manifest_csv(ROOT / "tests" / "fixtures" / "live_fake" / "fake_live_manifest.csv")
    assert len(tasks) == 1
    assert tasks[0].task_id == "FAKE-LIVE-I2I"
    assert tasks[0].provider == ProviderName.fake_live_provider


def test_27_fake_provider_scenarios_are_deterministic() -> None:
    assert FakeLiveProvider(scenario="submit_then_querying").query("id").status == "querying"
    assert FakeLiveProvider(scenario="submit_then_success").query("id").status == "success"
    assert FakeLiveProvider(scenario="submit_then_fail").query("id").status == "fail"


def test_28_fake_live_run_artifacts_exist(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path)
    required_files = [
        artifacts.run_manifest_snapshot_csv,
        artifacts.run_plan_json,
        artifacts.provider_requests_jsonl,
        artifacts.provider_responses_jsonl,
        artifacts.submitted_tasks_csv,
        artifacts.querying_tasks_csv,
        artifacts.completed_tasks_csv,
        artifacts.failed_tasks_csv,
        artifacts.downloaded_files_csv,
        artifacts.execution_log_txt,
        artifacts.job_store_json,
        artifacts.command_preview_csv,
    ]
    for path in required_files:
        assert path.exists()
    for name in ["input_media", "downloads", "output", "reports"]:
        assert (artifacts.run_root / name).is_dir()


def test_29_success_downloaded_not_renamed_scenario_pauses_before_rename(tmp_path: Path) -> None:
    _, artifacts = _run_fake_live(tmp_path, scenario="success_downloaded_not_renamed")
    store_payload = json.loads(artifacts.job_store_json.read_text(encoding="utf-8"))
    assert store_payload["jobs"][0]["status"] == "downloaded"
    assert not (artifacts.run_root / "output" / "FAKE-LIVE-I2I_output.txt").exists()
