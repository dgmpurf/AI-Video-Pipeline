# Phase G3 Shuangji Character Subject Readiness Report

## 1) Candidate production task summary
- task_id: `A-CH-B-SUBJECT-001`
- production_id: `chi_yan_tian_qiong`
- phase: `asset_character`
- task_type: `text2image`
- provider: `dreamina_cli`
- model_version: `5.0`
- ratio: `9:16`
- resolution_type: `2k`
- output_name: `A-CH-B-SUBJECT-001_shuangji_full_body_subject`
- reference_ids: none
- this is a character subject reference, not a shot keyframe.

## 2) Prompt record path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\production_character_subject_prompt_A-CH-B-SUBJECT-001.json`

## 3) Manifest path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\manifests\production_text2image_A-CH-B-SUBJECT-001.csv`

## 4) Dry-run run_dir
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260614_051705_A-CH-B-SUBJECT-001`

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
  "A full-body front-facing character subject reference of Shuangji, an adult female ancient fantasy martial guardian with a cold calm presence. She has long silver-blue hair tied in a high ponytail, a focused elegant expression, clear facial features, slender athletic build, blue and silver layered light armor combined with flowing long robe panels, modest high-collar outfit, practical shoulder and arm guards, clean readable silhouette, standing in a neutral strong pose with both feet visible, arms relaxed at her sides, cinematic semi-realistic 3D character design, high detail, consistent proportions, plain light gray studio background, no environment, no extra people, no weapon, no text, no watermark, no character sheet layout, no three-view layout, no multiple poses, no cropped feet, no revealing outfit, no exaggerated chest armor, no modern clothing, no sci-fi armor, no cartoon style, no cel-shading.",
  "--resolution_type",
  "2k"
]
```

## 6) command_preview path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260614_051705_A-CH-B-SUBJECT-001\command_preview.csv`

## 7) provider_requests path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260614_051705_A-CH-B-SUBJECT-001\provider_requests.jsonl`

## 8) Default live gate result
- allowed: `false`
- reason: `live-run denied by safety gate: dreamina_cli live-run disabled by provider config`
- required_actions: `['dreamina_cli live-run disabled by provider config', 'approve fs_write_plan']`

## 9) Hypothetical readiness result
- allowed: `false`
- readiness package prepared: `true`
- blocked until provider live-run is explicitly enabled: `true`
- blocked until fs_write_plan is reviewed: `true`
- required_actions: `['dreamina_cli live-run disabled by provider config', 'approve fs_write_plan']`

## 10) fs_write_plan path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\A-CH-B-SUBJECT-001_fs_write_plan.json`
- approved: `false`
- all planned operations executed: `false`

## 11) Approval checklist path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\A-CH-B-SUBJECT-001_LIVE_APPROVAL_CHECKLIST.json`
- user_approved_live_run: `false`
- provider_live_run_enabled: `false`

## 12) Provider config proof
- `configs/providers.json` has `dreamina_cli.allow_live_run=false`.

## 13) Safety proof
- No Dreamina submit command was executed.
- No Dreamina query_result command was executed.
- No download command was executed.
- No external path was touched.
- `run_dir` created under workspace only.

## 14) Pytest result
- pytest result: `python -m pytest -q` passed with exit code `0`.

## 15) Final verdict
- `PHASE_G3_ACCEPTED`
