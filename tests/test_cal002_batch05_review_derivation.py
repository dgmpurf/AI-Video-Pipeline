from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path
from types import ModuleType

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = (
    ROOT
    / "experiments"
    / "CAL-002"
    / "ACTION_CALIBRATION_V1"
    / "BATCH05_DESIGN"
    / "tools"
    / "batch05_review_derivation.py"
)


def _load_tool() -> ModuleType:
    spec = importlib.util.spec_from_file_location("batch05_review_derivation", TOOL_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


tool = _load_tool()


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def _copy_repo_files(repo: Path) -> None:
    paths = (
        tool.BLIND_SCHEMA_RELATIVE_PATH,
        tool.POST_SCHEMA_RELATIVE_PATH,
        tool.DESIGN_MANIFEST_RELATIVE_PATH,
        tool.TASK_MATRIX_RELATIVE_PATH,
        tool.TOOL_RELATIVE_PATH,
    )
    for relative in paths:
        source = ROOT / relative
        target = repo / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def _make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _copy_repo_files(repo)
    _git(repo, "init", "-q")
    _git(repo, "config", "user.name", "CAL002 Test")
    _git(repo, "config", "user.email", "cal002@example.invalid")
    _git(repo, "add", "--all")
    _git(repo, "commit", "-q", "-m", "fixture")
    return repo


def _commit_all(repo: Path, message: str = "fixture update") -> None:
    _git(repo, "add", "--all")
    _git(repo, "commit", "-q", "-m", message)


def _video_review(alias: str) -> dict[str, object]:
    return {
        "action_family": (
            "push_reaction" if alias.startswith("PUSH") else "brief_impact_recoil"
        ),
        "action_family_match": "MATCH",
        "action_onset_visible": "YES",
        "attacker_release_or_retract": "CLEAR",
        "camera_compliance": "PASS",
        "complete_mp4_review_confirmed": True,
        "contact_duration_class": "READABLE",
        "contact_onset_visible": "YES",
        "ending_contract_satisfied": "YES",
        "first_frame_state": "VISIBLY_SEPARATED",
        "foot_result_after_contact": "YES",
        "foot_result_count": 1,
        "foot_result_type": "REAR_FOOT_RECOVERY_PLACEMENT",
        "full_body_visibility": "PASS_ALL_TIMES",
        "identity_consistency": "STABLE",
        "overall_visual_usability": "CALIBRATION_USABLE",
        "post_contact_reaction_visible": "YES",
        "primary_endpoint_result": "PASS",
        "prolonged_contact": "ABSENT",
        "review_alias": alias,
        "static_tail_duration_seconds": 0.25,
        "static_tail_start_time_seconds": 4.5,
        "technical_validity": "PASS",
        "torso_displacement_strength": "READABLE",
        "upper_body_recoil_strength": "READABLE",
    }


def _blind_record() -> dict[str, object]:
    return {
        "schema_version": "CAL002_BATCH05_BLIND_VISUAL_REVIEW_RECORD_V0_3",
        "video_reviews": [_video_review(alias) for alias in tool.VIDEO_ALIASES],
        "pair_reviews": [
            {
                "pair_id": pair_id,
                "comparison_validity": "VALID",
                "preference": "NO_CLEAR_DIFFERENCE",
                "reviewer_rationale": "Complete MP4 reviewed.",
            }
            for pair_id in tool.PAIR_IDS
        ],
    }


def _write_json(path: Path, value: object) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(tool.canonical_json_bytes(value))
    return path


def _blind_path(repo: Path, record: dict[str, object] | None = None) -> Path:
    return _write_json(
        repo / "review" / "batch05_blind_review_record.json",
        record or _blind_record(),
    )


def _schema(repo: Path, relative: str) -> dict[str, object]:
    return json.loads((repo / relative).read_text(encoding="utf-8"))


def _assert_blind_rejected(repo: Path, record: dict[str, object]) -> None:
    with pytest.raises(tool.DerivationError):
        tool.validate_blind_record(
            record,
            _schema(repo, tool.BLIND_SCHEMA_RELATIVE_PATH),
        )


def _derive_to_file(repo: Path, blind: Path) -> tuple[dict[str, object], Path]:
    record = tool.derive_record(repo, blind)
    path = _write_json(repo / "review" / "derived.json", record)
    return record, path


def test_blind_exact_identity_complete_record_passes(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    record = _blind_record()
    assert tool.validate_blind_record(
        record,
        _schema(repo, tool.BLIND_SCHEMA_RELATIVE_PATH),
    ) is record


@pytest.mark.parametrize("mode", ["duplicate", "omitted"])
def test_blind_duplicate_or_omitted_alias_rejected(
    tmp_path: Path,
    mode: str,
) -> None:
    repo = _make_repo(tmp_path)
    record = _blind_record()
    reviews = record["video_reviews"]
    assert isinstance(reviews, list)
    if mode == "duplicate":
        reviews[-1]["review_alias"] = reviews[0]["review_alias"]
    else:
        reviews.pop()
    _assert_blind_rejected(repo, record)


@pytest.mark.parametrize("mode", ["duplicate", "omitted"])
def test_blind_duplicate_or_omitted_pair_rejected(
    tmp_path: Path,
    mode: str,
) -> None:
    repo = _make_repo(tmp_path)
    record = _blind_record()
    reviews = record["pair_reviews"]
    assert isinstance(reviews, list)
    if mode == "duplicate":
        reviews[-1]["pair_id"] = reviews[0]["pair_id"]
    else:
        reviews.pop()
    _assert_blind_rejected(repo, record)


def test_blind_alias_action_family_mismatch_rejected(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    record = _blind_record()
    record["video_reviews"][0]["action_family"] = "brief_impact_recoil"
    _assert_blind_rejected(repo, record)


@pytest.mark.parametrize(
    ("validity", "preference"),
    [
        ("VALID", "NOT_COMPARABLE"),
        ("INVALID_UNCONTROLLED_VARIATION", "A_CLEARLY_BETTER"),
        ("INVALID_TECHNICAL", "B_CLEARLY_BETTER"),
        ("INCONCLUSIVE", "A_CLEARLY_BETTER"),
    ],
)
def test_blind_invalid_validity_preference_combinations_rejected(
    tmp_path: Path,
    validity: str,
    preference: str,
) -> None:
    repo = _make_repo(tmp_path)
    record = _blind_record()
    record["pair_reviews"][0]["comparison_validity"] = validity
    record["pair_reviews"][0]["preference"] = preference
    _assert_blind_rejected(repo, record)


def test_blind_empty_rationale_rejected(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    record = _blind_record()
    record["pair_reviews"][0]["reviewer_rationale"] = ""
    _assert_blind_rejected(repo, record)


@pytest.mark.parametrize(
    (
        "candidate_side",
        "control_side",
        "validity",
        "preference",
        "expected_class",
        "expected_advantage",
    ),
    [
        (
            "A",
            "B",
            "VALID",
            "A_CLEARLY_BETTER",
            "CANDIDATE_CLEAR_ADVANTAGE",
            True,
        ),
        (
            "A",
            "B",
            "VALID",
            "B_CLEARLY_BETTER",
            "CONTROL_CLEAR_ADVANTAGE",
            False,
        ),
        (
            "B",
            "A",
            "VALID",
            "B_CLEARLY_BETTER",
            "CANDIDATE_CLEAR_ADVANTAGE",
            True,
        ),
        (
            "B",
            "A",
            "VALID",
            "A_CLEARLY_BETTER",
            "CONTROL_CLEAR_ADVANTAGE",
            False,
        ),
        (
            "A",
            "B",
            "VALID",
            "NO_CLEAR_DIFFERENCE",
            "NO_CLEAR_ADVANTAGE",
            False,
        ),
        (
            "B",
            "A",
            "INVALID_UNCONTROLLED_VARIATION",
            "NOT_COMPARABLE",
            "INVALID_COMPARISON",
            False,
        ),
        (
            "A",
            "B",
            "INVALID_TECHNICAL",
            "NOT_COMPARABLE",
            "INVALID_COMPARISON",
            False,
        ),
        (
            "A",
            "B",
            "INCONCLUSIVE",
            "NO_CLEAR_DIFFERENCE",
            "INCONCLUSIVE_COMPARISON",
            False,
        ),
        (
            "B",
            "A",
            "INCONCLUSIVE",
            "NOT_COMPARABLE",
            "INCONCLUSIVE_COMPARISON",
            False,
        ),
    ],
)
def test_pair_truth_table_valid_combinations(
    candidate_side: str,
    control_side: str,
    validity: str,
    preference: str,
    expected_class: str,
    expected_advantage: bool,
) -> None:
    result = tool.derive_pair(
        pair_id="PUSH_PAIR_01",
        candidate_side=candidate_side,
        control_side=control_side,
        comparison_validity=validity,
        preference=preference,
    )
    assert result["derivation_class"] == expected_class
    assert result["candidate_clear_advantage"] is expected_advantage


PAIR_CONTRADICTIONS = (
    {
        "candidate_side": "A",
        "control_side": "B",
        "blind_comparison_validity": "VALID",
        "blind_preference": "B_CLEARLY_BETTER",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "candidate_side": "B",
        "control_side": "A",
        "blind_comparison_validity": "VALID",
        "blind_preference": "A_CLEARLY_BETTER",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "candidate_side": "B",
        "control_side": "A",
        "blind_comparison_validity": "VALID",
        "blind_preference": "A_CLEARLY_BETTER",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "blind_comparison_validity": "INVALID_TECHNICAL",
        "blind_preference": "NOT_COMPARABLE",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "blind_comparison_validity": "INVALID_UNCONTROLLED_VARIATION",
        "blind_preference": "NOT_COMPARABLE",
        "derivation_class": "CONTROL_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": False,
    },
    {
        "blind_comparison_validity": "INCONCLUSIVE",
        "blind_preference": "NOT_COMPARABLE",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "candidate_side": "A",
        "control_side": "B",
        "blind_comparison_validity": "VALID",
        "blind_preference": "A_CLEARLY_BETTER",
        "derivation_class": "CONTROL_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": False,
    },
    {
        "candidate_side": "A",
        "control_side": "B",
        "blind_comparison_validity": "VALID",
        "blind_preference": "B_CLEARLY_BETTER",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "blind_comparison_validity": "VALID",
        "blind_preference": "NO_CLEAR_DIFFERENCE",
        "derivation_class": "CANDIDATE_CLEAR_ADVANTAGE",
        "candidate_clear_advantage": True,
    },
    {
        "blind_comparison_validity": "INVALID_TECHNICAL",
        "blind_preference": "A_CLEARLY_BETTER",
        "derivation_class": "INVALID_COMPARISON",
        "candidate_clear_advantage": False,
    },
)


@pytest.mark.parametrize("changes", PAIR_CONTRADICTIONS)
def test_post_schema_rejects_audit_pair_contradictions(
    tmp_path: Path,
    changes: dict[str, object],
) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    record = tool.derive_record(repo, blind)
    record["pair_derivations"][0].update(changes)
    validator = Draft202012Validator(_schema(repo, tool.POST_SCHEMA_RELATIVE_PATH))
    assert not validator.is_valid(record)


def test_changing_blind_values_changes_exact_byte_hash(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    original_hash = hashlib.sha256(blind.read_bytes()).hexdigest()
    record = _blind_record()
    record["pair_reviews"][0]["preference"] = "A_CLEARLY_BETTER"
    _write_json(blind, record)
    assert hashlib.sha256(blind.read_bytes()).hexdigest() != original_hash


def test_old_derived_record_fails_after_blind_substitution(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    _, derived = _derive_to_file(repo, blind)
    changed = _blind_record()
    changed["pair_reviews"][0]["preference"] = "A_CLEARLY_BETTER"
    _write_json(blind, changed)
    with pytest.raises(tool.DerivationError):
        tool.verify_derived_record(repo, blind, derived)


def test_manual_copied_blind_value_change_fails_verify(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    record, derived = _derive_to_file(repo, blind)
    pair = record["pair_derivations"][0]
    pair["blind_preference"] = "B_CLEARLY_BETTER"
    pair["candidate_clear_advantage"] = True
    pair["derivation_class"] = "CANDIDATE_CLEAR_ADVANTAGE"
    _write_json(derived, record)
    with pytest.raises(tool.DerivationError):
        tool.verify_derived_record(repo, blind, derived)


def test_arbitrary_mapping_hash_fails_verify(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    record, derived = _derive_to_file(repo, blind)
    record["mapping_source_bindings"][0]["sha256"] = "0" * 64
    _write_json(derived, record)
    with pytest.raises(tool.DerivationError):
        tool.verify_derived_record(repo, blind, derived)


def test_dirty_worktree_mapping_bytes_fail(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    manifest = repo / tool.DESIGN_MANIFEST_RELATIVE_PATH
    manifest.write_bytes(manifest.read_bytes() + b" ")
    with pytest.raises(tool.DerivationError, match="differs from committed HEAD"):
        tool.derive_record(repo, blind)


def test_manifest_task_matrix_mapping_disagreement_fails(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    manifest_path = repo / tool.DESIGN_MANIFEST_RELATIVE_PATH
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["blind_review_mapping"][0]["task_id"] = (
        "CAL002-B05-PUSH-CONTROL-R01-MISMATCH"
    )
    _write_json(manifest_path, manifest)
    _commit_all(repo)
    with pytest.raises(tool.DerivationError, match="disagreement"):
        tool.derive_record(repo, blind)


@pytest.mark.parametrize("duplicate_field", ["review_alias", "task_id"])
def test_duplicate_alias_or_task_mapping_fails(
    tmp_path: Path,
    duplicate_field: str,
) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    manifest_path = repo / tool.DESIGN_MANIFEST_RELATIVE_PATH
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["blind_review_mapping"][1][duplicate_field] = (
        manifest["blind_review_mapping"][0][duplicate_field]
    )
    _write_json(manifest_path, manifest)
    _commit_all(repo)
    with pytest.raises(tool.DerivationError, match="duplicate"):
        tool.derive_record(repo, blind)


def _family_review(
    primary: str,
    *,
    mismatch: bool = False,
    technical_fail: bool = False,
) -> dict[str, str]:
    return {
        "primary_endpoint_result": primary,
        "action_family_match": "MISMATCH" if mismatch else "MATCH",
        "technical_validity": "FAIL" if technical_fail else "PASS",
    }


def _family_pair(
    derivation_class: str,
    *,
    validity: str = "VALID",
) -> dict[str, str]:
    return {
        "blind_comparison_validity": validity,
        "derivation_class": derivation_class,
    }


@pytest.mark.parametrize(
    ("candidate", "control", "pairs", "expected"),
    [
        (
            ["PASS", "PASS"],
            ["FAIL", "FAIL"],
            ["CANDIDATE_CLEAR_ADVANTAGE", "CANDIDATE_CLEAR_ADVANTAGE"],
            "FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL",
        ),
        (
            ["PASS", "PASS"],
            ["PASS", "PASS"],
            ["NO_CLEAR_ADVANTAGE", "NO_CLEAR_ADVANTAGE"],
            "BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE",
        ),
        (
            ["PASS", "FAIL"],
            ["PASS", "FAIL"],
            ["NO_CLEAR_ADVANTAGE", "INCONCLUSIVE_COMPARISON"],
            "INCONCLUSIVE_REPLICATION",
        ),
        (
            ["FAIL", "FAIL"],
            ["PASS", "PASS"],
            ["CONTROL_CLEAR_ADVANTAGE", "CONTROL_CLEAR_ADVANTAGE"],
            "CANDIDATE_FAMILY_COMPILER_REGRESSION",
        ),
        (
            ["FAIL", "FAIL"],
            ["FAIL", "FAIL"],
            ["NO_CLEAR_ADVANTAGE", "NO_CLEAR_ADVANTAGE"],
            "ROUTE_RESET_REQUIRED",
        ),
    ],
)
def test_each_family_decision_class_has_deterministic_fixture(
    candidate: list[str],
    control: list[str],
    pairs: list[str],
    expected: str,
) -> None:
    mapped = [
        *[("candidate", _family_review(value)) for value in candidate],
        *[("control", _family_review(value)) for value in control],
    ]
    derived_pairs = [_family_pair(value) for value in pairs]
    result = tool.derive_family_decision(
        action_family="push_reaction",
        mapped_video_reviews=mapped,
        pair_derivations=derived_pairs,
    )
    assert result["family_level_result"] == expected


FAMILY_CONTRADICTIONS = (
    {
        "candidate_primary_pass_count": 0,
        "control_primary_pass_count": 2,
        "valid_pair_comparison_count": 0,
        "candidate_clear_advantage_count": 0,
        "family_level_result": "FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL",
    },
    {
        "candidate_primary_pass_count": 1,
        "family_level_result": "FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL",
    },
    {
        "candidate_clear_advantage_count": 1,
        "family_level_result": "FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL",
    },
    {
        "valid_pair_comparison_count": 1,
        "family_level_result": "FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL",
    },
    {
        "candidate_primary_pass_count": 1,
        "family_level_result": (
            "BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE"
        ),
    },
    {
        "candidate_clear_advantage_count": 2,
        "family_level_result": (
            "BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE"
        ),
    },
    {"family_level_result": "CANDIDATE_FAMILY_COMPILER_REGRESSION"},
    {"family_level_result": "ROUTE_RESET_REQUIRED"},
    {"family_level_result": "INCONCLUSIVE_REPLICATION"},
)


@pytest.mark.parametrize("changes", FAMILY_CONTRADICTIONS)
def test_verify_rejects_audit_family_contradictions(
    tmp_path: Path,
    changes: dict[str, object],
) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    record, derived = _derive_to_file(repo, blind)
    record["family_decisions"][0].update(changes)
    assert Draft202012Validator(
        _schema(repo, tool.POST_SCHEMA_RELATIVE_PATH)
    ).is_valid(record)
    _write_json(derived, record)
    with pytest.raises(tool.DerivationError):
        tool.verify_derived_record(repo, blind, derived)


@pytest.mark.parametrize(
    "raw",
    [
        b'{"a": 1, "a": 2}\n',
        b"\xef\xbb\xbf{}\n",
        b'{"value": NaN}\n',
        b"\xff\n",
    ],
)
def test_strict_input_parser_rejects_unsafe_json(raw: bytes) -> None:
    with pytest.raises(tool.DerivationError):
        tool.strict_json_load_bytes(raw, label="probe")


def test_same_inputs_produce_byte_identical_output_and_verify(
    tmp_path: Path,
) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    first = tool.derive_record_bytes(repo, blind)
    second = tool.derive_record_bytes(repo, blind)
    assert first == second
    assert first == tool.canonical_json_bytes(json.loads(first))
    derived = repo / "review" / "derived.json"
    tool.atomic_write(derived, first, overwrite=False)
    assert tool.canonical_json_bytes(
        tool.verify_derived_record(repo, blind, derived)
    ) == first


def test_verify_rejects_one_byte_semantic_mutation(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    record, derived = _derive_to_file(repo, blind)
    record["family_decisions"][0]["decision_rationale"] += "x"
    _write_json(derived, record)
    with pytest.raises(tool.DerivationError):
        tool.verify_derived_record(repo, blind, derived)


def test_cli_derive_verify_and_no_overwrite(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    blind = _blind_path(repo)
    derived = repo / "review" / "cli-derived.json"
    assert tool.main(
        [
            "derive",
            "--repo-root",
            str(repo),
            "--blind-record",
            str(blind),
            "--output",
            str(derived),
        ]
    ) == 0
    assert tool.main(
        [
            "verify",
            "--repo-root",
            str(repo),
            "--blind-record",
            str(blind),
            "--derived-record",
            str(derived),
        ]
    ) == 0
    assert tool.main(
        [
            "derive",
            "--repo-root",
            str(repo),
            "--blind-record",
            str(blind),
            "--output",
            str(derived),
        ]
    ) == 1
