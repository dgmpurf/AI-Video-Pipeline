# Phase G2 Fenshou Subject Text2Image Live Run Report

## 1) Pre-submit check result
- result: `passed`
- checks passed: `68`

## 2) Live authorization result
- scoped one-shot authorization matched only `A-CH-A-SUBJECT-001`.
- authorization was consumed after submit.
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
  "A full-body front-facing character subject reference of Fenshou, an adult male ancient fantasy martial warrior. He has long black hair tied in a high ponytail, a stern focused expression, strong athletic build, black and dark red layered battle armor with sharp but practical metal plates, subtle crimson accents, black boots, clean readable silhouette, standing in a neutral strong pose with both feet visible, arms relaxed and fists lightly clenched, cinematic semi-realistic 3D character design, high detail, consistent proportions, plain light gray studio background, no environment, no extra people, no weapon, no text, no watermark, no character sheet layout, no three-view layout, no multiple poses, no cropped feet, no modern clothing, no sci-fi armor, no cartoon style, no cel-shading.",
  "--resolution_type",
  "2k"
]
```

## 4) submit_id / provider_task_id
- submit_id: `a97f7551-b598-4929-9314-ceac79f37f5a`
- provider_task_id: `a97f7551-b598-4929-9314-ceac79f37f5a`

## 5) Submit stdout / stderr summary
- submit returncode: `0`
- stdout summary: `{
  "submit_id": "a97f7551-b598-4929-9314-ceac79f37f5a",
  "logid": "202606140020021692540470088496361",
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
- querying_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_162002_A-CH-A-SUBJECT-001\querying_tasks.csv`
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_162002_A-CH-A-SUBJECT-001\raw_responses\query_response.json`
- next allowed action: query existing submit_id only.

## 8) Safety proof
- No batch run happened.
- No parallel run happened.
- No retry happened.
- No auto-continue happened.
- No old project path was accessed by this runner.
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_162002_A-CH-A-SUBJECT-001`
- All writes stayed inside workspace via PathPolicy.
- providers.json dreamina_cli.allow_live_run: `false`
- No locked_refs or locked_videos write was performed.
- No asset was registered or locked.

## 9) Pytest result
- `python -m pytest -q` passed with exit code `0`.

## 10) Final verdict
- `PHASE_G2_SUBMITTED_QUERYING`
