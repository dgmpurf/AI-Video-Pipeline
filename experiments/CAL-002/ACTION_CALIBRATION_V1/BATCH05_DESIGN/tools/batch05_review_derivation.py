from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


TOOL_VERSION = "CAL002_BATCH05_REVIEW_DERIVATION_TOOL_V0_1"
TOOL_RELATIVE_PATH = (
    "experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/"
    "tools/batch05_review_derivation.py"
)
BLIND_SCHEMA_RELATIVE_PATH = (
    "experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/"
    "batch05_visual_review_schema.json"
)
POST_SCHEMA_RELATIVE_PATH = (
    "experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/"
    "batch05_post_unblinding_analysis_schema.json"
)
DESIGN_MANIFEST_RELATIVE_PATH = (
    "experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/"
    "batch05_design_manifest.json"
)
TASK_MATRIX_RELATIVE_PATH = (
    "experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/"
    "batch05_task_matrix.csv"
)

VIDEO_ALIASES = (
    "PUSH_PAIR_01_A",
    "PUSH_PAIR_01_B",
    "PUSH_PAIR_02_A",
    "PUSH_PAIR_02_B",
    "IMPACT_PAIR_01_A",
    "IMPACT_PAIR_01_B",
    "IMPACT_PAIR_02_A",
    "IMPACT_PAIR_02_B",
)
PAIR_IDS = (
    "PUSH_PAIR_01",
    "PUSH_PAIR_02",
    "IMPACT_PAIR_01",
    "IMPACT_PAIR_02",
)
ACTION_FAMILIES = ("push_reaction", "brief_impact_recoil")

EXPECTED_MAPPING = {
    "PUSH_PAIR_01_A": {
        "task_id": "CAL002-B05-PUSH-CONTROL-R01",
        "action_family": "push_reaction",
        "treatment": "control",
        "replicate": "R01",
    },
    "PUSH_PAIR_01_B": {
        "task_id": "CAL002-B05-PUSH-CANDIDATE-R01",
        "action_family": "push_reaction",
        "treatment": "candidate",
        "replicate": "R01",
    },
    "PUSH_PAIR_02_A": {
        "task_id": "CAL002-B05-PUSH-CANDIDATE-R02",
        "action_family": "push_reaction",
        "treatment": "candidate",
        "replicate": "R02",
    },
    "PUSH_PAIR_02_B": {
        "task_id": "CAL002-B05-PUSH-CONTROL-R02",
        "action_family": "push_reaction",
        "treatment": "control",
        "replicate": "R02",
    },
    "IMPACT_PAIR_01_A": {
        "task_id": "CAL002-B05-IMPACT-CANDIDATE-R01",
        "action_family": "brief_impact_recoil",
        "treatment": "candidate",
        "replicate": "R01",
    },
    "IMPACT_PAIR_01_B": {
        "task_id": "CAL002-B05-IMPACT-CONTROL-R01",
        "action_family": "brief_impact_recoil",
        "treatment": "control",
        "replicate": "R01",
    },
    "IMPACT_PAIR_02_A": {
        "task_id": "CAL002-B05-IMPACT-CONTROL-R02",
        "action_family": "brief_impact_recoil",
        "treatment": "control",
        "replicate": "R02",
    },
    "IMPACT_PAIR_02_B": {
        "task_id": "CAL002-B05-IMPACT-CANDIDATE-R02",
        "action_family": "brief_impact_recoil",
        "treatment": "candidate",
        "replicate": "R02",
    },
}


class DerivationError(ValueError):
    """Raised when review evidence cannot be deterministically derived."""


class DuplicateJSONKeyError(DerivationError):
    """Raised when strict JSON parsing finds a duplicate object key."""


class NonFiniteJSONError(DerivationError):
    """Raised when strict JSON parsing finds NaN or Infinity."""


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    try:
        text = json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise DerivationError(f"record is not canonical JSON compatible: {exc}") from exc
    return (text + "\n").encode("utf-8")


def _strict_object_pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_nonfinite(token: str) -> None:
    raise NonFiniteJSONError(f"non-finite JSON number: {token}")


def strict_json_load_bytes(
    raw: bytes,
    *,
    label: str,
    require_canonical: bool = True,
) -> Any:
    if raw.startswith(b"\xef\xbb\xbf"):
        raise DerivationError(f"{label}: UTF-8 BOM is forbidden")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise DerivationError(f"{label}: invalid UTF-8") from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=_strict_object_pairs,
            parse_constant=_reject_nonfinite,
        )
    except json.JSONDecodeError as exc:
        raise DerivationError(f"{label}: invalid JSON: {exc}") from exc
    if require_canonical and canonical_json_bytes(value) != raw:
        raise DerivationError(
            f"{label}: JSON must use sorted keys, two-space indentation, "
            "and exactly one terminal LF"
        )
    return value


def strict_json_load_path(path: Path, *, label: str | None = None) -> tuple[Any, bytes]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise DerivationError(f"cannot read {path}: {exc}") from exc
    return strict_json_load_bytes(raw, label=label or str(path)), raw


def _validate_schema_instance(
    instance: Any,
    schema: dict[str, Any],
    *,
    label: str,
) -> None:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        details = "; ".join(
            f"{'/'.join(str(part) for part in error.absolute_path) or '<root>'}: "
            f"{error.message}"
            for error in errors[:8]
        )
        raise DerivationError(f"{label}: schema validation failed: {details}")


def _load_schema(repo_root: Path, relative_path: str) -> dict[str, Any]:
    value, _ = strict_json_load_path(repo_root / relative_path, label=relative_path)
    if not isinstance(value, dict):
        raise DerivationError(f"{relative_path}: schema root must be an object")
    try:
        Draft202012Validator.check_schema(value)
    except Exception as exc:
        raise DerivationError(f"{relative_path}: invalid JSON Schema: {exc}") from exc
    return value


def _repo_relative_path(repo_root: Path, path: Path) -> str:
    resolved_root = repo_root.resolve()
    resolved_path = path.resolve()
    try:
        return resolved_path.relative_to(resolved_root).as_posix()
    except ValueError as exc:
        raise DerivationError("blind review record must be inside the repository") from exc


def _git_head_bytes(repo_root: Path, relative_path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative_path}"],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise DerivationError(
            f"cannot read committed HEAD bytes for {relative_path}: {message}"
        )
    return result.stdout


def _require_committed_worktree_bytes(
    repo_root: Path,
    relative_path: str,
) -> bytes:
    try:
        worktree = (repo_root / relative_path).read_bytes()
    except OSError as exc:
        raise DerivationError(f"cannot read mapping source {relative_path}: {exc}") from exc
    committed = _git_head_bytes(repo_root, relative_path)
    if worktree != committed:
        raise DerivationError(
            f"mapping source differs from committed HEAD bytes: {relative_path}"
        )
    return worktree


def _parse_task_matrix(raw: bytes) -> list[dict[str, str]]:
    if raw.startswith(b"\xef\xbb\xbf"):
        raise DerivationError("task matrix: UTF-8 BOM is forbidden")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise DerivationError("task matrix: invalid UTF-8") from exc
    if "\r" in text or not text.endswith("\n") or text.endswith("\n\n"):
        raise DerivationError("task matrix: expected LF-only text with one terminal LF")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if reader.fieldnames is None or len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise DerivationError("task matrix: missing or duplicate header")
    required = {
        "task_id",
        "action_family",
        "treatment",
        "replicate",
        "review_alias",
    }
    if not required.issubset(reader.fieldnames):
        raise DerivationError("task matrix: required mapping columns are missing")
    rows = list(reader)
    if any(
        key is None or value is None
        for row in rows
        for key, value in row.items()
    ):
        raise DerivationError("task matrix: malformed row")
    return rows


def _validate_mapping_bytes(
    manifest_raw: bytes,
    task_matrix_raw: bytes,
) -> dict[str, dict[str, str]]:
    manifest = strict_json_load_bytes(
        manifest_raw,
        label=DESIGN_MANIFEST_RELATIVE_PATH,
    )
    if not isinstance(manifest, dict):
        raise DerivationError("design manifest must be an object")
    blind_mapping = manifest.get("blind_review_mapping")
    if not isinstance(blind_mapping, list) or len(blind_mapping) != 8:
        raise DerivationError("design manifest must contain exactly eight blind mappings")

    manifest_aliases: list[str] = []
    manifest_tasks: list[str] = []
    manifest_map: dict[str, str] = {}
    for entry in blind_mapping:
        if not isinstance(entry, dict) or set(entry) != {"review_alias", "task_id"}:
            raise DerivationError("design manifest blind mapping has invalid shape")
        alias = entry["review_alias"]
        task_id = entry["task_id"]
        if not isinstance(alias, str) or not isinstance(task_id, str):
            raise DerivationError("design manifest blind mapping values must be strings")
        manifest_aliases.append(alias)
        manifest_tasks.append(task_id)
        manifest_map[alias] = task_id
    if len(set(manifest_aliases)) != 8:
        raise DerivationError("design manifest contains duplicate blind aliases")
    if len(set(manifest_tasks)) != 8:
        raise DerivationError("design manifest contains duplicate task IDs")
    if tuple(manifest_aliases) != VIDEO_ALIASES:
        raise DerivationError("design manifest blind alias order or coverage is invalid")

    rows = _parse_task_matrix(task_matrix_raw)
    if len(rows) != 8:
        raise DerivationError("task matrix must contain exactly eight tasks")
    aliases = [row["review_alias"] for row in rows]
    task_ids = [row["task_id"] for row in rows]
    if len(set(aliases)) != 8:
        raise DerivationError("task matrix contains duplicate blind aliases")
    if len(set(task_ids)) != 8:
        raise DerivationError("task matrix contains duplicate task IDs")
    if set(aliases) != set(VIDEO_ALIASES):
        raise DerivationError("task matrix blind alias coverage is incomplete")

    rows_by_alias = {row["review_alias"]: row for row in rows}
    for alias in VIDEO_ALIASES:
        expected = EXPECTED_MAPPING[alias]
        row = rows_by_alias[alias]
        for field in ("task_id", "action_family", "treatment", "replicate"):
            if row[field] != expected[field]:
                raise DerivationError(
                    f"task matrix {field} disagreement for {alias}: "
                    f"{row[field]!r} != {expected[field]!r}"
                )
        if manifest_map.get(alias) != row["task_id"]:
            raise DerivationError(
                f"manifest/task-matrix mapping disagreement for {alias}"
            )
    return rows_by_alias


def load_verified_mapping(
    repo_root: Path,
) -> tuple[dict[str, dict[str, str]], list[dict[str, Any]]]:
    manifest_raw = _require_committed_worktree_bytes(
        repo_root,
        DESIGN_MANIFEST_RELATIVE_PATH,
    )
    task_matrix_raw = _require_committed_worktree_bytes(
        repo_root,
        TASK_MATRIX_RELATIVE_PATH,
    )
    mapping = _validate_mapping_bytes(manifest_raw, task_matrix_raw)
    bindings = [
        {
            "relative_path": DESIGN_MANIFEST_RELATIVE_PATH,
            "byte_length": len(manifest_raw),
            "sha256": sha256_bytes(manifest_raw),
        },
        {
            "relative_path": TASK_MATRIX_RELATIVE_PATH,
            "byte_length": len(task_matrix_raw),
            "sha256": sha256_bytes(task_matrix_raw),
        },
    ]
    return mapping, bindings


def validate_blind_record(
    record: Any,
    schema: dict[str, Any],
) -> dict[str, Any]:
    if not isinstance(record, dict):
        raise DerivationError("blind review record must be an object")
    _validate_schema_instance(record, schema, label="blind review record")
    aliases = [review["review_alias"] for review in record["video_reviews"]]
    pair_ids = [review["pair_id"] for review in record["pair_reviews"]]
    if tuple(aliases) != VIDEO_ALIASES or len(set(aliases)) != len(VIDEO_ALIASES):
        raise DerivationError("blind review alias order or coverage is invalid")
    if tuple(pair_ids) != PAIR_IDS or len(set(pair_ids)) != len(PAIR_IDS):
        raise DerivationError("blind pair ID order or coverage is invalid")
    return record


def load_blind_record(
    repo_root: Path,
    blind_record_path: Path,
) -> tuple[dict[str, Any], bytes]:
    record, raw = strict_json_load_path(
        blind_record_path,
        label="blind review record",
    )
    schema = _load_schema(repo_root, BLIND_SCHEMA_RELATIVE_PATH)
    return validate_blind_record(record, schema), raw


def derive_pair(
    *,
    pair_id: str,
    candidate_side: str,
    control_side: str,
    comparison_validity: str,
    preference: str,
) -> dict[str, Any]:
    if {candidate_side, control_side} != {"A", "B"}:
        raise DerivationError(f"{pair_id}: Candidate and Control sides must differ")

    candidate_preference = f"{candidate_side}_CLEARLY_BETTER"
    control_preference = f"{control_side}_CLEARLY_BETTER"
    if comparison_validity == "VALID":
        if preference == candidate_preference:
            derivation_class = "CANDIDATE_CLEAR_ADVANTAGE"
            candidate_clear_advantage = True
            rationale = (
                f"VALID: blind preference selects Candidate side {candidate_side}."
            )
        elif preference == control_preference:
            derivation_class = "CONTROL_CLEAR_ADVANTAGE"
            candidate_clear_advantage = False
            rationale = (
                f"VALID: blind preference selects Control side {control_side}."
            )
        elif preference == "NO_CLEAR_DIFFERENCE":
            derivation_class = "NO_CLEAR_ADVANTAGE"
            candidate_clear_advantage = False
            rationale = "VALID: blind review records no clear A/B difference."
        else:
            raise DerivationError(
                f"{pair_id}: VALID comparison has invalid preference {preference}"
            )
    elif comparison_validity in {
        "INVALID_UNCONTROLLED_VARIATION",
        "INVALID_TECHNICAL",
    }:
        if preference != "NOT_COMPARABLE":
            raise DerivationError(
                f"{pair_id}: invalid comparison must be NOT_COMPARABLE"
            )
        derivation_class = "INVALID_COMPARISON"
        candidate_clear_advantage = False
        rationale = f"{comparison_validity}: pair is not comparable."
    elif comparison_validity == "INCONCLUSIVE":
        if preference not in {"NO_CLEAR_DIFFERENCE", "NOT_COMPARABLE"}:
            raise DerivationError(
                f"{pair_id}: INCONCLUSIVE comparison has invalid preference"
            )
        derivation_class = "INCONCLUSIVE_COMPARISON"
        candidate_clear_advantage = False
        rationale = f"INCONCLUSIVE: blind preference is {preference}."
    else:
        raise DerivationError(
            f"{pair_id}: unknown comparison validity {comparison_validity}"
        )

    return {
        "pair_id": pair_id,
        "candidate_side": candidate_side,
        "control_side": control_side,
        "blind_comparison_validity": comparison_validity,
        "blind_preference": preference,
        "candidate_clear_advantage": candidate_clear_advantage,
        "derivation_class": derivation_class,
        "derivation_rationale": rationale,
    }


def _pair_sides(
    pair_id: str,
    mapping: dict[str, dict[str, str]],
) -> tuple[str, str]:
    side_treatment = {
        side: mapping[f"{pair_id}_{side}"]["treatment"] for side in ("A", "B")
    }
    candidate_sides = [
        side for side, treatment in side_treatment.items() if treatment == "candidate"
    ]
    control_sides = [
        side for side, treatment in side_treatment.items() if treatment == "control"
    ]
    if len(candidate_sides) != 1 or len(control_sides) != 1:
        raise DerivationError(f"{pair_id}: invalid Candidate/Control side mapping")
    return candidate_sides[0], control_sides[0]


def derive_pair_records(
    blind_record: dict[str, Any],
    mapping: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    pair_reviews = {
        review["pair_id"]: review for review in blind_record["pair_reviews"]
    }
    derived: list[dict[str, Any]] = []
    for pair_id in PAIR_IDS:
        candidate_side, control_side = _pair_sides(pair_id, mapping)
        review = pair_reviews[pair_id]
        derived.append(
            derive_pair(
                pair_id=pair_id,
                candidate_side=candidate_side,
                control_side=control_side,
                comparison_validity=review["comparison_validity"],
                preference=review["preference"],
            )
        )
    return derived


def derive_family_decision(
    *,
    action_family: str,
    mapped_video_reviews: list[tuple[str, dict[str, Any]]],
    pair_derivations: list[dict[str, Any]],
) -> dict[str, Any]:
    if action_family not in ACTION_FAMILIES:
        raise DerivationError(f"unknown action family: {action_family}")
    candidate_reviews = [
        review for treatment, review in mapped_video_reviews if treatment == "candidate"
    ]
    control_reviews = [
        review for treatment, review in mapped_video_reviews if treatment == "control"
    ]
    if len(candidate_reviews) != 2 or len(control_reviews) != 2:
        raise DerivationError(
            f"{action_family}: expected two Candidate and two Control reviews"
        )
    if len(pair_derivations) != 2:
        raise DerivationError(f"{action_family}: expected two pair derivations")

    candidate_primary_pass_count = sum(
        review["primary_endpoint_result"] == "PASS" for review in candidate_reviews
    )
    control_primary_pass_count = sum(
        review["primary_endpoint_result"] == "PASS" for review in control_reviews
    )
    valid_pair_comparison_count = sum(
        pair["blind_comparison_validity"] == "VALID" for pair in pair_derivations
    )
    candidate_clear_advantage_count = sum(
        pair["derivation_class"] == "CANDIDATE_CLEAR_ADVANTAGE"
        for pair in pair_derivations
    )
    control_clear_advantage_count = sum(
        pair["derivation_class"] == "CONTROL_CLEAR_ADVANTAGE"
        for pair in pair_derivations
    )
    no_clear_advantage_count = sum(
        pair["derivation_class"] == "NO_CLEAR_ADVANTAGE"
        for pair in pair_derivations
    )
    invalid_pair_count = sum(
        pair["derivation_class"] == "INVALID_COMPARISON"
        for pair in pair_derivations
    )
    inconclusive_pair_count = sum(
        pair["derivation_class"] == "INCONCLUSIVE_COMPARISON"
        for pair in pair_derivations
    )
    candidate_action_family_mismatch_count = sum(
        review["action_family_match"] == "MISMATCH" for review in candidate_reviews
    )
    control_action_family_mismatch_count = sum(
        review["action_family_match"] == "MISMATCH" for review in control_reviews
    )
    candidate_technical_invalid_count = sum(
        review["technical_validity"] == "FAIL" for review in candidate_reviews
    )
    control_technical_invalid_count = sum(
        review["technical_validity"] == "FAIL" for review in control_reviews
    )

    both_treatments_frequently_fail = (
        candidate_primary_pass_count == 0 and control_primary_pass_count == 0
    )
    uncontrolled_variation_prevents_comparison = all(
        pair["blind_comparison_validity"] == "INVALID_UNCONTROLLED_VARIATION"
        for pair in pair_derivations
    )
    candidate_repeated_wrong_family = candidate_action_family_mismatch_count == 2
    candidate_worse_than_control = (
        candidate_primary_pass_count < control_primary_pass_count
        or control_clear_advantage_count > candidate_clear_advantage_count
    )

    if (
        both_treatments_frequently_fail
        or uncontrolled_variation_prevents_comparison
    ):
        family_level_result = "ROUTE_RESET_REQUIRED"
        decision_rationale = (
            "Rule 1 ROUTE_RESET_REQUIRED: "
            f"both_treatments_frequently_fail="
            f"{str(both_treatments_frequently_fail).lower()}; "
            f"uncontrolled_variation_prevents_comparison="
            f"{str(uncontrolled_variation_prevents_comparison).lower()}."
        )
    elif candidate_repeated_wrong_family or candidate_worse_than_control:
        family_level_result = "CANDIDATE_FAMILY_COMPILER_REGRESSION"
        decision_rationale = (
            "Rule 2 CANDIDATE_FAMILY_COMPILER_REGRESSION: "
            f"candidate_repeated_wrong_family="
            f"{str(candidate_repeated_wrong_family).lower()}; "
            f"candidate_worse_than_control="
            f"{str(candidate_worse_than_control).lower()}."
        )
    elif (
        candidate_primary_pass_count == 2
        and valid_pair_comparison_count == 2
        and candidate_clear_advantage_count == 2
    ):
        family_level_result = "FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL"
        decision_rationale = (
            "Rule 3 FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL: Candidate "
            "passes 2/2 and has clear advantage in both valid pairs."
        )
    elif (
        candidate_primary_pass_count == 2
        and control_primary_pass_count == 2
        and valid_pair_comparison_count == 2
        and candidate_clear_advantage_count == 0
        and control_clear_advantage_count == 0
        and no_clear_advantage_count == 2
    ):
        family_level_result = (
            "BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE"
        )
        decision_rationale = (
            "Rule 4 BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE: "
            "both treatments pass 2/2 and both valid pairs show no clear "
            "advantage."
        )
    else:
        family_level_result = "INCONCLUSIVE_REPLICATION"
        decision_rationale = (
            "Rule 5 INCONCLUSIVE_REPLICATION: no higher-precedence decision "
            "rule is satisfied."
        )

    return {
        "action_family": action_family,
        "candidate_primary_pass_count": candidate_primary_pass_count,
        "control_primary_pass_count": control_primary_pass_count,
        "valid_pair_comparison_count": valid_pair_comparison_count,
        "candidate_clear_advantage_count": candidate_clear_advantage_count,
        "control_clear_advantage_count": control_clear_advantage_count,
        "no_clear_advantage_count": no_clear_advantage_count,
        "invalid_pair_count": invalid_pair_count,
        "inconclusive_pair_count": inconclusive_pair_count,
        "candidate_action_family_mismatch_count": (
            candidate_action_family_mismatch_count
        ),
        "control_action_family_mismatch_count": control_action_family_mismatch_count,
        "candidate_technical_invalid_count": candidate_technical_invalid_count,
        "control_technical_invalid_count": control_technical_invalid_count,
        "both_treatments_frequently_fail": both_treatments_frequently_fail,
        "uncontrolled_variation_prevents_comparison": (
            uncontrolled_variation_prevents_comparison
        ),
        "candidate_repeated_wrong_family": candidate_repeated_wrong_family,
        "candidate_worse_than_control": candidate_worse_than_control,
        "family_level_result": family_level_result,
        "decision_rationale": decision_rationale,
    }


def derive_family_records(
    blind_record: dict[str, Any],
    mapping: dict[str, dict[str, str]],
    pair_derivations: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    reviews_by_alias = {
        review["review_alias"]: review for review in blind_record["video_reviews"]
    }
    records: list[dict[str, Any]] = []
    for family in ACTION_FAMILIES:
        mapped_reviews = [
            (mapping[alias]["treatment"], reviews_by_alias[alias])
            for alias in VIDEO_ALIASES
            if mapping[alias]["action_family"] == family
        ]
        family_pairs = [
            pair
            for pair in pair_derivations
            if (
                (family == "push_reaction" and pair["pair_id"].startswith("PUSH_"))
                or (
                    family == "brief_impact_recoil"
                    and pair["pair_id"].startswith("IMPACT_")
                )
            )
        ]
        records.append(
            derive_family_decision(
                action_family=family,
                mapped_video_reviews=mapped_reviews,
                pair_derivations=family_pairs,
            )
        )
    return records


def _tool_binding(repo_root: Path) -> dict[str, Any]:
    raw = _require_committed_worktree_bytes(repo_root, TOOL_RELATIVE_PATH)
    return {
        "relative_path": TOOL_RELATIVE_PATH,
        "byte_length": len(raw),
        "sha256": sha256_bytes(raw),
        "tool_version": TOOL_VERSION,
    }


def derive_record(
    repo_root: Path,
    blind_record_path: Path,
) -> dict[str, Any]:
    resolved_root = repo_root.resolve()
    blind_record, blind_raw = load_blind_record(
        resolved_root,
        blind_record_path.resolve(),
    )
    mapping, mapping_bindings = load_verified_mapping(resolved_root)
    pair_derivations = derive_pair_records(blind_record, mapping)
    family_decisions = derive_family_records(
        blind_record,
        mapping,
        pair_derivations,
    )
    record = {
        "schema_version": "CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_2",
        "derivation_tool_binding": _tool_binding(resolved_root),
        "blind_review_record_path": _repo_relative_path(
            resolved_root,
            blind_record_path,
        ),
        "blind_review_record_byte_length": len(blind_raw),
        "blind_review_record_sha256": sha256_bytes(blind_raw),
        "blind_review_record_finalized_before_unblinding": True,
        "mapping_source_bindings": mapping_bindings,
        "pair_derivations": pair_derivations,
        "family_decisions": family_decisions,
    }
    post_schema = _load_schema(resolved_root, POST_SCHEMA_RELATIVE_PATH)
    _validate_schema_instance(
        record,
        post_schema,
        label="post-unblinding derived record",
    )
    return record


def derive_record_bytes(repo_root: Path, blind_record_path: Path) -> bytes:
    return canonical_json_bytes(derive_record(repo_root, blind_record_path))


def verify_derived_record(
    repo_root: Path,
    blind_record_path: Path,
    derived_record_path: Path,
) -> dict[str, Any]:
    supplied, supplied_raw = strict_json_load_path(
        derived_record_path,
        label="post-unblinding derived record",
    )
    if not isinstance(supplied, dict):
        raise DerivationError("post-unblinding derived record must be an object")
    post_schema = _load_schema(repo_root.resolve(), POST_SCHEMA_RELATIVE_PATH)
    _validate_schema_instance(
        supplied,
        post_schema,
        label="post-unblinding derived record",
    )
    expected = derive_record(repo_root.resolve(), blind_record_path.resolve())
    expected_raw = canonical_json_bytes(expected)
    if supplied_raw != expected_raw:
        raise DerivationError(
            "derived record does not byte-match deterministic re-derivation"
        )
    return expected


def _sync_parent_directory(path: Path) -> None:
    flags = os.O_RDONLY
    if hasattr(os, "O_DIRECTORY"):
        flags |= os.O_DIRECTORY
    try:
        fd = os.open(path, flags)
    except OSError:
        return
    try:
        os.fsync(fd)
    except OSError:
        pass
    finally:
        os.close(fd)


def atomic_write(path: Path, raw: bytes, *, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise DerivationError(f"output exists; use --overwrite explicitly: {path}")
    temp_path: Path | None = None
    try:
        fd, temp_name = tempfile.mkstemp(
            prefix=f".{path.name}.",
            suffix=".tmp",
            dir=path.parent,
        )
        temp_path = Path(temp_name)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
        except Exception:
            try:
                os.close(fd)
            except OSError:
                pass
            raise
        if overwrite:
            os.replace(temp_path, path)
        else:
            try:
                os.link(temp_path, path)
            except FileExistsError as exc:
                raise DerivationError(f"output already exists: {path}") from exc
            temp_path.unlink()
            temp_path = None
        _sync_parent_directory(path.parent)
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink()
            except FileNotFoundError:
                pass


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Derive and verify CAL-002 Batch05 review analysis records."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    derive_parser = subparsers.add_parser("derive")
    derive_parser.add_argument("--repo-root", required=True, type=Path)
    derive_parser.add_argument("--blind-record", required=True, type=Path)
    derive_parser.add_argument("--output", required=True, type=Path)
    derive_parser.add_argument("--overwrite", action="store_true")

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("--repo-root", required=True, type=Path)
    verify_parser.add_argument("--blind-record", required=True, type=Path)
    verify_parser.add_argument("--derived-record", required=True, type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command == "derive":
            raw = derive_record_bytes(args.repo_root, args.blind_record)
            atomic_write(args.output, raw, overwrite=args.overwrite)
            receipt = {
                "byte_length": len(raw),
                "mode": "derive",
                "output": str(args.output),
                "sha256": sha256_bytes(raw),
                "tool_version": TOOL_VERSION,
            }
        else:
            verified = verify_derived_record(
                args.repo_root,
                args.blind_record,
                args.derived_record,
            )
            raw = canonical_json_bytes(verified)
            receipt = {
                "byte_length": len(raw),
                "mode": "verify",
                "sha256": sha256_bytes(raw),
                "tool_version": TOOL_VERSION,
                "verified": True,
            }
    except (DerivationError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
