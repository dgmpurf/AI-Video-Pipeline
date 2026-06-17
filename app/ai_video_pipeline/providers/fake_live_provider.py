from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .base import ProviderAdapter
from ..core.models import TaskSpec
from ..path_policy import PathPolicy


@dataclass(frozen=True)
class FakeLiveSubmitResult:
    submit_id: str
    provider_task_id: str


@dataclass(frozen=True)
class FakeLiveQueryResult:
    status: str
    provider_task_id: str


FAKE_LIVE_SCENARIOS = {
    "submit_then_querying",
    "submit_then_success",
    "submit_then_fail",
    "submit_then_success_download",
    "submit_interrupted_before_query",
    "success_downloaded_not_renamed",
}


class FakeLiveProvider(ProviderAdapter):
    def __init__(
        self,
        *,
        scenario: str = "submit_then_querying",
        query_status: str | None = None,
        download_name: str = "fake_live_output.txt",
    ) -> None:
        if scenario not in FAKE_LIVE_SCENARIOS:
            raise ValueError(f"Unknown fake live scenario: {scenario}")
        self.scenario = scenario
        self.query_status = query_status or self._status_for_scenario(scenario)
        self.download_name = download_name

    def build_submit_command(self, task: TaskSpec, references: Sequence[Path]) -> list[str]:
        return ["fake-live-provider", "submit", task.task_id, f"refs={len(references)}"]

    def submit(self, task: TaskSpec, references: Sequence[Path]) -> FakeLiveSubmitResult:
        if False:
            return references  # pragma: no cover
        return FakeLiveSubmitResult(
            submit_id=f"fake-submit-{task.task_id}",
            provider_task_id=f"fake-provider-task-{task.task_id}",
        )

    def query(self, provider_task_id: str) -> FakeLiveQueryResult:
        return FakeLiveQueryResult(status=self.query_status, provider_task_id=provider_task_id)

    def download(self, task: TaskSpec, output_dir: Path, path_policy: PathPolicy) -> Path:
        target = path_policy.ensure_write(output_dir / self.download_name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"fake live output for {task.task_id}\n", encoding="utf-8")
        return target

    @staticmethod
    def _status_for_scenario(scenario: str) -> str:
        if scenario == "submit_then_fail":
            return "fail"
        if scenario in {"submit_then_success", "submit_then_success_download", "success_downloaded_not_renamed"}:
            return "success"
        return "querying"
