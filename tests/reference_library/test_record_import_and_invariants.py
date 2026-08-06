from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library import (
    CandidatePackageError,
    ReferenceCatalog,
    UNKNOWN,
    load_candidate_package,
)
from app.ai_video_pipeline.reference_library.record_loader import (
    EXPECTED_PILOT_CLIP_IDS,
)
from app.ai_video_pipeline.reference_library.schema_loader import (
    PACKAGE_BYTES,
    PACKAGE_FILENAME,
    PACKAGE_MEMBER_COUNT,
    PACKAGE_SHA256,
)
from app.ai_video_pipeline.reference_library.validator import (
    EXPECTED_RIGHTS,
    LEGACY_SCORE_FIELDS,
)


FIXTURE = Path(__file__).parent / "fixtures" / PACKAGE_FILENAME


@pytest.fixture(scope="module")
def catalog() -> ReferenceCatalog:
    return ReferenceCatalog.from_package(FIXTURE)


def test_candidate_package_outer_and_inner_binding() -> None:
    raw = FIXTURE.read_bytes()
    assert len(raw) == PACKAGE_BYTES
    assert hashlib.sha256(raw).hexdigest() == PACKAGE_SHA256
    package = load_candidate_package(FIXTURE)
    assert len(package.member_names) == PACKAGE_MEMBER_COUNT
    assert len(package.raw_records) == 30
    assert len(package.schema["required"]) == 16


def test_catalog_fixed_global_invariants(catalog: ReferenceCatalog) -> None:
    summary = catalog.validation.to_dict()
    assert summary == {
        "record_count": 30,
        "unique_id_count": 30,
        "technical_failure_count": 14,
        "current_proxy_file_count": 57,
        "current_proxy_bytes": 267538642,
        "retained_segment_count": 4,
        "retained_segment_bytes": 31831333,
        "current_total_derived_media_bytes": 299369975,
        "clip005_historical_deleted_bytes": 1702329164,
        "legacy_unknown_slots": 198,
        "unknown_to_zero": 0,
        "narrative_reference_extension_count": 1,
        "taxonomy_decision_required_count": 1,
        "validation_status": "PASS",
    }
    assert tuple(record.pilot_clip_id for record in catalog.records) == (
        EXPECTED_PILOT_CLIP_IDS
    )


def test_rights_failures_and_extension_are_kept_separate(
    catalog: ReferenceCatalog,
) -> None:
    assert all(record.rights == EXPECTED_RIGHTS for record in catalog.records)
    failed_artifacts = [
        artifact
        for record in catalog.records
        for artifact in record.artifacts
        if artifact["technical_validation_status"]
        == "PROXY_TECHNICAL_VALIDATION_FAILED"
    ]
    assert len(failed_artifacts) == 14
    extension_records = [
        record
        for record in catalog.records
        if "narrative_reference" in record.reference_duty_extensions
    ]
    assert [record.pilot_clip_id for record in extension_records] == [
        "G01D-CLIP-001"
    ]
    assert (
        extension_records[0].reference_taxonomy_status
        == "TAXONOMY_DECISION_REQUIRED"
    )


def test_all_198_legacy_slots_remain_unknown(catalog: ReferenceCatalog) -> None:
    values: list[object] = []
    for record in catalog.records:
        raw = record.to_dict()
        if (
            raw["field_provenance"]["scores"]
            != "EXPLICIT_UNKNOWN_FROM_LEGACY_BACKFILL"
        ):
            continue
        values.append(raw["review_observation"]["numeric_confidence"])
        values.extend(raw["scores"][field] for field in LEGACY_SCORE_FIELDS)
    assert len(values) == 198
    assert set(values) == {UNKNOWN}
    assert 0 not in values
    assert False not in values


def test_records_and_catalog_copies_are_immutable(catalog: ReferenceCatalog) -> None:
    record = catalog.get("G01D-CLIP-005")
    mutable = record.to_dict()
    mutable["rights"]["publication_allowed"] = "YES"
    assert record.rights["publication_allowed"] == UNKNOWN

    schema = catalog.schema
    schema["required"].clear()
    assert len(catalog.schema["required"]) == 16


def test_package_identity_failure_is_explicit(tmp_path: Path) -> None:
    destination = tmp_path / PACKAGE_FILENAME
    raw = bytearray(FIXTURE.read_bytes())
    raw[-1] ^= 1
    destination.write_bytes(raw)
    with pytest.raises(CandidatePackageError, match="SHA-256 mismatch"):
        load_candidate_package(destination)
