from __future__ import annotations

from typing import Protocol


class PromptGenerator(Protocol):
    def generate_prompt(self, scene_desc: str) -> str:
        """Generate prompt text for an image/video generation task."""
