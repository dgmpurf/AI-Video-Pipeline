from __future__ import annotations

import os
import sqlite3
import stat
from dataclasses import dataclass
from pathlib import Path

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


@dataclass(frozen=True)
class RuntimeStateProtectionPolicy:
    repository_root: str | Path
    source_root: str | Path
    media_roots: tuple[str | Path, ...]


def _resolve_protected_root(value: str | Path, *, role: str) -> Path:
    try:
        root = Path(value)
    except TypeError as error:
        raise UnsafePathError(f"{role} must be an explicit absolute path") from error
    if not root.is_absolute():
        raise UnsafePathError(f"{role} must be an explicit absolute path")
    return root.resolve(strict=False)


def _protected_roots(policy: RuntimeStateProtectionPolicy | None) -> tuple[Path, ...]:
    if not isinstance(policy, RuntimeStateProtectionPolicy):
        raise UnsafePathError("complete runtime-state protection policy is required")
    if isinstance(policy.media_roots, (str, bytes, Path)) or not policy.media_roots:
        raise UnsafePathError("runtime-state protection policy requires one or more media roots")
    repository = _resolve_protected_root(policy.repository_root, role="repository root")
    source = _resolve_protected_root(policy.source_root, role="Source root")
    media = tuple(
        _resolve_protected_root(root, role="media root") for root in policy.media_roots
    )
    return (repository, source, *media)


def _is_within(path: Path, boundary: Path) -> bool:
    candidate_text = os.path.normcase(str(path))
    boundary_text = os.path.normcase(str(boundary))
    try:
        return os.path.commonpath((candidate_text, boundary_text)) == boundary_text
    except ValueError:
        return False


def _is_reparse_point(path: Path) -> bool:
    reparse = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    attributes = getattr(os.lstat(path), "st_file_attributes", 0)
    return bool(reparse and attributes & reparse)


def _reject_link_or_reparse_traversal(path: Path) -> None:
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise UnsafePathError("state root may not traverse a symlink")
        try:
            reparse_point = _is_reparse_point(parent)
        except FileNotFoundError:
            continue
        if reparse_point:
            raise UnsafePathError("state root may not traverse a reparse point")


def validate_state_root(
    path: str | Path,
    *,
    protection_policy: RuntimeStateProtectionPolicy | None = None,
) -> Path:
    protected_roots = _protected_roots(protection_policy)
    raw = Path(path)
    if not raw.is_absolute():
        raise UnsafePathError("state root must be an explicit absolute path")
    _reject_link_or_reparse_traversal(raw)
    resolved = raw.resolve(strict=False)
    for boundary in protected_roots:
        if _is_within(resolved, boundary):
            raise UnsafePathError(f"state root is inside a protected boundary: {boundary}")
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
