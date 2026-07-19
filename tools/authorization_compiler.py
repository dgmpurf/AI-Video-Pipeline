from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from app.ai_video_pipeline.governance.authorization_serialization import (  # noqa: E402
    compile_authorization_bytes,
    stable_json_bytes,
    verify_authorization_bytes,
    verify_authorization_record,
    verify_checkpoint_binding,
)


class OutputAlreadyExistsError(RuntimeError):
    pass


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile or verify exact authorization bytes without live actions."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    compile_parser = commands.add_parser("compile")
    _add_exact_input(compile_parser)
    _add_output_options(compile_parser)

    verify_parser = commands.add_parser("verify")
    _add_exact_input(verify_parser)
    verify_parser.add_argument("--expected-byte-length", required=True, type=int)
    verify_parser.add_argument("--expected-sha256", required=True)
    verify_parser.add_argument("--expected-base64")
    _add_output_options(verify_parser)

    record_parser = commands.add_parser("verify-record")
    _add_exact_input(record_parser)
    record_parser.add_argument("--record", required=True, type=Path)
    _add_output_options(record_parser)

    checkpoint_parser = commands.add_parser("verify-checkpoint")
    checkpoint_parser.add_argument("--required-checkpoint", required=True)
    checkpoint_parser.add_argument("--local-head", required=True)
    checkpoint_parser.add_argument("--origin-main", required=True)
    _add_output_options(checkpoint_parser)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        payload, passed = _run_command(args)
        _emit(payload, output=args.output, overwrite=args.overwrite)
    except OutputAlreadyExistsError:
        _emit_error(args.command, "output_exists_overwrite_not_authorized")
        return 2
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError):
        _emit_error(args.command, "input_or_output_error")
        return 2
    return 0 if passed else 1


def _run_command(args: argparse.Namespace) -> tuple[dict[str, Any], bool]:
    if args.command == "verify-checkpoint":
        result = verify_checkpoint_binding(
            args.required_checkpoint,
            args.local_head,
            args.origin_main,
        )
        payload = result.to_dict()
        payload["command"] = args.command
        return payload, result.checkpoint_binding_verified

    raw_bytes = _read_exact_input(args)
    if args.command == "compile":
        result = compile_authorization_bytes(raw_bytes)
    elif args.command == "verify":
        expected: dict[str, Any] = {
            "byte_length": args.expected_byte_length,
            "sha256": args.expected_sha256,
        }
        if args.expected_base64 is not None:
            expected["base64"] = args.expected_base64
        result = verify_authorization_bytes(raw_bytes, expected)
    elif args.command == "verify-record":
        record_bytes = args.record.read_bytes()
        record = json.loads(record_bytes.decode("utf-8", errors="strict"))
        if not isinstance(record, Mapping):
            raise ValueError("authorization record must contain a JSON object")
        result = verify_authorization_record(raw_bytes, record)
    else:
        raise ValueError("unsupported command")

    payload = result.to_dict()
    payload["command"] = args.command
    return payload, result.authorization_verified


def _add_exact_input(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text-file", type=Path)
    group.add_argument("--stdin-exact", action="store_true")


def _add_output_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--output", type=Path)
    parser.add_argument("--overwrite", action="store_true")


def _read_exact_input(args: argparse.Namespace) -> bytes:
    if args.text_file is not None:
        return args.text_file.read_bytes()
    return sys.stdin.buffer.read()


def _emit(payload: Mapping[str, Any], *, output: Path | None, overwrite: bool) -> None:
    encoded = stable_json_bytes(payload)
    if output is None:
        sys.stdout.buffer.write(encoded)
        sys.stdout.buffer.flush()
        return
    _atomic_write_bytes(output, encoded, overwrite=overwrite)


def _emit_error(command: str, error: str) -> None:
    payload = {
        "authorized_operation_count_consumed": 0,
        "command": command,
        "eligible_for_authority_activation": False,
        "error": error,
        "execution_authority_active": False,
        "provider_command_allowed": False,
        "provider_command_invocation_count": 0,
    }
    sys.stderr.buffer.write(stable_json_bytes(payload))
    sys.stderr.buffer.flush()


def _atomic_write_bytes(path: Path, data: bytes, *, overwrite: bool) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.", suffix=".tmp", dir=str(target.parent)
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if overwrite:
            os.replace(temporary, target)
        else:
            try:
                os.link(temporary, target)
            except FileExistsError as error:
                raise OutputAlreadyExistsError from error
            temporary.unlink()
        _fsync_parent(target.parent)
    finally:
        if temporary.exists():
            temporary.unlink()


def _fsync_parent(parent: Path) -> None:
    directory_flag = getattr(os, "O_DIRECTORY", None)
    if directory_flag is None:
        return
    descriptor: int | None = None
    try:
        descriptor = os.open(str(parent), os.O_RDONLY | directory_flag)
        os.fsync(descriptor)
    except OSError:
        return
    finally:
        if descriptor is not None:
            os.close(descriptor)


if __name__ == "__main__":
    raise SystemExit(main())
