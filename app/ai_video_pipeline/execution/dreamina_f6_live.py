from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Sequence

from ..core.manifest import MANIFEST_FIELDS, parse_manifest_csv
from ..core.models import ProviderName, ProviderRequest, RunMode, TaskSpec, TaskType
from ..path_policy import PathPolicy
from ..providers.dreamina_cli import DreaminaCLIProvider
from .dreamina_f4_live import (
    CommandResult,
    check_image_integrity,
    default_subprocess_runner,
    extract_field,
    extract_query_status,
    extract_submit_id,
    find_downloaded_file,
)
from .job_store import add_or_update_job, create_job_store, save_job_store
from .recorder import write_csv, write_json, write_jsonl
from .run_context import RunContext, create_run_dir
from .run_plan import build_run_plan

TASK_ID = "A-SC-TEMPLE-COURTYARD-001"
PRODUCTION_ID = "chi_yan_tian_qiong"
OUTPUT_NAME = "A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard"
MANIFEST_NAME = "production_text2image_A-SC-TEMPLE-COURTYARD-001.csv"
PROMPT_RECORD_NAME = "production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-001.json"
CHECKLIST_NAME = "A-SC-TEMPLE-COURTYARD-001_LIVE_APPROVAL_CHECKLIST.json"
FS_PLAN_NAME = "A-SC-TEMPLE-COURTYARD-001_fs_write_plan.json"
FORBIDDEN_SUBMIT_TOKENS = {
    "--output_name",
    "output_dir",
    "download_dir",
    "submit_id",
    "query_result",
    "--image",
    "--images",
    "--refs",
    "--ref_strength",
}
OLD_PATH_TOKENS = {
    "G:\\AICODING\\AI视频工作流",
    "G:\\AICODING\\dreamina_upload_staging",
    "G:\\AICODING\\AI_VIDEO\\Achieve",
    "G:\\AICODING\\AI_VIDEO\\" + "API" + "TEST",
    "G:\\AICODING\\AI_VIDEO\\" + "CLI" + "_md",
    "DreaminaBatcher",
    "AI_VIDEO_PIPELINE_V2",
    "AI_VIDEO_PIPELINE_V3",
}


@dataclass
class ProductionOneShotAuthorization:
    task_id: str
    provider: str
    task_type: str
    user_confirmed: bool
    allow_single_task_only: bool
    allow_batch: bool
    allow_parallel: bool
    allow_auto_continue: bool
    allow_retry: bool
    expires_after_submit: bool
    consumed: bool = False

    @classmethod
    def required(cls) -> "ProductionOneShotAuthorization":
        return cls(
            task_id=TASK_ID,
            provider=ProviderName.dreamina_cli.value,
            task_type=TaskType.text2image.value,
            user_confirmed=True,
            allow_single_task_only=True,
            allow_batch=False,
            allow_parallel=False,
            allow_auto_continue=False,
            allow_retry=False,
            expires_after_submit=True,
        )

    def allows(self, task: TaskSpec, task_count: int) -> bool:
        return (
            not self.consumed
            and self.user_confirmed is True
            and self.allow_single_task_only is True
            and self.allow_batch is False
            and self.allow_parallel is False
            and self.allow_auto_continue is False
            and self.allow_retry is False
            and self.expires_after_submit is True
            and task_count == 1
            and task.task_id == self.task_id
            and task.provider.value == self.provider
            and task.task_type.value == self.task_type
        )

    def consume(self) -> None:
        if self.consumed:
            raise RuntimeError("one-shot authorization is already consumed")
        self.consumed = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "provider": self.provider,
            "task_type": self.task_type,
            "user_confirmed": self.user_confirmed,
            "allow_single_task_only": self.allow_single_task_only,
            "allow_batch": self.allow_batch,
            "allow_parallel": self.allow_parallel,
            "allow_auto_continue": self.allow_auto_continue,
            "allow_retry": self.allow_retry,
            "expires_after_submit": self.expires_after_submit,
            "consumed": self.consumed,
        }


@dataclass(frozen=True)
class F6LiveResult:
    verdict: str
    run_context: RunContext
    submit_id: str
    submit_result: CommandResult | None
    query_result: CommandResult | None
    download_result: CommandResult | None
    query_status: str
    output_path: Path | None
    integrity: dict[str, Any]
    pre_submit_checks: list[str]


Runner = Callable[[Sequence[str]], CommandResult]


def load_f6_task(manifest_path: Path) -> TaskSpec:
    tasks = parse_manifest_csv(manifest_path)
    if len(tasks) != 1:
        raise ValueError("F6 manifest must contain exactly one task")
    return tasks[0]


def build_production_submit_argv(task: TaskSpec, executable: str) -> list[str]:
    return DreaminaCLIProvider(executable).build_submit_command(task, [])


def run_pre_submit_checks(
    *,
    workspace_root: Path,
    task: TaskSpec,
    providers_config: dict[str, Any],
    argv: list[str],
    run_context: RunContext,
    fs_write_plan_path: Path,
    checklist_path: Path,
    prompt_record_path: Path,
    authorization: ProductionOneShotAuthorization,
) -> list[str]:
    root = Path(workspace_root).resolve()
    policy = PathPolicy(root)
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise RuntimeError(f"pre-submit check failed: {message}")
        checks.append(message)

    dreamina_config = providers_config.get("providers", {}).get("dreamina_cli", {})
    prompt_record = json.loads(policy.ensure(prompt_record_path).read_text(encoding="utf-8"))
    require(task.task_id == TASK_ID, "task_id is exact")
    require(task.phase == "asset_scene", "phase is asset_scene")
    require(task.task_type == TaskType.text2image, "task_type is text2image")
    require(task.provider == ProviderName.dreamina_cli, "provider is dreamina_cli")
    require(task.model_version == "5.0", "model_version is 5.0")
    require(task.ratio == "16:9", "ratio is 16:9")
    require(task.resolution_type == "2k", "resolution_type is 2k")
    require(task.output_name == OUTPUT_NAME, "output_name remains internal metadata")
    require(task.reference_ids == [], "no reference media is used")
    require(prompt_record.get("asset_scope") == "production_scene_asset", "prompt record is production scene asset")
    require(dreamina_config.get("executable") == argv[0], "Dreamina executable path comes from providers.json")
    require(isinstance(argv, list) and all(isinstance(item, str) for item in argv), "command argv is a Python list")
    require(argv[1] == "text2image", "argv uses text2image")
    require(_flag_value(argv, "--model_version") == "5.0", "argv includes model_version 5.0")
    require(_flag_value(argv, "--ratio") == "16:9", "argv includes ratio 16:9")
    require(_flag_value(argv, "--prompt") == task.prompt, "argv includes prompt as one argv element")
    require(_flag_value(argv, "--resolution_type") == "2k", "argv includes resolution_type 2k")
    joined = " ".join(argv)
    for forbidden in FORBIDDEN_SUBMIT_TOKENS:
        require(forbidden not in joined, f"submit argv excludes {forbidden}")
    require(_timestamp_count(run_context.run_dir_name) == 1, "run_dir basename contains exactly one timestamp")
    require(run_context.run_root.name == run_context.run_dir_name, "run_id and run_dir basename match")
    require(run_context.run_root.is_relative_to(root), "run_dir is inside workspace")
    require(policy.ensure(fs_write_plan_path).exists(), "fs_write_plan exists")
    require(policy.ensure(checklist_path).exists(), "approval checklist exists")
    require(authorization.allows(task, 1), "one-shot user authorization applies to this exact task only")
    fs_plan = json.loads(policy.ensure(fs_write_plan_path).read_text(encoding="utf-8"))
    planned_values = [str(item) for item in fs_plan.get("planned_files", [])]
    for item in fs_plan.get("planned_operations", []):
        if isinstance(item, dict):
            planned_values.append(str(item.get("target", "")))
    for planned in planned_values:
        if planned.startswith(str(root)) or not Path(planned).is_absolute():
            require(True, f"planned output path is workspace-scoped: {planned}")
        else:
            raise RuntimeError(f"pre-submit check failed: planned output path outside workspace: {planned}")
    all_paths_text = " ".join([joined, str(run_context.run_root), *planned_values])
    for old_token in OLD_PATH_TOKENS:
        require(old_token not in all_paths_text, f"old path token absent: {old_token}")
    require(dreamina_config.get("allow_live_run") is False, "providers.json remains allow_live_run false")
    return checks


def execute_f6_live_run(
    workspace_root: Path,
    *,
    runner: Runner = default_subprocess_runner,
    authorization: ProductionOneShotAuthorization | None = None,
) -> F6LiveResult:
    root = Path(workspace_root).resolve()
    policy = PathPolicy(root)
    manifest_path = root / "productions" / PRODUCTION_ID / "manifests" / MANIFEST_NAME
    prompt_record_path = root / "productions" / PRODUCTION_ID / "prompts" / PROMPT_RECORD_NAME
    fs_plan_path = root / "reports" / FS_PLAN_NAME
    checklist_path = root / "reports" / CHECKLIST_NAME
    providers_config = json.loads(policy.ensure(root / "configs" / "providers.json").read_text(encoding="utf-8"))
    executable = providers_config["providers"]["dreamina_cli"]["executable"]
    task = load_f6_task(manifest_path)
    auth = authorization or ProductionOneShotAuthorization.required()

    run_context = create_run_dir(root, PRODUCTION_ID, RunMode.live, task.task_id, policy=policy)
    for required_dir in [run_context.downloads_dir, run_context.output_dir, run_context.raw_responses_dir, run_context.reports_dir]:
        policy.mkdir(required_dir, exist_ok=True)

    argv = build_production_submit_argv(task, executable)
    pre_checks = run_pre_submit_checks(
        workspace_root=root,
        task=task,
        providers_config=providers_config,
        argv=argv,
        run_context=run_context,
        fs_write_plan_path=fs_plan_path,
        checklist_path=checklist_path,
        prompt_record_path=prompt_record_path,
        authorization=auth,
    )
    _write_initial_artifacts(run_context, task, argv, auth, policy)

    submit_result = runner(argv)
    write_json(run_context.raw_responses_dir / "submit_response.json", _command_result_payload(submit_result), policy)
    submit_id = extract_submit_id(submit_result.stdout + "\n" + submit_result.stderr)
    auth.consume()
    _write_authorization(run_context, auth, policy)

    if submit_result.returncode != 0 or not submit_id:
        _persist_failed_submit(run_context, task, submit_result, policy)
        return F6LiveResult("PHASE_F6_FAILED", run_context, submit_id, submit_result, None, None, "submit_failed", None, {}, pre_checks)

    _persist_submitted(run_context, task, submit_result, submit_id, argv, policy)

    query_argv = [executable, "query_result", "--submit_id", submit_id]
    query_result = runner(query_argv)
    write_json(run_context.raw_responses_dir / "query_response.json", _command_result_payload(query_result), policy)
    query_status = extract_query_status(query_result.stdout + "\n" + query_result.stderr, query_result.returncode)

    if query_status == "querying":
        _persist_querying(run_context, task, submit_id, query_result, policy)
        return F6LiveResult("PHASE_F6_SUBMITTED_QUERYING", run_context, submit_id, submit_result, query_result, None, query_status, None, {}, pre_checks)
    if query_status == "success":
        download_argv = [executable, "query_result", "--submit_id", submit_id, "--download_dir", str(run_context.downloads_dir)]
        download_result = runner(download_argv)
        write_json(run_context.raw_responses_dir / "download_response.json", _command_result_payload(download_result), policy)
        if download_result.returncode != 0:
            _persist_failed_query(run_context, task, submit_id, download_result, "download_failed", policy)
            return F6LiveResult("PHASE_F6_FAILED", run_context, submit_id, submit_result, query_result, download_result, "download_failed", None, {}, pre_checks)
        raw_download = find_downloaded_file(run_context.downloads_dir)
        output_path = _rename_downloaded_image(raw_download, run_context.output_dir / f"{task.output_name}.png", policy)
        integrity = check_image_integrity(output_path)
        _persist_success(run_context, task, submit_id, query_result, download_result, raw_download, output_path, integrity, policy)
        return F6LiveResult("PHASE_F6_SUCCESS_DOWNLOADED", run_context, submit_id, submit_result, query_result, download_result, query_status, output_path, integrity, pre_checks)

    _persist_failed_query(run_context, task, submit_id, query_result, query_status, policy)
    return F6LiveResult("PHASE_F6_FAILED", run_context, submit_id, submit_result, query_result, None, query_status, None, {}, pre_checks)


def _write_initial_artifacts(run_context: RunContext, task: TaskSpec, argv: list[str], auth: ProductionOneShotAuthorization, policy: PathPolicy) -> None:
    write_csv(run_context.run_manifest_snapshot_csv, [task.to_manifest_row()], MANIFEST_FIELDS, policy)
    write_json(run_context.run_plan_json, build_run_plan([task]).to_dict(), policy)
    request = ProviderRequest(task.task_id, task.provider, task.task_type, argv, output_name=task.output_name)
    write_jsonl(run_context.provider_requests_jsonl, [request.__dict__], policy)
    write_csv(run_context.command_preview_csv, [{"task_id": task.task_id, "provider": task.provider.value, "task_type": task.task_type.value, "command": " ".join(argv)}], ["task_id", "provider", "task_type", "command"], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="planned", provider=task.provider.value, output_name=task.output_name, last_event="f6_live_plan_created")
    save_job_store(run_context.job_store_json, store, policy)
    _write_authorization(run_context, auth, policy)
    _write_log(run_context, ["phase=F6", "mode=live", "status=pre_submit_checks_passed", f"task_id={task.task_id}"], policy)


def _persist_submitted(run_context: RunContext, task: TaskSpec, result: CommandResult, submit_id: str, argv: list[str], policy: PathPolicy) -> None:
    write_csv(run_context.submitted_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "submitted", "submit_id": submit_id, "returncode": result.returncode}], ["task_id", "provider", "status", "submit_id", "returncode"], policy)
    write_jsonl(run_context.provider_responses_jsonl, [{"task_id": task.task_id, "provider": task.provider.value, "status": "submitted", "submit_id": submit_id, "provider_task_id": submit_id, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr, "credit_count": extract_field(result.stdout + result.stderr, "credit_count"), "gen_status": extract_field(result.stdout + result.stderr, "gen_status")}], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="submitted", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event="f6_submit_persisted_before_query")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["phase=F6", "mode=live", "status=submitted", f"submit_id={submit_id}", "submit_persisted_before_query=true", f"submit_returncode={result.returncode}", "batch=false", "parallel=false", "retry=false", "auto_continue=false"], policy)


def _persist_failed_submit(run_context: RunContext, task: TaskSpec, result: CommandResult, policy: PathPolicy) -> None:
    write_csv(run_context.failed_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "submit_failed", "returncode": result.returncode, "error": result.stderr or result.stdout}], ["task_id", "provider", "status", "returncode", "error"], policy)
    write_jsonl(run_context.provider_responses_jsonl, [{"task_id": task.task_id, "provider": task.provider.value, "status": "submit_failed", "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="failed", provider=task.provider.value, output_name=task.output_name, last_event="f6_submit_failed_no_retry")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["phase=F6", "mode=live", "status=submit_failed", f"submit_returncode={result.returncode}", "retry=false"], policy)


def _persist_querying(run_context: RunContext, task: TaskSpec, submit_id: str, result: CommandResult, policy: PathPolicy) -> None:
    write_csv(run_context.querying_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "querying", "submit_id": submit_id}], ["task_id", "provider", "status", "submit_id"], policy)
    write_jsonl(run_context.provider_responses_jsonl, [{"task_id": task.task_id, "provider": task.provider.value, "status": "querying", "submit_id": submit_id, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="querying", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event="f6_querying_stop_no_download")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["phase=F6", "mode=live", "status=querying", f"submit_id={submit_id}", "download=false", "retry=false"], policy)


def _persist_failed_query(run_context: RunContext, task: TaskSpec, submit_id: str, result: CommandResult, status: str, policy: PathPolicy) -> None:
    write_csv(run_context.failed_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": status, "submit_id": submit_id, "returncode": result.returncode, "error": result.stderr or result.stdout}], ["task_id", "provider", "status", "submit_id", "returncode", "error"], policy)
    write_jsonl(run_context.provider_responses_jsonl, [{"task_id": task.task_id, "provider": task.provider.value, "status": status, "submit_id": submit_id, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="failed", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event=f"f6_{status}_no_retry")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["phase=F6", "mode=live", f"status={status}", f"submit_id={submit_id}", "retry=false"], policy)


def _persist_success(run_context: RunContext, task: TaskSpec, submit_id: str, query: CommandResult, download: CommandResult, raw_download: Path, output: Path, integrity: dict[str, Any], policy: PathPolicy) -> None:
    write_csv(run_context.completed_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "completed", "submit_id": submit_id, "output_path": output}], ["task_id", "provider", "status", "submit_id", "output_path"], policy)
    write_csv(run_context.downloaded_files_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "downloaded", "submit_id": submit_id, "raw_download_path": raw_download, "renamed_output_path": output, "file_size": integrity.get("file_size", 0), "width": integrity.get("width", ""), "height": integrity.get("height", ""), "format": integrity.get("format", "")}], ["task_id", "provider", "status", "submit_id", "raw_download_path", "renamed_output_path", "file_size", "width", "height", "format"], policy)
    write_jsonl(run_context.provider_responses_jsonl, [{"task_id": task.task_id, "provider": task.provider.value, "status": "success", "submit_id": submit_id, "query_returncode": query.returncode, "download_returncode": download.returncode, "output_path": output, "integrity": integrity}], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="completed", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event="f6_download_renamed_integrity_checked")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["phase=F6", "mode=live", "status=completed", f"submit_id={submit_id}", f"output_path={output}", f"pillow_openable={integrity.get('openable')}", "retry=false"], policy)


def _write_authorization(run_context: RunContext, auth: ProductionOneShotAuthorization, policy: PathPolicy) -> None:
    write_json(run_context.reports_dir / "one_shot_live_authorization.json", auth.to_dict(), policy)


def _rename_downloaded_image(source: Path, target: Path, policy: PathPolicy) -> Path:
    safe_source = policy.ensure(source)
    safe_target = policy.ensure_write(target)
    safe_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(safe_source), str(safe_target))
    return safe_target


def _write_log(run_context: RunContext, lines: list[str], policy: PathPolicy) -> None:
    current = ""
    if run_context.execution_log_txt.exists():
        current = run_context.execution_log_txt.read_text(encoding="utf-8")
    policy.write_text(run_context.execution_log_txt, current + "\n".join(lines) + "\n", encoding="utf-8")


def _command_result_payload(result: CommandResult) -> dict[str, Any]:
    return {"argv": result.argv, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}


def _flag_value(argv: list[str], flag: str) -> str:
    if flag not in argv:
        return ""
    index = argv.index(flag)
    if index + 1 >= len(argv):
        return ""
    return argv[index + 1]


def _timestamp_count(value: str) -> int:
    import re

    return len(re.findall(r"\d{8}_\d{6}", value))
