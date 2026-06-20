# PHASE K10: SHOT-02-V007 Preimpact Pressure Charge Image2Video Package Report

Date: 2026-06-19

## Scope

- Prepare SHOT-02-V007 image2video package only.
- Do not submit Dreamina, query, download, generate media, lock, mark final master, or auto-continue.
- Do not modify Source files, runtime code, or configs/providers.json.

## Context

- SHOT-02 has a usable shockwave edit candidate:
  - TEST_B: preferred_impact_edit_candidate.
  - CUT03: preferred_full_shockwave_short_extract_candidate.
- Problem: CUT03 begins after the shockwave has already formed.
- V007 purpose: create a short pre-impact pressure build-up source clip before TEST_B / CUT03.

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Use the official locked SHOT-02 first-clash keyframe as the only input image.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 0.4-0.8s
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image
- command_contract_valid: true

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V007_preimpact_pressure_charge_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V007.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V007.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V007.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V007_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Strong but controlled.
- Build hit-stop tension and contact-point rain-particle abnormality.
- Avoid full shockwave reveal, water wall, circular large water curtain, and over-effect poster reading.
- Preserve the locked SHOT-02 keyframe composition and two-character contact relationship.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V007_preimpact_pressure_charge_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- The model may trigger the large shockwave too early; prompt says this is pre-impact only and forbids complete giant spherical shockwave.
- If the clip is too static, use only the strongest 0.4-0.8s pressure segment in edit.
- If water behavior becomes too large, reject sections that become water wall, circular large water curtain, or ground-only splash.
- The camera must remain stable enough to preserve the main-hall axis and current contact composition.

## Validation Result

- JSON parse: passed for prompt JSON and shot video record.
- CSV read: passed for image2video manifest.
- Input image path exists: true.
- duration=4 recorded: true.
- ratio omitted: true.
- image_input_count=1: true.
- command_contract_valid=true: true.
- final_edit_target=0.4-0.8s: true.

## Decision

SHOT_02_V007_COMBO_EDIT_RANKED

## Submit Metadata
- Status: human_review_combo_edit_ranked
- submit_id: e9070a25-d412-4dfc-8b3d-1d872ac7fb64
- logid: 20260619221705169254047008630EE57
- credit_count: 56
- command_contract_preflight: pass
- command_contract_valid: true
- first_query_status: querying
- queue_status: Generating
- downloaded: false
- output_path: null
- final_master: false
- locked: false
- usable_video_candidate: false
- human_review_required_after_download: true

## Query / Download Metadata
- Status: human_review_combo_edit_ranked
- query_status: success
- queue_status: Finish
- downloaded: true
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V007_20260619_222501
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V007_20260619_222501/SHOT-02-V007_preimpact_pressure_charge_motion.mp4
- file_size: 10105086
- sha256: e19fad647822f4e134833e6b46e20fdb9f6a266326fad5bf265d5a749c2b92bf
- video_duration: 4.01666666666667
- resolution: 1280x720
- fps: 24.149377593361
- frame_count: 97
- technical_valid: true
- final_master: false
- locked: false
- usable_video_candidate: false
- human_review_required_after_download: true

## Human Review / Combo Ranking
- status: human_review_combo_edit_ranked
- human_review_result: combo_edit_ranked
- V007_full_clip_usable: false
- V007_preimpact_extract_usable: true
- source_video_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V007_20260619_222501/SHOT-02-V007_preimpact_pressure_charge_motion.mp4
- source_video_sha256: e19fad647822f4e134833e6b46e20fdb9f6a266326fad5bf265d5a749c2b92bf
- source_video_duration: 4.016666666666667s
- source_video_resolution: 1280x720
- source_video_fps: 24.149377593360995
- source_video_frame_count: 97
- source_video_file_size: 10105086
- preferred_preimpact_charge: V007_PREVIEW_C_0p50_to_1p30
- preferred_preimpact_charge_path: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_C_0p50_to_1p30.mp4
- safe_preimpact_backup: V007_PREVIEW_B_0p25_to_1p05
- safe_preimpact_backup_path: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_B_0p25_to_1p05.mp4
- too_static_backup: V007_PREVIEW_A_0p00_to_0p80
- too_static_backup_path: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_A_0p00_to_0p80.mp4
- preferred_combo_edit: C1
- preferred_combo_edit_path: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-v007-combo/SHOT-02_COMBO_TEST_C1_V007C_plus_CUT03.mp4
- preferred_combo_sha256: c4d168b5dff9454a2d0af6fa0a197693a3f0bf9b06b6c20e0ae9afbca41c9342
- preferred_combo_duration: 2.125s
- safe_combo_backup: B1
- safe_combo_backup_path: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-v007-combo/SHOT-02_COMBO_TEST_B1_V007B_plus_CUT03.mp4
- safe_combo_backup_sha256: 85970fb17893278dd7494f024499b10a043c8a0ad735da40ba43226e94f8a3e9
- safe_combo_backup_duration: 2.125s
- rejected_combo: C2
- rejected_combo_path: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-v007-combo/SHOT-02_COMBO_TEST_C2_V007C_plus_TESTB.mp4
- rejected_combo_sha256: ab98b79b09835eba1281155e13ab58c196b2e6b13f65f6fa908069064da1db41
- rejected_combo_duration: 2.625s
- rejected_combo_reason: too_slow_repeated_hold
- recommended_impact_sequence: V007_PREVIEW_C_0p50_to_1p30 followed by V006 CUT03 2p00_to_3p35
- V007_R01_needed: false
- further_dreamina_generation_needed_for_preimpact: false
- final_master: false
- locked: false
- next_recommended_action: prepare SHOT-02-V008 aftershock/rain recovery planning or package

