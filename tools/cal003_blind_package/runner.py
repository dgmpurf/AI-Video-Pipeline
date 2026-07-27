"""Bounded orchestration for verified ZIP persistence."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Collection, Mapping, Optional

from .durability import (
    CommitmentVerifier,
    atomic_publish_verified_zip,
    cleanup_task_created_paths,
)
from .failure_state import (
    FailurePhase,
    OperationCode,
    PhaseTracker,
    SanitizedFailure,
    sanitize_exception,
)


@dataclass(frozen=True)
class RunnerResult:
    success: bool
    failure_phase: str
    operation_code: Optional[str]
    failure: Optional[SanitizedFailure]
    cleanup_requested: int
    cleanup_removed: int
    cleanup_already_absent: int


class BlindPackagePersistenceRunner:
    """Publish one prebuilt ZIP with no internal retry."""

    def __init__(
        self,
        *,
        partial_path: Path,
        final_path: Path,
        expected_members: Collection[str],
        expected_member_hashes: Mapping[str, str],
        commitment_verifier: CommitmentVerifier,
        cleanup_paths: Collection[Path],
        cleanup_root: Path,
        tracker: Optional[PhaseTracker] = None,
        governed_final_path: Optional[Path] = None,
        repository_root: Optional[Path] = None,
    ) -> None:
        self._partial_path = Path(partial_path)
        self._final_path = Path(final_path)
        self._expected_members = tuple(expected_members)
        self._expected_member_hashes = dict(expected_member_hashes)
        self._commitment_verifier = commitment_verifier
        self._cleanup_paths = tuple(Path(path) for path in cleanup_paths)
        self._cleanup_root = Path(cleanup_root)
        self._tracker = tracker if tracker is not None else PhaseTracker()
        self._governed_final_path = governed_final_path
        self._repository_root = repository_root

    @property
    def tracker(self) -> PhaseTracker:
        return self._tracker

    def run(self) -> RunnerResult:
        try:
            self._tracker.transition(
                FailurePhase.SEALED_ZIP_WRITE,
                OperationCode.WRITE_PARTIAL_ZIP,
            )
            atomic_publish_verified_zip(
                self._partial_path,
                self._final_path,
                expected_members=self._expected_members,
                expected_member_hashes=self._expected_member_hashes,
                commitment_verifier=self._commitment_verifier,
                tracker=self._tracker,
            )
            return RunnerResult(
                success=True,
                failure_phase=self._tracker.phase.value,
                operation_code=self._tracker.operation.value,
                failure=None,
                cleanup_requested=0,
                cleanup_removed=0,
                cleanup_already_absent=0,
            )
        except Exception as exc:
            failure = sanitize_exception(exc, self._tracker)
            summary = {
                "already_absent": 0,
                "removed": 0,
                "requested": len(self._cleanup_paths),
            }
            try:
                summary = cleanup_task_created_paths(
                    self._cleanup_paths,
                    allowed_root=self._cleanup_root,
                    tracker=self._tracker,
                    governed_final_path=self._governed_final_path,
                    repository_root=self._repository_root,
                )
            except Exception as cleanup_exc:
                failure = sanitize_exception(cleanup_exc, self._tracker)
            return RunnerResult(
                success=False,
                failure_phase=failure.failure_phase,
                operation_code=failure.operation_code,
                failure=failure,
                cleanup_requested=summary["requested"],
                cleanup_removed=summary["removed"],
                cleanup_already_absent=summary["already_absent"],
            )
