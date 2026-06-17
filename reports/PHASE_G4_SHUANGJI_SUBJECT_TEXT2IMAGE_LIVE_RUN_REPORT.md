# Phase G4 Shuangji Subject Text2Image Live Run Report

## 1) Pre-submit check result
- result: `passed`
- checks passed: `64`

## 2) Live authorization result
- scoped one-shot authorization matched only `A-CH-B-SUBJECT-001`.
- authorization consumed after submit: `true`
- batch, parallel, retry, and auto-continue remained disabled.

## 3) Actual submit argv list
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "text2image",
  "--model_version",
  "5.0",
  "--ratio",
  "9:16",
  "--prompt",
  "A full-body front-facing character subject reference of Shuangji, an adult female ancient fantasy martial guardian with a cold calm presence. She has long silver-blue hair tied in a high ponytail, a focused elegant expression, clear facial features, slender athletic build, blue and silver layered light armor combined with flowing long robe panels, modest high-collar outfit, practical shoulder and arm guards, clean readable silhouette, standing in a neutral strong pose with both feet visible, arms relaxed at her sides, cinematic semi-realistic 3D character design, high detail, consistent proportions, plain light gray studio background, no environment, no extra people, no weapon, no text, no watermark, no character sheet layout, no three-view layout, no multiple poses, no cropped feet, no revealing outfit, no exaggerated chest armor, no modern clothing, no sci-fi armor, no cartoon style, no cel-shading.",
  "--resolution_type",
  "2k"
]
```

## 4) submit_id / provider_task_id
- submit_id: `b381e6d4-c559-4689-a09c-03289ac63319`
- provider_task_id: `b381e6d4-c559-4689-a09c-03289ac63319`

## 5) Submit stdout / stderr summary
- submit returncode: `0`
- stdout summary: `{
  "submit_id": "b381e6d4-c559-4689-a09c-03289ac63319",
  "logid": "202606141352541692540470083987C46",
  "gen_status": "querying",
  "credit_count": 3
}`
- stderr summary: ``
- credit_count: `3`
- gen_status: `querying`

## 6) Query status
- query status: `querying`
- query returncode: `0`

## 7) Querying result
- querying_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_055254_A-CH-B-SUBJECT-001\querying_tasks.csv`
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_055254_A-CH-B-SUBJECT-001\raw_responses\query_response.json`
- next allowed action: query existing submit_id only.

## 8) Safety proof
- No batch run happened.
- No parallel run happened.
- No retry happened.
- No auto-continue happened.
- No old project path was accessed by this runner.
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_055254_A-CH-B-SUBJECT-001`
- All writes stayed inside workspace via PathPolicy.
- providers.json dreamina_cli.allow_live_run: `false`
- providers.json was not permanently enabled.
- No locked_refs or locked_videos write was performed.
- No asset was registered or locked.

## 9) Pytest result
- `python -m pytest -q` passed with exit code `0`.

## 10) Final verdict
- `PHASE_G4_SUBMITTED_QUERYING`
