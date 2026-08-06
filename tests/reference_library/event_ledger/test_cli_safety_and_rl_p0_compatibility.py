from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library import ReferenceCatalog
from app.ai_video_pipeline.reference_library.event_ledger.base_catalog import (
    load_base_catalog,
)
from app.ai_video_pipeline.reference_library.event_ledger.cli import (
    FORBIDDEN_FEATURE_TERMS,
    build_parser,
    main,
    validate_write_target,
)
from app.ai_video_pipeline.reference_library.event_ledger.errors import (
    UnsafeLedgerPathError,
)
from app.ai_video_pipeline.reference_library.event_ledger.registry import (
    EVENT_TYPE_REGISTRY,
)

PROJECT_ROOT = Path(__file__).parents[3]
FIXTURE_PATH = (
    PROJECT_ROOT
    / "tests"
    / "reference_library"
    / "fixtures"
    / "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_CANDIDATE_V0_1.zip"
)


EXPECTED_COMMANDS = {
    "append-event",
    "export-events-json",
    "export-events-jsonl",
    "export-projection-json",
    "init-ledger",
    "list-events",
    "list-projections",
    "replay",
    "show-event",
    "show-projection",
    "summary",
    "validate-ledger",
    "verify-checkpoint",
}


def test_rl_p0_public_catalog_is_reused_without_behavior_change(base_adapter) -> None:
    catalog = ReferenceCatalog.from_package(FIXTURE_PATH)
    assert len(catalog.records) == 30
    assert [record.canonical_json for record in catalog.records] == [
        json.dumps(
            record,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for record in base_adapter.records
    ]
    assert base_adapter.validation == catalog.validation.to_dict()


def test_fixture_identity_is_bound_and_never_modified(base_adapter) -> None:
    before = FIXTURE_PATH.read_bytes()
    assert len(before) == 99429
    assert hashlib.sha256(before).hexdigest() == (
        "83bb0a7597bf4a8700f956e9da5b5249ec9bbc8d1b6ed909c8c0d69b601df622"
    )
    assert base_adapter.binding.package_bytes == 99429
    assert base_adapter.binding.record_count == 30
    assert FIXTURE_PATH.read_bytes() == before


def test_base_package_is_read_in_memory_and_never_extracted(monkeypatch) -> None:
    def forbidden(*_args, **_kwargs):
        raise AssertionError("ZIP extraction is forbidden")

    monkeypatch.setattr(zipfile.ZipFile, "extract", forbidden)
    monkeypatch.setattr(zipfile.ZipFile, "extractall", forbidden)
    assert load_base_catalog(FIXTURE_PATH).binding.record_count == 30


def test_cli_has_exact_separate_command_surface() -> None:
    parser = build_parser()
    subparser_action = next(
        action for action in parser._actions if action.dest == "command"
    )
    assert set(subparser_action.choices) == EXPECTED_COMMANDS
    assert {
        "media",
        "ffprobe",
        "sqlite",
        "provider",
        "dreamina",
        "network",
        "delete",
        "final",
        "lock",
    }.issubset(FORBIDDEN_FEATURE_TERMS)


def test_write_target_must_be_absolute_outside_git_and_runtime(tmp_path: Path) -> None:
    accepted = tmp_path / "ledger"
    assert validate_write_target(accepted) == accepted.resolve()
    with pytest.raises(UnsafeLedgerPathError, match="absolute"):
        validate_write_target(Path("relative-ledger"))
    git_root = tmp_path / "git-root"
    git_root.mkdir()
    (git_root / ".git").write_text("gitdir: synthetic", encoding="utf-8")
    with pytest.raises(UnsafeLedgerPathError, match="Git"):
        validate_write_target(git_root / "ledger")
    runtime = (
        Path(__file__).parents[3]
        / "app"
        / "ai_video_pipeline"
        / "reference_library"
        / "synthetic-ledger"
    )
    with pytest.raises(UnsafeLedgerPathError, match="runtime"):
        validate_write_target(runtime)


def test_cli_init_append_validate_and_export_are_deterministic(
    tmp_path: Path, make_event, capsys
) -> None:
    ledger = tmp_path / "ledger"
    init_args = [
        "init-ledger",
        "--ledger",
        str(ledger),
        "--base-package",
        str(FIXTURE_PATH),
        "--created-by",
        "CODEX_SYNTHETIC_TEST",
        "--created-at",
        "2026-08-07T00:00:00Z",
    ]
    assert main(init_args) == 0
    init_output = capsys.readouterr().out
    assert init_output.endswith("\n") and not init_output.endswith("\n\n")
    assert json.loads(init_output)["initialized"] is True

    event_path = tmp_path / "event.json"
    event_path.write_text(
        json.dumps(make_event(), ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    append_args = [
        "append-event",
        "--ledger",
        str(ledger),
        "--base-package",
        str(FIXTURE_PATH),
        "--event-file",
        str(event_path),
    ]
    assert main(append_args) == 0
    append_output = capsys.readouterr().out
    event_id = json.loads(append_output)["entry"]["event"]["event_id"]

    common = ["--ledger", str(ledger), "--base-package", str(FIXTURE_PATH)]
    assert main(["validate-ledger", *common]) == 0
    assert json.loads(capsys.readouterr().out)["valid"] is True
    assert main(["show-event", *common, "--event-id", event_id]) == 0
    assert json.loads(capsys.readouterr().out)["event_id"] == event_id
    assert main(["export-events-jsonl", *common]) == 0
    jsonl = capsys.readouterr().out
    assert jsonl.endswith("\n") and not jsonl.endswith("\n\n")
    assert json.loads(jsonl)["event_id"] == event_id


def test_runtime_modules_do_not_import_side_effect_capabilities() -> None:
    root = (
        Path(__file__).parents[3]
        / "app"
        / "ai_video_pipeline"
        / "reference_library"
        / "event_ledger"
    )
    combined = "\n".join(path.read_text(encoding="utf-8") for path in root.glob("*.py"))
    for forbidden_import in (
        "import sqlite3",
        "import subprocess",
        "import requests",
        "import urllib",
        "import socket",
        "import dreamina",
        "from dreamina",
        "import ffprobe",
        "from ffprobe",
        "import ffmpeg",
        "from ffmpeg",
    ):
        assert forbidden_import not in combined.lower()


def test_rl_p0_does_not_import_event_ledger() -> None:
    root = Path(__file__).parents[3] / "app" / "ai_video_pipeline" / "reference_library"
    existing = [path for path in root.glob("*.py")]
    assert existing
    for path in existing:
        assert "event_ledger" not in path.read_text(encoding="utf-8")
    assert len(EVENT_TYPE_REGISTRY) == 14
