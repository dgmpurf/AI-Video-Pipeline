from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from app.ai_video_pipeline.execution.runner import PipelineRunner
from app.ai_video_pipeline.path_policy import PathPolicy
from app.ai_video_pipeline.providers.dreamina_preflight import (
    build_capabilities,
    generate_preflight_command_previews,
    parse_supported_flags,
    write_capabilities,
)

ROOT = Path(__file__).resolve().parents[1]
EXECUTABLE = "C:/Users/msjpurf/bin/dreamina.exe"

IMAGE2IMAGE_HELP = """
usage: dreamina image2image [-h] --model_version MODEL --ratio RATIO --resolution_type RES --images IMAGE --prompt PROMPT --output_name NAME
"""

MULTIMODAL2VIDEO_HELP = """
usage: dreamina multimodal2video [-h] --model_version MODEL --ratio RATIO --duration DURATION --video_resolution VIDEO_RESOLUTION --image IMAGE --prompt PROMPT --output_name NAME
"""


class _Help:
    def __init__(self, stdout: str, stderr: str = "", returncode: int = 0, ran: bool = True) -> None:
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode
        self.ran = ran


def _workspace(tmp_path: Path) -> Path:
    workspace = tmp_path / "ws"
    (workspace / "reports").mkdir(parents=True, exist_ok=True)
    (workspace / "staging").mkdir(parents=True, exist_ok=True)
    (workspace / "configs").mkdir(parents=True, exist_ok=True)
    (workspace / "tests" / "fixtures" / "media").mkdir(parents=True, exist_ok=True)
    for item in ["path_policy.json", "providers.json", "runtime_defaults.json"]:
        shutil.copy2(ROOT / "configs" / item, workspace / "configs" / item)
    for name in ["ref_a.png", "ref_b.png", "scene.png", "keyframe.png"]:
        (workspace / "tests" / "fixtures" / "media" / name).write_text(f"dummy {name}", encoding="utf-8")
    return workspace


def test_01_preflight_parser_detects_images_in_image2image_help() -> None:
    assert "--images" in parse_supported_flags(IMAGE2IMAGE_HELP)


def test_02_preflight_parser_detects_image_in_multimodal2video_help() -> None:
    assert "--image" in parse_supported_flags(MULTIMODAL2VIDEO_HELP)


def test_03_preflight_parser_rejects_refs_as_unsupported_when_absent() -> None:
    flags = parse_supported_flags(MULTIMODAL2VIDEO_HELP)
    assert "--refs" not in flags
    assert "--ref_strength" not in flags


def test_04_capabilities_json_can_be_generated_from_fixture_help(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    capabilities = build_capabilities(
        EXECUTABLE,
        {
            "image2image": _Help(IMAGE2IMAGE_HELP),
            "multimodal2video": _Help(MULTIMODAL2VIDEO_HELP),
        },
        checked_at="2026-06-13T00:00:00+00:00",
    )
    path = write_capabilities(workspace / "configs" / "dreamina_cli_capabilities.json", capabilities, PathPolicy(workspace))
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["commands"]["image2image"]["available"] is True
    assert "--images" in payload["commands"]["image2image"]["flags"]


def test_05_image2image_preview_uses_repeated_images(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    previews = generate_preflight_command_previews(workspace, EXECUTABLE, PathPolicy(workspace))
    i2i = next(item for item in previews if item.task_id == "TEST-PREFLIGHT-I2I")
    assert i2i.argv.count("--images") == 3


def test_06_multimodal2video_preview_uses_repeated_image(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    previews = generate_preflight_command_previews(workspace, EXECUTABLE, PathPolicy(workspace))
    m2v = next(item for item in previews if item.task_id == "TEST-PREFLIGHT-M2V")
    assert m2v.argv.count("--image") == 4
    assert "--images" not in m2v.argv


def test_07_image2video_preview_uses_single_image(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    previews = generate_preflight_command_previews(workspace, EXECUTABLE, PathPolicy(workspace))
    i2v = next(item for item in previews if item.task_id == "TEST-PREFLIGHT-I2V")
    assert i2v.argv.count("--image") == 1
    assert "--ratio" not in i2v.argv


def test_08_preview_submit_command_never_includes_output_dir(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    previews = generate_preflight_command_previews(workspace, EXECUTABLE, PathPolicy(workspace))
    for preview in previews:
        joined = " ".join(preview.argv)
        assert "output_name" not in joined
        assert "output_dir" not in joined
        assert "--refs" not in joined
        assert "--ref_strength" not in joined


def test_09_preflight_outputs_stay_inside_workspace(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    generate_preflight_command_previews(workspace, EXECUTABLE, PathPolicy(workspace))
    for path in (workspace / "reports" / "preflight_command_previews").glob("*"):
        assert path.is_relative_to(workspace)


def test_10_staged_preview_media_stays_inside_workspace(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    previews = generate_preflight_command_previews(workspace, EXECUTABLE, PathPolicy(workspace))
    for preview in previews:
        for staged in preview.staged_media:
            assert Path(staged).is_relative_to(workspace)
            assert Path(staged).name.isascii()


def test_11_live_run_remains_disabled(tmp_path: Path) -> None:
    workspace = _workspace(tmp_path)
    assert PipelineRunner(workspace).can_run_live() is False


def test_12_dreamina_cli_allow_live_run_remains_false() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert payload["providers"]["dreamina_cli"]["allow_live_run"] is False


def test_13_fake_provider_remains_test_only() -> None:
    payload = json.loads((ROOT / "configs" / "providers.json").read_text(encoding="utf-8"))
    assert "fake_live_provider" not in payload["providers"]


@pytest.mark.parametrize(
    "path",
    [
        ROOT / "reports" / "PHASE_F2_DREAMINA_PREFLIGHT_REPORT.md",
        ROOT / "reports" / "DREAMINA_CLI_HELP_SNAPSHOT.md",
    ],
)
def test_14_reports_do_not_contain_question_mark_artifact(path: Path) -> None:
    assert "????" not in path.read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "path",
    [
        ROOT / "reports" / "PHASE_F2_DREAMINA_PREFLIGHT_REPORT.md",
        ROOT / "reports" / "DREAMINA_CLI_HELP_SNAPSHOT.md",
    ],
)
def test_15_reports_do_not_contain_false_true_artifact(path: Path) -> None:
    assert "false?True" not in path.read_text(encoding="utf-8")
