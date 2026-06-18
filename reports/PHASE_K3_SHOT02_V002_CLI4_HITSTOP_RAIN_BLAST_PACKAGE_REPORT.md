# PHASE K3: SHOT-02-V002-CLI4 Hit-Stop Rain Blast Image2Video Package Report

Date: 2026-06-18

## Scope

- Mark the old SHOT-02-V002 duration=2 CLI package as command-contract-invalid.
- Create SHOT-02-V002-CLI4 image2video package only.
- Use the locked official SHOT-02 keyframe as the only input image.
- Create a 4-second CLI-legal action highlight source intended to be edited down to the strongest 1-2 seconds.
- Do not submit, query, download, generate media, lock output, auto-continue, stage, or commit.
- Do not modify Source files, runtime code, or configs/providers.json.

## Old V002 Invalid Package Record

- Old task: SHOT-02-V002
- Old duration: 2
- Old CLI status: command_contract_invalid
- command_contract_valid: false
- invalid_reason: duration=2 is not supported by current CLI image2video seedance2.0_vip; supported range is 4-15s
- do_not_submit_via_cli: true
- manual_web_possible: true
- recommended_fix: use SHOT-02-V002-CLI4 with duration=4 for CLI, then edit down to 1-2s
- final_master: false
- locked: false
- usable_video_candidate: false
- Historical files preserved; old prompt text unchanged.

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Planning reference: reports/PHASE_K1_COMBAT_RHYTHM_AND_CAMERA_REQUIREMENTS.md
- Contract audit reference: reports/PHASE_K2B_DREAMINA_CLI_EXECUTION_CONTRACT_AUDIT.md
- Purpose: hit-stop rainwater reaction beat; not long slow push-in; not a new combo.

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

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V002-CLI4_hitstop_rain_blast_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002-CLI4.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002-CLI4.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002-CLI4.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V002-CLI4_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Natural timing language: 第一秒 / 中间两秒 / 最后一秒.
- Avoid decimal timestamp wording.
- Avoid weapon wording in the prompt body.
- Avoid magical-effect wording in the prompt body.
- Ground the visual effect in physical rainwater, droplets, puddles, ripples, and wet stone reflections.
- Keep the locked keyframe composition and two-character contact pose stable.
- Generate 4 seconds only because this is the current CLI minimum for seedance2.0_vip image2video, then edit down to 1-2 seconds.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and the command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V002-CLI4_hitstop_rain_blast_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- CLI4 should not create a new fight sequence or second exchange.
- CLI4 should not use a long slow push-in despite the 4-second CLI minimum.
- Keep camera locked or nearly locked with only very light handheld vibration.
- Preserve the main hall frontal axis because SHOT-02 continuity depends on it.
- Do not emphasize hand objects or introduce new props.
- The source keyframe's accepted minor risks remain: chain/whip-like hand element and slight horizontal-duel tendency.

## Validation Result

- JSON parse: pass
  - productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002.json
  - productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002.json
  - productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002-CLI4.json
  - productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002-CLI4.json
- Manifest CSV parse: pass
  - productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002.csv
  - task_id: SHOT-02-V002
  - status: command_contract_invalid
  - duration: 2
  - productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002-CLI4.csv
  - task_id: SHOT-02-V002-CLI4
  - status: package_ready_no_submit
  - duration: 4
- Input image path existence: pass
  - productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- CLI4 command contract field check: pass
  - duration: 4
  - ratio: omitted / null
  - image_input_count: 1
  - command_contract_valid: true
- Old V002 invalid status check: pass
  - status: command_contract_invalid
  - command_contract_valid: false
  - do_not_submit_via_cli: true
- CLI4 prompt forbidden-term check: pass
  - no forbidden prompt body terms found for: 爆炸, 能量波, 魔法冲击, 武器

## Decision

SHOT_02_V002_CLI4_PACKAGE_READY_NO_SUBMIT

## Live Query / Download Result

Date: 2026-06-18

- query_status: success
- queue_status: Finish
- submit_id: e3342ada-9805-4322-82c5-6e246ef7f834
- logid: 202606181510101692540470089439C60
- credit_count: 56
- download happened: yes
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V002-CLI4_20260618_151532
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V002-CLI4_20260618_151532/SHOT-02-V002-CLI4_hitstop_rain_blast_motion.mp4
- output filename: SHOT-02-V002-CLI4_hitstop_rain_blast_motion.mp4

## Downloaded Output Metadata

- file exists: true
- file_size: 8641277 bytes
- sha256: 03cbb462e18b15361bc8ec9015421d4a80ad574106c58658db58f91281b7bc18
- duration: 4.042 seconds
- resolution: 1280x720
- fps: 24
- frame_count: not available; ffprobe not installed in local environment
- metadata source: Dreamina query_result plus local file size/hash validation

## Status After Download

- status: success_downloaded_review_required
- review_required: true
- final_master: false
- locked: false
- usable_video_candidate: false
- no auto-continue performed
- no lock performed
- no final-master decision made

## Decision

SHOT_02_V002_CLI4_SUCCESS_DOWNLOADED_REVIEW_REQUIRED

## Human Review Target Miss

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

### Review Notes

- V002-CLI4 was technically valid and downloaded successfully.
- It missed the intended visual target.
- The result mainly produced ground-level splashing water / water curtain effects.
- The intended effect is a volumetric rain-displacement shockwave: airborne rain streaks, suspended droplets, and rain mist pushed outward into a short-lived spherical or hemispherical rain-shell cavity around the central contact point.
- Preserve V002-CLI4 as historical generated evidence; do not mark usable, locked, or final master.

### Decision

SHOT_02_V002_CLI4_HUMAN_REVIEW_TARGET_MISS
