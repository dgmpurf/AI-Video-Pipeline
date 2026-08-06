from __future__ import annotations

import ast
import zipfile
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library import ReferenceCatalog
from app.ai_video_pipeline.reference_library.cli import FORBIDDEN_OPTIONS, run
from app.ai_video_pipeline.reference_library.schema_loader import (
    PACKAGE_FILENAME,
    load_candidate_package,
)


FIXTURE = Path(__file__).parent / "fixtures" / PACKAGE_FILENAME


@pytest.mark.parametrize("option", FORBIDDEN_OPTIONS)
def test_cli_rejects_write_media_database_provider_and_delete_options(
    option: str,
) -> None:
    with pytest.raises(ValueError, match="forbidden read-only option"):
        run(("--package", str(FIXTURE), "summary", option, "value"))


def test_zip_is_read_in_memory_and_never_extracted(monkeypatch: pytest.MonkeyPatch) -> None:
    def forbidden(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("ZIP extraction is forbidden")

    monkeypatch.setattr(zipfile.ZipFile, "extract", forbidden)
    monkeypatch.setattr(zipfile.ZipFile, "extractall", forbidden)
    package = load_candidate_package(FIXTURE)
    assert len(package.raw_records) == 30


def test_read_only_commands_create_no_files(tmp_path: Path) -> None:
    package = tmp_path / PACKAGE_FILENAME
    package.write_bytes(FIXTURE.read_bytes())
    before = {path.relative_to(tmp_path) for path in tmp_path.rglob("*")}
    run(("--package", str(package), "summary"))
    run(("--package", str(package), "export-jsonl"))
    after = {path.relative_to(tmp_path) for path in tmp_path.rglob("*")}
    assert after == before


def test_runtime_modules_do_not_import_media_database_or_network_clients() -> None:
    package_root = Path(__file__).parents[2] / "app" / "ai_video_pipeline" / (
        "reference_library"
    )
    imported_roots: set[str] = set()
    for path in sorted(package_root.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".", 1)[0])
    assert {
        "sqlite3",
        "requests",
        "urllib",
        "subprocess",
    }.isdisjoint(imported_roots)


def test_catalog_has_no_mutating_api() -> None:
    catalog = ReferenceCatalog.from_package(FIXTURE)
    forbidden_methods = {"add", "delete", "remove", "save", "update", "write"}
    assert forbidden_methods.isdisjoint(dir(catalog))
