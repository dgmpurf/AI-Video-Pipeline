from __future__ import annotations

import json
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional

from ..core.manifest import MANIFEST_FIELDS, parse_manifest_csv
from ..core.manifest_discovery import discover_manifests
from ..core.models import ProviderName, ProviderRequest, RunMode, TaskSpec
from ..path_policy import PathPolicy
from ..providers.base import ProviderConfig, ProviderAdapter
from ..providers.dreamina_cli import DreaminaCLIProvider
from ..providers.fake_live_provider import FakeLiveProvider
from ..providers.stubs import StubProvider
from .live_gate import LiveRunGate, LiveRunRequest
from .job_store import (
    JobRecord,
    add_or_update_job,
    create_job_store,
    get_job,
    JobStore,
    save_job_store,
)
from .recorder import write_csv, write_json, write_jsonl
from .run_context import RunContext, create_run_dir
from .run_plan import RunPlan, build_run_plan


def _load_json(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _default_output_extension(task_type: str, defaults: dict) -> str:
    ext_map = defaults.get("default_output_extension_by_task", {})
    if isinstance(ext_map, dict):
        return str(ext_map.get(task_type, ".bin"))
    return ".bin"


@dataclass
class RunArtifacts:
    run_id: str
    run_root: Path
    run_manifest_snapshot_csv: Path
    run_plan_json: Path
    provider_requests_jsonl: Path
    provider_responses_jsonl: Path
    command_preview_csv: Path
    submitted_csv: Path
    completed_csv: Path
    downloaded_csv: Path
    submitted_tasks_csv: Path
    completed_tasks_csv: Path
    downloaded_files_csv: Path
    querying_tasks_csv: Path
    failed_tasks_csv: Path
    execution_log_txt: Path
    job_store_json: Path


class PipelineRunner:
    def __init__(
        self,
        workspace_root: Path,
        *,
        providers_config_path: Optional[Path] = None,
        runtime_defaults_path: Optional[Path] = None,
        reference_registry: Optional[Dict[str, str]] = None,
    ) -> None:
        self.workspace_root = Path(workspace_root).resolve()
        self.path_policy = PathPolicy(self.workspace_root)

        default_provider_path = self.workspace_root / "configs" / "providers.json"
        default_runtime_path = self.workspace_root / "configs" / "runtime_defaults.json"
        self.providers_config_path = Path(providers_config_path) if providers_config_path else default_provider_path
        self.runtime_defaults_path = Path(runtime_defaults_path) if runtime_defaults_path else default_runtime_path

        self.providers_config = _load_json(self.providers_config_path)
        self.runtime_defaults = _load_json(self.runtime_defaults_path)
        self.reference_registry = reference_registry or {}
        self.provider_map = self._build_provider_map()
        self.default_provider = self.providers_config.get("default_provider", "dreamina_cli")

    def _build_provider_map(self) -> dict[str, ProviderAdapter]:
        raw_providers = self.providers_config.get("providers", {})
        result: dict[str, ProviderAdapter] = {}
        for name, entry in raw_providers.items():
            cfg = ProviderConfig.from_mapping(name, entry)
            if cfg.mode == "fake_live" and bool(entry.get("test_context", False)):
                result[name] = FakeLiveProvider(
                    scenario=str(entry.get("fake_scenario", "submit_then_querying")),
                    query_status=entry.get("fake_query_status"),
                )
            elif cfg.name == ProviderName.dreamina_cli.value and cfg.mode == "cli":
                result[name] = DreaminaCLIProvider(cfg.executable or "dreamina")
            else:
                result[name] = StubProvider()
        return result

    def _get_provider(self, provider: ProviderName) -> ProviderAdapter:
        provider_entry = self.providers_config.get("providers", {}).get(provider.value)
        if provider_entry is None:
            raise ValueError(f"Unknown provider: {provider.value}")
        if not provider_entry.get("enabled", False):
            raise ValueError(f"Provider is disabled: {provider.value}")
        return self.provider_map[provider.value]

    def _resolve_references(self, task: TaskSpec) -> list[Path]:
        staging_root = self.workspace_root / str(self.runtime_defaults.get("staging_dir", "staging"))
        resolved = []
        for ref in task.reference_ids:
            mapped_ref = self.reference_registry.get(ref, ref)
            candidate = Path(mapped_ref)
            if not candidate.is_absolute():
                candidate = self.workspace_root / candidate
            candidate = self.path_policy.ensure(candidate)
            if not candidate.exists():
                raise FileNotFoundError(f"Reference missing: {candidate}")
            resolved.append(candidate)
        # keep behavior stable while remaining safe for mock path usage
        return resolved

    def _build_provider_requests(self, tasks: list[TaskSpec]) -> list[ProviderRequest]:
        requests: list[ProviderRequest] = []
        for task in tasks:
            refs = []
            for ref in task.reference_ids:
                mapped_ref = self.reference_registry.get(ref, ref)
                candidate = Path(mapped_ref)
                if not candidate.is_absolute():
                    candidate = self.workspace_root / candidate
                refs.append(self._stage_reference(candidate))
            provider = self._get_provider(task.provider)
            cmd = provider.build_submit_command(task, refs)
            if not isinstance(cmd, list):
                raise TypeError("submit command must be an argv list")
            if any(not isinstance(token, str) for token in cmd):
                raise TypeError("submit command items must all be strings")
            requests.append(
                ProviderRequest(
                    task_id=task.task_id,
                    provider=task.provider,
                    task_type=task.task_type,
                    command_argv=cmd,
                    output_name=task.output_name,
                )
            )
        return requests

    def _stage_reference(self, candidate: Path) -> Path:
        from ..assets.staging import stage_media_file

        staging_root = self.workspace_root / str(self.runtime_defaults.get("staging_dir", "staging"))
        return stage_media_file(candidate, staging_root, self.path_policy)[0]

    def _load_tasks(self, production_id: Optional[str], manifest_paths: Optional[Iterable[Path]]) -> list[TaskSpec]:
        if manifest_paths is not None:
            return [task for manifest in manifest_paths for task in parse_manifest_csv(self.path_policy.ensure(Path(manifest)))]
        if not production_id:
            return []
        production_root = self.workspace_root / "productions" / production_id
        manifest_files = discover_manifests(production_root, self.path_policy)
        return [task for manifest in manifest_files for task in parse_manifest_csv(manifest)]

    def _build_run_context(self, production_id: Optional[str], run_mode: RunMode, run_id: Optional[str], task_or_batch_name: str) -> RunContext:
        if not production_id:
            raise ValueError("production_id is required for run execution")
        return create_run_dir(
            self.workspace_root,
            production_id,
            run_mode,
            task_or_batch_name,
            run_id=run_id,
            policy=self.path_policy,
        )

    def _make_artifacts(self, run_root: Path) -> RunArtifacts:
        return RunArtifacts(
            run_id=run_root.name,
            run_root=run_root,
            run_manifest_snapshot_csv=run_root / "run_manifest_snapshot.csv",
            run_plan_json=run_root / "run_plan.json",
            provider_requests_jsonl=run_root / "provider_requests.jsonl",
            provider_responses_jsonl=run_root / "provider_responses.jsonl",
            command_preview_csv=run_root / "command_preview.csv",
            submitted_csv=run_root / str(self.runtime_defaults.get("submitted_file", "submitted.csv")),
            completed_csv=run_root / str(self.runtime_defaults.get("completed_file", "completed.csv")),
            downloaded_csv=run_root / str(self.runtime_defaults.get("downloaded_file", "downloaded.csv")),
            submitted_tasks_csv=run_root / str(self.runtime_defaults.get("submitted_tasks_file", "submitted_tasks.csv")),
            completed_tasks_csv=run_root / str(self.runtime_defaults.get("completed_tasks_file", "completed_tasks.csv")),
            downloaded_files_csv=run_root / str(self.runtime_defaults.get("downloaded_files_file", "downloaded_files.csv")),
            querying_tasks_csv=run_root / "querying_tasks.csv",
            failed_tasks_csv=run_root / "failed_tasks.csv",
            execution_log_txt=run_root / str(self.runtime_defaults.get("execution_log_file", "execution_log.txt")),
            job_store_json=run_root / "job_store.json",
        )

    def _write_manifest_snapshot(self, manifest_path: Path, tasks: list[TaskSpec], policy: PathPolicy) -> Path:
        rows = [task.to_manifest_row() for task in tasks]
        return write_csv(manifest_path, rows, MANIFEST_FIELDS, policy)

    def _write_run_plan(self, run_plan_path: Path, plan: RunPlan, policy: PathPolicy) -> Path:
        return write_json(run_plan_path, plan.to_dict(), policy)

    def _build_job_store(self, run_context: RunContext, plan: RunPlan, mode: str) -> JobStore:
        job_store = create_job_store(run_context.run_dir_name, run_context.production_id, mode)
        for item in plan.items:
            add_or_update_job(
                job_store,
                task_id=item.task_id,
                status="planned",
                provider=item.provider,
                output_name=item.output_name,
                last_event="plan_created",
            )
        return job_store

    def _write_command_preview(self, path: Path, provider_requests: list[ProviderRequest], policy: PathPolicy) -> Path:
        write_csv(
            path,
            [
                {
                    "task_id": request.task_id,
                    "provider": request.provider.value,
                    "task_type": request.task_type.value,
                    "command": " ".join(request.command_argv),
                }
                for request in provider_requests
            ],
            headers=("task_id", "provider", "task_type", "command"),
            policy=policy,
        )
        return path

    def _write_job_state_rows(self, artifacts: RunArtifacts, jobs: list[JobRecord], rows: Iterable[Mapping[str, object]]) -> None:
        submitted_rows: list[Mapping[str, object]] = []
        completed_rows: list[Mapping[str, object]] = []
        downloaded_rows: list[Mapping[str, object]] = []
        failed_rows: list[Mapping[str, object]] = []
        querying_rows: list[Mapping[str, object]] = []

        for row in rows:
            task_id = str(row.get("task_id", ""))
            status = str(row.get("status", ""))
            provider = str(row.get("provider", ""))
            output_path = str(row.get("output_path", "")) or str(row.get("download_path", ""))
            submitted_rows.append({"task_id": task_id, "provider": provider, "status": status})
            if status in {"completed", "mock_completed", "dry_run_completed"}:
                completed_rows.append({"task_id": task_id, "provider": provider, "status": status, "output_path": output_path})
            if status in {"downloaded", "download_complete"}:
                downloaded_rows.append({"task_id": task_id, "provider": provider, "status": status, "download_path": output_path})
            if status == "failed":
                failed_rows.append({"task_id": task_id, "provider": provider, "status": status, "error": str(row.get("error", ""))})
            if status == "querying":
                querying_rows.append({"task_id": task_id, "provider": provider, "status": status})

        write_csv(artifacts.submitted_tasks_csv, submitted_rows, ["task_id", "provider", "status"], self.path_policy)
        write_csv(artifacts.completed_tasks_csv, completed_rows, ["task_id", "provider", "status", "output_path"], self.path_policy)
        write_csv(artifacts.downloaded_files_csv, downloaded_rows, ["task_id", "provider", "status", "download_path"], self.path_policy)
        write_csv(artifacts.querying_tasks_csv, querying_rows, ["task_id", "provider", "status"], self.path_policy)
        write_csv(artifacts.failed_tasks_csv, failed_rows, ["task_id", "provider", "status", "error"], self.path_policy)
        # compatibility outputs
        write_csv(artifacts.submitted_csv, submitted_rows, ["task_id", "provider", "status"], self.path_policy)
        write_csv(artifacts.completed_csv, completed_rows, ["task_id", "provider", "status", "output_path"], self.path_policy)
        write_csv(artifacts.downloaded_csv, downloaded_rows, ["task_id", "provider", "status", "download_path"], self.path_policy)

    def dry_run(
        self,
        tasks: Optional[list[TaskSpec]] = None,
        run_id: Optional[str] = None,
        *,
        production_id: Optional[str] = None,
        manifest_paths: Optional[Iterable[Path]] = None,
        task_or_batch_name: str = "run",
    ) -> RunArtifacts:
        selected_tasks = tasks or self._load_tasks(production_id, manifest_paths)
        if not selected_tasks:
            raise RuntimeError("No tasks available for dry run")
        run_context = self._build_run_context(production_id=production_id, run_mode=RunMode.dry_run, run_id=run_id, task_or_batch_name=task_or_batch_name)
        artifacts = self._make_artifacts(run_context.run_root)
        run_plan = build_run_plan(selected_tasks)
        self._write_manifest_snapshot(artifacts.run_manifest_snapshot_csv, selected_tasks, self.path_policy)
        self._write_run_plan(artifacts.run_plan_json, run_plan, self.path_policy)
        provider_requests = self._build_provider_requests(selected_tasks)
        write_jsonl(
            artifacts.provider_requests_jsonl,
            [request.__dict__ for request in provider_requests],
            self.path_policy,
        )
        self._write_command_preview(artifacts.command_preview_csv, provider_requests, self.path_policy)

        job_store = self._build_job_store(run_context, run_plan, "dry_run")
        state_rows: list[dict[str, object]] = []
        for record in job_store.jobs:
            add_or_update_job(job_store, task_id=record.task_id, status="dry_run_completed", last_event="dry_run_completed")
            state_rows.append({"task_id": record.task_id, "provider": record.provider, "status": record.status, "output_path": ""})
        save_job_store(artifacts.job_store_json, job_store, self.path_policy)
        self._write_job_state_rows(artifacts, job_store.jobs, state_rows)
        self._write_execution_log(
            artifacts,
            [
                f"run_id={artifacts.run_id}",
                "mode=dry_run",
                f"task_count={len(selected_tasks)}",
                f"timestamp={datetime.utcnow().isoformat()}",
            ],
        )
        return artifacts

    def mock_run(
        self,
        tasks: Optional[list[TaskSpec]] = None,
        run_id: Optional[str] = None,
        *,
        production_id: Optional[str] = None,
        manifest_paths: Optional[Iterable[Path]] = None,
        task_or_batch_name: str = "run",
    ) -> RunArtifacts:
        selected_tasks = tasks or self._load_tasks(production_id, manifest_paths)
        if not selected_tasks:
            raise RuntimeError("No tasks available for mock run")
        run_context = self._build_run_context(production_id=production_id, run_mode=RunMode.mock, run_id=run_id, task_or_batch_name=task_or_batch_name)
        artifacts = self._make_artifacts(run_context.run_root)
        self.path_policy.mkdir(run_context.mock_outputs_dir, exist_ok=True)
        run_plan = build_run_plan(selected_tasks)
        self._write_manifest_snapshot(artifacts.run_manifest_snapshot_csv, selected_tasks, self.path_policy)
        self._write_run_plan(artifacts.run_plan_json, run_plan, self.path_policy)
        provider_requests = self._build_provider_requests(selected_tasks)
        write_jsonl(
            artifacts.provider_requests_jsonl,
            [request.__dict__ for request in provider_requests],
            self.path_policy,
        )
        self._write_command_preview(artifacts.command_preview_csv, provider_requests, self.path_policy)

        provider_responses: list[dict[str, object]] = []
        state_rows: list[dict[str, object]] = []
        job_store = self._build_job_store(run_context, run_plan, "mock")
        for request in provider_requests:
            output_ext = _default_output_extension(request.task_type.value, self.runtime_defaults)
            output_path = run_context.mock_outputs_dir / f"{request.task_id}{output_ext}"
            output_path.write_text(f"mock-output for {request.task_id}", encoding="utf-8")
            provider_task_id = f"mock-{uuid.uuid4().hex[:10]}"
            submit_id = f"submit-{uuid.uuid4().hex[:8]}"
            add_or_update_job(
                job_store,
                task_id=request.task_id,
                provider_task_id=provider_task_id,
                submit_id=submit_id,
                status="mock_submitted",
                last_event="mock_submitted",
            )
            provider_responses.append(
                {
                    "task_id": request.task_id,
                    "provider": request.provider.value,
                    "output_path": str(output_path),
                    "status": "submitted",
                }
            )
            current_record = get_job(job_store, request.task_id)
            state_rows.append(
                {
                    "task_id": request.task_id,
                    "provider": request.provider.value,
                    "status": "mock_submitted",
                    "provider_task_id": provider_task_id,
                    "submit_id": current_record.submit_id if current_record else "",
                    "output_path": str(output_path),
                }
            )

            add_or_update_job(
                job_store,
                task_id=request.task_id,
                status="mock_completed",
                last_event="mock_completed",
                output_name=request.output_name,
            )
            state_rows.append(
                {
                    "task_id": request.task_id,
                    "provider": request.provider.value,
                    "status": "mock_completed",
                    "output_path": str(output_path),
                }
            )

        save_job_store(artifacts.job_store_json, job_store, self.path_policy)
        write_jsonl(artifacts.provider_responses_jsonl, provider_responses, self.path_policy)
        self._write_job_state_rows(artifacts, job_store.jobs, state_rows)
        self._write_execution_log(
            artifacts,
            [
                f"run_id={artifacts.run_id}",
                "mode=mock",
                f"task_count={len(selected_tasks)}",
                f"task_or_batch={task_or_batch_name}",
                f"timestamp={datetime.utcnow().isoformat()}",
            ],
        )
        return artifacts

    def live_run(
        self,
        tasks: Optional[list[TaskSpec]] = None,
        run_id: Optional[str] = None,
        *,
        production_id: Optional[str] = None,
        manifest_paths: Optional[Iterable[Path]] = None,
        task_or_batch_name: str = "run",
        fs_write_plan_path: Optional[Path] = None,
        reference_registry_path: Optional[Path] = None,
        user_confirmed: bool = False,
        allow_single_task_only: bool = True,
        dry_run_id: str = "",
        stop_after_submit: bool = False,
    ) -> RunArtifacts:
        selected_tasks = tasks or self._load_tasks(production_id, manifest_paths)
        if not selected_tasks:
            raise RuntimeError("No tasks available for live run")
        run_context = self._build_run_context(
            production_id=production_id,
            run_mode=RunMode.live,
            run_id=run_id,
            task_or_batch_name=task_or_batch_name,
        )
        artifacts = self._make_artifacts(run_context.run_root)
        run_plan = build_run_plan(selected_tasks)
        self._write_manifest_snapshot(artifacts.run_manifest_snapshot_csv, selected_tasks, self.path_policy)
        self._write_run_plan(artifacts.run_plan_json, run_plan, self.path_policy)

        task = selected_tasks[0]
        staged_refs = self._stage_task_references(task) if len(selected_tasks) == 1 else []
        request = LiveRunRequest(
            production_id=production_id or "",
            task_id=task.task_id,
            run_mode=RunMode.live,
            provider=task.provider.value,
            manifest_path=next(iter(manifest_paths), None) if manifest_paths is not None else None,
            reference_registry_path=reference_registry_path,
            fs_write_plan_path=fs_write_plan_path,
            user_confirmed=user_confirmed,
            allow_single_task_only=allow_single_task_only,
            dry_run_id=dry_run_id,
            notes="Phase F1 fake live-run full loop",
        )
        decision = LiveRunGate(self.path_policy).validate(
            request,
            selected_tasks,
            self.providers_config,
            staged_media_paths=staged_refs,
        )
        if not decision.allowed:
            self._write_execution_log(
                artifacts,
                [
                    f"run_id={artifacts.run_id}",
                    "mode=live",
                    "status=denied",
                    f"reason={decision.reason}",
                    f"required_actions={';'.join(decision.required_actions)}",
                ],
            )
            raise RuntimeError(f"{decision.reason}: {', '.join(decision.required_actions)}")

        provider = self._get_provider(task.provider)
        if not isinstance(provider, FakeLiveProvider):
            raise RuntimeError("Real live provider execution is not implemented in Phase F1")

        provider_request = ProviderRequest(
            task_id=task.task_id,
            provider=task.provider,
            task_type=task.task_type,
            command_argv=provider.build_submit_command(task, staged_refs),
            output_name=task.output_name,
        )
        write_jsonl(artifacts.provider_requests_jsonl, [provider_request.__dict__], self.path_policy)
        self._write_command_preview(artifacts.command_preview_csv, [provider_request], self.path_policy)

        job_store = self._build_job_store(run_context, run_plan, "live")
        submit_result = provider.submit(task, staged_refs)
        add_or_update_job(
            job_store,
            task_id=task.task_id,
            provider_task_id=submit_result.provider_task_id,
            submit_id=submit_result.submit_id,
            status="submitted",
            last_event="fake_submit_persisted",
            output_name=task.output_name,
        )
        provider_responses: list[dict[str, object]] = [
            {
                "task_id": task.task_id,
                "provider": task.provider.value,
                "status": "submitted",
                "submit_id": submit_result.submit_id,
                "provider_task_id": submit_result.provider_task_id,
            }
        ]
        state_rows: list[dict[str, object]] = [
            {
                "task_id": task.task_id,
                "provider": task.provider.value,
                "status": "submitted",
                "provider_task_id": submit_result.provider_task_id,
                "submit_id": submit_result.submit_id,
                "output_path": "",
            }
        ]
        save_job_store(artifacts.job_store_json, job_store, self.path_policy)
        write_jsonl(artifacts.provider_responses_jsonl, provider_responses, self.path_policy)
        self._write_job_state_rows(artifacts, job_store.jobs, state_rows)
        self._write_execution_log(
            artifacts,
            [
                f"run_id={artifacts.run_id}",
                "mode=live",
                "status=submitted",
                f"submit_id={submit_result.submit_id}",
                "submit_id_persisted_before_query=true",
            ],
        )
        if stop_after_submit:
            return artifacts

        query_result = provider.query(submit_result.provider_task_id)
        query_status = "failed" if query_result.status in {"fail", "failed"} else query_result.status
        add_or_update_job(
            job_store,
            task_id=task.task_id,
            status=query_status,
            last_event=f"fake_query_{query_status}",
        )
        provider_responses.append(
            {
                "task_id": task.task_id,
                "provider": task.provider.value,
                "status": query_status,
                "provider_task_id": submit_result.provider_task_id,
            }
        )
        state_rows.append(
            {
                "task_id": task.task_id,
                "provider": task.provider.value,
                "status": query_status,
                "provider_task_id": submit_result.provider_task_id,
                "output_path": "",
            }
        )

        if query_status == "success":
            downloaded_path = provider.download(task, run_context.downloads_dir, self.path_policy)
            add_or_update_job(job_store, task_id=task.task_id, status="downloaded", last_event="fake_download_completed")
            state_rows.append(
                {
                    "task_id": task.task_id,
                    "provider": task.provider.value,
                    "status": "downloaded",
                    "provider_task_id": submit_result.provider_task_id,
                    "download_path": str(downloaded_path),
                }
            )
            provider_responses.append(
                {
                    "task_id": task.task_id,
                    "provider": task.provider.value,
                    "status": "downloaded",
                    "output_path": str(downloaded_path),
                }
            )
            if provider.scenario == "success_downloaded_not_renamed":
                save_job_store(artifacts.job_store_json, job_store, self.path_policy)
                write_jsonl(artifacts.provider_responses_jsonl, provider_responses, self.path_policy)
                self._write_job_state_rows(artifacts, job_store.jobs, state_rows)
                return artifacts
            final_output_path = self._rename_downloaded_output(downloaded_path, task, run_context.output_dir)
            add_or_update_job(job_store, task_id=task.task_id, status="completed", last_event="fake_rename_completed")
            state_rows.append(
                {
                    "task_id": task.task_id,
                    "provider": task.provider.value,
                    "status": "completed",
                    "provider_task_id": submit_result.provider_task_id,
                    "output_path": str(final_output_path),
                }
            )
            provider_responses.append(
                {
                    "task_id": task.task_id,
                    "provider": task.provider.value,
                    "status": "renamed",
                    "output_path": str(final_output_path),
                    "integrity": "present",
                }
            )

        save_job_store(artifacts.job_store_json, job_store, self.path_policy)
        write_jsonl(artifacts.provider_responses_jsonl, provider_responses, self.path_policy)
        self._write_job_state_rows(artifacts, job_store.jobs, state_rows)
        return artifacts

    def _rename_downloaded_output(self, downloaded_path: Path, task: TaskSpec, output_dir: Path) -> Path:
        self.path_policy.mkdir(output_dir, exist_ok=True)
        suffix = downloaded_path.suffix or ".txt"
        final_output_path = self.path_policy.ensure_write(output_dir / f"{task.output_name}{suffix}")
        self.path_policy.rename(downloaded_path, final_output_path)
        if not final_output_path.exists() or final_output_path.stat().st_size <= 0:
            raise RuntimeError(f"Fake output integrity check failed: {final_output_path}")
        return final_output_path

    def _stage_task_references(self, task: TaskSpec) -> list[Path]:
        staged_refs: list[Path] = []
        for ref in task.reference_ids:
            mapped_ref = self.reference_registry.get(ref, ref)
            candidate = Path(mapped_ref)
            if not candidate.is_absolute():
                candidate = self.workspace_root / candidate
            staged_refs.append(self._stage_reference(candidate))
        return staged_refs

    def _write_execution_log(self, artifacts: RunArtifacts, lines: list[str]) -> None:
        self.path_policy.write_text(artifacts.execution_log_txt, "\n".join(lines) + "\n", encoding="utf-8")

    def can_run_live(self) -> bool:
        default_cfg = self.providers_config.get("providers", {}).get(self.default_provider, {})
        return bool(default_cfg.get("allow_live_run", False))

    def run_mode_allowed(self, mode: RunMode) -> bool:
        if mode == RunMode.live:
            return bool(self.can_run_live() and self.runtime_defaults.get("default_live_enabled", False))
        return True

    def execute(
        self,
        mode: RunMode,
        tasks: Optional[list[TaskSpec]] = None,
        run_id: Optional[str] = None,
        *,
        production_id: Optional[str] = None,
        manifest_paths: Optional[Iterable[Path]] = None,
        task_or_batch_name: str = "run",
    ) -> RunArtifacts:
        if not self.run_mode_allowed(mode):
            raise RuntimeError("Live run is disabled by configuration")
        if mode == RunMode.dry_run:
            return self.dry_run(tasks, run_id=run_id, production_id=production_id, manifest_paths=manifest_paths, task_or_batch_name=task_or_batch_name)
        if mode == RunMode.mock:
            return self.mock_run(tasks, run_id=run_id, production_id=production_id, manifest_paths=manifest_paths, task_or_batch_name=task_or_batch_name)
        raise NotImplementedError("Live mode not implemented in Phase B")
