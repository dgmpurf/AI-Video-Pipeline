# SHOT-02-V002-CLI4 Image2Video Readiness Review

Task: SHOT-02-V002-CLI4
Shot: SHOT-02
Status: package_ready_no_submit

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

- Create a CLI-legal 4-second action highlight source from the official SHOT-02 keyframe.
- Final edit should use only the strongest 1-2 seconds.
- This is not a long slow push-in.
- This is not a new combo or second exchange.
- The visual center remains the existing arm contact / near-contact point.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, main hall door, stone steps, railings, rain, wet stone floor, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central close-range arm contact or near-contact point.
- Preserve separated readable bodies and grounded feet.
- Keep motion limited to brief held pressure, physical rainwater reaction, puddle ripples, droplets, slight hair/robe/rain movement, and very light camera vibration.
- Avoid weapon wording and magical-effect wording in the prompt body.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, and command_contract_valid=true before any live submit.

## Risk Notes

- The locked keyframe accepted minor risks remain present as source context: chain/whip-like hand element and slight horizontal-duel tendency.
- The prompt avoids drawing attention to handheld objects to reduce unwanted prop emphasis.
- Duration is CLI-legal but creative intent remains a 1-2 second final highlight after editing.
- Large camera movement is avoided because SHOT-02 still depends on the frontal main-hall anchor.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V002-CLI4_hitstop_rain_blast_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002-CLI4.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002-CLI4.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002-CLI4.json
- Package report: reports/PHASE_K3_SHOT02_V002_CLI4_HITSTOP_RAIN_BLAST_PACKAGE_REPORT.md

## Decision

SHOT_02_V002_CLI4_PACKAGE_READY_NO_SUBMIT
