from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from .runner import RunArtifacts


def load_completed_task_ids(artifacts: RunArtifacts) -> List[str]:
    if not artifacts.completed_csv.exists():
        return []
    lines = [line.strip() for line in artifacts.completed_csv.read_text(encoding="utf-8").splitlines()]
    if not lines:
        return []
    header = lines[0].split(",")
    rows = [dict(zip(header, row.split(","))) for row in lines[1:] if row.strip()]
    return [row.get("task_id", "") for row in rows if row.get("task_id")]


def pending_tasks(all_task_ids: List[str], completed_task_ids: List[str]) -> List[str]:
    return [item for item in all_task_ids if item not in set(completed_task_ids)]
