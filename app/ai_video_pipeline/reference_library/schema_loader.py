from __future__ import annotations

import hashlib
import io
import json
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


PACKAGE_FILENAME = (
    "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_"
    "CANDIDATE_V0_1.zip"
)
PACKAGE_BYTES = 99_429
PACKAGE_SHA256 = (
    "83bb0a7597bf4a8700f956e9da5b5249ec9bbc8d1b6ed909c8c0d69b601df622"
)
PACKAGE_MEMBER_COUNT = 44
PACKAGE_ROOT = (
    "REFERENCE_LIBRARY_PILOT_V0_1_SCHEMA_NORMALIZATION_PATCH_"
    "CANDIDATE_V0_1"
)

RECORD_RELATIVE_NAMES = tuple(
    f"03_records/G01D-CLIP-{number:03}.json" for number in range(1, 31)
)
EXPECTED_RELATIVE_MEMBERS = (
    "00_control/README.md",
    "00_control/manifest.json",
    "00_control/package_summary.json",
    "01_schema/canonical_record.schema.json",
    "02_vocabularies/controlled_vocabularies.json",
    *RECORD_RELATIVE_NAMES,
    "04_validation/independent_validation_report.json",
    "04_validation/validate_package.py",
    "04_validation/validation_contract.json",
    "04_validation/validation_report.json",
    "05_audit/PATCH_CANDIDATE_CHECKPOINT.md",
    "05_audit/materialization_audit.json",
    "06_synthesis/REFERENCE_LIBRARY_PILOT_V0_1_RESULTS_SYNTHESIS.md",
    "07_source_boundary/PROJECT_SOURCE_UPDATE_EVIDENCE_REQUIREMENTS.md",
    "SHA256SUMS",
)


class CandidatePackageError(ValueError):
    pass


@dataclass(frozen=True)
class CandidatePackageData:
    path: Path
    member_names: tuple[str, ...]
    _schema_json: str
    _vocabularies_json: str
    _record_jsons: tuple[str, ...]
    _validation_contract_json: str
    _validation_report_json: str

    @property
    def schema(self) -> dict[str, Any]:
        return json.loads(self._schema_json)

    @property
    def vocabularies(self) -> dict[str, Any]:
        return json.loads(self._vocabularies_json)

    @property
    def raw_records(self) -> tuple[dict[str, Any], ...]:
        return tuple(json.loads(value) for value in self._record_jsons)

    @property
    def validation_contract(self) -> dict[str, Any]:
        return json.loads(self._validation_contract_json)

    @property
    def validation_report(self) -> dict[str, Any]:
        return json.loads(self._validation_report_json)


def _full_name(relative_name: str) -> str:
    return f"{PACKAGE_ROOT}/{relative_name}"


def _parse_json_object(data: bytes, name: str) -> dict[str, Any]:
    try:
        value = json.loads(data.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CandidatePackageError(f"invalid JSON member: {name}") from error
    if not isinstance(value, dict):
        raise CandidatePackageError(f"JSON member must be an object: {name}")
    return value


def _validate_member_paths(names: tuple[str, ...]) -> None:
    if len(names) != len(set(names)):
        raise CandidatePackageError("duplicate ZIP member name")
    for name in names:
        pure = PurePosixPath(name)
        if pure.is_absolute() or ".." in pure.parts or "\\" in name:
            raise CandidatePackageError(f"unsafe ZIP member: {name}")
        if name.endswith("/"):
            raise CandidatePackageError(f"directory member is not allowed: {name}")


def _validate_sha256sums(member_bytes: dict[str, bytes]) -> None:
    sums_name = _full_name("SHA256SUMS")
    try:
        lines = member_bytes[sums_name].decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as error:
        raise CandidatePackageError("SHA256SUMS is not valid UTF-8") from error
    expected_relative = EXPECTED_RELATIVE_MEMBERS[:-1]
    if len(lines) != len(expected_relative):
        raise CandidatePackageError("SHA256SUMS coverage is not 43/43")
    listed: list[str] = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None:
            raise CandidatePackageError("malformed SHA256SUMS line")
        expected_hash, relative_name = match.groups()
        listed.append(relative_name)
        full_name = _full_name(relative_name)
        if full_name not in member_bytes:
            raise CandidatePackageError(f"SHA256SUMS member missing: {relative_name}")
        observed_hash = hashlib.sha256(member_bytes[full_name]).hexdigest()
        if observed_hash != expected_hash:
            raise CandidatePackageError(f"SHA256SUMS mismatch: {relative_name}")
    if tuple(listed) != expected_relative:
        raise CandidatePackageError("SHA256SUMS member order mismatch")


def load_candidate_package(path: str | Path) -> CandidatePackageData:
    package_path = Path(path)
    if package_path.name != PACKAGE_FILENAME:
        raise CandidatePackageError("candidate ZIP filename mismatch")
    if not package_path.is_file():
        raise CandidatePackageError("candidate ZIP is not a regular file")
    raw = package_path.read_bytes()
    if len(raw) != PACKAGE_BYTES:
        raise CandidatePackageError("candidate ZIP byte length mismatch")
    if hashlib.sha256(raw).hexdigest() != PACKAGE_SHA256:
        raise CandidatePackageError("candidate ZIP SHA-256 mismatch")

    try:
        with zipfile.ZipFile(io.BytesIO(raw), "r") as archive:
            infos = archive.infolist()
            names = tuple(info.filename for info in infos)
            if len(names) != PACKAGE_MEMBER_COUNT:
                raise CandidatePackageError("candidate ZIP member count mismatch")
            _validate_member_paths(names)
            expected_names = tuple(_full_name(name) for name in EXPECTED_RELATIVE_MEMBERS)
            if names != expected_names:
                raise CandidatePackageError("candidate ZIP member inventory mismatch")
            if archive.testzip() is not None:
                raise CandidatePackageError("candidate ZIP CRC validation failed")
            member_bytes = {name: archive.read(name) for name in names}
    except (OSError, zipfile.BadZipFile) as error:
        raise CandidatePackageError("candidate ZIP cannot be read") from error

    _validate_sha256sums(member_bytes)
    json_names = tuple(name for name in names if name.endswith(".json"))
    if len(json_names) != 38:
        raise CandidatePackageError("candidate ZIP JSON count mismatch")
    parsed_json = {name: _parse_json_object(member_bytes[name], name) for name in json_names}

    record_jsons = tuple(
        member_bytes[_full_name(relative)].decode("utf-8", errors="strict")
        for relative in RECORD_RELATIVE_NAMES
    )
    return CandidatePackageData(
        path=package_path,
        member_names=names,
        _schema_json=json.dumps(
            parsed_json[_full_name("01_schema/canonical_record.schema.json")],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ),
        _vocabularies_json=json.dumps(
            parsed_json[_full_name("02_vocabularies/controlled_vocabularies.json")],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ),
        _record_jsons=record_jsons,
        _validation_contract_json=json.dumps(
            parsed_json[_full_name("04_validation/validation_contract.json")],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ),
        _validation_report_json=json.dumps(
            parsed_json[_full_name("04_validation/validation_report.json")],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ),
    )
