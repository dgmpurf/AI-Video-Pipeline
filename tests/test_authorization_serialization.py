from __future__ import annotations

import base64
import hashlib
import json
import re
from pathlib import Path

import pytest

from app.ai_video_pipeline.governance import authorization_serialization
from app.ai_video_pipeline.governance.authorization_serialization import (
    compile_authorization_bytes,
    compile_authorization_text,
    evaluate_activation_eligibility,
    stable_json_text,
    verify_authorization_bytes,
    verify_authorization_record,
    verify_checkpoint_binding,
)


ROOT = Path(__file__).resolve().parents[1]
AUTH_ROOT = ROOT / "experiments" / "CAL-001" / "authorizations"
R1_REPORT = (
    ROOT
    / "reports"
    / "PHASE_CAL001_P3D_W01_F06_RECOVERY_ONE_QUERY_ONLY_RESULT.md"
)
HISTORICAL_RECORDS = (
    (
        AUTH_ROOT
        / "CAL001_P3D_W01_F06_recovery_one_query_only_reauthorization_R2.json",
        432,
        "0f4306d42084ab96044eea5a89d338e0cf1e41c31e39d8df85b25a15626fe883",
    ),
    (
        AUTH_ROOT
        / "CAL001_P3D_W01_F06_recovery_one_download_only_authorization.json",
        607,
        "e56a37cc5e7f17aaa691ec4e5862fa9253e1a0273221523f9b2a2c172601ff4a",
    ),
    (
        AUTH_ROOT
        / "CAL001_P3D_W01_F06_recovery_review_artifact_creation_authorization.json",
        583,
        "472da91ce12a778f6505844fb52e80a86dd2c1e11cafd469c344cfe08d4df1a1",
    ),
    (
        AUTH_ROOT
        / "CAL001_P3D_W01_F06_recovery_visual_review_record_and_technical_completion_authorization.json",
        1036,
        "e50c231685d549167eeb71ce229e3f61e17ad392da1fc1468aa41d9ccdcb2632",
    ),
)
CHECKPOINT = "a838723b8824a1003b6abab220257d0e20fa31ad"
BOOLEAN_GROUPS = frozenset(
    {
        "utf8_decode_valid",
        "bom_present",
        "cr_present",
        "lf_present",
        "trailing_carriage_return",
        "trailing_newline",
        "trailing_space",
        "markdown_fence_present",
        "decoded_bytes_equal_original",
        "base64_round_trip_verified",
        "decoded_sha256_equal_original",
        "byte_profile_valid",
        "serialization_round_trip_verified",
        "authorization_verified",
    }
)
INTEGER_GROUPS = frozenset(
    {"byte_length", "base64_character_count", "base64_decode_count"}
)
STRING_GROUPS = frozenset(
    {
        "sha256",
        "base64",
        "canonical_text",
        "authority_source",
        "encoding",
        "last_character",
        "last_byte_hex",
        "decoded_sha256",
    }
)
BOOLEAN_ALIAS_CASES = (
    ("utf8_decode_valid", "utf8_decode_valid", True),
    ("bom", "bom_present", False),
    ("bom_present", "bom_present", False),
    ("cr_present", "cr_present", False),
    ("lf_present", "lf_present", False),
    ("trailing_carriage_return", "trailing_carriage_return", False),
    ("trailing_newline", "trailing_newline", False),
    ("trailing_space", "trailing_space", False),
    ("markdown_fence_present", "markdown_fence_present", False),
    ("decoded_bytes_equal_original", "decoded_bytes_equal_original", True),
    ("base64_round_trip_verified", "base64_round_trip_verified", True),
    (
        "decoded_sha256_equal_original",
        "decoded_sha256_equal_original",
        True,
    ),
    ("byte_profile_valid", "byte_profile_valid", True),
    (
        "serialization_round_trip_verified",
        "serialization_round_trip_verified",
        True,
    ),
    ("authorization_verified", "authorization_verified", True),
)
INTEGER_ALIAS_CASES = (
    ("byte_length", "byte_length"),
    ("authorization_byte_length", "byte_length"),
    ("base64_character_count", "base64_character_count"),
    ("derived_base64_character_count", "base64_character_count"),
    ("base64_decode_count", "base64_decode_count"),
    ("locally_generated_base64_decode_count", "base64_decode_count"),
)
STRING_ALIAS_CASES = tuple(
    (alias, group)
    for group, aliases in (
        ("sha256", ("sha256", "authorization_text_sha256")),
        (
            "base64",
            (
                "base64",
                "authorization_base64",
                "locally_derived_base64",
                "locally_generated_base64",
            ),
        ),
        (
            "canonical_text",
            ("canonical_authorization_text", "exact_authorization_text"),
        ),
        ("authority_source", ("authority_source",)),
        ("encoding", ("encoding",)),
        ("last_character", ("last_character",)),
        ("last_byte_hex", ("last_byte_hex",)),
        ("decoded_sha256", ("decoded_sha256",)),
    )
    for alias in aliases
)


def _expected_for(raw: bytes) -> dict[str, object]:
    compiled = compile_authorization_bytes(raw)
    return {
        "byte_length": compiled.byte_length,
        "sha256": compiled.sha256,
        "base64": compiled.base64,
        "base64_character_count": compiled.base64_character_count,
        "base64_decode_count": 1,
        "decoded_bytes_equal_original": True,
        "authorization_verified": True,
    }


def _required_record(raw: bytes) -> dict[str, object]:
    return {
        "byte_length": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def _full_strict_record(raw: bytes) -> dict[str, object]:
    compiled = compile_authorization_bytes(raw)
    return {
        "authority_source": "exact_canonical_text",
        "encoding": "UTF-8",
        "utf8_decode_valid": True,
        "bom": False,
        "cr_present": False,
        "lf_present": False,
        "trailing_carriage_return": False,
        "trailing_newline": False,
        "trailing_space": False,
        "markdown_fence_present": False,
        "byte_length": compiled.byte_length,
        "sha256": compiled.sha256,
        "base64": compiled.base64,
        "base64_character_count": compiled.base64_character_count,
        "base64_decode_count": 1,
        "decoded_bytes_equal_original": True,
        "base64_round_trip_verified": True,
        "decoded_sha256_equal_original": True,
        "last_character": ".",
        "last_byte_hex": "2E",
        "byte_profile_valid": True,
        "serialization_round_trip_verified": True,
        "decoded_sha256": compiled.sha256,
        "canonical_authorization_text": raw.decode("ascii"),
        "authorization_verified": True,
    }


def _assert_failed_without_authority(result: object) -> None:
    assert result.authorization_evidence_verified is False
    assert result.authorization_verified is False
    assert result.eligible_for_authority_activation is False
    assert result.execution_authority_active is False
    assert result.provider_command_allowed is False
    assert result.provider_command_invocation_count == 0
    assert result.authorized_operation_count_consumed == 0


def _canonical_bytes(record: dict[str, object]) -> bytes:
    direct = record.get("canonical_authorization_text")
    if isinstance(direct, str):
        return direct.encode("utf-8")
    nested = record["canonical_authorization"]
    assert isinstance(nested, dict)
    exact_text = nested["exact_authorization_text"]
    assert isinstance(exact_text, str)
    return exact_text.encode("utf-8")


def test_valid_exact_utf8_round_trip_and_stable_json() -> None:
    raw = b"APPROVE_EXACT_BYTES_FINAL_MASTER_FALSE_LOCKED_FALSE."
    result = compile_authorization_bytes(raw)

    assert result.utf8_decode_valid is True
    assert result.byte_profile_valid is True
    assert result.base64_decode_count == 1
    assert result.decoded_bytes_equal_original is True
    assert result.decoded_sha256_equal_original is True
    assert result.serialization_round_trip_verified is True
    assert result.serialization_profile_valid is True
    assert result.authorization_evidence_verified is False
    assert result.authorization_verified is False
    assert result.eligible_for_authority_activation is False
    assert result.execution_authority_active is False
    assert result.provider_command_allowed is False
    assert result.provider_command_invocation_count == 0
    assert result.authorized_operation_count_consumed == 0
    assert stable_json_text(result.to_dict()) == stable_json_text(result.to_dict())


def test_same_length_single_character_mutation_is_rejected() -> None:
    original = b"APPROVE_ALPHA_BETA."
    mutated = b"BPPROVE_ALPHA_BETA."
    assert len(mutated) == len(original)

    result = verify_authorization_bytes(mutated, _expected_for(original))

    assert result.expected_byte_length_matches is True
    assert result.expected_sha256_matches is False
    assert result.authorization_verified is False
    assert result.eligible_for_authority_activation is False


def test_underscore_replaced_by_letter_without_length_change_is_rejected() -> None:
    original = b"APPROVE_ALPHA_BETA."
    mutated = original.replace(b"_", b"X", 1)
    assert len(mutated) == len(original)

    result = verify_authorization_bytes(mutated, _expected_for(original))

    assert result.expected_byte_length_matches is True
    assert result.expected_sha256_matches is False
    assert result.authorization_verified is False


@pytest.mark.parametrize(
    ("contaminated", "expected_error"),
    (
        (b"APPROVE_EXACT.\n", "line_feed_present"),
        (b"APPROVE_EXACT.\r\n", "carriage_return_present"),
        (b"\xef\xbb\xbfAPPROVE_EXACT.", "utf8_bom_present"),
        (b"APPROVE_EXACT. ", "trailing_space_present"),
        (b"```APPROVE_EXACT.```", "markdown_fence_present"),
    ),
)
def test_default_profile_rejects_contamination(
    contaminated: bytes,
    expected_error: str,
) -> None:
    result = compile_authorization_bytes(contaminated)

    assert result.byte_profile_valid is False
    assert result.authorization_verified is False
    assert expected_error in result.validation_errors


def test_supplied_base64_must_decode_to_canonical_bytes() -> None:
    canonical = b"APPROVE_ROUTE_A."
    different = b"APPROVE_ROUTE_B."
    expected = _expected_for(canonical)
    expected["base64"] = base64.b64encode(different).decode("ascii")

    result = verify_authorization_bytes(canonical, expected)

    assert result.expected_sha256_matches is True
    assert result.expected_base64_matches is False
    assert result.expected_base64_decode_count == 1
    assert result.expected_base64_decoded_bytes_equal_original is False
    assert result.expected_base64_decoded_sha256_equal_original is False
    assert result.authorization_verified is False


def test_correct_sha256_does_not_override_incorrect_base64() -> None:
    canonical = b"APPROVE_QUERY_ONCE."
    expected = {
        "authorization_byte_length": len(canonical),
        "authorization_text_sha256": hashlib.sha256(canonical).hexdigest(),
        "locally_derived_base64": base64.b64encode(
            b"APPROVE_QUERY_TWICE"
        ).decode("ascii"),
    }

    result = verify_authorization_bytes(canonical, expected)

    assert result.expected_byte_length_matches is True
    assert result.expected_sha256_matches is True
    assert result.expected_base64_matches is False
    assert result.authorization_verified is False


def test_existing_authorization_base64_alias_is_verified() -> None:
    canonical = b"APPROVE_QUERY_ONCE."
    expected = {
        "authorization_byte_length": len(canonical),
        "authorization_text_sha256": hashlib.sha256(canonical).hexdigest(),
        "authorization_base64": base64.b64encode(canonical).decode("ascii"),
    }

    result = verify_authorization_bytes(canonical, expected)

    assert result.expected_base64_present is True
    assert result.expected_base64_matches is True
    assert result.authorization_verified is True


def test_conflicting_recognized_record_representations_are_rejected() -> None:
    canonical = b"APPROVE_CONFLICT_AUDIT."
    sha256 = hashlib.sha256(canonical).hexdigest()
    encoded = base64.b64encode(canonical).decode("ascii")
    different = base64.b64encode(b"APPROVE_CONFLICT_OTHER.").decode("ascii")
    cases = (
        (
            "base64",
            {
                "byte_length": len(canonical),
                "sha256": sha256,
                "base64": encoded,
                "authorization_base64": different,
            },
        ),
        (
            "base64",
            {
                "byte_length": len(canonical),
                "sha256": sha256,
                "locally_derived_base64": encoded,
                "locally_generated_base64": different,
            },
        ),
        (
            "byte_length",
            {
                "byte_length": len(canonical) + 1,
                "canonical_serialization": {
                    "authorization_byte_length": len(canonical),
                    "authorization_text_sha256": sha256,
                    "locally_derived_base64": encoded,
                },
            },
        ),
        (
            "sha256",
            {
                "sha256": "0" * 64,
                "canonical_serialization": {
                    "authorization_byte_length": len(canonical),
                    "authorization_text_sha256": sha256,
                    "locally_derived_base64": encoded,
                },
            },
        ),
        (
            "canonical_text",
            {
                "byte_length": len(canonical),
                "sha256": sha256,
                "base64": encoded,
                "canonical_authorization_text": canonical.decode("ascii"),
                "exact_authorization_text": "APPROVE_CONFLICT_OTHER.",
            },
        ),
    )

    for conflict_name, record in cases:
        result = verify_authorization_bytes(canonical, record)

        assert result.record_representations_consistent is False
        assert conflict_name in result.record_representation_conflicts
        assert (
            f"record_representation_conflict:{conflict_name}"
            in result.validation_errors
        )
        assert result.authorization_evidence_verified is False
        assert result.authorization_verified is False
        assert result.eligible_for_authority_activation is False


def test_conflicting_nested_verification_fact_is_rejected() -> None:
    canonical = b"APPROVE_NESTED_FACT."
    record = _expected_for(canonical)
    record["decoded_bytes_equal_original"] = False
    record["canonical_serialization"] = {
        "decoded_bytes_equal_original": True,
    }

    result = verify_authorization_bytes(canonical, record)

    assert result.record_representations_consistent is False
    assert "decoded_bytes_equal_original" in result.record_representation_conflicts
    assert result.authorization_evidence_verified is False


def test_matching_duplicate_representations_remain_compatible() -> None:
    canonical = b"APPROVE_MATCHING_ALIASES."
    sha256 = hashlib.sha256(canonical).hexdigest()
    encoded = base64.b64encode(canonical).decode("ascii")
    record = {
        "byte_length": len(canonical),
        "authorization_byte_length": len(canonical),
        "sha256": sha256,
        "authorization_text_sha256": sha256.upper(),
        "base64": encoded,
        "authorization_base64": encoded,
        "canonical_authorization_text": canonical.decode("ascii"),
        "exact_authorization_text": canonical.decode("ascii"),
    }

    result = verify_authorization_bytes(canonical, record)

    assert result.record_representations_consistent is True
    assert result.record_representation_conflicts == ()
    assert result.authorization_evidence_verified is True
    assert result.authorization_verified is True


def test_type_contract_covers_every_recognized_group_and_alias() -> None:
    expected_types = {
        **{name: bool for name in BOOLEAN_GROUPS},
        **{name: int for name in INTEGER_GROUPS},
        **{name: str for name in STRING_GROUPS},
    }
    expected_alias_groups = {
        alias: group for alias, group, _actual in BOOLEAN_ALIAS_CASES
    }
    expected_alias_groups.update(dict(INTEGER_ALIAS_CASES))
    expected_alias_groups.update(dict(STRING_ALIAS_CASES))
    declared_alias_groups = {
        alias: group
        for group, aliases in authorization_serialization._RECORD_REPRESENTATION_GROUPS
        for alias in aliases
    }

    assert authorization_serialization._RECORD_FACT_TYPES == expected_types
    assert declared_alias_groups == expected_alias_groups


@pytest.mark.parametrize(
    ("alias", "group", "actual"),
    BOOLEAN_ALIAS_CASES,
)
def test_boolean_fact_occurrences_reject_integer_values(
    alias: str,
    group: str,
    actual: bool,
) -> None:
    raw = b"APPROVE_STRICT_BOOLEAN_TYPES."
    record = _required_record(raw)
    record[alias] = int(actual)

    result = verify_authorization_bytes(raw, record)

    assert f"record_fact_invalid_type:{group}" in result.validation_errors
    _assert_failed_without_authority(result)


@pytest.mark.parametrize(("alias", "group"), INTEGER_ALIAS_CASES)
@pytest.mark.parametrize("wrong_boolean", (False, True))
def test_integer_fact_occurrences_reject_boolean_values(
    alias: str,
    group: str,
    wrong_boolean: bool,
) -> None:
    raw = b"APPROVE_STRICT_INTEGER_TYPES."
    record = _required_record(raw)
    record["base64"] = base64.b64encode(raw).decode("ascii")
    record[alias] = wrong_boolean

    result = verify_authorization_bytes(raw, record)

    assert f"record_fact_invalid_type:{group}" in result.validation_errors
    _assert_failed_without_authority(result)


@pytest.mark.parametrize(("alias", "group"), STRING_ALIAS_CASES)
def test_string_fact_occurrences_reject_non_string_values(
    alias: str,
    group: str,
) -> None:
    raw = b"APPROVE_STRICT_STRING_TYPES."
    record = _required_record(raw)
    record[alias] = 7

    result = verify_authorization_bytes(raw, record)

    assert f"record_fact_invalid_type:{group}" in result.validation_errors
    _assert_failed_without_authority(result)


def test_identical_malformed_bool_int_duplicates_are_rejected() -> None:
    raw = b"APPROVE_IDENTICAL_MALFORMED_TYPES."
    record = _required_record(raw)
    record["utf8_decode_valid"] = 1
    record["canonical_serialization"] = {"utf8_decode_valid": 1}

    result = verify_authorization_bytes(raw, record)

    assert result.record_representations_consistent is True
    assert "record_fact_invalid_type:utf8_decode_valid" in result.validation_errors
    _assert_failed_without_authority(result)


def test_valid_fact_cannot_hide_malformed_secondary_occurrence() -> None:
    raw = b"APPROVE_MALFORMED_SECONDARY_TYPE."
    record = _required_record(raw)
    record["utf8_decode_valid"] = True
    record["canonical_authorization"] = {"utf8_decode_valid": 1}

    result = verify_authorization_bytes(raw, record)

    assert result.record_representations_consistent is False
    assert "utf8_decode_valid" in result.record_representation_conflicts
    assert "record_fact_invalid_type:utf8_decode_valid" in result.validation_errors
    _assert_failed_without_authority(result)


def test_full_record_with_exact_json_types_remains_valid() -> None:
    raw = b"APPROVE_FULL_STRICT_RECORD."

    result = verify_authorization_bytes(raw, _full_strict_record(raw))

    assert result.validation_errors == ()
    assert result.record_representations_consistent is True
    assert result.authorization_evidence_verified is True
    assert result.authorization_verified is True


@pytest.mark.parametrize(
    "invalid_container",
    ("not-an-object", [], 7, True, None),
    ids=("string", "array", "number", "boolean", "null"),
)
@pytest.mark.parametrize(
    "container_name",
    ("canonical_serialization", "canonical_authorization"),
)
def test_present_nonobject_recognized_container_is_rejected(
    container_name: str,
    invalid_container: object,
) -> None:
    raw = b"APPROVE_CONTAINER_SHAPE."
    record = _required_record(raw)
    record[container_name] = invalid_container

    result = verify_authorization_bytes(raw, record)

    assert (
        f"recognized_container_not_object:{container_name}"
        in result.validation_errors
    )
    _assert_failed_without_authority(result)


@pytest.mark.parametrize(
    "invalid_container",
    ("not-an-object", [], 7, True, None),
    ids=("string", "array", "number", "boolean", "null"),
)
@pytest.mark.parametrize(
    "parent_name",
    ("canonical_serialization", "canonical_authorization"),
)
def test_present_nonobject_nested_verification_container_is_rejected(
    parent_name: str,
    invalid_container: object,
) -> None:
    raw = b"APPROVE_NESTED_CONTAINER_SHAPE."
    record = _required_record(raw)
    record[parent_name] = {"verification": invalid_container}

    result = verify_authorization_bytes(raw, record)

    assert (
        f"recognized_container_not_object:{parent_name}.verification"
        in result.validation_errors
    )
    _assert_failed_without_authority(result)


def test_absent_and_valid_object_optional_containers_remain_compatible() -> None:
    raw = b"APPROVE_OPTIONAL_CONTAINERS."
    absent = verify_authorization_bytes(raw, _required_record(raw))
    record = _required_record(raw)
    record["canonical_serialization"] = {"verification": {}}
    record["canonical_authorization"] = {"verification": {}}
    present = verify_authorization_bytes(raw, record)

    assert absent.authorization_evidence_verified is True
    assert present.authorization_evidence_verified is True
    assert absent.validation_errors == ()
    assert present.validation_errors == ()


def test_base64_count_without_base64_is_a_blocking_error() -> None:
    raw = b"APPROVE_BASE64_COUNT_REQUIRES_BASE64."
    record = _required_record(raw)
    record["base64_character_count"] = len(base64.b64encode(raw))

    result = verify_authorization_bytes(raw, record)

    assert "expected_base64_missing" in result.validation_errors
    _assert_failed_without_authority(result)


@pytest.mark.parametrize(
    ("field", "value", "group"),
    (
        ("authority_source", "human_text", "authority_source"),
        ("encoding", "utf-8", "encoding"),
        ("base64_character_count", -1, "base64_character_count"),
        ("base64_decode_count", 0, "base64_decode_count"),
    ),
)
def test_fact_specific_invalid_values_are_blocking(
    field: str,
    value: object,
    group: str,
) -> None:
    raw = b"APPROVE_FACT_VALUE_VALIDATION."
    record = _required_record(raw)
    record["base64"] = base64.b64encode(raw).decode("ascii")
    record[field] = value

    result = verify_authorization_bytes(raw, record)

    assert f"record_fact_invalid_value:{group}" in result.validation_errors
    _assert_failed_without_authority(result)


def test_valid_hexadecimal_facts_compare_case_insensitively() -> None:
    raw = b"APPROVE_HEXADECIMAL_CASE."
    digest = hashlib.sha256(raw).hexdigest()
    record = {
        "byte_length": len(raw),
        "sha256": digest.upper(),
        "decoded_sha256": digest.upper(),
        "last_byte_hex": "2e",
    }

    result = verify_authorization_bytes(raw, record)

    assert result.validation_errors == ()
    assert result.authorization_evidence_verified is True


@pytest.mark.parametrize(
    ("field", "value", "group"),
    (
        ("sha256", "g" * 64, "sha256"),
        ("sha256", "a" * 63, "sha256"),
        ("sha256", "a" * 65, "sha256"),
        ("decoded_sha256", "g" * 64, "decoded_sha256"),
        ("decoded_sha256", "a" * 63, "decoded_sha256"),
        ("decoded_sha256", "a" * 65, "decoded_sha256"),
    ),
)
def test_invalid_sha256_syntax_is_rejected(
    field: str,
    value: str,
    group: str,
) -> None:
    raw = b"APPROVE_INVALID_SHA_SYNTAX."
    record = _required_record(raw)
    record[field] = value

    result = verify_authorization_bytes(raw, record)

    assert f"record_fact_invalid_value:{group}" in result.validation_errors
    _assert_failed_without_authority(result)


@pytest.mark.parametrize(
    "invalid_value",
    ("GG", "E", "02E", "0x2E", " 2E", "2E "),
)
def test_invalid_last_byte_hex_syntax_is_rejected(invalid_value: str) -> None:
    raw = b"APPROVE_INVALID_LAST_BYTE_HEX."
    record = _required_record(raw)
    record["last_byte_hex"] = invalid_value

    result = verify_authorization_bytes(raw, record)

    assert "record_fact_invalid_value:last_byte_hex" in result.validation_errors
    _assert_failed_without_authority(result)


def test_invalid_utf8_is_a_deterministic_failure() -> None:
    result = compile_authorization_bytes(b"APPROVE_\xff.")

    assert result.utf8_decode_valid is False
    assert result.last_character is None
    assert result.authorization_verified is False
    assert "invalid_utf8" in result.validation_errors


def test_empty_input_is_rejected() -> None:
    result = compile_authorization_bytes(b"")

    assert result.byte_length == 0
    assert result.last_byte_hex is None
    assert result.authorization_verified is False
    assert "empty_input" in result.validation_errors


def test_checkpoint_binding_success_is_eligibility_only() -> None:
    checkpoint = verify_checkpoint_binding(CHECKPOINT, CHECKPOINT, CHECKPOINT)

    assert checkpoint.checkpoint_binding_verified is True
    assert checkpoint.eligible_for_authority_activation is False
    assert checkpoint.execution_authority_active is False
    assert checkpoint.provider_command_allowed is False
    assert checkpoint.provider_command_invocation_count == 0
    assert checkpoint.authorized_operation_count_consumed == 0


def test_local_head_mismatch_requires_reauthorization() -> None:
    other = "b" * 40
    result = verify_checkpoint_binding(CHECKPOINT, other, CHECKPOINT)

    assert result.local_head_matches_required is False
    assert result.checkpoint_binding_verified is False
    assert result.checkpoint_change_requires_reauthorization is True
    assert "local_head_mismatch" in result.validation_errors


def test_origin_main_mismatch_requires_reauthorization() -> None:
    other = "c" * 40
    result = verify_checkpoint_binding(CHECKPOINT, CHECKPOINT, other)

    assert result.origin_main_matches_required is False
    assert result.checkpoint_binding_verified is False
    assert result.checkpoint_change_requires_reauthorization is True
    assert "origin_main_mismatch" in result.validation_errors


def test_checkpoint_change_invalidates_old_binding() -> None:
    changed = "d" * 40
    result = verify_checkpoint_binding(CHECKPOINT, changed, changed)

    assert result.local_head_matches_origin_main is True
    assert result.local_head_matches_required is False
    assert result.origin_main_matches_required is False
    assert result.checkpoint_change_requires_reauthorization is True


def test_failed_verification_consumes_no_authority_or_operation_count() -> None:
    raw = b"APPROVE_ONE_OPERATION."
    failed = verify_authorization_bytes(
        raw,
        {
            "byte_length": len(raw),
            "sha256": "0" * 64,
        },
    )
    eligibility = evaluate_activation_eligibility(failed)

    assert eligibility.eligible_for_authority_activation is False
    assert eligibility.decision == "safe_block"
    assert eligibility.authorization_evidence_verified is False
    assert eligibility.checkpoint_binding_required is True
    assert eligibility.checkpoint_binding_verified is None
    assert "checkpoint_binding_required" in eligibility.validation_errors
    assert eligibility.execution_authority_active is False
    assert eligibility.provider_command_allowed is False
    assert eligibility.provider_command_invocation_count == 0
    assert eligibility.authorized_operation_count_consumed == 0


def test_successful_verification_only_marks_eligibility() -> None:
    raw = b"APPROVE_ONE_OPERATION."
    verified = verify_authorization_bytes(raw, _expected_for(raw))
    checkpoint = verify_checkpoint_binding(CHECKPOINT, CHECKPOINT, CHECKPOINT)
    eligibility = evaluate_activation_eligibility(verified, checkpoint)

    assert verified.authorization_verified is True
    assert verified.authorization_evidence_verified is True
    assert verified.eligible_for_authority_activation is False
    assert eligibility.eligible_for_authority_activation is True
    assert eligibility.decision == "ready"
    assert eligibility.execution_authority_active is False
    assert eligibility.provider_command_allowed is False
    assert eligibility.provider_command_invocation_count == 0
    assert eligibility.authorized_operation_count_consumed == 0


def test_compile_only_cannot_be_activation_eligible() -> None:
    raw = b"APPROVE_COMPILE_ONLY."
    compiled = compile_authorization_bytes(raw)
    checkpoint = verify_checkpoint_binding(CHECKPOINT, CHECKPOINT, CHECKPOINT)

    eligibility = evaluate_activation_eligibility(compiled, checkpoint)

    assert compiled.serialization_profile_valid is True
    assert compiled.authorization_evidence_verified is False
    assert compiled.authorization_verified is False
    assert compiled.eligible_for_authority_activation is False
    assert eligibility.authorization_evidence_verified is False
    assert eligibility.eligible_for_authority_activation is False
    assert eligibility.decision == "safe_block"
    assert (
        "authorization_evidence_verification_required"
        in eligibility.validation_errors
    )


def test_verified_evidence_without_checkpoint_cannot_be_activation_eligible() -> None:
    raw = b"APPROVE_RECORD_WITHOUT_CHECKPOINT."
    verified = verify_authorization_bytes(raw, _expected_for(raw))

    eligibility = evaluate_activation_eligibility(verified)

    assert verified.authorization_evidence_verified is True
    assert verified.eligible_for_authority_activation is False
    assert eligibility.checkpoint_binding_required is True
    assert eligibility.checkpoint_binding_verified is None
    assert eligibility.eligible_for_authority_activation is False
    assert eligibility.decision == "safe_block"
    assert "checkpoint_binding_required" in eligibility.validation_errors


def test_verified_evidence_with_mismatched_checkpoint_is_not_eligible() -> None:
    raw = b"APPROVE_RECORD_WITH_WRONG_CHECKPOINT."
    verified = verify_authorization_bytes(raw, _expected_for(raw))
    mismatched = verify_checkpoint_binding(CHECKPOINT, "f" * 40, CHECKPOINT)

    eligibility = evaluate_activation_eligibility(verified, mismatched)

    assert verified.authorization_evidence_verified is True
    assert mismatched.checkpoint_binding_verified is False
    assert eligibility.authorization_evidence_verified is True
    assert eligibility.checkpoint_binding_verified is False
    assert eligibility.eligible_for_authority_activation is False
    assert eligibility.decision == "safe_block"
    assert "checkpoint_binding_failed" in eligibility.validation_errors


def test_exact_text_is_not_unicode_normalized() -> None:
    composed = compile_authorization_text("APPROVE_\u00e9.")
    decomposed = compile_authorization_text("APPROVE_e\u0301.")

    assert composed.serialization_profile_valid is True
    assert decomposed.serialization_profile_valid is True
    assert composed.authorization_verified is False
    assert decomposed.authorization_verified is False
    assert composed.sha256 != decomposed.sha256
    assert composed.base64 != decomposed.base64
    assert composed.byte_length != decomposed.byte_length


@pytest.mark.parametrize(("record_path", "byte_length", "expected_sha256"), HISTORICAL_RECORDS)
def test_successful_historical_f06_records_reproduce_exact_evidence(
    record_path: Path,
    byte_length: int,
    expected_sha256: str,
) -> None:
    record = json.loads(record_path.read_bytes().decode("utf-8", errors="strict"))
    raw = _canonical_bytes(record)

    compiled = compile_authorization_bytes(raw)
    verified = verify_authorization_record(raw, record)

    assert compiled.byte_length == byte_length
    assert compiled.sha256 == expected_sha256
    assert verified.expected_byte_length_matches is True
    assert verified.expected_sha256_matches is True
    assert verified.expected_base64_matches is True
    assert verified.expected_base64_decoded_bytes_equal_original is True
    assert verified.expected_base64_decoded_sha256_equal_original is True
    assert verified.authorization_verified is True
    assert verified.execution_authority_active is False
    assert verified.provider_command_invocation_count == 0


def test_historical_r1_same_length_base64_mismatch_is_rejected() -> None:
    report = R1_REPORT.read_bytes().decode("utf-8", errors="strict")
    canonical_match = re.search(
        r"The supplied canonical authorization text was:\r?\n\r?\n```text\r?\n([^\r\n]+)\r?\n```",
        report,
    )
    base64_match = re.search(
        r"The supplied Base64 value was:\r?\n\r?\n```text\r?\n([^\r\n]+)\r?\n```",
        report,
    )
    assert canonical_match is not None
    assert base64_match is not None
    canonical = canonical_match.group(1).encode("utf-8")
    supplied_base64 = base64_match.group(1)
    supplied_bytes = base64.b64decode(supplied_base64, validate=True)
    expected = {
        "authorization_byte_length": len(canonical),
        "authorization_text_sha256": hashlib.sha256(canonical).hexdigest(),
        "locally_derived_base64": supplied_base64,
    }

    result = verify_authorization_bytes(canonical, expected)

    assert len(canonical) == 416
    assert len(supplied_bytes) == len(canonical)
    assert supplied_bytes != canonical
    assert hashlib.sha256(canonical).hexdigest() == (
        "2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3"
    )
    assert hashlib.sha256(supplied_bytes).hexdigest() == (
        "f5eb16120e865791f0444a8f0e45cf85aedf141d8f1334c7795196bfb5704b11"
    )
    assert result.expected_byte_length_matches is True
    assert result.expected_sha256_matches is True
    assert result.expected_base64_decoded_bytes_equal_original is False
    assert result.authorization_verified is False
    assert result.eligible_for_authority_activation is False
    assert result.execution_authority_active is False
    assert result.provider_command_allowed is False
    assert result.provider_command_invocation_count == 0
    assert result.authorized_operation_count_consumed == 0
