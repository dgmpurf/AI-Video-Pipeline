from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import RunMode
from app.ai_video_pipeline.execution.dreamina_g2_live import (
    CharacterSubjectOneShotAuthorization,
    CommandResult,
    build_character_subject_submit_argv,
    execute_g2_live_run,
)
from app.ai_video_pipeline.execution.runner import PipelineRunner

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "PHASE_G2_FENSHOU_SUBJECT_TEXT2IMAGE_LIVE_RUN_REPORT.md"
MANIFEST = ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "production_text2image_A-CH-A-SUBJECT-001.csv"
PROMPT_RECORD = ROOT / "productions" / "chi_yan_tian_qiong" / "prompts" / "production_character_subject_prompt_A-CH-A-SUBJECT-001.json"


def _workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / "chi_yan_tian_qiong" / "manifests").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / "chi_yan_tian_qiong" / "prompts").mkdir(parents=True, exist_ok=True)
    for item in ["providers.json", "runtime_defaults.json", "path_policy.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    shutil.copy2(MANIFEST, workspace / "productions" / "chi_yan_tian_qiong" / "manifests" / MANIFEST.name)
    shutil.copy2(PROMPT_RECORD, workspace / "productions" / "chi_yan_tian_qiong" / "prompts" / PROMPT_RECORD.name)
    fs_plan = json.loads((ROOT / "reports" / "A-CH-A-SUBJECT-001_fs_write_plan.json").read_text(encoding="utf-8"))
    future_live_root = workspace / "productions" / "chi_yan_tian_qiong" / "runs" / "live" / "FUTURE_RUN_ID"
    fs_plan["workspace_root"] = str(workspace)
    fs_plan["planned_files"] = [
        str(future_live_root / "submitted_tasks.csv"),
        str(future_live_root / "provider_requests.jsonl"),
        str(future_live_root / "provider_responses.jsonl"),
        str(future_live_root / "job_store.json"),
        str(future_live_root / "execution_log.txt"),
        str(future_live_root / "downloads"),
        str(future_live_root / "output"),
        str(future_live_root / "raw_responses"),
        str(future_live_root / "reports"),
    ]
    (workspace / "reports" / "A-CH-A-SUBJECT-001_fs_write_plan.json").write_text(json.dumps(fs_plan, ensure_ascii=True, indent=2), encoding="utf-8")
    shutil.copy2(ROOT / "reports" / "A-CH-A-SUBJECT-001_LIVE_APPROVAL_CHECKLIST.json", workspace / "reports" / "A-CH-A-SUBJECT-001_LIVE_APPROVAL_CHECKLIST.json")
    return workspace


def _task():
    return parse_manifest_csv(MANIFEST)[0]


def _write_test_image(path: Path) -> None:
    image = Image.effect_noise((256, 256), 64).convert("RGB")
    image.save(path, "PNG")


def test_01_one_shot_authorization_applies_only_to_exact_task_id() -> None:
    auth = CharacterSubjectOneShotAuthorization.required()
    assert auth.allows(_task(), 1) is True
    other = _task()
    other.task_id = "OTHER"
    assert auth.allows(other, 1) is False


def test_02_authorization_is_consumed_after_submit() -> None:
    auth = CharacterSubjectOneShotAuthorization.required()
    auth.consume()
    assert auth.consumed is True
    assert auth.allows(_task(), 1) is False


def test_03_character_subject_live_argv_does_not_include_output_name_or_output_dir() -> None:
    argv = build_character_subject_submit_argv(_task(), "dreamina.exe")
    assert "--output_name" not in argv
    assert "output_dir" not in " ".join(argv)


def test_04_query_result_is_not_in_submit_argv() -> None:
    assert "query_result" not in build_character_subject_submit_argv(_task(), "dreamina.exe")


def test_05_download_dir_is_only_used_in_download_stage(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    calls: list[list[str]] = []

    def runner(argv):
        calls.append(list(argv))
        if argv[1] == "text2image":
            return CommandResult(list(argv), 0, '{"submit_id":"G2SUB123"}', "")
        if "--download_dir" not in argv:
            return CommandResult(list(argv), 0, '{"status":"success"}', "")
        download_dir = Path(argv[argv.index("--download_dir") + 1])
        _write_test_image(download_dir / "raw.png")
        return CommandResult(list(argv), 0, '{"status":"downloaded"}', "")

    result = execute_g2_live_run(workspace, runner=runner)
    assert result.verdict == "PHASE_G2_SUCCESS_DOWNLOADED"
    assert "--download_dir" not in calls[0]
    assert "--download_dir" not in calls[1]
    assert "--download_dir" in calls[2]


def test_06_submit_id_persistence_happens_before_query(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    evidence: dict[str, bool] = {}

    def runner(argv):
        if argv[1] == "text2image":
            return CommandResult(list(argv), 0, '{"submit_id":"G2SUB123"}', "")
        run_dirs = sorted((workspace / "productions" / "chi_yan_tian_qiong" / "runs" / "live").iterdir())
        current = run_dirs[-1]
        evidence["submitted_before_query"] = "G2SUB123" in (current / "job_store.json").read_text(encoding="utf-8")
        return CommandResult(list(argv), 0, '{"status":"querying"}', "")

    execute_g2_live_run(workspace, runner=runner)
    assert evidence["submitted_before_query"] is True


def test_07_querying_state_resumes_query_only(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)

    def runner(argv):
        if argv[1] == "text2image":
            return CommandResult(list(argv), 0, '{"submit_id":"G2SUB123"}', "")
        return CommandResult(list(argv), 0, '{"status":"querying"}', "")

    result = execute_g2_live_run(workspace, runner=runner)
    assert result.verdict == "PHASE_G2_SUBMITTED_QUERYING"
    assert result.run_context.querying_tasks_csv.read_text(encoding="utf-8")
    assert not result.run_context.downloaded_files_csv.read_text(encoding="utf-8").strip()


def test_08_success_state_downloads_and_renames_only_inside_workspace(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)

    def runner(argv):
        if argv[1] == "text2image":
            return CommandResult(list(argv), 0, '{"submit_id":"G2SUB123"}', "")
        if "--download_dir" not in argv:
            return CommandResult(list(argv), 0, '{"status":"success"}', "")
        download_dir = Path(argv[argv.index("--download_dir") + 1])
        _write_test_image(download_dir / "raw.png")
        return CommandResult(list(argv), 0, '{"status":"downloaded"}', "")

    result = execute_g2_live_run(workspace, runner=runner)
    assert result.output_path is not None
    assert result.output_path.name == "A-CH-A-SUBJECT-001_fenshou_full_body_subject.png"
    assert result.output_path.is_relative_to(workspace)


def test_09_providers_json_remains_allow_live_run_false() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert payload["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_10_no_batch_parallel_or_retry_allowed() -> None:
    auth = CharacterSubjectOneShotAuthorization.required()
    assert auth.allow_batch is False
    assert auth.allow_parallel is False
    assert auth.allow_retry is False
    assert auth.allow_auto_continue is False
    assert auth.allows(_task(), 2) is False


def test_11_reports_do_not_contain_question_mark_artifact() -> None:
    assert "????" not in REPORT.read_text(encoding="utf-8")


def test_12_reports_do_not_contain_false_true_artifact() -> None:
    assert "false?True" not in REPORT.read_text(encoding="utf-8")


def test_13_live_run_remains_disabled_for_general_runner() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False
