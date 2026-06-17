from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from enum import Enum
import uuid
from pathlib import Path
from typing import Iterable

from ..assets.registry import AssetRegistry
from ..core.models import AssetStatus, AssetRecord, ReviewStatus
from ..path_policy import PathPolicy


def _now() -> datetime:
    return datetime.now(timezone.utc)


class ReviewDecision(str, Enum):
    approve = "approve"
    reject = "reject"
    needs_rerun = "needs_rerun"
    hold = "hold"


@dataclass
class ReviewDecisionRecord:
    review_id: str
    logical_id: str
    candidate_id: str
    decision: ReviewDecision
    reviewer: str
    score: float | None = None
    issue_tags: list[str] = field(default_factory=list)
    note: str = ""
    created_at: datetime = field(default_factory=_now)
    source_path: str = ""
    target_status_after_decision: str = AssetStatus.candidate.value
    rerun_reason: str = ""

    def to_json_line(self) -> str:
        payload = {
            "review_id": self.review_id,
            "logical_id": self.logical_id,
            "candidate_id": self.candidate_id,
            "decision": self.decision,
            "reviewer": self.reviewer,
            "score": self.score,
            "issue_tags": self.issue_tags,
            "note": self.note,
            "created_at": self.created_at.isoformat(),
            "source_path": self.source_path,
            "target_status_after_decision": self.target_status_after_decision,
            "rerun_reason": self.rerun_reason,
        }
        return json.dumps(payload, ensure_ascii=True)


class ReviewLocker:
    """Review decision helper used by Phase C."""

    def __init__(self, registry: AssetRegistry, production_dir: Path, path_policy: PathPolicy) -> None:
        self.registry = registry
        self.path_policy = path_policy
        self.production_dir = path_policy.ensure(production_dir)
        self.record_path = self.production_dir / "reviews" / "review_records.jsonl"
        self.record_path = self.path_policy.ensure(self.record_path)

    def create_review_record(self, record: ReviewDecisionRecord) -> Path:
        self.record_path.parent.mkdir(parents=True, exist_ok=True)
        with self.record_path.open("a", encoding="utf-8") as handle:
            handle.write(record.to_json_line() + "\n")
        return self.record_path

    def lock_asset(
        self,
        logical_id: str,
        candidate_id: str,
        reviewer: str,
        score: float | None = None,
        issue_tags: Iterable[str] | None = None,
        note: str = "",
        source_path: str = "",
    ) -> ReviewDecisionRecord:
        # System reviewer cannot directly lock finalized production assets.
        if reviewer == "system":
            raise ValueError("Reviewer 'system' cannot auto-lock assets in production")

        return self._transition_to_status(
            decision=ReviewDecision.approve,
            logical_id=logical_id,
            candidate_id=candidate_id,
            reviewer=reviewer,
            score=score,
            issue_tags=list(issue_tags or []),
            note=note,
            source_path=source_path,
            target_status=AssetStatus.locked_after_human_review,
        )

    def approve_candidate(self, logical_id: str, candidate_id: str, reviewer: str = "user", **kwargs: object) -> ReviewDecisionRecord:
        return self.lock_asset(logical_id=logical_id, candidate_id=candidate_id, reviewer=reviewer, **kwargs)

    def reject_asset(
        self,
        logical_id: str,
        candidate_id: str,
        reason: str,
        reviewer: str = "user",
        score: float | None = None,
        issue_tags: Iterable[str] | None = None,
        source_path: str = "",
    ) -> ReviewDecisionRecord:
        if not reason:
            raise ValueError("reject must include reason")
        return self._transition_to_status(
            decision=ReviewDecision.reject,
            logical_id=logical_id,
            candidate_id=candidate_id,
            reviewer=reviewer,
            score=score,
            issue_tags=list(issue_tags or []),
            note=reason,
            source_path=source_path,
            target_status=AssetStatus.rejected,
            review_status=ReviewStatus.rejected,
        )

    def request_rerun(
        self,
        logical_id: str,
        candidate_id: str,
        rerun_reason: str,
        reviewer: str = "user",
        score: float | None = None,
        issue_tags: Iterable[str] | None = None,
        source_path: str = "",
    ) -> ReviewDecisionRecord:
        if not rerun_reason:
            raise ValueError("needs_rerun must include rerun_reason")
        return self._transition_to_status(
            decision=ReviewDecision.needs_rerun,
            logical_id=logical_id,
            candidate_id=candidate_id,
            reviewer=reviewer,
            score=score,
            issue_tags=list(issue_tags or []),
            note=rerun_reason,
            source_path=source_path,
            target_status=AssetStatus.candidate,
            review_status=ReviewStatus.needs_rerun,
            rerun_reason=rerun_reason,
        )

    def hold_for_review(
        self,
        logical_id: str,
        candidate_id: str,
        reviewer: str = "user",
        score: float | None = None,
        issue_tags: Iterable[str] | None = None,
        note: str = "",
        source_path: str = "",
    ) -> ReviewDecisionRecord:
        return self._transition_to_status(
            decision=ReviewDecision.hold,
            logical_id=logical_id,
            candidate_id=candidate_id,
            reviewer=reviewer,
            score=score,
            issue_tags=list(issue_tags or []),
            note=note,
            source_path=source_path,
            target_status=AssetStatus.candidate,
            review_status=ReviewStatus.pending_review,
        )

    def lock_ref(self, ref_name: str, status: ReviewStatus = ReviewStatus.approved) -> Path:  # Backward-compatible alias
        record = ReviewDecisionRecord(
            review_id=f"ref_{uuid.uuid4().hex}",
            logical_id=ref_name,
            candidate_id=f"ref-{ref_name}",
            decision=ReviewDecision.approve,
            reviewer="system",
            note="",
            created_at=_now(),
            target_status_after_decision=AssetStatus.locked_after_human_review.value,
        )
        self.create_review_record(record)
        path = self.production_dir / "reviews" / f"{ref_name}.json"
        if not path.name.endswith(".json"):
            raise RuntimeError("ref name is invalid")
        path.write_text(
            json.dumps(
                {"ref_name": ref_name, "status": status.value},
                ensure_ascii=True,
            ),
            encoding="utf-8",
        )
        return path

    def _transition_to_status(
        self,
        decision: ReviewDecision,
        logical_id: str,
        candidate_id: str,
        reviewer: str,
        score: float | None,
        issue_tags: list[str],
        note: str,
        source_path: str,
        target_status: AssetStatus,
        review_status: ReviewStatus | None = None,
        rerun_reason: str = "",
    ) -> ReviewDecisionRecord:
        matched = self.registry.get_by_logical_id(logical_id, candidate_id)
        if not matched:
            raise KeyError(f"asset not found: {logical_id}/{candidate_id}")

        asset = matched[0]
        if decision == ReviewDecision.approve:
            source_path_path = Path(source_path) if source_path else asset.source_path
            if source_path_path is not None and "mock" in str(source_path_path).lower():
                raise ValueError("mock output cannot be locked")

        if target_status == AssetStatus.locked_after_human_review:
            assert reviewer != "system", "reviewer=system cannot lock"

        target_review_status = review_status or ReviewStatus.pending_review
        self.registry.update_asset(
            logical_id=logical_id,
            candidate_id=candidate_id,
            status=target_status.value,
            review_status=target_review_status.value,
            review_note=note,
        )

        record = ReviewDecisionRecord(
            review_id=f"review_{uuid.uuid4().hex}",
            logical_id=logical_id,
            candidate_id=candidate_id,
            decision=decision,
            reviewer=reviewer,
            score=score,
            issue_tags=issue_tags,
            note=note,
            created_at=_now(),
            source_path=str(source_path or asset.source_path or ""),
            target_status_after_decision=target_status.value,
            rerun_reason=rerun_reason,
        )
        self.create_review_record(record)
        return record
