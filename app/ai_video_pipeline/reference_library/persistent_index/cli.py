from __future__ import annotations

import argparse
import sys
from typing import Any

from app.ai_video_pipeline.reference_library.event_ledger import (
    load_base_catalog,
    load_validated_ledger,
    replay_entries,
)

from .builder import build_generation
from .enums import SearchScope
from .exports import export_page_json, export_rows_jsonl
from .identity import canonical_json_bytes
from .mapper import map_projection
from .promotion import promote_generation
from .query import FacetQuery, ReadModel, SearchQuery
from .verify import verify_generation


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m app.ai_video_pipeline.reference_library.persistent_index"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    build = commands.add_parser("build", help="build one immutable generation")
    build.add_argument("--base-package", required=True)
    build.add_argument("--ledger-root", required=True)
    build.add_argument("--state-root", required=True)
    build.add_argument("--builder-source-identity", required=True)
    build.add_argument("--forbidden-root", action="append", default=[])

    verify = commands.add_parser("verify", help="verify one exact generation")
    verify.add_argument("--database", required=True)
    verify.add_argument("--pointer")

    promote = commands.add_parser("promote", help="atomically promote one verified generation")
    promote.add_argument("--database", required=True)

    facet = commands.add_parser("facet", help="run a deterministic exact/faceted query")
    _reader_arguments(facet)
    _facet_arguments(facet)

    search = commands.add_parser("search", help="run a bounded plain-text FTS query")
    _reader_arguments(search)
    _search_arguments(search, include_common=True)

    export = commands.add_parser("export", help="emit canonical query JSON or JSONL")
    _reader_arguments(export)
    export.add_argument("--mode", required=True, choices=("facet", "search"))
    export.add_argument("--format", required=True, choices=("json", "jsonl"))
    _facet_arguments(export)
    _search_arguments(export, text_required=False, include_common=False)
    return parser


def _reader_arguments(parser: argparse.ArgumentParser) -> None:
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--state-root")
    source.add_argument("--database")
    parser.add_argument("--pointer")


def _facet_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--pilot-clip-id", action="append", default=[])
    parser.add_argument("--content-family", action="append", default=[])
    parser.add_argument("--content-scope", action="append", default=[])
    parser.add_argument("--reference-duty", action="append", default=[])
    parser.add_argument("--technical-status", action="append", default=[])
    parser.add_argument("--artifact-availability", action="append", default=[])
    parser.add_argument("--artifact-lifecycle", action="append", default=[])
    parser.add_argument("--taxonomy-status", action="append", default=[])
    parser.add_argument("--rights-provenance", action="append", default=[])
    parser.add_argument("--generation-input-allowed", choices=("true", "false"))
    parser.add_argument("--publication-allowed", choices=("TRUE", "FALSE", "UNKNOWN"))
    parser.add_argument(
        "--sort-by",
        choices=(
            "pilot_clip_id", "record_id", "primary_family", "content_scope",
            "current_total_bytes",
        ),
        default="pilot_clip_id",
    )
    parser.add_argument("--descending", action="store_true")
    parser.add_argument("--page-size", type=int, default=50)
    parser.add_argument("--cursor")


def _search_arguments(
    parser: argparse.ArgumentParser,
    *,
    text_required: bool = True,
    include_common: bool,
) -> None:
    parser.add_argument("--text", required=text_required)
    parser.add_argument("--scope", choices=("CURRENT", "HISTORY"), default="CURRENT")
    parser.add_argument("--authority-class", action="append", default=[])
    if include_common:
        parser.add_argument("--pilot-clip-id", action="append", default=[])
        parser.add_argument("--rights-provenance", action="append", default=[])
        parser.add_argument("--generation-input-allowed", choices=("true", "false"))
        parser.add_argument("--publication-allowed", choices=("TRUE", "FALSE", "UNKNOWN"))
        parser.add_argument("--page-size", type=int, default=50)
        parser.add_argument("--cursor")


def _as_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    return value == "true"


def _facet_request(arguments: argparse.Namespace) -> FacetQuery:
    return FacetQuery(
        pilot_clip_ids=tuple(arguments.pilot_clip_id),
        content_families=tuple(arguments.content_family),
        content_scopes=tuple(arguments.content_scope),
        reference_duties=tuple(arguments.reference_duty),
        technical_statuses=tuple(arguments.technical_status),
        artifact_availabilities=tuple(arguments.artifact_availability),
        artifact_lifecycles=tuple(arguments.artifact_lifecycle),
        taxonomy_statuses=tuple(arguments.taxonomy_status),
        rights_provenances=tuple(arguments.rights_provenance),
        generation_input_allowed=_as_bool(arguments.generation_input_allowed),
        publication_allowed=arguments.publication_allowed,
        sort_by=arguments.sort_by,
        descending=arguments.descending,
        page_size=arguments.page_size,
        cursor=arguments.cursor,
    )


def _search_request(arguments: argparse.Namespace) -> SearchQuery:
    if arguments.text is None:
        raise ValueError("--text is required when --mode=search")
    return SearchQuery(
        text=arguments.text,
        scope=SearchScope(arguments.scope),
        pilot_clip_ids=tuple(arguments.pilot_clip_id),
        authority_classes=tuple(arguments.authority_class),
        rights_provenances=tuple(arguments.rights_provenance),
        generation_input_allowed=_as_bool(arguments.generation_input_allowed),
        publication_allowed=arguments.publication_allowed,
        page_size=arguments.page_size,
        cursor=arguments.cursor,
    )


def _open_reader(arguments: argparse.Namespace) -> ReadModel:
    if arguments.state_root:
        if arguments.pointer is not None:
            raise ValueError("--pointer cannot be combined with --state-root")
        return ReadModel.open_current(arguments.state_root)
    return ReadModel.open_generation(arguments.database, pointer=arguments.pointer)


def _write_json(value: Any) -> None:
    sys.stdout.buffer.write(canonical_json_bytes(value, terminal_lf=True))


def main(argv: list[str] | None = None) -> int:
    arguments = _parser().parse_args(argv)
    if arguments.command == "build":
        adapter = load_base_catalog(arguments.base_package)
        manifest, entries = load_validated_ledger(arguments.ledger_root, adapter)
        projection = replay_entries(manifest, adapter, entries)
        mapped = map_projection(
            adapter,
            manifest,
            entries,
            projection,
            builder_source_identity=arguments.builder_source_identity,
        )
        result = build_generation(
            arguments.state_root,
            mapped,
            forbidden_roots=arguments.forbidden_root,
        )
        _write_json(
            {
                "generation_path": str(result.generation_path),
                "logical_content_hash": result.logical_content_hash,
                "materialization_generation_id": result.materialization_generation_id,
                "verification_state": result.verification.state.value,
            }
        )
        return 0
    if arguments.command == "verify":
        result = verify_generation(arguments.database, pointer=arguments.pointer)
        _write_json(
            {
                "state": result.state.value,
                "logical_content_hash": result.logical_content_hash,
                "stored_logical_content_hash": result.stored_logical_content_hash,
                "metadata": dict(result.metadata),
                "diagnostics": list(result.diagnostics),
            }
        )
        return 0 if result.valid else 2
    if arguments.command == "promote":
        _write_json(dict(promote_generation(arguments.database)))
        return 0
    with _open_reader(arguments) as reader:
        if arguments.command == "facet":
            page = reader.facet(_facet_request(arguments))
            sys.stdout.buffer.write(export_page_json(page))
            return 0
        if arguments.command == "search":
            page = reader.search(_search_request(arguments))
            sys.stdout.buffer.write(export_page_json(page))
            return 0
        request = (
            _facet_request(arguments)
            if arguments.mode == "facet"
            else _search_request(arguments)
        )
        page = reader.facet(request) if isinstance(request, FacetQuery) else reader.search(request)
        payload = export_page_json(page) if arguments.format == "json" else export_rows_jsonl(page)
        sys.stdout.buffer.write(payload)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
