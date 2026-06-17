from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

import pytest

from app.ai_video_pipeline.core.manifest_discovery import discover_manifests
from app.ai_video_pipeline.core.models import ProviderName, RunMode, TaskSpec, TaskType
from app.ai_video_pipeline.execution.job_store import (
    JobRecord,
    add_or_update_job,
    create_job_store,
    get_job,
    list_jobs,
    load_job_store,
    save_job_store,
)
from app.ai_video_pipeline.execution.recorder import read_json
from app.ai_video_pipeline.execution.run_context import create_run_dir
from app.ai_video_pipeline.execution.run_plan import build_run_plan
from app.ai_video_pipeline.execution.resume_state import ResumeDecision, decide_resume_action
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy, PathPolicyError


ROOT = Path(__file__).resolve().parents[1]
TEST_PRODUCTION_ID = "test_production"


def _init_workspace(tmp_path: Path, production_id: str = TEST_PRODUCTION_ID) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    (workspace / "mock_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "live_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / production_id / "manifests").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / production_id / "locked_refs").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    return workspace


def _copy_media(workspace: Path, *names: str) -> dict[str, str]:
    source_dir = ROOT / "tests" / "fixtures" / "media"
    target_dir = workspace / "tests" / "fixtures" / "media"
    target_dir.mkdir(parents=True, exist_ok=True)
    result: dict[str, str] = {}
    for name in names:
        source = source_dir / name
        target = target_dir / name
        target.write_bytes(source.read_bytes())
        result[name] = str(target.relative_to(workspace))
    return result


def _sample_task(
    task_id: str = "TASK-01",
    task_type: TaskType = TaskType.image2image,
    provider: ProviderName = ProviderName.dreamina_cli,
    prompt: str = "phase B test prompt",
    output_name: str = "phase_b_output",
    reference_ids: list[str] | None = None,
    dependency_task_ids: list[str] | None = None,
) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        phase="phaseB",
        task_type=task_type,
        provider=provider,
        model_version="5.0",
        ratio="16:9",
        resolution_type="2k",
        duration=None,
        video_resolution="720p",
        prompt=prompt,
        reference_ids=reference_ids or [],
        output_name=output_name,
        status=None,
        review_status=None,
        notes=None,
        dependency_task_ids=dependency_task_ids or [],
    )


def test_01_discover_manifest_scans_only_workspace(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    (workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "sample.csv").write_text(
        "task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\nx,,text2image,dreamina_cli,,,,,,,o,,,\n"
    )
    policy = PathPolicy(workspace)
    with pytest.raises(PathPolicyError):
        discover_manifests((tmp_path / "outside"), policy)
    manifests = discover_manifests(workspace / "productions" / TEST_PRODUCTION_ID, policy)
    assert manifests and all(path.is_relative_to(workspace) for path in manifests)


def test_02_discover_manifest_files_deterministic_order(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    manifest_root = workspace / "productions" / TEST_PRODUCTION_ID / "manifests"
    manifest_root.mkdir(parents=True, exist_ok=True)
    for name in ["zz.csv", "aa.csv", "mm.csv"]:
        (manifest_root / name).write_text("task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\nx,,,,,,,,,,,", encoding="utf-8")
    discovered = discover_manifests(workspace / "productions" / TEST_PRODUCTION_ID, policy)
    assert [path.name for path in discovered] == ["aa.csv", "mm.csv", "zz.csv"]


def test_08_discover_manifests_scans_only_manifest_root(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    manifest_root = workspace / "productions" / TEST_PRODUCTION_ID / "manifests"
    other_root = workspace / "productions" / "other" / "manifests"
    other_root.mkdir(parents=True, exist_ok=True)
    (manifest_root / "a.csv").write_text("task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\nx,,,,,,,,,,,", encoding="utf-8")
    (other_root / "b.csv").write_text("task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\nx,,,,,,,,,,,", encoding="utf-8")
    discovered = discover_manifests(workspace / "productions" / TEST_PRODUCTION_ID, policy)
    assert len(discovered) == 1
    assert discovered[0].name == "a.csv"


def test_09_discover_manifests_ignores_hidden_files(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    manifest_root = workspace / "productions" / TEST_PRODUCTION_ID / "manifests"
    (manifest_root / "visible.csv").write_text("task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\nx,,,,,,,,,,,", encoding="utf-8")
    (manifest_root / ".hidden.csv").write_text("task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\nx,,,,,,,,,,,", encoding="utf-8")
    discovered = discover_manifests(workspace / "productions" / TEST_PRODUCTION_ID, policy)
    assert [path.name for path in discovered] == ["visible.csv"]


def test_10_manifest_discovery_module_exists() -> None:
    module = ROOT / "app" / "ai_video_pipeline" / "core" / "manifest_discovery.py"
    assert module.exists()


def test_11_no_parent_scan_and_no_legacy_fallback(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    task = _sample_task(task_id="TASK-PROD", reference_ids=["ref_a.png"])
    artifacts = runner.dry_run(task_or_batch_name="run-default", tasks=[task], production_id=TEST_PRODUCTION_ID)
    assert "legacy" not in artifacts.run_root.parts
    assert not (workspace / "productions" / "legacy").exists()


def test_12_legacy_can_be_created_only_by_explicit_id(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    task = _sample_task(task_id="TASK-LEGACY", reference_ids=["ref_a.png"])
    runner.dry_run(tasks=[task], production_id="legacy", task_or_batch_name="run-legacy",)
    assert (workspace / "productions" / "legacy").exists()


def test_03_run_plan_preserves_dependency_order(tmp_path: Path) -> None:
    tasks = [
        _sample_task(task_id="TASK-2", dependency_task_ids=["TASK-1"]),
        _sample_task(task_id="TASK-1"),
    ]
    plan = build_run_plan(tasks)
    assert plan.ordered_task_ids == ["TASK-1", "TASK-2"]


def test_04_run_plan_serializes_to_json(tmp_path: Path) -> None:
    tasks = [_sample_task(task_id="TASK-A"), _sample_task(task_id="TASK-B")]
    plan = build_run_plan(tasks)
    payload = json.loads(plan.to_json())
    assert payload["items"][0]["task_id"] == "TASK-A"
    assert payload["items"][1]["task_id"] == "TASK-B"


def test_05_run_context_is_created_inside_workspace(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    run_context = create_run_dir(workspace, TEST_PRODUCTION_ID, RunMode.dry_run, "RUN-X")
    assert run_context.run_root.is_relative_to(workspace)
    assert run_context.run_root.match(f"productions/{TEST_PRODUCTION_ID}/runs/dry_run/*")


def test_06_run_context_contains_expected_files_and_dirs(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    run_context = create_run_dir(workspace, TEST_PRODUCTION_ID, RunMode.dry_run, "RUN-Y")
    expected_files = [
        run_context.run_manifest_snapshot_csv,
        run_context.run_plan_json,
        run_context.provider_requests_jsonl,
        run_context.provider_responses_jsonl,
        run_context.submitted_tasks_csv,
        run_context.querying_tasks_csv,
        run_context.completed_tasks_csv,
        run_context.failed_tasks_csv,
        run_context.downloaded_files_csv,
        run_context.execution_log_txt,
        run_context.job_store_json,
        run_context.command_preview_csv,
        run_context.compatibility_submitted_csv,
        run_context.compatibility_completed_csv,
        run_context.compatibility_downloaded_csv,
    ]
    for path in expected_files:
        assert path.exists()
    for directory in [run_context.input_media_dir, run_context.downloads_dir, run_context.output_dir, run_context.mock_outputs_dir, run_context.reports_dir]:
        assert directory.exists()


def test_07_dry_run_writes_provider_requests(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.dry_run(
        [_sample_task(task_id="TASK-I2I", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-I2I",
    )
    assert artifacts.provider_requests_jsonl.exists()
    assert artifacts.command_preview_csv.exists()


def test_08_dry_run_stage_and_snapshot_manifest_and_run_plan(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.dry_run(
        [_sample_task(task_id="TASK-I2I", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-I2I",
    )
    assert artifacts.run_manifest_snapshot_csv.exists()
    with artifacts.run_manifest_snapshot_csv.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert rows and rows[0]["task_id"] == "TASK-I2I"
    run_plan = read_json(artifacts.run_plan_json, runner.path_policy)
    assert run_plan["items"][0]["task_id"] == "TASK-I2I"


def test_09_dry_run_writes_job_store(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.dry_run(
        [_sample_task(task_id="TASK-I2I", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-I2I",
    )
    store = load_job_store(artifacts.job_store_json, policy=runner.path_policy)
    assert len(store.jobs) == 1
    assert store.jobs[0].status == "dry_run_completed"
    assert store.mode == "dry_run"


def test_10_mock_run_writes_mock_outputs(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.mock_run(
        [_sample_task(task_id="TASK-MOCK", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-MOCK",
    )
    response_lines = [json.loads(line) for line in artifacts.provider_responses_jsonl.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert response_lines
    output_path = Path(response_lines[0]["output_path"])
    assert output_path.parent == artifacts.run_root / "mock_outputs"
    assert output_path.exists()


def test_11_mock_run_does_not_write_locked_refs(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    locked_dir = workspace / "productions" / TEST_PRODUCTION_ID / "locked_refs"
    existing = set(locked_dir.glob("*"))
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    runner.mock_run(
        [_sample_task(task_id="TASK-MOCK", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-MOCK",
    )
    assert set(locked_dir.glob("*")) == existing


def test_12_mock_run_updates_job_store(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.mock_run(
        [_sample_task(task_id="TASK-MOCK", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-MOCK",
    )
    store = load_job_store(artifacts.job_store_json, policy=runner.path_policy)
    assert all(job.status == "mock_completed" for job in store.jobs)
    assert any(job.provider_task_id for job in store.jobs)
    assert any(job.submit_id for job in store.jobs)


def test_13_resume_decision_completed_skip_when_provider_task_id_exists() -> None:
    job_decision = decide_resume_action(
        JobRecord(
            task_id="TASK-EX",
            status="mock_completed",
            provider="dreamina_cli",
            provider_task_id="provider-id",
            submit_id="submit-id",
            output_name="out",
        )
    )
    assert job_decision == ResumeDecision.completed_skip


def test_14_resume_decision_skips_completed_jobs() -> None:
    assert decide_resume_action(
        JobRecord(
            task_id="TASK-EX",
            status="dry_run_completed",
            provider="dreamina_cli",
            provider_task_id="provider-id",
        )
    ) == ResumeDecision.completed_skip


def test_15_resume_decision_failed_requires_user_action() -> None:
    decision = decide_resume_action(
        JobRecord(
            task_id="TASK-EX",
            status="failed",
            provider="dreamina_cli",
            provider_task_id="",
        )
    )
    assert decision == ResumeDecision.failed_requires_user_decision


def test_16_live_run_remains_disabled(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False
    with pytest.raises(RuntimeError):
        runner.execute(RunMode.live, tasks=[_sample_task(task_id="TASK-LIVE")], task_or_batch_name="RUN-LIVE")


def test_17_no_external_paths_written_in_artifacts(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.dry_run(
        [_sample_task(task_id="TASK-I2I", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-I2I",
    )
    for path in [
        artifacts.run_manifest_snapshot_csv,
        artifacts.run_plan_json,
        artifacts.provider_requests_jsonl,
        artifacts.command_preview_csv,
        artifacts.job_store_json,
        artifacts.submitted_tasks_csv,
        artifacts.querying_tasks_csv,
        artifacts.completed_tasks_csv,
        artifacts.failed_tasks_csv,
        artifacts.downloaded_files_csv,
        artifacts.execution_log_txt,
    ]:
        assert path.is_relative_to(workspace)


def test_18_manifest_discovery_handles_real_workspace_path(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    production = workspace / "productions" / TEST_PRODUCTION_ID
    shutil.copy2(ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "sample_phase_b_manifest.csv", production / "manifests" / "sample_phase_b_manifest.csv")
    refs = _copy_media(workspace, "ref_a.png", "ref_b.png", "scene.png", "keyframe.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.dry_run(production_id=TEST_PRODUCTION_ID, task_or_batch_name="PROD-RUN")
    plan = read_json(artifacts.run_plan_json, runner.path_policy)
    assert plan["items"][0]["task_id"] == "PHASEB-I2I"
    assert plan["items"][1]["task_id"] == "PHASEB-M2V"


def test_19_phase_b_report_is_ascii_safe(tmp_path: Path) -> None:
    report = ROOT / "reports" / "PHASE_B_RUN_STATE_REPORT.md"
    text = report.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text


def test_20_no_dreamina_command_execution_in_dry_or_mock_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    task = _sample_task(task_id="TASK-I2I", reference_ids=["ref_a.png"])
    calls: list[str] = []
    monkeypatch.setattr("subprocess.run", lambda *args, **kwargs: calls.append(str(args)))
    runner.dry_run([task], production_id=TEST_PRODUCTION_ID, task_or_batch_name="RUN-I2I")
    runner.mock_run([task], production_id=TEST_PRODUCTION_ID, task_or_batch_name="RUN-I2I")
    assert calls == []


def test_21_dry_run_rejects_missing_production_id(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    with pytest.raises(ValueError, match="production_id is required"):
        runner.dry_run(
            [_sample_task(task_id="TASK-MISSING", reference_ids=["ref_a.png"])],
            task_or_batch_name="RUN-MISSING",
        )


def test_22_run_directory_is_not_under_legacy(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    refs = _copy_media(workspace, "ref_a.png")
    runner = PipelineRunner(workspace, reference_registry=refs)
    artifacts = runner.dry_run(
        [_sample_task(task_id="TASK-I2I", reference_ids=["ref_a.png"])],
        production_id=TEST_PRODUCTION_ID,
        task_or_batch_name="RUN-I2I",
    )
    assert "legacy" not in artifacts.run_root.parts


def test_23_job_store_api_roundtrip_and_updates(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    store = create_job_store("run-test", "prod-test", "dry_run")
    add_or_update_job(store, "TASK-1", status="planned", provider="dreamina_cli", output_name="shot1")
    add_or_update_job(store, "TASK-1", status="mock_completed", provider_task_id="pid-1", submit_id="sid-1")
    stored_job = get_job(store, "TASK-1")
    assert stored_job is not None
    assert stored_job.status == "mock_completed"
    assert stored_job.provider_task_id == "pid-1"
    assert get_job(store, "TASK-2") is None
    assert [job.task_id for job in list_jobs(store)] == ["TASK-1"]

    policy = PipelineRunner(workspace).path_policy
    store_path = workspace / "job_store_roundtrip.json"
    save_job_store(store_path, store, policy)
    loaded = load_job_store(store_path, policy)
    assert loaded.run_id == "run-test"
    assert loaded.production_id == "prod-test"
    assert loaded.mode == "dry_run"


def test_24_gap_closure_report_is_ascii_safe() -> None:
    report = ROOT / "reports" / "PHASE_B1_1_GAP_CLOSURE_REPORT.md"
    text = report.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text
    assert "PHASE_B_ACCEPTED" in text
