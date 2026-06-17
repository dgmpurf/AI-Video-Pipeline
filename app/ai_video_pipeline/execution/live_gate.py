from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping

from ..core.models import RunMode, TaskSpec
from ..path_policy import PathPolicy, PathPolicyError


@dataclass(frozen=True)
class LiveRunRequest:
    production_id: str
    task_id: str
    run_mode: str | RunMode
    provider: str
    manifest_path: Path | None
    reference_registry_path: Path | None
    fs_write_plan_path: Path | None
    user_confirmed: bool
    allow_single_task_only: bool
    dry_run_id: str
    notes: str = ""


@dataclass(frozen=True)
class LiveRunGateDecision:
    allowed: bool
    reason: str
    required_actions: list[str] = field(default_factory=list)


class LiveRunGate:
    def __init__(self, path_policy: PathPolicy) -> None:
        self.path_policy = path_policy

    def validate(
        self,
        request: LiveRunRequest,
        tasks: Iterable[TaskSpec],
        provider_config: Mapping[str, Any],
        *,
        staged_media_paths: Iterable[Path] | None = None,
    ) -> LiveRunGateDecision:
        return validate_live_run_request(
            request,
            tasks,
            provider_config,
            self.path_policy,
            staged_media_paths=staged_media_paths,
        )


def validate_live_run_request(
    request: LiveRunRequest,
    tasks: Iterable[TaskSpec],
    provider_config: Mapping[str, Any],
    path_policy: PathPolicy,
    *,
    staged_media_paths: Iterable[Path] | None = None,
) -> LiveRunGateDecision:
    required_actions: list[str] = []
    selected_tasks = list(tasks)
    provider_entry = _provider_entry(provider_config, request.provider)

    if str(request.run_mode) not in {RunMode.live.value, "RunMode.live"}:
        required_actions.append("request run_mode=live")
    provider_mode = str(provider_entry.get("mode", ""))
    if not bool(provider_entry.get("allow_live_run", False)):
        if request.provider == "dreamina_cli":
            required_actions.append("dreamina_cli live-run disabled by provider config")
        else:
            required_actions.append("enable provider allow_live_run")
    if request.provider == "fake_live_provider":
        if provider_mode != "fake_live":
            required_actions.append("use fake live provider")
        if not bool(provider_entry.get("test_context", False)):
            required_actions.append("enable explicit fake provider test context")
    elif request.provider == "dreamina_cli":
        if provider_mode != "cli":
            required_actions.append("use dreamina_cli cli mode")
    else:
        required_actions.append("unsupported live-run provider")
    if not request.user_confirmed:
        required_actions.append("collect explicit user confirmation")
    if not request.allow_single_task_only:
        required_actions.append("confirm single-task live-run mode")
    if len(selected_tasks) != 1:
        required_actions.append("provide exactly one task")
    if not request.dry_run_id:
        required_actions.append("complete dry-run first")
    if not request.fs_write_plan_path:
        required_actions.append("provide fs_write_plan")

    _check_optional_path(request.manifest_path, path_policy, required_actions, "manifest path")
    _check_optional_path(request.reference_registry_path, path_policy, required_actions, "reference registry path")
    fs_plan = _load_fs_write_plan(request.fs_write_plan_path, path_policy, required_actions)
    if fs_plan is not None:
        if not bool(fs_plan.get("approved", False)):
            required_actions.append("approve fs_write_plan")
        for entry in fs_plan.get("planned_files", []):
            try:
                path_policy.ensure(Path(entry))
            except PathPolicyError:
                required_actions.append("keep planned output paths inside workspace")
                break

    if selected_tasks:
        task = selected_tasks[0]
        if request.task_id and task.task_id != request.task_id:
            required_actions.append("request task_id must match selected task")
        if task.reference_ids and not list(staged_media_paths or []):
            required_actions.append("stage media before live-run")

    for staged_path in staged_media_paths or []:
        try:
            path_policy.ensure(Path(staged_path))
        except PathPolicyError:
            required_actions.append("keep staged media inside workspace")
            break
        if not Path(staged_path).exists():
            required_actions.append("staged media file must exist")
            break

    if required_actions:
        return LiveRunGateDecision(False, "live-run denied by safety gate", required_actions)
    return LiveRunGateDecision(True, "live-run allowed by safety gate", [])


def _provider_entry(provider_config: Mapping[str, Any], provider: str) -> Mapping[str, Any]:
    if "providers" in provider_config:
        providers = provider_config.get("providers", {})
        if isinstance(providers, Mapping):
            entry = providers.get(provider, {})
            return entry if isinstance(entry, Mapping) else {}
    return provider_config


def _check_optional_path(path: Path | None, policy: PathPolicy, actions: list[str], label: str) -> None:
    if path is None:
        return
    try:
        policy.ensure(Path(path))
    except PathPolicyError:
        actions.append(f"keep {label} inside workspace")


def _load_fs_write_plan(path: Path | None, policy: PathPolicy, actions: list[str]) -> dict[str, Any] | None:
    if path is None:
        return None
    try:
        target = policy.ensure(Path(path))
    except PathPolicyError:
        actions.append("keep fs_write_plan inside workspace")
        return None
    if not target.exists():
        actions.append("create fs_write_plan")
        return None
    try:
        payload = json.loads(target.read_text(encoding="utf-8"))
    except Exception:
        actions.append("write valid fs_write_plan json")
        return None
    if not isinstance(payload, dict):
        actions.append("write fs_write_plan as object")
        return None
    return payload
