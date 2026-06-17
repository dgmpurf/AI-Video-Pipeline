from __future__ import annotations

from pathlib import Path
from typing import Sequence

from .base import ProviderAdapter
from ..core.models import TaskSpec, TaskType


class DreaminaCLIProvider(ProviderAdapter):
    def __init__(self, executable: str = "dreamina") -> None:
        self.executable = executable

    def build_submit_command(self, task: TaskSpec, references: Sequence[Path]) -> list[str]:
        cmd = [self.executable, task.task_type.value]

        if task.task_type == TaskType.text2image:
            self._append_if_present(cmd, "--model_version", task.model_version)
            self._append_if_present(cmd, "--ratio", task.ratio)
            cmd.extend(["--prompt", task.prompt])
            self._append_if_present(cmd, "--resolution_type", task.resolution_type)
        elif task.task_type == TaskType.image2image:
            self._append_if_present(cmd, "--model_version", task.model_version)
            self._append_if_present(cmd, "--ratio", task.ratio)
            cmd.extend(["--prompt", task.prompt])
            for ref in references:
                cmd.extend(["--images", str(ref)])
            self._append_if_present(cmd, "--resolution_type", task.resolution_type)
        elif task.task_type == TaskType.image2video:
            if not references:
                raise ValueError("image2video requires exactly one image reference")
            self._append_if_present(cmd, "--model_version", task.model_version)
            cmd.extend(["--prompt", task.prompt])
            self._append_if_present(cmd, "--duration", None if task.duration is None else str(task.duration))
            self._append_if_present(cmd, "--video_resolution", task.video_resolution)
            cmd.extend(["--image", str(references[0])])
        elif task.task_type == TaskType.frames2video:
            if len(references) < 2:
                raise ValueError("frames2video requires at least two frame refs")
            self._append_if_present(cmd, "--model_version", task.model_version)
            cmd.extend(["--prompt", task.prompt])
            self._append_if_present(cmd, "--duration", None if task.duration is None else str(task.duration))
            self._append_if_present(cmd, "--video_resolution", task.video_resolution)
            cmd.extend(["--first", str(references[0]), "--last", str(references[-1])])
        elif task.task_type == TaskType.multimodal2video:
            if not references:
                raise ValueError("multimodal2video requires at least one reference image")
            self._append_if_present(cmd, "--model_version", task.model_version)
            self._append_if_present(cmd, "--ratio", task.ratio)
            cmd.extend(["--prompt", task.prompt])
            self._append_if_present(cmd, "--duration", None if task.duration is None else str(task.duration))
            self._append_if_present(cmd, "--video_resolution", task.video_resolution)
            for ref in references:
                cmd.extend(["--image", str(ref)])

        return cmd

    @staticmethod
    def _append_if_present(cmd: list[str], flag: str, value: str | None) -> None:
        if value:
            cmd.extend([flag, value])
