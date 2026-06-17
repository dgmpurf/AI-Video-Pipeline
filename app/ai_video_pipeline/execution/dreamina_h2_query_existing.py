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

from ..core.manifest import parse_manifest_csv
from ..core.models import RunMode
from ..path_policy import PathPolicy
from .job_store import add_or_update_job, load_job_store, save_job_store
from .recorder import write_json
from .run_context import RunContext

TASK_ID = "SHOT-01-KF-001"
PRODUCTION_ID = "chi_yan_tian_qiong"
RUN_DIR_NAME = "20260614_064100_SHOT-01-KF-001"
SUBMIT_ID = "ccff71eb-e233-4a43-8ddc-7c756d1161bf"
OUTPUT_NAME = "SHOT-01-KF-001_temple_courtyard_standoff_keyframe.png"
MANIFEST_NAME = "production_image2image_SHOT-01-KF-001.csv"
REPORT_NAME = "PHASE_H2_1_EXISTING_SUBMIT_QUERY_REPORT.md"


@dataclass(frozen=True)
class CommandResult:
    argv: list[str]
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class H2QueryResult:
    verdict: str
    run_root: Path
    submit_id: str
    query_status: str
    query_argv: list[str]
    query_result: str
    query_stderr: str
    query_returncode: int
    output_path: Path | None
    raw_download_path: Path | None
    integrity: dict[str, Any]
    providers_live_flag_before: bool
    providers_live_flag_after: bool
    run_artifacts_updated: bool
    external_path_touched: bool


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


def execute_h2_query_only(workspace_root: Path, *, runner: Runner = default_subprocess_runner) -> H2QueryResult:
    root = Path(workspace_root).resolve()
    policy = PathPolicy(root)
    providers_path = root / "configs" / "providers.json"
    providers_payload = json.loads(policy.ensure(providers_path).read_text(encoding="utf-8"))
    providers_live_before = bool(
        providers_payload.get("providers", {})
        .get("dreamina_cli", {})
        .get("allow_live_run", False)
    )
    manifest = root / "productions" / PRODUCTION_ID / "manifests" / MANIFEST_NAME
    task = parse_manifest_csv(policy.ensure(manifest))[0]
    run_root = policy.ensure(root / "productions" / PRODUCTION_ID / "runs" / "live" / RUN_DIR_NAME)
    if not run_root.is_relative_to(root):
        raise RuntimeError("H2.1 run directory must stay inside workspace")

    run_context = RunContext(
        workspace_root=root,
        production_id=PRODUCTION_ID,
        run_mode=RunMode.live,
        run_dir_name=RUN_DIR_NAME,
        run_root=run_root,
        policy=policy,
    )

    executable = providers_payload.get("providers", {}).get("dreamina_cli", {}).get("executable")
    if not executable:
        raise RuntimeError("missing dreamina_cli.executable")

    query_argv = [executable, "query_result", "--submit_id", SUBMIT_ID]
    query_result = runner(query_argv)
    query_text = query_result.stdout + "\n" + query_result.stderr
    write_json(run_root / "raw_responses" / "query_response.json", command_result_payload(query_result), policy)

    query_status = extract_query_status(query_text, query_result.returncode)
    raw_download_path: Path | None = None
    output_path: Path | None = None
    integrity: dict[str, Any] = {}

    if query_status == "querying":
        _append_csv_row(
            run_context.querying_tasks_csv,
            ["task_id", "provider", "status", "submit_id"],
            [{"task_id": TASK_ID, "provider": "dreamina_cli", "status": "querying", "submit_id": SUBMIT_ID}],
            policy,
        )
        _update_job_store(
            run_context,
            task.task_id,
            status="querying",
            provider="dreamina_cli",
            provider_task_id=SUBMIT_ID,
            submit_id=SUBMIT_ID,
            output_name=task.output_name,
            last_event="querying_stop_no_download",
            policy=policy,
        )
        _append_execution_log(
            run_context,
            [
                "mode=live",
                "status=querying",
                f"submit_id={SUBMIT_ID}",
                "retry=false",
            ],
            policy,
        )
        verdict = "PHASE_H2_1_QUERYING"
    elif query_status == "success":
        download_argv = [executable, "query_result", "--submit_id", SUBMIT_ID, "--download_dir", str(run_context.downloads_dir)]
        download_result = runner(download_argv)
        write_json(run_root / "raw_responses" / "download_response.json", command_result_payload(download_result), policy)
        if download_result.returncode != 0:
            _append_csv_row(
                run_context.failed_tasks_csv,
                ["task_id", "provider", "status", "submit_id", "returncode", "error"],
                [{"task_id": TASK_ID, "provider": "dreamina_cli", "status": "download_failed", "submit_id": SUBMIT_ID, "returncode": download_result.returncode, "error": download_result.stderr or download_result.stdout}],
                policy,
            )
            _append_execution_log(
                run_context,
                ["mode=live", "status=download_failed", f"submit_id={SUBMIT_ID}", "retry=false"],
                policy,
            )
            verdict = "PHASE_H2_1_FAILED"
        else:
            raw_download_path = find_downloaded_file(run_context.downloads_dir)
            output_path = run_context.output_dir / OUTPUT_NAME
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(raw_download_path), str(output_path))
            integrity = check_image_integrity(output_path)
            _append_csv_row(
                run_context.completed_tasks_csv,
                ["task_id", "provider", "status", "submit_id", "output_path"],
                [{"task_id": TASK_ID, "provider": "dreamina_cli", "status": "completed", "submit_id": SUBMIT_ID, "output_path": str(output_path)}],
                policy,
            )
            downloaded_rows = [
                {
                    "task_id": TASK_ID,
                    "provider": "dreamina_cli",
                    "status": "downloaded",
                    "submit_id": SUBMIT_ID,
                    "raw_download_path": str(raw_download_path),
                    "renamed_output_path": str(output_path),
                    "file_size": integrity.get("file_size", 0),
                    "width": integrity.get("width", ""),
                    "height": integrity.get("height", ""),
                    "format": integrity.get("format", ""),
                    "sha256": integrity.get("sha256", ""),
                }
            ]
            _append_csv_row(
                run_context.downloaded_files_csv,
                ["task_id", "provider", "status", "submit_id", "raw_download_path", "renamed_output_path", "file_size", "width", "height", "format", "sha256"],
                downloaded_rows,
                policy,
            )
            _update_job_store(
                run_context,
                task.task_id,
                status="completed",
                provider="dreamina_cli",
                provider_task_id=SUBMIT_ID,
                submit_id=SUBMIT_ID,
                output_name=task.output_name,
                last_event="download_renamed_integrity_checked",
                policy=policy,
            )
            _append_execution_log(
                run_context,
                [
                    "mode=live",
                    "status=download_success",
                    f"submit_id={SUBMIT_ID}",
                    f"output_path={output_path}",
                    "retry=false",
                    f"pillow_openable={str(integrity.get('openable', False)).lower()}",
                ],
                policy,
            )
            verdict = "PHASE_H2_1_SUCCESS_DOWNLOADED"
    else:
        _append_csv_row(
            run_context.failed_tasks_csv,
            ["task_id", "provider", "status", "submit_id", "returncode", "error"],
            [{"task_id": TASK_ID, "provider": "dreamina_cli", "status": query_status, "submit_id": SUBMIT_ID, "returncode": query_result.returncode, "error": query_text}],
            policy,
        )
        _update_job_store(
            run_context,
            task.task_id,
            status="failed",
            provider="dreamina_cli",
            provider_task_id=SUBMIT_ID,
            submit_id=SUBMIT_ID,
            output_name=task.output_name,
            last_event=f"{query_status}_no_retry",
            policy=policy,
        )
        _append_execution_log(run_context, ["mode=live", f"status={query_status}", f"submit_id={SUBMIT_ID}", "retry=false"], policy)
        verdict = "PHASE_H2_1_FAILED"

    providers_payload_after = json.loads(policy.ensure(providers_path).read_text(encoding="utf-8"))
    providers_live_after = bool(providers_payload_after.get("providers", {}).get("dreamina_cli", {}).get("allow_live_run", False))
    providers_path_is_unchanged = providers_payload_after == providers_payload
    if not providers_path_is_unchanged:
        raise RuntimeError("providers.json changed during query-only flow")

    _write_report(
        root=root,
        verdict=verdict,
        run_root=run_root,
        submit_id=SUBMIT_ID,
        query_argv=query_argv,
        query_status=query_status,
        query_text=query_text,
        query_returncode=query_result.returncode,
        query_stderr=query_result.stderr,
        run_context=run_context,
        output_path=output_path,
        raw_download_path=raw_download_path,
        integrity=integrity,
        providers_live_before=providers_live_before,
        providers_live_after=providers_live_after,
        policy=policy,
    )
    return H2QueryResult(
        verdict=verdict,
        run_root=run_root,
        submit_id=SUBMIT_ID,
        query_status=query_status,
        query_argv=query_argv,
        query_result=query_result.stdout,
        query_stderr=query_result.stderr,
        query_returncode=query_result.returncode,
        output_path=output_path,
        raw_download_path=raw_download_path,
        integrity=integrity,
        providers_live_flag_before=providers_live_before,
        providers_live_flag_after=providers_live_after,
        run_artifacts_updated=True,
        external_path_touched=False,
    )


def _append_execution_log(run_context: RunContext, lines: list[str], policy: PathPolicy) -> None:
    current = run_context.execution_log_txt.read_text(encoding="utf-8") if run_context.execution_log_txt.exists() else ""
    run_context.policy.write_text(run_context.execution_log_txt, current + "\n".join(lines) + "\n", encoding="utf-8")


def _append_csv_row(path: Path, header: list[str], rows: list[dict[str, Any]], policy: PathPolicy) -> None:
    existing_rows: list[dict[str, Any]] = []
    if path.exists():
        text = policy.ensure(path).read_text(encoding="utf-8").strip()
        if text:
            with path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                existing_rows = [dict(item) for item in reader]
    fieldnames = list(header)
    all_rows = existing_rows + rows
    policy.ensure(path).parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _update_job_store(
    run_context: RunContext,
    task_id: str,
    *,
    status: str,
    provider: str,
    provider_task_id: str,
    submit_id: str,
    output_name: str,
    last_event: str,
    policy: PathPolicy,
) -> None:
    store = load_job_store(run_context.job_store_json, policy)
    add_or_update_job(
        store,
        task_id,
        status=status,
        provider=provider,
        provider_task_id=provider_task_id,
        submit_id=submit_id,
        output_name=output_name,
        last_event=last_event,
    )
    save_job_store(run_context.job_store_json, store, policy)


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


def find_downloaded_file(downloads_dir: Path) -> Path:
    candidates = sorted(
        [path for path in downloads_dir.iterdir() if path.is_file()],
        key=lambda item: item.stat().st_mtime,
        reverse=True,
    )
    if not candidates:
        raise RuntimeError("download succeeded but no downloaded file was found")
    return candidates[0]


def command_result_payload(result: CommandResult) -> dict[str, Any]:
    return {"argv": result.argv, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}


def _safe_summary(text: str, limit: int = 240) -> str:
    value = " ".join((text or "").split())
    value = value.replace("????", "[question-mark-artifact]").replace("false?True", "[false-true-artifact]")
    return value[:limit] if value else "empty"


def _write_report(
    *,
    root: Path,
    verdict: str,
    run_root: Path,
    submit_id: str,
    query_argv: list[str],
    query_status: str,
    query_text: str,
    query_returncode: int,
    query_stderr: str,
    run_context: RunContext,
    output_path: Path | None,
    raw_download_path: Path | None,
    integrity: dict[str, Any],
    providers_live_before: bool,
    providers_live_after: bool,
    policy: PathPolicy,
) -> None:
    query_raw = run_context.raw_responses_dir / "query_response.json"
    download_raw = run_context.raw_responses_dir / "download_response.json"
    lines = [
        "# Phase H2.1 Existing Submit Query Report",
        "",
        "## 1) task_id and submit_id",
        f"- task_id: `{TASK_ID}`",
        f"- submit_id: `{submit_id}`",
        "",
        "## 2) query command used",
        "```json",
        json.dumps(query_argv, ensure_ascii=True, indent=2),
        "```",
        "",
        "## 3) query result",
        f"- query status: `{query_status}`",
        f"- query returncode: `{query_returncode}`",
        f"- query stdout summary: `{_safe_summary(query_text)}`",
        f"- query stderr summary: `{_safe_summary(query_stderr)}`",
        "",
    ]
    if query_status == "success":
        lines.extend(
            [
                "## 4) success download result",
                f"- raw_download_path: `{raw_download_path}`",
                f"- renamed_output_path: `{output_path}`",
                f"- file_size: `{integrity.get('file_size', '')}`",
                f"- width: `{integrity.get('width', '')}`",
                f"- height: `{integrity.get('height', '')}`",
                f"- format: `{integrity.get('format', '')}`",
                f"- sha256: `{integrity.get('sha256', '')}`",
                f"- Pillow status: `{integrity.get('openable', False)}`",
                "",
            ]
        )
    elif query_status == "querying":
        lines.extend(
            [
                "## 4) querying stop state",
                f"- querying_tasks.csv path: `{run_context.querying_tasks_csv}`",
                f"- raw query response path: `{query_raw}`",
                "- next allowed action: query existing submit_id only.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## 4) failure state",
                f"- failed_tasks.csv path: `{run_context.failed_tasks_csv}`",
                f"- fail reason: `{query_status}`",
                "",
            ]
        )
    lines.extend(
        [
            "## 5) updated artifacts",
            f"- run_dir: `{run_root}`",
            f"- query raw response path: `{query_raw}`",
            f"- download response path: `{download_raw}`",
            f"- completed_tasks.csv path: `{run_context.completed_tasks_csv}`",
            f"- downloaded_files.csv path: `{run_context.downloaded_files_csv}`",
            f"- job_store.json path: `{run_context.job_store_json}`",
            f"- execution_log.txt path: `{run_context.execution_log_txt}`",
            "",
            "## 6) safety proof",
            "- No new submit happened.",
            "- No retry command was executed.",
            "- Query was executed only for `ccff71eb-e233-4a43-8ddc-7c756d1161bf`.",
            "- All writes stayed inside the workspace root.",
            f"- providers.json dreamina_cli.allow_live_run before: `{str(providers_live_before).lower()}`",
            f"- providers.json dreamina_cli.allow_live_run after: `{str(providers_live_after).lower()}`",
            "",
            "## 7) pytest result",
            "- `python -m pytest -q`",
            "",
            "## 8) Final verdict",
            f"- `{verdict}`",
        ]
    )
    policy.write_text(root / "reports" / REPORT_NAME, "\n".join(lines) + "\n", encoding="utf-8")


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


def main() -> None:
    result = execute_h2_query_only(Path.cwd())
    print(json.dumps({"verdict": result.verdict, "run_dir": str(result.run_root), "submit_id": result.submit_id, "query_status": result.query_status}, ensure_ascii=True))


if __name__ == "__main__":
    main()
