from __future__ import annotations

from PIL import Image
import hashlib
import json

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LOCKED_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "locked_refs"
    / "A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png"
)

SOURCE_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "runs"
    / "live"
    / "20260613_162002_A-CH-A-SUBJECT-001"
    / "output"
    / "A-CH-A-SUBJECT-001_fenshou_full_body_subject.png"
)

REGISTRY_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "assets"
    / "asset_registry.json"
)

RECORDS_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "reviews"
    / "review_records.jsonl"
)

REVIEW_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "reviews"
    / "image_reviews"
    / "A-CH-A-SUBJECT-001_cand_001_review.md"
)

STATUS_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "PRODUCTION_STATUS.md"


def test_01_f2_3_locked_image_exists_and_integrity() -> None:
    assert LOCKED_PATH.exists()
    assert LOCKED_PATH.stat().st_size == 1959523
    assert (
        hashlib.sha256(LOCKED_PATH.read_bytes()).hexdigest()
        == "83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f"
    )

    with Image.open(LOCKED_PATH) as image:
        assert image.width == 1440
        assert image.height == 2560
        assert image.format == "PNG"


def test_02_candidate_locked_state_in_registry() -> None:
    payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    matched = [
        item
        for item in payload.get("assets", [])
        if item["logical_id"] == "A-CH-A-SUBJECT-001"
        and item["candidate_id"] == "A-CH-A-SUBJECT-001_cand_001"
    ]
    assert len(matched) == 1
    item = matched[0]
    assert item["status"] == "locked_after_human_review"
    assert item["review_status"] == "approved"
    assert item["relative_path"] == "productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png"
    assert item["source_path"] == "productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/output/A-CH-A-SUBJECT-001_fenshou_full_body_subject.png"


def test_03_review_records_and_template_show_approve() -> None:
    lines = [json.loads(item) for item in RECORDS_PATH.read_text(encoding="utf-8").splitlines() if item.strip()]
    assert any(
        item["logical_id"] == "A-CH-A-SUBJECT-001"
        and item["candidate_id"] == "A-CH-A-SUBJECT-001_cand_001"
        and item["decision"] == "approve"
        for item in lines
    )

    text = REVIEW_PATH.read_text(encoding="utf-8")
    assert "Final decision" in text
    assert "- approve" in text


def test_04_status_summary_records_scene_and_character_locked() -> None:
    status_text = STATUS_PATH.read_text(encoding="utf-8")
    assert "scene_and_first_character_subject_locked" in status_text
    assert "A-SC-TEMPLE-COURTYARD-001" in status_text
    assert "A-CH-A-SUBJECT-001" in status_text
    assert "A-CH-B-SUBJECT-001" in status_text
    assert "G3 Shuangji character subject readiness package" in status_text
