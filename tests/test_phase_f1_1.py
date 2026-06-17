from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import ProviderName, RunMode, TaskSpec, TaskType
from app.ai_video_pipeline.execution.live_gate import LiveRunRequest, validate_live_run_request
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy

ROOT = Path(__file__).resolve().parents[1]
TEST_PRODUCTION_ID = "test_production"


def _workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / TEST_PRODUCTION_ID / "manifests").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    return workspace


def _task(task_id: str = "FAKE-ISO", provider: ProviderName = ProviderName.fake_live_provider) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        phase="phaseF1_1",
        task_type=TaskType.text2image,
        provider=provider,
        model_version="fake-model",
        ratio="16:9",
        resolution_type="2k",
        prompt="fake isolation prompt",
        reference_ids=[],
        output_name=f"{task_id}_output",
    )


def _request(workspace: Path, *, provider: ProviderName = ProviderName.fake_live_provider, confirmed: bool = True, fs_plan: Path | None = None) -> LiveRunRequest:
    return LiveRunRequest(
        production_id=TEST_PRODUCTION_ID,
        task_id="FAKE-ISO",
        run_mode=RunMode.live,
        provider=provider.value,
        manifest_path=None,
        reference_registry_path=None,
        fs_write_plan_path=fs_plan,
        user_confirmed=confirmed,
        allow_single_task_only=True,
        dry_run_id="dry-ok",
        notes="phase f1.1 isolation test",
    )


def _fs_plan(workspace: Path, *, external: bool = False) -> Path:
    path = workspace / "productions" / TEST_PRODUCTION_ID / "runs" / "fs_write_plan.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    planned = workspace.parent / "outside.txt" if external else workspace / "productions" / TEST_PRODUCTION_ID / "runs" / "live" / "planned.txt"
    path.write_text(json.dumps({"approved": True, "planned_files": [str(planned)]}), encoding="utf-8")
    return path


def _provider_config(*, test_context: bool = True) -> dict:
    return {
        "providers": {
            "fake_live_provider": {
                "enabled": True,
                "mode": "fake_live",
                "allow_live_run": True,
                "test_context": test_context,
            }
        }
    }


def test_01_fake_provider_allowed_in_tests_fixtures_only() -> None:
    tasks = parse_manifest_csv(ROOT / "tests" / "fixtures" / "live_fake" / "fake_live_manifest.csv")
    assert tasks[0].provider == ProviderName.fake_live_provider


def test_02_fake_provider_rejected_in_production_manifest(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    manifest = workspace / "productions" / TEST_PRODUCTION_ID / "manifests" / "fake.csv"
    manifest.write_text(
        "task_id,phase,task_type,provider,model_version,ratio,resolution_type,duration,video_resolution,prompt,reference_ids,output_name,status,review_status,notes\n"
        "FAKE,phaseF1_1,text2image,fake_live_provider,fake-model,16:9,2k,,,prompt,,out,,,\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="fake_live_provider is not allowed in production manifests"):
        parse_manifest_csv(manifest)


def test_03_fake_provider_cannot_be_enabled_in_production_config() -> None:
    config = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    fake_entry = config.get("providers", {}).get("fake_live_provider")
    assert fake_entry is None or fake_entry == {"enabled": False, "mode": "test_only", "allow_live_run": False}
    assert config["providers"]["dreamina_cli"]["allow_live_run"] is False
    for name, entry in config["providers"].items():
        if name != "dreamina_cli":
            assert entry.get("enabled", False) is False


def test_04_fake_provider_live_gate_requires_test_context(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_fs_plan(workspace)), [_task()], _provider_config(test_context=True), PathPolicy(workspace))
    assert decision.allowed is True


def test_05_fake_provider_live_gate_denied_without_test_context(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_fs_plan(workspace)), [_task()], _provider_config(test_context=False), PathPolicy(workspace))
    assert decision.allowed is False
    assert "enable explicit fake provider test context" in decision.required_actions


def test_06_dreamina_cli_live_run_remains_denied(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    config = json.loads((workspace / "configs" / "providers.json").read_text(encoding="utf-8"))
    decision = validate_live_run_request(
        _request(workspace, provider=ProviderName.dreamina_cli, fs_plan=_fs_plan(workspace)),
        [_task(provider=ProviderName.dreamina_cli)],
        config,
        PathPolicy(workspace),
    )
    assert decision.allowed is False
    assert "dreamina_cli live-run disabled by provider config" in decision.required_actions


def test_07_no_provider_can_live_run_without_user_confirmation(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, confirmed=False, fs_plan=_fs_plan(workspace)), [_task()], _provider_config(), PathPolicy(workspace))
    assert "collect explicit user confirmation" in decision.required_actions


def test_08_no_provider_can_live_run_multiple_tasks(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_fs_plan(workspace)), [_task(), _task("FAKE-ISO-2")], _provider_config(), PathPolicy(workspace))
    assert "provide exactly one task" in decision.required_actions


def test_09_no_external_path_write(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    decision = validate_live_run_request(_request(workspace, fs_plan=_fs_plan(workspace, external=True)), [_task()], _provider_config(), PathPolicy(workspace))
    assert "keep planned output paths inside workspace" in decision.required_actions


def test_10_no_dreamina_subprocess_call(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    workspace = _workspace(tmp_path)
    calls: list[tuple] = []
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: calls.append((args, kwargs)))
    runner = PipelineRunner(workspace)
    with pytest.raises(RuntimeError):
        runner.live_run([_task(provider=ProviderName.dreamina_cli)], production_id=TEST_PRODUCTION_ID, fs_write_plan_path=_fs_plan(workspace), user_confirmed=True, dry_run_id="dry-ok")
    assert calls == []


def test_11_reports_do_not_contain_question_mark_artifact() -> None:
    report = (ROOT / "reports" / "PHASE_F1_1_FAKE_PROVIDER_ISOLATION_REPORT.md").read_text(encoding="utf-8")
    assert "????" not in report


def test_12_reports_do_not_contain_false_true_artifact() -> None:
    report = (ROOT / "reports" / "PHASE_F1_1_FAKE_PROVIDER_ISOLATION_REPORT.md").read_text(encoding="utf-8")
    assert "false?True" not in report
