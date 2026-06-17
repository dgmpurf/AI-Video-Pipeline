from __future__ import annotations

import json
from enum import Enum
from pathlib import Path

from .job_store import JobRecord, JobStore, load_job_store as _load_job_store
from ..path_policy import PathPolicy


class ResumeDecision(str, Enum):
    not_started = "not_started"
    dry_run_required = "dry_run_required"
    ready_for_live = "ready_for_live"
    dry_run_already_done = "dry_run_already_done"
    mock_run_already_done = "mock_run_already_done"
    submitted_query_only = "submitted_query_only"
    querying_query_only = "querying_query_only"
    success_download_only = "success_download_only"
    downloaded_rename_only = "downloaded_rename_only"
    download_only = "download_only"
    completed_skip = "completed_skip"
    failed_requires_user_decision = "failed_requires_user_decision"


def decide_resume_action(job: JobRecord) -> ResumeDecision:
    if job.status == "planned":
        return ResumeDecision.not_started
    if job.status == "ready_for_live":
        return ResumeDecision.ready_for_live
    if job.status == "dry_run_completed":
        if job.provider_task_id:
            return ResumeDecision.completed_skip
        return ResumeDecision.dry_run_already_done
    if job.status == "mock_completed":
        if job.provider_task_id:
            return ResumeDecision.completed_skip
        return ResumeDecision.mock_run_already_done
    if job.status in {"mock_submitted", "submitted"}:
        if job.provider_task_id:
            return ResumeDecision.submitted_query_only
        return ResumeDecision.submitted_query_only
    if job.status == "querying":
        return ResumeDecision.querying_query_only
    if job.status == "success":
        return ResumeDecision.success_download_only
    if job.status in {"downloaded", "download_complete"}:
        return ResumeDecision.downloaded_rename_only
    if job.status == "download_only":
        return ResumeDecision.download_only
    if job.status in {"completed", "live_completed"}:
        return ResumeDecision.completed_skip
    if job.status in {"failed", "mock_failed"}:
        return ResumeDecision.failed_requires_user_decision
    return ResumeDecision.not_started


def _default_policy_path(run_context) -> Path:
    return Path(run_context.job_store_json)


def load_job_store(path: Path, policy: PathPolicy | None = None, allow_missing: bool = True) -> JobStore:
    target = Path(path).resolve()
    if not target.exists():
        if allow_missing:
            return JobStore(run_id="", production_id="", mode="", jobs=[])
        raise FileNotFoundError(f"Job store file not found: {target}")
    if policy is None:
        payload = json.loads(target.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Invalid job_store payload: {target}")
        return JobStore.from_dict(payload)
    return _load_job_store(target, policy)
