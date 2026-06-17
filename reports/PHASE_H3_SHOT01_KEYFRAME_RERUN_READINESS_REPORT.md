# Phase H3 SHOT-01 Keyframe Rerun Readiness Report

## SHOT-01-KF-001 failure review summary
- decision: `needs_rerun`
- primary issue: `three_layer_positioning_missing`
- secondary issues: `blocking_failure`, `characters_face_camera`, `foreground_lineup_not_courtyard_standoff`
- status after review: `candidate`
- review_status after review: `needs_rerun`
- locked_refs copy: `not_created`

## SHOT-01-KF-002 three-layer positioning matrix
- Space Layer: background anchor is the temple hall entrance; action zone is the mid-ground courtyard; visible wet stone ground must remain between characters.
- Character Blocking Layer: Fenshou is left-midground facing right toward Shuangji; Shuangji is right-midground facing left toward Fenshou; neither faces the viewer.
- Camera Layer: camera observes from a three-quarter front-side angle; composition forbids a front-facing character lineup.

## Locked reference verification
- `A-SC-TEMPLE-COURTYARD-001` source sha matches staged sha: `true`
- `A-CH-A-SUBJECT-001` source sha matches staged sha: `true`
- `A-CH-B-SUBJECT-001` source sha matches staged sha: `true`

## Staged reference mapping
- Reference 1: `A-SC-TEMPLE-COURTYARD-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\staging\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard_f5ff8003157b.png`
- Reference 2: `A-CH-A-SUBJECT-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\staging\A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject_83e21fe549d7.png`
- Reference 3: `A-CH-B-SUBJECT-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\staging\A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject_f5c4f29083d9.png`

## Generated paths
- prompt path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\shot_01_keyframe_prompt_SHOT-01-KF-002.json`
- manifest path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\manifests\production_image2image_SHOT-01-KF-002.csv`
- shot record path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\shots\shot_01_keyframe_record_SHOT-01-KF-002.json`
- dry-run run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260614_073206_SHOT-01-KF-002`
- input media manifest: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260614_073206_SHOT-01-KF-002\input_media\input_media_manifest.json`
- fs_write_plan path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\SHOT-01-KF-002_fs_write_plan.json`
- approval checklist path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\SHOT-01-KF-002_LIVE_APPROVAL_CHECKLIST.json`

## Exact dry-run argv
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "image2image",
  "--model_version",
  "5.0",
  "--ratio",
  "16:9",
  "--prompt",
  "Reference image 1 is the locked temple courtyard environment. Use it for the ancient Chinese temple courtyard, light rain, wet reflective stone ground, dark wooden hall, distant tower, prayer flags, cool blue-gray mist, and cinematic spatial depth. Do not copy its camera angle as a rigid layout. Use it as environment identity and atmosphere.\n\nReference image 2 is the locked Fenshou full-body subject. Use it for Fenshou's appearance: black high ponytail, stern male face, strong athletic build, black and dark red layered battle armor, boots, and cold martial presence. Do not copy the neutral front-facing pose from the subject reference.\n\nReference image 3 is the locked Shuangji full-body subject. Use it for Shuangji's appearance: silver-blue high ponytail, calm cold face, blue-silver light armor, long robe silhouette, modest high-collar outfit, and restrained guardian presence. Do not copy the neutral front-facing pose from the subject reference.\n\nCreate a cinematic semi-realistic 3D keyframe for SHOT-01: the first confrontation in the rain-soaked temple courtyard.\n\nThe main temple hall entrance is the background anchor. Fenshou and Shuangji stand in the mid-ground action zone of the courtyard, in front of the temple hall entrance, not close to the camera.\n\nFenshou stands in the left-midground courtyard area, body turned three-quarter toward the right. His shoulders, chest, feet, and eyes point toward Shuangji.\n\nShuangji stands in the right-midground courtyard area, body turned three-quarter toward the left. Her shoulders, chest, feet, and eyes point toward Fenshou.\n\nThey form a clear diagonal confrontation axis across the wet stone courtyard. There is visible open wet stone ground between them for future combat movement.\n\nThe camera observes from a three-quarter front-side angle across the courtyard. It is not a front-facing character lineup. It is not a two-character poster. The shot should feel like a real film scene with spatial blocking.\n\nRain falls through the scene. Prayer flags move slightly in the wind. The wet ground reflects the characters and temple architecture. Mist softens the background. The image should preserve the locked character designs and the locked temple atmosphere.\n\nStyle: cinematic semi-realistic 3D wuxia fantasy, cool blue-gray atmosphere, low saturation, subtle ink-wash mood, detailed but not over-cluttered.\n\nRestrictions: no text, no watermark, no extra people, no animals, no character sheet layout, no three-view layout, no multiple poses, no extra heads, no duplicate Fenshou, no duplicate Shuangji, no merged bodies, no cropped feet, no modern objects, no neon lights, no sci-fi elements, no cartoon style, no cel-shading, no overpowered magic effects, no blood, do not make both characters face the viewer, do not place them as a foreground lineup, do not paste them onto the camera plane.",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard_f5ff8003157b.png",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject_83e21fe549d7.png",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject_f5c4f29083d9.png",
  "--resolution_type",
  "2k"
]
```

## Default live gate result
- allowed: `false`
- reason: `live-run denied by safety gate`
- required_actions: `dreamina_cli live-run disabled by provider config, collect explicit user confirmation, approve fs_write_plan, stage media before live-run`

## Safety proof
- No Dreamina command was executed.
- No submit/query/download happened.
- No live run_dir was created in this phase.
- providers.json was not modified.
- All writes stayed inside the current workspace.
- SHOT-01-KF-001 was not copied to locked_refs and was not locked.

## pytest result
- `python -m pytest -q`
- result: `passed`

## Final verdict
- `PHASE_H3_ACCEPTED`
