from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .enums import GenerationState
from .errors import MappingError


@dataclass(frozen=True)
class MappedReadModel:
    rows: Mapping[str, tuple[tuple[Any, ...], ...]]
    materialization_generation_id: str
    upstream_identity: Mapping[str, Any]

    def table(self, name: str) -> tuple[tuple[Any, ...], ...]:
        try:
            return self.rows[name]
        except KeyError as error:
            raise MappingError(f"unknown mapped table: {name}") from error


@dataclass(frozen=True)
class RuntimeStateProtectionPolicy:
    repository_root: str | Path
    source_root: str | Path
    media_roots: tuple[str | Path, ...]


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


@dataclass(frozen=True)
class BuildResult:
    generation_path: Path
    logical_content_hash: str
    materialization_generation_id: str
    verification: VerificationResult
