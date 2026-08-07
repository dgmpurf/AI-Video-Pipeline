from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.persistent_index import builder as builder_module
from app.ai_video_pipeline.reference_library.persistent_index.builder import (
    LOCK_FILENAME,
    RuntimeStateProtectionPolicy,
    build_generation,
    validate_state_root,
)
from app.ai_video_pipeline.reference_library.persistent_index.cli import (
    main as cli_main,
)
from app.ai_video_pipeline.reference_library.persistent_index.errors import UnsafePathError
from app.ai_video_pipeline.reference_library.persistent_index.promotion import (
    POINTER_FILENAME,
    POINTER_TEMP_FILENAME,
)
from app.ai_video_pipeline.reference_library.persistent_index.query import (
    FacetQuery,
    ReadModel,
    SearchQuery,
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def test_unknown_rights_remain_distinct_from_false_zero_and_absent(built_generation):
    with ReadModel.open_generation(built_generation.generation_path) as reader:
        unknown = reader.facet(FacetQuery(publication_allowed="UNKNOWN", page_size=200))
        denied = reader.facet(FacetQuery(publication_allowed="FALSE", page_size=200))
        disabled = reader.facet(
            FacetQuery(generation_input_allowed=False, page_size=200)
        )
    assert len(unknown.rows) == 30
    assert denied.rows == ()
    assert len(disabled.rows) == 30
    assert all(row["publication_allowed"] == "UNKNOWN" for row in unknown.rows)
    assert all(row["generation_input_allowed"] == 0 for row in disabled.rows)


def test_rights_evidence_does_not_create_a_rights_decision(ledger_harness):
    ledger_harness.append("RIGHTS_EVIDENCE_ADDED")
    mapped = ledger_harness.mapped()
    assert len(mapped.table("rights_evidence_history")) == 1
    assert mapped.table("rights_decision_history") == ()
    current = {row[0]: row for row in mapped.table("rights_current")}
    assert current["G01D-CLIP-001"][2:5] == (0, "UNKNOWN", "RL_P0_BASE")


def test_scores_and_proposals_do_not_create_human_or_execution_authority(ledger_harness):
    ledger_harness.append("SCORE_RECORD_ADDED")
    ledger_harness.append("STORAGE_PROPOSAL_ADDED")
    mapped = ledger_harness.mapped()
    assert len(mapped.table("score_record_history")) == 1
    assert len(mapped.table("storage_proposal_history")) == 1
    assert mapped.table("human_decision_history") == ()
    assert mapped.table("execution_receipt_history") == ()


def test_human_decision_and_execution_receipt_remain_separate(ledger_harness):
    proposal = ledger_harness.append("STORAGE_PROPOSAL_ADDED")
    decision = ledger_harness.append(
        "HUMAN_DECISION_RECORDED",
        payload={
            "decision_domain": "storage",
            "decision": "ACCEPT",
            "proposal_event_ids": [proposal.event.event_id],
            "reason": "bounded human decision",
            "authorization_trace_ids": ["AUTH-SYNTHETIC-DECISION-001"],
        },
    )
    mapped_before_receipt = ledger_harness.mapped()
    assert len(mapped_before_receipt.table("human_decision_history")) == 1
    assert mapped_before_receipt.table("execution_receipt_history") == ()
    ledger_harness.append(
        "EXECUTION_AUDIT_RECORDED",
        payload={
            "operation_type": "SYNTHETIC_NOOP",
            "authorization_id": "AUTH-SYNTHETIC-DECISION-001",
            "decision_event_ids": [decision.event.event_id],
            "operation_success": True,
            "before_identity": {"state": "before"},
            "after_identity": {"state": "after"},
            "receipt_trace_ids": ["RECEIPT-SYNTHETIC-002"],
            "external_operation_count": 0,
        },
    )
    mapped = ledger_harness.mapped()
    assert len(mapped.table("human_decision_history")) == 1
    assert len(mapped.table("execution_receipt_history")) == 1
    assert mapped.table("execution_receipt_decision")[0][1] == decision.event.event_id


def test_search_relevance_is_read_only_and_never_changes_authority(
    tmp_path: Path, ledger_harness, runtime_state_policy
):
    marker = "zzrlp2authoritymarkerq9v7"
    base_documents = ledger_harness.mapped().table("search_document")
    assert all(marker not in str(value) for row in base_documents for value in row)
    ledger_harness.append(
        "REVIEW_OBSERVATION_ADDED",
        payload={
            "observation_type": "PLAIN_LANGUAGE_DESCRIPTION",
            "statement": marker,
        },
    )
    built_generation = build_generation(
        tmp_path / "state",
        ledger_harness.mapped(),
        protection_policy=runtime_state_policy,
    )
    before = _sha256(built_generation.generation_path)
    authority_tables = (
        "rights_current",
        "rights_decision_history",
        "human_decision_history",
        "execution_receipt_history",
        "storage_proposal_history",
        "score_record_history",
    )

    def authority_state(reader: ReadModel):
        return {
            table: tuple(
                tuple(row)
                for row in reader.connection.execute(
                    f'SELECT * FROM "{table}" ORDER BY 1'
                )
            )
            for table in authority_tables
        }

    with ReadModel.open_generation(built_generation.generation_path) as reader:
        authority_before = authority_state(reader)
        page = reader.search(SearchQuery(marker))
        authority_after = authority_state(reader)
        rights_before_close = reader.connection.execute(
            "SELECT generation_input_allowed,publication_allowed FROM rights_current "
            "ORDER BY pilot_clip_id"
        ).fetchall()
    after = _sha256(built_generation.generation_path)
    assert page.rows
    assert all("search_relevance" in row for row in page.rows)
    assert authority_before == authority_after
    assert before == after
    assert all(tuple(row) == (0, "UNKNOWN") for row in rights_before_close)


def test_state_root_requires_absolute_external_nonprotected_path(
    tmp_path: Path, mapped_empty
):
    repository = tmp_path / "repository"
    source = tmp_path / "Source"
    media = tmp_path / "media"
    policy = RuntimeStateProtectionPolicy(repository, source, (media,))
    external = tmp_path / "external" / "runtime"

    with pytest.raises(UnsafePathError, match="complete runtime-state protection"):
        build_generation(external, mapped_empty)
    assert not external.exists()

    incomplete = RuntimeStateProtectionPolicy(repository, source, ())
    with pytest.raises(UnsafePathError, match="one or more media roots"):
        build_generation(external, mapped_empty, protection_policy=incomplete)
    assert not external.exists()

    with pytest.raises(UnsafePathError, match="explicit absolute"):
        validate_state_root("relative/state", protection_policy=policy)

    relative_policies = (
        RuntimeStateProtectionPolicy("relative-repository", source, (media,)),
        RuntimeStateProtectionPolicy(repository, "relative-source", (media,)),
        RuntimeStateProtectionPolicy(repository, source, ("relative-media",)),
    )
    for relative_policy in relative_policies:
        with pytest.raises(UnsafePathError, match="explicit absolute"):
            build_generation(
                external,
                mapped_empty,
                protection_policy=relative_policy,
            )
        assert not external.exists()

    for boundary in (repository, source, media):
        for rejected in (boundary, boundary / "runtime"):
            with pytest.raises(UnsafePathError, match="protected boundary"):
                build_generation(
                    rejected,
                    mapped_empty,
                    protection_policy=policy,
                )
            assert not rejected.exists()

    built = build_generation(external, mapped_empty, protection_policy=policy)
    assert built.generation_path.exists()
    assert not (external / LOCK_FILENAME).exists()

    common_cli = ["promote", "--database", str(built.generation_path)]
    role_arguments = {
        "--repository-root": str(repository),
        "--source-root": str(source),
        "--media-root": str(media),
    }
    for missing_role in role_arguments:
        arguments = list(common_cli)
        for role, value in role_arguments.items():
            if role != missing_role:
                arguments.extend((role, value))
        with pytest.raises(SystemExit):
            cli_main(arguments)
        assert not (external / POINTER_FILENAME).exists()
        assert not (external / POINTER_TEMP_FILENAME).exists()

    for relative_role in role_arguments:
        arguments = list(common_cli)
        for role, value in role_arguments.items():
            arguments.extend((role, "relative-protected-root" if role == relative_role else value))
        with pytest.raises(UnsafePathError, match="explicit absolute"):
            cli_main(arguments)
        assert not (external / POINTER_FILENAME).exists()
        assert not (external / POINTER_TEMP_FILENAME).exists()

    duplicate_repository = [
        *common_cli,
        "--repository-root",
        str(repository),
        "--repository-root",
        str(repository),
        "--source-root",
        str(source),
        "--media-root",
        str(media),
    ]
    with pytest.raises(SystemExit):
        cli_main(duplicate_repository)
    assert not (external / POINTER_FILENAME).exists()

    complete_cli = list(common_cli)
    for role, value in role_arguments.items():
        complete_cli.extend((role, value))
    assert cli_main(complete_cli) == 0
    assert (external / POINTER_FILENAME).is_file()
    assert not (external / POINTER_TEMP_FILENAME).exists()


def test_symlink_policy_fails_before_build(
    tmp_path: Path, monkeypatch, mapped_empty, runtime_state_policy
):
    state = tmp_path / "external" / "state"
    state.mkdir(parents=True)
    concrete_path_type = type(state)
    original = concrete_path_type.is_symlink

    def synthetic_symlink(path):
        return path == state or original(path)

    with monkeypatch.context() as context:
        context.setattr(concrete_path_type, "is_symlink", synthetic_symlink)
        with pytest.raises(UnsafePathError, match="symlink"):
            build_generation(
                state,
                mapped_empty,
                protection_policy=runtime_state_policy,
            )
    assert list(state.iterdir()) == []

    with monkeypatch.context() as context:
        context.setattr(
            builder_module,
            "_is_reparse_point",
            lambda path: path == state,
        )
        with pytest.raises(UnsafePathError, match="reparse point"):
            build_generation(
                state,
                mapped_empty,
                protection_policy=runtime_state_policy,
            )
    assert list(state.iterdir()) == []
