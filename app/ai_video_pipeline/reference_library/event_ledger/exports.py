from __future__ import annotations

from typing import Any, Iterable

from .canonical import canonical_json_text
from .models import LedgerEntry, ProjectionResult


def events_to_json(entries: Iterable[LedgerEntry]) -> str:
    selected = tuple(entries)
    return canonical_json_text(
        {
            "event_count": len(selected),
            "events": [entry.event.to_dict() for entry in selected],
        },
        terminal_lf=True,
    )


def events_to_jsonl(entries: Iterable[LedgerEntry]) -> str:
    lines = [canonical_json_text(entry.event.to_dict()) for entry in entries]
    return "\n".join(lines) + "\n"


def projection_to_json(projection: ProjectionResult) -> str:
    return canonical_json_text(
        {
            "projection_hash": projection.projection_hash,
            "projection": projection.to_dict(),
        },
        terminal_lf=True,
    )


def deterministic_json(value: Any) -> str:
    return canonical_json_text(value, terminal_lf=True)
