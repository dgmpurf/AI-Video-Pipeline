from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from app.ai_video_pipeline.reference_library import ReferenceCatalog, ReferenceQuery
from app.ai_video_pipeline.reference_library.cli import run
from app.ai_video_pipeline.reference_library.exports import (
    deterministic_json,
    records_to_json,
    records_to_jsonl,
)
from app.ai_video_pipeline.reference_library.schema_loader import PACKAGE_FILENAME


FIXTURE = Path(__file__).parent / "fixtures" / PACKAGE_FILENAME


def test_query_filters_and_default_order_are_deterministic() -> None:
    catalog = ReferenceCatalog.from_package(FIXTURE)
    action = catalog.query(ReferenceQuery(content_families=("action",)))
    assert [record.pilot_clip_id for record in action] == [
        "G01D-CLIP-011",
        "G01D-CLIP-014",
        "G01D-CLIP-016",
    ]

    failed = catalog.query(
        ReferenceQuery(
            technical_validation_statuses=(
                "PROXY_TECHNICAL_VALIDATION_FAILED",
            )
        )
    )
    assert [record.pilot_clip_id for record in failed] == [
        "G01D-CLIP-003",
        "G01D-CLIP-008",
        "G01D-CLIP-014",
        "G01D-CLIP-019",
        "G01D-CLIP-026",
        "G01D-CLIP-027",
        "G01D-CLIP-028",
        "G01D-CLIP-029",
        "G01D-CLIP-030",
    ]

    camera_and_action = catalog.query(
        ReferenceQuery(
            reference_duties=("camera_reference", "action_reference")
        )
    )
    assert all(
        {"camera_reference", "action_reference"}.issubset(
            record.reference_duties
        )
        for record in camera_and_action
    )


def test_json_and_jsonl_exports_are_stable_and_complete() -> None:
    catalog = ReferenceCatalog.from_package(FIXTURE)
    selected = catalog.query(ReferenceQuery(pilot_clip_ids=("G01D-CLIP-005",)))
    first_json = records_to_json(selected)
    second_json = records_to_json(selected)
    assert first_json == second_json
    assert first_json.endswith("\n")
    parsed = json.loads(first_json)
    assert parsed["record_count"] == 1
    assert parsed["records"][0]["record_identity"]["pilot_clip_id"] == (
        "G01D-CLIP-005"
    )

    jsonl = records_to_jsonl(catalog.records)
    lines = jsonl.splitlines()
    assert len(lines) == 30
    assert all(isinstance(json.loads(line), dict) for line in lines)
    assert deterministic_json(catalog.summary()) == deterministic_json(
        catalog.summary()
    )


def test_cli_run_supports_validate_summary_show_and_filter() -> None:
    prefix = ("--package", str(FIXTURE))
    validation = json.loads(run((*prefix, "validate")))
    assert validation["technical_failure_count"] == 14
    summary = json.loads(run((*prefix, "summary")))
    assert summary["record_count"] == 30
    shown = json.loads(run((*prefix, "show", "G01D-CLIP-001")))
    assert shown["record_identity"]["pilot_clip_id"] == "G01D-CLIP-001"
    filtered = json.loads(
        run((*prefix, "list", "--content-family", "action"))
    )
    assert filtered["record_count"] == 3


def test_python_module_entry_point_writes_only_stdout() -> None:
    command = [
        sys.executable,
        "-m",
        "app.ai_video_pipeline.reference_library",
        "--package",
        str(FIXTURE),
        "validate",
    ]
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout)["validation_status"] == "PASS"
    assert completed.stderr == ""
