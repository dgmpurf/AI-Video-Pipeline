from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from ..core.models import ShotRecord, ShotType
from .negative_rules import get_default_negative_rules
from .reference_roles import ReferenceRole, _to_reference_role


class PromptFactory:
    @staticmethod
    def build_reference_role_block(reference_roles: Iterable[dict] | Iterable[ReferenceRole]) -> str:
        parsed = [_to_reference_role(item) for item in reference_roles]
        lines = [
            f"{role.order}. {role.logical_id} [{role.role_type}] {role.role_description}"
            for role in sorted(parsed, key=lambda item: item.order)
        ]
        return "\n".join(lines)

    @staticmethod
    def contains_vague_action_language(action_goal: str) -> bool:
        text = (action_goal or "").lower()
        vague = (
            "preparing",
            "about to",
            "before the action",
            "keep far apart",
        )
        return any(token in text for token in vague)

    @staticmethod
    def build_keyframe_prompt(
        shot_record: ShotRecord,
        reference_roles: Iterable[dict] | Iterable[ReferenceRole],
        style_rules: dict | list[str] | str,
        negative_rules: list[str] | None = None,
    ) -> str:
        shot_record.validate()
        lines = [
            f"Keyframe prompt for {shot_record.shot_id}",
            f"Story beat: {shot_record.story_beat}",
            f"Visual goal: {shot_record.visual_goal}",
        ]
        if shot_record.action_goal:
            lines.append(f"Action goal: {shot_record.action_goal}")
        if shot_record.camera_goal:
            lines.append(f"Camera goal: {shot_record.camera_goal}")

        style_goal = PromptFactory._style_lines(style_rules)
        if style_goal:
            lines.extend(style_goal)

        role_block = PromptFactory.build_reference_role_block(reference_roles)
        if role_block:
            lines.extend(["Reference roles:", role_block])

        negative = PromptFactory.build_negative_prompt(negative_rules or get_default_negative_rules("asset_image"))
        if negative:
            lines.append(f"Negative: {negative}")

        if shot_record.shot_type == ShotType.action and PromptFactory.contains_vague_action_language(shot_record.action_goal):
            lines.append("Avoid vague action wording; use contact point, force chain, and motion direction.")

        return "\n".join(lines)

    @staticmethod
    def build_video_prompt(
        shot_record: ShotRecord,
        reference_roles: Iterable[dict] | Iterable[ReferenceRole],
        motion_plan: str,
        camera_plan: str,
        negative_rules: list[str] | None = None,
    ) -> str:
        shot_record.validate()
        lines = [
            f"Video prompt for {shot_record.shot_id}",
            f"Story beat: {shot_record.story_beat}",
            f"Action goal: {shot_record.action_goal}",
            f"Camera goal: {shot_record.camera_goal}",
            f"Motion plan: {motion_plan}",
            f"Camera plan: {camera_plan}",
            f"Visual goal: {shot_record.visual_goal}",
        ]

        role_block = PromptFactory.build_reference_role_block(reference_roles)
        if role_block:
            lines.extend(["Reference roles:", role_block])

        negative = PromptFactory.build_negative_prompt(negative_rules or get_default_negative_rules("video"))
        if negative:
            lines.append(f"Negative: {negative}")

        if shot_record.shot_type == ShotType.action and PromptFactory.contains_vague_action_language(shot_record.action_goal):
            lines.append("Avoid vague action wording; prefer force chain, body weight transfer, and environmental feedback.")

        return "\n".join(lines)

    @staticmethod
    def build_negative_prompt(negative_rules: list[str]) -> str:
        if not negative_rules:
            return ""
        return "; ".join(item.strip() for item in negative_rules if str(item).strip())

    @staticmethod
    def _style_lines(style_rules: dict | list[str] | str) -> list[str]:
        if style_rules is None:
            return []
        if isinstance(style_rules, str):
            return [f"Style goal: {style_rules}"] if style_rules.strip() else []
        if isinstance(style_rules, list):
            return [f"Style goal: {item}" for item in style_rules if str(item).strip()]
        if isinstance(style_rules, dict):
            value = style_rules.get("style_goal") if isinstance(style_rules.get("style_goal"), str) else None
            if value and value.strip():
                return [f"Style goal: {value}"]
            return []
        return []