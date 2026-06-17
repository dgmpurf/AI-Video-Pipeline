from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional


class RunMode(str, Enum):
    dry_run = "dry_run"
    mock = "mock"
    live = "live"


class TaskType(str, Enum):
    text2image = "text2image"
    image2image = "image2image"
    image2video = "image2video"
    frames2video = "frames2video"
    multimodal2video = "multimodal2video"


class ProviderName(str, Enum):
    dreamina_cli = "dreamina_cli"
    fake_live_provider = "fake_live_provider"
    kling_api = "kling_api"
    hailuo_api = "hailuo_api"
    runway_api = "runway_api"
    midjourney_image = "midjourney_image"


class ShotType(str, Enum):
    establishing = "establishing"
    action = "action"
    dialogue = "dialogue"
    insert = "insert"
    movement = "movement"
    transition = "transition"


class ShotStatus(str, Enum):
    draft = "draft"
    planned = "planned"
    approved = "approved"
    locked = "locked"
    rejected = "rejected"
    archived = "archived"


class AssetStatus(str, Enum):
    candidate = "candidate"
    locked_after_human_review = "locked_after_human_review"
    rejected = "rejected"
    archived = "archived"
    # Reserved value used for transitional review states if needed by callers.
    pending_review = "pending_review"


class ReviewStatus(str, Enum):
    pending_review = "pending_review"
    approved = "approved"
    rejected = "rejected"
    needs_rerun = "needs_rerun"


class AssetType(str, Enum):
    image = "image"
    video = "video"
    audio = "audio"
    document = "document"


class AssetRole(str, Enum):
    character = "character"
    scene = "scene"
    prop = "prop"
    keyframe = "keyframe"
    shot_video = "shot_video"
    source = "source"
    other = "other"


class AssetRelationshipType(str, Enum):
    exact_duplicate = "exact_duplicate"
    near_duplicate_variant = "near_duplicate_variant"
    continuity_pair = "continuity_pair"
    derived_from = "derived_from"
    alternate_candidate = "alternate_candidate"
    replaces = "replaces"
    rejected_due_to = "rejected_due_to"


def _ensure_datetime(value: Optional[datetime]) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    return datetime.now(timezone.utc)


def _ensure_non_empty(value: Any, field_name: str) -> str:
    text = "" if value is None else str(value).strip()
    if not text:
        raise ValueError(f"{field_name} is required")
    return text


def _ensure_list_of_str(values: Any, field_name: str) -> List[str]:
    if values is None:
        return []
    if not isinstance(values, list):
        raise ValueError(f"{field_name} must be a list of strings")
    items: List[str] = []
    for item in values:
        text = "" if item is None else str(item).strip()
        if not text:
            raise ValueError(f"{field_name} entries must be non-empty")
        items.append(text)
    return items


@dataclass
class TaskSpec:
    task_id: str
    task_type: TaskType
    provider: ProviderName
    prompt: str
    output_name: str
    dependency_task_ids: List[str] = field(default_factory=list)
    phase: Optional[str] = None
    model_version: Optional[str] = None
    ratio: Optional[str] = None
    resolution_type: Optional[str] = None
    duration: Optional[int] = None
    video_resolution: Optional[str] = None
    reference_ids: List[str] = field(default_factory=list)
    status: Optional[str] = None
    review_status: Optional[ReviewStatus] = None
    notes: Optional[str] = None

    def to_manifest_row(self) -> Dict[str, str]:
        return {
            "task_id": self.task_id,
            "phase": self.phase or "",
            "task_type": self.task_type.value,
            "provider": self.provider.value,
            "model_version": self.model_version or "",
            "ratio": self.ratio or "",
            "resolution_type": self.resolution_type or "",
            "duration": "" if self.duration is None else str(self.duration),
            "video_resolution": self.video_resolution or "",
            "prompt": self.prompt,
            "reference_ids": "|".join(self.reference_ids),
            "output_name": self.output_name,
            "status": self.status or "",
            "review_status": self.review_status.value if isinstance(self.review_status, ReviewStatus) else (self.review_status or ""),
            "notes": self.notes or "",
        }

    def to_json(self) -> str:
        return json.dumps({
            "task_id": self.task_id,
            "task_type": self.task_type.value,
            "provider": self.provider.value,
            "prompt": self.prompt,
            "output_name": self.output_name,
            "reference_ids": self.reference_ids,
            "status": self.status,
            "review_status": self.review_status.value if isinstance(self.review_status, ReviewStatus) else self.review_status,
            "notes": self.notes,
            "model_version": self.model_version,
            "ratio": self.ratio,
            "resolution_type": self.resolution_type,
            "duration": self.duration,
            "video_resolution": self.video_resolution,
            "phase": self.phase,
        })


@dataclass
class AssetRecord:
    logical_id: str
    candidate_id: str
    asset_type: AssetType = AssetType.image
    role: AssetRole = AssetRole.other
    relative_path: Optional[Path] = None
    source_path: Optional[Path] = None
    status: AssetStatus = AssetStatus.candidate
    review_status: ReviewStatus = ReviewStatus.pending_review
    origin_project: Optional[str] = None
    source_task_id: Optional[str] = None
    submit_id: Optional[str] = None
    review_note: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    sha256: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration_seconds: Optional[float] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @staticmethod
    def _to_path(value: Any) -> Optional[Path]:
        if value is None:
            return None
        return Path(value)

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "AssetRecord":
        return cls(
            logical_id=raw["logical_id"],
            candidate_id=raw["candidate_id"],
            asset_type=AssetType(raw.get("asset_type", AssetType.image.value)),
            role=AssetRole(raw.get("role", AssetRole.other.value)),
            relative_path=cls._to_path(raw.get("relative_path")),
            source_path=cls._to_path(raw.get("source_path")),
            status=AssetStatus(raw.get("status", AssetStatus.candidate.value)),
            review_status=ReviewStatus(raw.get("review_status", ReviewStatus.pending_review.value)),
            origin_project=raw.get("origin_project"),
            source_task_id=raw.get("source_task_id"),
            submit_id=raw.get("submit_id"),
            review_note=raw.get("review_note"),
            tags=list(raw.get("tags", [])),
            sha256=raw.get("sha256"),
            width=raw.get("width"),
            height=raw.get("height"),
            duration_seconds=raw.get("duration_seconds"),
            created_at=_ensure_datetime(raw.get("created_at")),
            updated_at=_ensure_datetime(raw.get("updated_at")),
        )

    def asdict(self) -> Dict[str, Any]:
        return {
            "logical_id": self.logical_id,
            "candidate_id": self.candidate_id,
            "asset_type": self.asset_type.value,
            "role": self.role.value,
            "relative_path": str(self.relative_path) if self.relative_path is not None else None,
            "source_path": str(self.source_path) if self.source_path is not None else None,
            "status": self.status.value,
            "review_status": self.review_status.value,
            "origin_project": self.origin_project,
            "source_task_id": self.source_task_id,
            "submit_id": self.submit_id,
            "review_note": self.review_note,
            "tags": list(self.tags),
            "sha256": self.sha256,
            "width": self.width,
            "height": self.height,
            "duration_seconds": self.duration_seconds,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


@dataclass
class AssetRelationship:
    logical_id: str
    candidate_id: str
    related_logical_id: str
    related_candidate_id: str
    relationship_type: AssetRelationshipType
    is_canonical: bool = False
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    note: Optional[str] = None

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "AssetRelationship":
        return cls(
            logical_id=raw["logical_id"],
            candidate_id=raw["candidate_id"],
            related_logical_id=raw["related_logical_id"],
            related_candidate_id=raw["related_candidate_id"],
            relationship_type=AssetRelationshipType(raw["relationship_type"]),
            is_canonical=bool(raw.get("is_canonical", False)),
            created_at=_ensure_datetime(raw.get("created_at")),
            note=raw.get("note"),
        )

    def asdict(self) -> Dict[str, Any]:
        return {
            "logical_id": self.logical_id,
            "candidate_id": self.candidate_id,
            "related_logical_id": self.related_logical_id,
            "related_candidate_id": self.related_candidate_id,
            "relationship_type": self.relationship_type.value,
            "is_canonical": self.is_canonical,
            "created_at": self.created_at.isoformat(),
            "note": self.note,
        }


@dataclass
class MediaRef:
    asset_id: str
    path: Path
    checksum_sha256: str
    source: Optional[str] = None


@dataclass
class ProviderRequest:
    task_id: str
    provider: ProviderName
    task_type: TaskType
    command_argv: List[str]
    status: str = "prepared"
    output_name: Optional[str] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_json_line(self) -> str:
        return json.dumps(
            {
                "task_id": self.task_id,
                "provider": self.provider.value,
                "task_type": self.task_type.value,
                "command_argv": self.command_argv,
                "status": self.status,
                "output_name": self.output_name,
                "created_at": self.created_at.isoformat(),
            },
            ensure_ascii=True,
        )


@dataclass
class ProviderResult:
    task_id: str
    provider: ProviderName
    task_type: TaskType
    success: bool
    output_path: Optional[Path] = None
    notes: Optional[str] = None
    submitted_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_csv_row(self) -> Dict[str, str]:
        return {
            "task_id": self.task_id,
            "provider": self.provider.value,
            "task_type": self.task_type.value,
            "success": str(self.success),
            "output_path": str(self.output_path) if self.output_path else "",
            "notes": self.notes or "",
        }

    def to_dict(self) -> Dict[str, Any]:
        row = self.to_csv_row()
        row["success"] = self.success
        row["submitted_at"] = self.submitted_at.isoformat()
        return row


@dataclass
class RunRecord:
    run_id: str
    mode: RunMode
    tasks_total: int
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    status: str = "created"
    notes: Optional[str] = None

    def finish(self, status: str) -> None:
        self.completed_at = datetime.now(timezone.utc)
        self.status = status


@dataclass
class ReviewRecord:
    task_id: str
    status: ReviewStatus = ReviewStatus.pending_review
    reviewer: Optional[str] = None
    decided_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    notes: Optional[str] = None


@dataclass
class FSWritePlan:
    root: Path
    planned_files: List[Path] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "root": str(self.root),
            "planned_files": [str(item) for item in self.planned_files],
            "created_at": self.created_at.isoformat(),
        }


@dataclass
class ShotRecord:
    shot_id: str
    production_id: str
    sequence_id: str
    scene_id: str
    shot_index: int
    title: str
    shot_type: ShotType = ShotType.establishing
    duration_seconds: float = 0.0
    story_beat: str = ""
    visual_goal: str = ""
    action_goal: str = ""
    camera_goal: str = ""
    required_asset_ids: List[str] = field(default_factory=list)
    previous_shot_id: str | None = None
    next_shot_id: str | None = None
    status: ShotStatus = ShotStatus.draft
    review_status: ReviewStatus = ReviewStatus.pending_review
    notes: str = ""

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "ShotRecord":
        return cls(
            shot_id=_ensure_non_empty(raw.get("shot_id"), "shot_id"),
            production_id=_ensure_non_empty(raw.get("production_id"), "production_id"),
            sequence_id=_ensure_non_empty(raw.get("sequence_id"), "sequence_id"),
            scene_id=_ensure_non_empty(raw.get("scene_id"), "scene_id"),
            shot_index=int(raw.get("shot_index", 0)),
            title=_ensure_non_empty(raw.get("title"), "title"),
            shot_type=ShotType(raw.get("shot_type", ShotType.establishing.value)),
            duration_seconds=float(raw.get("duration_seconds", 0.0)),
            story_beat=str(raw.get("story_beat", "")).strip(),
            visual_goal=_ensure_non_empty(raw.get("visual_goal"), "visual_goal"),
            action_goal=str(raw.get("action_goal", "")).strip(),
            camera_goal=str(raw.get("camera_goal", "")).strip(),
            required_asset_ids=_ensure_list_of_str(raw.get("required_asset_ids", []), "required_asset_ids"),
            previous_shot_id=raw.get("previous_shot_id"),
            next_shot_id=raw.get("next_shot_id"),
            status=ShotStatus(raw.get("status", ShotStatus.draft.value)),
            review_status=ReviewStatus(raw.get("review_status", ReviewStatus.pending_review.value)),
            notes=str(raw.get("notes", "")).strip(),
        )

    def validate(self) -> None:
        if self.shot_type == ShotType.action and not self.action_goal:
            raise ValueError("action_goal is required for action shots")
        if self.duration_seconds < 0:
            raise ValueError("duration_seconds must be >= 0")

    def asdict(self) -> Dict[str, Any]:
        return {
            "shot_id": self.shot_id,
            "production_id": self.production_id,
            "sequence_id": self.sequence_id,
            "scene_id": self.scene_id,
            "shot_index": self.shot_index,
            "title": self.title,
            "shot_type": self.shot_type.value,
            "duration_seconds": self.duration_seconds,
            "story_beat": self.story_beat,
            "visual_goal": self.visual_goal,
            "action_goal": self.action_goal,
            "camera_goal": self.camera_goal,
            "required_asset_ids": list(self.required_asset_ids),
            "previous_shot_id": self.previous_shot_id,
            "next_shot_id": self.next_shot_id,
            "status": self.status.value,
            "review_status": self.review_status.value,
            "notes": self.notes,
        }


@dataclass
class ShotDependency:
    source_shot_id: str
    target_shot_id: str
    dependency_type: str
    notes: str = ""

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "ShotDependency":
        return cls(
            source_shot_id=_ensure_non_empty(raw.get("source_shot_id"), "source_shot_id"),
            target_shot_id=_ensure_non_empty(raw.get("target_shot_id"), "target_shot_id"),
            dependency_type=_ensure_non_empty(raw.get("dependency_type"), "dependency_type"),
            notes=str(raw.get("notes", "")).strip(),
        )

    def asdict(self) -> Dict[str, Any]:
        return {
            "source_shot_id": self.source_shot_id,
            "target_shot_id": self.target_shot_id,
            "dependency_type": self.dependency_type,
            "notes": self.notes,
        }


@dataclass
class ShotContinuity:
    source_shot_id: str
    target_shot_id: str
    relation: str = "sequence"

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "ShotContinuity":
        return cls(
            source_shot_id=_ensure_non_empty(raw.get("source_shot_id"), "source_shot_id"),
            target_shot_id=_ensure_non_empty(raw.get("target_shot_id"), "target_shot_id"),
            relation=str(raw.get("relation", "sequence")).strip() or "sequence",
        )

    def asdict(self) -> Dict[str, Any]:
        return {
            "source_shot_id": self.source_shot_id,
            "target_shot_id": self.target_shot_id,
            "relation": self.relation,
        }


@dataclass
class ShotAssetRequirement:
    shot_id: str
    logical_id: str
    candidate_id: str | None = None
    role: str | None = None
    mandatory: bool = True

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "ShotAssetRequirement":
        return cls(
            shot_id=_ensure_non_empty(raw.get("shot_id"), "shot_id"),
            logical_id=_ensure_non_empty(raw.get("logical_id"), "logical_id"),
            candidate_id=raw.get("candidate_id"),
            role=raw.get("role"),
            mandatory=bool(raw.get("mandatory", True)),
        )

    def asdict(self) -> Dict[str, Any]:
        return {
            "shot_id": self.shot_id,
            "logical_id": self.logical_id,
            "candidate_id": self.candidate_id,
            "role": self.role,
            "mandatory": self.mandatory,
        }
