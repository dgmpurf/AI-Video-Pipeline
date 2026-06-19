# SHOT-02-V006 Image2Video Readiness Review

Task: SHOT-02-V006
Shot: SHOT-02
Status: submitted_querying
Concept: giant_rain_shockwave_lens_pass / large spherical shockwave pull-back reveal / rain curtain sweeps past camera

## Prior Attempt Review

- Prior task: SHOT-02-V005
- Prior status: human_review_partial_success_direction_validated
- Technical validity: true
- Useful direction: visible spherical shockwave, rain/water reaction, strong-trigger prompt works, camera reveal direction partially works.
- Remaining issues: shockwave too small; scale does not reach visual distance; lacks pre-impact rain-particle build-up; camera pull-back not strong enough; shockwave edge does not sweep past camera foreground.
- Strategy change: keep strong trigger words, add pre-impact particle build-up, larger shockwave scale, stronger pull-back reveal, and lens-foreground rain curtain pass.

## Source Keyframe

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Use the original locked SHOT-02 first-clash keyframe as the clean start.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 1-2s
- video_resolution: 720p
- ratio: omitted; image2video infers ratio from input image
- image input count: exactly 1
- command_contract_valid: true

## Package Intent

- Create a CLI-legal 4-second action highlight source from the official SHOT-02 keyframe.
- Final edit should use only the strongest 1-2 seconds.
- Show pre-impact rain-line bending and suspended particle build-up before the shockwave.
- Make the shockwave much larger than V005 and reveal it with a faster pull-back.
- Make the outer shockwave edge sweep past the camera foreground like a rain curtain.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, wet stone courtyard, main hall door, stone steps, rain, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central fist/palm or arm contact point.
- Main effect originates from the central contact point, not the ground or feet.
- Shockwave scale should expand toward frame edges and foreground lens edge.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, final_edit_target=1-2s, and command_contract_valid=true before any live submit.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V006_giant_rain_shockwave_lens_pass_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V006.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V006.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V006.json
- Package report: reports/PHASE_K8_SHOT02_V006_GIANT_RAIN_SHOCKWAVE_LENS_PASS_PACKAGE_REPORT.md

## Decision

SHOT_02_V006_SUBMITTED_QUERYING

## Live Submit Record

- status=submitted_querying
- submit_id=44bcdf99-97c9-4d62-b47d-4c623f920b91
- logid=20260619145824169254047008114EAC2
- credit_count=56
- command_contract_preflight=pass
- command_contract_valid=true
- first_query_status=querying
- queue_status=Generating
- downloaded=false
- output_path=null
- final_master=false
- locked=false
- usable_video_candidate=false
- human_review_required_after_download=true
