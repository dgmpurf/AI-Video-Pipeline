# SHOT-02-V004 Image2Video Readiness Review

Task: SHOT-02-V004
Shot: SHOT-02
Status: package_ready_no_submit
Concept: rain_pressure_shell_camera_reaction / de-shielded volumetric rain displacement

## Prior Attempt Review

- Prior task: SHOT-02-V003
- Prior status: human_review_partial_success_stylized
- Prior technical validity: true
- Prior success: contact point highlight; visible spherical/hemispherical rain-shell expansion; stronger spectacle than V002-CLI4.
- Remaining issues: too smooth and too shield-like; reads as transparent barrier/dome; insufficient particle rain displacement; camera reaction still weak.
- V003 remains preserved as history and is not marked usable, locked, or final master.

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
- Reduce V003's smooth shield / dome reading.
- Emphasize physical rain-particle displacement, irregular rain-line boundaries, suspended droplets, mist, and pressure-wave camera reaction.
- This is not a long slow push-in and not a new combo.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, main hall door, stone steps, railings, rain, wet stone floor, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central close-range arm contact or near-contact point.
- Preserve separated readable bodies and grounded feet.
- Keep the visual origin at the central contact point, not the ground.
- Make the boundary broken, irregular, particle-like, and rain-line based, not smooth transparent shell-like.
- Camera may react with controlled hit-stop, short micro-shake, slight recoil, and quick recovery only.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, and command_contract_valid=true before any live submit.

## Forbidden-Term / Sensitive Visual Check

- magic/energy/lightning/fire/explosion/weapon wording is not used as desired effect.
- 魔法 / 能量 / 雷电 / 火焰 / 爆炸 / 武器 equivalents appear only as negative constraints or are absent from desired visual instructions.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V004_rain_pressure_shell_camera_reaction_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V004.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V004.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V004.json
- Package report: reports/PHASE_K5_SHOT02_V004_RAIN_PRESSURE_SHELL_CAMERA_REACTION_PACKAGE_REPORT.md

## Decision

SHOT_02_V004_RAIN_PRESSURE_SHELL_CAMERA_REACTION_PACKAGE_READY_NO_SUBMIT
