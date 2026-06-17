from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from app.ai_video_pipeline.assets.media_integrity import compute_sha256
from app.ai_video_pipeline.assets.staging import stage_media_file
from app.ai_video_pipeline.core.manifest import MANIFEST_FIELDS, parse_manifest_row
from app.ai_video_pipeline.core.models import ProviderName, RunMode, TaskSpec, TaskType
from app.ai_video_pipeline.core.validation import parse_reference_ids
from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy, PathPolicyError
from app.ai_video_pipeline.providers.dreamina_cli import DreaminaCLIProvider
from app.ai_video_pipeline.tools import DEFAULT_FORBIDDEN_TOKENS, scan_forbidden_paths, write_scan_report

ROOT = Path(__file__).resolve().parents[1]


def _init_workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    (workspace / "mock_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "live_outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "productions" / "chi_yan_tian_qiong" / "locked_refs").mkdir(parents=True, exist_ok=True)
    for file in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / file, workspace / "configs" / file)
    return workspace


def _sample_task(
    task_id: str = "task01",
    task_type: TaskType = TaskType.text2image,
    provider: ProviderName = ProviderName.dreamina_cli,
    prompt: str = "test prompt",
    output_name: str = "output_01",
    ratio: str | None = None,
    reference_ids: list[str] | None = None,
) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        phase="phase1",
        task_type=task_type,
        provider=provider,
        model_version=None,
        ratio=ratio or "16:9",
        resolution_type=None,
        duration=None,
        video_resolution=None,
        prompt=prompt,
        reference_ids=reference_ids or [],
        output_name=output_name,
        status=None,
        review_status=None,
        notes=None,
    )


def test_01_path_policy_denies_outside_workspace(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    outside = tmp_path / "outside" / "asset.txt"
    with pytest.raises(PathPolicyError):
        policy.ensure_write(outside)


def test_02_path_policy_allows_workspace_paths(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    target = workspace / "staging" / "in_workspace.txt"
    resolved = policy.ensure_write(target)
    assert resolved == target.resolve()


def test_03_external_staging_is_denied(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    source = workspace / "source.bin"
    source.write_bytes(b"abc")
    external_staging = tmp_path / "external_staging"
    with pytest.raises(PathPolicyError):
        stage_media_file(source, external_staging, policy)


def test_04_manifest_row_parses_into_task_spec() -> None:
    row = {field: "" for field in MANIFEST_FIELDS}
    row.update(
        {
            "task_id": "t1",
            "task_type": "image2video",
            "provider": "dreamina_cli",
            "prompt": "look here",
            "output_name": "shot01",
            "reference_ids": "ref1|ref2",
        }
    )
    task = parse_manifest_row(2, row)
    assert task.task_id == "t1"
    assert task.task_type == TaskType.image2video
    assert task.provider == ProviderName.dreamina_cli
    assert task.output_name == "shot01"


def test_05_manifest_row_missing_task_id_fails() -> None:
    row = {field: "" for field in MANIFEST_FIELDS}
    row.update({"task_type": "text2image", "provider": "dreamina_cli", "prompt": "x", "output_name": "y"})
    with pytest.raises(ValueError):
        parse_manifest_row(2, row)


def test_06_manifest_row_missing_output_name_fails() -> None:
    row = {field: "" for field in MANIFEST_FIELDS}
    row.update({"task_id": "t1", "task_type": "text2image", "provider": "dreamina_cli", "prompt": "x"})
    with pytest.raises(ValueError):
        parse_manifest_row(2, row)


def test_07_reference_ids_split_by_delimiter() -> None:
    assert parse_reference_ids("a|b|c") == ["a", "b", "c"]
    assert parse_reference_ids("a|b|  c  |") == ["a", "b", "c"]
    assert parse_reference_ids("") == []


def test_08_image2image_command_uses_repeated_images() -> None:
    task = _sample_task(task_id="t8", task_type=TaskType.image2image)
    cmd = DreaminaCLIProvider().build_submit_command(task, [Path("img1.png"), Path("img2.png")])
    assert cmd.count("--images") == 2


def test_09_multimodal2video_command_repeats_image_flag() -> None:
    task = _sample_task(task_id="t9", task_type=TaskType.multimodal2video)
    cmd = DreaminaCLIProvider().build_submit_command(task, [Path("img1.png"), Path("img2.png")])
    assert cmd.count("--image") == 2


def test_10_multimodal2video_command_no_refs() -> None:
    task = _sample_task(task_id="t10", task_type=TaskType.multimodal2video)
    cmd = DreaminaCLIProvider().build_submit_command(task, [Path("img1.png")])
    assert "--refs" not in cmd


def test_11_image2video_command_no_ratio() -> None:
    task = _sample_task(task_id="t11", task_type=TaskType.image2video, ratio="4:3")
    cmd = DreaminaCLIProvider().build_submit_command(task, [Path("img1.png")])
    assert "--ratio" not in cmd


def test_12_submit_command_never_includes_output_dir() -> None:
    task = _sample_task(task_id="t12", task_type=TaskType.text2image)
    cmd = DreaminaCLIProvider().build_submit_command(task, [])
    assert "--output_dir" not in cmd


def test_13_command_builder_returns_argv_list() -> None:
    task = _sample_task(task_id="t13", task_type=TaskType.text2image)
    cmd = DreaminaCLIProvider().build_submit_command(task, [])
    assert isinstance(cmd, list)
    assert all(isinstance(token, str) for token in cmd)


def test_14_staging_produces_ascii_filenames_and_stays_in_workspace(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    source = workspace / "中文名图片.png"
    source.write_bytes(b"hello")
    staged, _ = stage_media_file(source, workspace / "staging", policy)
    assert staged.is_relative_to(workspace)
    assert staged.name.encode("ascii")


def test_15_staging_sha256_matches_source(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    policy = PathPolicy(workspace)
    source = workspace / "source.bin"
    source.write_bytes(b"content-check")
    staged, digest = stage_media_file(source, workspace / "staging", policy)
    assert compute_sha256(staged) == digest


def test_16_mock_outputs_dont_enter_locked_refs(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    task = _sample_task(task_id="t16", task_type=TaskType.text2image)
    locked = workspace / "productions" / "chi_yan_tian_qiong" / "locked_refs"
    before = set(locked.glob("*"))
    artifacts = runner.mock_run([task], production_id="chi_yan_tian_qiong", run_id="run16")
    after = set(locked.glob("*"))
    assert after == before
    assert artifacts.completed_csv.exists()


def test_17_generated_reports_have_no_garbled_unicode_chars(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    task = _sample_task(task_id="t17", task_type=TaskType.text2image)
    artifacts = runner.mock_run([task], production_id="chi_yan_tian_qiong", run_id="run17")
    for path in [artifacts.provider_requests_jsonl, artifacts.command_preview_csv, artifacts.submitted_csv, artifacts.completed_csv, artifacts.downloaded_csv]:
        text = path.read_text(encoding="utf-8")
        assert "????" not in text
        assert "false?True" not in text


def test_18_provider_stubs_are_disabled(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    cfg = json.loads((workspace / "configs" / "providers.json").read_text(encoding="utf-8"))
    for name in ("kling_api", "hailuo_api", "runway_api", "midjourney_image"):
        assert cfg["providers"][name]["enabled"] is False


def test_19_live_run_disabled_by_default(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False


def test_20_dry_run_builds_preview_and_requests_without_submit(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    ref = workspace / "ref_a.png"
    ref.write_bytes(b"image")
    task = _sample_task(
        task_id="t20",
        task_type=TaskType.text2image,
    )
    runner = PipelineRunner(workspace)
    artifacts = runner.dry_run([task], production_id="chi_yan_tian_qiong", run_id="run20")
    assert artifacts.provider_requests_jsonl.exists()
    assert artifacts.command_preview_csv.exists()
    text = artifacts.provider_requests_jsonl.read_text(encoding="utf-8")
    assert "dreamina" in text


def test_21_forbidden_scan_includes_real_unicode_token(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    (workspace / "notes.txt").write_text(
        "Legacy workspace token: AI\u89c6\u9891\u5de5\u4f5c\u6d41",
        encoding="utf-8",
    )
    result = scan_forbidden_paths(workspace)
    matches = {m.token for m in result.matches}
    assert "AI\u89c6\u9891\u5de5\u4f5c\u6d41" in matches


def test_22_forbidden_scan_includes_mojibake_token(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    mojibake_token = "".join(["AI", chr(0x7459), chr(0x55db)])
    (workspace / "notes_mojibake.txt").write_text(f"Legacy mojibake marker: {mojibake_token}", encoding="utf-8")
    result = scan_forbidden_paths(workspace)
    matches = {m.token for m in result.matches}
    assert mojibake_token in matches


def test_23_forbidden_scan_only_scans_workspace(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    _outside = tmp_path / "outside"
    _outside.mkdir(exist_ok=True)
    (_outside / "outside.txt").write_text("AI\u89c6\u9891\u5de5\u4f5c\u6d41", encoding="utf-8")
    result = scan_forbidden_paths(workspace)
    scanned_any_outside = any(
        p.resolve().is_relative_to(_outside.resolve()) for p in result.files_scanned
    )
    assert not scanned_any_outside


def test_24_scan_report_is_ascii_safe_and_marks_final_result(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    forbidden = ["AI\u89c6\u9891\u5de5\u4f5c\u6d41"]
    result = scan_forbidden_paths(workspace, forbidden_tokens=forbidden)
    report = workspace / "reports" / "PHASE_A1_1_ENCODING_SAFE_PATH_SCAN.md"
    write_scan_report(report, result)
    text = report.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text
    assert "Final result: PASS" in text
    assert "- No Dreamina command was executed during the scan." in text
    assert "Parent directory was not scanned: verified." in text
    assert report.resolve().is_relative_to(workspace.resolve())


def test_25_forbidden_scan_report_reports_line_context_and_violation_status(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    (workspace / "bad.txt").write_text("Legacy path: AI\u89c6\u9891\u5de5\u4f5c\u6d41", encoding="utf-8")
    result = scan_forbidden_paths(workspace)
    report = workspace / "reports" / "PHASE_A1_1_ENCODING_SAFE_PATH_SCAN.md"
    write_scan_report(report, result)
    text = report.read_text(encoding="utf-8")
    assert "[violation]" in text
    assert "bad.txt:" in text
    assert "forbidden token list" in text.lower()


def test_26_no_old_project_accessed_and_live_disabled_remain(tmp_path: Path) -> None:
    workspace = _init_workspace(tmp_path)
    runner = PipelineRunner(workspace)
    assert runner.can_run_live() is False
    assert runner.run_mode_allowed(RunMode.live) is False
    result = scan_forbidden_paths(workspace)
    assert all(
        p.resolve().is_relative_to(workspace.resolve()) for p in result.files_scanned
    )
