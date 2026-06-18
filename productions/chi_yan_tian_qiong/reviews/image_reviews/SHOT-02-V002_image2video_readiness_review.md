# SHOT-02-V002 Image2Video Readiness Review

Task: SHOT-02-V002
Shot: SHOT-02
Status: command_contract_invalid

## Source Keyframe

- Official keyframe: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Lock status: source keyframe locked as official SHOT-02 keyframe

## Dreamina Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 2
- duration policy: integer-based 2-second action highlight clip
- video_resolution: 720p
- ratio: omitted; image2video infers ratio from input image
- image input count: exactly 1

## Package Intent

- Create a short hit-stop rainwater reaction beat from the official SHOT-02 keyframe.
- This is not a long slow push-in.
- This is not a new combo or second exchange.
- The visual center remains the existing arm contact / near-contact point.

## Command Contract Status

- status: command_contract_invalid
- command_contract_valid: false
- invalid_reason: duration=2 is not supported by current CLI image2video seedance2.0_vip; supported range is 4-15s
- do_not_submit_via_cli: true
- manual_web_possible: true
- recommended_fix: use SHOT-02-V002-CLI4 with duration=4 for CLI, then edit down to 1-2s
- final_master: false
- locked: false
- usable_video_candidate: false
- contract audit reference: reports/PHASE_K2B_DREAMINA_CLI_EXECUTION_CONTRACT_AUDIT.md

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, main hall door, stone steps, railings, rain, wet stone floor, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central close-range arm contact or near-contact point.
- Preserve separated readable bodies and grounded feet.
- Keep motion limited to brief held pressure, physical rainwater reaction, puddle ripples, droplets, slight hair/robe/rain movement, and very light camera vibration.
- Avoid weapon wording and magical-effect wording in the prompt body.
- Do not use ratio for image2video.

## Risk Notes

- The locked keyframe accepted minor risks remain present as source context: chain/whip-like hand element and slight horizontal-duel tendency.
- The prompt avoids drawing attention to handheld objects to reduce unwanted prop emphasis.
- The 2-second duration reduces drift, fusion, extra limb, and unintended choreography risk.
- Large camera movement is avoided because SHOT-02 still depends on the frontal main-hall anchor.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V002_hitstop_rain_blast_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002.json
- Package report: reports/PHASE_K2_SHOT02_V002_HITSTOP_RAIN_BLAST_PACKAGE_REPORT.md

## Decision

SHOT_02_V002_HITSTOP_RAIN_BLAST_PACKAGE_READY_NO_SUBMIT
SHOT_02_V002_COMMAND_CONTRACT_INVALID_DO_NOT_SUBMIT_VIA_CLI
