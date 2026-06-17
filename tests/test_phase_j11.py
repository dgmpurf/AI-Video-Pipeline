from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ID = "chi_yan_tian_qiong"
TASK_ID = "A-SC-TEMPLE-COURTYARD-004"
CANDIDATE_ID = "A-SC-TEMPLE-COURTYARD-004_cand_001"

SOURCE_PATH = (
    ROOT
    / "productions"
    / PRODUCTION_ID
    / "runs"
    / "live"
    / "20260617_150916_A-SC-TEMPLE-COURTYARD-004"
    / "output"
    / "A-SC-TEMPLE-COURTYARD-004_main_hall_true_frontal_axis_stage.png"
)
LOCKED_PATH = (
    ROOT
    / "productions"
    / PRODUCTION_ID
    / "locked_refs"
    / "A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png"
)
REGISTRY_PATH = ROOT / "productions" / PRODUCTION_ID / "assets" / "asset_registry.json"
RECORDS_PATH = ROOT / "productions" / PRODUCTION_ID / "reviews" / "review_records.jsonl"
PROMPT_JSON_PATH = (
    ROOT
    / "productions"
    / PRODUCTION_ID
    / "prompts"
    / "production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-004.json"
)
PROMPT_MANIFEST_PATH = ROOT / "productions" / PRODUCTION_ID / "prompts" / "prompt_manifest.json"
REVIEW_PATH = ROOT / "productions" / PRODUCTION_ID / "reviews" / "image_reviews" / "A-SC-TEMPLE-COURTYARD-004_readiness_review.md"
STATUS_PATH = ROOT / "productions" / PRODUCTION_ID / "PRODUCTION_STATUS.md"
REPORT_PATH = ROOT / "reports" / "PHASE_J11_A_SC_TEMPLE_COURTYARD_004_LOCK_REPORT.md"

EXPECTED_SHA256 = "831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452"


def _registry_assets() -> list[dict]:
    payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return payload.get("assets", [])


def test_01_locked_copy_exists_and_matches_preferred_source() -> None:
    assert SOURCE_PATH.exists()
    assert LOCKED_PATH.exists()
    assert sha256(SOURCE_PATH.read_bytes()).hexdigest() == EXPECTED_SHA256
    assert sha256(LOCKED_PATH.read_bytes()).hexdigest() == EXPECTED_SHA256
    with Image.open(LOCKED_PATH) as image:
        assert image.format == "PNG"
        assert image.width == 2560
        assert image.height == 1440


def test_02_registry_marks_a_sc_004_as_locked_scene_reference() -> None:
    matches = [
        item
        for item in _registry_assets()
        if item.get("logical_id") == TASK_ID and item.get("candidate_id") == CANDIDATE_ID
    ]
    assert len(matches) == 1
    item = matches[0]
    assert item["status"] == "locked_after_human_review"
    assert item["review_status"] == "approved"
    assert item["locked"] is True
    assert item["preferred_candidate"] is True
    assert item["relative_path"] == "productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png"
    assert item["source_path"] == "productions/chi_yan_tian_qiong/runs/live/20260617_150916_A-SC-TEMPLE-COURTYARD-004/output/A-SC-TEMPLE-COURTYARD-004_main_hall_true_frontal_axis_stage.png"
    assert item["sha256"] == EXPECTED_SHA256
    assert "locked_ref" in item["tags"]


def test_03_review_record_documents_user_lock_decision() -> None:
    records = [json.loads(line) for line in RECORDS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    matches = [
        item
        for item in records
        if item.get("logical_id") == TASK_ID
        and item.get("candidate_id") == CANDIDATE_ID
        and item.get("decision") == "approve"
    ]
    assert matches
    latest = matches[-1]
    assert latest["target_status_after_decision"] == "locked_after_human_review"
    assert latest["locked_path"] == "productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png"
    assert latest["source_path"] == "productions/chi_yan_tian_qiong/runs/live/20260617_150916_A-SC-TEMPLE-COURTYARD-004/output/A-SC-TEMPLE-COURTYARD-004_main_hall_true_frontal_axis_stage.png"


def test_04_prompt_and_status_files_unblock_shot_02_kf_002() -> None:
    prompt = json.loads(PROMPT_JSON_PATH.read_text(encoding="utf-8"))
    assert prompt["status"] == "locked_after_human_review"
    assert prompt["locked"] is True
    assert prompt["lock_status"] == "locked"
    assert prompt["locked_path"] == "productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png"

    manifest = json.loads(PROMPT_MANIFEST_PATH.read_text(encoding="utf-8"))
    records = manifest["prompts"]
    matches = [item for item in records if item.get("prompt_id") == TASK_ID]
    assert matches[-1]["status"] == "locked_after_human_review"
    assert matches[-1]["locked"] is True
    assert matches[-1]["locked_path"] == prompt["locked_path"]

    status = STATUS_PATH.read_text(encoding="utf-8")
    assert "current_production_status: shot_02_scene_anchor_004_locked" in status
    assert "blocker: cleared" in status
    assert "next_allowed_action: submit SHOT-02-KF-002" in status


def test_05_review_and_report_are_clean() -> None:
    review = REVIEW_PATH.read_text(encoding="utf-8")
    report = REPORT_PATH.read_text(encoding="utf-8")
    assert "Status: locked_after_human_review" in review
    assert "Final decision: approved_and_locked" in review
    assert "PHASE_J11_A_SC_004_LOCK_ACCEPTED" in report
    assert "C:/Users/msjpurf/bin/dreamina.exe" not in report
    assert "????" not in review + report
    assert "false?True" not in review + report
