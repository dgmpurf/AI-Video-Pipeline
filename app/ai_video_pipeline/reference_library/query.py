from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Iterable

from .models import ReferenceRecord


SORT_FIELDS = (
    "pilot_clip_id",
    "record_id",
    "content_family_primary",
    "content_scope",
    "current_total_derived_media_bytes",
)


@dataclass(frozen=True)
class ReferenceQuery:
    pilot_clip_ids: tuple[str, ...] = ()
    content_families: tuple[str, ...] = ()
    content_scopes: tuple[str, ...] = ()
    reference_duties: tuple[str, ...] = ()
    technical_validation_statuses: tuple[str, ...] = ()
    artifact_availabilities: tuple[str, ...] = ()
    artifact_lifecycles: tuple[str, ...] = ()
    taxonomy_statuses: tuple[str, ...] = ()
    sort_by: str = "pilot_clip_id"
    descending: bool = False

    def __post_init__(self) -> None:
        if self.sort_by not in SORT_FIELDS:
            raise ValueError(f"unsupported sort field: {self.sort_by}")

    def matches(self, record: ReferenceRecord) -> bool:
        if self.pilot_clip_ids and record.pilot_clip_id not in self.pilot_clip_ids:
            return False
        if (
            self.content_families
            and record.content_family_primary not in self.content_families
        ):
            return False
        if self.content_scopes and record.content_scope not in self.content_scopes:
            return False
        if self.reference_duties and not set(self.reference_duties).issubset(
            record.reference_duties
        ):
            return False
        if self.technical_validation_statuses and not set(
            self.technical_validation_statuses
        ).intersection(record.technical_validation_statuses):
            return False
        if self.artifact_availabilities and not set(
            self.artifact_availabilities
        ).intersection(record.artifact_availabilities):
            return False
        if self.artifact_lifecycles and not set(self.artifact_lifecycles).intersection(
            record.artifact_lifecycles
        ):
            return False
        if (
            self.taxonomy_statuses
            and record.reference_taxonomy_status not in self.taxonomy_statuses
        ):
            return False
        return True


def _sort_value(record: ReferenceRecord, field: str) -> Any:
    return getattr(record, field)


def apply_query(
    records: Iterable[ReferenceRecord], query: ReferenceQuery
) -> tuple[ReferenceRecord, ...]:
    selected = (record for record in records if query.matches(record))
    return tuple(
        sorted(
            selected,
            key=lambda record: (
                _sort_value(record, query.sort_by),
                record.pilot_clip_id,
            ),
            reverse=query.descending,
        )
    )


def _counter(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def summarize_records(records: Iterable[ReferenceRecord]) -> dict[str, Any]:
    selected = tuple(records)
    return {
        "record_count": len(selected),
        "pilot_clip_ids": [record.pilot_clip_id for record in selected],
        "content_family_primary": _counter(
            record.content_family_primary for record in selected
        ),
        "content_scope": _counter(record.content_scope for record in selected),
        "reference_taxonomy_status": _counter(
            record.reference_taxonomy_status for record in selected
        ),
        "current_proxy_bytes": sum(
            record.current_proxy_bytes for record in selected
        ),
        "current_segment_bytes": sum(
            record.current_segment_bytes for record in selected
        ),
        "current_total_derived_media_bytes": sum(
            record.current_total_derived_media_bytes for record in selected
        ),
    }
