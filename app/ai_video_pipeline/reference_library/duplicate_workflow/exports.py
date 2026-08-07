from __future__ import annotations

from typing import Any, Iterable, Mapping

from .canonical import canonical_json_bytes, sha256_hex


EXPORT_CONTRACT_VERSION = "RL_P3_AUTHORITY_PRESERVING_EXPORT_V0_1"


def export_json(document: Mapping[str, Any]) -> bytes:
    return canonical_json_bytes(
        {
            "export_contract_version": EXPORT_CONTRACT_VERSION,
            "document": dict(document),
        },
        terminal_lf=True,
    )


def export_rows_jsonl(
    rows: Iterable[Mapping[str, Any]],
    *,
    generation: Mapping[str, Any],
    query_kind: str,
) -> bytes:
    lines: list[bytes] = []
    for ordinal, row in enumerate(rows, start=1):
        lines.append(
            canonical_json_bytes(
                {
                    "export_contract_version": EXPORT_CONTRACT_VERSION,
                    "generation": dict(generation),
                    "query_kind": query_kind,
                    "row_ordinal": ordinal,
                    "row": dict(row),
                },
                terminal_lf=True,
            )
        )
    return b"".join(lines)


def export_manifest(payload: bytes, *, format_name: str, row_count: int) -> dict[str, Any]:
    if format_name not in {"JSON", "JSONL"}:
        raise ValueError("format_name must be JSON or JSONL")
    return {
        "export_contract_version": EXPORT_CONTRACT_VERSION,
        "format": format_name,
        "authority_fields_preserved": True,
        "source_trace_fields_preserved": True,
        "row_count": row_count,
        "bytes": len(payload),
        "sha256": sha256_hex(payload),
    }
