from __future__ import annotations

from typing import Protocol


class ShotPlanner(Protocol):
    def plan_shots(self, script: str) -> list[str]:
        """Create shot list from a script."""
