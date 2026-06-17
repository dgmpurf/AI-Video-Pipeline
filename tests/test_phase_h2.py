from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.core.models import ProviderName, TaskType
from app.ai_video_pipeline.execution.dreamina_h2_live import (
    CommandResult,
    OneShotLiveAuthorization,
    execute_h2_live_run,
)

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "SHOT-01-KF-001"
REPORT = ROOT / "reports" / "PHASE_H2_SHOT01_KEYFRAME_IMAGE2IMAGE_LIVE_RUN_REPORT.md"
MANIFEST = ROOT / "productions" / PRODUCTION_ID / "manifests" / "production_image2image_SHOT-01-KF-001.csv"
REF_IDS = [
    "A-SC-TEMPLE-COURTYARD-001",
    "A-CH-A-SUBJECT-001",
    "A-CH-B-SUBJECT-001",
]


def _make_image(path: Path, size: tuple[int, int], seed: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", size)
    pixels = image.load()
    for y in range(size[1]):
        for x in range(size[0]):
            pixels[x, y] = ((x * seed) % 256, (y * (seed + 3)) % 256, ((x + y) * (seed + 7)) % 256)
    image.save(path)


def _sha(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def _workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "configs").mkdir(parents=True)
    (workspace / "reports").mkdir(parents=True)
    (workspace / "productions" / PRODUCTION_ID / "manifests").mkdir(parents=True)
    (workspace / "productions" / PRODUCTION_ID / "prompts").mkdir(parents=True)
    (workspace / "productions" / PRODUCTION_ID / "assets").mkdir(parents=True)
    (workspace / "productions" / PRODUCTION_ID / "locked_refs").mkdir(parents=True)
    shutil.copy2(ROOT / "configs" / "providers.json", workspace / "configs" / "providers.json")
    shutil.copy2(MANIFEST, workspace / "productions" / PRODUCTION_ID / "manifests" / MANIFEST.name)
    shutil.copy2(
        ROOT / "productions" / PRODUCTION_ID / "prompts" / "shot_01_keyframe_prompt_SHOT-01-KF-001.json",
        workspace / "productions" / PRODUCTION_ID / "prompts" / "shot_01_keyframe_prompt_SHOT-01-KF-001.json",
    )
    records = []
    for index, logical_id in enumerate(REF_IDS, start=1):
        path = workspace / "productions" / PRODUCTION_ID / "locked_refs" / f"{logical_id}_locked.png"
        _make_image(path, (180 + index * 10, 180 + index * 10), index * 11)
        with Image.open(path) as image:
            width, height = image.width, image.height
        records.append(
            {
                "logical_id": logical_id,
                "candidate_id": f"{logical_id}_cand_001",
                "asset_type": "image",
                "role": "scene" if index == 1 else "character",
                "relative_path": f"productions/{PRODUCTION_ID}/locked_refs/{path.name}",
                "source_path": f"productions/{PRODUCTION_ID}/runs/live/source/{path.name}",
                "status": "locked_after_human_review",
                "review_status": "approved",
                "origin_project": "AI_VIDEO_PIPELINE",
                "source_task_id": logical_id,
                "submit_id": f"submit-{index}",
                "review_note": "test locked ref",
                "tags": ["locked_ref"],
                "sha256": _sha(path),
                "width": width,
                "height": height,
                "duration_seconds": None,
            }
        )
    (workspace / "productions" / PRODUCTION_ID / "assets" / "asset_registry.json").write_text(json.dumps({"assets": records, "relationships": []}, ensure_ascii=True, indent=2), encoding="utf-8")
    shutil.copy2(ROOT / "reports" / "SHOT-01-KF-001_fs_write_plan.json", workspace / "reports" / "SHOT-01-KF-001_fs_write_plan.json")
    shutil.copy2(ROOT / "reports" / "SHOT-01-KF-001_LIVE_APPROVAL_CHECKLIST.json", workspace / "reports" / "SHOT-01-KF-001_LIVE_APPROVAL_CHECKLIST.json")
    return workspace


def test_01_one_shot_authorization_applies_only_to_exact_task_id() -> None:
    task = parse_manifest_csv(MANIFEST)[0]
    auth = OneShotLiveAuthorization.required()
    assert auth.allows(task, 1) is True
    task.task_id = "OTHER"
    assert auth.allows(task, 1) is False


def test_02_authorization_is_consumed_after_submit() -> None:
    auth = OneShotLiveAuthorization.required()
    auth.consume()
    assert auth.consumed is True
    assert auth.allows(parse_manifest_csv(MANIFEST)[0], 1) is False


def test_03_live_argv_uses_image2image_repeated_images_and_no_forbidden_flags(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    calls: list[list[str]] = []

    def runner(argv):
        calls.append(list(argv))
        return CommandResult(list(argv), 0, '{"submit_id":"SUB-H2"}', "") if argv[1] == "image2image" else CommandResult(list(argv), 0, '{"status":"querying"}', "")

    execute_h2_live_run(workspace, runner=runner)
    argv = calls[0]
    joined = " ".join(argv)
    assert argv[1] == "image2image"
    assert argv.count("--images") == 3
    assert "--image" not in argv
    assert "--output_name" not in argv
    assert "output_dir" not in joined
    assert "query_result" not in argv


def test_04_download_dir_is_only_used_in_download_stage(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    calls: list[list[str]] = []

    def runner(argv):
        calls.append(list(argv))
        if argv[1] == "image2image":
            return CommandResult(list(argv), 0, '{"submit_id":"SUB-H2"}', "")
        if "--download_dir" not in argv:
            return CommandResult(list(argv), 0, '{"status":"success"}', "")
        download_dir = Path(argv[argv.index("--download_dir") + 1])
        _make_image(download_dir / "raw.png", (220, 220), 23)
        return CommandResult(list(argv), 0, '{"status":"downloaded"}', "")

    result = execute_h2_live_run(workspace, runner=runner)
    assert result.verdict == "PHASE_H2_SUCCESS_DOWNLOADED"
    assert "--download_dir" not in calls[0]
    assert "--download_dir" not in calls[1]
    assert "--download_dir" in calls[2]


def test_05_source_references_are_locked_approved_and_staged_with_matching_sha(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)

    def runner(argv):
        if argv[1] == "image2image":
            return CommandResult(list(argv), 0, '{"submit_id":"SUB-H2"}', "")
        return CommandResult(list(argv), 0, '{"status":"querying"}', "")

    result = execute_h2_live_run(workspace, runner=runner)
    assert len(result.staged_refs) == 3
    assert all(Path(item["staged_path"]).is_relative_to(workspace) for item in result.staged_refs)
    assert all(item["source_sha256"] == item["staged_sha256"] for item in result.staged_refs)
    assert (result.run_context.input_media_dir / "input_media_manifest.json").exists()


def test_06_submit_id_persistence_happens_before_query(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    evidence: dict[str, bool] = {}

    def runner(argv):
        if argv[1] == "image2image":
            return CommandResult(list(argv), 0, '{"submit_id":"SUB-H2"}', "")
        run_dir = sorted((workspace / "productions" / PRODUCTION_ID / "runs" / "live").iterdir())[-1]
        evidence["persisted"] = "SUB-H2" in (run_dir / "job_store.json").read_text(encoding="utf-8")
        return CommandResult(list(argv), 0, '{"status":"querying"}', "")

    execute_h2_live_run(workspace, runner=runner)
    assert evidence["persisted"] is True


def test_07_querying_state_resumes_query_only(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    calls: list[list[str]] = []

    def runner(argv):
        calls.append(list(argv))
        if argv[1] == "image2image":
            return CommandResult(list(argv), 0, '{"submit_id":"SUB-H2"}', "")
        return CommandResult(list(argv), 0, '{"status":"querying"}', "")

    result = execute_h2_live_run(workspace, runner=runner)
    assert result.verdict == "PHASE_H2_SUBMITTED_QUERYING"
    assert len(calls) == 2
    assert result.run_context.querying_tasks_csv.read_text(encoding="utf-8").strip()
    assert not result.run_context.downloaded_files_csv.read_text(encoding="utf-8").strip()


def test_08_success_state_downloads_and_renames_inside_workspace(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)

    def runner(argv):
        if argv[1] == "image2image":
            return CommandResult(list(argv), 0, '{"submit_id":"SUB-H2"}', "")
        if "--download_dir" not in argv:
            return CommandResult(list(argv), 0, '{"status":"success"}', "")
        download_dir = Path(argv[argv.index("--download_dir") + 1])
        _make_image(download_dir / "raw.png", (220, 220), 31)
        return CommandResult(list(argv), 0, '{"status":"downloaded"}', "")

    result = execute_h2_live_run(workspace, runner=runner)
    assert result.output_path is not None
    assert result.output_path.name == "SHOT-01-KF-001_temple_courtyard_standoff_keyframe.png"
    assert result.output_path.is_relative_to(workspace)


def test_09_providers_json_remains_allow_live_run_false() -> None:
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert providers["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_10_no_batch_parallel_or_retry_allowed() -> None:
    auth = OneShotLiveAuthorization.required()
    assert auth.allow_batch is False
    assert auth.allow_parallel is False
    assert auth.allow_retry is False
    assert auth.allow_auto_continue is False
    assert auth.allows(parse_manifest_csv(MANIFEST)[0], 2) is False


def test_11_phase_h2_report_has_no_prohibited_strings() -> None:
    report = REPORT.read_text(encoding="utf-8")
    assert "????" not in report
    assert "false?True" not in report
