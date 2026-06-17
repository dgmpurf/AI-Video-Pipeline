# Phase F5 Production Text2Image Readiness Report

## 1) Candidate production task summary
- task_id: `A-SC-TEMPLE-COURTYARD-001`
- production_id: `chi_yan_tian_qiong`
- phase: `asset_scene`
- task_type: `text2image`
- provider: `dreamina_cli`
- model_version: `5.0`
- ratio: `16:9`
- resolution_type: `2k`
- output_name: `A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard`
- reference_ids: none
- This is a scene asset, not a shot keyframe.

## 2) Prompt record path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-001.json`

## 3) Manifest path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\manifests\production_text2image_A-SC-TEMPLE-COURTYARD-001.csv`

## 4) Dry-run run_dir
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_143007_A-SC-TEMPLE-COURTYARD-001`

## 5) Exact dry-run argv list
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "text2image",
  "--model_version",
  "5.0",
  "--ratio",
  "16:9",
  "--prompt",
  "A cinematic semi-realistic 3D ancient Chinese temple courtyard in light rain, wet stone ground with clear reflections, dark wooden main hall in the background, distant bell tower, hanging prayer flags moving slightly in misty wind, cool blue-gray atmosphere, low saturation, subtle ink-wash mood, deep spatial perspective, no characters, no animals, no text, no watermark, no modern objects, no neon lights, no sci-fi elements.",
  "--resolution_type",
  "2k"
]
```

## 6) command_preview path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_143007_A-SC-TEMPLE-COURTYARD-001\command_preview.csv`

## 7) provider_requests path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_143007_A-SC-TEMPLE-COURTYARD-001\provider_requests.jsonl`

## 8) Default live gate result
- allowed: `false`
- reason: `live-run denied by safety gate`
- required_actions: `['dreamina_cli live-run disabled by provider config', 'approve fs_write_plan']`

## 9) Hypothetical readiness result
- allowed: `false`
- readiness package prepared: `true`
- blocked until provider live-run is explicitly enabled in a later approval phase: `true`
- blocked until fs_write_plan is reviewed and approved in a later approval phase: `true`
- required_actions: `['dreamina_cli live-run disabled by provider config', 'approve fs_write_plan']`

## 10) fs_write_plan path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\A-SC-TEMPLE-COURTYARD-001_fs_write_plan.json`
- approved: `false`
- all planned operations executed: `false`

## 11) Approval checklist path
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\A-SC-TEMPLE-COURTYARD-001_LIVE_APPROVAL_CHECKLIST.json`
- user_approved_live_run: `false`
- provider_live_run_enabled: `false`

## 12) Provider config proof
- `configs/providers.json` has `dreamina_cli.allow_live_run=false`.

## 13) Safety proof
- No Dreamina submit command was executed.
- No Dreamina query_result command was executed.
- No download command was executed.
- No external path was touched.
- No live run directory was created.
- No old project was accessed.

## 14) Pytest result
- Result: passed with exit code 0.

## 15) Final verdict
- `PHASE_F5_ACCEPTED`

