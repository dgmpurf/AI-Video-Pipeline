from __future__ import annotations

from typing import Protocol


class StoryPlanner(Protocol):
    def plan_story(self, source_text: str) -> str:
        """Return a structured story plan."""

