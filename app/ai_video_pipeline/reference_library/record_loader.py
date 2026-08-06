from __future__ import annotations

from .models import ReferenceRecord
from .schema_loader import CandidatePackageData


EXPECTED_PILOT_CLIP_IDS = tuple(
    f"G01D-CLIP-{number:03}" for number in range(1, 31)
)


class RecordLoadError(ValueError):
    pass


def load_reference_records(
    package: CandidatePackageData,
) -> tuple[ReferenceRecord, ...]:
    raw_records = package.raw_records
    if len(raw_records) != len(EXPECTED_PILOT_CLIP_IDS):
        raise RecordLoadError("candidate package must contain exactly 30 records")

    records = tuple(ReferenceRecord.from_mapping(value) for value in raw_records)
    observed_ids = tuple(record.pilot_clip_id for record in records)
    if observed_ids != EXPECTED_PILOT_CLIP_IDS:
        raise RecordLoadError("record IDs or record order do not match the contract")
    if len({record.record_id for record in records}) != len(records):
        raise RecordLoadError("record_id values must be unique")
    return records
