from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from .catalog import CatalogLookupError, ReferenceCatalog
from .exports import deterministic_json, records_to_json, records_to_jsonl
from .query import ReferenceQuery, SORT_FIELDS
from .record_loader import RecordLoadError
from .schema_loader import CandidatePackageError
from .validator import CatalogValidationError


FORBIDDEN_OPTIONS = (
    "--output",
    "--write",
    "--database",
    "--sqlite",
    "--fts",
    "--media-path",
    "--original-path",
    "--provider",
    "--dreamina",
    "--source-write",
    "--repository-write",
    "--delete",
    "--remove",
    "--replay",
)


def _reject_forbidden_options(arguments: Sequence[str]) -> None:
    for argument in arguments:
        option = argument.split("=", 1)[0]
        if option in FORBIDDEN_OPTIONS:
            raise ValueError(f"forbidden read-only option: {option}")


def _add_query_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--pilot-clip-id", action="append", default=[])
    parser.add_argument("--content-family", action="append", default=[])
    parser.add_argument("--content-scope", action="append", default=[])
    parser.add_argument("--reference-duty", action="append", default=[])
    parser.add_argument("--technical-status", action="append", default=[])
    parser.add_argument("--artifact-availability", action="append", default=[])
    parser.add_argument("--artifact-lifecycle", action="append", default=[])
    parser.add_argument("--taxonomy-status", action="append", default=[])
    parser.add_argument("--sort-by", choices=SORT_FIELDS, default="pilot_clip_id")
    parser.add_argument("--descending", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m app.ai_video_pipeline.reference_library",
        description="Read-only RL-P0 candidate catalog",
    )
    parser.add_argument("--package", required=True, help="bound candidate ZIP")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate package and fixed invariants")
    subparsers.add_parser("summary", help="emit a deterministic catalog summary")
    show = subparsers.add_parser("show", help="emit one complete record")
    show.add_argument("identifier")
    for name in ("list", "export-json", "export-jsonl"):
        query_parser = subparsers.add_parser(name)
        _add_query_arguments(query_parser)
    return parser


def _query_from_args(args: argparse.Namespace) -> ReferenceQuery:
    return ReferenceQuery(
        pilot_clip_ids=tuple(args.pilot_clip_id),
        content_families=tuple(args.content_family),
        content_scopes=tuple(args.content_scope),
        reference_duties=tuple(args.reference_duty),
        technical_validation_statuses=tuple(args.technical_status),
        artifact_availabilities=tuple(args.artifact_availability),
        artifact_lifecycles=tuple(args.artifact_lifecycle),
        taxonomy_statuses=tuple(args.taxonomy_status),
        sort_by=args.sort_by,
        descending=args.descending,
    )


def run(arguments: Sequence[str]) -> str:
    _reject_forbidden_options(arguments)
    args = build_parser().parse_args(list(arguments))
    catalog = ReferenceCatalog.from_package(args.package)
    if args.command == "validate":
        return deterministic_json(catalog.validation.to_dict())
    if args.command == "summary":
        return deterministic_json(catalog.summary())
    if args.command == "show":
        return deterministic_json(catalog.get(args.identifier).to_dict())

    records = catalog.query(_query_from_args(args))
    if args.command == "export-jsonl":
        return records_to_jsonl(records)
    return records_to_json(records)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = tuple(sys.argv[1:] if argv is None else argv)
    try:
        output = run(arguments)
    except (
        CandidatePackageError,
        CatalogLookupError,
        CatalogValidationError,
        RecordLoadError,
        ValueError,
    ) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(output)
    return 0
