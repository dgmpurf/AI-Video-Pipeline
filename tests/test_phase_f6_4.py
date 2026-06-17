from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
LOCKED_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "locked_refs"
    / "A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png"
)
SOURCE_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "runs"
    / "live"
    / "20260613_144850_A-SC-TEMPLE-COURTYARD-001"
    / "output"
    / "A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png"
)
REGISTRY_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "assets" / "asset_registry.json"
REVIEW_RECORDS = ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "review_records.jsonl"
REVIEW_MD = ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "image_reviews" / "A-SC-TEMPLE-COURTYARD-001_cand_001_review.md"
REPORT_PATH = ROOT / "reports" / "PHASE_F6_4_FIRST_LOCKED_ASSET_BASELINE_REPORT.md"
STATUS_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "PRODUCTION_STATUS.md"


def test_01_f6_4_locked_asset_integrity() -> None:
    assert LOCKED_PATH.exists()
    assert LOCKED_PATH.stat().st_size == 3563257
    sha256 = hashlib.sha256(LOCKED_PATH.read_bytes()).hexdigest()
    assert sha256 == "f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0"
    assert LOCKED_PATH.is_relative_to(ROOT)
    with Image.open(LOCKED_PATH) as image:
        assert image.size == (2560, 1440)
        assert image.format == "PNG"


def test_02_f6_4_review_and_registry_state() -> None:
    payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    matched = [
        item
        for item in payload.get("assets", [])
        if item["logical_id"] == "A-SC-TEMPLE-COURTYARD-001"
        and item["candidate_id"] == "A-SC-TEMPLE-COURTYARD-001_cand_001"
    ]
    assert len(matched) == 1
    item = matched[0]
    assert item["status"] == "locked_after_human_review"
    assert item["review_status"] == "approved"
    assert item["relative_path"] == "productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png"
    assert item["source_path"] == "productions/chi_yan_tian_qiong/runs/live/20260613_144850_A-SC-TEMPLE-COURTYARD-001/output/A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png"
    assert item["submit_id"] == "821c2865-26da-4c70-939f-07b4eb5a96d8"


def test_03_f6_4_review_record_exists() -> None:
    lines = [line for line in REVIEW_RECORDS.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert lines
    decoded = [json.loads(item) for item in lines]
    assert any(
        item["logical_id"] == "A-SC-TEMPLE-COURTYARD-001"
        and item["candidate_id"] == "A-SC-TEMPLE-COURTYARD-001_cand_001"
        and item["decision"] == "approve"
        for item in decoded
    )


def test_04_f6_4_review_markdown_decision_approve() -> None:
    text = REVIEW_MD.read_text(encoding="utf-8")
    assert "- approve" in text


def test_05_f6_4_report_and_status_files_and_verdict() -> None:
    assert REPORT_PATH.exists()
    report_text = REPORT_PATH.read_text(encoding="utf-8")
    assert "PHASE_F6_4_BASELINE_ACCEPTED" in report_text
    assert any(
        marker in report_text for marker in ("first_scene_asset_locked", "scene_and_first_character_subject_locked")
    )
    assert "No Dreamina command was executed" in report_text
    assert "No submit" in report_text
    assert "No external path was touched." in report_text
    assert STATUS_PATH.exists()
    status_text = STATUS_PATH.read_text(encoding="utf-8")
    assert "scene_and_first_character_subject_locked" in status_text
    assert "A-CH-A-SUBJECT-001" in status_text
