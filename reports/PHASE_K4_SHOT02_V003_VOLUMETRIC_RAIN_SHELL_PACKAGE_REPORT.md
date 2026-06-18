# PHASE K4: SHOT-02-V003 Volumetric Rain Shell Image2Video Package Report

Date: 2026-06-18

## Scope

- Register SHOT-02-V002-CLI4 as human_review_target_miss.
- Create SHOT-02-V003 image2video package only.
- Use the locked official SHOT-02 keyframe as the only input image.
- Create a 4-second CLI-legal action spectacle source intended to be edited down to the strongest 1-2 seconds.
- Submitted to Dreamina one live task; query result was success and media downloaded for review.
- Do not modify Source files, runtime code, or configs/providers.json.

## V002-CLI4 Human Review Result

- status: human_review_target_miss
- technical_valid: true
- command_contract_valid: true
- downloaded: true
- usable_video_candidate: false
- fallback_motion_clip: false
- final_master: false
- locked: false
- human_review_result: target_miss
- target_miss_reason: water effect manifested mainly as ground splash / side water curtain; intended volumetric rain-shell shockwave around central contact point was not achieved
- next_recommended_task: SHOT-02-V003_volumetric_rain_shell

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Contract audit reference: reports/PHASE_K2B_DREAMINA_CLI_EXECUTION_CONTRACT_AUDIT.md
- Purpose: volumetric rain-displacement shockwave around the central contact point; not ground splash only.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 1-2s
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image
- command_contract_valid: true

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V003_volumetric_rain_shell_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V003.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V003.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V003.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V003_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Natural timing language: 第一秒 / 第二秒 / 第三秒 / 第四秒.
- Avoid decimal timestamp wording.
- Avoid weapon wording in the prompt body.
- Avoid treating 爆炸 / 能量波 / 魔法冲击 / 雷电 / 火焰 as desired visual effects.
- Ground the visual effect in physical air pressure, rain streak displacement, suspended droplets, rain mist, and a short-lived hemispherical rain-shell cavity.
- Emphasize airborne rain displacement over ground splash.
- Keep ground water only as secondary ripples and small support splashes.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and the command-contract preflight passes:

`powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V003_volumetric_rain_shell_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
`

## Risk Notes

- V003 may still overproduce ground water because the locked keyframe includes a wet stone floor; prompt explicitly demotes puddles to secondary support.
- Camera reaction is tightly constrained to one restrained micro-shake and slight recoil to avoid losing the main-hall axis.
- The source keyframe's accepted minor risks remain: chain/whip-like hand element and slight horizontal-duel tendency.
- Do not mark V003 usable, locked, or final master without human review after generation.

## Validation Result

Pending local validation in this package step.

## Decision

SHOT_02_V003_SUCCESS_DOWNLOADED_REVIEW_REQUIRED

## Live Submit Metadata

- submit_id: 5d8cce8c-5710-47ae-9b6b-0a189c357abc
- logid: 2026061820113916925404700857686EC
- submit/gen status: success
- query status: success
- queue_status: Finish
- command_contract_preflight: pass
- command_contract_valid: true
- first query status: success
- credit_count: 56
- downloaded: true
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V003_20260618_203419/SHOT-02-V003_volumetric_rain_shell_motion.mp4
- media_validation:
  - output_exists: true
  - size_bytes: 7947770
  - sha256: cf147b15eb48110df6c02e2316db488a83dbbb5434268a1a7439a98be4b7752a
  - duration: 4.042
  - resolution: 1280x720
  - fps: 24
  - frame_count: unavailable (ffprobe missing in environment)
- final_master: false
- locked: false
- usable_video_candidate: false
- human_review_required_after_download: true

## Local Validation Result

- productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002-CLI4.json: json_parse_pass
- productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002-CLI4.json: json_parse_pass
- productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V003.json: json_parse_pass
- productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V003.json: json_parse_pass
- productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002-CLI4.csv: csv_read_pass
- productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V003.csv: csv_read_pass
- input_image_path_exists: True
- duration_4_recorded: True
- ratio_omitted: True
- exactly_one_image_recorded: True
- command_contract_valid_true: True
- final_edit_target_1_2s: True
- forbidden_term_check: 爆炸=negative_constraint_only_count_1; 能量波=absent_or_not_used; 魔法冲击=absent_or_not_used; 雷电=negative_constraint_only_count_1; 火焰=negative_constraint_only_count_1; 武器=absent_or_not_used


## Human Review Result

- status: human_review_partial_success_stylized
- technical_valid: true
- command_contract_valid: true
- downloaded: true
- visual_direction_validated: true
- human_review_result: partial_success_stylized
- target_success_points: contact point highlight; visible spherical/hemispherical rain-shell expansion; stronger spectacle than V002-CLI4
- remaining_issues: too smooth and too shield-like; reads as transparent barrier/dome; insufficient particle rain displacement; camera reaction still weak
- stylized_alt_candidate: true
- usable_video_candidate: false
- final_master: false
- locked: false
- next_recommended_task: SHOT-02-V004_rain_pressure_shell_camera_reaction
