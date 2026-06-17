from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "runs"
    / "live"
    / "20260614_055254_A-CH-B-SUBJECT-001"
    / "output"
    / "A-CH-B-SUBJECT-001_shuangji_full_body_subject.png"
)
LOCKED_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "locked_refs"
    / "A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png"
)
RECORD_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "assets" / "asset_registry.json"
RECORDS_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "review_records.jsonl"
REVIEW_TEMPLATE_PATH = (
    ROOT
    / "productions"
    / "chi_yan_tian_qiong"
    / "reviews"
    / "image_reviews"
    / "A-CH-B-SUBJECT-001_cand_001_review.md"
)
REPORT_PATH = ROOT / "reports" / "PHASE_G4_3_LOCK_SHUANGJI_SUBJECT_ASSET_REPORT.md"


def test_01_locked_asset_created_in_workspace_and_ascii_filename() -> None:
    assert LOCKED_PATH.exists()
    assert LOCKED_PATH.resolve().is_relative_to(ROOT)
    assert LOCKED_PATH.name.isascii()


def test_02_source_output_not_moved() -> None:
    assert SOURCE_PATH.exists()
    assert SOURCE_PATH.stat().st_size > 10 * 1024
    assert LOCKED_PATH.exists()


def test_03_locked_copy_matches_source_integrity() -> None:
    src_sha = hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest()
    locked_sha = hashlib.sha256(LOCKED_PATH.read_bytes()).hexdigest()
    assert src_sha == locked_sha

    with Image.open(SOURCE_PATH) as source_image:
        assert source_image.format == "PNG"
        assert source_image.width == 1440
        assert source_image.height == 2560

    with Image.open(LOCKED_PATH) as locked_image:
        assert locked_image.format == "PNG"
        assert locked_image.width == 1440
        assert locked_image.height == 2560

    assert SOURCE_PATH.stat().st_size == LOCKED_PATH.stat().st_size


def test_04_asset_registry_marks_locked_after_human_review() -> None:
    payload = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
    item = next(
        (
            asset
            for asset in payload.get("assets", [])
            if asset["logical_id"] == "A-CH-B-SUBJECT-001"
            and asset["candidate_id"] == "A-CH-B-SUBJECT-001_cand_001"
        ),
        None,
    )
    assert item is not None
    assert item["status"] == "locked_after_human_review"
    assert item["review_status"] == "approved"
    assert item["relative_path"].endswith("locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png")
    assert item["source_path"].endswith(
        "runs/live/20260614_055254_A-CH-B-SUBJECT-001/output/A-CH-B-SUBJECT-001_shuangji_full_body_subject.png"
    )
    assert item["submit_id"] == "b381e6d4-c559-4689-a09c-03289ac63319"


def test_05_review_record_and_template_show_approval() -> None:
    lines = [json.loads(item) for item in RECORDS_PATH.read_text(encoding="utf-8").splitlines() if item.strip()]
    assert any(
        item["logical_id"] == "A-CH-B-SUBJECT-001"
        and item["candidate_id"] == "A-CH-B-SUBJECT-001_cand_001"
        and item["decision"] == "approve"
        and item["target_status_after_decision"] == "locked_after_human_review"
        for item in lines
    )

    text = REVIEW_TEMPLATE_PATH.read_text(encoding="utf-8")
    assert "Final decision" in text
    assert "- approve" in text


def test_06_report_has_no_banned_artifacts_and_verdict() -> None:
    text = REPORT_PATH.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text
    assert "PHASE_G4_3_LOCKED_ASSET_ACCEPTED" in text
    assert "C:/Users/msjpurf/bin/dreamina.exe" not in text


def test_07_dreamina_live_run_still_disabled() -> None:
    config = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert config["providers"]["dreamina_cli"]["allow_live_run"] is False
