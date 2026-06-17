# Phase H2 Shot-01 Keyframe Image2Image Live-run Report

## 1) Pre-submit check result
- checks passed: `71`
- result: `PASS`

## 2) Live authorization result
- scoped authorization applied to `SHOT-01-KF-001` only.
- authorization consumed after submit: `true`
- batch: `false`
- parallel: `false`
- retry: `false`
- auto_continue: `false`

## 3) Staged reference mapping
- ref_01: `A-SC-TEMPLE-COURTYARD-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\input_media\ref_01.png`
- ref_02: `A-CH-A-SUBJECT-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\input_media\ref_02.png`
- ref_03: `A-CH-B-SUBJECT-001` -> `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\input_media\ref_03.png`

## 4) Input media manifest
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\input_media\input_media_manifest.json`

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
  "Locked keyframe reference for shot SHOT-01-KF-001: a wide establishing composition of the ancient temple courtyard under light rain, wet stone ground with clear reflections, distant prayer flags moving in cool mist, and two locked character subjects standing in a stable cinematic pose with clear identity continuity.",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\20260614_064100_SHOT-01-KF-001\\input_media\\ref_01.png",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\20260614_064100_SHOT-01-KF-001\\input_media\\ref_02.png",
  "--images",
  "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\20260614_064100_SHOT-01-KF-001\\input_media\\ref_03.png",
  "--resolution_type",
  "2k"
]
```

## 6) Submit result
- submit_id: `ccff71eb-e233-4a43-8ddc-7c756d1161bf`
- provider_task_id: `ccff71eb-e233-4a43-8ddc-7c756d1161bf`
- submit stdout summary: `{ "submit_id": "ccff71eb-e233-4a43-8ddc-7c756d1161bf", "prompt": "Locked keyframe reference for shot SHOT-01-KF-001: a wide establishing composition of the ancient temple courtyard under light rain, wet stone ground with clear reflections, `
- submit stderr summary: `empty`
- credit_count: `3`
- upload warning: `false`

## 7) Query result
- query status: `querying`

## 8) Querying stop state
- querying_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\querying_tasks.csv`
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\raw_responses\query_response.json`
- next allowed action: query existing submit_id only.

## 9) Safety proof
- No batch, parallel, retry, or auto-continue action happened.
- No old project path was accessed by this H2 module.
- All writes stayed inside `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE`.
- `configs/providers.json` was not permanently enabled.

## 10) pytest result
- `python -m pytest -q passed`

## 11) Final verdict
- `PHASE_H2_SUBMITTED_QUERYING`
