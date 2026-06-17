from __future__ import annotations

import json
from pathlib import Path

from app.ai_video_pipeline.core.manifest import parse_manifest_csv
from app.ai_video_pipeline.execution.runner import PipelineRunner

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "SHOT-01-KF-002"
FAILED_TASK_ID = "SHOT-01-KF-001"

PROMPT_PATH = ROOT / "productions" / PRODUCTION_ID / "prompts" / "shot_01_keyframe_prompt_SHOT-01-KF-002.json"
MANIFEST_PATH = ROOT / "productions" / PRODUCTION_ID / "manifests" / "production_image2image_SHOT-01-KF-002.csv"
SHOT_PATH = ROOT / "productions" / PRODUCTION_ID / "shots" / "shot_01_keyframe_record_SHOT-01-KF-002.json"
RULES_PATH = ROOT / "productions" / PRODUCTION_ID / "prompts" / "THREE_LAYER_POSITIONING_RULES.md"
SUMMARY_PATH = ROOT / "reports" / "SHOT-01-KF-002_readiness_summary.json"
FS_PLAN_PATH = ROOT / "reports" / "SHOT-01-KF-002_fs_write_plan.json"
CHECKLIST_PATH = ROOT / "reports" / "SHOT-01-KF-002_LIVE_APPROVAL_CHECKLIST.json"
REPORT_PATH = ROOT / "reports" / "PHASE_H3_SHOT01_KEYFRAME_RERUN_READINESS_REPORT.md"
REVIEW_PATH = ROOT / "productions" / PRODUCTION_ID / "reviews" / "image_reviews" / "SHOT-01-KF-001_cand_001_review.md"
REVIEW_RECORDS_PATH = ROOT / "productions" / PRODUCTION_ID / "reviews" / "review_records.jsonl"
ASSET_REGISTRY_PATH = ROOT / "productions" / PRODUCTION_ID / "assets" / "asset_registry.json"


def _summary() -> dict:
    return json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))


def _provider_request() -> dict:
    run_dir = Path(_summary()["dry_run_run_dir"])
    rows = [json.loads(line) for line in (run_dir / "provider_requests.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 1
    return rows[0]


def test_01_failed_keyframe_is_registered_as_needs_rerun_candidate() -> None:
    review = REVIEW_PATH.read_text(encoding="utf-8")
    assert "decision: needs_rerun" in review
    assert "three_layer_positioning_missing" in review
    registry = json.loads(ASSET_REGISTRY_PATH.read_text(encoding="utf-8"))
    matches = [item for item in registry["assets"] if item["logical_id"] == FAILED_TASK_ID and item["candidate_id"] == "SHOT-01-KF-001_cand_001"]
    assert matches
    item = matches[-1]
    assert item["status"] == "candidate"
    assert item["review_status"] == "needs_rerun"
    assert "locked_refs" not in item["relative_path"]


def test_02_review_record_was_added_without_locking_failed_keyframe() -> None:
    records = [json.loads(line) for line in REVIEW_RECORDS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    matches = [item for item in records if item.get("review_id") == "review-h2-2-shot-01-kf-001"]
    assert matches
    assert matches[-1]["decision"] == "needs_rerun"
    assert matches[-1]["target_status_after_decision"] == "candidate"
    assert matches[-1]["locked_path"] == ""


def test_03_three_layer_rules_and_prompt_matrix_exist() -> None:
    rules = RULES_PATH.read_text(encoding="utf-8")
    assert "Space Layer" in rules
    assert "Character Blocking Layer" in rules
    assert "Camera Layer" in rules
    prompt = json.loads(PROMPT_PATH.read_text(encoding="utf-8"))
    matrix = prompt["three_layer_positioning_matrix"]
    assert "space_layer" in matrix
    assert "character_blocking_layer" in matrix
    assert "camera_layer" in matrix
    assert "foreground lineup" in prompt["prompt_text"]


def test_04_new_manifest_is_single_image2image_task_with_reference_order() -> None:
    tasks = parse_manifest_csv(MANIFEST_PATH)
    assert len(tasks) == 1
    task = tasks[0]
    assert task.task_id == TASK_ID
    assert task.phase == "shot_keyframe"
    assert task.task_type.value == "image2image"
    assert task.provider.value == "dreamina_cli"
    assert task.model_version == "5.0"
    assert task.ratio == "16:9"
    assert task.resolution_type == "2k"
    assert task.output_name == "SHOT-01-KF-002_temple_gate_courtyard_standoff_keyframe"
    assert task.reference_ids == [
        "A-SC-TEMPLE-COURTYARD-001",
        "A-CH-A-SUBJECT-001",
        "A-CH-B-SUBJECT-001",
    ]


def test_05_shot_record_documents_rerun_spatial_blocking() -> None:
    shot_payload = json.loads(SHOT_PATH.read_text(encoding="utf-8"))
    shot = shot_payload["shots"][0]
    assert shot["shot_id"] == TASK_ID
    assert shot["previous_shot_id"] == FAILED_TASK_ID
    assert shot["shot_type"] == "action"
    assert "three-quarter front-side" in shot["camera_goal"].lower()
    assert shot["three_layer_positioning_matrix"]["space_layer"]


def test_06_dry_run_argv_has_image2image_repeated_images_and_no_forbidden_flags() -> None:
    argv = _provider_request()["command_argv"]
    joined = " ".join(argv)
    assert argv[0] == "C:/Users/msjpurf/bin/dreamina.exe"
    assert argv[1] == "image2image"
    assert argv.count("--images") == 3
    assert "--prompt" in argv
    assert "--resolution_type" in argv
    assert "--output_name" not in argv
    assert "output_dir" not in joined
    assert "download_dir" not in joined
    assert "query_result" not in joined
    assert "submit_id" not in joined
    assert "--image" not in argv
    assert "--refs" not in argv
    assert "--ref_strength" not in argv


def test_07_staged_reference_manifest_is_inside_workspace_ascii_and_sha_matched() -> None:
    manifest_path = Path(_summary()["input_media_manifest_path"])
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    refs = payload["references"]
    assert len(refs) == 3
    assert [item["logical_id"] for item in refs] == [
        "A-SC-TEMPLE-COURTYARD-001",
        "A-CH-A-SUBJECT-001",
        "A-CH-B-SUBJECT-001",
    ]
    assert all(Path(item["staged_path"]).is_relative_to(ROOT) for item in refs)
    assert all(item["staged_filename_ascii"] is True for item in refs)
    assert all(item["sha256_match"] is True for item in refs)


def test_08_approval_checklist_and_fs_plan_keep_live_run_closed() -> None:
    checklist = json.loads(CHECKLIST_PATH.read_text(encoding="utf-8"))
    assert checklist["user_approved_live_run"] is False
    assert checklist["allow_single_task_only"] is True
    assert checklist["allow_batch"] is False
    assert checklist["allow_parallel"] is False
    assert checklist["allow_auto_continue"] is False
    assert checklist["allow_retry"] is False
    assert checklist["dry_run_passed"] is True
    assert checklist["fs_write_plan_reviewed"] is False
    assert checklist["provider_live_run_enabled"] is False
    fs_plan = json.loads(FS_PLAN_PATH.read_text(encoding="utf-8"))
    assert fs_plan["approved"] is False
    assert all(item["executed"] is False for item in fs_plan["planned_operations"])
    assert not (ROOT / "productions" / PRODUCTION_ID / "runs" / "live" / _summary()["dry_run_run_id"]).exists()


def test_09_live_run_remains_disabled_and_default_gate_denies() -> None:
    runner = PipelineRunner(ROOT)
    assert runner.can_run_live() is False
    summary = _summary()
    assert summary["providers_json_allow_live_run"] is False
    assert summary["default_live_gate"]["allowed"] is False
    assert "dreamina_cli live-run disabled by provider config" in summary["default_live_gate"]["required_actions"]
    assert summary["dreamina_command_executed"] is False
    assert summary["submit_query_download_happened"] is False
    assert summary["external_path_touched"] is False


def test_10_report_and_artifacts_have_no_garbled_tokens() -> None:
    paths = [
        REPORT_PATH,
        SUMMARY_PATH,
        FS_PLAN_PATH,
        CHECKLIST_PATH,
        PROMPT_PATH,
        MANIFEST_PATH,
        SHOT_PATH,
        RULES_PATH,
        REVIEW_PATH,
    ]
    for path in paths:
        content = path.read_text(encoding="utf-8")
        assert "????" not in content
        assert "false?True" not in content
    assert "PHASE_H3_ACCEPTED" in REPORT_PATH.read_text(encoding="utf-8")
