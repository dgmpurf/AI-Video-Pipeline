# PHASE K7: SHOT-02-V005 Spherical Rain Shockwave Reveal Image2Video Package Report

Date: 2026-06-19

## Scope

- Mark SHOT-02-KF-003 as human_review_target_miss_over_effect.
- Create SHOT-02-V005 image2video package only.
- Use the original locked SHOT-02 first-clash keyframe as the only input image.
- Do not use SHOT-02-KF-003 as a video keyframe.
- Do not generate media, lock output, or auto-continue.
- Do not modify Source files, runtime code, or configs/providers.json.

## KF-003 Human Review Result

- status: human_review_target_miss_over_effect
- technical_valid: true
- command_contract_valid: true
- downloaded: true
- official_keyframe: false
- locked: false
- usable_keyframe_candidate: false
- human_review_result: target_miss_over_effect_multi_state
- target_miss_reason: multiple water spheres; central contact reads as splash; image mixes contact moment and post-impact expansion; not suitable as clean peak keyframe for frames2video
- lesson_learned: strong effect trigger words are useful, but should be used in video prompt with project anchors rather than overloading a static keyframe
- next_recommended_task: SHOT-02-V005_spherical_rain_shockwave_reveal

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Purpose: trigger a strong spherical rain shockwave in video while preserving the clean locked first-clash starting pose.

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

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V005_spherical_rain_shockwave_reveal_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V005.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V005.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V005.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V005_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Shorter and stronger than V003/V004.
- Strong effect trigger words appear early.
- Project anchors immediately follow the trigger: rainy ancient temple, Fenshou left, Shuangji right, central contact point, wuxia cinematic style.
- Camera plan: hold impact, brief shake, fast small pull-back reveal, then stabilize.
- Avoid over-explaining or long negative lists.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and the command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V005_spherical_rain_shockwave_reveal_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- Strong trigger words may again produce poster-like spectacle; V005 limits this by using the clean locked first-clash keyframe as the starting image and assigning expansion over time.
- Camera pull-back could reduce character readability; prompt constrains it to a small fast reveal and says not to pull so far that characters become unclear.
- The source keyframe's accepted minor risks remain: chain/whip-like hand element and slight horizontal-duel tendency.
- Do not mark V005 usable, final, or locked without human review after generation.

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

SHOT_02_V005_PARTIAL_SUCCESS_DIRECTION_VALIDATED

## Live Submit Record

- status: success_downloaded_review_required
- submit_id: 2af71f16-d097-4711-b28a-c34fb7d54e82
- logid: 20260619012030169254047008249ECB1
- credit_count: 56
- command_contract_preflight: pass
- command_contract_valid: true
- first_query_status: querying
- query_status: success
- queue_status: Finish
- downloaded: true
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V005_20260619_133555
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V005_20260619_133555/SHOT-02-V005_spherical_rain_shockwave_reveal_motion.mp4
- file_size: 9234307
- sha256: 5cefa6e995b48c4ad4e59e69774777c98da90e162c53092f688daf78fc2f5d03
- video_duration: 4.016666666666667
- resolution: 1280x720
- fps: 24.149377593360995
- frame_count: 97
- final_master: false
- locked: false
- usable_video_candidate: false
- human_review_required_after_download: true

## Human Review Result

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
