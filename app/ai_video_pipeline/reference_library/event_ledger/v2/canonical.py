from __future__ import annotations

import hashlib
import json
import math
import re
from datetime import datetime
from typing import Any, Mapping

from .errors import CanonicalizationError, SchemaValidationError


SHA256_RE = re.compile(r"^[0-9a-f]{64}$", flags=re.ASCII)
RFC3339_UTC_RE = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T"
    r"[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]+)?Z$",
    flags=re.ASCII,
)


def _reject_constant(value: str) -> Any:
    raise CanonicalizationError(f"non-finite JSON token is forbidden: {value}")


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CanonicalizationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(value: str | bytes | bytearray) -> Any:
    if isinstance(value, (bytes, bytearray)):
        raw = bytes(value)
        if raw.startswith(b"\xef\xbb\xbf"):
            raise CanonicalizationError("UTF-8 BOM is forbidden")
        try:
            text = raw.decode("utf-8", errors="strict")
        except UnicodeDecodeError as error:
            raise CanonicalizationError("input is not strict UTF-8") from error
    elif isinstance(value, str):
        text = value
        if text.startswith("\ufeff"):
            raise CanonicalizationError("UTF-8 BOM is forbidden")
    else:
        raise TypeError("strict_json_loads accepts text or bytes")
    try:
        return json.loads(
            text,
            object_pairs_hook=_strict_object,
            parse_constant=_reject_constant,
        )
    except CanonicalizationError:
        raise
    except json.JSONDecodeError as error:
        raise CanonicalizationError(f"invalid JSON: {error}") from error


def validate_json_value(value: Any, *, path: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value) or (value == 0 and math.copysign(1.0, value) < 0):
            raise CanonicalizationError(f"non-canonical number at {path}")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            validate_json_value(child, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise CanonicalizationError(f"non-string key at {path}")
            validate_json_value(child, path=f"{path}.{key}")
        return
    raise CanonicalizationError(
        f"unsupported JSON value at {path}: {type(value).__name__}"
    )


def canonical_json_bytes(value: Any, *, terminal_lf: bool = False) -> bytes:
    validate_json_value(value)
    text = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return (text + ("\n" if terminal_lf else "")).encode("utf-8")


def canonical_json_text(value: Any, *, terminal_lf: bool = False) -> str:
    return canonical_json_bytes(value, terminal_lf=terminal_lf).decode("utf-8")


def sha256_hex(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_sha256(value: Any) -> str:
    return sha256_hex(canonical_json_bytes(value))


def require_exact_keys(
    value: Mapping[str, Any],
    expected: set[str] | frozenset[str],
    *,
    field: str,
) -> None:
    actual = set(value)
    expected_set = set(expected)
    if actual != expected_set:
        raise SchemaValidationError(
            f"{field} keys differ; missing={sorted(expected_set - actual)}, "
            f"unexpected={sorted(actual - expected_set)}"
        )


def require_nonempty_string(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise SchemaValidationError(f"{field} must be a nonempty string")
    return value


def require_sha256(value: Any, *, field: str, nullable: bool = False) -> None:
    if value is None and nullable:
        return
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise SchemaValidationError(f"{field} must be lowercase SHA-256")


def binary_sorted(values: list[str] | tuple[str, ...]) -> list[str]:
    return sorted(values, key=lambda item: item.encode("utf-8"))


def require_sorted_unique_strings(
    value: Any,
    *,
    field: str,
    nonempty: bool = False,
    exact_length: int | None = None,
) -> tuple[str, ...]:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        raise SchemaValidationError(f"{field} must be an array of nonempty strings")
    if nonempty and not value:
        raise SchemaValidationError(f"{field} must not be empty")
    if exact_length is not None and len(value) != exact_length:
        raise SchemaValidationError(f"{field} must contain exactly {exact_length} values")
    if len(value) != len(set(value)):
        raise SchemaValidationError(f"{field} must contain unique values")
    if value != binary_sorted(value):
        raise SchemaValidationError(f"{field} must be bytewise sorted")
    return tuple(value)


def require_rfc3339_utc(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or RFC3339_UTC_RE.fullmatch(value) is None:
        raise SchemaValidationError(f"{field} must be explicit RFC3339 UTC")
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as error:
        raise SchemaValidationError(f"{field} is not a valid timestamp") from error
    return value
