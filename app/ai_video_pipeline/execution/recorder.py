from __future__ import annotations

import csv
import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..path_policy import PathPolicy


def _normalize_json_value(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [_normalize_json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(k): _normalize_json_value(v) for k, v in value.items()}
    return value


def write_json(path: Path, payload: Any, policy: PathPolicy) -> Path:
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        if isinstance(payload, (dict, list)):
            json.dump(payload, handle, ensure_ascii=True, indent=2)
        else:
            handle.write(json.dumps(payload, ensure_ascii=True))
    return target


def read_json(path: Path, policy: PathPolicy) -> Any:
    target = policy.ensure(path)
    return json.loads(target.read_text(encoding="utf-8"))


def write_jsonl(path: Path, rows: Iterable[Any], policy: PathPolicy) -> Path:
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        for row in rows:
            payload = _normalize_json_value(row)
            if not isinstance(payload, str):
                payload = json.dumps(payload, ensure_ascii=True)
            handle.write(payload + "\n")
    return target


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]], headers: Sequence[str], policy: PathPolicy) -> Path:
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(headers))
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _normalize_csv_value(row.get(key, "")) for key in headers})
    return target


def _normalize_csv_value(value: Any) -> str:
    normalized = _normalize_json_value(value)
    return str(normalized)
