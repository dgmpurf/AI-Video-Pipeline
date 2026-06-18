# SHOT-02-V003 Image2Video Readiness Review

Task: SHOT-02-V003
Shot: SHOT-02
Status: package_ready_no_submit
Concept: volumetric_rain_shell / contact-point rain-displacement shockwave

## Prior Attempt Review

- Prior task: SHOT-02-V002-CLI4
- Prior status: human_review_target_miss
- Prior technical validity: true
- Prior issue: water effect manifested mainly as ground splash / side water curtain; intended volumetric rain-shell shockwave around central contact point was not achieved.
- V002-CLI4 remains preserved as history and is not marked usable, locked, or final master.

## Source Keyframe

- Official keyframe: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Lock status: source keyframe locked as official SHOT-02 keyframe

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

- Create a CLI-legal 4-second action spectacle source from the official SHOT-02 keyframe.
- Final edit should use only the strongest 1-2 seconds.
- This is not a long slow push-in.
- This is not a new combo or second exchange.
- The visual center remains the existing central arm/fist contact point.
- The intended effect is airborne volumetric rain displacement, not ground splash.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, main hall door, stone steps, railings, rain, wet stone floor, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central close-range arm contact or near-contact point.
- Preserve separated readable bodies and grounded feet.
- Emphasize air-filled rain, rain streaks, suspended droplets, and rain mist being pushed outward from the contact point.
- Create a short-lived spherical or hemispherical rain-shell cavity.
- Keep ground ripples and puddle splashes secondary.
- Camera may react with one restrained micro-shake and slight recoil only.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, and command_contract_valid=true before any live submit.

## Forbidden-Term / Sensitive Visual Check

- 爆炸: appears only as a negative constraint, not as desired visual effect.
- 能量波: not used as desired visual effect.
- 魔法冲击: not used as desired visual effect.
- 雷电: appears only as a negative constraint, not as desired visual effect.
- 火焰: appears only as a negative constraint, not as desired visual effect.
- 武器: not used as desired visual effect.

## Risk Notes

- The locked keyframe accepted minor risks remain present as source context: chain/whip-like hand element and slight horizontal-duel tendency.
- V003 tries to correct V002-CLI4 by shifting the water effect from ground/puddle splash to airborne rain-volume displacement.
- The prompt strongly warns against side water curtains, wave-like water walls, and ground-splash dominance.
- Duration is CLI-legal but creative intent remains a 1-2 second final highlight after editing.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V003_volumetric_rain_shell_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V003.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V003.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V003.json
- Package report: reports/PHASE_K4_SHOT02_V003_VOLUMETRIC_RAIN_SHELL_PACKAGE_REPORT.md

## Decision

SHOT_02_V003_VOLUMETRIC_RAIN_SHELL_PACKAGE_READY_NO_SUBMIT
