from __future__ import annotations

import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import ProviderName, RunMode, TaskSpec, TaskType
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.providers.dreamina_cli import DreaminaCLIProvider

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "productions" / "chi_yan_tian_qiong" / "manifests" / "dreamina_preflight_text2image_001.csv"
SUMMARY = ROOT / "reports" / "dreamina_preflight_text2image_001_readiness_summary.json"
F3_REPORT = ROOT / "reports" / "PHASE_F3_DREAMINA_SINGLE_TASK_READINESS_REPORT.md"
F3_1_REPORT = ROOT / "reports" / "PHASE_F3_1_SUBMIT_ARGV_PURITY_REPORT.md"

INTERNAL_FIELD_NAMES = {
    "output_name",
    "output_dir",
    "local_output_path",
    "download_dir",
    "rename_path",
    "review_status",
    "notes",
    "status",
    "provider_task_id",
    "submit_id",
}


def _task(task_type: TaskType, *, task_id: str = "PURE", refs: list[str] | None = None) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        phase="phaseF3_1",
        task_type=task_type,
        provider=ProviderName.dreamina_cli,
        model_version="5.0" if task_type in {TaskType.text2image, TaskType.image2image} else "seedance2.0fast_vip",
        ratio="16:9",
        resolution_type="2k",
        duration=5,
        video_resolution="720p",
        prompt=f"{task_type.value} prompt",
        reference_ids=refs or [],
        output_name=f"{task_id}_output",
        status="draft",
        notes="pipeline-only note",
    )


def _argv(task_type: TaskType, refs: list[Path] | None = None) -> list[str]:
    return DreaminaCLIProvider("dreamina.exe").build_submit_command(_task(task_type), refs or [])


def _assert_no_internal_fields(argv: list[str]) -> None:
    for field in INTERNAL_FIELD_NAMES:
        assert field not in argv
        assert f"--{field}" not in argv


def test_01_text2image_submit_argv_does_not_contain_output_name() -> None:
    argv = _argv(TaskType.text2image)
    assert "--output_name" not in argv
    assert argv == [
        "dreamina.exe",
        "text2image",
        "--model_version",
        "5.0",
        "--ratio",
        "16:9",
        "--prompt",
        "text2image prompt",
        "--resolution_type",
        "2k",
    ]


def test_02_image2image_submit_argv_does_not_contain_output_name() -> None:
    argv = _argv(TaskType.image2image, [Path("a.png"), Path("b.png")])
    assert "--output_name" not in argv
    assert argv.count("--images") == 2


def test_03_multimodal2video_submit_argv_does_not_contain_output_name() -> None:
    argv = _argv(TaskType.multimodal2video, [Path("a.png"), Path("b.png")])
    assert "--output_name" not in argv
    assert argv.count("--image") == 2


def test_04_image2video_submit_argv_does_not_contain_output_name_or_ratio() -> None:
    argv = _argv(TaskType.image2video, [Path("a.png")])
    assert "--output_name" not in argv
    assert "--ratio" not in argv
    assert argv.count("--image") == 1


def test_05_frames2video_submit_argv_does_not_contain_output_name_or_ratio() -> None:
    argv = _argv(TaskType.frames2video, [Path("first.png"), Path("last.png")])
    assert "--output_name" not in argv
    assert "--ratio" not in argv
    assert "--first" in argv
    assert "--last" in argv


def test_06_no_submit_argv_contains_output_dir() -> None:
    for task_type, refs in [
        (TaskType.text2image, []),
        (TaskType.image2image, [Path("a.png")]),
        (TaskType.multimodal2video, [Path("a.png")]),
        (TaskType.image2video, [Path("a.png")]),
        (TaskType.frames2video, [Path("first.png"), Path("last.png")]),
    ]:
        assert "output_dir" not in _argv(task_type, refs)
        assert "--output_dir" not in _argv(task_type, refs)


def test_07_no_submit_argv_contains_download_dir() -> None:
    for task_type, refs in [
        (TaskType.text2image, []),
        (TaskType.image2image, [Path("a.png")]),
        (TaskType.multimodal2video, [Path("a.png")]),
        (TaskType.image2video, [Path("a.png")]),
        (TaskType.frames2video, [Path("first.png"), Path("last.png")]),
    ]:
        assert "download_dir" not in _argv(task_type, refs)
        assert "--download_dir" not in _argv(task_type, refs)


def test_08_no_submit_argv_contains_local_output_path() -> None:
    for task_type, refs in [
        (TaskType.text2image, []),
        (TaskType.image2image, [Path("a.png")]),
        (TaskType.multimodal2video, [Path("a.png")]),
        (TaskType.image2video, [Path("a.png")]),
        (TaskType.frames2video, [Path("first.png"), Path("last.png")]),
    ]:
        assert "local_output_path" not in _argv(task_type, refs)
        assert "--local_output_path" not in _argv(task_type, refs)


def test_09_no_submit_argv_contains_any_internal_field_name() -> None:
    for task_type, refs in [
        (TaskType.text2image, []),
        (TaskType.image2image, [Path("a.png")]),
        (TaskType.multimodal2video, [Path("a.png")]),
        (TaskType.image2video, [Path("a.png")]),
        (TaskType.frames2video, [Path("first.png"), Path("last.png")]),
    ]:
        _assert_no_internal_fields(_argv(task_type, refs))


def test_10_output_name_remains_present_in_task_spec() -> None:
    task = parse_manifest_csv(MANIFEST)[0]
    assert task.output_name == "DREAMINA_PREFLIGHT_TEXT2IMAGE_001"


def test_11_output_name_remains_present_in_run_plan_job_store_and_request_metadata() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    run_dir = Path(summary["dry_run_run_dir"])
    assert '"output_name"' in (run_dir / "run_plan.json").read_text(encoding="utf-8")
    assert '"output_name"' in (run_dir / "job_store.json").read_text(encoding="utf-8")
    assert '"output_name"' in Path(summary["provider_requests_path"]).read_text(encoding="utf-8")


def test_12_f3_dry_run_submit_argv_does_not_contain_output_name() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert "--output_name" not in summary["dry_run_argv"]
    request_text = Path(summary["provider_requests_path"]).read_text(encoding="utf-8")
    request = json.loads(request_text.splitlines()[0])
    assert "--output_name" not in request["command_argv"]
    assert request["output_name"] == "DREAMINA_PREFLIGHT_TEXT2IMAGE_001"


def test_13_reports_do_not_contain_question_mark_artifact() -> None:
    for report in [F3_REPORT, F3_1_REPORT]:
        assert "????" not in report.read_text(encoding="utf-8")


def test_14_reports_do_not_contain_false_true_artifact() -> None:
    for report in [F3_REPORT, F3_1_REPORT]:
        assert "false?True" not in report.read_text(encoding="utf-8")


def test_15_live_run_remains_disabled() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False


def test_16_no_dreamina_submit_query_or_download_happened() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert summary["submit_query_download_happened"] is False
    assert "query_result" not in summary["dry_run_argv"]
