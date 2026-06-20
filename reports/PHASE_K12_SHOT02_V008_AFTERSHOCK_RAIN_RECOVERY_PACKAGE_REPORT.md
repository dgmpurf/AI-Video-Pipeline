# PHASE K12: SHOT-02-V008 Aftershock Rain Recovery Image2Video Package Report

Date: 2026-06-20

## Scope

- Prepare SHOT-02-V008 image2video package only.
- Do not submit Dreamina, query, download, generate AI media, lock, mark final master, or auto-continue.
- Do not modify Source files, runtime code, or configs/providers.json.

## Context

- SHOT-02 currently has a preferred impact sequence:
  - V007_PREVIEW_C_0p50_to_1p30: preferred pre-impact charge.
  - V006 CUT03 2p00_to_3p35: preferred full-shockwave reveal.
  - C1: preferred combo edit candidate, V007C followed by CUT03.
- Problem: the current impact beat has pre-impact and explosion, but lacks aftershock / recovery.
- V008 purpose: create a short post-impact clip after CUT03 so the sequence does not end abruptly.

## Input Reference

- Source video: productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4
- Derived input image: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png
- Derived frame time: selected 1.15s frame from CUT03.
- Derived ref file size: 752739 bytes.
- Derived ref sha256: 82deaa75293ae75be3bd2b4d1b2da82ce3e4f263a5380ed2ed01a4ec5b3030df.
- Derived ref policy: local media only; do not stage or commit unless explicitly approved later.

## Start Frame Selection

- selected_start_frame_time: 1.15s
- selected_start_frame_path: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png
- selected_start_frame_resolution: 1280x720
- selected_start_frame_file_size: 752739
- selected_start_frame_sha256: 82deaa75293ae75be3bd2b4d1b2da82ce3e4f263a5380ed2ed01a4ec5b3030df
- backup_start_frame_time: 1.20s
- backup_start_frame_path: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p20s.png
- backup_start_frame_sha256: aa50b6e53fad45c5b8c1d90d1f74ef1751201b5aae5c0f056cd1ade23062b4ba
- review_notes: 1.15s is the preferred V008 start frame. 1.20s remains acceptable backup. 0.95s and 1.05s are slightly too early / still feel like shockwave continuation. 1.30s is usable but slightly too settled and has less aftershock energy.
- status: package_ready_no_submit
- command_contract_valid: true
- duration: 4
- video_resolution: 720p
- ratio_omitted: true
- exactly_one_image: true
- final_edit_target: 0.8-1.5s
- final_master: false
- locked: false
## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 0.8-1.5s
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image
- command_contract_valid: true

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V008_aftershock_rain_recovery_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V008.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V008.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V008.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V008_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Controlled, cinematic, low-action recovery.
- Keep ancient temple frontal axis, rainy courtyard, rain mist, water vapor, and character positions.
- Show aftermath after the shockwave has passed, not another shockwave.
- Forbid new large shockwave, second explosion, circular water curtain, shield dome, water wall, extra people, duplicated characters, body fusion, extra limbs, scene change, close-up, and watermark.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V008_aftershock_rain_recovery_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- The model may restart the shockwave; prompt says the shockwave has already passed.
- The model may make a shield-like dome or new circular water curtain; both are forbidden.
- If the clip drifts, use only the strongest 0.8-1.5s recovery segment.
- The derived frame is local media and should remain untracked unless later explicitly approved.

## Validation Result

- JSON parse: passed for prompt JSON and shot video record.
- CSV read: passed for image2video manifest.
- Derived input image path exists: true.
- duration=4 recorded: true.
- ratio omitted: true.
- image_input_count=1: true.
- command_contract_valid=true: true.
- final_edit_target=0.8-1.5s: true.

## Decision

SHOT_02_V008_AFTERSHOCK_RAIN_RECOVERY_PACKAGE_READY_NO_SUBMIT

