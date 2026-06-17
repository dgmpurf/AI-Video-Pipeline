from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable

from ..path_policy import PathPolicy
from ..core.models import RunMode


def _utcnow() -> str:
    return datetime.utcnow().isoformat()


@dataclass
class JobRecord:
    task_id: str
    status: str
    provider: str = ""
    provider_task_id: str = ""
    submit_id: str = ""
    output_name: str = ""
    created_at: str = field(default_factory=_utcnow)
    updated_at: str = field(default_factory=_utcnow)
    last_event: str = ""

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "status": self.status,
            "provider": self.provider,
            "provider_task_id": self.provider_task_id,
            "submit_id": self.submit_id,
            "output_name": self.output_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_event": self.last_event,
        }


@dataclass
class JobStore:
    run_id: str
    production_id: str
    mode: str
    jobs: list[JobRecord] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "production_id": self.production_id,
            "mode": self.mode,
            "jobs": [job.to_dict() for job in self.jobs],
        }

    @classmethod
    def from_dict(cls, payload: dict) -> "JobStore":
        jobs = [
            JobRecord(
                task_id=str(item.get("task_id", "")),
                status=str(item.get("status", "")),
                provider=str(item.get("provider", "")),
                provider_task_id=str(item.get("provider_task_id", "")),
                submit_id=str(item.get("submit_id", "")),
                output_name=str(item.get("output_name", "")),
                created_at=str(item.get("created_at", _utcnow())),
                updated_at=str(item.get("updated_at", _utcnow())),
                last_event=str(item.get("last_event", "")),
            )
            for item in payload.get("jobs", [])
            if isinstance(item, dict)
        ]
        return cls(
            run_id=str(payload.get("run_id", "")),
            production_id=str(payload.get("production_id", "")),
            mode=str(payload.get("mode", "")),
            jobs=jobs,
        )

    def __getitem__(self, task_id: str) -> JobRecord | None:
        return get_job(self, task_id)

    def copy(self) -> "JobStore":
        return JobStore(
            run_id=self.run_id,
            production_id=self.production_id,
            mode=self.mode,
            jobs=[JobRecord(**job.to_dict()) for job in self.jobs],
        )

    def with_updated_job(self, task_id: str, **changes) -> "JobStore":
        updated = self.copy()
        now = _utcnow()
        for index, job in enumerate(updated.jobs):
            if job.task_id != task_id:
                continue
            for key, value in changes.items():
                if hasattr(job, key):
                    setattr(updated.jobs[index], key, value)
            updated.jobs[index].updated_at = now
            return updated
        return updated

    def plan_jobs(self, tasks: Iterable[object], provider_name: str = "dreamina_cli") -> "JobStore":
        items = list(tasks)
        jobs = [
            JobRecord(
                task_id=getattr(task, "task_id"),
                status="planned",
                provider=provider_name,
                output_name=getattr(task, "output_name", ""),
            )
            for task in items
        ]
        return JobStore(run_id=self.run_id, production_id=self.production_id, mode=self.mode, jobs=jobs)


def create_job_store(run_id: str, production_id: str, mode: str) -> JobStore:
    return JobStore(run_id=str(run_id), production_id=str(production_id), mode=mode)


def add_or_update_job(store: JobStore, task_id: str, **changes) -> JobStore:
    now = _utcnow()
    for job in store.jobs:
        if job.task_id != task_id:
            continue
        for key, value in changes.items():
            if hasattr(job, key):
                setattr(job, key, str(value))
        job.updated_at = now
        return store

    job_kwargs = {
        "task_id": task_id,
        "status": str(changes.get("status", "planned")),
        "provider": str(changes.get("provider", "")),
        "provider_task_id": str(changes.get("provider_task_id", "")),
        "submit_id": str(changes.get("submit_id", "")),
        "output_name": str(changes.get("output_name", "")),
        "last_event": str(changes.get("last_event", "")),
    }
    store.jobs.append(JobRecord(**job_kwargs))
    return store


def get_job(store: JobStore, task_id: str) -> JobRecord | None:
    for job in store.jobs:
        if job.task_id == task_id:
            return job
    return None


def list_jobs(store: JobStore) -> list[JobRecord]:
    return list(store.jobs)


def load_job_store(path: Path, policy: PathPolicy) -> JobStore:
    if not path.exists():
        return JobStore(run_id="", production_id="", mode=RunMode.dry_run.value, jobs=[])
    target = policy.ensure(path)
    payload = json.loads(target.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Invalid job_store payload: {path}")
    return JobStore.from_dict(payload)


def save_job_store(path: Path, store: JobStore, policy: PathPolicy) -> Path:
    target = policy.ensure(path)
    target.write_text(json.dumps(store.to_dict(), ensure_ascii=True, indent=2), encoding="utf-8")
    return target


def write_job_store(path: Path, store: JobStore, policy: PathPolicy) -> Path:
    return save_job_store(path, store, policy)
