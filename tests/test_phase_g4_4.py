from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

RECORD_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "assets" / "asset_registry.json"
RECORDS_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "review_records.jsonl"
STATUS_PATH = ROOT / "productions" / "chi_yan_tian_qiong" / "PRODUCTION_STATUS.md"
REPORT_PATH = ROOT / "reports" / "PHASE_G4_4_CORE_ASSET_BASELINE_REPORT.md"

ASSETS = [
    {
        "logical_id": "A-SC-TEMPLE-COURTYARD-001",
        "candidate_id": "A-SC-TEMPLE-COURTYARD-001_cand_001",
        "locked_path": ROOT
        / "productions"
        / "chi_yan_tian_qiong"
        / "locked_refs"
        / "A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png",
        "expected_sha256": "f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0",
        "review_md": ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "image_reviews" / "A-SC-TEMPLE-COURTYARD-001_cand_001_review.md",
        "width": 2560,
        "height": 1440,
        "format": "PNG",
    },
    {
        "logical_id": "A-CH-A-SUBJECT-001",
        "candidate_id": "A-CH-A-SUBJECT-001_cand_001",
        "locked_path": ROOT
        / "productions"
        / "chi_yan_tian_qiong"
        / "locked_refs"
        / "A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png",
        "expected_sha256": "83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F",
        "review_md": ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "image_reviews" / "A-CH-A-SUBJECT-001_cand_001_review.md",
        "width": 1440,
        "height": 2560,
        "format": "PNG",
    },
    {
        "logical_id": "A-CH-B-SUBJECT-001",
        "candidate_id": "A-CH-B-SUBJECT-001_cand_001",
        "locked_path": ROOT
        / "productions"
        / "chi_yan_tian_qiong"
        / "locked_refs"
        / "A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png",
        "expected_sha256": "f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a",
        "review_md": ROOT / "productions" / "chi_yan_tian_qiong" / "reviews" / "image_reviews" / "A-CH-B-SUBJECT-001_cand_001_review.md",
        "width": 1440,
        "height": 2560,
        "format": "PNG",
    },
]


def test_01_all_locked_assets_exist_and_integrity() -> None:
    for item in ASSETS:
        path = item["locked_path"]
        assert path.exists()
        data = path.read_bytes()
        assert item["expected_sha256"].lower() == sha256(data).hexdigest()
        with Image.open(path) as image:
            assert image.width == item["width"]
            assert image.height == item["height"]
            assert image.format == item["format"]
        assert path.stat().st_size > 10 * 1024


def _load_registry() -> list[dict]:
    payload = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
    return payload.get("assets", [])


def test_02_all_locked_assets_have_approved_registry_entries() -> None:
    assets = _load_registry()
    for item in ASSETS:
        found = [
            row
            for row in assets
            if row.get("logical_id") == item["logical_id"] and row.get("candidate_id") == item["candidate_id"]
        ]
        assert len(found) == 1
        entry = found[0]
        assert entry["status"] == "locked_after_human_review"
        assert entry["review_status"] == "approved"
        assert str(item["locked_path"].as_posix().replace("\\", "/")).endswith(entry["relative_path"])


def test_03_all_locked_assets_have_review_records() -> None:
    records = [json.loads(item) for item in RECORDS_PATH.read_text(encoding="utf-8").splitlines() if item.strip()]
    for item in ASSETS:
        assert any(
            row.get("logical_id") == item["logical_id"]
            and row.get("candidate_id") == item["candidate_id"]
            and row.get("decision") == "approve"
            and row.get("target_status_after_decision") == "locked_after_human_review"
            for row in records
        )


def test_04_all_locked_assets_have_review_markdown_and_approve_decision() -> None:
    for item in ASSETS:
        text = item["review_md"].read_text(encoding="utf-8")
        assert "Final decision" in text
        assert "- approve" in text


def test_05_production_status_updated() -> None:
    status = STATUS_PATH.read_text(encoding="utf-8")
    assert "core_scene_and_main_subjects_locked" in status
    assert "A-SC-TEMPLE-COURTYARD-001" in status
    assert "A-CH-A-SUBJECT-001" in status
    assert "A-CH-B-SUBJECT-001" in status
    assert "H1 shot-01 keyframe readiness package" in status


def test_06_phase_g4_4_report_has_no_prohibited_strings() -> None:
    report = REPORT_PATH.read_text(encoding="utf-8")
    assert "????" not in report
    assert "false?True" not in report
    assert "PHASE_G4_4_CORE_ASSET_BASELINE_ACCEPTED" in report


def test_07_no_dreamina_execution_evidence() -> None:
    report = REPORT_PATH.read_text(encoding="utf-8")
    assert "C:/Users/msjpurf/bin/dreamina.exe" not in report
    assert "PHASE_G4_4_CORE_ASSET_BASELINE_ACCEPTED" in report
    providers = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert providers["providers"]["dreamina_cli"]["allow_live_run"] is False
