from __future__ import annotations

import json
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index.builder import build_generation
from app.ai_video_pipeline.reference_library.persistent_index.errors import QueryError
from app.ai_video_pipeline.reference_library.persistent_index.exports import (
    export_manifest,
    export_page_json,
    export_rows_jsonl,
)
from app.ai_video_pipeline.reference_library.persistent_index.identity import (
    canonical_json_bytes,
    sha256_hex,
)
from app.ai_video_pipeline.reference_library.persistent_index.query import (
    CURSOR_CONTRACT_VERSION,
    FacetQuery,
    ReadModel,
    SearchQuery,
    _encode_cursor,
)


def test_exact_facets_match_rl_p0_base_records(base_adapter, built_generation):
    family = base_adapter.records[0]["content"]["content_family"]["primary"]
    expected = sorted(
        record["record_identity"]["pilot_clip_id"]
        for record in base_adapter.records
        if record["content"]["content_family"]["primary"] == family
    )
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        page = reader.facet(FacetQuery(content_families=(family,), page_size=200))
    assert [row["pilot_clip_id"] for row in page.rows] == expected
    assert all(row["publication_allowed"] == "UNKNOWN" for row in page.rows)


def test_exact_filter_composition_preserves_rl_p0_semantics(base_adapter, built_generation):
    source = base_adapter.records[0]
    pilot = source["record_identity"]["pilot_clip_id"]
    duty = source["reference_profile"]["reference_duties"][0]
    status = source["artifacts"][0]["technical_validation_status"]
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        page = reader.facet(
            FacetQuery(
                pilot_clip_ids=(pilot,),
                reference_duties=(duty,),
                technical_statuses=(status,),
                publication_allowed="UNKNOWN",
            )
        )
    assert [row["pilot_clip_id"] for row in page.rows] == [pilot]


def test_facet_keyset_pages_concatenate_to_full_order(built_generation):
    seen: list[str] = []
    cursor = None
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        while True:
            page = reader.facet(
                FacetQuery(
                    sort_by="current_total_bytes",
                    page_size=7,
                    cursor=cursor,
                )
            )
            seen.extend(row["pilot_clip_id"] for row in page.rows)
            cursor = page.next_cursor
            if cursor is None:
                break
        full = reader.facet(
            FacetQuery(sort_by="current_total_bytes", page_size=200)
        )
    assert seen == [row["pilot_clip_id"] for row in full.rows]
    assert len(seen) == len(set(seen)) == 30


def test_fts_offset_pagination_and_cursor_binding(tmp_path: Path, ledger_harness):
    for index in range(1, 16):
        ledger_harness.append(
            "REVIEW_OBSERVATION_ADDED",
            pilot_clip_id=f"G01D-CLIP-{index:03d}",
            payload={
                "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
                "statement": "pagedtoken same document length",
            },
        )
    built = build_generation(tmp_path / "state", ledger_harness.mapped())
    with ReadModel.open_generation(built.generation_path) as reader:
        first = reader.search(SearchQuery("pagedtoken", page_size=5))
        second = reader.search(
            SearchQuery("pagedtoken", page_size=5, cursor=first.next_cursor)
        )
        with pytest.raises(QueryError, match="request differs"):
            reader.search(SearchQuery("different", page_size=5, cursor=first.next_cursor))
    assert first.page_offset == 0
    assert second.page_offset == 5
    assert len(first.rows) == len(second.rows) == 5
    assert {row["document_id"] for row in first.rows}.isdisjoint(
        row["document_id"] for row in second.rows
    )


def test_fts_deep_offset_is_bounded(built_generation):
    request = SearchQuery("原神", page_size=5)
    normalized = request.normalized()
    request_hash = sha256_hex(canonical_json_bytes(normalized))
    generation_id = built_generation.verification.metadata["materialization_generation_id"]
    cursor = _encode_cursor(
        {
            "cursor_contract_version": CURSOR_CONTRACT_VERSION,
            "mode": "FTS",
            "materialization_generation_id": generation_id,
            "request_hash": request_hash,
            "next_offset": 10001,
        }
    )
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        with pytest.raises(QueryError, match="bounded offset"):
            reader.search(SearchQuery("原神", page_size=5, cursor=cursor))


def test_deterministic_json_and_jsonl_exports(built_generation):
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        page = reader.facet(FacetQuery(page_size=4))
    first_json = export_page_json(page)
    second_json = export_page_json(page)
    first_jsonl = export_rows_jsonl(page)
    second_jsonl = export_rows_jsonl(page)
    assert first_json == second_json
    assert first_jsonl == second_jsonl
    assert first_json.endswith(b"\n") and not first_json.endswith(b"\n\n")
    assert len(first_jsonl.splitlines()) == 4
    assert all(json.loads(line) for line in first_jsonl.splitlines())
    manifest = export_manifest(first_jsonl, format_name="JSONL", page=page)
    assert manifest["bytes"] == len(first_jsonl)
    assert manifest["sha256"] == sha256_hex(first_jsonl)
    assert manifest["row_count"] == 4


def test_cursor_from_another_generation_is_rejected(tmp_path: Path, ledger_harness):
    first = build_generation(tmp_path / "first", ledger_harness.mapped())
    with ReadModel.open_generation(first.generation_path) as reader:
        page = reader.facet(FacetQuery(page_size=2))
    ledger_harness.append("REVIEW_OBSERVATION_ADDED")
    second = build_generation(tmp_path / "second", ledger_harness.mapped())
    with ReadModel.open_generation(second.generation_path) as reader:
        with pytest.raises(QueryError, match="generation or mode differs"):
            reader.facet(FacetQuery(page_size=2, cursor=page.next_cursor))
