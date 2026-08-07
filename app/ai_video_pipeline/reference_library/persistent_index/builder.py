from __future__ import annotations

import os
import sqlite3
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .enums import READ_MODEL_SCHEMA_VERSION
from .errors import BuildError, UnsafePathError
from .identity import generation_filename, logical_content_hash
from .mapper import MappedReadModel
from .schema import create_schema, insert_rows, populate_fts, require_fts5
from .verify import VerificationResult, verify_generation


LOCK_FILENAME = "rl_p2_builder.lock"


@dataclass(frozen=True)
class BuildResult:
    generation_path: Path
    logical_content_hash: str
    materialization_generation_id: str
    verification: VerificationResult


def validate_state_root(path: str | Path, *, forbidden_roots: Iterable[str | Path] = ()) -> Path:
    raw = Path(path)
    if not raw.is_absolute():
        raise UnsafePathError("state root must be an explicit absolute path")
    resolved = raw.resolve(strict=False)
    for parent in (resolved, *resolved.parents):
        if parent.exists() and parent.is_symlink():
            raise UnsafePathError("state root may not traverse a symlink")
        attributes = getattr(parent.stat(), "st_file_attributes", 0) if parent.exists() else 0
        reparse = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if reparse and attributes & reparse:
            raise UnsafePathError("state root may not traverse a reparse point")
    for forbidden in forbidden_roots:
        boundary = Path(forbidden).resolve(strict=False)
        try:
            resolved.relative_to(boundary)
        except ValueError:
            continue
        raise UnsafePathError(f"state root is inside a protected boundary: {boundary}")
    return resolved


def _exclusive_lock(path: Path) -> int:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    return os.open(path, flags, 0o600)


def build_generation(
    state_root: str | Path,
    mapped: MappedReadModel,
    *,
    forbidden_roots: Iterable[str | Path] = (),
) -> BuildResult:
    root = validate_state_root(state_root, forbidden_roots=forbidden_roots)
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / LOCK_FILENAME
    lock_descriptor = _exclusive_lock(lock_path)
    staging = root / (
        f"rl_p2--{READ_MODEL_SCHEMA_VERSION}--"
        f"{mapped.materialization_generation_id}.partial.sqlite3"
    )
    if staging.exists():
        os.close(lock_descriptor)
        raise BuildError("deterministic staging path already exists")
    success = False
    try:
        connection = sqlite3.connect(staging)
        try:
            create_schema(connection)
            require_fts5(connection)
            insert_rows(connection, mapped.rows)
            populate_fts(connection)
            connection.commit()
            logical_hash = logical_content_hash(connection)
            connection.execute(
                "UPDATE read_model_meta SET logical_content_hash=? WHERE meta_id=1",
                (logical_hash,),
            )
            connection.commit()
        finally:
            connection.close()
        candidate = verify_generation(staging, require_final_filename=False)
        if not candidate.valid:
            raise BuildError(f"candidate verification failed: {candidate.diagnostics}")
        final = root / generation_filename(mapped.materialization_generation_id, logical_hash)
        if final.exists():
            raise BuildError("immutable generation filename collision")
        os.rename(staging, final)
        final_verification = verify_generation(final)
        if not final_verification.valid:
            raise BuildError(f"final generation verification failed: {final_verification.diagnostics}")
        success = True
        return BuildResult(final, logical_hash, mapped.materialization_generation_id, final_verification)
    finally:
        os.close(lock_descriptor)
        if success:
            lock_path.unlink()
