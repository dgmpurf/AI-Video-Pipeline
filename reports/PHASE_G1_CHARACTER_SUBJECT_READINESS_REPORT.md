# Phase G1 Character Subject Readiness Report

## 1) Candidate production task summary
- task_id: `A-CH-A-SUBJECT-001`
- production_id: `chi_yan_tian_qiong`
- phase: `asset_character`
- task_type: `text2image`
- provider: `dreamina_cli`
- model_version: `5.0`
- ratio: `9:16`
- resolution_type: `2k`
- reference_ids: none
- output_name: `A-CH-A-SUBJECT-001_fenshou_full_body_subject`
- this is a character subject reference, not a shot keyframe.

## 2) Prompt record path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\production_character_subject_prompt_A-CH-A-SUBJECT-001.json`

## 3) Manifest path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\manifests\production_text2image_A-CH-A-SUBJECT-001.csv`

## 4) Dry-run run_dir
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_154840_A-CH-A-SUBJECT-001`

## 5) Exact dry-run argv list
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "text2image",
  "--model_version",
  "5.0",
  "--ratio",
  "9:16",
  "--prompt",
  "A full-body front-facing character subject of Fenshou, an adult male ancient fantasy martial warrior. He has long black hair tied in a high ponytail, a stern focused expression, strong athletic build, black and dark red layered battle armor with sharp but practical metal plates, subtle crimson accents, black boots, clean readable silhouette, standing in a neutral strong pose with both feet visible, arms relaxed and fists lightly clenched, cinematic semi-realistic 3D character design, high detail, consistent proportions, plain light gray studio background, no environment, no extra people, no weapon, no text, no watermark, no character sheet layout, no three-view layout, no multiple poses, no cropped feet, no modern clothing, no sci-fi armor, no cartoon style, no cel-shading.",
  "--resolution_type",
  "2k"
]
```

## 6) command_preview path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_154840_A-CH-A-SUBJECT-001\command_preview.csv`

## 7) provider_requests path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_154840_A-CH-A-SUBJECT-001\provider_requests.jsonl`

## 8) Default live gate result
- allowed: `false`
- reason: `live-run denied by safety gate`
- required_actions: ['dreamina_cli live-run disabled by provider config', 'collect explicit user confirmation', 'complete dry-run first', 'approve fs_write_plan']

## 9) Hypothetical readiness result
- allowed: `false`
- reason: `live-run denied by safety gate`
- required_actions: ['dreamina_cli live-run disabled by provider config', 'approve fs_write_plan']

## 10) fs_write_plan path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\A-CH-A-SUBJECT-001_fs_write_plan.json`
- approved: `false`
- all planned operations executed: `false`

## 11) Approval checklist path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\A-CH-A-SUBJECT-001_LIVE_APPROVAL_CHECKLIST.json`
- user_approved_live_run: `false`
- provider_live_run_enabled: `false`

## 12) Provider config proof
- `configs/providers.json` has `dreamina_cli.allow_live_run=false`.

## 13) Safety proof
- No Dreamina submit command was executed.
- No Dreamina query_result command was executed.
- No download command was executed.
- No external path was touched.
- Dry-run was executed in workspace only.

## 14) pytest result
- pytest result: `python -m pytest -q` passed with exit code `0`.

## 15) Final verdict
- `PHASE_G1_ACCEPTED`
