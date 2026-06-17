from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

from ..path_policy import PathPolicy
from ..core.models import RunMode

TIMESTAMP_PREFIX_RE = re.compile(r"^(?:\d{8}_\d{6}_)+")


def strip_existing_timestamp_prefix(name: str) -> str:
    stripped = TIMESTAMP_PREFIX_RE.sub("", str(name).strip())
    return stripped or "run"


def make_safe_run_label(task_id_or_name: str) -> str:
    value = strip_existing_timestamp_prefix(task_id_or_name)
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", value.strip() or "run")
    return safe[:64] if safe else "run"


def make_run_id(timestamp: str, label: str) -> str:
    return f"{timestamp}_{make_safe_run_label(label)}"


def _run_timestamp() -> str:
    return datetime.utcnow().strftime("%Y%m%d_%H%M%S")


@dataclass(frozen=True)
class RunContext:
    workspace_root: Path
    production_id: str
    run_mode: RunMode
    run_dir_name: str
    run_root: Path
    policy: PathPolicy

    @property
    def run_manifest_snapshot_csv(self) -> Path:
        return self.run_root / "run_manifest_snapshot.csv"

    @property
    def run_plan_json(self) -> Path:
        return self.run_root / "run_plan.json"

    @property
    def provider_requests_jsonl(self) -> Path:
        return self.run_root / "provider_requests.jsonl"

    @property
    def provider_responses_jsonl(self) -> Path:
        return self.run_root / "provider_responses.jsonl"

    @property
    def submitted_tasks_csv(self) -> Path:
        return self.run_root / "submitted_tasks.csv"

    @property
    def querying_tasks_csv(self) -> Path:
        return self.run_root / "querying_tasks.csv"

    @property
    def completed_tasks_csv(self) -> Path:
        return self.run_root / "completed_tasks.csv"

    @property
    def failed_tasks_csv(self) -> Path:
        return self.run_root / "failed_tasks.csv"

    @property
    def downloaded_files_csv(self) -> Path:
        return self.run_root / "downloaded_files.csv"

    @property
    def execution_log_txt(self) -> Path:
        return self.run_root / "execution_log.txt"

    @property
    def job_store_json(self) -> Path:
        return self.run_root / "job_store.json"

    @property
    def command_preview_csv(self) -> Path:
        return self.run_root / "command_preview.csv"

    @property
    def input_media_dir(self) -> Path:
        return self.run_root / "input_media"

    @property
    def downloads_dir(self) -> Path:
        return self.run_root / "downloads"

    @property
    def output_dir(self) -> Path:
        return self.run_root / "output"

    @property
    def mock_outputs_dir(self) -> Path:
        return self.run_root / "mock_outputs"

    @property
    def reports_dir(self) -> Path:
        return self.run_root / "reports"

    @property
    def raw_responses_dir(self) -> Path:
        return self.run_root / "raw_responses"

    @property
    def compatibility_submitted_csv(self) -> Path:
        return self.run_root / "submitted.csv"

    @property
    def compatibility_completed_csv(self) -> Path:
        return self.run_root / "completed.csv"

    @property
    def compatibility_downloaded_csv(self) -> Path:
        return self.run_root / "downloaded.csv"


def create_run_dir(
    workspace_root: Path,
    production_id: str,
    run_mode: RunMode,
    task_or_batch_name: str,
    run_id: Optional[str] = None,
    policy: Optional[PathPolicy] = None,
) -> RunContext:
    root = Path(workspace_root).resolve()
    path_policy = policy or PathPolicy(root)
    mode_name = run_mode.value if isinstance(run_mode, RunMode) else str(run_mode)
    label = run_id if run_id else task_or_batch_name
    run_dir_name = make_run_id(_run_timestamp(), label)
    run_root = path_policy.ensure(root / "productions" / production_id / "runs" / mode_name / run_dir_name)
    path_policy.mkdir(run_root, exist_ok=True)

    required_files = [
        "run_manifest_snapshot.csv",
        "run_plan.json",
        "provider_requests.jsonl",
        "provider_responses.jsonl",
        "submitted_tasks.csv",
        "querying_tasks.csv",
        "completed_tasks.csv",
        "failed_tasks.csv",
        "downloaded_files.csv",
        "execution_log.txt",
        "job_store.json",
        "command_preview.csv",
        "submitted.csv",
        "completed.csv",
        "downloaded.csv",
    ]
    for name in required_files:
        path = run_root / name
        if path.suffix == ".json":
            path_policy.write_text(path, "{}", encoding="utf-8")
        else:
            path_policy.write_text(path, "", encoding="utf-8")

    for directory in [run_root / "input_media", run_root / "downloads", run_root / "output", run_root / "mock_outputs", run_root / "reports", run_root / "raw_responses"]:
        path_policy.mkdir(directory, exist_ok=True)

    return RunContext(
        workspace_root=root,
        production_id=production_id,
        run_mode=run_mode if isinstance(run_mode, RunMode) else RunMode(run_mode),
        run_dir_name=run_dir_name,
        run_root=run_root,
        policy=path_policy,
    )
