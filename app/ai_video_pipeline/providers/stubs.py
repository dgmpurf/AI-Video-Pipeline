from __future__ import annotations

from pathlib import Path
from typing import Sequence

from .base import ProviderAdapter
from ..core.models import TaskSpec


class StubProvider(ProviderAdapter):
    def build_submit_command(self, task: TaskSpec, references: Sequence[Path]) -> list[str]:
        if False:
            # Keep signature parity for linting and future extension.
            return references  # pragma: no cover
        return ["python", "-m", "ai_video_pipeline.provider_stub", str(task.task_type.value)]
