from __future__ import annotations

import os
from pathlib import Path
from typing import Any, BinaryIO, Iterable

from .canonical import (
    canonical_json_bytes,
    require_exact_keys,
    require_sha256,
    sha256_hex,
    strict_json_loads,
)
from .errors import (
    DuplicateEventError,
    EventCollisionError,
    LedgerValidationError,
)
from .locking import ExclusiveLedgerLock
from .manifest import EVENTS_FILENAME, LOCK_FILENAME, read_manifest
from .models import BaseCatalogAdapter, LedgerEntry
from .projection import replay_entries
from .schema import finalize_event, validate_stored_event


ENTRY_FIELDS = frozenset(
    {
        "ledger_schema_version",
        "ledger_id",
        "ledger_position",
        "previous_entry_hash",
        "event",
        "entry_hash",
    }
)
ZERO_HASH = "0" * 64


def _entry_hash(value_without_hash: dict[str, Any]) -> str:
    return sha256_hex(canonical_json_bytes(value_without_hash))


def build_entry(
    manifest: dict[str, Any],
    event: dict[str, Any],
    *,
    position: int,
    previous_entry_hash: str,
) -> dict[str, Any]:
    body = {
        "ledger_schema_version": manifest["ledger_schema_version"],
        "ledger_id": manifest["ledger_id"],
        "ledger_position": position,
        "previous_entry_hash": previous_entry_hash,
        "event": event,
    }
    return {**body, "entry_hash": _entry_hash(body)}


def validate_entry(
    value: Any,
    *,
    manifest: dict[str, Any],
    expected_position: int,
    expected_previous_hash: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise LedgerValidationError("ledger entry must be an object")
    try:
        require_exact_keys(value, ENTRY_FIELDS, field="ledger entry")
        if value["ledger_schema_version"] != manifest["ledger_schema_version"]:
            raise LedgerValidationError("entry ledger schema version differs")
        if value["ledger_id"] != manifest["ledger_id"]:
            raise LedgerValidationError("entry ledger ID differs")
        if not isinstance(value["ledger_position"], int) or isinstance(
            value["ledger_position"], bool
        ):
            raise LedgerValidationError("ledger position must be an integer")
        if value["ledger_position"] != expected_position:
            raise LedgerValidationError("ledger position is duplicate or skipped")
        require_sha256(value["previous_entry_hash"], field="previous_entry_hash")
        if value["previous_entry_hash"] != expected_previous_hash:
            raise LedgerValidationError("previous-entry hash is broken")
        validate_stored_event(value["event"])
        require_sha256(value["entry_hash"], field="entry_hash")
        body = {key: child for key, child in value.items() if key != "entry_hash"}
        if value["entry_hash"] != _entry_hash(body):
            raise LedgerValidationError("entry hash does not match")
    except LedgerValidationError:
        raise
    except Exception as error:
        raise LedgerValidationError(str(error)) from error
    return value


def read_ledger_entries(
    ledger_dir: str | Path,
    *,
    manifest: dict[str, Any],
) -> tuple[LedgerEntry, ...]:
    path = Path(ledger_dir) / EVENTS_FILENAME
    if not path.exists():
        return ()
    if path.is_symlink() or not path.is_file():
        raise LedgerValidationError("events.jsonl is not a regular file")
    raw = path.read_bytes()
    if not raw:
        raise LedgerValidationError("existing events.jsonl is empty residue")
    if not raw.endswith(b"\n"):
        raise LedgerValidationError("events.jsonl is missing final LF")
    entries: list[LedgerEntry] = []
    previous_hash = ZERO_HASH
    seen_event_ids: dict[str, str] = {}
    for position, line in enumerate(raw.splitlines(), start=1):
        if not line:
            raise LedgerValidationError("blank JSONL line is forbidden")
        try:
            value = strict_json_loads(line)
        except Exception as error:
            raise LedgerValidationError(f"invalid entry at position {position}: {error}") from error
        if line != canonical_json_bytes(value):
            raise LedgerValidationError("ledger entry is not canonical JSON")
        validate_entry(
            value,
            manifest=manifest,
            expected_position=position,
            expected_previous_hash=previous_hash,
        )
        event = value["event"]
        existing_hash = seen_event_ids.get(event["event_id"])
        if existing_hash is not None:
            if existing_hash == event["event_body_hash"]:
                raise LedgerValidationError("ledger contains a duplicate event ID")
            raise LedgerValidationError("ledger contains an event ID collision")
        seen_event_ids[event["event_id"]] = event["event_body_hash"]
        entry = LedgerEntry(value)
        entries.append(entry)
        previous_hash = entry.entry_hash
    return tuple(entries)


def load_validated_ledger(
    ledger_dir: str | Path,
    adapter: BaseCatalogAdapter,
) -> tuple[dict[str, Any], tuple[LedgerEntry, ...]]:
    manifest = read_manifest(ledger_dir, adapter=adapter)
    entries = read_ledger_entries(ledger_dir, manifest=manifest)
    replay_entries(manifest, adapter, entries)
    return manifest, entries


def _write_complete(handle: BinaryIO, data: bytes) -> None:
    view = memoryview(data)
    written = 0
    while written < len(view):
        count = handle.write(view[written:])
        if count is None or count <= 0:
            raise OSError("ledger append made no progress")
        written += count


def _append_durable(path: Path, data: bytes) -> None:
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT | getattr(os, "O_BINARY", 0)
    descriptor = os.open(path, flags, 0o600)
    with os.fdopen(descriptor, "ab", buffering=0, closefd=True) as handle:
        _write_complete(handle, data)
        handle.flush()
        os.fsync(handle.fileno())


def _post_write_validate(
    ledger_dir: Path,
    *,
    manifest: dict[str, Any],
    adapter: BaseCatalogAdapter,
    expected_entries: tuple[LedgerEntry, ...],
    expected_tail: LedgerEntry,
) -> None:
    observed = read_ledger_entries(ledger_dir, manifest=manifest)
    replay_entries(manifest, adapter, observed)
    if len(observed) != len(expected_entries) + 1:
        raise LedgerValidationError("post-write ledger length differs")
    tail = observed[-1]
    expected = expected_tail.to_dict()
    actual = tail.to_dict()
    fields = (
        "ledger_position",
        "previous_entry_hash",
        "entry_hash",
    )
    if any(actual[field] != expected[field] for field in fields):
        raise LedgerValidationError("post-write tail identity differs")
    for field in ("event_id", "event_body_hash"):
        if actual["event"][field] != expected["event"][field]:
            raise LedgerValidationError("post-write event identity differs")


def append_event(
    ledger_dir: str | Path,
    adapter: BaseCatalogAdapter,
    event_draft: dict[str, Any],
) -> LedgerEntry:
    root = Path(ledger_dir)
    manifest = read_manifest(root, adapter=adapter)
    lock_path = root / LOCK_FILENAME
    with ExclusiveLedgerLock(lock_path):
        existing = read_ledger_entries(root, manifest=manifest)
        current_projection = replay_entries(manifest, adapter, existing)
        event = finalize_event(event_draft)
        for entry in existing:
            prior = entry.event
            if prior.event_id != event["event_id"]:
                continue
            if (
                prior.event_body_hash == event["event_body_hash"]
                and prior.to_dict() == event
            ):
                raise DuplicateEventError(f"duplicate event: {prior.event_id}")
            raise EventCollisionError(f"event ID collision: {prior.event_id}")
        position = len(existing) + 1
        previous_hash = existing[-1].entry_hash if existing else ZERO_HASH
        value = build_entry(
            manifest,
            event,
            position=position,
            previous_entry_hash=previous_hash,
        )
        candidate = LedgerEntry(value)
        replay_entries(manifest, adapter, (*existing, candidate))
        _append_durable(root / EVENTS_FILENAME, canonical_json_bytes(value) + b"\n")
        _post_write_validate(
            root,
            manifest=manifest,
            adapter=adapter,
            expected_entries=existing,
            expected_tail=candidate,
        )
        return candidate


def validate_complete_ledger(
    ledger_dir: str | Path, adapter: BaseCatalogAdapter
) -> dict[str, Any]:
    manifest, entries = load_validated_ledger(ledger_dir, adapter)
    projection = replay_entries(manifest, adapter, entries)
    return {
        "ledger_id": manifest["ledger_id"],
        "entry_count": len(entries),
        "last_entry_hash": entries[-1].entry_hash if entries else ZERO_HASH,
        "projection_hash": projection.projection_hash,
        "valid": True,
    }
