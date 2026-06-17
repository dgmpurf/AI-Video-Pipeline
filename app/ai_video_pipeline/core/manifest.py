from __future__ import annotations

import csv
from pathlib import Path
from typing import List

from .models import ProviderName, ReviewStatus, TaskSpec
from .validation import ensure_non_empty, parse_int_maybe, parse_provider_name, parse_reference_ids, parse_task_type


MANIFEST_FIELDS = [
    "task_id",
    "phase",
    "task_type",
    "provider",
    "model_version",
    "ratio",
    "resolution_type",
    "duration",
    "video_resolution",
    "prompt",
    "reference_ids",
    "output_name",
    "status",
    "review_status",
    "notes",
]


def parse_manifest_row(row_num: int, row: dict) -> TaskSpec:
    task_id = ensure_non_empty(row.get("task_id"), "task_id")
    task_type = parse_task_type(ensure_non_empty(row.get("task_type"), "task_type"))
    provider = parse_provider_name(ensure_non_empty(row.get("provider"), "provider"))
    prompt = ensure_non_empty(row.get("prompt"), "prompt")
    output_name = ensure_non_empty(row.get("output_name"), "output_name")

    review_raw = row.get("review_status")
    review_status = None
    if review_raw is not None and str(review_raw).strip():
        try:
            review_status = ReviewStatus(str(review_raw).strip())
        except Exception as exc:
            valid = ", ".join([item.value for item in ReviewStatus])
            raise ValueError(f"Invalid review_status '{review_raw}'. Valid values: {valid}") from exc

    return TaskSpec(
        task_id=task_id,
        task_type=task_type,
        provider=provider,
        prompt=prompt,
        output_name=output_name,
        dependency_task_ids=parse_reference_ids(str(row.get("dependency_task_ids") or "")),
        phase=(row.get("phase") or "").strip() or None,
        model_version=(row.get("model_version") or "").strip() or None,
        ratio=(row.get("ratio") or "").strip() or None,
        resolution_type=(row.get("resolution_type") or "").strip() or None,
        duration=parse_int_maybe(row.get("duration") or ""),
        video_resolution=(row.get("video_resolution") or "").strip() or None,
        reference_ids=parse_reference_ids(row.get("reference_ids") or ""),
        status=(row.get("status") or "").strip() or None,
        review_status=review_status,
        notes=(row.get("notes") or "").strip() or None,
    )


def parse_manifest_csv(manifest_path: Path) -> List[TaskSpec]:
    path = Path(manifest_path)
    rows: List[TaskSpec] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in MANIFEST_FIELDS if field not in reader.fieldnames]
        if missing:
            raise ValueError(f"Manifest missing fields: {', '.join(missing)}")
        for index, row in enumerate(reader, start=2):
            task = parse_manifest_row(index, row)
            _validate_manifest_provider_scope(path, task)
            rows.append(task)
    return rows


def _validate_manifest_provider_scope(path: Path, task: TaskSpec) -> None:
    if task.provider != ProviderName.fake_live_provider:
        return
    parts = {part.lower() for part in path.parts}
    if "tests" in parts and "fixtures" in parts:
        return
    if "productions" in parts and "manifests" in parts:
        raise ValueError("fake_live_provider is not allowed in production manifests")
    raise ValueError("fake_live_provider is allowed only in tests/fixtures manifests")
