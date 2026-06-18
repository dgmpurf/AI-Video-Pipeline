# PHASE K5: SHOT-02-V004 Rain Pressure Shell Camera Reaction Image2Video Package Report

Date: 2026-06-18

## Scope

- Mark SHOT-02-V003 as human_review_partial_success_stylized.
- Create SHOT-02-V004 image2video package only.
- Use the locked official SHOT-02 keyframe as the only input image.
- Create a 4-second CLI-legal action spectacle source intended to be edited down to the strongest 1-2 seconds.
- Do not submit, query, download, generate media, lock output, auto-continue, stage, or commit.
- Do not modify Source files, runtime code, or configs/providers.json.

## V003 Human Review Result

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

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Contract audit reference: reports/PHASE_K2B_DREAMINA_CLI_EXECUTION_CONTRACT_AUDIT.md
- Purpose: de-shielded physical rain displacement and pressure-wave camera reaction around the central contact point.

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

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V004_rain_pressure_shell_camera_reaction_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V004.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V004.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V004.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V004_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Natural timing language: 第一秒 / 第二秒前半段 / 第二秒后半段 / 第三秒 / 第四秒.
- No CLI sub-second duration changes; sub-second timing is prompt semantics only.
- Avoid desired-effect wording related to magic, energy, lightning, fire, explosion, or weapon.
- Emphasize physical rainwater, rain streaks, mist, droplets, and air-pressure reaction.
- Emphasize broken rain-particle boundary rather than smooth transparent shell.
- Camera reaction is stronger but controlled: hit-stop, short micro-shake, slight recoil, quick recovery.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and the command-contract preflight passes:

`powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V004_rain_pressure_shell_camera_reaction_prompt.txt"
dreamina image2video \
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" \
  --prompt "$prompt" \
  --model_version seedance2.0_vip \
  --duration 4 \
  --video_resolution 720p \
  --poll 0
`

## Risk Notes

- V004 may still inherit V003's shield-like interpretation because the target remains a curved rain displacement volume; prompt explicitly requires broken, irregular, particle-based rain edges.
- Stronger camera reaction may risk losing readability; prompt constrains camera to one short micro-shake, slight recoil, and quick recovery.
- The source keyframe's accepted minor risks remain: chain/whip-like hand element and slight horizontal-duel tendency.
- Do not mark V004 usable, locked, or final master without human review after generation.

## Validation Result

Pending local validation in this package step.

## Decision

SHOT_02_V004_RAIN_PRESSURE_SHELL_CAMERA_REACTION_PACKAGE_READY_NO_SUBMIT
