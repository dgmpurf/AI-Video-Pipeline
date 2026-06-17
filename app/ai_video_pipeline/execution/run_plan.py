from __future__ import annotations

import json
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterable, List, Optional

from ..core.models import TaskSpec


@dataclass(frozen=True)
class RunPlanItem:
    task_id: str
    task_type: str
    provider: str
    phase: Optional[str]
    output_name: str
    reference_ids: list[str]
    dependency_task_ids: list[str]
    order_index: int
    status: str
    reason: str

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "provider": self.provider,
            "phase": self.phase,
            "output_name": self.output_name,
            "reference_ids": list(self.reference_ids),
            "dependency_task_ids": list(self.dependency_task_ids),
            "order_index": self.order_index,
            "status": self.status,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class RunPlan:
    items: list[RunPlanItem]

    def to_dict(self) -> dict:
        return {"items": [item.to_dict() for item in self.items]}

    def to_json(self, *, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=True)

    @property
    def ordered_task_ids(self) -> list[str]:
        return [item.task_id for item in self.items]


def _collect_dependencies(task: TaskSpec) -> list[str]:
    return list(getattr(task, "dependency_task_ids", []))


def _manifest_index_map(tasks: list[TaskSpec]) -> dict[str, int]:
    return {task.task_id: i for i, task in enumerate(tasks)}


def _dependency_key(task_id: str, manifest_index: dict[str, int]) -> tuple[int, str]:
    return manifest_index.get(task_id, len(manifest_index)), task_id


def _sort_run_plan_items(items: list[RunPlanItem], tasks: list[TaskSpec]) -> list[RunPlanItem]:
    if not items:
        return []
    manifest_index = _manifest_index_map(tasks)
    edges: dict[str, set[str]] = defaultdict(set)
    indegree: dict[str, int] = defaultdict(int)
    children: dict[str, set[str]] = defaultdict(set)

    for item in items:
        indegree.setdefault(item.task_id, 0)

    for task in tasks:
        deps = [dep for dep in _collect_dependencies(task) if dep in manifest_index]
        for dep in deps:
            edges[dep].add(task.task_id)
            indegree[task.task_id] += 1
            children[dep].add(task.task_id)

    queue: deque[str] = deque(sorted([tid for tid, degree in indegree.items() if degree == 0], key=lambda tid: _dependency_key(tid, manifest_index)))
    ordered: list[RunPlanItem] = []
    item_by_id = {item.task_id: item for item in items}

    while queue:
        tid = queue.popleft()
        ordered.append(item_by_id[tid])
        for child in sorted(children.get(tid, set()), key=lambda child: _dependency_key(child, manifest_index)):
            indegree[child] -= 1
            if indegree[child] <= 0:
                queue.append(child)
        queue = deque(sorted(list(queue), key=lambda item_id: _dependency_key(item_id, manifest_index)))

    if len(ordered) != len(items):
        completed = {item.task_id for item in ordered}
        for item in sorted((entry for entry in items if entry.task_id not in completed), key=lambda entry: _dependency_key(entry.task_id, manifest_index)):
            ordered.append(
                RunPlanItem(
                    task_id=item.task_id,
                    task_type=item.task_type,
                    provider=item.provider,
                    phase=item.phase,
                    output_name=item.output_name,
                    reference_ids=item.reference_ids,
                    dependency_task_ids=item.dependency_task_ids,
                    order_index=item.order_index,
                    status=item.status,
                    reason="dependency_cycle",
                )
            )
    return ordered


def build_run_plan(tasks: Iterable[TaskSpec]) -> RunPlan:
    source_tasks = list(tasks)
    items: list[RunPlanItem] = []
    for index, task in enumerate(source_tasks):
        items.append(
            RunPlanItem(
                task_id=task.task_id,
                task_type=str(task.task_type),
                provider=task.provider.value,
                phase=task.phase,
                output_name=task.output_name,
                reference_ids=list(task.reference_ids),
                dependency_task_ids=list(getattr(task, "dependency_task_ids", [])),
                order_index=index,
                status="planned",
                reason="manifest_order" if not getattr(task, "dependency_task_ids", []) else "dependency_order",
            )
        )
    ordered = _sort_run_plan_items(items, source_tasks)
    return RunPlan(items=ordered)
