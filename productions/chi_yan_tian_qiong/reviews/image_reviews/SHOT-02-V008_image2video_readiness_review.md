# SHOT-02-V008 Image2Video Readiness Review

Task: SHOT-02-V008
Shot: SHOT-02
Status: submitted_querying
Concept: aftershock_rain_recovery / rain mist settling / combatants stabilize after shockwave

## Context

- Current preferred pre-impact charge: V007_PREVIEW_C_0p50_to_1p30.
- Current preferred shockwave reveal: V006 CUT03 2p00_to_3p35.
- Current preferred combo edit candidate: C1, V007C followed by CUT03.
- Problem: the current impact beat lacks aftershock / recovery and ends abruptly.
- V008 role: create a short post-impact recovery source after CUT03.

## Input Reference

- Source video: productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4
- Derived input image: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png
- Derived frame time: selected 1.15s frame from CUT03.
- Derived ref file size: 752739 bytes.
- Derived ref sha256: 82deaa75293ae75be3bd2b4d1b2da82ce3e4f263a5380ed2ed01a4ec5b3030df.
- Commit policy: local media only; do not stage or commit unless explicitly approved later.

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
- Status: submitted_querying
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
- ratio: omitted; image2video infers ratio from input image
- image input count: exactly 1
- command_contract_valid: true

## Package Intent

- Create a CLI-legal 4-second source clip.
- Final edit should likely use only a 0.8-1.5s recovery segment.
- Show aftermath after the shockwave has passed: rain mist settling, puddle ripples, clothing/hair settling, and combatants stabilizing.
- Do not create a new shockwave, second explosion, magic ring, shield dome, or new attack.

## Readiness Checks

- Preserve ancient temple main hall frontal axis.
- Preserve wet stone courtyard, distant main hall, rainy atmosphere, water vapor, and reflections.
- Preserve two combatants only.
- Preserve the post-shockwave spatial relationship.
- Keep the motion controlled and recovery-focused.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, final_edit_target=0.8-1.5s, and command_contract_valid=true before any live submit.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V008_aftershock_rain_recovery_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V008.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V008.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V008.json
- Package report: reports/PHASE_K12_SHOT02_V008_AFTERSHOCK_RAIN_RECOVERY_PACKAGE_REPORT.md

## Risk Notes

- The model may restart the shockwave; the prompt says this is aftermath and forbids a new large shockwave.
- The model may create a shield dome or circular water curtain; both are explicitly forbidden.
- If the 4-second clip drifts, use only the best 0.8-1.5s recovery portion.
- The derived input frame is local media and should remain untracked unless explicitly approved.

## Decision

SHOT_02_V008_SUBMITTED_QUERYING

## Submit Metadata

- status: submitted_querying
- submit_id: 9c99d945-65c5-4e42-9d7a-f434313bec9a
- logid: 20260620145104169254047008671EB9D
- credit_count: 56
- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- video_resolution: 720p
- selected_start_frame_time: 1.15s
- selected_start_frame_sha256: 82deaa75293ae75be3bd2b4d1b2da82ce3e4f263a5380ed2ed01a4ec5b3030df
- command_contract_preflight: pass
- command_contract_valid: true
- submit_gen_status: querying
- first_query_status: querying
- queue_status: Generating
- fail_reason: none returned
- downloaded: false
- output_path: null
- final_master: false
- locked: false
- usable_video_candidate: false
- human_review_required_after_download: true

