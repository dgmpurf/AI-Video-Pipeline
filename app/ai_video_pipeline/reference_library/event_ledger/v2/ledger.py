from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Iterable, Mapping

from app.ai_video_pipeline.reference_library.event_ledger.locking import ExclusiveLedgerLock

from .canonical import (
    canonical_json_bytes,
    require_exact_keys,
    require_sha256,
    sha256_hex,
    strict_json_loads,
)
from .errors import DuplicateEventError, EventCollisionError, LedgerValidationError
from .manifest import EVENTS_FILENAME, LOCK_FILENAME, read_manifest
from .models import BaseV01Snapshot, LedgerEntry
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


def _entry_hash(value: Mapping[str, Any]) -> str:
    return sha256_hex(canonical_json_bytes(dict(value)))


def build_entry(
    manifest: Mapping[str, Any],
    event: Mapping[str, Any],
    *,
    position: int,
    previous_entry_hash: str,
) -> dict[str, Any]:
    body = {
        "ledger_schema_version": manifest["ledger_schema_version"],
        "ledger_id": manifest["ledger_id"],
        "ledger_position": position,
        "previous_entry_hash": previous_entry_hash,
        "event": dict(event),
    }
    return {**body, "entry_hash": _entry_hash(body)}


def validate_entry(
    value: Any,
    *,
    manifest: Mapping[str, Any],
    expected_position: int,
    expected_previous_hash: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise LedgerValidationError("ledger entry must be an object")
    try:
        require_exact_keys(value, ENTRY_FIELDS, field="ledger entry")
        if value["ledger_schema_version"] != manifest["ledger_schema_version"]:
            raise LedgerValidationError("ledger schema differs")
        if value["ledger_id"] != manifest["ledger_id"]:
            raise LedgerValidationError("ledger ID differs")
        if value["ledger_position"] != expected_position:
            raise LedgerValidationError("ledger position is duplicate or skipped")
        require_sha256(value["previous_entry_hash"], field="previous_entry_hash")
        if value["previous_entry_hash"] != expected_previous_hash:
            raise LedgerValidationError("previous-entry hash is broken")
        validate_stored_event(value["event"])
        require_sha256(value["entry_hash"], field="entry_hash")
        if value["entry_hash"] != _entry_hash(
            {key: child for key, child in value.items() if key != "entry_hash"}
        ):
            raise LedgerValidationError("entry hash does not match")
    except LedgerValidationError:
        raise
    except Exception as error:
        raise LedgerValidationError(str(error)) from error
    return value


def read_ledger_entries(
    ledger_dir: str | Path,
    *,
    manifest: Mapping[str, Any],
) -> tuple[LedgerEntry, ...]:
    path = Path(ledger_dir) / EVENTS_FILENAME
    if not path.exists():
        return ()
    if path.is_symlink() or not path.is_file():
        raise LedgerValidationError("events.jsonl is not a regular file")
    raw = path.read_bytes()
    if not raw or not raw.endswith(b"\n"):
        raise LedgerValidationError("events.jsonl is empty or missing final LF")
    entries: list[LedgerEntry] = []
    previous = ZERO_HASH
    seen: dict[str, str] = {}
    for position, line in enumerate(raw.splitlines(), start=1):
        if not line:
            raise LedgerValidationError("blank JSONL line is forbidden")
        value = strict_json_loads(line)
        if line != canonical_json_bytes(value):
            raise LedgerValidationError("ledger entry is not canonical JSON")
        validate_entry(
            value,
            manifest=manifest,
            expected_position=position,
            expected_previous_hash=previous,
        )
        event = value["event"]
        prior_hash = seen.get(event["event_id"])
        if prior_hash is not None:
            if prior_hash == event["event_body_hash"]:
                raise LedgerValidationError("ledger contains a duplicate event ID")
            raise LedgerValidationError("ledger contains an event ID collision")
        seen[event["event_id"]] = event["event_body_hash"]
        entry = LedgerEntry(value)
        entries.append(entry)
        previous = entry.entry_hash
    return tuple(entries)


def load_validated_ledger(
    ledger_dir: str | Path,
    base: BaseV01Snapshot,
    *,
    accepted_checkpoints: Iterable[Mapping[str, Any]] = (),
) -> tuple[dict[str, Any], tuple[LedgerEntry, ...]]:
    manifest = read_manifest(ledger_dir, base=base)
    entries = read_ledger_entries(ledger_dir, manifest=manifest)
    replay_entries(
        manifest, base, entries, accepted_checkpoints=tuple(accepted_checkpoints)
    )
    return manifest, entries


def _append_durable(path: Path, data: bytes) -> None:
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT | getattr(os, "O_BINARY", 0)
    descriptor = os.open(path, flags, 0o600)
    try:
        offset = 0
        while offset < len(data):
            count = os.write(descriptor, data[offset:])
            if count <= 0:
                raise OSError("ledger append made no progress")
            offset += count
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def append_event(
    ledger_dir: str | Path,
    base: BaseV01Snapshot,
    event_draft: Mapping[str, Any],
    *,
    accepted_checkpoints: Iterable[Mapping[str, Any]] = (),
) -> LedgerEntry:
    root = Path(ledger_dir)
    checkpoints = tuple(accepted_checkpoints)
    manifest = read_manifest(root, base=base)
    with ExclusiveLedgerLock(root / LOCK_FILENAME):
        existing = read_ledger_entries(root, manifest=manifest)
        replay_entries(manifest, base, existing, accepted_checkpoints=checkpoints)
        event = finalize_event(event_draft)
        for prior_entry in existing:
            prior = prior_entry.event
            if prior.event_id != event["event_id"]:
                continue
            if prior.event_body_hash == event["event_body_hash"] and prior.to_dict() == event:
                raise DuplicateEventError(f"duplicate event: {prior.event_id}")
            raise EventCollisionError(f"event ID collision: {prior.event_id}")
        candidate = LedgerEntry(
            build_entry(
                manifest,
                event,
                position=len(existing) + 1,
                previous_entry_hash=existing[-1].entry_hash if existing else ZERO_HASH,
            )
        )
        replay_entries(
            manifest, base, (*existing, candidate), accepted_checkpoints=checkpoints
        )
        _append_durable(
            root / EVENTS_FILENAME,
            canonical_json_bytes(candidate.to_dict(), terminal_lf=True),
        )
        observed = read_ledger_entries(root, manifest=manifest)
        if len(observed) != len(existing) + 1 or observed[-1].to_dict() != candidate.to_dict():
            raise LedgerValidationError("post-write V0.2 ledger validation differs")
        return candidate


def validate_complete_ledger(
    ledger_dir: str | Path,
    base: BaseV01Snapshot,
    *,
    accepted_checkpoints: Iterable[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    manifest, entries = load_validated_ledger(
        ledger_dir, base, accepted_checkpoints=tuple(accepted_checkpoints)
    )
    projection = replay_entries(
        manifest, base, entries, accepted_checkpoints=tuple(accepted_checkpoints)
    )
    return {
        "ledger_id": manifest["ledger_id"],
        "entry_count": len(entries),
        "last_entry_hash": entries[-1].entry_hash if entries else ZERO_HASH,
        "projection_hash": projection.projection_hash,
        "valid": True,
    }
