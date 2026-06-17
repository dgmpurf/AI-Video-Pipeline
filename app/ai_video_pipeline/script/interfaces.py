from __future__ import annotations

from typing import Protocol


class ScriptExpander(Protocol):
    def expand(self, outline: str) -> str:
        """Expand a brief outline into a full production script."""
