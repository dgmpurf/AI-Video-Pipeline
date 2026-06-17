from __future__ import annotations

from typing import Iterable

NEGATIVE_RULE_DEFINITIONS = {
    "no_text": "no readable text, titles, subtitles, labels, logos, or UI",
    "no_watermark": "no watermark, no brand stamps, no captions in frame",
    "no_extra_people": "no extra people",
    "no_character_duplicate": "no duplicated characters",
    "no_reference_card_artifact": "no reference card artifacts or overlays",
    "no_three_view_artifact": "no three-view chart artifacts",
    "no_cartoon_style": "no cartoon, illustration, or anime style",
    "no_modern_objects": "no modern objects unrelated to period",
    "no_face_drift": "no face drift or identity drift",
    "no_body_merge": "no body merge or impossible joints",
}

DEFAULT_NEGATIVE_RULE_SETS = {
    "asset_image": ["no_text", "no_watermark", "no_reference_card_artifact", "no_face_drift", "no_body_merge"],
    "keyframe_image": ["no_text", "no_watermark", "no_three_view_artifact", "no_reference_card_artifact", "no_character_duplicate"],
    "video": ["no_text", "no_watermark", "no_extra_people", "no_body_merge", "no_face_drift", "no_modern_objects"],
}


def get_default_negative_rules(prompt_type: str) -> list[str]:
    prompt_type_key = str(prompt_type).strip().lower()
    if prompt_type_key not in DEFAULT_NEGATIVE_RULE_SETS:
        raise ValueError(f"Unknown prompt_type: {prompt_type}")
    names: list[str] = list(DEFAULT_NEGATIVE_RULE_SETS[prompt_type_key])
    return [NEGATIVE_RULE_DEFINITIONS[name] for name in names if name in NEGATIVE_RULE_DEFINITIONS]


def resolve_negative_rule_names(prompt_type: str) -> list[str]:
    rules = get_default_negative_rules(prompt_type)
    return [name for name in DEFAULT_NEGATIVE_RULE_SETS[prompt_type] if name in NEGATIVE_RULE_DEFINITIONS]


def normalize_negative_rules(raw_rules: Iterable[str]) -> list[str]:
    out: list[str] = []
    for value in raw_rules:
        text = str(value).strip()
        if not text:
            continue
        out.append(text)
    return out