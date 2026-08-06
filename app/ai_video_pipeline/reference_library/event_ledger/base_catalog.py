from __future__ import annotations

import hashlib
import stat
from pathlib import Path
from typing import Any

from app.ai_video_pipeline.reference_library import ReferenceCatalog

from .canonical import canonical_sha256
from .errors import ManifestValidationError
from .models import BaseCatalogAdapter, BaseCatalogBinding


def _require_regular_file(path: Path) -> None:
    if path.is_symlink() or not path.exists() or not path.is_file():
        raise ManifestValidationError("base package must be a regular file")
    attributes = getattr(path.stat(), "st_file_attributes", 0)
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    if reparse_flag and attributes & reparse_flag:
        raise ManifestValidationError("base package may not be a reparse point")


def load_base_catalog(path: str | Path) -> BaseCatalogAdapter:
    package_path = Path(path)
    _require_regular_file(package_path)
    package_bytes = package_path.stat().st_size
    package_sha256 = hashlib.sha256(package_path.read_bytes()).hexdigest()
    catalog = ReferenceCatalog.from_package(package_path)
    records = tuple(record.to_dict() for record in catalog.records)
    schema_versions = {
        str(record["record_identity"]["schema_version"]) for record in records
    }
    if len(schema_versions) != 1:
        raise ManifestValidationError("base records do not share one schema version")
    catalog_hash_input: dict[str, Any] = {
        "package_filename": package_path.name,
        "package_bytes": package_bytes,
        "package_sha256": package_sha256,
        "record_count": len(records),
        "record_schema_version": next(iter(schema_versions)),
        "records": list(records),
    }
    binding = BaseCatalogBinding(
        package_filename=package_path.name,
        package_bytes=package_bytes,
        package_sha256=package_sha256,
        record_count=len(records),
        record_schema_version=next(iter(schema_versions)),
        base_catalog_hash=canonical_sha256(catalog_hash_input),
    )
    return BaseCatalogAdapter(
        package_path=package_path,
        binding=binding,
        records=records,
        validation=catalog.validation.to_dict(),
    )


def validate_base_binding(
    manifest_binding: dict[str, Any], adapter: BaseCatalogAdapter
) -> None:
    if manifest_binding != adapter.binding.to_dict():
        raise ManifestValidationError("base-catalog identity does not match manifest")
