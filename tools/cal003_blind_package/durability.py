"""Writable file durability and verified atomic ZIP publication."""

from __future__ import annotations

import hashlib
import os
import re
import stat
import zipfile
from pathlib import Path, PurePosixPath
from typing import Callable, Collection, Iterable, Mapping, Optional

from .failure_state import FailurePhase, OperationCode, PhaseTracker

CommitmentVerifier = Callable[[Path], bool]


def _require_regular_file(path: Path) -> None:
    if path.is_symlink():
        raise ValueError("symlinks are not accepted")
    if not path.exists() or not path.is_file():
        raise ValueError("path must be an existing regular file")
    attributes = getattr(path.stat(), "st_file_attributes", 0)
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    if reparse_flag and attributes & reparse_flag:
        raise ValueError("reparse points are not accepted")


def flush_file_durable(
    path: Path,
    *,
    tracker: PhaseTracker,
    phase: FailurePhase,
    operation: OperationCode,
) -> None:
    """Flush and fsync an existing file through a writable binary handle."""

    path = Path(path)
    tracker.transition(phase, operation)
    _require_regular_file(path)
    with path.open("r+b") as handle:
        handle.flush()
        os.fsync(handle.fileno())


def _validate_member_name(name: str) -> None:
    normalized = name.replace("\\", "/")
    if (
        normalized.startswith("/")
        or re.match(r"^[A-Za-z]:", normalized)
        or PurePosixPath(normalized).is_absolute()
    ):
        raise ValueError("absolute ZIP member names are forbidden")
    if ".." in PurePosixPath(normalized).parts:
        raise ValueError("ZIP member traversal is forbidden")


def validate_zip_archive(
    path: Path,
    *,
    expected_members: Collection[str],
    expected_member_hashes: Mapping[str, str],
    commitment_verifier: CommitmentVerifier,
    tracker: PhaseTracker,
    phase: FailurePhase,
    operation: OperationCode,
) -> None:
    """Validate exact members, hashes, integrity, and a caller commitment."""

    path = Path(path)
    tracker.transition(phase, operation)
    _require_regular_file(path)
    expected = set(expected_members)
    if set(expected_member_hashes) != expected:
        raise ValueError("expected hash keys must match expected members")
    with zipfile.ZipFile(path, "r") as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        for name in names:
            _validate_member_name(name)
        if len(names) != len(set(names)):
            raise ValueError("duplicate ZIP members are forbidden")
        if set(names) != expected:
            raise ValueError("ZIP member set does not match")
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity test failed")
        for name in names:
            digest = hashlib.sha256(archive.read(name)).hexdigest()
            if digest != expected_member_hashes[name]:
                raise ValueError("ZIP member hash does not match")
    if commitment_verifier(path) is not True:
        raise ValueError("commitment verification failed")


def _volume_identity(path: Path) -> tuple[str, str]:
    resolved = path.resolve(strict=False)
    if resolved.drive:
        return ("drive", resolved.drive.casefold())
    parent = resolved if resolved.exists() else resolved.parent
    while not parent.exists() and parent != parent.parent:
        parent = parent.parent
    return ("device", str(parent.stat().st_dev))


def atomic_publish_verified_zip(
    partial_path: Path,
    final_path: Path,
    *,
    expected_members: Collection[str],
    expected_member_hashes: Mapping[str, str],
    commitment_verifier: CommitmentVerifier,
    tracker: PhaseTracker,
) -> None:
    """Durably validate, atomically publish, and revalidate one ZIP."""

    partial = Path(partial_path)
    final = Path(final_path)
    if _volume_identity(partial) != _volume_identity(final):
        raise ValueError("partial and final paths must share one volume")
    if final.exists() or final.is_symlink():
        raise FileExistsError("final path must be absent")
    _require_regular_file(partial)
    flush_file_durable(
        partial,
        tracker=tracker,
        phase=FailurePhase.SEALED_PACKAGE_FILE_FLUSH,
        operation=OperationCode.FLUSH_PARTIAL_ZIP,
    )
    validate_zip_archive(
        partial,
        expected_members=expected_members,
        expected_member_hashes=expected_member_hashes,
        commitment_verifier=commitment_verifier,
        tracker=tracker,
        phase=FailurePhase.SEALED_ZIP_INTEGRITY,
        operation=OperationCode.VERIFY_PARTIAL_ZIP,
    )
    tracker.transition(FailurePhase.ATOMIC_RENAME, OperationCode.ATOMIC_REPLACE)
    os.replace(partial, final)
    flush_file_durable(
        final,
        tracker=tracker,
        phase=FailurePhase.FINAL_PACKAGE_FILE_FLUSH,
        operation=OperationCode.FLUSH_FINAL_ZIP,
    )
    validate_zip_archive(
        final,
        expected_members=expected_members,
        expected_member_hashes=expected_member_hashes,
        commitment_verifier=commitment_verifier,
        tracker=tracker,
        phase=FailurePhase.FINAL_ZIP_INTEGRITY,
        operation=OperationCode.VERIFY_FINAL_ZIP,
    )
    tracker.transition(FailurePhase.COMPLETE, OperationCode.VERIFY_FINAL_ZIP)


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def cleanup_task_created_paths(
    paths: Iterable[Path],
    *,
    allowed_root: Path,
    tracker: PhaseTracker,
    governed_final_path: Optional[Path] = None,
    repository_root: Optional[Path] = None,
) -> dict[str, int]:
    """Remove only explicit regular-file paths confined to an allowed root."""

    tracker.transition(
        FailurePhase.CLEANUP,
        OperationCode.CLEANUP_TASK_CREATED_PATHS,
    )
    root = Path(allowed_root).resolve(strict=False)
    governed = (
        Path(governed_final_path).resolve(strict=False)
        if governed_final_path is not None
        else None
    )
    repository = (
        Path(repository_root).resolve(strict=False)
        if repository_root is not None
        else None
    )
    requested = 0
    removed = 0
    already_absent = 0
    for raw_path in paths:
        requested += 1
        raw = Path(raw_path)
        if raw.is_symlink():
            raise ValueError("cleanup does not follow symlinks")
        candidate = raw.resolve(strict=False)
        if candidate == root or not _is_within(candidate, root):
            raise ValueError("cleanup path escapes the allowlisted root")
        if governed is not None and candidate == governed:
            raise ValueError("governed final path is protected")
        if repository is not None and _is_within(candidate, repository):
            raise ValueError("repository paths are protected")
        if not candidate.exists():
            already_absent += 1
            continue
        if not candidate.is_file():
            raise ValueError("cleanup accepts regular files only")
        candidate.unlink()
        removed += 1
    return {
        "already_absent": already_absent,
        "removed": removed,
        "requested": requested,
    }
