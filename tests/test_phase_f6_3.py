from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

RECORD_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "assets" / "asset_registry.json"
RECORDS_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "review_records.jsonl"
REVIEW_TEMPLATE_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "image_reviews" / "A-SC-TEMPLE-COURTYARD-001_cand_001_review.md"
REPORT_PATH = ROOT / "reports" / "PHASE_F6_3_LOCK_SCENE_ASSET_REPORT.md"
SOURCE_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "runs" / "live" / "20260613_144850_A-SC-TEMPLE-COURTYARD-001" / "output" / "A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png"
LOCKED_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "locked_refs" / "A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png"


def _load_asset_registry() -> dict[str, object]:
    payload = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
    for item in payload.get("assets", []):
        if item.get("logical_id") == "A-SC-TEMPLE-COURTYARD-001" and item.get("candidate_id") == "A-SC-TEMPLE-COURTYARD-001_cand_001":
            return item
    raise AssertionError("target candidate asset not found")


def test_14_f6_3_candidate_is_locked_and_reviewed() -> None:
    asset = _load_asset_registry()
    assert asset["status"] == "locked_after_human_review"
    assert asset["review_status"] == "approved"
    assert asset["review_note"].startswith("User-approved")
    assert asset["relative_path"].endswith("locked_refs/A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png")
    assert asset["source_path"].endswith("runs/live/20260613_144850_A-SC-TEMPLE-COURTYARD-001/output/A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png")
    tags = set(asset["tags"])
    assert "production_candidate" in tags
    assert "production_asset" in tags
    assert "locked_ref" in tags
    assert asset["sha256"]
    assert asset["width"] == 2560
    assert asset["height"] == 1440


def test_15_f6_3_locked_copy_matches_source_integrity() -> None:
    assert SOURCE_PATH.exists()
    assert LOCKED_PATH.exists()

    src_sha = hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest()
    dst_sha = hashlib.sha256(LOCKED_PATH.read_bytes()).hexdigest()
    assert src_sha == dst_sha

    with Image.open(SOURCE_PATH) as image:
        assert image.width == 2560
        assert image.height == 1440
        assert image.format == "PNG"
        assert image.width > 0
        assert image.height > 0

    with Image.open(LOCKED_PATH) as image:
        assert image.width == 2560
        assert image.height == 1440
        assert image.format == "PNG"
        assert image.width > 0
        assert image.height > 0

    assert LOCKED_PATH.stat().st_size == SOURCE_PATH.stat().st_size


def test_16_f6_3_review_record_appends_lock_with_paths() -> None:
    lines = [json.loads(item) for item in RECORDS_PATH.read_text(encoding="utf-8").splitlines() if item.strip()]
    sc_records = [
        item
        for item in lines
        if item.get("logical_id") == "A-SC-TEMPLE-COURTYARD-001"
        and item.get("candidate_id") == "A-SC-TEMPLE-COURTYARD-001_cand_001"
    ]
    assert any(
        item.get("decision") == "approve"
        and item.get("logical_id") == "A-SC-TEMPLE-COURTYARD-001"
        and item.get("candidate_id") == "A-SC-TEMPLE-COURTYARD-001_cand_001"
        and item.get("target_status_after_decision") == "locked_after_human_review"
        for item in lines
    )
    assert len(sc_records) >= 1
    latest = sc_records[-1]
    assert latest["target_status_after_decision"] == "locked_after_human_review"
    assert latest["source_path"].endswith("runs/live/20260613_144850_A-SC-TEMPLE-COURTYARD-001/output/A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png")
    assert latest["locked_path"].endswith("locked_refs/A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png")


def test_17_f6_3_review_template_reflects_approval() -> None:
    text = REVIEW_TEMPLATE_PATH.read_text(encoding="utf-8")
    assert "Final decision" in text
    assert "approve" in text.split("Final decision", 1)[1]
    assert "User approved" in text


def test_18_f6_3_report_exists_no_garbled_tokens_and_verdict() -> None:
    text = REPORT_PATH.read_text(encoding="utf-8")
    assert "????" not in text
    assert "false?True" not in text
    assert "PHASE_F6_3_LOCKED_ASSET_ACCEPTED" in text


def test_19_f6_3_live_run_and_external_command_stays_disabled() -> None:
    config = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert config["providers"]["dreamina_cli"]["allow_live_run"] is False
