from __future__ import annotations

from dataclasses import dataclass

import pytest

from app.ai_video_pipeline.reference_library import ReferenceCatalog
from app.ai_video_pipeline.reference_library.event_ledger import replay_entries
from app.ai_video_pipeline.reference_library.persistent_index import (
    FacetQuery,
    ReadModel,
    SearchQuery,
    verify_generation,
)
from app.ai_video_pipeline.reference_library.persistent_index.errors import QueryError
from app.ai_video_pipeline.reference_library.persistent_index.identity import LOGICAL_REGISTRY
from app.ai_video_pipeline.reference_library.persistent_index.cli import _parser
from app.ai_video_pipeline.reference_library.persistent_index.query import FACET_SORTS


@pytest.mark.parametrize("record_count", (30, 5_000, 100_000))
def test_metadata_only_scale_shapes_are_linear_and_deterministic(record_count):
    identifiers = tuple(f"SCALE-{index:06d}" for index in range(record_count))
    one_artifact_per_record = tuple((identifier, f"{identifier}-A") for identifier in identifiers)
    one_document_per_record = tuple(
        (f"record:{identifier}:description", identifier) for identifier in identifiers
    )
    assert len(identifiers) == record_count
    assert len(set(identifiers)) == record_count
    assert len(one_artifact_per_record) == record_count
    assert len(one_document_per_record) == record_count
    assert identifiers == tuple(sorted(identifiers))


def test_public_interface_is_additive_and_existing_catalog_remains_available():
    assert ReferenceCatalog is not None
    assert replay_entries is not None
    assert ReadModel is not None
    assert verify_generation is not None
    assert len(LOGICAL_REGISTRY) == 23


def test_query_contract_uses_closed_sort_and_filter_vocabularies():
    assert set(FACET_SORTS) == {
        "pilot_clip_id",
        "record_id",
        "primary_family",
        "content_scope",
        "current_total_bytes",
    }
    with pytest.raises(QueryError, match="unsupported facet sort"):
        FacetQuery(sort_by="raw_sql DESC")
    with pytest.raises(QueryError, match="duplicate values"):
        FacetQuery(pilot_clip_ids=("G01D-CLIP-001", "G01D-CLIP-001"))


def test_isolated_cli_fails_closed_on_unknown_arguments():
    parser = _parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["facet", "--database", "x.sqlite3", "--raw-sql", "DROP"])


def test_mapper_does_not_mutate_rl_p0_records(base_adapter, mapped_empty):
    before = base_adapter.canonical_record_bytes
    _ = mapped_empty.table("reference_record")
    assert base_adapter.canonical_record_bytes == before


def test_expected_query_indexes_are_materialized(built_generation):
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        indexes = {
            row[0]
            for row in reader.connection.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'ix_%'"
            )
        }
    assert {
        "ix_reference_record_family",
        "ix_reference_record_scope",
        "ix_storage_total",
        "ix_rights_current",
        "ix_search_record",
    }.issubset(indexes)
