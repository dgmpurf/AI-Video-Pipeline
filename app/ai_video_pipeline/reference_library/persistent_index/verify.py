from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .enums import (
    BUILDER_CONTRACT_VERSION,
    LOGICAL_HASH_REGISTRY_VERSION,
    READ_MODEL_SCHEMA_VERSION,
    TOKENIZER_CONTRACT_VERSION,
    GenerationState,
)
from .errors import IdentityError, SchemaError, VerificationError
from .identity import (
    POINTER_FIELDS,
    canonical_json_bytes,
    logical_content_hash,
    parse_generation_filename,
    validate_pointer,
)
from .schema import validate_fts_parity


@dataclass(frozen=True)
class VerificationResult:
    state: GenerationState
    logical_content_hash: str | None
    stored_logical_content_hash: str | None
    metadata: Mapping[str, Any]
    diagnostics: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return self.state == GenerationState.VALID_CURRENT_GENERATION


def open_read_only(path: str | Path) -> sqlite3.Connection:
    resolved = Path(path).resolve(strict=True)
    connection = sqlite3.connect(resolved.as_uri() + "?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def _metadata(connection: sqlite3.Connection) -> dict[str, Any]:
    rows = connection.execute("SELECT * FROM read_model_meta").fetchall()
    if len(rows) != 1:
        raise VerificationError("read_model_meta must contain exactly one row")
    return dict(rows[0])


def _pointer_mapping(pointer: Mapping[str, Any] | str | Path | None) -> Mapping[str, Any] | None:
    if pointer is None:
        return None
    if isinstance(pointer, Mapping):
        value = dict(pointer)
    else:
        pointer_path = Path(pointer)
        if pointer_path.is_symlink() or not pointer_path.is_file():
            raise IdentityError("pointer is absent, non-regular, or a symlink")
        raw = pointer_path.read_bytes()
        if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
            raise IdentityError("pointer must contain exactly one terminal LF")
        value = json.loads(raw.decode("utf-8"))
    validate_pointer(value)
    if not isinstance(pointer, Mapping) and raw != canonical_json_bytes(value, terminal_lf=True):
        raise IdentityError("pointer is not canonical JSON")
    return value


def verify_generation(
    path: str | Path,
    *,
    pointer: Mapping[str, Any] | str | Path | None = None,
    expected_upstream: Mapping[str, Any] | None = None,
    require_final_filename: bool = True,
) -> VerificationResult:
    diagnostics: list[str] = []
    metadata: dict[str, Any] = {}
    computed: str | None = None
    stored: str | None = None
    try:
        with open_read_only(path) as connection:
            integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
            if integrity != "ok":
                raise VerificationError(f"SQLite integrity_check failed: {integrity}")
            foreign = connection.execute("PRAGMA foreign_key_check").fetchall()
            if foreign:
                raise VerificationError("foreign-key validation failed")
            metadata = _metadata(connection)
            if metadata["read_model_schema_version"] != READ_MODEL_SCHEMA_VERSION:
                return VerificationResult(
                    GenerationState.INCOMPATIBLE_GENERATION, None,
                    metadata.get("logical_content_hash"), metadata,
                    ("unsupported read-model schema",),
                )
            if metadata["logical_hash_registry_version"] != LOGICAL_HASH_REGISTRY_VERSION:
                return VerificationResult(
                    GenerationState.INCOMPATIBLE_GENERATION, None,
                    metadata.get("logical_content_hash"), metadata,
                    ("unsupported logical-hash registry",),
                )
            if metadata["builder_contract_version"] != BUILDER_CONTRACT_VERSION:
                return VerificationResult(
                    GenerationState.INCOMPATIBLE_GENERATION, None,
                    metadata.get("logical_content_hash"), metadata,
                    ("unsupported builder contract",),
                )
            if metadata["tokenizer_contract_version"] != TOKENIZER_CONTRACT_VERSION:
                return VerificationResult(
                    GenerationState.INCOMPATIBLE_GENERATION, None,
                    metadata.get("logical_content_hash"), metadata,
                    ("unsupported tokenizer contract",),
                )
            stored = metadata.get("logical_content_hash")
            try:
                computed = logical_content_hash(connection)
            except SchemaError as error:
                diagnostics.append(str(error))
                return VerificationResult(
                    GenerationState.INCOMPATIBLE_GENERATION,
                    computed,
                    stored,
                    metadata,
                    tuple(diagnostics),
                )
            if stored != computed:
                raise VerificationError("stored and recomputed logical hashes differ")
            try:
                validate_fts_parity(connection)
            except SchemaError as error:
                diagnostics.append(str(error))
                return VerificationResult(
                    GenerationState.CORRUPT_OR_TAMPERED_GENERATION,
                    computed,
                    stored,
                    metadata,
                    tuple(diagnostics),
                )
        if require_final_filename:
            parsed = parse_generation_filename(path)
            if parsed["schema"] != READ_MODEL_SCHEMA_VERSION:
                raise VerificationError("generation filename schema differs")
            if parsed["generation"] != metadata["materialization_generation_id"]:
                raise VerificationError("generation filename ID differs")
            if parsed["logical"] != computed:
                raise VerificationError("generation filename hash differs")
        pointer_value = _pointer_mapping(pointer)
        if pointer_value is not None:
            if pointer_value["generation_filename"] != Path(path).name:
                raise VerificationError("pointer names another generation")
            for field in POINTER_FIELDS - {"pointer_schema_version", "generation_filename"}:
                if pointer_value[field] != metadata[field]:
                    raise VerificationError(f"pointer metadata differs: {field}")
        state = GenerationState.VALID_CURRENT_GENERATION
        if expected_upstream is not None:
            absent = set(expected_upstream) - set(metadata)
            if absent:
                return VerificationResult(
                    GenerationState.INCOMPATIBLE_GENERATION,
                    computed,
                    stored,
                    metadata,
                    (f"expected upstream fields are absent: {sorted(absent)}",),
                )
            mismatched = {
                key for key, value in expected_upstream.items()
                if metadata[key] != value
            }
            if mismatched:
                stable_fields = mismatched - {"through_position", "through_entry_hash", "projection_hash", "checkpoint_id"}
                expected_position = expected_upstream.get("through_position")
                if (
                    not stable_fields
                    and isinstance(expected_position, int)
                    and expected_position > int(metadata["through_position"])
                ):
                    state = GenerationState.STALE_GENERATION
                    diagnostics.append("internally valid generation trails the requested ledger tail")
                else:
                    state = GenerationState.INCOMPATIBLE_GENERATION
                    diagnostics.append("upstream identity is incompatible")
        return VerificationResult(state, computed, stored, metadata, tuple(diagnostics))
    except (OSError, sqlite3.Error, IdentityError, VerificationError) as error:
        diagnostics.append(str(error))
        return VerificationResult(
            GenerationState.CORRUPT_OR_TAMPERED_GENERATION,
            computed,
            stored,
            metadata,
            tuple(diagnostics),
        )


def require_valid_generation(
    path: str | Path,
    *,
    pointer: Mapping[str, Any] | str | Path | None = None,
    expected_upstream: Mapping[str, Any] | None = None,
) -> VerificationResult:
    result = verify_generation(path, pointer=pointer, expected_upstream=expected_upstream)
    if not result.valid:
        raise VerificationError(f"generation is not current and valid: {result.state.value}")
    return result
