from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from .models import ReferenceRecord, json_clone
from .query import ReferenceQuery, apply_query, summarize_records
from .record_loader import load_reference_records
from .schema_loader import CandidatePackageData, load_candidate_package
from .validator import CatalogValidationSummary, validate_catalog


class CatalogLookupError(KeyError):
    pass


@dataclass(frozen=True)
class ReferenceCatalog:
    """Validated, immutable, in-memory view of the candidate ZIP."""

    package_path: Path
    _records: tuple[ReferenceRecord, ...]
    _by_identifier: Mapping[str, ReferenceRecord]
    _schema: dict[str, Any]
    _vocabularies: dict[str, Any]
    validation: CatalogValidationSummary

    @classmethod
    def from_package(cls, path: str | Path) -> "ReferenceCatalog":
        package = load_candidate_package(path)
        return cls.from_loaded_package(package)

    @classmethod
    def from_loaded_package(
        cls, package: CandidatePackageData
    ) -> "ReferenceCatalog":
        records = load_reference_records(package)
        validation = validate_catalog(package, records)
        by_identifier: dict[str, ReferenceRecord] = {}
        for record in records:
            by_identifier[record.pilot_clip_id] = record
            by_identifier[record.record_id] = record
        return cls(
            package_path=package.path,
            _records=records,
            _by_identifier=MappingProxyType(by_identifier),
            _schema=package.schema,
            _vocabularies=package.vocabularies,
            validation=validation,
        )

    @property
    def records(self) -> tuple[ReferenceRecord, ...]:
        return self._records

    @property
    def schema(self) -> dict[str, Any]:
        return json_clone(self._schema)

    @property
    def vocabularies(self) -> dict[str, Any]:
        return json_clone(self._vocabularies)

    def get(self, identifier: str) -> ReferenceRecord:
        try:
            return self._by_identifier[identifier]
        except KeyError as error:
            raise CatalogLookupError(f"unknown reference record: {identifier}") from error

    def query(self, query: ReferenceQuery | None = None) -> tuple[ReferenceRecord, ...]:
        return apply_query(self._records, query or ReferenceQuery())

    def summary(self) -> dict[str, Any]:
        result = summarize_records(self._records)
        result["validation"] = self.validation.to_dict()
        return result
