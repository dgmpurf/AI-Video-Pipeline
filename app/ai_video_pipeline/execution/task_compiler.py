from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

from ..assets.registry import AssetRegistry
from ..core.models import ProviderName, ShotRecord, TaskSpec, TaskType
from ..prompts.prompt_record import PromptRecord
from ..prompts.prompt_validation import validate_prompt_record


@dataclass(frozen=True)
class TaskCompilerDefaults:
    provider: ProviderName = ProviderName.dreamina_cli
    phase: str = "phaseE"
    image_model_version: str = "5.0"
    image_ratio: str = "16:9"
    image_resolution_type: str = "2k"
    video_model_version: str = "seedance2.0fast_vip"
    video_ratio: str = "16:9"
    video_duration: int = 5
    video_resolution: str = "720p"

    @classmethod
    def from_mapping(cls, raw: Mapping[str, Any] | None) -> "TaskCompilerDefaults":
        raw = raw or {}
        provider_raw = str(raw.get("provider", raw.get("default_provider", cls.provider.value)))
        return cls(
            provider=ProviderName(provider_raw),
            phase=str(raw.get("phase", cls.phase)),
            image_model_version=str(raw.get("image_model_version", cls.image_model_version)),
            image_ratio=str(raw.get("image_ratio", cls.image_ratio)),
            image_resolution_type=str(raw.get("image_resolution_type", cls.image_resolution_type)),
            video_model_version=str(raw.get("video_model_version", cls.video_model_version)),
            video_ratio=str(raw.get("video_ratio", cls.video_ratio)),
            video_duration=int(raw.get("video_duration", cls.video_duration)),
            video_resolution=str(raw.get("video_resolution", cls.video_resolution)),
        )


def compile_prompt_to_task(
    prompt_record: PromptRecord,
    shot_record: ShotRecord,
    provider_defaults: Mapping[str, Any] | TaskCompilerDefaults | None,
    *,
    asset_registry: AssetRegistry | None = None,
) -> TaskSpec:
    defaults = _coerce_defaults(provider_defaults)
    validate_prompt_record(prompt_record, shot_record, asset_registry)

    task_type = _task_type_for_prompt(prompt_record)
    kwargs = _task_defaults_for_type(task_type, defaults)
    return TaskSpec(
        task_id=prompt_record.prompt_id,
        phase=defaults.phase,
        task_type=task_type,
        provider=defaults.provider,
        prompt=prompt_record.prompt_text,
        reference_ids=list(prompt_record.reference_ids),
        output_name=_build_output_name(prompt_record, shot_record),
        status=prompt_record.status,
        review_status=None,
        notes=_build_notes(prompt_record),
        **kwargs,
    )


def compile_shot_prompts_to_tasks(
    shot_registry: Any,
    prompt_records: Iterable[PromptRecord],
    provider_defaults: Mapping[str, Any] | TaskCompilerDefaults | None,
    *,
    asset_registry: AssetRegistry | None = None,
) -> list[TaskSpec]:
    shots = _load_shots(shot_registry)
    by_shot_id = {shot.shot_id: shot for shot in shots}
    tasks: list[TaskSpec] = []
    for prompt_record in sorted(prompt_records, key=lambda item: item.prompt_id):
        if not prompt_record.shot_id:
            raise ValueError(f"prompt_record has no shot_id: {prompt_record.prompt_id}")
        shot_record = by_shot_id.get(prompt_record.shot_id)
        if shot_record is None:
            raise ValueError(f"shot not found for prompt: {prompt_record.shot_id}")
        tasks.append(
            compile_prompt_to_task(
                prompt_record,
                shot_record,
                provider_defaults,
                asset_registry=asset_registry,
            )
        )
    return tasks


def _coerce_defaults(provider_defaults: Mapping[str, Any] | TaskCompilerDefaults | None) -> TaskCompilerDefaults:
    if isinstance(provider_defaults, TaskCompilerDefaults):
        return provider_defaults
    return TaskCompilerDefaults.from_mapping(provider_defaults)


def _load_shots(shot_registry: Any) -> list[ShotRecord]:
    if hasattr(shot_registry, "load"):
        return list(shot_registry.load())
    return list(shot_registry)


def _task_type_for_prompt(prompt_record: PromptRecord) -> TaskType:
    if prompt_record.prompt_type == "keyframe_image":
        return TaskType.image2image
    if prompt_record.prompt_type == "video":
        return TaskType.multimodal2video
    if prompt_record.prompt_type == "asset_image":
        return TaskType.image2image if prompt_record.reference_ids else TaskType.text2image
    raise ValueError(f"unknown prompt_type: {prompt_record.prompt_type}")


def _task_defaults_for_type(task_type: TaskType, defaults: TaskCompilerDefaults) -> dict[str, Any]:
    if task_type == TaskType.multimodal2video:
        return {
            "model_version": defaults.video_model_version,
            "ratio": defaults.video_ratio,
            "resolution_type": None,
            "duration": defaults.video_duration,
            "video_resolution": defaults.video_resolution,
        }
    return {
        "model_version": defaults.image_model_version,
        "ratio": defaults.image_ratio,
        "resolution_type": defaults.image_resolution_type,
        "duration": None,
        "video_resolution": None,
    }


def _build_output_name(prompt_record: PromptRecord, shot_record: ShotRecord) -> str:
    source = prompt_record.shot_id or shot_record.shot_id
    suffix = prompt_record.prompt_type.replace("_", "-")
    return f"{source}-{suffix}-{prompt_record.version}".replace(" ", "-")


def _build_notes(prompt_record: PromptRecord) -> str:
    if prompt_record.negative_prompt:
        return f"{prompt_record.notes} negative_prompt={prompt_record.negative_prompt}".strip()
    return prompt_record.notes
