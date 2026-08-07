from __future__ import annotations

import hashlib
import json
import math
from typing import Any, Mapping

from .errors import IdentityError


def _validate_json(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value) or (value == 0 and math.copysign(1.0, value) < 0):
            raise IdentityError(f"non-canonical number at {path}")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            _validate_json(child, f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise IdentityError(f"non-string JSON key at {path}")
            _validate_json(child, f"{path}.{key}")
        return
    raise IdentityError(f"unsupported JSON value at {path}: {type(value).__name__}")


def canonical_json_bytes(value: Any, *, terminal_lf: bool = False) -> bytes:
    _validate_json(value)
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


def canonicalize_bounded_json(value: Any) -> str:
    if isinstance(value, str):
        def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            result: dict[str, Any] = {}
            for key, child in pairs:
                if key in result:
                    raise IdentityError(f"duplicate bounded JSON key: {key}")
                result[key] = child
            return result

        try:
            parsed = json.loads(
                value,
                object_pairs_hook=strict_object,
                parse_constant=lambda token: (_ for _ in ()).throw(
                    IdentityError(f"non-finite bounded JSON number: {token}")
                ),
            )
        except (json.JSONDecodeError, IdentityError) as error:
            raise IdentityError("bounded JSON text is invalid") from error
    else:
        parsed = value
    return canonical_json_text(parsed)
