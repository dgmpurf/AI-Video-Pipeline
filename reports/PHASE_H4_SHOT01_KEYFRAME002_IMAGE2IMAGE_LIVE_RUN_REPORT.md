# Phase H4 SHOT-01-KF-002 Image2Image Live-run Report

## 1) Pre-submit check result
- checks passed: `63`
- result: `PASS`

## 2) Live authorization result
- scoped authorization applied to `SHOT-01-KF-002` only.
- authorization consumed after submit: `true`
- batch: `false`
- parallel: `false`
- retry: `false`
- auto_continue: `false`

## 3) Staged reference mapping
- ref_01: `A-SC-TEMPLE-COURTYARD-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\input_media\ref_01.png`
- ref_02: `A-CH-A-SUBJECT-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\input_media\ref_02.png`
- ref_03: `A-CH-B-SUBJECT-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\input_media\ref_03.png`

## 4) Input media manifest
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\input_media\input_media_manifest.json`

## 5) Actual submit argv list
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
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\20260614_074829_SHOT-01-KF-002\\input_media\\ref_01.png",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\20260614_074829_SHOT-01-KF-002\\input_media\\ref_02.png",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\20260614_074829_SHOT-01-KF-002\\input_media\\ref_03.png",
  "--resolution_type",
  "2k"
]
```

## 6) Submit result
- submit_id: `6530e396-3a79-44bf-8623-2bc2e6ecc12f`
- provider_task_id: `6530e396-3a79-44bf-8623-2bc2e6ecc12f`
- submit stdout summary: `{ "submit_id": "6530e396-3a79-44bf-8623-2bc2e6ecc12f", "prompt": "Reference image 1 is the locked temple courtyard environment. Use it for the ancient Chinese temple courtyard, light rain, wet reflective stone ground, dark wooden hall, dist`
- submit stderr summary: `empty`
- credit_count: `3`
- upload warning: `false`

## 7) Query result
- query status: `querying`

## 8) Querying stop state
- querying_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\querying_tasks.csv`
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\raw_responses\query_response.json`
- next allowed action: query existing submit_id only.

## 9) Safety proof
- No batch, parallel, retry, or auto-continue action happened.
- No old project path was accessed by this H4 module.
- All writes stayed inside `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE`.
- `configs/providers.json` was not permanently enabled.

## 10) pytest result
- `passed`

## 11) Final verdict
- `PHASE_H4_SUBMITTED_QUERYING`
