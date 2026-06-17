from __future__ import annotations

import json
import re
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from ..assets.staging import stage_media_file
from ..core.models import ProviderName, TaskSpec, TaskType
from ..path_policy import PathPolicy
from .dreamina_cli import DreaminaCLIProvider


DREAMINA_EXECUTABLE = "C:/Users/msjpurf/bin/dreamina.exe"
DREAMINA_HELP_COMMANDS: dict[str, list[str]] = {
    "root": ["-h"],
    "text2image": ["text2image", "-h"],
    "image2image": ["image2image", "-h"],
    "image2video": ["image2video", "-h"],
    "frames2video": ["frames2video", "-h"],
    "multimodal2video": ["multimodal2video", "-h"],
    "query_result": ["query_result", "-h"],
}

EXPECTED_FLAGS: dict[str, set[str]] = {
    "text2image": {"--prompt", "--model_version", "--ratio", "--resolution_type"},
    "image2image": {"--prompt", "--model_version", "--ratio", "--resolution_type", "--images"},
    "multimodal2video": {"--prompt", "--model_version", "--ratio", "--duration", "--video_resolution", "--image"},
    "image2video": {"--prompt", "--model_version", "--duration", "--video_resolution", "--image"},
    "frames2video": {"--prompt", "--model_version", "--duration", "--video_resolution", "--first", "--last"},
    "query_result": {"--submit_id", "--download_dir"},
}

FORBIDDEN_PREVIEW_FLAGS = {
    "--refs",
    "--ref_strength",
    "--output_name",
    "output_name",
    "output_dir",
    "local_output_path",
    "download_dir",
    "rename_path",
    "review_status",
    "provider_task_id",
    "submit_id",
}


@dataclass(frozen=True)
class HelpResult:
    command: str
    argv: list[str]
    stdout: str
    stderr: str
    returncode: int
    ran: bool


@dataclass(frozen=True)
class MappingComparison:
    command: str
    missing_expected_flags: list[str]
    unsupported_preview_flags_present: list[str]
    warnings: list[str]


@dataclass(frozen=True)
class PreviewResult:
    task_id: str
    argv: list[str]
    staged_media: list[str]
    valid: bool
    warnings: list[str]


def load_dreamina_executable_from_config(config_path: Path) -> str:
    payload = json.loads(Path(config_path).read_text(encoding="utf-8"))
    executable = payload.get("providers", {}).get("dreamina_cli", {}).get("executable", "")
    if executable != DREAMINA_EXECUTABLE:
        raise ValueError("dreamina_cli executable does not match configured preflight path")
    return executable


def executable_exists(executable: str) -> bool:
    return Path(executable).is_file()


def capture_help_outputs(executable: str) -> dict[str, HelpResult]:
    if executable != DREAMINA_EXECUTABLE:
        raise ValueError("refusing to run unapproved Dreamina executable")
    if not executable_exists(executable):
        return {
            name: HelpResult(
                command=name,
                argv=[executable, *args],
                stdout="",
                stderr="Executable not found; help command was not run.",
                returncode=-1,
                ran=False,
            )
            for name, args in DREAMINA_HELP_COMMANDS.items()
        }

    results: dict[str, HelpResult] = {}
    for name, args in DREAMINA_HELP_COMMANDS.items():
        completed = subprocess.run(
            [executable, *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        results[name] = HelpResult(
            command=name,
            argv=[executable, *args],
            stdout=completed.stdout or "",
            stderr=completed.stderr or "",
            returncode=int(completed.returncode),
            ran=True,
        )
    return results


def parse_supported_flags(help_text: str) -> list[str]:
    return sorted(set(re.findall(r"--[A-Za-z0-9_-]+", help_text or "")))


def build_capabilities(executable: str, help_results: Mapping[str, HelpResult], checked_at: str | None = None) -> dict[str, Any]:
    checked_at = checked_at or datetime.now(timezone.utc).isoformat()
    return {
        "executable": executable,
        "checked_at": checked_at,
        "commands": {
            name: {
                "available": result.ran and result.returncode == 0,
                "returncode": result.returncode,
                "flags": parse_supported_flags(result.stdout + "\n" + result.stderr),
            }
            for name, result in help_results.items()
            if name != "root"
        },
    }


def compare_command_mapping(help_results: Mapping[str, HelpResult]) -> list[MappingComparison]:
    comparisons: list[MappingComparison] = []
    for command, expected in EXPECTED_FLAGS.items():
        result = help_results.get(command)
        flags = set(parse_supported_flags((result.stdout + "\n" + result.stderr) if result else ""))
        missing = sorted(expected - flags)
        unsupported = sorted({"--refs", "--ref_strength"} & flags)
        warnings: list[str] = []
        if result is None or not result.ran:
            warnings.append("help command was not run")
        if missing:
            warnings.append("expected flags missing from help")
        if unsupported:
            warnings.append("unsupported preview flags appear in help")
        if command == "image2image" and "--image" in flags and "--images" not in flags:
            warnings.append("image2image help suggests --image instead of --images")
        if command == "multimodal2video" and "--images" in flags:
            warnings.append("multimodal2video help exposes --images; builder uses --image")
        if command == "image2video" and "--ratio" in flags:
            warnings.append("image2video help exposes --ratio; builder intentionally omits ratio")
        comparisons.append(
            MappingComparison(
                command=command,
                missing_expected_flags=missing,
                unsupported_preview_flags_present=unsupported,
                warnings=warnings,
            )
        )
    return comparisons


def write_help_snapshot(report_path: Path, executable: str, help_results: Mapping[str, HelpResult], path_policy: PathPolicy) -> Path:
    target = path_policy.ensure_write(report_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Dreamina CLI Help Snapshot",
        "",
        f"Executable: `{executable}`",
        "",
    ]
    for name in DREAMINA_HELP_COMMANDS:
        result = help_results[name]
        lines.extend(
            [
                f"## {name} help",
                f"- Ran: `{str(result.ran).lower()}`",
                f"- Return code: `{result.returncode}`",
                "",
                "### stdout",
                "```text",
                _clean_report_text(result.stdout),
                "```",
                "",
                "### stderr",
                "```text",
                _clean_report_text(result.stderr),
                "```",
                "",
            ]
        )
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def write_capabilities(capabilities_path: Path, capabilities: Mapping[str, Any], path_policy: PathPolicy) -> Path:
    target = path_policy.ensure_write(capabilities_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(capabilities, ensure_ascii=True, indent=2), encoding="utf-8")
    return target


def generate_preflight_command_previews(workspace_root: Path, executable: str, path_policy: PathPolicy) -> list[PreviewResult]:
    preview_dir = path_policy.ensure_write(Path(workspace_root) / "reports" / "preflight_command_previews")
    preview_dir.mkdir(parents=True, exist_ok=True)
    staging_root = path_policy.ensure_write(Path(workspace_root) / "staging" / "preflight")
    staging_root.mkdir(parents=True, exist_ok=True)
    media_root = path_policy.ensure(Path(workspace_root) / "tests" / "fixtures" / "media")
    provider = DreaminaCLIProvider(executable)

    specs = [
        (
            TaskSpec(
                task_id="TEST-PREFLIGHT-I2I",
                phase="phaseF2",
                task_type=TaskType.image2image,
                provider=ProviderName.dreamina_cli,
                model_version="5.0",
                ratio="16:9",
                resolution_type="2k",
                prompt="preflight image2image prompt",
                reference_ids=["ref_a", "ref_b", "scene"],
                output_name="TEST-PREFLIGHT-I2I_output",
            ),
            ["ref_a.png", "ref_b.png", "scene.png"],
        ),
        (
            TaskSpec(
                task_id="TEST-PREFLIGHT-M2V",
                phase="phaseF2",
                task_type=TaskType.multimodal2video,
                provider=ProviderName.dreamina_cli,
                model_version="seedance2.0fast_vip",
                ratio="16:9",
                duration=5,
                video_resolution="720p",
                prompt="preflight multimodal2video prompt",
                reference_ids=["keyframe", "ref_a", "ref_b", "scene"],
                output_name="TEST-PREFLIGHT-M2V_output",
            ),
            ["keyframe.png", "ref_a.png", "ref_b.png", "scene.png"],
        ),
        (
            TaskSpec(
                task_id="TEST-PREFLIGHT-I2V",
                phase="phaseF2",
                task_type=TaskType.image2video,
                provider=ProviderName.dreamina_cli,
                model_version="seedance2.0fast_vip",
                ratio="16:9",
                duration=5,
                video_resolution="720p",
                prompt="preflight image2video prompt",
                reference_ids=["keyframe"],
                output_name="TEST-PREFLIGHT-I2V_output",
            ),
            ["keyframe.png"],
        ),
    ]

    results: list[PreviewResult] = []
    for task, filenames in specs:
        staged_paths = [stage_media_file(media_root / name, staging_root, path_policy)[0] for name in filenames]
        argv = provider.build_submit_command(task, staged_paths)
        warnings = _validate_preview(task, argv, staged_paths, path_policy)
        result = PreviewResult(
            task_id=task.task_id,
            argv=argv,
            staged_media=[str(path) for path in staged_paths],
            valid=not warnings,
            warnings=warnings,
        )
        _write_preview_files(preview_dir, result)
        results.append(result)
    return results


def run_dreamina_preflight(workspace_root: Path) -> dict[str, Any]:
    root = Path(workspace_root).resolve()
    policy = PathPolicy(root)
    executable = load_dreamina_executable_from_config(root / "configs" / "providers.json")
    help_results = capture_help_outputs(executable)
    snapshot_path = write_help_snapshot(root / "reports" / "DREAMINA_CLI_HELP_SNAPSHOT.md", executable, help_results, policy)
    capabilities = build_capabilities(executable, help_results)
    capabilities_path = write_capabilities(root / "configs" / "dreamina_cli_capabilities.json", capabilities, policy)
    previews = generate_preflight_command_previews(root, executable, policy)
    comparisons = compare_command_mapping(help_results)
    return {
        "executable": executable,
        "executable_exists": executable_exists(executable),
        "help_commands_ran": any(result.ran for result in help_results.values()),
        "snapshot_path": str(snapshot_path),
        "capabilities_path": str(capabilities_path),
        "previews": [asdict(result) for result in previews],
        "comparisons": [asdict(result) for result in comparisons],
    }


def _validate_preview(task: TaskSpec, argv: list[str], staged_paths: list[Path], path_policy: PathPolicy) -> list[str]:
    warnings: list[str] = []
    joined = " ".join(argv)
    for forbidden in FORBIDDEN_PREVIEW_FLAGS:
        if forbidden in joined:
            warnings.append(f"forbidden preview token present: {forbidden}")
    if task.task_type == TaskType.image2image and argv.count("--images") != len(staged_paths):
        warnings.append("image2image preview must use repeated --images")
    if task.task_type == TaskType.multimodal2video and argv.count("--image") != len(staged_paths):
        warnings.append("multimodal2video preview must use repeated --image")
    if task.task_type == TaskType.image2video and argv.count("--image") != 1:
        warnings.append("image2video preview must use a single --image")
    for staged in staged_paths:
        path_policy.ensure(staged)
        if not staged.name.isascii():
            warnings.append("staged filename is not ASCII")
    return warnings


def _write_preview_files(preview_dir: Path, result: PreviewResult) -> None:
    base = preview_dir / result.task_id
    (base.with_suffix(".argv.json")).write_text(json.dumps(result.argv, ensure_ascii=True, indent=2), encoding="utf-8")
    (base.with_suffix(".command.txt")).write_text(" ".join(result.argv) + "\n", encoding="utf-8")
    (base.with_suffix(".validation.json")).write_text(
        json.dumps({"valid": result.valid, "warnings": result.warnings, "staged_media": result.staged_media}, ensure_ascii=True, indent=2),
        encoding="utf-8",
    )


def _clean_report_text(value: str) -> str:
    return (value or "").replace("????", "[question-mark artifact]").replace("false?True", "[false-true artifact]")
