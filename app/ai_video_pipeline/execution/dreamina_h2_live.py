from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Sequence

from ..core.manifest import MANIFEST_FIELDS, parse_manifest_csv
from ..core.models import AssetStatus, ProviderName, ProviderRequest, ReviewStatus, RunMode, TaskSpec, TaskType
from ..path_policy import PathPolicy
from ..providers.dreamina_cli import DreaminaCLIProvider
from .job_store import add_or_update_job, create_job_store, save_job_store
from .recorder import write_csv, write_json, write_jsonl
from .run_context import RunContext, create_run_dir
from .run_plan import build_run_plan

TASK_ID = "SHOT-01-KF-001"
PRODUCTION_ID = "chi_yan_tian_qiong"
OUTPUT_NAME = "SHOT-01-KF-001_temple_courtyard_standoff_keyframe"
MANIFEST_NAME = "production_image2image_SHOT-01-KF-001.csv"
PROMPT_NAME = "shot_01_keyframe_prompt_SHOT-01-KF-001.json"
REPORT_NAME = "PHASE_H2_SHOT01_KEYFRAME_IMAGE2IMAGE_LIVE_RUN_REPORT.md"
REFERENCE_IDS = [
    "A-SC-TEMPLE-COURTYARD-001",
    "A-CH-A-SUBJECT-001",
    "A-CH-B-SUBJECT-001",
]
REFERENCE_TARGETS = ["ref_01.png", "ref_02.png", "ref_03.png"]
FORBIDDEN_SUBMIT_TOKENS = {
    "--output_name",
    "output_dir",
    "download_dir",
    "submit_id",
    "query_result",
    "--image",
    "--refs",
    "--ref_strength",
}
OLD_PATH_TOKENS = {
    "G:\\AICODING\\" + "AI视频工作流",
    "G:/AICODING/" + "AI视频工作流",
    "G:\\AICODING\\" + "AI瑙嗛",
    "G:\\AICODING\\" + "dreamina_upload" + "_staging",
    "G:/AICODING/" + "dreamina_upload" + "_staging",
    "G:\\AICODING\\AI_VIDEO\\Achieve",
    "G:\\AICODING\\AI_VIDEO\\" + "API" + "TEST",
    "G:\\AICODING\\AI_VIDEO\\" + "CLI" + "_md",
    "DreaminaBatcher",
    "AI_VIDEO_PIPELINE_V2",
    "AI_VIDEO_PIPELINE_V3",
}
UPLOAD_WARNING_TOKENS = ["gen_status: fail", "upload phase", "no file upload", "upload resource"]


@dataclass
class OneShotLiveAuthorization:
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
    def required(cls) -> "OneShotLiveAuthorization":
        return cls(
            task_id=TASK_ID,
            provider=ProviderName.dreamina_cli.value,
            task_type=TaskType.image2image.value,
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
            raise RuntimeError("one-shot live authorization is already consumed")
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
class CommandResult:
    argv: list[str]
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class H2LiveResult:
    verdict: str
    run_context: RunContext
    submit_id: str
    submit_result: CommandResult | None
    query_result: CommandResult | None
    download_result: CommandResult | None
    query_status: str
    output_path: Path | None
    raw_download_path: Path | None
    integrity: dict[str, Any]
    pre_submit_checks: list[str]
    staged_refs: list[dict[str, Any]]
    upload_warning: bool
    report_path: Path


Runner = Callable[[Sequence[str]], CommandResult]


def default_subprocess_runner(argv: Sequence[str]) -> CommandResult:
    completed = subprocess.run(
        list(argv),
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
        check=False,
    )
    return CommandResult(
        argv=list(argv),
        returncode=int(completed.returncode),
        stdout=completed.stdout or "",
        stderr=completed.stderr or "",
    )


def execute_h2_live_run(
    workspace_root: Path,
    *,
    runner: Runner = default_subprocess_runner,
    authorization: OneShotLiveAuthorization | None = None,
) -> H2LiveResult:
    root = Path(workspace_root).resolve()
    policy = PathPolicy(root)
    manifest_path = root / "productions" / PRODUCTION_ID / "manifests" / MANIFEST_NAME
    prompt_path = root / "productions" / PRODUCTION_ID / "prompts" / PROMPT_NAME
    fs_plan_path = root / "reports" / "SHOT-01-KF-001_fs_write_plan.json"
    checklist_path = root / "reports" / "SHOT-01-KF-001_LIVE_APPROVAL_CHECKLIST.json"
    providers_path = root / "configs" / "providers.json"
    providers = json.loads(policy.ensure(providers_path).read_text(encoding="utf-8"))
    executable = providers["providers"]["dreamina_cli"]["executable"]
    auth = authorization or OneShotLiveAuthorization.required()
    task = load_h2_task(manifest_path, prompt_path)

    run_context = create_run_dir(root, PRODUCTION_ID, RunMode.live, TASK_ID, policy=policy)
    staged_refs = stage_ordered_references(root, run_context, task.reference_ids, policy)
    input_media_manifest = run_context.input_media_dir / "input_media_manifest.json"
    write_json(input_media_manifest, {"task_id": TASK_ID, "references": staged_refs}, policy)

    argv = DreaminaCLIProvider(executable).build_submit_command(task, [Path(item["staged_path"]) for item in staged_refs])
    pre_checks = run_pre_submit_checks(
        workspace_root=root,
        task=task,
        providers_config=providers,
        argv=argv,
        run_context=run_context,
        fs_write_plan_path=fs_plan_path,
        checklist_path=checklist_path,
        authorization=auth,
        staged_refs=staged_refs,
    )
    _write_initial_artifacts(run_context, task, argv, auth, pre_checks, staged_refs, policy)

    responses: list[dict[str, Any]] = []
    submit_result = runner(argv)
    write_json(run_context.raw_responses_dir / "submit_response.json", command_result_payload(submit_result), policy)
    submit_text = submit_result.stdout + "\n" + submit_result.stderr
    submit_id = extract_submit_id(submit_text)
    upload_warning = has_upload_warning(submit_text)
    auth.consume()
    _write_authorization(run_context, auth, policy)

    if submit_result.returncode != 0 or not submit_id:
        _persist_failed_submit(run_context, task, submit_result, responses, policy)
        result = H2LiveResult("PHASE_H2_FAILED", run_context, submit_id, submit_result, None, None, "submit_failed", None, None, {}, pre_checks, staged_refs, upload_warning, root / "reports" / REPORT_NAME)
        _write_report(root, result, "pending", policy)
        return result

    _persist_submitted(run_context, task, submit_result, submit_id, argv, responses, upload_warning, policy)

    query_argv = [executable, "query_result", "--submit_id", submit_id]
    query_result = runner(query_argv)
    write_json(run_context.raw_responses_dir / "query_response.json", command_result_payload(query_result), policy)
    query_status = extract_query_status(query_result.stdout + "\n" + query_result.stderr, query_result.returncode)

    if query_status == "querying":
        _persist_querying(run_context, task, submit_id, query_result, responses, policy)
        verdict = "PHASE_H2_SUBMITTED_WITH_UPLOAD_WARNING" if upload_warning else "PHASE_H2_SUBMITTED_QUERYING"
        result = H2LiveResult(verdict, run_context, submit_id, submit_result, query_result, None, query_status, None, None, {}, pre_checks, staged_refs, upload_warning, root / "reports" / REPORT_NAME)
        _write_report(root, result, "pending", policy)
        return result

    if query_status == "success":
        download_argv = [executable, "query_result", "--submit_id", submit_id, "--download_dir", str(run_context.downloads_dir)]
        download_result = runner(download_argv)
        write_json(run_context.raw_responses_dir / "download_response.json", command_result_payload(download_result), policy)
        if download_result.returncode != 0:
            _persist_failed_query(run_context, task, submit_id, download_result, "download_failed", responses, policy)
            result = H2LiveResult("PHASE_H2_FAILED", run_context, submit_id, submit_result, query_result, download_result, "download_failed", None, None, {}, pre_checks, staged_refs, upload_warning, root / "reports" / REPORT_NAME)
            _write_report(root, result, "pending", policy)
            return result
        raw_download = find_downloaded_file(run_context.downloads_dir)
        output_path = rename_downloaded_image(raw_download, run_context.output_dir / f"{OUTPUT_NAME}.png", policy)
        integrity = check_image_integrity(output_path)
        _persist_success(run_context, task, submit_id, query_result, download_result, raw_download, output_path, integrity, responses, policy)
        result = H2LiveResult("PHASE_H2_SUCCESS_DOWNLOADED", run_context, submit_id, submit_result, query_result, download_result, query_status, output_path, raw_download, integrity, pre_checks, staged_refs, upload_warning, root / "reports" / REPORT_NAME)
        _write_report(root, result, "pending", policy)
        return result

    _persist_failed_query(run_context, task, submit_id, query_result, query_status, responses, policy)
    result = H2LiveResult("PHASE_H2_FAILED", run_context, submit_id, submit_result, query_result, None, query_status, None, None, {}, pre_checks, staged_refs, upload_warning, root / "reports" / REPORT_NAME)
    _write_report(root, result, "pending", policy)
    return result


def load_h2_task(manifest_path: Path, prompt_path: Path) -> TaskSpec:
    tasks = parse_manifest_csv(manifest_path)
    if len(tasks) != 1:
        raise ValueError("H2 manifest must contain exactly one task")
    task = tasks[0]
    prompt_payload = json.loads(prompt_path.read_text(encoding="utf-8"))
    task.prompt = str(prompt_payload["prompt_text"])
    return task


def stage_ordered_references(root: Path, run_context: RunContext, reference_ids: list[str], policy: PathPolicy) -> list[dict[str, Any]]:
    if reference_ids != REFERENCE_IDS:
        raise RuntimeError("pre-submit check failed: reference_ids order is exact")
    registry = json.loads((root / "productions" / PRODUCTION_ID / "assets" / "asset_registry.json").read_text(encoding="utf-8"))
    records = registry.get("assets", [])
    staged: list[dict[str, Any]] = []
    for index, logical_id in enumerate(REFERENCE_IDS, start=1):
        record = _registry_record(records, logical_id)
        if record.get("status") != AssetStatus.locked_after_human_review.value:
            raise RuntimeError(f"pre-submit check failed: {logical_id} is not locked")
        if record.get("review_status") != ReviewStatus.approved.value:
            raise RuntimeError(f"pre-submit check failed: {logical_id} is not approved")
        source = policy.ensure(root / str(record["relative_path"]))
        if "locked_refs" not in source.parts:
            raise RuntimeError(f"pre-submit check failed: {logical_id} source is not under locked_refs")
        source_integrity = check_image_integrity(source)
        expected_sha = str(record.get("sha256", "")).lower()
        if expected_sha and source_integrity["sha256"].lower() != expected_sha:
            raise RuntimeError(f"pre-submit check failed: {logical_id} sha256 does not match registry")
        target = run_context.input_media_dir / REFERENCE_TARGETS[index - 1]
        policy.copy(source, target)
        staged_integrity = check_image_integrity(target)
        if staged_integrity["sha256"].lower() != source_integrity["sha256"].lower():
            raise RuntimeError(f"pre-submit check failed: staged sha256 mismatch for {logical_id}")
        staged.append(
            {
                "order": index,
                "logical_id": logical_id,
                "source_path": str(source),
                "staged_path": str(policy.ensure(target)),
                "source_sha256": source_integrity["sha256"],
                "staged_sha256": staged_integrity["sha256"],
                "file_size": staged_integrity["file_size"],
                "width": staged_integrity["width"],
                "height": staged_integrity["height"],
                "format": staged_integrity["format"],
            }
        )
    return staged


def run_pre_submit_checks(
    *,
    workspace_root: Path,
    task: TaskSpec,
    providers_config: dict[str, Any],
    argv: list[str],
    run_context: RunContext,
    fs_write_plan_path: Path,
    checklist_path: Path,
    authorization: OneShotLiveAuthorization,
    staged_refs: list[dict[str, Any]],
) -> list[str]:
    root = Path(workspace_root).resolve()
    policy = PathPolicy(root)
    checks: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise RuntimeError(f"pre-submit check failed: {message}")
        checks.append(message)

    dreamina_cfg = providers_config.get("providers", {}).get("dreamina_cli", {})
    require(task.task_id == TASK_ID, "task_id is SHOT-01-KF-001")
    require(task.phase == "shot_keyframe", "phase is shot_keyframe")
    require(task.task_type == TaskType.image2image, "task_type is image2image")
    require(task.provider == ProviderName.dreamina_cli, "provider is dreamina_cli")
    require(task.model_version == "5.0", "model_version is 5.0")
    require(task.ratio == "16:9", "ratio is 16:9")
    require(task.resolution_type == "2k", "resolution_type is 2k")
    require(task.output_name == OUTPUT_NAME, "output_name remains internal metadata")
    require(task.reference_ids == REFERENCE_IDS, "reference_ids order is exact")
    require(len(staged_refs) == 3, "three references are staged")
    require([item["logical_id"] for item in staged_refs] == REFERENCE_IDS, "staged reference order is exact")
    require([Path(item["staged_path"]).name for item in staged_refs] == REFERENCE_TARGETS, "staged filenames are ASCII ref_NN.png")
    for item in staged_refs:
        require(Path(item["staged_path"]).is_relative_to(root), f"staged path is inside workspace: {item['logical_id']}")
        require(str(item["source_sha256"]).lower() == str(item["staged_sha256"]).lower(), f"staged sha256 matches source: {item['logical_id']}")
    require((run_context.input_media_dir / "input_media_manifest.json").exists(), "input_media_manifest is generated")
    require(isinstance(argv, list) and all(isinstance(item, str) for item in argv), "command argv is a Python list")
    require(argv[1] == "image2image", "argv uses image2image")
    require(_flag_value(argv, "--model_version") == "5.0", "argv includes model_version 5.0")
    require(_flag_value(argv, "--ratio") == "16:9", "argv includes ratio 16:9")
    require(_flag_value(argv, "--prompt") == task.prompt, "argv includes prompt as one argv element")
    require(argv.count("--images") == 3, "argv uses repeated --images")
    require(_flag_value(argv, "--resolution_type") == "2k", "argv includes resolution_type 2k")
    joined = " ".join(argv)
    for forbidden in FORBIDDEN_SUBMIT_TOKENS:
        if forbidden.startswith("--"):
            require(forbidden not in argv, f"submit argv excludes {forbidden}")
        else:
            require(forbidden not in argv, f"submit argv excludes {forbidden}")
    require(_timestamp_count(run_context.run_dir_name) == 1, "run_dir basename contains exactly one timestamp")
    require(run_context.run_root.name == run_context.run_dir_name, "run_id and run_dir basename match")
    require(run_context.run_root.is_relative_to(root), "run_dir is inside workspace")
    require(policy.ensure(fs_write_plan_path).exists(), "fs_write_plan exists")
    require(policy.ensure(checklist_path).exists(), "approval checklist exists")
    require(authorization.allows(task, 1), "scoped one-shot authorization applies to exact task")
    fs_plan = json.loads(policy.ensure(fs_write_plan_path).read_text(encoding="utf-8"))
    require(fs_plan.get("task_id") == TASK_ID, "fs_write_plan is for SHOT-01-KF-001")
    for planned in _planned_path_strings(fs_plan):
        normalized = planned.replace("\\", "/")
        require(
            normalized.startswith(str(root).replace("\\", "/")) or normalized.startswith("productions/") or "<future_run_id>" in normalized,
            f"planned output path is workspace-scoped: {planned}",
        )
    all_paths_text = " ".join([joined, str(run_context.run_root), *[str(item["staged_path"]) for item in staged_refs], *_planned_path_strings(fs_plan)])
    for token in OLD_PATH_TOKENS:
        require(token not in all_paths_text, "old path token absent")
    require(dreamina_cfg.get("allow_live_run") is False, "providers.json remains allow_live_run false")
    return checks


def check_image_integrity(path: Path) -> dict[str, Any]:
    from PIL import Image

    target = Path(path)
    payload: dict[str, Any] = {
        "exists": target.exists(),
        "file_size": target.stat().st_size if target.exists() else 0,
        "openable": False,
        "width": None,
        "height": None,
        "format": None,
        "sha256": "",
    }
    if not payload["exists"]:
        return payload
    data = target.read_bytes()
    payload["sha256"] = hashlib.sha256(data).hexdigest()
    if payload["file_size"] <= 10 * 1024:
        return payload
    with Image.open(target) as image:
        image.verify()
    with Image.open(target) as image:
        payload.update({"openable": True, "width": image.width, "height": image.height, "format": image.format})
    return payload


def extract_submit_id(text: str) -> str:
    for payload in _json_candidates(text):
        found = _find_key(payload, {"submit_id", "id", "task_id", "provider_task_id"})
        if found:
            return found
    for pattern in [r"submit[_ -]?id[\"':= ]+([A-Za-z0-9._:-]+)", r"task[_ -]?id[\"':= ]+([A-Za-z0-9._:-]+)"]:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""


def extract_query_status(text: str, returncode: int = 0) -> str:
    for payload in _json_candidates(text):
        found = _find_key(payload, {"status", "gen_status", "state"})
        if found:
            normalized = found.lower()
            if normalized in {"success", "succeeded", "done", "completed"}:
                return "success"
            if normalized in {"querying", "running", "processing", "pending"}:
                return "querying"
            if normalized in {"fail", "failed", "error"}:
                return "fail"
    lowered = text.lower()
    if "success" in lowered or "completed" in lowered:
        return "success"
    if "querying" in lowered or "processing" in lowered or "pending" in lowered:
        return "querying"
    if "fail" in lowered or "error" in lowered or returncode != 0:
        return "fail"
    return "querying"


def has_upload_warning(text: str) -> bool:
    lowered = text.lower()
    return any(token in lowered for token in UPLOAD_WARNING_TOKENS)


def find_downloaded_file(downloads_dir: Path) -> Path:
    candidates = sorted([path for path in downloads_dir.iterdir() if path.is_file()], key=lambda item: item.stat().st_mtime, reverse=True)
    if not candidates:
        raise RuntimeError("download succeeded but no downloaded file was found")
    return candidates[0]


def rename_downloaded_image(source: Path, target: Path, policy: PathPolicy) -> Path:
    safe_source = policy.ensure(source)
    safe_target = policy.ensure_write(target)
    safe_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(safe_source), str(safe_target))
    return safe_target


def command_result_payload(result: CommandResult) -> dict[str, Any]:
    return {"argv": result.argv, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}


def _registry_record(records: list[dict[str, Any]], logical_id: str) -> dict[str, Any]:
    matches = [item for item in records if item.get("logical_id") == logical_id]
    if len(matches) != 1:
        raise RuntimeError(f"pre-submit check failed: expected one registry record for {logical_id}")
    return matches[0]


def _write_initial_artifacts(
    run_context: RunContext,
    task: TaskSpec,
    argv: list[str],
    auth: OneShotLiveAuthorization,
    pre_checks: list[str],
    staged_refs: list[dict[str, Any]],
    policy: PathPolicy,
) -> None:
    write_csv(run_context.run_manifest_snapshot_csv, [task.to_manifest_row()], MANIFEST_FIELDS, policy)
    write_json(run_context.run_plan_json, build_run_plan([task]).to_dict(), policy)
    request = ProviderRequest(task.task_id, task.provider, task.task_type, argv, output_name=task.output_name)
    write_jsonl(run_context.provider_requests_jsonl, [request.__dict__], policy)
    write_csv(run_context.command_preview_csv, [{"task_id": task.task_id, "provider": task.provider.value, "task_type": task.task_type.value, "command": " ".join(argv)}], ["task_id", "provider", "task_type", "command"], policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="planned", provider=task.provider.value, output_name=task.output_name, last_event="h2_pre_submit_checks_passed")
    save_job_store(run_context.job_store_json, store, policy)
    write_json(run_context.reports_dir / "pre_submit_checks.json", {"checks": pre_checks}, policy)
    write_json(run_context.reports_dir / "staged_reference_mapping.json", {"references": staged_refs}, policy)
    _write_authorization(run_context, auth, policy)
    _write_log(run_context, ["mode=live", "phase=H2", "status=pre_submit_checks_passed", f"task_id={task.task_id}"], policy)


def _persist_submitted(
    run_context: RunContext,
    task: TaskSpec,
    result: CommandResult,
    submit_id: str,
    argv: list[str],
    responses: list[dict[str, Any]],
    upload_warning: bool,
    policy: PathPolicy,
) -> None:
    status = "submitted_with_upload_warning" if upload_warning else "submitted"
    write_csv(run_context.submitted_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": status, "submit_id": submit_id, "returncode": result.returncode}], ["task_id", "provider", "status", "submit_id", "returncode"], policy)
    responses.append({"task_id": task.task_id, "provider": task.provider.value, "status": status, "submit_id": submit_id, "provider_task_id": submit_id, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr, "credit_count": extract_field(result.stdout + result.stderr, "credit_count"), "gen_status": extract_field(result.stdout + result.stderr, "gen_status"), "upload_warning": upload_warning, "argv": argv})
    write_jsonl(run_context.provider_responses_jsonl, responses, policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status=status, provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event="submit_persisted_before_query")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["mode=live", f"status={status}", f"submit_id={submit_id}", "submit_persisted_before_query=true", f"submit_returncode={result.returncode}", f"upload_warning={str(upload_warning).lower()}", "batch=false", "parallel=false", "retry=false", "auto_continue=false"], policy)


def _persist_failed_submit(run_context: RunContext, task: TaskSpec, result: CommandResult, responses: list[dict[str, Any]], policy: PathPolicy) -> None:
    write_csv(run_context.failed_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "submit_failed", "returncode": result.returncode, "error": result.stderr or result.stdout}], ["task_id", "provider", "status", "returncode", "error"], policy)
    responses.append({"task_id": task.task_id, "provider": task.provider.value, "status": "submit_failed", "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
    write_jsonl(run_context.provider_responses_jsonl, responses, policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="failed", provider=task.provider.value, output_name=task.output_name, last_event="submit_failed_no_retry")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["mode=live", "status=submit_failed", f"submit_returncode={result.returncode}", "retry=false"], policy)


def _persist_querying(run_context: RunContext, task: TaskSpec, submit_id: str, result: CommandResult, responses: list[dict[str, Any]], policy: PathPolicy) -> None:
    write_csv(run_context.querying_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "querying", "submit_id": submit_id}], ["task_id", "provider", "status", "submit_id"], policy)
    responses.append({"task_id": task.task_id, "provider": task.provider.value, "status": "querying", "submit_id": submit_id, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
    write_jsonl(run_context.provider_responses_jsonl, responses, policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="querying", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event="querying_stop_no_download")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["mode=live", "status=querying", f"submit_id={submit_id}", "download=false", "retry=false"], policy)


def _persist_failed_query(run_context: RunContext, task: TaskSpec, submit_id: str, result: CommandResult, status: str, responses: list[dict[str, Any]], policy: PathPolicy) -> None:
    write_csv(run_context.failed_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": status, "submit_id": submit_id, "returncode": result.returncode, "error": result.stderr or result.stdout}], ["task_id", "provider", "status", "submit_id", "returncode", "error"], policy)
    responses.append({"task_id": task.task_id, "provider": task.provider.value, "status": status, "submit_id": submit_id, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
    write_jsonl(run_context.provider_responses_jsonl, responses, policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="failed", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event=f"{status}_no_retry")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["mode=live", f"status={status}", f"submit_id={submit_id}", "retry=false"], policy)


def _persist_success(
    run_context: RunContext,
    task: TaskSpec,
    submit_id: str,
    query: CommandResult,
    download: CommandResult,
    raw_download: Path,
    output: Path,
    integrity: dict[str, Any],
    responses: list[dict[str, Any]],
    policy: PathPolicy,
) -> None:
    write_csv(run_context.completed_tasks_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "completed", "submit_id": submit_id, "output_path": output}], ["task_id", "provider", "status", "submit_id", "output_path"], policy)
    write_csv(run_context.downloaded_files_csv, [{"task_id": task.task_id, "provider": task.provider.value, "status": "downloaded", "submit_id": submit_id, "raw_download_path": raw_download, "renamed_output_path": output, "file_size": integrity.get("file_size", 0), "width": integrity.get("width", ""), "height": integrity.get("height", ""), "format": integrity.get("format", ""), "sha256": integrity.get("sha256", "")}], ["task_id", "provider", "status", "submit_id", "raw_download_path", "renamed_output_path", "file_size", "width", "height", "format", "sha256"], policy)
    responses.append({"task_id": task.task_id, "provider": task.provider.value, "status": "success", "submit_id": submit_id, "query_returncode": query.returncode, "download_returncode": download.returncode, "output_path": output, "integrity": integrity})
    write_jsonl(run_context.provider_responses_jsonl, responses, policy)
    store = create_job_store(run_context.run_dir_name, PRODUCTION_ID, RunMode.live.value)
    add_or_update_job(store, task.task_id, status="completed", provider=task.provider.value, provider_task_id=submit_id, submit_id=submit_id, output_name=task.output_name, last_event="download_renamed_integrity_checked")
    save_job_store(run_context.job_store_json, store, policy)
    _write_log(run_context, ["mode=live", "status=completed", f"submit_id={submit_id}", f"output_path={output}", f"pillow_openable={integrity.get('openable')}", "retry=false"], policy)


def _write_report(root: Path, result: H2LiveResult, pytest_result: str, policy: PathPolicy) -> Path:
    submit_summary = _safe_summary(result.submit_result.stdout if result.submit_result else "")
    stderr_summary = _safe_summary(result.submit_result.stderr if result.submit_result else "")
    raw_download = str(result.raw_download_path) if result.raw_download_path else ""
    output_path = str(result.output_path) if result.output_path else ""
    query_raw = result.run_context.raw_responses_dir / "query_response.json"
    lines = [
        "# Phase H2 Shot-01 Keyframe Image2Image Live-run Report",
        "",
        "## 1) Pre-submit check result",
        f"- checks passed: `{len(result.pre_submit_checks)}`",
        "- result: `PASS`",
        "",
        "## 2) Live authorization result",
        "- scoped authorization applied to `SHOT-01-KF-001` only.",
        "- authorization consumed after submit: `true`",
        "- batch: `false`",
        "- parallel: `false`",
        "- retry: `false`",
        "- auto_continue: `false`",
        "",
        "## 3) Staged reference mapping",
    ]
    for item in result.staged_refs:
        lines.append(f"- ref_{item['order']:02d}: `{item['logical_id']}` -> `{item['staged_path']}`")
    lines.extend(
        [
            "",
            "## 4) Input media manifest",
            f"- `{result.run_context.input_media_dir / 'input_media_manifest.json'}`",
            "",
            "## 5) Actual submit argv list",
            "```json",
            json.dumps(result.submit_result.argv if result.submit_result else [], ensure_ascii=True, indent=2),
            "```",
            "",
            "## 6) Submit result",
            f"- submit_id: `{result.submit_id}`",
            f"- provider_task_id: `{result.submit_id}`",
            f"- submit stdout summary: `{submit_summary}`",
            f"- submit stderr summary: `{stderr_summary}`",
            f"- credit_count: `{extract_field((result.submit_result.stdout if result.submit_result else '') + (result.submit_result.stderr if result.submit_result else ''), 'credit_count') or 'not reported'}`",
            f"- upload warning: `{str(result.upload_warning).lower()}`",
            "",
            "## 7) Query result",
            f"- query status: `{result.query_status}`",
        ]
    )
    if result.query_status == "success":
        lines.extend(
            [
                "",
                "## 8) Download result",
                f"- raw_download_path: `{raw_download}`",
                f"- renamed output path: `{output_path}`",
                f"- file_size: `{result.integrity.get('file_size', '')}`",
                f"- width: `{result.integrity.get('width', '')}`",
                f"- height: `{result.integrity.get('height', '')}`",
                f"- format: `{result.integrity.get('format', '')}`",
                f"- sha256: `{result.integrity.get('sha256', '')}`",
                f"- Pillow status: `{result.integrity.get('openable', False)}`",
            ]
        )
    elif result.query_status == "querying":
        lines.extend(
            [
                "",
                "## 8) Querying stop state",
                f"- querying_tasks.csv path: `{result.run_context.querying_tasks_csv}`",
                f"- raw query response path: `{query_raw}`",
                "- next allowed action: query existing submit_id only.",
            ]
        )
    elif result.query_status:
        lines.extend(
            [
                "",
                "## 8) Failure state",
                f"- failed_tasks.csv path: `{result.run_context.failed_tasks_csv}`",
                f"- fail reason: `{result.query_status}`",
            ]
        )
    lines.extend(
        [
            "",
            "## 9) Safety proof",
            "- No batch, parallel, retry, or auto-continue action happened.",
            "- No old project path was accessed by this H2 module.",
            f"- All writes stayed inside `{root}`.",
            "- `configs/providers.json` was not permanently enabled.",
            "",
            "## 10) pytest result",
            f"- `{pytest_result}`",
            "",
            "## 11) Final verdict",
            f"- `{result.verdict}`",
        ]
    )
    report = root / "reports" / REPORT_NAME
    policy.write_text(report, "\n".join(lines) + "\n", encoding="utf-8")
    return report


def update_report_pytest_result(root: Path, pytest_result: str) -> None:
    report = root / "reports" / REPORT_NAME
    text = report.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^- `pending`$", f"- `{pytest_result}`", text)
    report.write_text(text, encoding="utf-8")


def _write_authorization(run_context: RunContext, auth: OneShotLiveAuthorization, policy: PathPolicy) -> None:
    write_json(run_context.reports_dir / "one_shot_live_authorization.json", auth.to_dict(), policy)


def _write_log(run_context: RunContext, lines: list[str], policy: PathPolicy) -> None:
    current = run_context.execution_log_txt.read_text(encoding="utf-8") if run_context.execution_log_txt.exists() else ""
    policy.write_text(run_context.execution_log_txt, current + "\n".join(lines) + "\n", encoding="utf-8")


def _flag_value(argv: list[str], flag: str) -> str:
    if flag not in argv:
        return ""
    index = argv.index(flag)
    return argv[index + 1] if index + 1 < len(argv) else ""


def _timestamp_count(value: str) -> int:
    return len(re.findall(r"\d{8}_\d{6}", value))


def _planned_path_strings(fs_plan: dict[str, Any]) -> list[str]:
    values = [str(item) for item in fs_plan.get("planned_files", [])]
    for item in fs_plan.get("planned_operations", []):
        if isinstance(item, dict):
            values.append(str(item.get("target", "")))
    return values


def _json_candidates(text: str) -> list[Any]:
    candidates: list[Any] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            candidates.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    try:
        candidates.append(json.loads(text))
    except json.JSONDecodeError:
        pass
    return candidates


def _find_key(payload: Any, keys: set[str]) -> str:
    if isinstance(payload, dict):
        for key, value in payload.items():
            if str(key).lower() in keys and value is not None:
                return str(value)
            nested = _find_key(value, keys)
            if nested:
                return nested
    if isinstance(payload, list):
        for item in payload:
            nested = _find_key(item, keys)
            if nested:
                return nested
    return ""


def extract_field(text: str, field: str) -> str:
    for payload in _json_candidates(text):
        found = _find_key(payload, {field})
        if found:
            return found
    match = re.search(rf"{re.escape(field)}[\"':= ]+([A-Za-z0-9._:-]+)", text, flags=re.IGNORECASE)
    return match.group(1) if match else ""


def _safe_summary(text: str, limit: int = 240) -> str:
    value = " ".join((text or "").split())
    value = value.replace("????", "[question-mark-artifact]").replace("false?True", "[false-true-artifact]")
    return value[:limit] if value else "empty"


def main() -> None:
    result = execute_h2_live_run(Path.cwd())
    print(json.dumps({"verdict": result.verdict, "run_dir": str(result.run_context.run_root), "submit_id": result.submit_id, "query_status": result.query_status}, ensure_ascii=True))


if __name__ == "__main__":
    main()
