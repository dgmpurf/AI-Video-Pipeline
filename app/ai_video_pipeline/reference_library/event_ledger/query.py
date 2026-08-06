from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from .models import LedgerEntry, ProjectionResult


@dataclass(frozen=True)
class EventQuery:
    event_types: tuple[str, ...] = ()
    pilot_clip_ids: tuple[str, ...] = ()
    authority_classes: tuple[str, ...] = ()
    source_trace_ids: tuple[str, ...] = ()

    def matches(self, entry: LedgerEntry) -> bool:
        event = entry.event.to_dict()
        if self.event_types and event["event_type"] not in self.event_types:
            return False
        if self.pilot_clip_ids and event["pilot_clip_id"] not in self.pilot_clip_ids:
            return False
        if (
            self.authority_classes
            and event["authority_class"] not in self.authority_classes
        ):
            return False
        if self.source_trace_ids and not set(self.source_trace_ids).issubset(
            event["source_trace_ids"]
        ):
            return False
        return True


def query_entries(
    entries: Iterable[LedgerEntry], query: EventQuery | None = None
) -> tuple[LedgerEntry, ...]:
    selected = query or EventQuery()
    return tuple(entry for entry in entries if selected.matches(entry))


def get_event(entries: Iterable[LedgerEntry], event_id: str) -> dict[str, Any]:
    matches = [
        entry.event.to_dict() for entry in entries if entry.event.event_id == event_id
    ]
    if len(matches) != 1:
        raise KeyError(f"event is not unique and present: {event_id}")
    return matches[0]


def projection_record(
    projection: ProjectionResult, pilot_clip_id: str
) -> dict[str, Any]:
    records = projection.to_dict()["records"]
    try:
        return records[pilot_clip_id]
    except KeyError as error:
        raise KeyError(f"unknown projected record: {pilot_clip_id}") from error


def projection_records(projection: ProjectionResult) -> list[dict[str, Any]]:
    state = projection.to_dict()
    return [
        {"pilot_clip_id": pilot_clip_id, **state["records"][pilot_clip_id]}
        for pilot_clip_id in sorted(state["records"])
    ]


def ledger_summary(
    entries: Iterable[LedgerEntry], projection: ProjectionResult
) -> dict[str, Any]:
    selected = tuple(entries)
    event_type_counts: dict[str, int] = {}
    authority_counts: dict[str, int] = {}
    for entry in selected:
        event = entry.event.to_dict()
        event_type = event["event_type"]
        authority = event["authority_class"]
        event_type_counts[event_type] = event_type_counts.get(event_type, 0) + 1
        authority_counts[authority] = authority_counts.get(authority, 0) + 1
    state = projection.to_dict()
    return {
        "ledger_id": state["ledger_id"],
        "entry_count": len(selected),
        "event_type_counts": dict(sorted(event_type_counts.items())),
        "authority_class_counts": dict(sorted(authority_counts.items())),
        "projection_hash": projection.projection_hash,
        "through_position": state["through_position"],
        "through_entry_hash": state["through_entry_hash"],
        "record_count": len(state["records"]),
        "checkpoint_count": len(state["checkpoints"]),
    }
