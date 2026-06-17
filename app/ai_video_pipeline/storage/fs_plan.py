from __future__ import annotations

import json
from pathlib import Path

from ..core.models import FSWritePlan
from ..path_policy import PathPolicy


def materialize_fs_write_plan(plan: FSWritePlan, policy: PathPolicy) -> None:
    policy.ensure(plan.root)
    plan.root.mkdir(parents=True, exist_ok=True)


def read_fs_write_plan(path: Path) -> FSWritePlan:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return FSWritePlan(
        root=Path(payload["root"]),
        planned_files=[Path(item) for item in payload.get("planned_files", [])],
    )
