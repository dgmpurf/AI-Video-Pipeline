# SHOT-02-V007 Image2Video Readiness Review

Task: SHOT-02-V007
Shot: SHOT-02
Status: submitted_querying
Concept: preimpact_pressure_charge / contact-point rain-particle build-up / hit-stop tension before shockwave

## Context

- Current preferred impact edit: TEST_B.
- Current preferred full shockwave short extract: CUT03.
- Problem: CUT03 begins after the shockwave has already formed.
- V007 role: create a short pre-impact pressure build-up source before TEST_B / CUT03.
- This package must not create the large shockwave reveal.

## Source Keyframe

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Use the official locked SHOT-02 first-clash keyframe as the only image input.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 0.4-0.8s
- video_resolution: 720p
- ratio: omitted; image2video infers ratio from input image
- image input count: exactly 1
- command_contract_valid: true

## Package Intent

- Create a CLI-legal 4-second source clip.
- Final edit should only use a very short 0.4-0.8s segment.
- Show the moment before the shockwave: hit-stop, pressure accumulating, rain and droplets behaving abnormally.
- Keep the large shockwave absent; this is the pressure charge, not the release.

## Readiness Checks

- Preserve locked keyframe composition.
- Preserve frontal main-hall axis, wet stone courtyard, rain, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve one central fist/palm or arm contact point.
- Bodies remain separated and readable.
- Feet remain planted on wet stone.
- No complete giant spherical shockwave.
- No circular large water curtain.
- No ground-only splash.
- No second exchange.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, final_edit_target=0.4-0.8s, and command_contract_valid=true before any live submit.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V007_preimpact_pressure_charge_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V007.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V007.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V007.json
- Package report: reports/PHASE_K10_SHOT02_V007_PREIMPACT_PRESSURE_CHARGE_PACKAGE_REPORT.md

## Risk Notes

- The model may trigger the large shockwave too early; prompt repeatedly constrains this as pre-impact only.
- If the clip is too static, only the strongest 0.4-0.8s segment should be used.
- Water effects must remain small and centered around the contact point.
- Camera movement must stay restrained to preserve the locked composition.

## Decision

SHOT_02_V007_PREIMPACT_PRESSURE_CHARGE_SUBMITTED_QUERYING

## Submit Metadata
- status: submitted_querying
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
