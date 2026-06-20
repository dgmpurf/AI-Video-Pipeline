# SHOT-02-V009 Image2Video Readiness Review

Task: SHOT-02-V009
Shot: SHOT-02
Status: package_ready_no_submit
Concept: body_footwork_reaction / stance recovery / transition to next combat beat

## Context

- Current preferred SHOT-02 impact sequence: V007C preimpact charge -> V006 CUT03 shockwave reveal -> V008B aftershock recovery.
- Current preferred full impact beat: FULL_B.
- Next missing material: body / footwork reaction and transition into the next combat beat.
- V009 is not another shockwave clip.

## Input Reference

- Source video: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-full-impact-beat/SHOT-02_FULL_TEST_B_C1_plus_V008B.mp4
- Selected input image: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_3p20s.png
- Selected frame time: 3.20s from FULL_B.
- Selected frame resolution: 1280x720.
- Selected frame file size: 730539 bytes.
- Selected frame sha256: e5aa966d0e7f99f1b09f694f6ea32792a9d07fb0bd1f17cacda50489ecb11d91.
- Backup input image: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_2p75s.png
- Backup frame sha256: 9c1754b0576baaad6b38b38a6bfb974c59c29294531e8698208be0f0ef67123a.
- Commit policy: local media only; do not stage or commit derived PNGs unless explicitly approved later.

## Start Frame Selection

- selected_start_frame_time: 3.20s
- selected_start_frame_path: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_3p20s.png
- backup_start_frame_time: 2.75s
- backup_start_frame_path: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_2p75s.png
- review_reference: reports/PHASE_K14_SHOT02_V009_START_FRAME_REVIEW.md
- review_notes: 3.20s is preferred because the spherical shockwave has mostly cleared while fighters and environment remain readable. 2.75s remains backup if a more active start is needed.

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
- Final edit will likely use only a 0.8-1.5s body/footwork reaction segment.
- Show stance recovery, body weight shift, small grounded foot sliding, hair/clothing settling, and a pause before the next exchange.
- Do not create a new shockwave, second explosion, water wall, magic ring, or full new attack.

## Readiness Checks

- Preserve ancient temple main hall frontal axis.
- Preserve wet stone courtyard, distant main hall, rainy atmosphere, mist, and reflections.
- Preserve two combatants only.
- Preserve readable bodies and grounded feet.
- Keep motion controlled, physical, and transitional.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, final_edit_target=0.8-1.5s, and command_contract_valid=true before any live submit.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V009_body_footwork_reaction_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V009.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V009.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V009.json
- Package report: reports/PHASE_K15_SHOT02_V009_BODY_FOOTWORK_REACTION_PACKAGE_REPORT.md

## Risk Notes

- The model may restart the shockwave; prompt explicitly forbids new shockwave, water wall, circular water curtain, and second explosion.
- The model may turn body recovery into a new attack; prompt limits action to recovery and setup.
- The model may drift into pose reset; prompt asks for grounded weight shift and physical continuity.
- The selected input frame is local media and should remain untracked unless explicitly approved.

## Decision

SHOT_02_V009_BODY_FOOTWORK_REACTION_PACKAGE_READY_NO_SUBMIT
