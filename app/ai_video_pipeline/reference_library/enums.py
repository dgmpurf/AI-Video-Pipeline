from __future__ import annotations

from enum import Enum


class ValueEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class TechnicalValidationStatus(ValueEnum):
    success = "SUCCESS"
    failed = "PROXY_TECHNICAL_VALIDATION_FAILED"
    not_evaluated = "NOT_EVALUATED"
    not_applicable = "NOT_APPLICABLE"
    unknown = "UNKNOWN"


class ArtifactAvailability(ValueEnum):
    present = "PRESENT"
    absent = "ABSENT"
    not_created = "NOT_CREATED"
    unknown = "UNKNOWN"


class ArtifactLifecycle(ValueEnum):
    active = "ACTIVE"
    preserved = "PRESERVED"
    deleted = "DELETED"
    failed_no_output = "FAILED_NO_OUTPUT"
    never_created = "NEVER_CREATED"
    superseded = "SUPERSEDED"
    unknown = "UNKNOWN"


class StorageProposalAction(ValueEnum):
    keep = "KEEP"
    keep_temporarily = "KEEP_TEMPORARILY"
    delete_candidate = "DELETE_CANDIDATE"
    targeted_segment_candidate = "TARGETED_SEGMENT_CANDIDATE"
    no_change = "NO_CHANGE"
    unknown = "UNKNOWN"


class ExactDuplicateStatus(ValueEnum):
    confirmed = "CONFIRMED"
    rejected = "REJECTED"
    unknown = "UNKNOWN"


class ReferenceTaxonomyStatus(ValueEnum):
    controlled = "CONTROLLED"
    decision_required = "TAXONOMY_DECISION_REQUIRED"
