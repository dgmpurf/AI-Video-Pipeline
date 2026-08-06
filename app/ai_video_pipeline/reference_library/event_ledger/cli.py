from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .base_catalog import load_base_catalog
from .canonical import canonical_json_text, strict_json_loads
from .errors import EventLedgerError, UnsafeLedgerPathError
from .exports import events_to_json, events_to_jsonl, projection_to_json
from .ledger import append_event, load_validated_ledger, validate_complete_ledger
from .manifest import initialize_manifest
from .projection import replay_entries
from .query import (
    EventQuery,
    get_event,
    ledger_summary,
    projection_record,
    projection_records,
    query_entries,
)


FORBIDDEN_FEATURE_TERMS = frozenset(
    {
        "media",
        "original",
        "ffprobe",
        "hash-media",
        "proxy",
        "segment",
        "sqlite",
        "database",
        "fts",
        "gui",
        "provider",
        "dreamina",
        "network",
        "source-write",
        "repository-mutation",
        "delete",
        "move",
        "rename",
        "final",
        "lock",
    }
)


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _git_marker_in_ancestors(path: Path) -> Path | None:
    current = path
    while True:
        marker = current / ".git"
        if marker.exists():
            return marker
        if current.parent == current:
            return None
        current = current.parent


def validate_write_target(path: str | Path) -> Path:
    raw = Path(path)
    if not raw.is_absolute():
        raise UnsafeLedgerPathError("write-capable ledger path must be absolute")
    resolved = raw.resolve(strict=False)
    runtime_root = Path(__file__).resolve().parent.parent
    if _inside(resolved, runtime_root):
        raise UnsafeLedgerPathError(
            "ledger target may not be inside the project reference_library runtime"
        )
    ancestor = resolved if resolved.exists() else resolved.parent
    if _git_marker_in_ancestors(ancestor) is not None:
        raise UnsafeLedgerPathError("ledger target may not be inside a Git worktree")
    return resolved


def _add_read_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--base-package", required=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="reference-library-event-ledger")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init-ledger")
    _add_read_arguments(init_parser)
    init_parser.add_argument("--created-by", required=True)
    init_parser.add_argument("--created-at", required=True)

    append_parser = subparsers.add_parser("append-event")
    _add_read_arguments(append_parser)
    append_parser.add_argument("--event-file", required=True)

    for command in (
        "validate-ledger",
        "list-events",
        "list-projections",
        "summary",
        "export-events-json",
        "export-events-jsonl",
        "export-projection-json",
    ):
        _add_read_arguments(subparsers.add_parser(command))

    replay_parser = subparsers.add_parser("replay")
    _add_read_arguments(replay_parser)
    boundary = replay_parser.add_mutually_exclusive_group()
    boundary.add_argument("--position", type=int)
    boundary.add_argument("--entry-hash")
    boundary.add_argument("--checkpoint-id")

    show_event = subparsers.add_parser("show-event")
    _add_read_arguments(show_event)
    show_event.add_argument("--event-id", required=True)

    show_projection = subparsers.add_parser("show-projection")
    _add_read_arguments(show_projection)
    show_projection.add_argument("--pilot-clip-id", required=True)

    verify_checkpoint = subparsers.add_parser("verify-checkpoint")
    _add_read_arguments(verify_checkpoint)
    verify_checkpoint.add_argument("--checkpoint-id", required=True)
    return parser


def _write_json(value: Any) -> None:
    sys.stdout.write(canonical_json_text(value, terminal_lf=True))


def _load(args: argparse.Namespace):
    adapter = load_base_catalog(args.base_package)
    manifest, entries = load_validated_ledger(args.ledger, adapter)
    projection = replay_entries(manifest, adapter, entries)
    return adapter, manifest, entries, projection


def run_command(args: argparse.Namespace) -> int:
    if args.command == "init-ledger":
        ledger = validate_write_target(args.ledger)
        adapter = load_base_catalog(args.base_package)
        manifest = initialize_manifest(
            ledger,
            adapter,
            created_by=args.created_by,
            created_at=args.created_at,
        )
        _write_json({"initialized": True, "manifest": manifest})
        return 0
    if args.command == "append-event":
        ledger = validate_write_target(args.ledger)
        adapter = load_base_catalog(args.base_package)
        event_path = Path(args.event_file)
        event = strict_json_loads(event_path.read_bytes())
        entry = append_event(ledger, adapter, event)
        _write_json({"appended": True, "entry": entry.to_dict()})
        return 0

    adapter, manifest, entries, projection = _load(args)
    if args.command == "validate-ledger":
        _write_json(validate_complete_ledger(args.ledger, adapter))
    elif args.command == "replay":
        selected = replay_entries(
            manifest,
            adapter,
            entries,
            through_position=args.position,
            through_entry_hash=args.entry_hash,
            through_checkpoint_id=args.checkpoint_id,
        )
        sys.stdout.write(projection_to_json(selected))
    elif args.command == "show-event":
        _write_json(get_event(entries, args.event_id))
    elif args.command == "list-events":
        _write_json(
            {
                "events": [
                    entry.event.to_dict()
                    for entry in query_entries(entries, EventQuery())
                ]
            }
        )
    elif args.command == "show-projection":
        _write_json(
            {
                "pilot_clip_id": args.pilot_clip_id,
                "projection_hash": projection.projection_hash,
                "record": projection_record(projection, args.pilot_clip_id),
            }
        )
    elif args.command == "list-projections":
        _write_json(
            {
                "projection_hash": projection.projection_hash,
                "records": projection_records(projection),
            }
        )
    elif args.command == "summary":
        _write_json(ledger_summary(entries, projection))
    elif args.command == "verify-checkpoint":
        checkpoint = projection.to_dict()["checkpoints"].get(args.checkpoint_id)
        if checkpoint is None:
            raise KeyError(f"unknown checkpoint: {args.checkpoint_id}")
        _write_json({"checkpoint_id": args.checkpoint_id, "verified": True})
    elif args.command == "export-events-json":
        sys.stdout.write(events_to_json(entries))
    elif args.command == "export-events-jsonl":
        sys.stdout.write(events_to_jsonl(entries))
    elif args.command == "export-projection-json":
        sys.stdout.write(projection_to_json(projection))
    else:
        raise ValueError(f"unsupported command: {args.command}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return run_command(args)
    except (EventLedgerError, KeyError, OSError, ValueError, json.JSONDecodeError) as error:
        code = getattr(error, "code", type(error).__name__)
        sys.stderr.write(
            canonical_json_text(
                {"error": {"code": code, "message": str(error)}}, terminal_lf=True
            )
        )
        return 2
