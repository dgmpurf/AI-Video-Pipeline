from __future__ import annotations

from typing import Any, Iterable, Mapping

from .identity import canonical_json_bytes, sha256_hex
from .query import QUERY_CONTRACT_VERSION, QueryPage


EXPORT_CONTRACT_VERSION = "RL_P2_DETERMINISTIC_EXPORT_V0_1R1"


def export_page_json(page: QueryPage) -> bytes:
    """Return one canonical UTF-8 JSON response with exactly one terminal LF."""

    return canonical_json_bytes(page.to_dict(), terminal_lf=True)


def export_rows_jsonl(page: QueryPage) -> bytes:
    """Return deterministic provenance-bearing JSONL rows in query order."""

    lines: list[bytes] = []
    for ordinal, row in enumerate(page.rows, start=1):
        lines.append(
            canonical_json_bytes(
                {
                    "export_contract_version": EXPORT_CONTRACT_VERSION,
                    "query_contract_version": QUERY_CONTRACT_VERSION,
                    "request_hash": page.request_hash,
                    "generation": dict(page.generation),
                    "row_ordinal": ordinal,
                    "row": dict(row),
                },
                terminal_lf=True,
            )
        )
    return b"".join(lines)


def export_stream_jsonl(
    rows: Iterable[Mapping[str, Any]],
    *,
    request_hash: str,
    generation: Mapping[str, Any],
) -> bytes:
    """Serialize an already pinned, fully ordered result stream."""

    lines: list[bytes] = []
    for ordinal, row in enumerate(rows, start=1):
        lines.append(
            canonical_json_bytes(
                {
                    "export_contract_version": EXPORT_CONTRACT_VERSION,
                    "query_contract_version": QUERY_CONTRACT_VERSION,
                    "request_hash": request_hash,
                    "generation": dict(generation),
                    "row_ordinal": ordinal,
                    "row": dict(row),
                },
                terminal_lf=True,
            )
        )
    return b"".join(lines)


def export_manifest(
    payload: bytes,
    *,
    format_name: str,
    page: QueryPage,
) -> dict[str, Any]:
    if format_name not in {"JSON", "JSONL"}:
        raise ValueError("format_name must be JSON or JSONL")
    return {
        "export_contract_version": EXPORT_CONTRACT_VERSION,
        "format": format_name,
        "query_contract_version": QUERY_CONTRACT_VERSION,
        "request_hash": page.request_hash,
        "generation": dict(page.generation),
        "sort_contract": page.request.get("sort_by"),
        "row_count": len(page.rows),
        "bytes": len(payload),
        "sha256": sha256_hex(payload),
    }
