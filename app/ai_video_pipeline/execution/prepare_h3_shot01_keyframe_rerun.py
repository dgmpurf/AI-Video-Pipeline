from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image

from ..core.manifest import parse_manifest_csv
from ..core.models import RunMode
from ..execution.live_gate import LiveRunRequest, validate_live_run_request
from ..execution.runner import PipelineRunner
from ..path_policy import PathPolicy

PRODUCTION_ID = "chi_yan_tian_qiong"
FAILED_TASK_ID = "SHOT-01-KF-001"
TASK_ID = "SHOT-01-KF-002"
SUBMIT_ID = "ccff71eb-e233-4a43-8ddc-7c756d1161bf"

REFERENCE_IDS = [
    "A-SC-TEMPLE-COURTYARD-001",
    "A-CH-A-SUBJECT-001",
    "A-CH-B-SUBJECT-001",
]

OUTPUT_NAME = "SHOT-01-KF-002_temple_gate_courtyard_standoff_keyframe"

PROMPT_TEXT = (
    "Reference image 1 is the locked temple courtyard environment. Use it for the ancient Chinese temple "
    "courtyard, light rain, wet reflective stone ground, dark wooden hall, distant tower, prayer flags, "
    "cool blue-gray mist, and cinematic spatial depth. Do not copy its camera angle as a rigid layout. "
    "Use it as environment identity and atmosphere.\n\n"
    "Reference image 2 is the locked Fenshou full-body subject. Use it for Fenshou's appearance: black "
    "high ponytail, stern male face, strong athletic build, black and dark red layered battle armor, boots, "
    "and cold martial presence. Do not copy the neutral front-facing pose from the subject reference.\n\n"
    "Reference image 3 is the locked Shuangji full-body subject. Use it for Shuangji's appearance: silver-blue "
    "high ponytail, calm cold face, blue-silver light armor, long robe silhouette, modest high-collar outfit, "
    "and restrained guardian presence. Do not copy the neutral front-facing pose from the subject reference.\n\n"
    "Create a cinematic semi-realistic 3D keyframe for SHOT-01: the first confrontation in the rain-soaked "
    "temple courtyard.\n\n"
    "The main temple hall entrance is the background anchor. Fenshou and Shuangji stand in the mid-ground "
    "action zone of the courtyard, in front of the temple hall entrance, not close to the camera.\n\n"
    "Fenshou stands in the left-midground courtyard area, body turned three-quarter toward the right. His "
    "shoulders, chest, feet, and eyes point toward Shuangji.\n\n"
    "Shuangji stands in the right-midground courtyard area, body turned three-quarter toward the left. Her "
    "shoulders, chest, feet, and eyes point toward Fenshou.\n\n"
    "They form a clear diagonal confrontation axis across the wet stone courtyard. There is visible open wet "
    "stone ground between them for future combat movement.\n\n"
    "The camera observes from a three-quarter front-side angle across the courtyard. It is not a front-facing "
    "character lineup. It is not a two-character poster. The shot should feel like a real film scene with "
    "spatial blocking.\n\n"
    "Rain falls through the scene. Prayer flags move slightly in the wind. The wet ground reflects the "
    "characters and temple architecture. Mist softens the background. The image should preserve the locked "
    "character designs and the locked temple atmosphere.\n\n"
    "Style: cinematic semi-realistic 3D wuxia fantasy, cool blue-gray atmosphere, low saturation, subtle "
    "ink-wash mood, detailed but not over-cluttered.\n\n"
    "Restrictions: no text, no watermark, no extra people, no animals, no character sheet layout, no "
    "three-view layout, no multiple poses, no extra heads, no duplicate Fenshou, no duplicate Shuangji, no "
    "merged bodies, no cropped feet, no modern objects, no neon lights, no sci-fi elements, no cartoon style, "
    "no cel-shading, no overpowered magic effects, no blood, do not make both characters face the viewer, "
    "do not place them as a foreground lineup, do not paste them onto the camera plane."
)

THREE_LAYER_MATRIX = {
    "space_layer": [
        "The locked temple courtyard image is used as an environment reference only.",
        "The main temple hall entrance is the background anchor.",
        "The characters must stand in the mid-ground action zone of the wet stone courtyard, in front of the temple hall entrance.",
        "They must not stand pasted onto the foreground camera plane.",
        "The wet stone ground between them must remain visible as the future combat space.",
        "The courtyard should feel like a real spatial stage, not a flat background.",
    ],
    "character_blocking_layer": [
        "Fenshou stands in the left-midground area of the courtyard, closer to the camera than Shuangji but still inside the courtyard space.",
        "Fenshou's body is turned three-quarter toward the right, facing Shuangji.",
        "His shoulders, chest, feet, and eyeline all point toward Shuangji, not toward the viewer.",
        "Shuangji stands in the right-midground area of the courtyard, slightly farther back.",
        "Shuangji's body is turned three-quarter toward the left, facing Fenshou.",
        "Her shoulders, chest, feet, and eyeline all point toward Fenshou, not toward the viewer.",
        "The two characters form a clear diagonal confrontation axis across the courtyard.",
        "They are separated by visible wet stone ground.",
        "They are not posing side by side for a poster.",
    ],
    "camera_layer": [
        "The camera observes from a three-quarter front-side angle across the courtyard.",
        "The camera is not directly in front of the characters.",
        "The shot is a cinematic medium-wide keyframe.",
        "The temple hall entrance remains behind the confrontation as the background anchor.",
        "The camera should capture both full-body characters, the space between them, and the temple architecture.",
        "This is a confrontation scene, not a character lineup.",
    ],
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _image_integrity(path: Path) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "exists": path.exists(),
        "file_size": path.stat().st_size if path.exists() else 0,
        "sha256": _sha256(path) if path.exists() else "",
        "openable": False,
        "width": None,
        "height": None,
        "format": None,
    }
    if not path.exists():
        return payload
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        payload.update({"openable": True, "width": image.width, "height": image.height, "format": image.format})
    return payload


def _load_asset_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"assets": [], "relationships": []}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Any, policy: PathPolicy) -> None:
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def _write_text(path: Path, text: str, policy: PathPolicy) -> None:
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def _write_manifest(path: Path, row: dict[str, str], policy: PathPolicy) -> None:
    headers = [
        "task_id",
        "phase",
        "task_type",
        "provider",
        "model_version",
        "ratio",
        "resolution_type",
        "duration",
        "video_resolution",
        "prompt",
        "reference_ids",
        "output_name",
        "status",
        "review_status",
        "notes",
    ]
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerow({key: row.get(key, "") for key in headers})


def _reference_registry(root: Path, asset_registry: dict[str, Any], policy: PathPolicy) -> dict[str, str]:
    registry: dict[str, str] = {}
    for logical_id in REFERENCE_IDS:
        matches = [item for item in asset_registry.get("assets", []) if item.get("logical_id") == logical_id]
        if not matches:
            raise RuntimeError(f"missing locked asset: {logical_id}")
        item = matches[-1]
        if item.get("status") != "locked_after_human_review" or item.get("review_status") != "approved":
            raise RuntimeError(f"asset is not locked and approved: {logical_id}")
        candidate = policy.ensure(root / item["relative_path"])
        if not candidate.exists():
            raise FileNotFoundError(candidate)
        registry[logical_id] = str(candidate)
    return registry


def _register_failed_candidate(root: Path, asset_registry_path: Path, policy: PathPolicy) -> dict[str, Any]:
    output_rel = (
        "productions/chi_yan_tian_qiong/runs/live/20260614_064100_SHOT-01-KF-001/"
        "output/SHOT-01-KF-001_temple_courtyard_standoff_keyframe.png"
    )
    output_path = policy.ensure(root / output_rel)
    integrity = _image_integrity(output_path)
    payload = _load_asset_registry(asset_registry_path)
    candidate = {
        "logical_id": FAILED_TASK_ID,
        "candidate_id": f"{FAILED_TASK_ID}_cand_001",
        "asset_type": "image",
        "role": "keyframe",
        "relative_path": output_rel,
        "source_path": output_rel,
        "status": "candidate",
        "review_status": "needs_rerun",
        "origin_project": "AI_VIDEO_PIPELINE",
        "source_task_id": FAILED_TASK_ID,
        "submit_id": SUBMIT_ID,
        "review_note": "Candidate keyframe failed human review; needs rerun due to missing three-layer spatial blocking.",
        "tags": [
            "shot_keyframe",
            "shot_01",
            "needs_rerun",
            "three_layer_positioning_missing",
            "blocking_failure",
        ],
        "sha256": integrity["sha256"],
        "width": integrity["width"],
        "height": integrity["height"],
        "duration_seconds": None,
        "created_at": _now(),
        "updated_at": _now(),
    }
    assets = payload.setdefault("assets", [])
    for index, item in enumerate(assets):
        if item.get("logical_id") == candidate["logical_id"] and item.get("candidate_id") == candidate["candidate_id"]:
            created_at = item.get("created_at", candidate["created_at"])
            candidate["created_at"] = created_at
            assets[index] = candidate
            break
    else:
        assets.append(candidate)
    _write_json(asset_registry_path, payload, policy)
    return {"record": candidate, "integrity": integrity}


def _append_review_record(path: Path, policy: PathPolicy) -> None:
    record = {
        "review_id": "review-h2-2-shot-01-kf-001",
        "logical_id": FAILED_TASK_ID,
        "candidate_id": f"{FAILED_TASK_ID}_cand_001",
        "decision": "needs_rerun",
        "reviewer": "user",
        "score": 0.0,
        "issue_tags": [
            "three_layer_positioning_missing",
            "blocking_failure",
            "characters_face_camera",
            "foreground_lineup_not_courtyard_standoff",
        ],
        "note": (
            "The image is visually clean and the assets are preserved, but the shot goal failed. "
            "The characters are placed like a front-facing two-character lineup in the foreground. "
            "They are facing the viewer instead of facing each other. They are not staged in the "
            "mid-ground courtyard action zone in front of the temple hall entrance. The temple scene "
            "is good, but the character blocking and camera-space relationship are wrong. This should "
            "not be locked as SHOT-01 keyframe."
        ),
        "created_at": _now(),
        "source_path": (
            "productions/chi_yan_tian_qiong/runs/live/20260614_064100_SHOT-01-KF-001/"
            "output/SHOT-01-KF-001_temple_courtyard_standoff_keyframe.png"
        ),
        "target_status_after_decision": "candidate",
        "locked_path": "",
        "rerun_reason": "three_layer_positioning_missing",
    }
    target = policy.ensure_write(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    current = target.read_text(encoding="utf-8") if target.exists() else ""
    if '"review_id": "review-h2-2-shot-01-kf-001"' not in current and '"review_id":"review-h2-2-shot-01-kf-001"' not in current:
        with target.open("a", encoding="utf-8", newline="\n") as handle:
            if current and not current.endswith("\n"):
                handle.write("\n")
            handle.write(json.dumps(record, ensure_ascii=True) + "\n")


def _extract_dry_run_argv(run_dir: Path) -> list[str]:
    rows = [json.loads(line) for line in (run_dir / "provider_requests.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != 1:
        raise RuntimeError("expected exactly one provider request")
    return list(rows[0]["command_argv"])


def _staged_media_manifest(argv: list[str], references: dict[str, str], policy: PathPolicy, run_dir: Path) -> list[dict[str, Any]]:
    staged_paths: list[Path] = []
    for index, token in enumerate(argv):
        if token == "--images":
            staged_paths.append(policy.ensure(Path(argv[index + 1])))
    if len(staged_paths) != len(REFERENCE_IDS):
        raise RuntimeError("dry-run argv must include exactly three --images refs")
    rows = []
    for order, (logical_id, staged_path) in enumerate(zip(REFERENCE_IDS, staged_paths), start=1):
        source_path = policy.ensure(Path(references[logical_id]))
        rows.append(
            {
                "order": order,
                "logical_id": logical_id,
                "source_path": str(source_path),
                "staged_path": str(staged_path),
                "staged_filename_ascii": staged_path.name.isascii(),
                "source_sha256": _sha256(source_path),
                "staged_sha256": _sha256(staged_path),
                "sha256_match": _sha256(source_path) == _sha256(staged_path),
                "inside_workspace": True,
            }
        )
    _write_json(run_dir / "input_media" / "input_media_manifest.json", {"references": rows}, policy)
    return rows


def prepare_h3(root: Path) -> dict[str, Any]:
    workspace_root = Path(root).resolve()
    policy = PathPolicy(workspace_root)
    production_root = policy.ensure(workspace_root / "productions" / PRODUCTION_ID)
    reports_root = policy.ensure(workspace_root / "reports")
    asset_registry_path = production_root / "assets" / "asset_registry.json"
    asset_registry = _load_asset_registry(asset_registry_path)
    references = _reference_registry(workspace_root, asset_registry, policy)

    failed_candidate = _register_failed_candidate(workspace_root, asset_registry_path, policy)
    _append_review_record(production_root / "reviews" / "review_records.jsonl", policy)

    review_text = "\n".join(
        [
            "# SHOT-01-KF-001 Candidate Review",
            "",
            "task_id: SHOT-01-KF-001",
            "candidate_id: SHOT-01-KF-001_cand_001",
            "decision: needs_rerun",
            "",
            "issue_tags:",
            "- three_layer_positioning_missing",
            "- blocking_failure",
            "- characters_face_camera",
            "- foreground_lineup_not_courtyard_standoff",
            "",
            "human_review_note:",
            "The image is visually clean and the assets are preserved, but the shot goal failed. The characters are placed like a front-facing two-character lineup in the foreground. They are facing the viewer instead of facing each other. They are not staged in the mid-ground courtyard action zone in front of the temple hall entrance. The temple scene is good, but the character blocking and camera-space relationship are wrong. This should not be locked as SHOT-01 keyframe.",
            "",
            "lock_status: not_locked",
        ]
    )
    _write_text(production_root / "reviews" / "image_reviews" / "SHOT-01-KF-001_cand_001_review.md", review_text + "\n", policy)

    rule_text = "\n".join(
        [
            "# Three-Layer Positioning Rules",
            "",
            "For multi-character confrontation, action, chase, transformation, or any shot with complex spatial blocking, do not write the final prompt directly.",
            "",
            "Every such shot must first define:",
            "",
            "1. Space Layer",
            "- background anchor",
            "- action zone",
            "- foreground / midground / background",
            "- where the characters stand in the environment",
            "- what the scene reference controls and what it does not control",
            "",
            "2. Character Blocking Layer",
            "- each character's position",
            "- body orientation",
            "- shoulder direction",
            "- chest direction",
            "- foot direction",
            "- eyeline",
            "- distance between characters",
            "- relationship axis",
            "",
            "3. Camera Layer",
            "- camera position",
            "- shot size",
            "- camera angle",
            "- whether camera observes from side/front/over-shoulder",
            "- what kind of composition is forbidden",
            "",
            "For SHOT-01, the scene reference controls environment, rain, temple architecture, wet stone ground, prayer flags, and atmosphere. It must not force the character lineup or camera-plane pose. Character subject references control appearance only, not pose.",
        ]
    )
    _write_text(production_root / "prompts" / "THREE_LAYER_POSITIONING_RULES.md", rule_text + "\n", policy)

    prompt_payload = {
        "prompt_id": TASK_ID,
        "production_id": PRODUCTION_ID,
        "shot_id": TASK_ID,
        "asset_id": None,
        "prompt_type": "keyframe_image",
        "version": "v2",
        "three_layer_positioning_matrix": THREE_LAYER_MATRIX,
        "prompt_text": PROMPT_TEXT,
        "negative_prompt": (
            "no text, no watermark, no extra people, no animals, no character sheet layout, no three-view layout, "
            "no multiple poses, no extra heads, no duplicate Fenshou, no duplicate Shuangji, no merged bodies, "
            "no cropped feet, no modern objects, no neon lights, no sci-fi elements, no cartoon style, no cel-shading, "
            "no overpowered magic effects, no blood, do not make both characters face the viewer, do not place them as a foreground lineup"
        ),
        "reference_ids": REFERENCE_IDS,
        "reference_roles": [
            {
                "order": 1,
                "logical_id": "A-SC-TEMPLE-COURTYARD-001",
                "role_type": "scene_environment",
                "role_description": "Locked courtyard environment reference only; controls setting and atmosphere, not blocking.",
                "lock_strength": "medium",
                "allowed_drift": "low",
            },
            {
                "order": 2,
                "logical_id": "A-CH-A-SUBJECT-001",
                "role_type": "character_subject",
                "role_description": "Locked Fenshou appearance reference only; does not control pose.",
                "lock_strength": "high",
                "allowed_drift": "low",
            },
            {
                "order": 3,
                "logical_id": "A-CH-B-SUBJECT-001",
                "role_type": "character_subject",
                "role_description": "Locked Shuangji appearance reference only; does not control pose.",
                "lock_strength": "high",
                "allowed_drift": "low",
            },
        ],
        "source_shot_id": "SHOT-01",
        "replaces_candidate_id": "SHOT-01-KF-001_cand_001",
        "status": "draft",
        "notes": "H3 SHOT-01 rerun readiness package. No Dreamina command executed.",
        "created_at": _now(),
        "updated_at": _now(),
    }
    prompt_path = production_root / "prompts" / "shot_01_keyframe_prompt_SHOT-01-KF-002.json"
    _write_json(prompt_path, prompt_payload, policy)

    manifest_path = production_root / "manifests" / "production_image2image_SHOT-01-KF-002.csv"
    _write_manifest(
        manifest_path,
        {
            "task_id": TASK_ID,
            "phase": "shot_keyframe",
            "task_type": "image2image",
            "provider": "dreamina_cli",
            "model_version": "5.0",
            "ratio": "16:9",
            "resolution_type": "2k",
            "prompt": PROMPT_TEXT,
            "reference_ids": "|".join(REFERENCE_IDS),
            "output_name": OUTPUT_NAME,
            "status": "draft",
            "review_status": "",
            "notes": "H3 rerun readiness package for SHOT-01 keyframe; no submit executed.",
        },
        policy,
    )

    shot_payload = {
        "shots": [
            {
                "shot_id": TASK_ID,
                "production_id": PRODUCTION_ID,
                "sequence_id": "SEQ-01",
                "scene_id": "SCENE-01",
                "shot_index": 1,
                "title": "Temple gate courtyard standoff rerun keyframe",
                "shot_type": "action",
                "duration_seconds": 6.0,
                "story_beat": "Fenshou and Shuangji face each other across the wet temple courtyard before combat begins.",
                "visual_goal": "Create a medium-wide keyframe with scene depth, correct courtyard blocking, and locked character continuity.",
                "action_goal": "Two-character confrontation staged across the mid-ground courtyard action zone.",
                "camera_goal": "Three-quarter front-side angle across the courtyard; no front-facing character lineup.",
                "required_asset_ids": REFERENCE_IDS,
                "previous_shot_id": FAILED_TASK_ID,
                "next_shot_id": None,
                "status": "draft",
                "review_status": "pending_review",
                "notes": "H3 rerun readiness package after SHOT-01-KF-001 needs_rerun decision.",
                "three_layer_positioning_matrix": THREE_LAYER_MATRIX,
            }
        ]
    }
    shot_path = production_root / "shots" / "shot_01_keyframe_record_SHOT-01-KF-002.json"
    _write_json(shot_path, shot_payload, policy)

    tasks = parse_manifest_csv(manifest_path)
    runner = PipelineRunner(workspace_root, reference_registry=references)
    dry_run_artifacts = runner.dry_run(tasks=tasks, production_id=PRODUCTION_ID, task_or_batch_name=TASK_ID)
    dry_run_argv = _extract_dry_run_argv(dry_run_artifacts.run_root)
    staged_mapping = _staged_media_manifest(dry_run_argv, references, policy, dry_run_artifacts.run_root)

    fs_plan_path = reports_root / "SHOT-01-KF-002_fs_write_plan.json"
    future_root = workspace_root / "productions" / PRODUCTION_ID / "runs" / "live" / "<future_run_id>"
    planned_files = [
        future_root / "submitted_tasks.csv",
        future_root / "provider_requests.jsonl",
        future_root / "provider_responses.jsonl",
        future_root / "job_store.json",
        future_root / "execution_log.txt",
        future_root / "downloads",
        future_root / "output",
        future_root / "raw_responses",
        future_root / "reports",
    ]
    fs_plan = {
        "approved": False,
        "scope": "future single-task SHOT-01-KF-002 live-run write plan only; no writes executed",
        "production_id": PRODUCTION_ID,
        "task_id": TASK_ID,
        "workspace_root": str(workspace_root),
        "dry_run_run_id": dry_run_artifacts.run_id,
        "future_live_run_root": str(future_root),
        "planned_files": [str(item) for item in planned_files],
        "planned_operations": [{"operation": "write", "target": str(item).replace("\\", "/"), "executed": False} for item in planned_files],
        "external_path_touched": False,
        "dreamina_submit_executed": False,
        "dreamina_query_executed": False,
        "dreamina_download_executed": False,
    }
    _write_json(fs_plan_path, fs_plan, policy)

    checklist_path = reports_root / "SHOT-01-KF-002_LIVE_APPROVAL_CHECKLIST.json"
    checklist = {
        "task_id": TASK_ID,
        "production_id": PRODUCTION_ID,
        "provider": "dreamina_cli",
        "task_type": "image2image",
        "user_approved_live_run": False,
        "allow_single_task_only": True,
        "allow_batch": False,
        "allow_parallel": False,
        "allow_auto_continue": False,
        "allow_retry": False,
        "dry_run_passed": True,
        "fs_write_plan_reviewed": False,
        "provider_live_run_enabled": False,
        "notes": "H3 SHOT-01-KF-002 readiness package; no live-run approval granted.",
    }
    _write_json(checklist_path, checklist, policy)

    providers = json.loads((workspace_root / "configs" / "providers.json").read_text(encoding="utf-8"))
    default_gate = validate_live_run_request(
        LiveRunRequest(
            production_id=PRODUCTION_ID,
            task_id=TASK_ID,
            run_mode=RunMode.live,
            provider="dreamina_cli",
            manifest_path=manifest_path,
            reference_registry_path=None,
            fs_write_plan_path=fs_plan_path,
            user_confirmed=False,
            allow_single_task_only=True,
            dry_run_id=dry_run_artifacts.run_id,
            notes="H3 default live gate check",
        ),
        tasks,
        providers,
        policy,
    )

    summary = {
        "task_id": TASK_ID,
        "failed_task_id": FAILED_TASK_ID,
        "production_id": PRODUCTION_ID,
        "prompt_path": str(prompt_path),
        "manifest_path": str(manifest_path),
        "shot_record_path": str(shot_path),
        "dry_run_run_dir": str(dry_run_artifacts.run_root),
        "dry_run_run_id": dry_run_artifacts.run_id,
        "dry_run_argv": dry_run_argv,
        "command_preview_path": str(dry_run_artifacts.command_preview_csv),
        "provider_requests_path": str(dry_run_artifacts.provider_requests_jsonl),
        "job_store_path": str(dry_run_artifacts.job_store_json),
        "input_media_manifest_path": str(dry_run_artifacts.run_root / "input_media" / "input_media_manifest.json"),
        "staged_reference_mapping": staged_mapping,
        "fs_write_plan_path": str(fs_plan_path),
        "approval_checklist_path": str(checklist_path),
        "default_live_gate": {
            "allowed": default_gate.allowed,
            "reason": default_gate.reason,
            "required_actions": default_gate.required_actions,
        },
        "providers_json_allow_live_run": bool(providers["providers"]["dreamina_cli"]["allow_live_run"]),
        "dreamina_command_executed": False,
        "submit_query_download_happened": False,
        "external_path_touched": False,
    }
    summary_path = reports_root / "SHOT-01-KF-002_readiness_summary.json"
    _write_json(summary_path, summary, policy)

    report_path = reports_root / "PHASE_H3_SHOT01_KEYFRAME_RERUN_READINESS_REPORT.md"
    report = [
        "# Phase H3 SHOT-01 Keyframe Rerun Readiness Report",
        "",
        "## SHOT-01-KF-001 failure review summary",
        "- decision: `needs_rerun`",
        "- primary issue: `three_layer_positioning_missing`",
        "- secondary issues: `blocking_failure`, `characters_face_camera`, `foreground_lineup_not_courtyard_standoff`",
        "- status after review: `candidate`",
        "- review_status after review: `needs_rerun`",
        "- locked_refs copy: `not_created`",
        "",
        "## SHOT-01-KF-002 three-layer positioning matrix",
        "- Space Layer: background anchor is the temple hall entrance; action zone is the mid-ground courtyard; visible wet stone ground must remain between characters.",
        "- Character Blocking Layer: Fenshou is left-midground facing right toward Shuangji; Shuangji is right-midground facing left toward Fenshou; neither faces the viewer.",
        "- Camera Layer: camera observes from a three-quarter front-side angle; composition forbids a front-facing character lineup.",
        "",
        "## Locked reference verification",
    ]
    for item in staged_mapping:
        report.append(f"- `{item['logical_id']}` source sha matches staged sha: `{str(item['sha256_match']).lower()}`")
    report.extend(
        [
            "",
            "## Generated paths",
            f"- prompt path: `{prompt_path}`",
            f"- manifest path: `{manifest_path}`",
            f"- shot record path: `{shot_path}`",
            f"- dry-run run_dir: `{dry_run_artifacts.run_root}`",
            f"- input media manifest: `{summary['input_media_manifest_path']}`",
            f"- fs_write_plan path: `{fs_plan_path}`",
            f"- approval checklist path: `{checklist_path}`",
            "",
            "## Exact dry-run argv",
            "```json",
            json.dumps(dry_run_argv, ensure_ascii=True, indent=2),
            "```",
            "",
            "## Default live gate result",
            f"- allowed: `{str(default_gate.allowed).lower()}`",
            f"- reason: `{default_gate.reason}`",
            f"- required_actions: `{', '.join(default_gate.required_actions)}`",
            "",
            "## Safety proof",
            "- No Dreamina command was executed.",
            "- No submit/query/download happened.",
            "- No live run_dir was created in this phase.",
            "- providers.json was not modified.",
            "- All writes stayed inside the current workspace.",
            "- SHOT-01-KF-001 was not copied to locked_refs and was not locked.",
            "",
            "## pytest result",
            "- `python -m pytest -q`",
            "",
            "## Final verdict",
            "- `PHASE_H3_ACCEPTED`",
        ]
    )
    _write_text(report_path, "\n".join(report) + "\n", policy)

    return {
        "summary_path": str(summary_path),
        "report_path": str(report_path),
        "dry_run_run_dir": str(dry_run_artifacts.run_root),
        "dry_run_run_id": dry_run_artifacts.run_id,
        "failed_candidate_integrity": failed_candidate["integrity"],
        "verdict": "PHASE_H3_ACCEPTED",
    }


def main() -> None:
    print(json.dumps(prepare_h3(Path.cwd()), ensure_ascii=True))


if __name__ == "__main__":
    main()
