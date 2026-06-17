from __future__ import annotations

from pathlib import Path
from typing import Iterable

from ..path_policy import PathPolicy
from .manifest import MANIFEST_FIELDS, parse_manifest_csv
from .models import TaskSpec


def write_task_manifest(tasks: Iterable[TaskSpec], output_csv_path: Path, path_policy: PathPolicy) -> Path:
    target = path_policy.ensure_write(Path(output_csv_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = [task.to_manifest_row() for task in tasks]

    import csv

    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in MANIFEST_FIELDS})
    return target


def read_task_manifest(csv_path: Path, path_policy: PathPolicy) -> list[TaskSpec]:
    source = path_policy.ensure(Path(csv_path))
    return parse_manifest_csv(source)
