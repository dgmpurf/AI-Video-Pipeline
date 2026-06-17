"""Validation helpers for manifest and task fields."""

from __future__ import annotations

from typing import Any, Iterable, List
from .models import ProviderName, TaskType


def parse_reference_ids(raw: str) -> List[str]:
    if not raw:
        return []
    return [item.strip() for item in raw.split("|") if item and item.strip()]


def parse_int_maybe(value: str) -> int | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    try:
        return int(text)
    except ValueError as exc:
        raise ValueError(f"Invalid integer field: {value}") from exc


def parse_task_type(value: str) -> TaskType:
    try:
        return TaskType(value.strip())
    except Exception as exc:
        valid = ", ".join([item.value for item in TaskType])
        raise ValueError(f"Invalid task_type '{value}'. Valid values: {valid}") from exc


def parse_provider_name(value: str) -> ProviderName:
    try:
        return ProviderName(value.strip())
    except Exception as exc:
        valid = ", ".join([item.value for item in ProviderName])
        raise ValueError(f"Invalid provider '{value}'. Valid values: {valid}") from exc


def ensure_non_empty(value: Any, field_name: str) -> str:
    text = "" if value is None else str(value).strip()
    if text == "":
        raise ValueError(f"Missing required field: {field_name}")
    return text
