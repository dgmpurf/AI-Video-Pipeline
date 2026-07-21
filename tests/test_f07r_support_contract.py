from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
import stat
from pathlib import Path

import pytest

import app.ai_video_pipeline.execution.f07r_support_contract as support
from app.ai_video_pipeline.execution.f07r_support_contract import (
    DuplicateJSONKeyError,
    ExclusiveClaimExists,
    NonFiniteJSONError,
    StrictJSONError,
    TransitionChainError,
    build_raw_stream_metadata,
    canonical_json_bytes,
    create_append_only_transition,
    create_exclusive_submit_claim,
    strict_json_load_file,
    strict_json_loads,
    validate_all_identifier_occurrences,
    validate_transition_chain,
    validate_zero_charge_prequeue_noncreation,
)


EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
BOUND_SUBMIT_COUNTER_KEY = support.ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY
TRANSITION_SCHEMA_VERSION = "CAL001_F07R_TRANSITION_V1"
EXPERIMENT_ID = "CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1"


def _claim_kwargs(operation_id: str = "submit-001") -> dict[str, object]:
    return {
        "schema_version": "CAL001_F07R_EXCLUSIVE_CLAIM_V1",
        "record_type": "CAL001_F07R_EXCLUSIVE_SUBMIT_CLAIM",
        "experiment_id": EXPERIMENT_ID,
        "operation_id": operation_id,
        "submit_authorized": True,
        "created_at": "2026-07-21T00:00:00Z",
    }


def _anchor_record(
    path: Path,
    *,
    allowance_consumed: bool = False,
    invocation_count: int = 0,
    counters: dict[str, int] | None = None,
) -> Path:
    resolved_counters = dict(counters) if counters is not None else {"submit": invocation_count}
    resolved_counters.setdefault(BOUND_SUBMIT_COUNTER_KEY, invocation_count)
    payload = {
        "schema_version": TRANSITION_SCHEMA_VERSION,
        "record_type": "ANCHOR",
        "experiment_id": EXPERIMENT_ID,
        "route_status_code": "BINDING_CREATED_NOT_AUDITED",
        "route_provider_submit_allowance_consumed": allowance_consumed,
        "route_provider_submit_invocation_count": invocation_count,
        "authority_flags": {"submit_authorized": False},
        "operation_counters": resolved_counters,
    }
    path.write_bytes(canonical_json_bytes(payload))
    return path


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _transition_kwargs(
    previous: Path,
    *,
    sequence: int,
    state: str,
    counters: dict[str, int] | None = None,
    allowance_consumed: bool = True,
    invocation_count: int = 1,
) -> dict[str, object]:
    resolved_counters = (
        dict(counters)
        if counters is not None
        else {"submit": invocation_count, "query": 0}
    )
    resolved_counters.setdefault(BOUND_SUBMIT_COUNTER_KEY, invocation_count)
    return {
        "schema_version": TRANSITION_SCHEMA_VERSION,
        "record_type": "CAL001_F07R_ROUTE_TRANSITION",
        "experiment_id": EXPERIMENT_ID,
        "transition_id": f"transition-{sequence}",
        "sequence_number": sequence,
        "previous_record_path": str(previous.resolve()),
        "previous_record_sha256": _sha(previous) if previous.exists() else "0" * 64,
        "current_state_code": state,
        "transition_reason": f"reason-{sequence}",
        "authority_flags": {
            "submit_authorized": False,
            "query_authorized": False,
            "download_authorized": False,
        },
        "operation_counters": resolved_counters,
        "route_provider_submit_allowance_consumed": allowance_consumed,
        "route_provider_submit_invocation_count": invocation_count,
        "created_at": f"2026-07-21T00:00:0{sequence}Z",
    }


def _write_transition_record(
    path: Path,
    previous: Path,
    *,
    sequence: int,
    previous_sha: str | None = None,
    state: str | None = None,
    allowance_consumed: bool = True,
    invocation_count: int = 1,
    counters: dict[str, int] | None = None,
) -> Path:
    payload = _transition_kwargs(
        previous,
        sequence=sequence,
        state=state or f"STATE_{sequence}",
        counters=counters,
        allowance_consumed=allowance_consumed,
        invocation_count=invocation_count,
    )
    if previous_sha is not None:
        payload["previous_record_sha256"] = previous_sha
    path.write_bytes(canonical_json_bytes(payload))
    return path


def _valid_noncreation_kwargs() -> dict[str, object]:
    handle = "NEW-HANDLE-001"
    sanitized_stdout = f"submit_id={handle}"
    sanitized_stderr = ""
    return {
        "provider_invocation_started": True,
        "submit_allowance_consumed": True,
        "creation_classification": "orphaned_handle_after_prequeue_upload_failure",
        "prequeue_upload_marker": "upload phase, no file upload",
        "new_submit_handle": handle,
        "historical_quarantined_handles": ("OLD-HANDLE-001", "OLD-HANDLE-002"),
        "new_handle_quarantined": True,
        "logid_absent": True,
        "queue_status_evidence_absent": True,
        "provider_task_evidence_absent": True,
        "successful_output_evidence_absent": True,
        "provider_task_created": False,
        "created_task_count": 0,
        "provider_credit_count": None,
        "immediate_pre_credit": 1000,
        "immediate_post_credit": 1000,
        "sanitized_stdout": sanitized_stdout,
        "sanitized_stderr": sanitized_stderr,
        "identifier_result": validate_all_identifier_occurrences(
            sanitized_stdout, sanitized_stderr
        ),
        "evidence_durable": True,
        "evidence_reread_verified": True,
        "query_authorized": False,
        "download_authorized": False,
        "retry_authorized": False,
        "resubmit_authorized": False,
        "batch_authorized": False,
    }


def test_strict_json_canonical_profile_and_round_trip() -> None:
    payload = {"z": 1, "a": ["\u96ea", {"ok": True}]}
    raw = canonical_json_bytes(payload)

    assert raw == b'{\n  "a": [\n    "\\u96ea",\n    {\n      "ok": true\n    }\n  ],\n  "z": 1\n}\n'
    assert strict_json_loads(raw) == payload
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")


def test_strict_json_file_loader_preserves_source_order(tmp_path: Path) -> None:
    path = tmp_path / "ordered.json"
    path.write_bytes(b'{"b":1,"a":2}\n')

    loaded = strict_json_load_file(path)

    assert list(loaded) == ["b", "a"]


def test_strict_json_rejects_duplicate_keys() -> None:
    with pytest.raises(DuplicateJSONKeyError):
        strict_json_loads('{"a":1,"a":2}')


@pytest.mark.parametrize("token", ["NaN", "Infinity", "-Infinity"])
def test_strict_json_rejects_nonfinite_values(token: str) -> None:
    with pytest.raises(NonFiniteJSONError):
        strict_json_loads(f'{{"value":{token}}}')


def test_strict_json_rejects_trailing_data_bom_and_self_hash() -> None:
    with pytest.raises(StrictJSONError):
        strict_json_loads('{"a":1} trailing')
    with pytest.raises(StrictJSONError):
        strict_json_loads(b"\xef\xbb\xbf{}")
    with pytest.raises(StrictJSONError):
        canonical_json_bytes({"self_sha256": "0" * 64})


def test_identifier_stdout_precedes_stderr_globally() -> None:
    result = validate_all_identifier_occurrences(
        "submit_id=SUB-1",
        "logid=LOG-1",
    )
    combined = result["all_submit_id_candidates"] + result["all_logid_candidates"]
    ordered = sorted(combined, key=lambda item: item["discovery_order"])

    assert [item["channel"] for item in ordered] == ["stdout", "stderr"]
    assert [item["discovery_order"] for item in ordered] == [1, 2]


def test_identifier_source_family_order_is_full_line_then_text() -> None:
    channel = '{"submit_id":"S-1","message":"submit_id=S-1;"}'
    result = validate_all_identifier_occurrences(channel, "")

    assert [item["source_kind"] for item in result["all_submit_id_candidates"]] == [
        "full_stream_json",
        "line_json",
        "text_token",
    ]
    assert result["submit_id_consistency_classification"] == "DUPLICATE_EQUAL"


def test_identifier_recursive_dictionary_and_array_preorder() -> None:
    channel = json.dumps(
        {
            "outer": {
                "submit_id": "S-1",
                "items": [{"log_id": "L-1"}, {"submit-id": "S-2"}],
            }
        },
        separators=(",", ":"),
    )
    result = validate_all_identifier_occurrences(channel, "")
    occurrences = sorted(
        result["all_submit_id_candidates"] + result["all_logid_candidates"],
        key=lambda item: item["discovery_order"],
    )

    assert [(item["identifier_type"], item["value"]) for item in occurrences[:3]] == [
        ("submit_id", "S-1"),
        ("logid", "L-1"),
        ("submit_id", "S-2"),
    ]
    assert occurrences[0]["json_path"] == '$["outer"]["submit_id"]'
    assert all(item["character_offset"] >= 0 for item in occurrences)


@pytest.mark.parametrize("key", ["submit_id", "submitid", "submit-id", " SUBMIT_ID "])
def test_identifier_all_structured_submit_key_spellings(key: str) -> None:
    result = validate_all_identifier_occurrences(json.dumps({key: "S-1"}), "")

    assert result["selected_submit_id"] == "S-1"
    assert result["submit_id_consistency_classification"] == "DUPLICATE_EQUAL"


@pytest.mark.parametrize("key", ["logid", "log_id", "log-id", " LOG_ID "])
def test_identifier_all_structured_logid_key_spellings(key: str) -> None:
    result = validate_all_identifier_occurrences(json.dumps({key: "L-1"}), "")

    assert result["selected_logid"] == "L-1"
    assert result["logid_consistency_classification"] == "DUPLICATE_EQUAL"


@pytest.mark.parametrize(
    "text",
    [
        "submit_id=S-1",
        "submit-id:S-1",
        "submitid S-1",
        "'submit_id'=S-1",
        '"submit-id":S-1',
        "SUBMITID\tS-1",
    ],
)
def test_identifier_all_text_submit_forms(text: str) -> None:
    result = validate_all_identifier_occurrences(text, "")

    assert result["selected_submit_id"] == "S-1"
    assert result["submit_id_consistency_classification"] == "UNIQUE"


@pytest.mark.parametrize(
    "text",
    [
        "logid=L-1",
        "log_id:L-1",
        "log-id L-1",
        "'logid'=L-1",
        '"log_id":L-1',
        "LOG-ID\tL-1",
    ],
)
def test_identifier_all_text_logid_forms(text: str) -> None:
    result = validate_all_identifier_occurrences("", text)

    assert result["selected_logid"] == "L-1"
    assert result["logid_consistency_classification"] == "UNIQUE"


def test_identifier_allowed_token_characters_and_integer_values() -> None:
    text_result = validate_all_identifier_occurrences("submit_id=Az09._:-", "")
    json_result = validate_all_identifier_occurrences('{"logid":42}', "")

    assert text_result["selected_submit_id"] == "Az09._:-"
    assert json_result["selected_logid"] == "42"


def test_identifier_malformed_text_token_is_rejected() -> None:
    result = validate_all_identifier_occurrences("submit_id=bad/value", "")

    assert result["all_submit_id_candidates"] == []
    assert result["submit_id_consistency_classification"] == "MISSING"


def test_identifier_missing_unique_duplicate_equal_and_conflicting() -> None:
    missing = validate_all_identifier_occurrences("nothing", "")
    unique = validate_all_identifier_occurrences("submit_id=S-1", "")
    duplicate = validate_all_identifier_occurrences("submit_id=S-1; submit_id=S-1", "")
    conflict = validate_all_identifier_occurrences("submit_id=S-1; submit_id=S-2", "")

    assert missing["submit_id_consistency_classification"] == "MISSING"
    assert unique["submit_id_consistency_classification"] == "UNIQUE"
    assert duplicate["submit_id_consistency_classification"] == "DUPLICATE_EQUAL"
    assert conflict["submit_id_consistency_classification"] == "CONFLICTING"
    assert conflict["selected_submit_id"] is None


def test_identifier_cross_source_conflict_cannot_be_hidden() -> None:
    channel = '{"submit_id":"S-JSON","message":"submit_id=S-TEXT;"}'
    result = validate_all_identifier_occurrences(channel, "")

    assert {item["value"] for item in result["all_submit_id_candidates"]} == {
        "S-JSON",
        "S-TEXT",
    }
    assert result["submit_id_consistency_classification"] == "CONFLICTING"
    assert result["contradictory_identifiers_present"] is True


def test_identifier_cross_channel_conflict_cannot_be_hidden() -> None:
    result = validate_all_identifier_occurrences("submit_id=S-OUT", "submit_id=S-ERR")

    assert result["submit_id_consistency_classification"] == "CONFLICTING"
    assert result["selected_submit_id"] is None


def test_identifier_duplicate_equal_occurrences_are_preserved() -> None:
    result = validate_all_identifier_occurrences('{"submit_id":"S-1"}', "")

    assert len(result["all_submit_id_candidates"]) == 2
    assert [item["source_kind"] for item in result["all_submit_id_candidates"]] == [
        "full_stream_json",
        "line_json",
    ]


def test_identifier_duplicate_json_key_safe_blocks_both_lists() -> None:
    result = validate_all_identifier_occurrences('{"submit_id":"S-1","submit_id":"S-2"}', "")

    assert result["contradictory_identifiers_present"] is True
    assert result["submit_id_consistency_classification"] == "CONFLICTING"
    assert result["logid_consistency_classification"] == "CONFLICTING"
    assert {item["error_code"] for item in result["strict_frame_errors"]} == {
        "duplicate_json_key"
    }


def test_identifier_nonfinite_json_safe_blocks() -> None:
    result = validate_all_identifier_occurrences('{"submit_id":"S-1","value":NaN}', "")

    assert result["contradictory_identifiers_present"] is True
    assert result["submit_id_consistency_classification"] == "CONFLICTING"
    assert {item["error_code"] for item in result["strict_frame_errors"]} == {
        "nonfinite_json_value"
    }


def test_identifier_nested_conflicting_ids_safe_block() -> None:
    result = validate_all_identifier_occurrences(
        '{"submit_id":"S-1","nested":{"submit-id":"S-2"}}',
        "",
    )

    assert result["submit_id_consistency_classification"] == "CONFLICTING"
    assert result["selected_submit_id"] is None


@pytest.mark.parametrize("invalid_value", [True, None, [], {}, "", "bad/value"])
def test_identifier_structured_invalid_values_safe_block(invalid_value: object) -> None:
    result = validate_all_identifier_occurrences(json.dumps({"submit_id": invalid_value}), "")

    assert result["submit_id_consistency_classification"] == "CONFLICTING"
    assert result["contradictory_identifiers_present"] is True
    assert all(
        item["error_code"] == "invalid_structured_identifier_value"
        for item in result["strict_frame_errors"]
    )


def test_identifier_text_key_boundaries_exclude_longer_identifiers() -> None:
    result = validate_all_identifier_occurrences(
        "xsubmit_id=A submit_idx=B submit_id=C submit_idd=D",
        "",
    )

    assert [item["value"] for item in result["all_submit_id_candidates"]] == ["C"]


def test_identifier_line_frames_keep_line_and_offset_evidence() -> None:
    result = validate_all_identifier_occurrences(
        "noise\n  {\"submit_id\":\"S-1\"}\n",
        "",
    )
    json_candidates = [
        item for item in result["all_submit_id_candidates"] if item["source_kind"] == "line_json"
    ]

    assert len(json_candidates) == 1
    assert json_candidates[0]["line_number"] == 2
    assert json_candidates[0]["frame_index"] == 2
    assert json_candidates[0]["character_offset"] > len("noise\n")


def test_identifier_line_framing_uses_only_crlf_cr_and_lf() -> None:
    result = validate_all_identifier_occurrences(
        "noise\r{\"submit_id\":\"S-1\"}\u2028{\"logid\":\"L-1\"}",
        "",
    )

    assert len(
        [item for item in result["all_submit_id_candidates"] if item["source_kind"] == "line_json"]
    ) == 0
    assert result["all_logid_candidates"] == []


def test_raw_metadata_empty_streams_use_empty_hash() -> None:
    result = build_raw_stream_metadata(b"", b"")

    assert result["raw_stdout_byte_count"] == 0
    assert result["raw_stderr_byte_count"] == 0
    assert result["raw_stdout_sha256"] == EMPTY_SHA256
    assert result["raw_stderr_sha256"] == EMPTY_SHA256
    assert result["stdout_utf8_replacement_count"] == 0
    assert result["stderr_utf8_replacement_count"] == 0


def test_raw_metadata_ordinary_utf8_and_separate_hashes() -> None:
    stdout = "stdout snow \u96ea".encode()
    stderr = b"stderr"
    result = build_raw_stream_metadata(stdout, stderr)

    assert result["raw_stdout_byte_count"] == len(stdout)
    assert result["raw_stderr_byte_count"] == len(stderr)
    assert result["raw_stdout_sha256"] == hashlib.sha256(stdout).hexdigest()
    assert result["raw_stderr_sha256"] == hashlib.sha256(stderr).hexdigest()
    assert result["sanitized_stdout"] == stdout.decode()
    assert result["sanitized_stderr"] == "stderr"


def test_raw_metadata_undecodable_binary_uses_replacement_decoding() -> None:
    stdout = b"A\xffB\xf0\x9f"
    result = build_raw_stream_metadata(stdout, b"\x80")

    assert result["sanitized_stdout"] == stdout.decode("utf-8", errors="replace")
    assert result["sanitized_stderr"] == "\ufffd"
    assert result["stdout_utf8_replacement_count"] == 2
    assert result["stderr_utf8_replacement_count"] == 1


def test_raw_metadata_literal_replacement_character_is_not_decode_error() -> None:
    raw = "literal \ufffd".encode("utf-8")
    result = build_raw_stream_metadata(raw, b"")

    assert result["sanitized_stdout"] == "literal \ufffd"
    assert result["stdout_utf8_replacement_count"] == 0


def test_raw_metadata_reuses_sanitization_and_removes_sensitive_values() -> None:
    stdout = (
        "prompt: private scene\n"
        "access_token=TOKEN-123\n"
        "session=SESSION-123\n"
        "https://example.test/file?signature=secret\n"
        "custom=CUSTOM-SECRET"
    ).encode()
    stderr = b"Cookie: SID=COOKIE-123\nAuthorization: Bearer BEARER-123"
    result = build_raw_stream_metadata(
        stdout,
        stderr,
        secret_values=("CUSTOM-SECRET",),
    )
    serialized = json.dumps(result, sort_keys=True)

    for secret in (
        "private scene",
        "TOKEN-123",
        "SESSION-123",
        "signature=secret",
        "CUSTOM-SECRET",
        "COOKIE-123",
        "BEARER-123",
    ):
        assert secret not in serialized
    assert "<redacted" in serialized


def test_raw_metadata_redacts_whitespace_separated_sensitive_fields() -> None:
    raw = (
        "prompt private scene\n"
        "token TOKEN-SPACE\n"
        "session SESSION-SPACE\n"
        "cookie COOKIE-SPACE\n"
        "authorization Bearer AUTH-SPACE"
    ).encode()

    result = build_raw_stream_metadata(raw, b"")
    serialized = json.dumps(result)

    for secret in (
        "private scene",
        "TOKEN-SPACE",
        "SESSION-SPACE",
        "COOKIE-SPACE",
        "AUTH-SPACE",
    ):
        assert secret not in serialized


def test_raw_metadata_sanitized_hashes_cover_sanitized_utf8() -> None:
    result = build_raw_stream_metadata(b"submit_id=S-1", b"logid=L-1")

    assert result["sanitized_stdout_sha256"] == hashlib.sha256(
        result["sanitized_stdout"].encode("utf-8")
    ).hexdigest()
    assert result["sanitized_stderr_sha256"] == hashlib.sha256(
        result["sanitized_stderr"].encode("utf-8")
    ).hexdigest()


def test_raw_metadata_contains_no_raw_or_reversible_content() -> None:
    raw = b"\x00\xffPRIVATE-BYTES"
    result = build_raw_stream_metadata(raw, b"", secret_values=("PRIVATE-BYTES",))

    assert result["raw_content_persisted"] is False
    assert not any(isinstance(value, bytes) for value in result.values())
    assert "PRIVATE-BYTES" not in json.dumps(result)
    assert "\u0000" not in json.dumps(result)
    assert set(result) == {
        "raw_stdout_byte_count",
        "raw_stdout_sha256",
        "raw_stderr_byte_count",
        "raw_stderr_sha256",
        "stdout_decoding",
        "stderr_decoding",
        "stdout_utf8_replacement_count",
        "stderr_utf8_replacement_count",
        "sanitized_stdout",
        "sanitized_stdout_sha256",
        "sanitized_stderr",
        "sanitized_stderr_sha256",
        "raw_content_persisted",
    }


def test_noncreation_full_conjunction_proves_noncreation() -> None:
    result = validate_zero_charge_prequeue_noncreation(**_valid_noncreation_kwargs())

    assert result == {
        "provider_task_noncreation_proven": True,
        "provider_task_creation_proven": False,
        "failed_prerequisites": [],
        "route_status_code": "CLOSED_PREQUEUE_UPLOAD_FAILURE",
        "route_closed": True,
        "allowance_consumed": True,
        "second_submit_permitted": False,
        "query_authorized": False,
        "download_authorized": False,
        "retry_authorized": False,
        "resubmit_authorized": False,
        "batch_authorized": False,
    }


@pytest.mark.parametrize(
    ("field", "bad_value", "expected_failure"),
    [
        ("provider_invocation_started", False, "provider_invocation_started"),
        ("submit_allowance_consumed", False, "submit_allowance_consumed"),
        ("creation_classification", "other", "creation_classification"),
        ("prequeue_upload_marker", "similar marker", "recognized_prequeue_upload_marker"),
        ("new_submit_handle", "", "new_submit_handle_nonempty"),
        ("new_handle_quarantined", False, "new_handle_quarantined"),
        ("logid_absent", False, "logid_absent"),
        ("queue_status_evidence_absent", False, "queue_status_evidence_absent"),
        ("provider_task_evidence_absent", False, "provider_task_evidence_absent"),
        ("successful_output_evidence_absent", False, "successful_output_evidence_absent"),
        ("provider_task_created", None, "provider_task_created_exact_false"),
        ("created_task_count", 1, "created_task_count_zero"),
        ("provider_credit_count", 1, "provider_credit_count_absent_or_zero"),
        ("provider_credit_count", "zero", "provider_credit_count_absent_or_zero"),
        ("immediate_post_credit", 999, "immediate_credit_delta_zero"),
        ("immediate_post_credit", "unknown", "immediate_credits_numeric"),
        ("evidence_durable", False, "evidence_durable"),
        ("evidence_reread_verified", False, "evidence_reread_verified"),
    ],
)
def test_noncreation_each_scalar_prerequisite_fails_closed(
    field: str,
    bad_value: object,
    expected_failure: str,
) -> None:
    values = _valid_noncreation_kwargs()
    values[field] = bad_value

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["provider_task_creation_proven"] is False
    assert result["second_submit_permitted"] is False
    assert expected_failure in result["failed_prerequisites"]


def test_noncreation_historical_handle_collision_fails() -> None:
    values = _valid_noncreation_kwargs()
    values["new_submit_handle"] = "OLD-HANDLE-001"
    values["sanitized_stdout"] = "submit_id=OLD-HANDLE-001"
    values["identifier_result"] = validate_all_identifier_occurrences(
        "submit_id=OLD-HANDLE-001", ""
    )

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert "new_handle_distinct" in result["failed_prerequisites"]


def test_noncreation_logid_or_identifier_conflict_fails() -> None:
    values = _valid_noncreation_kwargs()
    values["sanitized_stdout"] = "submit_id=NEW-HANDLE-001 logid=L-1"
    values["sanitized_stderr"] = "submit_id=OTHER-HANDLE"
    values["identifier_result"] = validate_all_identifier_occurrences(
        values["sanitized_stdout"],
        values["sanitized_stderr"],
    )

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert "identifier_no_contradiction" in result["failed_prerequisites"]
    assert "selected_submit_matches" in result["failed_prerequisites"]
    assert "selected_logid_absent" in result["failed_prerequisites"]
    assert "logid_classification_missing" in result["failed_prerequisites"]


def test_noncreation_selected_submit_mismatch_fails() -> None:
    values = _valid_noncreation_kwargs()
    values["sanitized_stdout"] = "submit_id=OTHER-HANDLE"
    values["identifier_result"] = validate_all_identifier_occurrences(
        "submit_id=OTHER-HANDLE", ""
    )

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert "selected_submit_matches" in result["failed_prerequisites"]


@pytest.mark.parametrize(
    "historical_handles",
    [None, "AB", (), ("ONLY-ONE",), ("SAME", "SAME"), (1, 2)],
)
def test_noncreation_malformed_historical_handles_return_failed_result(
    historical_handles: object,
) -> None:
    values = _valid_noncreation_kwargs()
    values["historical_quarantined_handles"] = historical_handles

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "historical_quarantined_handles_exact" in result["failed_prerequisites"]


def test_noncreation_internal_derivation_passes_without_external_result() -> None:
    values = _valid_noncreation_kwargs()
    del values["identifier_result"]

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is True
    assert result["failed_prerequisites"] == []


def test_noncreation_exact_external_deep_copy_passes() -> None:
    values = _valid_noncreation_kwargs()
    values["identifier_result"] = json.loads(json.dumps(values["identifier_result"]))

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is True
    assert result["failed_prerequisites"] == []


def test_noncreation_exact_external_canonical_round_trip_passes() -> None:
    values = _valid_noncreation_kwargs()
    values["identifier_result"] = strict_json_loads(
        canonical_json_bytes(values["identifier_result"])
    )

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is True
    assert result["failed_prerequisites"] == []


def test_noncreation_malformed_external_identifier_result_fails_comparison() -> None:
    values = _valid_noncreation_kwargs()
    values["identifier_result"] = []

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


@pytest.mark.parametrize("field_action", ["missing", "unexpected"])
def test_noncreation_rejects_identifier_result_field_set_changes(
    field_action: str,
) -> None:
    values = _valid_noncreation_kwargs()
    identifier_result = dict(values["identifier_result"])
    if field_action == "missing":
        del identifier_result["all_logid_candidates"]
    else:
        identifier_result["unexpected"] = False
    values["identifier_result"] = identifier_result

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


def test_noncreation_rejects_identifier_classification_mismatch() -> None:
    values = _valid_noncreation_kwargs()
    identifier_result = dict(values["identifier_result"])
    identifier_result["submit_id_consistency_classification"] = "MISSING"
    values["identifier_result"] = identifier_result

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


def test_noncreation_rejects_missing_candidates_with_selected_identifier() -> None:
    values = _valid_noncreation_kwargs()
    identifier_result = dict(values["identifier_result"])
    identifier_result["all_submit_id_candidates"] = []
    values["identifier_result"] = identifier_result

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


def test_noncreation_rejects_frame_error_hidden_by_false_contradiction() -> None:
    values = _valid_noncreation_kwargs()
    identifier_result = dict(values["identifier_result"])
    unsafe = validate_all_identifier_occurrences(
        '{"submit_id":"A","submit_id":"B"}',
        "",
    )
    identifier_result["strict_frame_errors"] = [unsafe["strict_frame_errors"][0]]
    identifier_result["contradictory_identifiers_present"] = False
    values["identifier_result"] = identifier_result

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("identifier_type", "logid"),
        ("value", " BAD-HANDLE "),
        ("channel", "combined"),
        ("source_kind", "unknown"),
        ("frame_index", -1),
        ("line_number", -1),
        ("character_offset", -1),
        ("json_path", "$"),
        ("discovery_order", 0),
    ],
)
def test_noncreation_rejects_malformed_identifier_occurrence(
    field: str,
    bad_value: object,
) -> None:
    values = _valid_noncreation_kwargs()
    identifier_result = json.loads(json.dumps(values["identifier_result"]))
    identifier_result["all_submit_id_candidates"][0][field] = bad_value
    values["identifier_result"] = identifier_result

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


def test_noncreation_rejects_duplicate_global_discovery_order() -> None:
    values = _valid_noncreation_kwargs()
    identifier_result = validate_all_identifier_occurrences(
        "submit_id=NEW-HANDLE-001 submit_id=NEW-HANDLE-001",
        "",
    )
    identifier_result["all_submit_id_candidates"][1]["discovery_order"] = 1
    values["identifier_result"] = identifier_result

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("sanitized_stdout", None),
        ("sanitized_stdout", b"submit_id=NEW-HANDLE-001"),
        ("sanitized_stderr", None),
        ("sanitized_stderr", b""),
    ],
)
def test_noncreation_invalid_sanitized_stream_pair_fails_closed(
    field: str,
    bad_value: object,
) -> None:
    values = _valid_noncreation_kwargs()
    values[field] = bad_value
    values["identifier_result"] = None

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "identifier_evidence_stream_pair" in result["failed_prerequisites"]


def test_noncreation_rejects_cross_type_global_order_swap() -> None:
    values = _valid_noncreation_kwargs()
    stdout = "submit_id=NEW-HANDLE-001"
    stderr = "logid=L-1"
    external = validate_all_identifier_occurrences(stdout, stderr)
    assert external["all_submit_id_candidates"][0]["discovery_order"] == 1
    assert external["all_logid_candidates"][0]["discovery_order"] == 2
    external["all_submit_id_candidates"][0]["discovery_order"] = 2
    external["all_logid_candidates"][0]["discovery_order"] = 1
    values["sanitized_stdout"] = stdout
    values["sanitized_stderr"] = stderr
    values["identifier_result"] = external

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "identifier_evidence_rederivation_match" in result["failed_prerequisites"]


def test_noncreation_rejects_impossible_stderr_before_stdout_order() -> None:
    values = _valid_noncreation_kwargs()
    stdout = "submit_id=NEW-HANDLE-001"
    stderr = "submit_id=NEW-HANDLE-001"
    external = validate_all_identifier_occurrences(stdout, stderr)
    candidates = external["all_submit_id_candidates"]
    assert [(item["channel"], item["discovery_order"]) for item in candidates] == [
        ("stdout", 1),
        ("stderr", 2),
    ]
    candidates[0]["channel"] = "stderr"
    candidates[1]["channel"] = "stdout"
    values["sanitized_stdout"] = stdout
    values["sanitized_stderr"] = stderr
    values["identifier_result"] = external

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert result["failed_prerequisites"] == [
        "identifier_evidence_rederivation_match"
    ]


@pytest.mark.parametrize(
    "mutation",
    [
        "candidate_reordered",
        "channel",
        "source_kind",
        "frame_index",
        "line_number",
        "character_offset",
        "json_path",
        "identifier_value",
        "classification",
        "selected_value",
        "strict_frame_errors",
        "contradiction_flag",
        "discovery_order",
        "candidate_removed",
        "candidate_added",
    ],
)
def test_noncreation_rejects_any_external_identifier_evidence_tampering(
    mutation: str,
) -> None:
    values = _valid_noncreation_kwargs()
    stdout = "submit_id=NEW-HANDLE-001"
    stderr = ""
    if mutation == "candidate_reordered":
        stderr = "submit_id=NEW-HANDLE-001"
    elif mutation == "json_path":
        stdout = 'noise\n{"submit_id":"NEW-HANDLE-001"}\n'
    external = validate_all_identifier_occurrences(stdout, stderr)
    candidates = external["all_submit_id_candidates"]

    if mutation == "candidate_reordered":
        candidates.reverse()
    elif mutation == "channel":
        candidates[0]["channel"] = "stderr"
    elif mutation == "source_kind":
        candidates[0].update(
            source_kind="line_json",
            frame_index=1,
            line_number=1,
            json_path='$["submit_id"]',
        )
    elif mutation == "frame_index":
        candidates[0]["frame_index"] = 1
    elif mutation == "line_number":
        candidates[0]["line_number"] = 2
    elif mutation == "character_offset":
        candidates[0]["character_offset"] += 1
    elif mutation == "json_path":
        candidates[0]["json_path"] = '$["other"]'
    elif mutation == "identifier_value":
        candidates[0]["value"] = "OTHER-HANDLE"
        external["selected_submit_id"] = "OTHER-HANDLE"
    elif mutation == "classification":
        external["submit_id_consistency_classification"] = "MISSING"
    elif mutation == "selected_value":
        external["selected_submit_id"] = "OTHER-HANDLE"
    elif mutation == "strict_frame_errors":
        unsafe = validate_all_identifier_occurrences('{"submit_id":[]}', "")
        external["strict_frame_errors"] = [unsafe["strict_frame_errors"][0]]
        external["submit_id_consistency_classification"] = "CONFLICTING"
        external["selected_submit_id"] = None
        external["contradictory_identifiers_present"] = True
    elif mutation == "contradiction_flag":
        external["contradictory_identifiers_present"] = True
    elif mutation == "discovery_order":
        candidates[0]["discovery_order"] = 2
    elif mutation == "candidate_removed":
        candidates.clear()
    elif mutation == "candidate_added":
        duplicate = json.loads(json.dumps(candidates[0]))
        duplicate["discovery_order"] = 2
        candidates.append(duplicate)
        external["submit_id_consistency_classification"] = "DUPLICATE_EQUAL"
    else:  # pragma: no cover - the parametrization is exhaustive
        raise AssertionError(mutation)

    values["sanitized_stdout"] = stdout
    values["sanitized_stderr"] = stderr
    values["identifier_result"] = external

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "identifier_evidence_rederivation_match" in result["failed_prerequisites"]


@pytest.mark.parametrize(
    ("stdout", "stderr", "submit_classification", "logid_classification"),
    [
        ("", "", "MISSING", "MISSING"),
        ("submit_id=S-1", "", "UNIQUE", "MISSING"),
        ("submit_id=S-1 submit_id=S-1", "", "DUPLICATE_EQUAL", "MISSING"),
        ("submit_id=S-1", "submit_id=S-2", "CONFLICTING", "MISSING"),
    ],
)
def test_identifier_result_strict_revalidation_accepts_exact_classifications(
    stdout: str,
    stderr: str,
    submit_classification: str,
    logid_classification: str,
) -> None:
    identifier_result = validate_all_identifier_occurrences(stdout, stderr)

    validated = support._validate_identifier_result(identifier_result)

    assert validated == identifier_result
    assert validated["submit_id_consistency_classification"] == submit_classification
    assert validated["logid_consistency_classification"] == logid_classification


def test_identifier_result_strict_revalidation_accepts_recognized_frame_errors() -> None:
    identifier_result = validate_all_identifier_occurrences(
        '{"submit_id":[]}',
        "",
    )

    validated = support._validate_identifier_result(identifier_result)

    assert validated == identifier_result
    assert validated["strict_frame_errors"]
    assert validated["contradictory_identifiers_present"] is True


def test_identifier_result_strict_revalidation_rejects_malformed_frame_error() -> None:
    identifier_result = validate_all_identifier_occurrences(
        '{"submit_id":"A","submit_id":"B"}',
        "",
    )
    identifier_result["strict_frame_errors"][0]["identifier_type"] = "submit_id"

    with pytest.raises(support.IdentifierConsistencyError):
        support._validate_identifier_result(identifier_result)


@pytest.mark.parametrize(
    "historical_handles",
    [
        (" NEW-HANDLE-001 ", "OLD-HANDLE-002"),
        ("OLD-HANDLE-001", " OLD-HANDLE-001 "),
    ],
)
def test_noncreation_rejects_whitespace_wrapped_historical_handles(
    historical_handles: tuple[str, str],
) -> None:
    values = _valid_noncreation_kwargs()
    values["historical_quarantined_handles"] = historical_handles

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "historical_quarantined_handles_exact" in result["failed_prerequisites"]


@pytest.mark.parametrize(
    "new_handle",
    [" NEW-HANDLE-001 ", "NEW HANDLE", "NEW/HANDLE", "NEW-HANDLE\t"],
)
def test_noncreation_rejects_noncanonical_new_handle(new_handle: str) -> None:
    values = _valid_noncreation_kwargs()
    values["new_submit_handle"] = new_handle

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "new_submit_handle_canonical" in result["failed_prerequisites"]


def test_noncreation_unhashable_marker_returns_failed_result() -> None:
    values = _valid_noncreation_kwargs()
    values["prequeue_upload_marker"] = ["upload phase, no file upload"]

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert result["provider_task_noncreation_proven"] is False
    assert "recognized_prequeue_upload_marker" in result["failed_prerequisites"]


@pytest.mark.parametrize(
    "authority",
    [
        "query_authorized",
        "download_authorized",
        "retry_authorized",
        "resubmit_authorized",
        "batch_authorized",
    ],
)
def test_noncreation_any_later_authority_fails(authority: str) -> None:
    values = _valid_noncreation_kwargs()
    values[authority] = True

    result = validate_zero_charge_prequeue_noncreation(**values)

    assert f"{authority}_false" in result["failed_prerequisites"]
    assert result[authority] is False


def test_exclusive_claim_first_succeeds_and_second_fails(tmp_path: Path) -> None:
    path = tmp_path / "claim.json"
    first = create_exclusive_submit_claim(path, **_claim_kwargs())
    original = path.read_bytes()

    with pytest.raises(ExclusiveClaimExists):
        create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.read_bytes() == original
    assert first["sha256"] == hashlib.sha256(original).hexdigest()


def test_exclusive_claim_bytes_are_canonical_and_fields_are_exact(tmp_path: Path) -> None:
    path = tmp_path / "claim.json"
    result = create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.read_bytes() == canonical_json_bytes(result["record"])
    assert strict_json_load_file(path)["route_provider_submit_allowance_consumed"] is True
    assert result["record"]["route_provider_submit_invocation_count"] == 1
    assert result["record"]["route_status_code"] == "SUBMIT_INVOCATION_STARTED_ALLOWANCE_CONSUMED"
    assert all(
        result["record"][name] is False
        for name in (
            "query_authorized",
            "download_authorized",
            "retry_authorized",
            "resubmit_authorized",
            "batch_authorized",
        )
    )


def test_exclusive_claim_race_has_exactly_one_winner(tmp_path: Path) -> None:
    path = tmp_path / "claim.json"

    def attempt(index: int) -> str:
        try:
            create_exclusive_submit_claim(path, **_claim_kwargs(f"submit-{index}"))
            return "won"
        except ExclusiveClaimExists:
            return "blocked"

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        outcomes = list(pool.map(attempt, range(8)))

    assert outcomes.count("won") == 1
    assert outcomes.count("blocked") == 7
    strict_json_load_file(path)


def test_exclusive_claim_existing_file_is_untouched(tmp_path: Path) -> None:
    path = tmp_path / "claim.json"
    path.write_bytes(b"existing evidence")

    with pytest.raises(ExclusiveClaimExists):
        create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.read_bytes() == b"existing evidence"


@pytest.mark.skipif(os.name != "posix", reason="POSIX permission bits are not stable on Windows")
def test_exclusive_claim_mode_is_owner_read_write(tmp_path: Path) -> None:
    path = tmp_path / "claim.json"
    create_exclusive_submit_claim(path, **_claim_kwargs())

    assert stat.S_IMODE(path.stat().st_mode) == 0o600


def test_exclusive_claim_write_failure_leaves_claim_and_blocks_second(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / "claim.json"
    original_write_all = support._write_all

    def fail_after_partial_write(descriptor: int, payload: bytes) -> None:
        os.write(descriptor, payload[:8])
        raise OSError("simulated write failure")

    with monkeypatch.context() as scoped:
        scoped.setattr(support, "_write_all", fail_after_partial_write)
        with pytest.raises(OSError, match="simulated write failure"):
            create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.exists()
    monkeypatch.setattr(support, "_write_all", original_write_all)
    with pytest.raises(ExclusiveClaimExists):
        create_exclusive_submit_claim(path, **_claim_kwargs())


def test_exclusive_claim_fsync_failure_leaves_claim_and_blocks_second(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / "claim.json"

    with monkeypatch.context() as scoped:
        scoped.setattr(
            support,
            "_fsync_file",
            lambda descriptor: (_ for _ in ()).throw(OSError("simulated fsync failure")),
        )
        with pytest.raises(OSError, match="simulated fsync failure"):
            create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.exists()
    with pytest.raises(ExclusiveClaimExists):
        create_exclusive_submit_claim(path, **_claim_kwargs())


def test_exclusive_claim_verification_failure_leaves_claim_and_blocks_second(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / "claim.json"

    with monkeypatch.context() as scoped:
        scoped.setattr(
            support,
            "_verify_persisted_bytes",
            lambda target, expected: (_ for _ in ()).throw(RuntimeError("verify failed")),
        )
        with pytest.raises(RuntimeError, match="verify failed"):
            create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.exists()
    with pytest.raises(ExclusiveClaimExists):
        create_exclusive_submit_claim(path, **_claim_kwargs())


def test_exclusive_claim_never_uses_replace_or_delete(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / "claim.json"

    with monkeypatch.context() as scoped:
        scoped.setattr(os, "replace", lambda *args: (_ for _ in ()).throw(AssertionError("replace used")))
        scoped.setattr(os, "unlink", lambda *args: (_ for _ in ()).throw(AssertionError("unlink used")))
        create_exclusive_submit_claim(path, **_claim_kwargs())

    assert path.exists()


def test_exclusive_claim_requires_existing_parent(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        create_exclusive_submit_claim(tmp_path / "missing" / "claim.json", **_claim_kwargs())


@pytest.mark.parametrize("submit_authorized", [False, None, 0, 1, "true"])
def test_exclusive_claim_rejects_unauthorized_before_open(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    submit_authorized: object,
) -> None:
    path = tmp_path / "claim.json"
    values = _claim_kwargs()
    values["submit_authorized"] = submit_authorized

    with monkeypatch.context() as scoped:
        scoped.setattr(
            support.os,
            "open",
            lambda *args, **kwargs: (_ for _ in ()).throw(
                AssertionError("os.open must not be called")
            ),
        )
        with pytest.raises(ValueError, match="exactly true"):
            create_exclusive_submit_claim(path, **values)

    assert not path.exists()


def test_transition_valid_chain_returns_terminal_evidence(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    first = tmp_path / "transition-1.json"
    second = tmp_path / "transition-2.json"
    create_append_only_transition(
        first,
        **_transition_kwargs(anchor, sequence=1, state="CLAIMED"),
    )
    create_append_only_transition(
        second,
        **_transition_kwargs(
            first,
            sequence=2,
            state="CLOSED",
            counters={"submit": 1, "query": 0},
        ),
    )

    result = validate_transition_chain(anchor, [second, first])

    assert result["valid"] is True
    assert result["ordered_paths"] == [str(first.resolve()), str(second.resolve())]
    assert result["terminal_state"] == "CLOSED"
    assert result["terminal_hash"] == _sha(second)
    assert result["finding_details"] == []


@pytest.mark.parametrize(
    ("field", "bad_value", "message"),
    [
        ("experiment_id", "EXPERIMENT-B", "experiment_id mismatch"),
        ("schema_version", "SCHEMA_V2", "schema_version mismatch"),
    ],
)
def test_transition_creation_rejects_cross_identity_before_open(
    tmp_path: Path,
    field: str,
    bad_value: str,
    message: str,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    target = tmp_path / "transition.json"
    values = _transition_kwargs(anchor, sequence=1, state="STATE_1")
    values[field] = bad_value

    with pytest.raises(TransitionChainError, match=message):
        create_append_only_transition(target, **values)

    assert not target.exists()


@pytest.mark.parametrize(
    ("field", "bad_value", "finding_code"),
    [
        ("experiment_id", "EXPERIMENT-B", "experiment_id_mismatch:"),
        ("schema_version", "SCHEMA_V2", "schema_version_mismatch:"),
    ],
)
def test_transition_chain_rejects_cross_identity_splicing(
    tmp_path: Path,
    field: str,
    bad_value: str,
    finding_code: str,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
    )
    payload = strict_json_load_file(transition)
    payload[field] = bad_value
    transition.write_bytes(canonical_json_bytes(payload))

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any(
        finding.startswith(finding_code) for finding in result["finding_details"]
    )


@pytest.mark.parametrize(
    ("allowance_consumed", "invocation_count"),
    [(False, 1), (True, 0)],
)
def test_transition_creation_rejects_invalid_allowance_invocation_pair(
    tmp_path: Path,
    allowance_consumed: bool,
    invocation_count: int,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    target = tmp_path / "transition.json"

    with pytest.raises(TransitionChainError, match="pair is invalid"):
        create_append_only_transition(
            target,
            **_transition_kwargs(
                anchor,
                sequence=1,
                state="STATE_1",
                allowance_consumed=allowance_consumed,
                invocation_count=invocation_count,
            ),
        )

    assert not target.exists()


@pytest.mark.parametrize(
    ("allowance_consumed", "invocation_count"),
    [(False, 1), (True, 0)],
)
def test_transition_chain_rejects_invalid_allowance_invocation_pair(
    tmp_path: Path,
    allowance_consumed: bool,
    invocation_count: int,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
        allowance_consumed=allowance_consumed,
        invocation_count=invocation_count,
    )

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any(
        finding.startswith("invalid_allowance_invocation_pair:")
        for finding in result["finding_details"]
    )


@pytest.mark.parametrize(
    ("allowance_consumed", "invocation_count"),
    [(False, 1), (True, 0)],
)
def test_transition_chain_rejects_invalid_anchor_allowance_invocation_pair(
    tmp_path: Path,
    allowance_consumed: bool,
    invocation_count: int,
) -> None:
    anchor = _anchor_record(
        tmp_path / "anchor.json",
        allowance_consumed=allowance_consumed,
        invocation_count=invocation_count,
    )

    result = validate_transition_chain(anchor, [])

    assert result["valid"] is False
    assert any(
        finding.startswith("invalid_allowance_invocation_pair:")
        for finding in result["finding_details"]
    )


@pytest.mark.parametrize(
    ("allowance_consumed", "invocation_count"),
    [(False, 1), (True, 0)],
)
def test_transition_creation_rejects_invalid_predecessor_allowance_invocation_pair(
    tmp_path: Path,
    allowance_consumed: bool,
    invocation_count: int,
) -> None:
    anchor = _anchor_record(
        tmp_path / "anchor.json",
        allowance_consumed=allowance_consumed,
        invocation_count=invocation_count,
    )
    target = tmp_path / "transition.json"

    with pytest.raises(TransitionChainError, match="invalid state shape"):
        create_append_only_transition(
            target,
            **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
        )

    assert not target.exists()


def test_transition_creation_rejects_missing_bound_submit_counter(
    tmp_path: Path,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    target = tmp_path / "transition.json"
    values = _transition_kwargs(anchor, sequence=1, state="STATE_1")
    del values["operation_counters"][BOUND_SUBMIT_COUNTER_KEY]

    with pytest.raises(TransitionChainError, match="must include"):
        create_append_only_transition(target, **values)

    assert not target.exists()


def test_transition_creation_rejects_bound_submit_counter_mismatch(
    tmp_path: Path,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    target = tmp_path / "transition.json"
    values = _transition_kwargs(anchor, sequence=1, state="STATE_1")
    values["operation_counters"][BOUND_SUBMIT_COUNTER_KEY] = 0

    with pytest.raises(TransitionChainError, match="counter mismatch"):
        create_append_only_transition(target, **values)

    assert not target.exists()


@pytest.mark.parametrize("counter_change", ["missing", "mismatch"])
def test_transition_creation_rejects_invalid_predecessor_bound_submit_counter(
    tmp_path: Path,
    counter_change: str,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    payload = strict_json_load_file(anchor)
    if counter_change == "missing":
        del payload["operation_counters"][BOUND_SUBMIT_COUNTER_KEY]
    else:
        payload["operation_counters"][BOUND_SUBMIT_COUNTER_KEY] = 1
    anchor.write_bytes(canonical_json_bytes(payload))
    target = tmp_path / "transition.json"

    with pytest.raises(TransitionChainError, match="invalid state shape"):
        create_append_only_transition(
            target,
            **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
        )

    assert not target.exists()


@pytest.mark.parametrize("counter_change", ["missing", "mismatch"])
def test_transition_chain_rejects_invalid_bound_submit_counter(
    tmp_path: Path,
    counter_change: str,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
    )
    payload = strict_json_load_file(transition)
    if counter_change == "missing":
        del payload["operation_counters"][BOUND_SUBMIT_COUNTER_KEY]
        expected = "missing_bound_submit_invocation_counter:"
    else:
        payload["operation_counters"][BOUND_SUBMIT_COUNTER_KEY] = 0
        expected = "bound_submit_invocation_counter_mismatch:"
    transition.write_bytes(canonical_json_bytes(payload))

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any(
        finding.startswith(expected) for finding in result["finding_details"]
    )


@pytest.mark.parametrize(
    "authority_flags",
    [{}, {"": False}, {"submit_authorized": "no"}, []],
)
def test_transition_creation_rejects_invalid_predecessor_authority_flags(
    tmp_path: Path,
    authority_flags: object,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    payload = strict_json_load_file(anchor)
    payload["authority_flags"] = authority_flags
    anchor.write_bytes(canonical_json_bytes(payload))
    target = tmp_path / "transition.json"

    with pytest.raises(TransitionChainError, match="invalid state shape"):
        create_append_only_transition(
            target,
            **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
        )

    assert not target.exists()


def test_transition_sequence_gap_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(tmp_path / "transition-2.json", anchor, sequence=2)

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert "first_sequence_not_one" in result["finding_details"]
    assert "sequence_gap" in result["finding_details"]


def test_transition_duplicate_sequence_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    first = _write_transition_record(tmp_path / "a.json", anchor, sequence=1)
    second = _write_transition_record(tmp_path / "b.json", anchor, sequence=1)

    result = validate_transition_chain(anchor, [first, second])

    assert result["valid"] is False
    assert "duplicate_sequence:1" in result["finding_details"]


def test_transition_duplicate_path_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(tmp_path / "transition.json", anchor, sequence=1)

    result = validate_transition_chain(anchor, [transition, transition])

    assert result["valid"] is False
    assert "duplicate_path" in result["finding_details"]


def test_transition_prior_path_mismatch_and_orphan_safe_block(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    missing = tmp_path / "missing.json"
    transition = _write_transition_record(
        tmp_path / "transition.json",
        missing,
        sequence=1,
        previous_sha="0" * 64,
    )

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any(item.startswith("orphan:") for item in result["finding_details"])
    assert any(item.startswith("prior_path_mismatch:") for item in result["finding_details"])


def test_transition_prior_hash_mismatch_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
        previous_sha="0" * 64,
    )

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any(item.startswith("previous_hash_mismatch:") for item in result["finding_details"])


def test_transition_fork_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    first = _write_transition_record(tmp_path / "first.json", anchor, sequence=1)
    second = _write_transition_record(tmp_path / "second.json", anchor, sequence=2)

    result = validate_transition_chain(anchor, [first, second])

    assert result["valid"] is False
    assert any(item.startswith("fork:") for item in result["finding_details"])


def test_transition_cycle_safe_blocks_where_constructible(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"
    _write_transition_record(first, second, sequence=1, previous_sha="0" * 64)
    _write_transition_record(second, first, sequence=2, previous_sha="0" * 64)

    result = validate_transition_chain(anchor, [first, second])

    assert result["valid"] is False
    assert any(item.startswith("cycle:") for item in result["finding_details"])


def test_transition_allowance_restoration_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(
        tmp_path / "anchor.json",
        allowance_consumed=True,
        invocation_count=1,
    )
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
        allowance_consumed=False,
    )

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any(item.startswith("allowance_restoration:") for item in result["finding_details"])


def test_transition_decreasing_counter_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(
        tmp_path / "anchor.json",
        allowance_consumed=True,
        invocation_count=1,
        counters={"submit": 1, "query": 1},
    )
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
        counters={"submit": 1, "query": 0},
    )

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any("decreasing_operation_counter" in item for item in result["finding_details"])


def test_transition_invocation_count_above_one_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(
        tmp_path / "transition.json",
        anchor,
        sequence=1,
        invocation_count=2,
    )

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any("invalid_submit_invocation_count" in item for item in result["finding_details"])


def test_transition_noncanonical_record_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = tmp_path / "transition.json"
    payload = _transition_kwargs(anchor, sequence=1, state="STATE_1")
    transition.write_text(json.dumps(payload, default=str), encoding="utf-8")

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any("noncanonical_or_unreadable_record" in item for item in result["finding_details"])


def test_transition_invalid_anchor_state_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    payload = strict_json_load_file(anchor)
    payload["route_provider_submit_invocation_count"] = 2
    payload["authority_flags"] = {"submit_authorized": "no"}
    anchor.write_bytes(canonical_json_bytes(payload))

    result = validate_transition_chain(anchor, [])

    assert result["valid"] is False
    assert any("invalid_submit_invocation_count" in item for item in result["finding_details"])
    assert any("invalid_authority_flag" in item for item in result["finding_details"])


def test_transition_invalid_record_shape_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = _write_transition_record(tmp_path / "transition.json", anchor, sequence=1)
    payload = strict_json_load_file(transition)
    payload["authority_flags"] = {}
    payload["operation_counters"] = {"submit": -1}
    del payload["transition_reason"]
    transition.write_bytes(canonical_json_bytes(payload))

    result = validate_transition_chain(anchor, [transition])

    assert result["valid"] is False
    assert any("invalid_authority_flags" in item for item in result["finding_details"])
    assert any("invalid_operation_counter" in item for item in result["finding_details"])
    assert any("missing_or_invalid_field" in item for item in result["finding_details"])


def test_transition_existing_path_is_untouched(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = tmp_path / "transition.json"
    transition.write_bytes(b"existing transition evidence")

    with pytest.raises(TransitionChainError, match="already exists"):
        create_append_only_transition(
            transition,
            **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
        )

    assert transition.read_bytes() == b"existing transition evidence"


def test_transition_creation_rejects_previous_hash_mismatch(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    values = _transition_kwargs(anchor, sequence=1, state="STATE_1")
    values["previous_record_sha256"] = "0" * 64

    with pytest.raises(TransitionChainError, match="SHA-256 mismatch"):
        create_append_only_transition(tmp_path / "transition.json", **values)

    assert not (tmp_path / "transition.json").exists()


def test_transition_creation_rejects_sequence_gap(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")

    with pytest.raises(TransitionChainError, match="exactly 1"):
        create_append_only_transition(
            tmp_path / "transition.json",
            **_transition_kwargs(anchor, sequence=2, state="STATE_2"),
        )

    assert not (tmp_path / "transition.json").exists()


def test_transition_creation_rejects_allowance_restoration(tmp_path: Path) -> None:
    anchor = _anchor_record(
        tmp_path / "anchor.json",
        allowance_consumed=True,
        invocation_count=1,
    )

    with pytest.raises(TransitionChainError, match="cannot be restored"):
        create_append_only_transition(
            tmp_path / "transition.json",
            **_transition_kwargs(
                anchor,
                sequence=1,
                state="STATE_1",
                allowance_consumed=False,
                invocation_count=0,
            ),
        )

    assert not (tmp_path / "transition.json").exists()


def test_transition_creation_rejects_decreasing_counter(tmp_path: Path) -> None:
    anchor = _anchor_record(
        tmp_path / "anchor.json",
        allowance_consumed=True,
        invocation_count=1,
        counters={"submit": 1, "query": 1},
    )

    with pytest.raises(TransitionChainError, match="cannot decrease: query"):
        create_append_only_transition(
            tmp_path / "transition.json",
            **_transition_kwargs(
                anchor,
                sequence=1,
                state="STATE_1",
                counters={"submit": 1, "query": 0},
            ),
        )

    assert not (tmp_path / "transition.json").exists()


def test_transition_post_create_failure_preserves_record(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = tmp_path / "transition.json"

    with monkeypatch.context() as scoped:
        scoped.setattr(
            support,
            "_verify_persisted_bytes",
            lambda target, expected: (_ for _ in ()).throw(RuntimeError("verify failed")),
        )
        with pytest.raises(RuntimeError, match="verify failed"):
            create_append_only_transition(
                transition,
                **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
            )

    assert transition.exists()
    with pytest.raises(TransitionChainError, match="already exists"):
        create_append_only_transition(
            transition,
            **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
        )


def test_transition_contradictory_duplicate_state_safe_blocks(tmp_path: Path) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"
    create_append_only_transition(
        first,
        **_transition_kwargs(anchor, sequence=1, state="SAME", counters={"submit": 1}),
    )
    create_append_only_transition(
        second,
        **_transition_kwargs(first, sequence=2, state="SAME", counters={"submit": 1, "query": 1}),
    )

    result = validate_transition_chain(anchor, [first, second])

    assert result["valid"] is False
    assert "contradictory_duplicate_state:SAME" in result["finding_details"]


def test_transition_creation_never_uses_replace_or_delete(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    anchor = _anchor_record(tmp_path / "anchor.json")
    transition = tmp_path / "transition.json"

    with monkeypatch.context() as scoped:
        scoped.setattr(os, "replace", lambda *args: (_ for _ in ()).throw(AssertionError("replace used")))
        scoped.setattr(os, "unlink", lambda *args: (_ for _ in ()).throw(AssertionError("unlink used")))
        create_append_only_transition(
            transition,
            **_transition_kwargs(anchor, sequence=1, state="STATE_1"),
        )

    assert transition.exists()
