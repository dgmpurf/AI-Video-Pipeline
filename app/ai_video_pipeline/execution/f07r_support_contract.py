from __future__ import annotations

import errno
import hashlib
import json
import math
import os
import re
from dataclasses import asdict, dataclass
from numbers import Number
from pathlib import Path
from typing import Any, Mapping, Sequence

from app.ai_video_pipeline.execution.dreamina_evidence import sanitize_text


__all__ = [
    "DuplicateJSONKeyError",
    "ExclusiveClaimExists",
    "IdentifierConsistencyError",
    "StrictJSONError",
    "TransitionChainError",
    "build_raw_stream_metadata",
    "canonical_json_bytes",
    "create_append_only_transition",
    "create_exclusive_submit_claim",
    "strict_json_load_file",
    "strict_json_loads",
    "validate_all_identifier_occurrences",
    "validate_transition_chain",
    "validate_zero_charge_prequeue_noncreation",
]


ASCII_WHITESPACE = " \t\r\n\f\v"
IDENTIFIER_VALUE_RE = re.compile(r"[A-Za-z0-9._:-]+\Z", flags=re.ASCII)
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z", flags=re.ASCII)
ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY = (
    "route_provider_submit_invocation_count"
)
_IDENTIFIER_RESULT_FIELDS = frozenset(
    {
        "all_submit_id_candidates",
        "all_logid_candidates",
        "submit_id_consistency_classification",
        "logid_consistency_classification",
        "selected_submit_id",
        "selected_logid",
        "strict_frame_errors",
        "contradictory_identifiers_present",
    }
)
_IDENTIFIER_OCCURRENCE_FIELDS = frozenset(
    {
        "identifier_type",
        "value",
        "channel",
        "source_kind",
        "frame_index",
        "line_number",
        "character_offset",
        "json_path",
        "discovery_order",
    }
)
_STRICT_FRAME_ERROR_FIELDS = frozenset(
    {
        "channel",
        "source_kind",
        "frame_index",
        "line_number",
        "character_offset",
        "error_code",
        "identifier_type",
        "message",
    }
)
_IDENTIFIER_TYPES = frozenset({"submit_id", "logid"})
_IDENTIFIER_CHANNELS = frozenset({"stdout", "stderr"})
_IDENTIFIER_SOURCE_KINDS = frozenset(
    {"full_stream_json", "line_json", "text_token"}
)
_STRICT_FRAME_ERROR_CODES = frozenset(
    {
        "duplicate_json_key",
        "nonfinite_json_value",
        "strict_json_error",
        "invalid_structured_identifier_value",
    }
)
_TRANSITION_MARKER_FIELDS = frozenset(
    {
        "transition_id",
        "sequence_number",
        "previous_record_path",
        "previous_record_sha256",
    }
)
PREQUEUE_UPLOAD_FAILURE_MARKERS = frozenset(
    {
        "upload phase, no file upload",
        "upload phase: no file upload",
    }
)
_SELF_HASH_KEYS = frozenset(
    {
        "own_hash",
        "own_sha256",
        "self_hash",
        "self_sha256",
    }
)
_TEXT_KEY_PATTERN = r"(?:submit_id|submit-id|submitid|logid|log_id|log-id)"
_TEXT_IDENTIFIER_RE = re.compile(
    rf"(?<![A-Za-z0-9_-])"
    rf"(?:"
    rf"(?P<quote>['\"])(?P<quoted_key>{_TEXT_KEY_PATTERN})(?P=quote)"
    rf"|"
    rf"(?P<plain_key>{_TEXT_KEY_PATTERN})(?![A-Za-z0-9_-])"
    rf")"
    rf"(?:[ \t\f\v]*[:=][ \t\f\v]*|[ \t\f\v]+)"
    rf"(?P<value>[A-Za-z0-9._:-]+)"
    rf"(?=$|[ \t\r\n\f\v,;}}\]\)])",
    flags=re.IGNORECASE | re.ASCII,
)
_RESIDUAL_SENSITIVE_FIELD_RE = re.compile(
    r"(?im)(?<![A-Za-z0-9_])"
    r"([\"']?(?:prompt|negative_prompt|password|credential|device_code|"
    r"authorization|access_token|refresh_token|api_key|token|secret|session|cookie)"
    r"[\"']?(?:[ \t\f\v]*[:=][ \t\f\v]*|[ \t\f\v]+))"
    r"(?:[\"'][^\r\n]*?[\"']|[^\r\n,}\]]+)"
)
_UNSAFE_CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_ASCII_LOWER_TRANSLATION = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
)


class StrictJSONError(ValueError):
    """Raised when JSON bytes or text violate the strict contract."""


class StrictJSONSyntaxError(StrictJSONError):
    """Raised for ordinary JSON syntax failures."""


class DuplicateJSONKeyError(StrictJSONError):
    """Raised when a JSON object contains the same key more than once."""

    def __init__(self, key: str) -> None:
        super().__init__(f"duplicate JSON key: {key}")
        self.key = key


class NonFiniteJSONError(StrictJSONError):
    """Raised when JSON contains NaN or an infinity token."""


class IdentifierConsistencyError(ValueError):
    """Raised when identifier evidence cannot be accepted consistently."""


class ExclusiveClaimExists(FileExistsError):
    """Raised when an exclusive allowance claim already exists."""


class TransitionChainError(RuntimeError):
    """Raised when a transition cannot be created safely."""


@dataclass(frozen=True)
class IdentifierOccurrence:
    identifier_type: str
    value: str
    channel: str
    source_kind: str
    frame_index: int
    line_number: int | None
    character_offset: int
    json_path: str | None
    discovery_order: int


@dataclass(frozen=True)
class StrictFrameError:
    channel: str
    source_kind: str
    frame_index: int
    line_number: int | None
    character_offset: int
    error_code: str
    identifier_type: str | None
    message: str


def _reject_nonfinite_constant(value: str) -> Any:
    raise NonFiniteJSONError(f"nonfinite JSON value: {value}")


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(key)
        result[key] = value
    return result


def strict_json_loads(value: str | bytes | bytearray) -> Any:
    """Load one strict JSON value with duplicate and nonfinite rejection."""

    if isinstance(value, (bytes, bytearray)):
        raw = bytes(value)
        if raw.startswith(b"\xef\xbb\xbf"):
            raise StrictJSONError("UTF-8 BOM is not permitted")
        try:
            text = raw.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise StrictJSONError("JSON is not strict UTF-8") from exc
    elif isinstance(value, str):
        text = value
        if text.startswith("\ufeff"):
            raise StrictJSONError("UTF-8 BOM is not permitted")
    else:
        raise TypeError("strict_json_loads accepts str or bytes")

    try:
        return json.loads(
            text,
            object_pairs_hook=_strict_object,
            parse_constant=_reject_nonfinite_constant,
        )
    except (DuplicateJSONKeyError, NonFiniteJSONError):
        raise
    except json.JSONDecodeError as exc:
        raise StrictJSONSyntaxError(str(exc)) from exc


def strict_json_load_file(path: str | os.PathLike[str]) -> Any:
    """Read and strictly parse one JSON file without accepting partial data."""

    return strict_json_loads(Path(path).read_bytes())


def _validate_json_value(value: Any, *, path: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise StrictJSONError(f"nonfinite value at {path}")
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise StrictJSONError(f"non-string object key at {path}")
            normalized_key = (
                key.strip(ASCII_WHITESPACE)
                .translate(_ASCII_LOWER_TRANSLATION)
                .replace("-", "_")
            )
            if normalized_key in _SELF_HASH_KEYS:
                raise StrictJSONError(f"self-hash field is forbidden at {path}")
            _validate_json_value(child, path=f"{path}[{json.dumps(key)}]")
        return
    if isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            _validate_json_value(child, path=f"{path}[{index}]")
        return
    raise StrictJSONError(f"unsupported JSON value at {path}: {type(value).__name__}")


def canonical_json_bytes(payload: Any) -> bytes:
    """Serialize a strict JSON value as deterministic UTF-8 with one final LF."""

    _validate_json_value(payload)
    try:
        text = json.dumps(
            payload,
            ensure_ascii=True,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise StrictJSONError("payload cannot be serialized canonically") from exc
    return (text + "\n").encode("utf-8")


def _read_canonical_json_record(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    payload = strict_json_loads(raw)
    if not isinstance(payload, dict):
        raise StrictJSONError("persisted record must be a JSON object")
    if raw != canonical_json_bytes(payload):
        raise StrictJSONError("persisted record is not canonical JSON")
    return payload, raw


def _normalize_identifier_key(key: str) -> str | None:
    normalized = (
        key.strip(ASCII_WHITESPACE)
        .translate(_ASCII_LOWER_TRANSLATION)
        .replace("_", "")
        .replace("-", "")
    )
    if normalized == "submitid":
        return "submit_id"
    if normalized == "logid":
        return "logid"
    return None


def _identifier_value(value: Any) -> str | None:
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        return None
    normalized = str(value).strip(ASCII_WHITESPACE)
    if not normalized or IDENTIFIER_VALUE_RE.fullmatch(normalized) is None:
        return None
    return normalized


def _json_key_positions(text: str) -> list[tuple[str, int]]:
    decoder = json.JSONDecoder()
    positions: list[tuple[str, int]] = []
    index = 0
    while index < len(text):
        if text[index] != '"':
            index += 1
            continue
        try:
            decoded, end = decoder.raw_decode(text, index)
        except json.JSONDecodeError:
            index += 1
            continue
        if isinstance(decoded, str):
            after = end
            while after < len(text) and text[after] in ASCII_WHITESPACE:
                after += 1
            if after < len(text) and text[after] == ":":
                positions.append((decoded, index))
        index = max(end, index + 1)
    return positions


def _json_path(parent: str, key: str | int) -> str:
    if isinstance(key, int):
        return f"{parent}[{key}]"
    return f"{parent}[{json.dumps(key, ensure_ascii=True)}]"


def _line_number_at(text: str, offset: int) -> int:
    return sum(1 for _ in re.finditer(r"\r\n|\r|\n", text[:offset])) + 1


def _iter_channel_lines(text: str) -> Sequence[tuple[int, int, str]]:
    lines: list[tuple[int, int, str]] = []
    start = 0
    line_number = 1
    for separator in re.finditer(r"\r\n|\r|\n", text):
        lines.append((line_number, start, text[start : separator.start()]))
        start = separator.end()
        line_number += 1
    if start < len(text):
        lines.append((line_number, start, text[start:]))
    return lines


def validate_all_identifier_occurrences(
    stdout: str,
    stderr: str,
) -> dict[str, Any]:
    """Collect and classify every recognized identifier occurrence deterministically."""

    if not isinstance(stdout, str) or not isinstance(stderr, str):
        raise TypeError("stdout and stderr must be decoded strings")

    occurrences: list[IdentifierOccurrence] = []
    frame_errors: list[StrictFrameError] = []
    unsafe_types: set[str] = set()
    globally_unsafe = False
    discovery_order = 0

    def add_occurrence(
        *,
        identifier_type: str,
        value: str,
        channel: str,
        source_kind: str,
        frame_index: int,
        line_number: int | None,
        character_offset: int,
        json_path: str | None,
    ) -> None:
        nonlocal discovery_order
        discovery_order += 1
        occurrences.append(
            IdentifierOccurrence(
                identifier_type=identifier_type,
                value=value,
                channel=channel,
                source_kind=source_kind,
                frame_index=frame_index,
                line_number=line_number,
                character_offset=character_offset,
                json_path=json_path,
                discovery_order=discovery_order,
            )
        )

    def add_frame_error(
        *,
        channel: str,
        source_kind: str,
        frame_index: int,
        line_number: int | None,
        character_offset: int,
        error_code: str,
        message: str,
        identifier_type: str | None = None,
    ) -> None:
        nonlocal globally_unsafe
        frame_errors.append(
            StrictFrameError(
                channel=channel,
                source_kind=source_kind,
                frame_index=frame_index,
                line_number=line_number,
                character_offset=character_offset,
                error_code=error_code,
                identifier_type=identifier_type,
                message=message,
            )
        )
        if identifier_type is None:
            globally_unsafe = True
        else:
            unsafe_types.add(identifier_type)

    def record_strict_error(
        exc: StrictJSONError,
        *,
        channel: str,
        source_kind: str,
        frame_index: int,
        line_number: int | None,
        character_offset: int,
    ) -> None:
        if isinstance(exc, DuplicateJSONKeyError):
            code = "duplicate_json_key"
        elif isinstance(exc, NonFiniteJSONError):
            code = "nonfinite_json_value"
        else:
            code = "strict_json_error"
        add_frame_error(
            channel=channel,
            source_kind=source_kind,
            frame_index=frame_index,
            line_number=line_number,
            character_offset=character_offset,
            error_code=code,
            message=str(exc),
        )

    def traverse_json(
        value: Any,
        *,
        channel: str,
        source_kind: str,
        frame_index: int,
        line_number: int | None,
        frame_text: str,
        frame_offset: int,
    ) -> None:
        positions = [
            (identifier_type, position)
            for raw_key, position in _json_key_positions(frame_text)
            if (identifier_type := _normalize_identifier_key(raw_key)) is not None
        ]
        position_cursor = 0

        def visit(node: Any, path: str) -> None:
            nonlocal position_cursor
            if isinstance(node, dict):
                for key, child in node.items():
                    child_path = _json_path(path, key)
                    identifier_type = _normalize_identifier_key(key)
                    if identifier_type is not None:
                        local_offset = 0
                        for candidate_index in range(position_cursor, len(positions)):
                            candidate_type, candidate_offset = positions[candidate_index]
                            if candidate_type == identifier_type:
                                local_offset = candidate_offset
                                position_cursor = candidate_index + 1
                                break
                        candidate_value = _identifier_value(child)
                        if candidate_value is None:
                            add_frame_error(
                                channel=channel,
                                source_kind=source_kind,
                                frame_index=frame_index,
                                line_number=line_number,
                                character_offset=frame_offset + local_offset,
                                error_code="invalid_structured_identifier_value",
                                identifier_type=identifier_type,
                                message=f"invalid structured identifier at {child_path}",
                            )
                        else:
                            add_occurrence(
                                identifier_type=identifier_type,
                                value=candidate_value,
                                channel=channel,
                                source_kind=source_kind,
                                frame_index=frame_index,
                                line_number=line_number,
                                character_offset=frame_offset + local_offset,
                                json_path=child_path,
                            )
                    visit(child, child_path)
            elif isinstance(node, list):
                for index, child in enumerate(node):
                    visit(child, _json_path(path, index))

        visit(value, "$")

    def process_channel(channel: str, text: str) -> None:
        if text:
            try:
                value = strict_json_loads(text)
            except StrictJSONSyntaxError:
                pass
            except StrictJSONError as exc:
                record_strict_error(
                    exc,
                    channel=channel,
                    source_kind="full_stream_json",
                    frame_index=0,
                    line_number=None,
                    character_offset=0,
                )
            else:
                traverse_json(
                    value,
                    channel=channel,
                    source_kind="full_stream_json",
                    frame_index=0,
                    line_number=None,
                    frame_text=text,
                    frame_offset=0,
                )

        for line_number, line_offset, line in _iter_channel_lines(text):
            if line:
                trimmed = line.strip(ASCII_WHITESPACE)
                leading = len(line) - len(line.lstrip(ASCII_WHITESPACE))
                try:
                    value = strict_json_loads(trimmed)
                except StrictJSONSyntaxError:
                    pass
                except StrictJSONError as exc:
                    record_strict_error(
                        exc,
                        channel=channel,
                        source_kind="line_json",
                        frame_index=line_number,
                        line_number=line_number,
                        character_offset=line_offset + leading,
                    )
                else:
                    traverse_json(
                        value,
                        channel=channel,
                        source_kind="line_json",
                        frame_index=line_number,
                        line_number=line_number,
                        frame_text=trimmed,
                        frame_offset=line_offset + leading,
                    )
        for match_index, match in enumerate(_TEXT_IDENTIFIER_RE.finditer(text)):
            key = match.group("quoted_key") or match.group("plain_key")
            identifier_type = _normalize_identifier_key(key)
            if identifier_type is None:
                continue
            add_occurrence(
                identifier_type=identifier_type,
                value=match.group("value"),
                channel=channel,
                source_kind="text_token",
                frame_index=match_index,
                line_number=_line_number_at(text, match.start()),
                character_offset=match.start(),
                json_path=None,
            )

    process_channel("stdout", stdout)
    process_channel("stderr", stderr)

    submit_occurrences = [item for item in occurrences if item.identifier_type == "submit_id"]
    logid_occurrences = [item for item in occurrences if item.identifier_type == "logid"]

    def classify(
        identifier_type: str,
        candidates: list[IdentifierOccurrence],
    ) -> tuple[str, str | None]:
        values = [item.value for item in candidates]
        if globally_unsafe or identifier_type in unsafe_types or len(set(values)) > 1:
            return "CONFLICTING", None
        if not values:
            return "MISSING", None
        if len(values) == 1:
            return "UNIQUE", values[0]
        return "DUPLICATE_EQUAL", values[0]

    submit_classification, selected_submit_id = classify("submit_id", submit_occurrences)
    logid_classification, selected_logid = classify("logid", logid_occurrences)
    contradictory = (
        submit_classification == "CONFLICTING"
        or logid_classification == "CONFLICTING"
        or bool(frame_errors)
    )

    return {
        "all_submit_id_candidates": [asdict(item) for item in submit_occurrences],
        "all_logid_candidates": [asdict(item) for item in logid_occurrences],
        "submit_id_consistency_classification": submit_classification,
        "logid_consistency_classification": logid_classification,
        "selected_submit_id": selected_submit_id,
        "selected_logid": selected_logid,
        "strict_frame_errors": [asdict(item) for item in frame_errors],
        "contradictory_identifiers_present": contradictory,
    }


def _decode_utf8_replace_with_count(raw: bytes) -> tuple[str, int]:
    parts: list[str] = []
    cursor = 0
    replacement_count = 0
    while cursor < len(raw):
        try:
            parts.append(raw[cursor:].decode("utf-8", errors="strict"))
            cursor = len(raw)
        except UnicodeDecodeError as exc:
            if exc.start:
                parts.append(raw[cursor : cursor + exc.start].decode("utf-8"))
            parts.append("\ufffd")
            replacement_count += 1
            cursor += exc.end
    decoded = "".join(parts)
    if decoded != raw.decode("utf-8", errors="replace"):
        raise UnicodeError("replacement decoder diverged from utf-8/errors-replace")
    return decoded, replacement_count


def _sanitize_stream(value: str, *, secret_values: Sequence[str]) -> str:
    sanitized = sanitize_text(value, secret_values=secret_values)
    sanitized = _RESIDUAL_SENSITIVE_FIELD_RE.sub(r"\1<redacted>", sanitized)
    sanitized = _UNSAFE_CONTROL_RE.sub("<control>", sanitized)
    for secret in sorted({str(item) for item in secret_values if str(item)}, key=len, reverse=True):
        sanitized = sanitized.replace(secret, "<redacted_secret>")
    return sanitized


def build_raw_stream_metadata(
    raw_stdout: bytes,
    raw_stderr: bytes,
    *,
    secret_values: Sequence[str] = (),
) -> dict[str, Any]:
    """Build nonreversible metadata from separate predecode stdout/stderr bytes."""

    if not isinstance(raw_stdout, bytes) or not isinstance(raw_stderr, bytes):
        raise TypeError("raw_stdout and raw_stderr must be bytes")
    stdout, stdout_replacements = _decode_utf8_replace_with_count(raw_stdout)
    stderr, stderr_replacements = _decode_utf8_replace_with_count(raw_stderr)
    sanitized_stdout = _sanitize_stream(stdout, secret_values=secret_values)
    sanitized_stderr = _sanitize_stream(stderr, secret_values=secret_values)
    return {
        "raw_stdout_byte_count": len(raw_stdout),
        "raw_stdout_sha256": hashlib.sha256(raw_stdout).hexdigest(),
        "raw_stderr_byte_count": len(raw_stderr),
        "raw_stderr_sha256": hashlib.sha256(raw_stderr).hexdigest(),
        "stdout_decoding": "utf-8/errors-replace",
        "stderr_decoding": "utf-8/errors-replace",
        "stdout_utf8_replacement_count": stdout_replacements,
        "stderr_utf8_replacement_count": stderr_replacements,
        "sanitized_stdout": sanitized_stdout,
        "sanitized_stdout_sha256": hashlib.sha256(sanitized_stdout.encode("utf-8")).hexdigest(),
        "sanitized_stderr": sanitized_stderr,
        "sanitized_stderr_sha256": hashlib.sha256(sanitized_stderr.encode("utf-8")).hexdigest(),
        "raw_content_persisted": False,
    }


def _is_exact_true(value: Any) -> bool:
    return value is True


def _is_exact_false(value: Any) -> bool:
    return value is False


def _is_numeric(value: Any) -> bool:
    if isinstance(value, bool) or not isinstance(value, Number):
        return False
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError, OverflowError):
        return False


def _is_nonnegative_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _canonical_identifier_token(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value:
        raise IdentifierConsistencyError(f"{name} must be a nonempty string")
    if value != value.strip(ASCII_WHITESPACE):
        raise IdentifierConsistencyError(
            f"{name} must not contain outer ASCII whitespace"
        )
    if IDENTIFIER_VALUE_RE.fullmatch(value) is None:
        raise IdentifierConsistencyError(f"{name} has invalid identifier characters")
    return value


def _validate_occurrence(
    value: Any,
    *,
    expected_identifier_type: str,
) -> dict[str, Any]:
    if (
        not isinstance(value, Mapping)
        or set(value) != _IDENTIFIER_OCCURRENCE_FIELDS
    ):
        raise IdentifierConsistencyError("identifier occurrence has an invalid field set")
    if value.get("identifier_type") != expected_identifier_type:
        raise IdentifierConsistencyError("identifier occurrence has the wrong identifier type")
    _canonical_identifier_token("identifier occurrence value", value.get("value"))
    channel = value.get("channel")
    source_kind = value.get("source_kind")
    frame_index = value.get("frame_index")
    line_number = value.get("line_number")
    character_offset = value.get("character_offset")
    json_path = value.get("json_path")
    discovery_order = value.get("discovery_order")
    if channel not in _IDENTIFIER_CHANNELS:
        raise IdentifierConsistencyError("identifier occurrence has an invalid channel")
    if source_kind not in _IDENTIFIER_SOURCE_KINDS:
        raise IdentifierConsistencyError("identifier occurrence has an invalid source kind")
    if not _is_nonnegative_integer(frame_index):
        raise IdentifierConsistencyError("identifier occurrence has an invalid frame index")
    if line_number is not None and not _is_nonnegative_integer(line_number):
        raise IdentifierConsistencyError("identifier occurrence has an invalid line number")
    if not _is_nonnegative_integer(character_offset):
        raise IdentifierConsistencyError("identifier occurrence has an invalid character offset")
    if (
        not isinstance(discovery_order, int)
        or isinstance(discovery_order, bool)
        or discovery_order < 1
    ):
        raise IdentifierConsistencyError("identifier occurrence has an invalid discovery order")
    if source_kind == "full_stream_json":
        if frame_index != 0 or line_number is not None:
            raise IdentifierConsistencyError("full-stream occurrence has invalid frame metadata")
        if not isinstance(json_path, str) or not json_path.startswith("$["):
            raise IdentifierConsistencyError("full-stream occurrence has an invalid JSON path")
    elif source_kind == "line_json":
        if line_number is None or line_number < 1 or frame_index != line_number:
            raise IdentifierConsistencyError("line occurrence has invalid frame metadata")
        if not isinstance(json_path, str) or not json_path.startswith("$["):
            raise IdentifierConsistencyError("line occurrence has an invalid JSON path")
    else:
        if line_number is None or line_number < 1 or json_path is not None:
            raise IdentifierConsistencyError("text occurrence has invalid frame metadata")
    return dict(value)


def _validate_strict_frame_error(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != _STRICT_FRAME_ERROR_FIELDS:
        raise IdentifierConsistencyError("strict frame error has an invalid field set")
    channel = value.get("channel")
    source_kind = value.get("source_kind")
    frame_index = value.get("frame_index")
    line_number = value.get("line_number")
    character_offset = value.get("character_offset")
    error_code = value.get("error_code")
    identifier_type = value.get("identifier_type")
    message = value.get("message")
    if channel not in _IDENTIFIER_CHANNELS:
        raise IdentifierConsistencyError("strict frame error has an invalid channel")
    if source_kind not in {"full_stream_json", "line_json"}:
        raise IdentifierConsistencyError("strict frame error has an invalid source kind")
    if not _is_nonnegative_integer(frame_index):
        raise IdentifierConsistencyError("strict frame error has an invalid frame index")
    if line_number is not None and not _is_nonnegative_integer(line_number):
        raise IdentifierConsistencyError("strict frame error has an invalid line number")
    if not _is_nonnegative_integer(character_offset):
        raise IdentifierConsistencyError("strict frame error has an invalid character offset")
    if error_code not in _STRICT_FRAME_ERROR_CODES:
        raise IdentifierConsistencyError("strict frame error has an invalid error code")
    if identifier_type is not None and identifier_type not in _IDENTIFIER_TYPES:
        raise IdentifierConsistencyError("strict frame error has an invalid identifier type")
    if not isinstance(message, str) or not message:
        raise IdentifierConsistencyError("strict frame error has an invalid message")
    if source_kind == "full_stream_json" and (
        frame_index != 0 or line_number is not None
    ):
        raise IdentifierConsistencyError("full-stream error has invalid frame metadata")
    if source_kind == "line_json" and (
        line_number is None or line_number < 1 or frame_index != line_number
    ):
        raise IdentifierConsistencyError("line error has invalid frame metadata")
    if error_code == "invalid_structured_identifier_value":
        if identifier_type is None:
            raise IdentifierConsistencyError(
                "structured identifier error must name its identifier type"
            )
    elif identifier_type is not None:
        raise IdentifierConsistencyError(
            "strict JSON frame error must not name an identifier type"
        )
    return dict(value)


def _expected_identifier_classification(
    identifier_type: str,
    candidates: Sequence[Mapping[str, Any]],
    strict_frame_errors: Sequence[Mapping[str, Any]],
) -> tuple[str, str | None]:
    unsafe = any(
        error["identifier_type"] is None
        or error["identifier_type"] == identifier_type
        for error in strict_frame_errors
    )
    values = [candidate["value"] for candidate in candidates]
    if unsafe or len(set(values)) > 1:
        return "CONFLICTING", None
    if not values:
        return "MISSING", None
    if len(values) == 1:
        return "UNIQUE", values[0]
    return "DUPLICATE_EQUAL", values[0]


def _validate_identifier_result(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != _IDENTIFIER_RESULT_FIELDS:
        raise IdentifierConsistencyError("identifier result has an invalid field set")
    submit_candidates_raw = value.get("all_submit_id_candidates")
    logid_candidates_raw = value.get("all_logid_candidates")
    strict_errors_raw = value.get("strict_frame_errors")
    if not isinstance(submit_candidates_raw, list) or not isinstance(
        logid_candidates_raw, list
    ):
        raise IdentifierConsistencyError("identifier candidates must be lists")
    if not isinstance(strict_errors_raw, list):
        raise IdentifierConsistencyError("strict frame errors must be a list")

    submit_candidates = [
        _validate_occurrence(item, expected_identifier_type="submit_id")
        for item in submit_candidates_raw
    ]
    logid_candidates = [
        _validate_occurrence(item, expected_identifier_type="logid")
        for item in logid_candidates_raw
    ]
    strict_errors = [_validate_strict_frame_error(item) for item in strict_errors_raw]

    for candidates in (submit_candidates, logid_candidates):
        orders = [candidate["discovery_order"] for candidate in candidates]
        if orders != sorted(orders) or len(orders) != len(set(orders)):
            raise IdentifierConsistencyError(
                "candidate discovery order is not strictly increasing"
            )
    all_orders = [
        candidate["discovery_order"]
        for candidate in [*submit_candidates, *logid_candidates]
    ]
    if len(all_orders) != len(set(all_orders)) or sorted(all_orders) != list(
        range(1, len(all_orders) + 1)
    ):
        raise IdentifierConsistencyError("global candidate discovery order is invalid")

    expected_submit = _expected_identifier_classification(
        "submit_id", submit_candidates, strict_errors
    )
    expected_logid = _expected_identifier_classification(
        "logid", logid_candidates, strict_errors
    )
    actual_submit = (
        value.get("submit_id_consistency_classification"),
        value.get("selected_submit_id"),
    )
    actual_logid = (
        value.get("logid_consistency_classification"),
        value.get("selected_logid"),
    )
    for name, selected in (
        ("selected_submit_id", actual_submit[1]),
        ("selected_logid", actual_logid[1]),
    ):
        if selected is not None:
            _canonical_identifier_token(name, selected)
    if actual_submit != expected_submit:
        raise IdentifierConsistencyError("submit identifier classification is inconsistent")
    if actual_logid != expected_logid:
        raise IdentifierConsistencyError("logid classification is inconsistent")

    contradiction = value.get("contradictory_identifiers_present")
    if not isinstance(contradiction, bool):
        raise IdentifierConsistencyError("contradiction flag must be boolean")
    expected_contradiction = (
        expected_submit[0] == "CONFLICTING"
        or expected_logid[0] == "CONFLICTING"
        or bool(strict_errors)
    )
    if contradiction is not expected_contradiction:
        raise IdentifierConsistencyError("contradiction flag is inconsistent")
    return dict(value)


def validate_zero_charge_prequeue_noncreation(
    *,
    provider_invocation_started: Any,
    submit_allowance_consumed: Any,
    creation_classification: Any,
    prequeue_upload_marker: Any,
    new_submit_handle: Any,
    historical_quarantined_handles: Any,
    new_handle_quarantined: Any,
    logid_absent: Any,
    queue_status_evidence_absent: Any,
    provider_task_evidence_absent: Any,
    successful_output_evidence_absent: Any,
    provider_task_created: Any,
    created_task_count: Any,
    provider_credit_count: Any,
    immediate_pre_credit: Any,
    immediate_post_credit: Any,
    sanitized_stdout: str,
    sanitized_stderr: str,
    identifier_result: Mapping[str, Any] | None = None,
    evidence_durable: Any,
    evidence_reread_verified: Any,
    query_authorized: Any,
    download_authorized: Any,
    retry_authorized: Any,
    resubmit_authorized: Any,
    batch_authorized: Any,
) -> dict[str, Any]:
    """Prove provider task noncreation only when every prerequisite is exact."""

    failed: list[str] = []

    def require(name: str, condition: bool) -> None:
        if not condition:
            failed.append(name)

    try:
        handle = _canonical_identifier_token("new_submit_handle", new_submit_handle)
        handle_valid = True
    except IdentifierConsistencyError:
        handle = ""
        handle_valid = False
    historical_sequence_valid = (
        isinstance(historical_quarantined_handles, Sequence)
        and not isinstance(historical_quarantined_handles, (str, bytes, bytearray))
        and len(historical_quarantined_handles) == 2
    )
    historical_values: list[str] = []
    if historical_sequence_valid:
        try:
            historical_values = [
                _canonical_identifier_token("historical_quarantined_handle", item)
                for item in historical_quarantined_handles
            ]
        except IdentifierConsistencyError:
            historical_values = []
    historical_valid = (
        historical_sequence_valid
        and len(historical_values) == 2
        and len(set(historical_values)) == 2
    )
    historical = tuple(historical_values) if historical_valid else tuple()
    stream_pair_valid = isinstance(sanitized_stdout, str) and isinstance(
        sanitized_stderr, str
    )
    identifiers = (
        validate_all_identifier_occurrences(sanitized_stdout, sanitized_stderr)
        if stream_pair_valid
        else {}
    )
    external_result_matches = True
    if identifier_result is not None:
        external_result_matches = False
        if stream_pair_valid:
            try:
                validated_external = _validate_identifier_result(identifier_result)
                external_result_matches = canonical_json_bytes(
                    validated_external
                ) == canonical_json_bytes(identifiers)
            except (IdentifierConsistencyError, StrictJSONError):
                pass
    require("provider_invocation_started", _is_exact_true(provider_invocation_started))
    require("submit_allowance_consumed", _is_exact_true(submit_allowance_consumed))
    require(
        "creation_classification",
        creation_classification == "orphaned_handle_after_prequeue_upload_failure",
    )
    require(
        "recognized_prequeue_upload_marker",
        isinstance(prequeue_upload_marker, str)
        and prequeue_upload_marker in PREQUEUE_UPLOAD_FAILURE_MARKERS,
    )
    require("new_submit_handle_nonempty", bool(handle))
    require("new_submit_handle_canonical", handle_valid)
    require(
        "historical_quarantined_handles_exact",
        historical_valid,
    )
    require(
        "new_handle_distinct",
        handle_valid and historical_valid and handle not in historical,
    )
    require("new_handle_quarantined", _is_exact_true(new_handle_quarantined))
    require("logid_absent", _is_exact_true(logid_absent))
    require("queue_status_evidence_absent", _is_exact_true(queue_status_evidence_absent))
    require("provider_task_evidence_absent", _is_exact_true(provider_task_evidence_absent))
    require("successful_output_evidence_absent", _is_exact_true(successful_output_evidence_absent))
    require("provider_task_created_exact_false", _is_exact_false(provider_task_created))
    require(
        "created_task_count_zero",
        isinstance(created_task_count, int)
        and not isinstance(created_task_count, bool)
        and created_task_count == 0,
    )
    credit_count_valid = provider_credit_count is None or (
        _is_numeric(provider_credit_count) and provider_credit_count == 0
    )
    require("provider_credit_count_absent_or_zero", credit_count_valid)
    credits_numeric = _is_numeric(immediate_pre_credit) and _is_numeric(immediate_post_credit)
    require("immediate_credits_numeric", credits_numeric)
    credit_delta_zero = False
    if credits_numeric:
        try:
            credit_delta_zero = immediate_pre_credit - immediate_post_credit == 0
        except (TypeError, ValueError, ArithmeticError):
            credit_delta_zero = False
    require("immediate_credit_delta_zero", credit_delta_zero)
    require("identifier_evidence_stream_pair", stream_pair_valid)
    require("identifier_evidence_rederivation_match", external_result_matches)
    require(
        "identifier_no_contradiction",
        identifiers.get("contradictory_identifiers_present") is False,
    )
    require("selected_submit_matches", identifiers.get("selected_submit_id") == handle and bool(handle))
    require("selected_logid_absent", identifiers.get("selected_logid") is None)
    require(
        "logid_classification_missing",
        identifiers.get("logid_consistency_classification") == "MISSING",
    )
    require("evidence_durable", _is_exact_true(evidence_durable))
    require("evidence_reread_verified", _is_exact_true(evidence_reread_verified))
    later_authorities = {
        "query_authorized": query_authorized,
        "download_authorized": download_authorized,
        "retry_authorized": retry_authorized,
        "resubmit_authorized": resubmit_authorized,
        "batch_authorized": batch_authorized,
    }
    for name, value in later_authorities.items():
        require(f"{name}_false", _is_exact_false(value))

    proven = not failed
    return {
        "provider_task_noncreation_proven": proven,
        "provider_task_creation_proven": False,
        "failed_prerequisites": failed,
        "route_status_code": (
            "CLOSED_PREQUEUE_UPLOAD_FAILURE"
            if proven
            else "CLOSED_NONCREATION_PROOF_FAILED"
        ),
        "route_closed": True,
        "allowance_consumed": _is_exact_true(submit_allowance_consumed),
        "second_submit_permitted": False,
        "query_authorized": False,
        "download_authorized": False,
        "retry_authorized": False,
        "resubmit_authorized": False,
        "batch_authorized": False,
    }


def _require_nonempty_string(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip(ASCII_WHITESPACE):
        raise ValueError(f"{name} must be a nonempty string")
    return value


def _write_all(descriptor: int, payload: bytes) -> None:
    offset = 0
    while offset < len(payload):
        written = os.write(descriptor, payload[offset:])
        if written <= 0:
            raise OSError("exclusive write made no progress")
        offset += written


def _fsync_file(descriptor: int) -> None:
    os.fsync(descriptor)


def _fsync_parent_directory(parent: Path) -> None:
    """Fsync the parent where supported; Windows has no portable directory fsync."""

    directory_flag = getattr(os, "O_DIRECTORY", None)
    if directory_flag is None:
        return
    descriptor: int | None = None
    try:
        descriptor = os.open(str(parent), os.O_RDONLY | directory_flag)
        os.fsync(descriptor)
    except OSError as exc:
        if exc.errno not in {errno.EBADF, errno.EINVAL, errno.ENOTSUP, errno.EPERM}:
            raise
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _verify_persisted_bytes(path: Path, expected: bytes) -> None:
    actual = path.read_bytes()
    if actual != expected:
        raise RuntimeError("exclusive record verification failed")
    strict_json_loads(actual)


def _exclusive_create_bytes(path: Path, payload: bytes) -> None:
    descriptor: int
    try:
        descriptor = os.open(
            str(path),
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0),
            0o600,
        )
    except FileExistsError as exc:
        raise ExclusiveClaimExists(str(path)) from exc

    try:
        _write_all(descriptor, payload)
        _fsync_file(descriptor)
    except BaseException:
        try:
            os.close(descriptor)
        except OSError:
            pass
        raise
    os.close(descriptor)
    _fsync_parent_directory(path.parent)
    _verify_persisted_bytes(path, payload)


def create_exclusive_submit_claim(
    path: str | os.PathLike[str],
    *,
    schema_version: str,
    record_type: str,
    experiment_id: str,
    operation_id: str,
    submit_authorized: bool,
    created_at: str,
) -> dict[str, Any]:
    """Create one durable allowance-consumption claim without replacement."""

    target = Path(path)
    if submit_authorized is not True:
        raise ValueError("submit_authorized must be exactly true")
    _validate_allowance_invocation_pair(True, 1)
    if not target.parent.is_dir():
        raise FileNotFoundError(f"claim parent does not exist: {target.parent}")
    record = {
        "schema_version": _require_nonempty_string("schema_version", schema_version),
        "record_type": _require_nonempty_string("record_type", record_type),
        "experiment_id": _require_nonempty_string("experiment_id", experiment_id),
        "operation_id": _require_nonempty_string("operation_id", operation_id),
        "route_provider_submit_allowance_consumed": True,
        "route_provider_submit_invocation_count": 1,
        "route_status_code": "SUBMIT_INVOCATION_STARTED_ALLOWANCE_CONSUMED",
        "submit_authorized": submit_authorized,
        "query_authorized": False,
        "download_authorized": False,
        "retry_authorized": False,
        "resubmit_authorized": False,
        "batch_authorized": False,
        "created_at": _require_nonempty_string("created_at", created_at),
    }
    payload = canonical_json_bytes(record)
    _exclusive_create_bytes(target, payload)
    return {
        "path": str(target.resolve()),
        "byte_length": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "record": record,
    }


def _validate_authority_flags(authority_flags: Mapping[str, Any]) -> dict[str, bool]:
    if not isinstance(authority_flags, Mapping) or not authority_flags:
        raise TransitionChainError("authority_flags must not be empty")
    result: dict[str, bool] = {}
    for key, value in authority_flags.items():
        if not isinstance(key, str) or not key:
            raise TransitionChainError("authority flag names must be nonempty strings")
        if not isinstance(value, bool):
            raise TransitionChainError(f"authority flag {key} must be boolean")
        result[key] = value
    return result


def _validate_operation_counters(
    operation_counters: Mapping[str, Any],
    *,
    expected_submit_invocation_count: int,
) -> dict[str, int]:
    if not isinstance(operation_counters, Mapping) or not operation_counters:
        raise TransitionChainError("operation_counters must not be empty")
    result: dict[str, int] = {}
    for key, value in operation_counters.items():
        if not isinstance(key, str) or not key:
            raise TransitionChainError("counter names must be nonempty strings")
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise TransitionChainError(f"counter {key} must be a nonnegative integer")
        result[key] = value
    if ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY not in result:
        raise TransitionChainError(
            f"operation_counters must include {ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY}"
        )
    if (
        result[ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY]
        != expected_submit_invocation_count
    ):
        raise TransitionChainError("bound submit invocation counter mismatch")
    return result


def _validate_allowance_invocation_pair(
    allowance_consumed: Any,
    invocation_count: Any,
) -> tuple[bool, int]:
    if not isinstance(allowance_consumed, bool):
        raise TransitionChainError("allowance-consumed state must be boolean")
    if (
        isinstance(invocation_count, bool)
        or not isinstance(invocation_count, int)
        or invocation_count < 0
        or invocation_count > 1
    ):
        raise TransitionChainError("submit invocation count must be zero or one")
    if (allowance_consumed, invocation_count) not in {(False, 0), (True, 1)}:
        raise TransitionChainError(
            "allowance-consumed and invocation-count pair is invalid"
        )
    return allowance_consumed, invocation_count


def _state_shape_findings(
    record: Mapping[str, Any],
    *,
    anchor: bool,
) -> list[str]:
    findings: list[str] = []
    for field in ("schema_version", "record_type", "experiment_id"):
        if not isinstance(record.get(field), str) or not record.get(field):
            findings.append(f"missing_or_invalid_field:{field}")

    allowance = record.get("route_provider_submit_allowance_consumed")
    invocations = record.get("route_provider_submit_invocation_count")
    if not isinstance(allowance, bool):
        findings.append("invalid_allowance_state")
    if (
        isinstance(invocations, bool)
        or not isinstance(invocations, int)
        or invocations < 0
        or invocations > 1
    ):
        findings.append("invalid_submit_invocation_count")
    elif isinstance(allowance, bool) and (allowance, invocations) not in {
        (False, 0),
        (True, 1),
    }:
        findings.append("invalid_allowance_invocation_pair")

    flags = record.get("authority_flags")
    if not isinstance(flags, Mapping) or not flags:
        findings.append("invalid_authority_flags")
    else:
        for key, value in flags.items():
            if not isinstance(key, str) or not key or not isinstance(value, bool):
                findings.append(f"invalid_authority_flag:{key}")

    counters = record.get("operation_counters")
    if not isinstance(counters, Mapping) or not counters:
        findings.append("invalid_operation_counters")
    else:
        for key, value in counters.items():
            if (
                not isinstance(key, str)
                or not key
                or isinstance(value, bool)
                or not isinstance(value, int)
                or value < 0
            ):
                findings.append(f"invalid_operation_counter:{key}")
        if ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY not in counters:
            findings.append("missing_bound_submit_invocation_counter")
        elif _is_nonnegative_integer(invocations) and (
            counters.get(ROUTE_PROVIDER_SUBMIT_INVOCATION_COUNTER_KEY) != invocations
        ):
            findings.append("bound_submit_invocation_counter_mismatch")

    if anchor:
        if not isinstance(record.get("route_status_code"), str) or not record.get(
            "route_status_code"
        ):
            findings.append("missing_or_invalid_field:route_status_code")
        for field in sorted(_TRANSITION_MARKER_FIELDS.intersection(record)):
            findings.append(f"anchor_transition_field_present:{field}")
    else:
        for field in (
            "transition_id",
            "previous_record_path",
            "previous_record_sha256",
            "current_state_code",
            "transition_reason",
            "created_at",
        ):
            if not isinstance(record.get(field), str) or not record.get(field):
                findings.append(f"missing_or_invalid_field:{field}")
        sequence = record.get("sequence_number")
        if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 1:
            findings.append("invalid_sequence_number")
        previous_hash = record.get("previous_record_sha256")
        if not isinstance(previous_hash, str) or SHA256_RE.fullmatch(previous_hash) is None:
            findings.append("invalid_previous_record_sha256")
    return list(dict.fromkeys(findings))


def create_append_only_transition(
    path: str | os.PathLike[str],
    *,
    schema_version: str,
    record_type: str,
    experiment_id: str,
    transition_id: str,
    sequence_number: int,
    previous_record_path: str | os.PathLike[str],
    previous_record_sha256: str,
    current_state_code: str,
    transition_reason: str,
    authority_flags: Mapping[str, bool],
    operation_counters: Mapping[str, int],
    route_provider_submit_allowance_consumed: bool,
    route_provider_submit_invocation_count: int,
    created_at: str,
) -> dict[str, Any]:
    """Create one immutable transition after verifying its exact predecessor."""

    target = Path(path)
    previous = Path(previous_record_path).resolve()
    validated_schema_version = _require_nonempty_string("schema_version", schema_version)
    validated_experiment_id = _require_nonempty_string("experiment_id", experiment_id)
    if not target.parent.is_dir():
        raise FileNotFoundError(f"transition parent does not exist: {target.parent}")
    if (
        isinstance(sequence_number, bool)
        or not isinstance(sequence_number, int)
        or sequence_number < 1
    ):
        raise TransitionChainError("sequence_number must be a positive integer")
    if not SHA256_RE.fullmatch(str(previous_record_sha256)):
        raise TransitionChainError("previous_record_sha256 must be lowercase SHA-256")
    try:
        previous_record, previous_bytes = _read_canonical_json_record(previous)
    except (OSError, StrictJSONError) as exc:
        raise TransitionChainError("previous record is absent or noncanonical") from exc
    actual_previous_sha = hashlib.sha256(previous_bytes).hexdigest()
    if actual_previous_sha != previous_record_sha256:
        raise TransitionChainError("previous record SHA-256 mismatch")

    previous_is_anchor = not any(
        field in previous_record for field in _TRANSITION_MARKER_FIELDS
    )
    previous_findings = _state_shape_findings(
        previous_record,
        anchor=previous_is_anchor,
    )
    if previous_findings:
        raise TransitionChainError(
            "previous record has invalid state shape: " + ", ".join(previous_findings)
        )
    if previous_record["experiment_id"] != validated_experiment_id:
        raise TransitionChainError("predecessor experiment_id mismatch")
    if previous_record["schema_version"] != validated_schema_version:
        raise TransitionChainError("predecessor schema_version mismatch")

    _validate_allowance_invocation_pair(
        route_provider_submit_allowance_consumed,
        route_provider_submit_invocation_count,
    )
    validated_flags = _validate_authority_flags(authority_flags)
    validated_counters = _validate_operation_counters(
        operation_counters,
        expected_submit_invocation_count=route_provider_submit_invocation_count,
    )

    expected_sequence = 1
    if not previous_is_anchor:
        previous_sequence = previous_record.get("sequence_number")
        if isinstance(previous_sequence, bool) or not isinstance(previous_sequence, int):
            raise TransitionChainError("previous record has invalid sequence_number")
        expected_sequence = previous_sequence + 1
    if sequence_number != expected_sequence:
        raise TransitionChainError(
            f"sequence_number must be exactly {expected_sequence} for this predecessor"
        )

    previous_allowance = previous_record["route_provider_submit_allowance_consumed"]
    previous_invocations = previous_record["route_provider_submit_invocation_count"]
    previous_counters = previous_record["operation_counters"]
    if previous_allowance and not route_provider_submit_allowance_consumed:
        raise TransitionChainError("submit allowance cannot be restored")
    if route_provider_submit_invocation_count < previous_invocations:
        raise TransitionChainError("submit invocation count cannot decrease")
    for key, previous_value in previous_counters.items():
        current_value = validated_counters.get(key)
        if current_value is None or current_value < previous_value:
            raise TransitionChainError(f"operation counter cannot decrease: {key}")

    record = {
        "schema_version": validated_schema_version,
        "record_type": _require_nonempty_string("record_type", record_type),
        "experiment_id": validated_experiment_id,
        "transition_id": _require_nonempty_string("transition_id", transition_id),
        "sequence_number": sequence_number,
        "previous_record_path": str(previous),
        "previous_record_sha256": previous_record_sha256,
        "current_state_code": _require_nonempty_string("current_state_code", current_state_code),
        "transition_reason": _require_nonempty_string("transition_reason", transition_reason),
        "authority_flags": validated_flags,
        "operation_counters": validated_counters,
        "route_provider_submit_allowance_consumed": route_provider_submit_allowance_consumed,
        "route_provider_submit_invocation_count": route_provider_submit_invocation_count,
        "created_at": _require_nonempty_string("created_at", created_at),
    }
    current_findings = _state_shape_findings(record, anchor=False)
    if current_findings:
        raise TransitionChainError(
            "new transition has invalid state shape: " + ", ".join(current_findings)
        )
    payload = canonical_json_bytes(record)
    try:
        _exclusive_create_bytes(target, payload)
    except ExclusiveClaimExists as exc:
        raise TransitionChainError(f"transition path already exists: {target}") from exc
    return {
        "path": str(target.resolve()),
        "byte_length": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "record": record,
    }


def _normalized_path(value: str | os.PathLike[str]) -> str:
    return str(Path(value).resolve())


def _record_state_snapshot(record: Mapping[str, Any]) -> tuple[Any, ...]:
    return (
        record.get("route_provider_submit_allowance_consumed"),
        record.get("route_provider_submit_invocation_count"),
        json.dumps(record.get("authority_flags"), sort_keys=True),
        json.dumps(record.get("operation_counters"), sort_keys=True),
    )


def validate_transition_chain(
    anchor_record_path: str | os.PathLike[str],
    transition_paths: Sequence[str | os.PathLike[str]],
) -> dict[str, Any]:
    """Validate one canonical, append-only, monotonic transition chain."""

    findings: list[str] = []
    anchor_path = _normalized_path(anchor_record_path)
    normalized_paths = [_normalized_path(path) for path in transition_paths]
    if len(normalized_paths) != len(set(normalized_paths)):
        findings.append("duplicate_path")

    records: dict[str, dict[str, Any]] = {}
    raw_by_path: dict[str, bytes] = {}
    for path in [anchor_path, *dict.fromkeys(normalized_paths)]:
        try:
            record, raw = _read_canonical_json_record(Path(path))
        except (OSError, StrictJSONError):
            findings.append(f"noncanonical_or_unreadable_record:{path}")
            continue
        records[path] = record
        raw_by_path[path] = raw

    transition_records = {
        path: records[path] for path in dict.fromkeys(normalized_paths) if path in records
    }

    anchor_experiment_id: str | None = None
    anchor_schema_version: str | None = None
    if anchor_path in records:
        anchor_record = records[anchor_path]
        for finding in _state_shape_findings(anchor_record, anchor=True):
            findings.append(f"{finding}:{anchor_path}")
        if isinstance(anchor_record.get("experiment_id"), str) and anchor_record.get(
            "experiment_id"
        ):
            anchor_experiment_id = anchor_record["experiment_id"]
        if isinstance(anchor_record.get("schema_version"), str) and anchor_record.get(
            "schema_version"
        ):
            anchor_schema_version = anchor_record["schema_version"]
    for path, record in transition_records.items():
        for finding in _state_shape_findings(record, anchor=False):
            findings.append(f"{finding}:{path}")
        if (
            anchor_experiment_id is not None
            and record.get("experiment_id") != anchor_experiment_id
        ):
            findings.append(f"experiment_id_mismatch:{path}")
        if (
            anchor_schema_version is not None
            and record.get("schema_version") != anchor_schema_version
        ):
            findings.append(f"schema_version_mismatch:{path}")

    sequence_to_paths: dict[int, list[str]] = {}
    for path, record in transition_records.items():
        sequence = record.get("sequence_number")
        if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 1:
            findings.append(f"invalid_sequence_number:{path}")
            continue
        sequence_to_paths.setdefault(sequence, []).append(path)
    for sequence, paths in sequence_to_paths.items():
        if len(paths) > 1:
            findings.append(f"duplicate_sequence:{sequence}")

    ordered_paths = [
        paths[0] for _, paths in sorted(sequence_to_paths.items()) if len(paths) == 1
    ]
    ordered_sequences = sorted(sequence_to_paths)
    if normalized_paths and (not ordered_sequences or ordered_sequences[0] != 1):
        findings.append("first_sequence_not_one")
    if ordered_sequences and ordered_sequences != list(range(1, max(ordered_sequences) + 1)):
        findings.append("sequence_gap")

    known_paths = {anchor_path, *transition_records}
    children: dict[str, list[str]] = {}
    for path, record in transition_records.items():
        previous_value = record.get("previous_record_path")
        if not isinstance(previous_value, str) or not previous_value:
            findings.append(f"missing_previous_record_path:{path}")
            continue
        previous_path = _normalized_path(previous_value)
        children.setdefault(previous_path, []).append(path)
        if previous_path not in known_paths:
            findings.append(f"orphan:{path}")
        expected_hash = record.get("previous_record_sha256")
        if previous_path in raw_by_path:
            actual_hash = hashlib.sha256(raw_by_path[previous_path]).hexdigest()
            if expected_hash != actual_hash:
                findings.append(f"previous_hash_mismatch:{path}")
    for parent, child_paths in children.items():
        if len(child_paths) > 1:
            findings.append(f"fork:{parent}")

    for path in transition_records:
        visited: set[str] = set()
        cursor = path
        while cursor in transition_records:
            if cursor in visited:
                findings.append(f"cycle:{path}")
                break
            visited.add(cursor)
            previous_value = transition_records[cursor].get("previous_record_path")
            if not isinstance(previous_value, str):
                break
            cursor = _normalized_path(previous_value)

    previous_path = anchor_path
    previous_record = records.get(anchor_path)
    seen_state: dict[str, tuple[Any, ...]] = {}
    for path in ordered_paths:
        record = transition_records[path]
        expected_previous = _normalized_path(str(record.get("previous_record_path", "")))
        if expected_previous != previous_path:
            findings.append(f"prior_path_mismatch:{path}")
        if previous_record is not None:
            prior_allowance = previous_record.get("route_provider_submit_allowance_consumed")
            current_allowance = record.get("route_provider_submit_allowance_consumed")
            if not isinstance(current_allowance, bool):
                findings.append(f"invalid_allowance_state:{path}")
            if prior_allowance is True and current_allowance is False:
                findings.append(f"allowance_restoration:{path}")
            prior_invocations = previous_record.get("route_provider_submit_invocation_count")
            current_invocations = record.get("route_provider_submit_invocation_count")
            if (
                isinstance(current_invocations, bool)
                or not isinstance(current_invocations, int)
                or current_invocations < 0
                or current_invocations > 1
            ):
                findings.append(f"invalid_submit_invocation_count:{path}")
            elif isinstance(prior_invocations, int) and not isinstance(prior_invocations, bool):
                if current_invocations < prior_invocations:
                    findings.append(f"decreasing_submit_invocation_count:{path}")

            prior_counters = previous_record.get("operation_counters", {})
            current_counters = record.get("operation_counters")
            if not isinstance(prior_counters, dict) or not isinstance(current_counters, dict):
                findings.append(f"invalid_operation_counters:{path}")
            else:
                for key, prior_value in prior_counters.items():
                    current_value = current_counters.get(key)
                    if (
                        isinstance(prior_value, bool)
                        or not isinstance(prior_value, int)
                        or isinstance(current_value, bool)
                        or not isinstance(current_value, int)
                        or current_value < prior_value
                    ):
                        findings.append(f"decreasing_operation_counter:{path}:{key}")
                for key, current_value in current_counters.items():
                    if isinstance(current_value, bool) or not isinstance(current_value, int) or current_value < 0:
                        findings.append(f"invalid_operation_counter:{path}:{key}")

        state_code = record.get("current_state_code")
        if not isinstance(state_code, str) or not state_code:
            findings.append(f"invalid_current_state_code:{path}")
        else:
            snapshot = _record_state_snapshot(record)
            if state_code in seen_state and seen_state[state_code] != snapshot:
                findings.append(f"contradictory_duplicate_state:{state_code}")
            seen_state[state_code] = snapshot
        previous_path = path
        previous_record = record

    unique_findings = list(dict.fromkeys(findings))
    valid = not unique_findings and len(transition_records) == len(set(normalized_paths))
    terminal_path = ordered_paths[-1] if valid and ordered_paths else anchor_path if valid else None
    terminal_record = records.get(terminal_path) if terminal_path is not None else None
    terminal_state = (
        terminal_record.get("current_state_code")
        or terminal_record.get("route_status_code")
        if terminal_record is not None
        else None
    )
    terminal_hash = (
        hashlib.sha256(raw_by_path[terminal_path]).hexdigest()
        if terminal_path is not None and terminal_path in raw_by_path
        else None
    )
    return {
        "valid": valid,
        "ordered_paths": ordered_paths,
        "terminal_state": terminal_state,
        "terminal_hash": terminal_hash,
        "finding_details": unique_findings,
    }
