from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Callable, Mapping

from .builder import RuntimeStateProtectionPolicy, validate_state_root
from .errors import PromotionError
from .identity import canonical_json_bytes, pointer_from_meta, validate_pointer
from .verify import require_valid_generation


POINTER_FILENAME = "current_read_model.json"
POINTER_TEMP_FILENAME = "current_read_model.json.partial"


def read_pointer(path: str | Path) -> dict[str, Any]:
    pointer_path = Path(path)
    if pointer_path.is_symlink() or not pointer_path.is_file():
        raise PromotionError("pointer is absent, non-regular, or a symlink")
    raw = pointer_path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise PromotionError("pointer must contain exactly one terminal LF")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PromotionError("pointer is not strict UTF-8 JSON") from error
    validate_pointer(value)
    if raw != canonical_json_bytes(value, terminal_lf=True):
        raise PromotionError("pointer is not canonical JSON")
    return value


def _write_exclusive(path: Path, data: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    descriptor = os.open(path, flags, 0o600)
    try:
        view = memoryview(data)
        offset = 0
        while offset < len(view):
            written = os.write(descriptor, view[offset:])
            if written <= 0:
                raise OSError("pointer write made no progress")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def promote_generation(
    generation_path: str | Path,
    *,
    protection_policy: RuntimeStateProtectionPolicy | None = None,
    replace_operation: Callable[[str | bytes | Path, str | bytes | Path], None] = os.replace,
) -> Mapping[str, Any]:
    requested_generation = Path(generation_path)
    root = validate_state_root(
        requested_generation.parent,
        protection_policy=protection_policy,
    )
    generation = requested_generation.resolve(strict=True)
    if generation.parent != root:
        raise PromotionError("generation must resolve inside the validated state root")
    validation = require_valid_generation(generation)
    pointer_path = root / POINTER_FILENAME
    temporary = root / POINTER_TEMP_FILENAME
    if temporary.exists():
        raise PromotionError("pointer temporary path already exists")
    pointer = pointer_from_meta(validation.metadata, generation.name)
    _write_exclusive(temporary, canonical_json_bytes(pointer, terminal_lf=True))
    try:
        if pointer_path.exists():
            replace_operation(temporary, pointer_path)
        else:
            os.rename(temporary, pointer_path)
    except Exception as error:
        raise PromotionError("atomic pointer promotion failed") from error
    observed = read_pointer(pointer_path)
    postcheck = require_valid_generation(generation, pointer=observed)
    if not postcheck.valid:
        raise PromotionError("post-promotion generation verification failed")
    return observed


def resolve_current(state_root: str | Path) -> tuple[Path, Mapping[str, Any]]:
    root = Path(state_root).resolve(strict=True)
    pointer = read_pointer(root / POINTER_FILENAME)
    generation = root / str(pointer["generation_filename"])
    require_valid_generation(generation, pointer=pointer)
    return generation, pointer
