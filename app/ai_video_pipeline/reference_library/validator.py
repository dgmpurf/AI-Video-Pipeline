from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping

from .models import ReferenceRecord, UNKNOWN
from .record_loader import EXPECTED_PILOT_CLIP_IDS
from .schema_loader import CandidatePackageData


EXPECTED_RIGHTS = {
    "rights_provenance": "purchased_unverified_license",
    "active_generation_input_allowed": False,
    "publication_allowed": UNKNOWN,
}
LEGACY_SCORE_FIELDS = (
    "numeric_confidence",
    "action_value",
    "camera_value",
    "vfx_value",
    "performance_value",
    "reuse_probability",
    "rarity",
    "irreplaceability",
    "production_relevance",
    "descriptive_total_score",
)
FIXED_INVARIANTS = {
    "record_count": 30,
    "unique_id_count": 30,
    "technical_failure_count": 14,
    "current_proxy_file_count": 57,
    "current_proxy_bytes": 267_538_642,
    "retained_segment_count": 4,
    "retained_segment_bytes": 31_831_333,
    "current_total_derived_media_bytes": 299_369_975,
    "clip005_historical_deleted_bytes": 1_702_329_164,
    "legacy_unknown_slots": 198,
    "unknown_to_zero": 0,
    "narrative_reference_extension_count": 1,
    "taxonomy_decision_required_count": 1,
}


class CatalogValidationError(ValueError):
    pass


@dataclass(frozen=True)
class CatalogValidationSummary:
    record_count: int
    unique_id_count: int
    technical_failure_count: int
    current_proxy_file_count: int
    current_proxy_bytes: int
    retained_segment_count: int
    retained_segment_bytes: int
    current_total_derived_media_bytes: int
    clip005_historical_deleted_bytes: int
    legacy_unknown_slots: int
    unknown_to_zero: int
    narrative_reference_extension_count: int
    taxonomy_decision_required_count: int
    validation_status: str = "PASS"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _require_mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CatalogValidationError(f"{path} must be an object")
    return value


def _require_list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise CatalogValidationError(f"{path} must be an array")
    return value


def _require_keys(value: Mapping[str, Any], keys: Iterable[str], path: str) -> None:
    missing = tuple(key for key in keys if key not in value)
    if missing:
        raise CatalogValidationError(
            f"{path} missing required fields: {', '.join(missing)}"
        )


def _require_nonnegative_int(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise CatalogValidationError(f"{path} must be a nonnegative integer")
    return value


def _require_vocab(value: Any, allowed: set[str], path: str) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise CatalogValidationError(f"{path} is outside the controlled vocabulary")
    return value


def _validate_storage_arithmetic(
    clip_id: str,
    raw: Mapping[str, Any],
    artifacts: list[Any],
) -> tuple[int, int, int, int, int]:
    storage = _require_mapping(raw["artifact_storage"], f"{clip_id}.artifact_storage")
    _require_keys(
        storage,
        (
            "current_proxy_file_count",
            "current_proxy_bytes",
            "current_segment_count",
            "current_segment_bytes",
            "current_total_derived_media_bytes",
            "historical_deleted_bytes",
            "arithmetic_status",
        ),
        f"{clip_id}.artifact_storage",
    )

    present_proxies = [
        artifact
        for artifact in artifacts
        if artifact["artifact_type"] == "PROXY"
        and artifact["artifact_availability"] == "PRESENT"
    ]
    present_segments = [
        artifact
        for artifact in artifacts
        if artifact["artifact_type"] == "TARGETED_SEGMENT"
        and artifact["artifact_availability"] == "PRESENT"
    ]
    deleted_artifacts = [
        artifact
        for artifact in artifacts
        if artifact["artifact_lifecycle"] == "DELETED"
    ]

    proxy_count = len(present_proxies)
    proxy_bytes = sum(int(artifact["artifact_bytes"]) for artifact in present_proxies)
    segment_count = len(present_segments)
    segment_bytes = sum(
        int(artifact["artifact_bytes"]) for artifact in present_segments
    )
    deleted_bytes = sum(
        int(artifact["artifact_bytes"]) for artifact in deleted_artifacts
    )
    expected = {
        "current_proxy_file_count": proxy_count,
        "current_proxy_bytes": proxy_bytes,
        "current_segment_count": segment_count,
        "current_segment_bytes": segment_bytes,
        "current_total_derived_media_bytes": proxy_bytes + segment_bytes,
        "historical_deleted_bytes": deleted_bytes,
    }
    for field, value in expected.items():
        observed = _require_nonnegative_int(
            storage[field], f"{clip_id}.artifact_storage.{field}"
        )
        if observed != value:
            raise CatalogValidationError(
                f"{clip_id}.artifact_storage.{field} arithmetic mismatch"
            )
    if storage["arithmetic_status"] != "PASS":
        raise CatalogValidationError(f"{clip_id} storage arithmetic is not PASS")
    return proxy_count, proxy_bytes, segment_count, segment_bytes, deleted_bytes


def _validate_contract_surfaces(package: CandidatePackageData) -> None:
    contract = package.validation_contract
    report = package.validation_report
    contract_expected = {
        "patch_target_scope_exactly": 30,
        "unique_ids": 30,
        "technical_failures_exact": 14,
        "current_proxy_file_count": 57,
        "current_proxy_bytes": 267_538_642,
        "retained_segment_count": 4,
        "retained_segment_bytes": 31_831_333,
        "current_total_derived_media_bytes": 299_369_975,
        "CLIP005_deleted_bytes": 1_702_329_164,
        "legacy_unknown_slots": 198,
        "UNKNOWN_to_zero": 0,
        "semantic_change_count": 0,
        "score_change_count": 0,
        "media_operation_count": 0,
        "all_30_pass_required": True,
    }
    for field, expected in contract_expected.items():
        if contract.get(field) != expected:
            raise CatalogValidationError(f"validation contract mismatch: {field}")
    if contract.get("rights") != EXPECTED_RIGHTS:
        raise CatalogValidationError("validation contract rights mismatch")
    if contract.get("narrative_reference") != {
        "location": "reference_duty_extensions",
        "status": "TAXONOMY_DECISION_REQUIRED",
    }:
        raise CatalogValidationError("narrative_reference contract mismatch")

    report_expected = {
        "status": "ALL_30_PASS",
        "record_count": 30,
        "unique_id_count": 30,
        "technical_failure_count": 14,
        "current_proxy_file_count": 57,
        "current_proxy_bytes": 267_538_642,
        "retained_segment_count": 4,
        "retained_segment_bytes": 31_831_333,
        "current_total_derived_media_bytes": 299_369_975,
        "CLIP005_deleted_bytes": 1_702_329_164,
        "legacy_unknown_slots": 198,
        "UNKNOWN_to_zero": 0,
        "semantic_change_count": 0,
        "score_change_count": 0,
        "rights_change_count": 0,
        "media_operation_count": 0,
        "errors": [],
    }
    for field, expected in report_expected.items():
        if report.get(field) != expected:
            raise CatalogValidationError(f"validation report mismatch: {field}")
    if report.get("rights") != EXPECTED_RIGHTS:
        raise CatalogValidationError("validation report rights mismatch")


def validate_catalog(
    package: CandidatePackageData,
    records: tuple[ReferenceRecord, ...],
) -> CatalogValidationSummary:
    _validate_contract_surfaces(package)
    schema = package.schema
    vocabularies = package.vocabularies
    required_root = tuple(schema.get("required", ()))
    if len(required_root) != 16:
        raise CatalogValidationError("canonical schema root field count mismatch")
    if len(records) != 30:
        raise CatalogValidationError("catalog record count must be exactly 30")

    primary_vocab = set(vocabularies["content_family_primary"])
    scope_vocab = set(vocabularies["content_scope"])
    duty_vocab = set(vocabularies["reference_duties"])
    extension_vocab = dict(vocabularies["reference_duty_extensions"])
    technical_vocab = set(vocabularies["technical_validation_status"])
    availability_vocab = set(vocabularies["artifact_availability"])
    lifecycle_vocab = set(vocabularies["artifact_lifecycle"])
    proposal_vocab = set(vocabularies["storage_proposal_action"])
    duplicate_vocab = set(vocabularies["exact_duplicate_status"])
    retained_role_vocab = set(vocabularies["retained_artifact_roles"])

    seen_record_ids: set[str] = set()
    seen_clip_ids: set[str] = set()
    technical_failures = 0
    proxy_count = 0
    proxy_bytes = 0
    segment_count = 0
    segment_bytes = 0
    clip005_deleted_bytes = 0
    legacy_unknown_slots = 0
    unknown_to_zero = 0
    narrative_extension_count = 0
    taxonomy_decision_count = 0

    for expected_clip_id, record in zip(EXPECTED_PILOT_CLIP_IDS, records):
        raw = record.to_dict()
        _require_keys(raw, required_root, expected_clip_id)
        identity = _require_mapping(raw["record_identity"], "record_identity")
        clip_id = identity.get("pilot_clip_id")
        record_id = identity.get("record_id")
        if clip_id != expected_clip_id:
            raise CatalogValidationError("record order or pilot_clip_id mismatch")
        if not isinstance(record_id, str) or not record_id:
            raise CatalogValidationError(f"{clip_id}.record_id is invalid")
        if clip_id in seen_clip_ids or record_id in seen_record_ids:
            raise CatalogValidationError("duplicate record identity")
        seen_clip_ids.add(clip_id)
        seen_record_ids.add(record_id)

        content = _require_mapping(raw["content"], f"{clip_id}.content")
        family = _require_mapping(
            content.get("content_family"), f"{clip_id}.content.content_family"
        )
        _require_vocab(
            family.get("primary"), primary_vocab, f"{clip_id}.content_family.primary"
        )
        _require_vocab(
            content.get("content_scope"), scope_vocab, f"{clip_id}.content_scope"
        )

        profile = _require_mapping(
            raw["reference_profile"], f"{clip_id}.reference_profile"
        )
        duties = _require_list(
            profile.get("reference_duties"), f"{clip_id}.reference_duties"
        )
        for index, duty in enumerate(duties):
            _require_vocab(duty, duty_vocab, f"{clip_id}.reference_duties[{index}]")
        extensions = _require_list(
            profile.get("reference_duty_extensions"),
            f"{clip_id}.reference_duty_extensions",
        )
        for extension in extensions:
            if extension not in extension_vocab:
                raise CatalogValidationError(
                    f"{clip_id} has an unregistered reference-duty extension"
                )
            if extension == "narrative_reference":
                narrative_extension_count += 1
        taxonomy_status = profile.get("reference_taxonomy_status")
        if extensions:
            expected_statuses = {extension_vocab[value] for value in extensions}
            if taxonomy_status not in expected_statuses:
                raise CatalogValidationError(
                    f"{clip_id} extension taxonomy status mismatch"
                )
        elif taxonomy_status != "CONTROLLED":
            raise CatalogValidationError(f"{clip_id} taxonomy status must be CONTROLLED")
        if taxonomy_status == "TAXONOMY_DECISION_REQUIRED":
            taxonomy_decision_count += 1

        if raw["rights"] != EXPECTED_RIGHTS:
            raise CatalogValidationError(f"{clip_id} rights boundary mismatch")

        validation = _require_mapping(
            raw["record_validation"], f"{clip_id}.record_validation"
        )
        if validation.get("semantic_change") is not False:
            raise CatalogValidationError(f"{clip_id} semantic_change must be false")
        if validation.get("score_change") is not False:
            raise CatalogValidationError(f"{clip_id} score_change must be false")
        if validation.get("rights_change") is not False:
            raise CatalogValidationError(f"{clip_id} rights_change must be false")
        if validation.get("unknown_preserved") is not True:
            raise CatalogValidationError(f"{clip_id} unknown_preserved must be true")
        if validation.get("validation_status") != "PASS":
            raise CatalogValidationError(f"{clip_id} validation status is not PASS")

        artifacts = _require_list(raw["artifacts"], f"{clip_id}.artifacts")
        if len(artifacts) < 3:
            raise CatalogValidationError(f"{clip_id} has fewer than three artifacts")
        artifact_ids: set[str] = set()
        normalized_artifacts: list[Mapping[str, Any]] = []
        for index, value in enumerate(artifacts):
            artifact = _require_mapping(value, f"{clip_id}.artifacts[{index}]")
            _require_keys(
                artifact,
                (
                    "artifact_id",
                    "artifact_type",
                    "technical_validation_status",
                    "artifact_availability",
                    "artifact_lifecycle",
                    "artifact_bytes",
                ),
                f"{clip_id}.artifacts[{index}]",
            )
            artifact_id = artifact["artifact_id"]
            if not isinstance(artifact_id, str) or artifact_id in artifact_ids:
                raise CatalogValidationError(f"{clip_id} duplicate artifact identity")
            artifact_ids.add(artifact_id)
            _require_vocab(
                artifact["technical_validation_status"],
                technical_vocab,
                f"{artifact_id}.technical_validation_status",
            )
            _require_vocab(
                artifact["artifact_availability"],
                availability_vocab,
                f"{artifact_id}.artifact_availability",
            )
            _require_vocab(
                artifact["artifact_lifecycle"],
                lifecycle_vocab,
                f"{artifact_id}.artifact_lifecycle",
            )
            _require_nonnegative_int(artifact["artifact_bytes"], f"{artifact_id}.bytes")
            if artifact["technical_validation_status"] == (
                "PROXY_TECHNICAL_VALIDATION_FAILED"
            ):
                technical_failures += 1
            normalized_artifacts.append(artifact)

        retained_roles = _require_list(
            raw["retained_artifact_roles"], f"{clip_id}.retained_artifact_roles"
        )
        for retained in retained_roles:
            retained_mapping = _require_mapping(retained, f"{clip_id}.retained_role")
            _require_vocab(
                retained_mapping.get("role"),
                retained_role_vocab,
                f"{clip_id}.retained_role.role",
            )
            if retained_mapping.get("artifact_id") not in artifact_ids:
                raise CatalogValidationError(f"{clip_id} retained role has unknown artifact")

        proposals = _require_list(
            raw["storage_proposals"], f"{clip_id}.storage_proposals"
        )
        for proposal in proposals:
            proposal_mapping = _require_mapping(proposal, f"{clip_id}.proposal")
            _require_vocab(
                proposal_mapping.get("storage_proposal_action"),
                proposal_vocab,
                f"{clip_id}.proposal.action",
            )
            if proposal_mapping.get("executed") is not False:
                raise CatalogValidationError(f"{clip_id} proposal cannot be executed")

        overlap = _require_mapping(raw["overlap"], f"{clip_id}.overlap")
        _require_vocab(
            overlap.get("exact_duplicate_status"),
            duplicate_vocab,
            f"{clip_id}.overlap.exact_duplicate_status",
        )

        counts = _validate_storage_arithmetic(
            clip_id, raw, list(normalized_artifacts)
        )
        proxy_count += counts[0]
        proxy_bytes += counts[1]
        segment_count += counts[2]
        segment_bytes += counts[3]
        if clip_id == "G01D-CLIP-005":
            clip005_deleted_bytes = counts[4]
        elif counts[4] != 0:
            raise CatalogValidationError(f"unexpected deleted bytes in {clip_id}")

        provenance = _require_mapping(
            raw["field_provenance"], f"{clip_id}.field_provenance"
        )
        if provenance.get("scores") == "EXPLICIT_UNKNOWN_FROM_LEGACY_BACKFILL":
            review = _require_mapping(
                raw["review_observation"], f"{clip_id}.review_observation"
            )
            scores = _require_mapping(raw["scores"], f"{clip_id}.scores")
            legacy_values = [review.get("numeric_confidence")]
            legacy_values.extend(scores.get(field) for field in LEGACY_SCORE_FIELDS)
            for value in legacy_values:
                if value == 0 and not isinstance(value, bool):
                    unknown_to_zero += 1
                if value != UNKNOWN:
                    raise CatalogValidationError(
                        f"{clip_id} legacy unsupported value was not preserved as UNKNOWN"
                    )
                legacy_unknown_slots += 1

    observed_ids = tuple(record.pilot_clip_id for record in records)
    if observed_ids != EXPECTED_PILOT_CLIP_IDS:
        raise CatalogValidationError("catalog pilot ID coverage mismatch")

    summary = CatalogValidationSummary(
        record_count=len(records),
        unique_id_count=len(seen_clip_ids),
        technical_failure_count=technical_failures,
        current_proxy_file_count=proxy_count,
        current_proxy_bytes=proxy_bytes,
        retained_segment_count=segment_count,
        retained_segment_bytes=segment_bytes,
        current_total_derived_media_bytes=proxy_bytes + segment_bytes,
        clip005_historical_deleted_bytes=clip005_deleted_bytes,
        legacy_unknown_slots=legacy_unknown_slots,
        unknown_to_zero=unknown_to_zero,
        narrative_reference_extension_count=narrative_extension_count,
        taxonomy_decision_required_count=taxonomy_decision_count,
    )
    for field, expected in FIXED_INVARIANTS.items():
        if getattr(summary, field) != expected:
            raise CatalogValidationError(f"global invariant mismatch: {field}")
    return summary
