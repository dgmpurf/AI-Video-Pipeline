from __future__ import annotations

import base64
import binascii
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from typing import Any, Mapping


_SHA256_RE = re.compile(r"[0-9a-fA-F]{64}\Z")
_LAST_BYTE_HEX_RE = re.compile(r"[0-9a-fA-F]{2}\Z")
_CHECKPOINT_RE = re.compile(r"[0-9a-fA-F]{40}\Z")
_MISSING = object()
_RECORD_REPRESENTATION_GROUPS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("byte_length", ("byte_length", "authorization_byte_length")),
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
        "base64_character_count",
        ("base64_character_count", "derived_base64_character_count"),
    ),
    (
        "canonical_text",
        ("canonical_authorization_text", "exact_authorization_text"),
    ),
    ("authority_source", ("authority_source",)),
    ("encoding", ("encoding",)),
    ("utf8_decode_valid", ("utf8_decode_valid",)),
    ("bom_present", ("bom", "bom_present")),
    ("cr_present", ("cr_present",)),
    ("lf_present", ("lf_present",)),
    ("trailing_carriage_return", ("trailing_carriage_return",)),
    ("trailing_newline", ("trailing_newline",)),
    ("trailing_space", ("trailing_space",)),
    ("markdown_fence_present", ("markdown_fence_present",)),
    ("last_character", ("last_character",)),
    ("last_byte_hex", ("last_byte_hex",)),
    (
        "base64_decode_count",
        ("base64_decode_count", "locally_generated_base64_decode_count"),
    ),
    ("decoded_bytes_equal_original", ("decoded_bytes_equal_original",)),
    ("base64_round_trip_verified", ("base64_round_trip_verified",)),
    (
        "decoded_sha256_equal_original",
        ("decoded_sha256_equal_original",),
    ),
    ("byte_profile_valid", ("byte_profile_valid",)),
    (
        "serialization_round_trip_verified",
        ("serialization_round_trip_verified",),
    ),
    ("decoded_sha256", ("decoded_sha256",)),
    ("authorization_verified", ("authorization_verified",)),
)
_BOOLEAN_FACT_GROUPS = frozenset(
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
_INTEGER_FACT_GROUPS = frozenset(
    {"byte_length", "base64_character_count", "base64_decode_count"}
)
_STRING_FACT_GROUPS = frozenset(
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
_RECORD_FACT_TYPES: dict[str, type[Any]] = {
    **{name: bool for name in _BOOLEAN_FACT_GROUPS},
    **{name: int for name in _INTEGER_FACT_GROUPS},
    **{name: str for name in _STRING_FACT_GROUPS},
}
_RECOGNIZED_FACT_GROUPS = frozenset(
    label for label, _aliases in _RECORD_REPRESENTATION_GROUPS
)
if frozenset(_RECORD_FACT_TYPES) != _RECOGNIZED_FACT_GROUPS:
    raise RuntimeError("every recognized authorization fact requires an exact type")

_CASE_INSENSITIVE_HEX_GROUPS = frozenset(
    {"sha256", "decoded_sha256", "last_byte_hex"}
)


@dataclass(frozen=True)
class AuthorizationSerializationResult:
    authority_source: str
    encoding: str
    utf8_decode_valid: bool
    bom_present: bool
    cr_present: bool
    lf_present: bool
    trailing_carriage_return: bool
    trailing_newline: bool
    trailing_space: bool
    markdown_fence_present: bool
    byte_length: int
    sha256: str
    base64: str
    base64_character_count: int
    base64_decode_count: int
    decoded_bytes_equal_original: bool
    decoded_sha256_equal_original: bool
    last_character: str | None
    last_byte_hex: str | None
    byte_profile_valid: bool
    serialization_round_trip_verified: bool
    serialization_profile_valid: bool
    authorization_evidence_verified: bool
    authorization_verified: bool
    validation_errors: tuple[str, ...]
    eligible_for_authority_activation: bool
    execution_authority_active: bool = False
    provider_command_allowed: bool = False
    provider_command_invocation_count: int = 0
    authorized_operation_count_consumed: int = 0

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["validation_errors"] = list(self.validation_errors)
        return payload


@dataclass(frozen=True)
class AuthorizationVerificationResult:
    serialization: AuthorizationSerializationResult
    expected_byte_length: int | None
    expected_sha256: str | None
    expected_base64_present: bool
    expected_base64_character_count: int | None
    expected_byte_length_matches: bool
    expected_sha256_matches: bool
    expected_base64_matches: bool | None
    expected_base64_decode_count: int
    expected_base64_decoded_bytes_equal_original: bool | None
    expected_base64_decoded_sha256_equal_original: bool | None
    record_canonical_text_present: bool
    record_canonical_text_matches: bool | None
    record_serialization_facts_match: bool
    record_fact_mismatches: tuple[str, ...]
    record_representations_consistent: bool
    record_representation_conflicts: tuple[str, ...]
    expected_values_match: bool
    authorization_evidence_verified: bool
    authorization_verified: bool
    validation_errors: tuple[str, ...]
    eligible_for_authority_activation: bool
    execution_authority_active: bool = False
    provider_command_allowed: bool = False
    provider_command_invocation_count: int = 0
    authorized_operation_count_consumed: int = 0

    def to_dict(self) -> dict[str, Any]:
        payload = self.serialization.to_dict()
        payload["serialization_authorization_verified"] = payload[
            "authorization_verified"
        ]
        payload.update(
            {
                "expected_byte_length": self.expected_byte_length,
                "expected_sha256": self.expected_sha256,
                "expected_base64_present": self.expected_base64_present,
                "expected_base64_character_count": self.expected_base64_character_count,
                "expected_byte_length_matches": self.expected_byte_length_matches,
                "expected_sha256_matches": self.expected_sha256_matches,
                "expected_base64_matches": self.expected_base64_matches,
                "expected_base64_decode_count": self.expected_base64_decode_count,
                "expected_base64_decoded_bytes_equal_original": (
                    self.expected_base64_decoded_bytes_equal_original
                ),
                "expected_base64_decoded_sha256_equal_original": (
                    self.expected_base64_decoded_sha256_equal_original
                ),
                "record_canonical_text_present": self.record_canonical_text_present,
                "record_canonical_text_matches": self.record_canonical_text_matches,
                "record_serialization_facts_match": (
                    self.record_serialization_facts_match
                ),
                "record_fact_mismatches": list(self.record_fact_mismatches),
                "record_representations_consistent": (
                    self.record_representations_consistent
                ),
                "record_representation_conflicts": list(
                    self.record_representation_conflicts
                ),
                "expected_values_match": self.expected_values_match,
                "authorization_evidence_verified": (
                    self.authorization_evidence_verified
                ),
                "authorization_verified": self.authorization_verified,
                "validation_errors": list(self.validation_errors),
                "eligible_for_authority_activation": (
                    self.eligible_for_authority_activation
                ),
                "execution_authority_active": self.execution_authority_active,
                "provider_command_allowed": self.provider_command_allowed,
                "provider_command_invocation_count": (
                    self.provider_command_invocation_count
                ),
                "authorized_operation_count_consumed": (
                    self.authorized_operation_count_consumed
                ),
            }
        )
        return payload


@dataclass(frozen=True)
class CheckpointBindingResult:
    required_checkpoint: str
    local_head: str
    origin_main: str
    required_checkpoint_valid: bool
    local_head_valid: bool
    origin_main_valid: bool
    local_head_matches_required: bool
    origin_main_matches_required: bool
    local_head_matches_origin_main: bool
    checkpoint_binding_verified: bool
    checkpoint_change_requires_reauthorization: bool
    validation_errors: tuple[str, ...]
    eligible_for_authority_activation: bool
    execution_authority_active: bool = False
    provider_command_allowed: bool = False
    provider_command_invocation_count: int = 0
    authorized_operation_count_consumed: int = 0

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["validation_errors"] = list(self.validation_errors)
        return payload


@dataclass(frozen=True)
class ActivationEligibilityResult:
    serialization_verified: bool
    serialization_profile_valid: bool
    authorization_evidence_verified: bool
    checkpoint_binding_required: bool
    checkpoint_binding_verified: bool | None
    eligible_for_authority_activation: bool
    decision: str
    validation_errors: tuple[str, ...]
    execution_authority_active: bool = False
    provider_command_allowed: bool = False
    provider_command_invocation_count: int = 0
    authorized_operation_count_consumed: int = 0

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["validation_errors"] = list(self.validation_errors)
        return payload


def compile_authorization_bytes(raw_bytes: bytes) -> AuthorizationSerializationResult:
    """Compile exact bytes without repairing, normalizing, or trimming them."""
    if not isinstance(raw_bytes, bytes):
        raise TypeError("raw_bytes must be bytes")

    errors: list[str] = []
    decoded_text: str | None
    try:
        decoded_text = raw_bytes.decode("utf-8", errors="strict")
        utf8_decode_valid = True
    except UnicodeDecodeError:
        decoded_text = None
        utf8_decode_valid = False

    bom_present = raw_bytes.startswith(b"\xef\xbb\xbf")
    cr_present = b"\r" in raw_bytes
    lf_present = b"\n" in raw_bytes
    trailing_carriage_return = raw_bytes.endswith(b"\r")
    trailing_newline = raw_bytes.endswith(b"\n")
    trailing_space = raw_bytes.endswith(b" ")
    markdown_fence_present = b"```" in raw_bytes

    if not raw_bytes:
        errors.append("empty_input")
    if not utf8_decode_valid:
        errors.append("invalid_utf8")
    if bom_present:
        errors.append("utf8_bom_present")
    if cr_present:
        errors.append("carriage_return_present")
    if lf_present:
        errors.append("line_feed_present")
    if trailing_space:
        errors.append("trailing_space_present")
    if markdown_fence_present:
        errors.append("markdown_fence_present")

    digest = hashlib.sha256(raw_bytes).hexdigest()
    encoded_base64 = base64.b64encode(raw_bytes).decode("ascii")
    base64_decode_count = 1
    decoded_round_trip = base64.b64decode(encoded_base64, validate=True)
    decoded_bytes_equal_original = decoded_round_trip == raw_bytes
    decoded_sha256_equal_original = (
        hashlib.sha256(decoded_round_trip).hexdigest() == digest
    )
    if not decoded_bytes_equal_original:
        errors.append("derived_base64_bytes_mismatch")
    if not decoded_sha256_equal_original:
        errors.append("derived_base64_sha256_mismatch")

    last_character = decoded_text[-1] if decoded_text else None
    last_byte_hex = f"{raw_bytes[-1]:02X}" if raw_bytes else None
    byte_profile_valid = not any(
        error
        in {
            "empty_input",
            "invalid_utf8",
            "utf8_bom_present",
            "carriage_return_present",
            "line_feed_present",
            "trailing_space_present",
            "markdown_fence_present",
        }
        for error in errors
    )
    serialization_round_trip_verified = (
        decoded_bytes_equal_original and decoded_sha256_equal_original
    )
    serialization_profile_valid = (
        byte_profile_valid and serialization_round_trip_verified
    )

    return AuthorizationSerializationResult(
        authority_source="exact_canonical_text",
        encoding="UTF-8",
        utf8_decode_valid=utf8_decode_valid,
        bom_present=bom_present,
        cr_present=cr_present,
        lf_present=lf_present,
        trailing_carriage_return=trailing_carriage_return,
        trailing_newline=trailing_newline,
        trailing_space=trailing_space,
        markdown_fence_present=markdown_fence_present,
        byte_length=len(raw_bytes),
        sha256=digest,
        base64=encoded_base64,
        base64_character_count=len(encoded_base64),
        base64_decode_count=base64_decode_count,
        decoded_bytes_equal_original=decoded_bytes_equal_original,
        decoded_sha256_equal_original=decoded_sha256_equal_original,
        last_character=last_character,
        last_byte_hex=last_byte_hex,
        byte_profile_valid=byte_profile_valid,
        serialization_round_trip_verified=serialization_round_trip_verified,
        serialization_profile_valid=serialization_profile_valid,
        authorization_evidence_verified=False,
        authorization_verified=False,
        validation_errors=tuple(errors),
        eligible_for_authority_activation=False,
    )


def compile_authorization_text(exact_text: str) -> AuthorizationSerializationResult:
    """Compile a caller-supplied exact string using deterministic UTF-8 encoding."""
    if not isinstance(exact_text, str):
        raise TypeError("exact_text must be str")
    return compile_authorization_bytes(exact_text.encode("utf-8", errors="strict"))


def verify_authorization_bytes(
    raw_bytes: bytes,
    expected_record: Mapping[str, Any],
) -> AuthorizationVerificationResult:
    """Verify exact bytes against expected evidence without activating authority."""
    if not isinstance(expected_record, Mapping):
        raise TypeError("expected_record must be a mapping")

    serialization = compile_authorization_bytes(raw_bytes)
    containers, container_errors = _record_containers(expected_record)
    errors = list(serialization.validation_errors)
    errors.extend(container_errors)
    fact_validation_errors = _record_fact_validation_errors(containers)
    errors.extend(fact_validation_errors)
    representation_conflicts = _record_representation_conflicts(containers)
    errors.extend(
        f"record_representation_conflict:{name}"
        for name in representation_conflicts
    )
    record_representations_consistent = not representation_conflicts

    expected_length_raw = _first_value(
        containers, "byte_length", "authorization_byte_length"
    )
    expected_byte_length = _coerce_integer(expected_length_raw)
    if expected_byte_length is None:
        errors.append("expected_byte_length_missing_or_invalid")
    expected_byte_length_matches = expected_byte_length == serialization.byte_length
    if expected_byte_length is not None and not expected_byte_length_matches:
        errors.append("expected_byte_length_mismatch")

    expected_sha_raw = _first_value(
        containers, "sha256", "authorization_text_sha256"
    )
    expected_sha256 = expected_sha_raw if isinstance(expected_sha_raw, str) else None
    expected_sha_valid = bool(
        expected_sha256 and _SHA256_RE.fullmatch(expected_sha256)
    )
    if not expected_sha_valid:
        errors.append("expected_sha256_missing_or_invalid")
    expected_sha256_matches = bool(
        expected_sha_valid
        and expected_sha256
        and expected_sha256.lower() == serialization.sha256
    )
    if expected_sha_valid and not expected_sha256_matches:
        errors.append("expected_sha256_mismatch")

    expected_base64_raw = _first_value(
        containers,
        "base64",
        "authorization_base64",
        "locally_derived_base64",
        "locally_generated_base64",
    )
    expected_base64_present = isinstance(expected_base64_raw, str)
    expected_base64_count_raw = _first_value(
        containers,
        "base64_character_count",
        "derived_base64_character_count",
    )
    expected_base64_character_count = _coerce_integer(expected_base64_count_raw)
    expected_base64_matches: bool | None = None
    expected_base64_decode_count = 0
    expected_decoded_equal: bool | None = None
    expected_decoded_sha_equal: bool | None = None

    if expected_base64_present:
        expected_base64 = expected_base64_raw
        expected_base64_matches = expected_base64 == serialization.base64
        if not expected_base64_matches:
            errors.append("expected_base64_mismatch")
        if (
            expected_base64_character_count is not None
            and expected_base64_character_count != len(expected_base64)
        ):
            errors.append("expected_base64_character_count_mismatch")
        expected_base64_decode_count = 1
        try:
            expected_decoded = base64.b64decode(expected_base64, validate=True)
        except (binascii.Error, ValueError):
            errors.append("expected_base64_invalid")
        else:
            expected_decoded_equal = expected_decoded == raw_bytes
            expected_decoded_sha_equal = (
                hashlib.sha256(expected_decoded).hexdigest() == serialization.sha256
            )
            if not expected_decoded_equal:
                errors.append("expected_base64_decoded_bytes_mismatch")
            if not expected_decoded_sha_equal:
                errors.append("expected_base64_decoded_sha256_mismatch")
    elif expected_base64_count_raw is not _MISSING:
        errors.append("expected_base64_missing")

    record_text_raw = _first_value(
        containers,
        "canonical_authorization_text",
        "exact_authorization_text",
    )
    record_canonical_text_present = record_text_raw is not _MISSING
    record_canonical_text_matches: bool | None = None
    if record_canonical_text_present:
        if isinstance(record_text_raw, str):
            try:
                record_text_bytes = record_text_raw.encode(
                    "utf-8", errors="strict"
                )
            except UnicodeEncodeError:
                record_canonical_text_matches = False
                errors.append("record_canonical_text_invalid")
            else:
                record_canonical_text_matches = record_text_bytes == raw_bytes
            if not record_canonical_text_matches:
                errors.append("record_canonical_text_mismatch")
        else:
            record_canonical_text_matches = False
            errors.append("record_canonical_text_invalid")

    fact_mismatches = _record_fact_mismatches(containers, serialization)
    errors.extend(f"record_fact_mismatch:{name}" for name in fact_mismatches)
    record_serialization_facts_match = not fact_mismatches

    expected_values_match = all(
        (
            expected_byte_length_matches,
            expected_sha256_matches,
            expected_base64_matches is not False,
            expected_decoded_equal is not False,
            expected_decoded_sha_equal is not False,
            record_canonical_text_matches is not False,
            record_serialization_facts_match,
            record_representations_consistent,
        )
    )
    authorization_evidence_verified = (
        serialization.serialization_profile_valid
        and expected_values_match
        and not errors
    )
    authorization_verified = authorization_evidence_verified

    return AuthorizationVerificationResult(
        serialization=serialization,
        expected_byte_length=expected_byte_length,
        expected_sha256=expected_sha256,
        expected_base64_present=expected_base64_present,
        expected_base64_character_count=expected_base64_character_count,
        expected_byte_length_matches=expected_byte_length_matches,
        expected_sha256_matches=expected_sha256_matches,
        expected_base64_matches=expected_base64_matches,
        expected_base64_decode_count=expected_base64_decode_count,
        expected_base64_decoded_bytes_equal_original=expected_decoded_equal,
        expected_base64_decoded_sha256_equal_original=expected_decoded_sha_equal,
        record_canonical_text_present=record_canonical_text_present,
        record_canonical_text_matches=record_canonical_text_matches,
        record_serialization_facts_match=record_serialization_facts_match,
        record_fact_mismatches=tuple(fact_mismatches),
        record_representations_consistent=record_representations_consistent,
        record_representation_conflicts=tuple(representation_conflicts),
        expected_values_match=expected_values_match,
        authorization_evidence_verified=authorization_evidence_verified,
        authorization_verified=authorization_verified,
        validation_errors=tuple(errors),
        eligible_for_authority_activation=False,
    )


def verify_authorization_record(
    raw_bytes: bytes,
    record: Mapping[str, Any],
) -> AuthorizationVerificationResult:
    """Verify exact bytes against a committed authorization JSON record."""
    return verify_authorization_bytes(raw_bytes, record)


def verify_checkpoint_binding(
    required_checkpoint: str,
    local_head: str,
    origin_main: str,
) -> CheckpointBindingResult:
    """Verify explicitly supplied checkpoint facts without invoking Git."""
    values = (required_checkpoint, local_head, origin_main)
    if not all(isinstance(value, str) for value in values):
        raise TypeError("checkpoint values must be strings")

    required_valid = bool(_CHECKPOINT_RE.fullmatch(required_checkpoint))
    local_valid = bool(_CHECKPOINT_RE.fullmatch(local_head))
    origin_valid = bool(_CHECKPOINT_RE.fullmatch(origin_main))
    errors: list[str] = []
    if not required_valid:
        errors.append("required_checkpoint_invalid")
    if not local_valid:
        errors.append("local_head_invalid")
    if not origin_valid:
        errors.append("origin_main_invalid")

    required_key = required_checkpoint.lower()
    local_key = local_head.lower()
    origin_key = origin_main.lower()
    local_matches_required = required_valid and local_valid and local_key == required_key
    origin_matches_required = (
        required_valid and origin_valid and origin_key == required_key
    )
    local_matches_origin = local_valid and origin_valid and local_key == origin_key
    if required_valid and local_valid and not local_matches_required:
        errors.append("local_head_mismatch")
    if required_valid and origin_valid and not origin_matches_required:
        errors.append("origin_main_mismatch")
    if local_valid and origin_valid and not local_matches_origin:
        errors.append("local_head_origin_main_mismatch")

    verified = all(
        (
            required_valid,
            local_valid,
            origin_valid,
            local_matches_required,
            origin_matches_required,
            local_matches_origin,
        )
    )
    return CheckpointBindingResult(
        required_checkpoint=required_checkpoint,
        local_head=local_head,
        origin_main=origin_main,
        required_checkpoint_valid=required_valid,
        local_head_valid=local_valid,
        origin_main_valid=origin_valid,
        local_head_matches_required=local_matches_required,
        origin_main_matches_required=origin_matches_required,
        local_head_matches_origin_main=local_matches_origin,
        checkpoint_binding_verified=verified,
        checkpoint_change_requires_reauthorization=not verified,
        validation_errors=tuple(errors),
        eligible_for_authority_activation=False,
    )


def evaluate_activation_eligibility(
    authorization_result: AuthorizationSerializationResult
    | AuthorizationVerificationResult,
    checkpoint_result: CheckpointBindingResult | None = None,
) -> ActivationEligibilityResult:
    """Require verified evidence and checkpoint binding without activating authority."""
    if isinstance(authorization_result, AuthorizationVerificationResult):
        serialization_profile_valid = (
            authorization_result.serialization.serialization_profile_valid
        )
        authorization_evidence_verified = (
            authorization_result.authorization_evidence_verified
            and authorization_result.record_representations_consistent
        )
    elif isinstance(authorization_result, AuthorizationSerializationResult):
        serialization_profile_valid = authorization_result.serialization_profile_valid
        authorization_evidence_verified = False
    else:
        raise TypeError(
            "authorization_result must be a serialization or verification result"
        )

    serialization_verified = serialization_profile_valid
    checkpoint_required = True
    checkpoint_verified = (
        checkpoint_result.checkpoint_binding_verified if checkpoint_result else None
    )
    errors: list[str] = []
    if not serialization_profile_valid:
        errors.append("serialization_profile_validation_failed")
    if not authorization_evidence_verified:
        if isinstance(authorization_result, AuthorizationSerializationResult):
            errors.append("authorization_evidence_verification_required")
        else:
            errors.append("authorization_evidence_verification_failed")
    if checkpoint_result is None:
        errors.append("checkpoint_binding_required")
    elif not checkpoint_verified:
        errors.append("checkpoint_binding_failed")
    eligible = all(
        (
            serialization_profile_valid,
            authorization_evidence_verified,
            checkpoint_verified is True,
        )
    )
    return ActivationEligibilityResult(
        serialization_verified=serialization_verified,
        serialization_profile_valid=serialization_profile_valid,
        authorization_evidence_verified=authorization_evidence_verified,
        checkpoint_binding_required=checkpoint_required,
        checkpoint_binding_verified=checkpoint_verified,
        eligible_for_authority_activation=eligible,
        decision="ready" if eligible else "safe_block",
        validation_errors=tuple(errors),
    )


def stable_json_text(payload: Mapping[str, Any]) -> str:
    """Return deterministic UTF-8-compatible JSON text with one final LF."""
    return json.dumps(
        dict(payload),
        ensure_ascii=True,
        indent=2,
        sort_keys=True,
    ) + "\n"


def stable_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return stable_json_text(payload).encode("utf-8")


def _record_containers(
    record: Mapping[str, Any],
) -> tuple[tuple[Mapping[str, Any], ...], tuple[str, ...]]:
    containers: list[Mapping[str, Any]] = [record]
    errors: list[str] = []
    for key in ("canonical_serialization", "canonical_authorization"):
        if key not in record:
            continue
        value = record[key]
        if not isinstance(value, Mapping):
            errors.append(f"recognized_container_not_object:{key}")
            continue
        containers.insert(0, value)
        if "verification" not in value:
            continue
        verification = value["verification"]
        if not isinstance(verification, Mapping):
            errors.append(f"recognized_container_not_object:{key}.verification")
            continue
        containers.append(verification)
    return tuple(containers), tuple(errors)


def _record_fact_validation_errors(
    containers: tuple[Mapping[str, Any], ...],
) -> tuple[str, ...]:
    errors: list[str] = []
    for label, aliases in _RECORD_REPRESENTATION_GROUPS:
        values = _all_values(containers, *aliases)
        if not values:
            continue
        expected_type = _RECORD_FACT_TYPES[label]
        correctly_typed = tuple(
            value for value in values if type(value) is expected_type
        )
        if len(correctly_typed) != len(values):
            errors.append(f"record_fact_invalid_type:{label}")
        if any(
            not _record_fact_value_valid(label, value)
            for value in correctly_typed
        ):
            errors.append(f"record_fact_invalid_value:{label}")
    return tuple(errors)


def _record_fact_value_valid(label: str, value: Any) -> bool:
    if label in _INTEGER_FACT_GROUPS and value < 0:
        return False
    if label == "base64_decode_count":
        return value == 1
    if label in {"sha256", "decoded_sha256"}:
        return bool(_SHA256_RE.fullmatch(value))
    if label == "last_byte_hex":
        return bool(_LAST_BYTE_HEX_RE.fullmatch(value))
    if label == "authority_source":
        return value == "exact_canonical_text"
    if label == "encoding":
        return value == "UTF-8"
    return True


def _record_representation_conflicts(
    containers: tuple[Mapping[str, Any], ...],
) -> list[str]:
    conflicts: list[str] = []
    for label, aliases in _RECORD_REPRESENTATION_GROUPS:
        values = _all_values(containers, *aliases)
        if len(values) < 2:
            continue
        first = values[0]
        if any(
            not _record_values_equal(label, first, candidate)
            for candidate in values[1:]
        ):
            conflicts.append(label)
    return conflicts


def _all_values(
    containers: tuple[Mapping[str, Any], ...],
    *names: str,
) -> tuple[Any, ...]:
    return tuple(
        container[name]
        for container in containers
        for name in names
        if name in container
    )


def _record_values_equal(label: str, left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if label in _CASE_INSENSITIVE_HEX_GROUPS and isinstance(left, str):
        pattern = _LAST_BYTE_HEX_RE if label == "last_byte_hex" else _SHA256_RE
        if pattern.fullmatch(left) and pattern.fullmatch(right):
            return left.lower() == right.lower()
    return left == right


def _first_value(
    containers: tuple[Mapping[str, Any], ...],
    *names: str,
) -> Any:
    for container in containers:
        for name in names:
            if name in container:
                return container[name]
    return _MISSING


def _coerce_integer(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


def _record_fact_mismatches(
    containers: tuple[Mapping[str, Any], ...],
    result: AuthorizationSerializationResult,
) -> list[str]:
    checks: tuple[tuple[tuple[str, ...], Any, str], ...] = (
        (("authority_source",), result.authority_source, "authority_source"),
        (("encoding",), result.encoding, "encoding"),
        (("utf8_decode_valid",), result.utf8_decode_valid, "utf8_decode_valid"),
        (("bom", "bom_present"), result.bom_present, "bom_present"),
        (("cr_present",), result.cr_present, "cr_present"),
        (("lf_present",), result.lf_present, "lf_present"),
        (
            ("trailing_carriage_return",),
            result.trailing_carriage_return,
            "trailing_carriage_return",
        ),
        (("trailing_newline",), result.trailing_newline, "trailing_newline"),
        (("trailing_space",), result.trailing_space, "trailing_space"),
        (
            ("markdown_fence_present",),
            result.markdown_fence_present,
            "markdown_fence_present",
        ),
        (("last_character",), result.last_character, "last_character"),
        (("last_byte_hex",), result.last_byte_hex, "last_byte_hex"),
        (
            ("base64_character_count", "derived_base64_character_count"),
            result.base64_character_count,
            "base64_character_count",
        ),
        (
            ("base64_decode_count", "locally_generated_base64_decode_count"),
            result.base64_decode_count,
            "base64_decode_count",
        ),
        (
            ("decoded_bytes_equal_original",),
            result.decoded_bytes_equal_original,
            "decoded_bytes_equal_original",
        ),
        (
            ("base64_round_trip_verified",),
            result.serialization_round_trip_verified,
            "base64_round_trip_verified",
        ),
        (
            ("decoded_sha256_equal_original",),
            result.decoded_sha256_equal_original,
            "decoded_sha256_equal_original",
        ),
        (("byte_profile_valid",), result.byte_profile_valid, "byte_profile_valid"),
        (
            ("serialization_round_trip_verified",),
            result.serialization_round_trip_verified,
            "serialization_round_trip_verified",
        ),
    )
    mismatches: list[str] = []
    for aliases, actual, label in checks:
        expected = _first_value(containers, *aliases)
        if (
            expected is not _MISSING
            and not _record_values_equal(label, expected, actual)
        ):
            mismatches.append(label)

    decoded_sha = _first_value(containers, "decoded_sha256")
    if (
        decoded_sha is not _MISSING
        and not _record_values_equal("decoded_sha256", decoded_sha, result.sha256)
    ):
        mismatches.append("decoded_sha256")
    authorization_verified = _first_value(containers, "authorization_verified")
    if (
        authorization_verified is not _MISSING
        and not _record_values_equal(
            "authorization_verified", authorization_verified, True
        )
    ):
        mismatches.append("record_authorization_verified")
    return mismatches
