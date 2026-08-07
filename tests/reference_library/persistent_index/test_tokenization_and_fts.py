from __future__ import annotations

import unicodedata
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index.builder import build_generation
from app.ai_video_pipeline.reference_library.persistent_index.enums import SearchScope
from app.ai_video_pipeline.reference_library.persistent_index.errors import QueryError
from app.ai_video_pipeline.reference_library.persistent_index.query import (
    ReadModel,
    SearchQuery,
)
from app.ai_video_pipeline.reference_library.persistent_index.tokenize import (
    GOLDEN_TOKEN_FIXTURES,
    TokenizerIdentity,
    prepare_document,
    prepare_match_query,
    prepared_token_sequence,
)


@pytest.mark.parametrize("text,expected", tuple(GOLDEN_TOKEN_FIXTURES.items()))
def test_tokenizer_golden_fixtures(text, expected):
    assert prepared_token_sequence(text) == expected


def test_tokenizer_identity_binds_actual_unicode_runtime():
    identity = TokenizerIdentity().to_dict()
    assert identity["unicode_runtime_version"] == unicodedata.unidata_version
    assert identity["normalization_form"] == "NFKC"
    assert identity["cjk_strategy"] == "OVERLAPPING_BIGRAM_WITH_SINGLETON_FALLBACK"


@pytest.mark.parametrize(
    "value",
    ("", "   ", "()", 'alpha"beta', "alpha*", "alpha OR beta", "field:value"),
)
def test_query_parser_rejects_empty_raw_or_advanced_fts_syntax(value):
    with pytest.raises(QueryError):
        prepare_match_query(value)


def test_document_and_query_cjk_preparation_are_symmetric():
    assert prepare_document("原神动作") == "原神 神动 动作"
    assert prepare_match_query("原神动作") == '"原神" AND "神动" AND "动作"'
    assert prepare_document("known UNKNOWN value") == "known value"
    assert prepare_match_query("UNKNOWN") == '"unknown"'


def test_current_and_history_fts_are_separate(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    history_marker = "zzrlp2historyonlymarkerq9v7"
    current_marker = "zzrlp2currentmarkerq9v7"
    base_documents = ledger_harness.mapped().table("search_document")
    assert all(
        marker not in str(value)
        for marker in (history_marker, current_marker)
        for row in base_documents
        for value in row
    )
    first = ledger_harness.append(
        "REVIEW_OBSERVATION_ADDED",
        payload={
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": history_marker,
        },
    )
    ledger_harness.append(
        "REVIEW_OBSERVATION_CORRECTED",
        payload={
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": current_marker,
        },
        supersedes=(first.event.event_id,),
    )
    mapped = ledger_harness.mapped()
    built = build_generation(
        tmp_path / "state", mapped, protection_policy=runtime_state_policy
    )
    with ReadModel.open_generation(built.generation_path) as reader:
        current = reader.search(SearchQuery(current_marker, scope=SearchScope.CURRENT))
        old_current = reader.search(
            SearchQuery(history_marker, scope=SearchScope.CURRENT)
        )
        history = reader.search(SearchQuery(history_marker, scope=SearchScope.HISTORY))
    assert [row["source_event_id"] for row in current.rows] == [
        mapped.table("review_observation_history")[1][0]
    ]
    assert old_current.rows == ()
    assert len(history.rows) == 1
    assert history.rows[0]["active_state"] == "HISTORY"


def test_equal_relevance_ties_use_binary_identity_order(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    statement = {
        "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
        "statement": "same deterministic ranking token",
    }
    ledger_harness.append(
        "REVIEW_OBSERVATION_ADDED",
        pilot_clip_id="G01D-CLIP-002",
        payload=statement,
    )
    ledger_harness.append(
        "REVIEW_OBSERVATION_ADDED",
        pilot_clip_id="G01D-CLIP-001",
        payload=statement,
    )
    built = build_generation(
        tmp_path / "state",
        ledger_harness.mapped(),
        protection_policy=runtime_state_policy,
    )
    with ReadModel.open_generation(built.generation_path) as reader:
        page = reader.search(SearchQuery("deterministic ranking token"))
    assert [row["pilot_clip_id"] for row in page.rows] == [
        "G01D-CLIP-001",
        "G01D-CLIP-002",
    ]
    assert all("search_relevance" in row for row in page.rows)
