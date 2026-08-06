from __future__ import annotations

import json
from typing import Any, Iterable

from .models import ReferenceRecord


def deterministic_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ) + "\n"


def records_to_json(records: Iterable[ReferenceRecord]) -> str:
    selected = tuple(records)
    return deterministic_json(
        {
            "record_count": len(selected),
            "records": [record.to_dict() for record in selected],
        }
    )


def records_to_jsonl(records: Iterable[ReferenceRecord]) -> str:
    lines = [
        json.dumps(
            record.to_dict(),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for record in records
    ]
    return "\n".join(lines) + ("\n" if lines else "")
