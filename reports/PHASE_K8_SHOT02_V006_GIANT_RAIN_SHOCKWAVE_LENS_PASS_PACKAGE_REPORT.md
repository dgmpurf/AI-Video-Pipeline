# PHASE K8: SHOT-02-V006 Giant Rain Shockwave Lens Pass Image2Video Package Report

Date: 2026-06-19

## Scope

- Mark SHOT-02-V005 as human_review_partial_success_direction_validated.
- Create SHOT-02-V006 image2video package only.
- Use the original locked SHOT-02 first-clash keyframe as the only input image.
- Do not submit, query, download, generate media, lock output, auto-continue, stage, or commit.
- Do not modify Source files, runtime code, or configs/providers.json.

## V005 Human Review Result

- status: human_review_partial_success_direction_validated
- technical_valid: true
- command_contract_valid: true
- downloaded: true
- usable_reference_clip: true
- usable_video_candidate: false
- final_master: false
- locked: false
- human_review_result: partial_success_direction_validated
- success_points: spherical shockwave appears; rain/water reacts; strong-trigger prompt works; camera reveal direction partially works
- remaining_issues: shockwave too small; scale does not reach visual distance; lacks pre-impact rain-particle build-up; camera pull-back not strong enough; shockwave edge does not sweep past camera foreground
- lesson_learned: strong trigger words should remain, but V006 must add pre-impact particle build-up and larger camera pull-back reveal
- next_recommended_task: SHOT-02-V006_giant_rain_shockwave_lens_pass

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Purpose: use the clean first-clash keyframe as the stable start while increasing shockwave scale, pull-back reveal, and foreground lens-pass effect.

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

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V006_giant_rain_shockwave_lens_pass_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V006.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V006.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V006.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V006_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Short, strong, result-oriented.
- Strong effect trigger words appear early.
- Project anchors immediately follow the trigger: rainy ancient temple, Fenshou left, Shuangji right, central contact point, wuxia cinematic style.
- New emphasis: pre-impact particle build-up, giant shockwave scale, fast pull-back reveal, shockwave edge sweeping past camera foreground.
- Use only essential negative constraints.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and the command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V006_giant_rain_shockwave_lens_pass_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- The fast pull-back may reduce character readability; prompt explicitly says not to pull back so far that characters become unclear.
- The lens-pass rain curtain may become too abstract; prompt anchors it to rain droplets, water mist, and the ancient temple scene.
- Strong trigger words may produce too much spectacle; prompt keeps the effect centered on the existing contact point and forbids modern city, fist close-up, ground-only splash, and small water-ball failure modes.
- Do not mark V006 usable, final, or locked without human review after generation.

## Validation Result

- JSON parse: passed for prompt JSON and shot video record.
- CSV read: passed for image2video manifest.
- Input image path exists: true.
- duration=4 recorded: true.
- ratio omitted: true.
- image_input_count=1: true.
- command_contract_valid=true: true.
- final_edit_target=1-2s: true.

## Decision

SHOT_02_V006_GIANT_RAIN_SHOCKWAVE_LENS_PASS_PACKAGE_READY_NO_SUBMIT
