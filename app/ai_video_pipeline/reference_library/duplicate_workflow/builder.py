from __future__ import annotations

import os
import sqlite3
import stat
from pathlib import Path

from .enums import READ_MODEL_SCHEMA_VERSION
from .errors import BuildError, UnsafePathError
from .identity import generation_filename, logical_content_hash, path_is_within
from .models import BuildResult, MappedReadModel, RuntimeStateProtectionPolicy
from .schema import create_schema, insert_rows
from .verify import verify_generation


LOCK_FILENAME = "rl_p3_builder.lock"


def _absolute_root(value: str | Path, *, role: str) -> Path:
    try:
        raw = Path(value)
    except TypeError as error:
        raise UnsafePathError(f"{role} must be an explicit absolute path") from error
    if not raw.is_absolute():
        raise UnsafePathError(f"{role} must be an explicit absolute path")
    return raw.resolve(strict=False)


def _protected_roots(
    policy: RuntimeStateProtectionPolicy | None,
) -> tuple[Path, ...]:
    if not isinstance(policy, RuntimeStateProtectionPolicy):
        raise UnsafePathError("complete runtime-state protection policy is required")
    if isinstance(policy.media_roots, (str, bytes, Path)) or not policy.media_roots:
        raise UnsafePathError("protection policy requires one or more media roots")
    return (
        _absolute_root(policy.repository_root, role="repository root"),
        _absolute_root(policy.source_root, role="Source root"),
        *(
            _absolute_root(root, role="media root")
            for root in policy.media_roots
        ),
    )


def _is_reparse_point(path: Path) -> bool:
    marker = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    attributes = getattr(os.lstat(path), "st_file_attributes", 0)
    return bool(marker and attributes & marker)


def _reject_link_or_reparse_traversal(path: Path) -> None:
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise UnsafePathError("state root may not traverse a symlink")
        try:
            if _is_reparse_point(candidate):
                raise UnsafePathError("state root may not traverse a reparse point")
        except FileNotFoundError:
            continue


def validate_state_root(
    path: str | Path,
    *,
    protection_policy: RuntimeStateProtectionPolicy | None = None,
) -> Path:
    protected = _protected_roots(protection_policy)
    try:
        raw = Path(path)
    except TypeError as error:
        raise UnsafePathError("state root must be an explicit absolute path") from error
    if not raw.is_absolute():
        raise UnsafePathError("state root must be an explicit absolute path")
    _reject_link_or_reparse_traversal(raw)
    resolved = raw.resolve(strict=False)
    if any(path_is_within(resolved, boundary) for boundary in protected):
        raise UnsafePathError("state root is inside a protected boundary")
    return resolved


def _exclusive_lock(path: Path) -> int:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    return os.open(path, flags, 0o600)


def build_generation(
    state_root: str | Path,
    mapped: MappedReadModel,
    *,
    protection_policy: RuntimeStateProtectionPolicy | None = None,
) -> BuildResult:
    root = validate_state_root(state_root, protection_policy=protection_policy)
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / LOCK_FILENAME
    descriptor = _exclusive_lock(lock_path)
    staging = root / (
        f"rl_p3--{READ_MODEL_SCHEMA_VERSION}--"
        f"{mapped.materialization_generation_id}.partial.sqlite3"
    )
    success = False
    try:
        if staging.exists():
            raise BuildError("deterministic staging path already exists")
        connection = sqlite3.connect(staging)
        try:
            create_schema(connection)
            insert_rows(connection, mapped.rows)
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
        final = root / generation_filename(
            mapped.materialization_generation_id, logical_hash
        )
        if final.exists():
            raise BuildError("immutable generation filename collision")
        os.rename(staging, final)
        verification = verify_generation(final)
        if not verification.valid:
            raise BuildError(f"final generation verification failed: {verification.diagnostics}")
        success = True
        return BuildResult(
            final,
            logical_hash,
            mapped.materialization_generation_id,
            verification,
        )
    finally:
        os.close(descriptor)
        if success:
            lock_path.unlink()
