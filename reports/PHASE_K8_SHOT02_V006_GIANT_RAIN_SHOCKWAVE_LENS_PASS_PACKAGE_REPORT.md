# PHASE K8: SHOT-02-V006 Giant Rain Shockwave Lens Pass Image2Video Package Report

Date: 2026-06-19

## Scope

- Rank extract candidates for SHOT-02-V006 and select a preferred full-shockwave short candidate.
- Keep the original locked SHOT-02 first-clash keyframe as the only input image.
- Compare CUT01/CUT02/CUT03 segments from the same source output.
- Do not lock output, mark final master, download media, or auto-continue.
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

SHOT_02_V006_EXTRACTS_RANKED_READY

## Live Submit Record

- status: success_downloaded_review_required
- submit_id: 44bcdf99-97c9-4d62-b47d-4c623f920b91
- logid: 20260619145824169254047008114EAC2
- credit_count: 56
- command_contract_preflight: pass
- command_contract_valid: true
- first_query_status: querying
- queue_status: Finish
- query_status: success
- downloaded: true
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923/SHOT-02-V006_giant_rain_shockwave_lens_pass_motion.mp4
- file_size: 8222075
- sha256: 959fe1aeea02ce2954a5a3735010609292382a031826996bffa0ae739b20a236
- video_duration: 4.016666666666667
- resolution: 1280x720
- fps: 24.149377593360995
- frame_count: 97
- final_master: false
- locked: false
- usable_video_candidate: false
- human_review_required_after_download: true

## Human Review Extract Candidate

- status: human_review_extracts_ranked
- human_review_result: usable_extract_candidate
- source_video_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923/SHOT-02-V006_giant_rain_shockwave_lens_pass_motion.mp4
- full_clip_usable: false
- usable_video_candidate: false
- extract_candidate: true
- final_master: false
- locked: false
- recommended_extract_cut01: 2.00s-4.00s
- recommended_extract_cut02: 2.00s-3.50s
- recommended_extract_cut03: 2.00s-3.35s
- success_points: large shockwave reveal after 2.0s; wide rain curtain; camera pull-back reveal works
- remaining_issues: front section looks like water spraying from fists; pre-impact particle build-up not convincing; full 4s clip too slow
- CUT01 role: long_full_shockwave_backup
- CUT02 role: tight_impact_extract_candidate
- CUT03 role: preferred_full_shockwave_short_extract_candidate
- preferred_extract: CUT03
- preferred_extract_path: productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4
- recommended_edit_structure: 0.3-0.6s contact/hit-stop beat followed by CUT03 shockwave reveal
- recommended_current_use: prefer CUT02 for fast impact edit; CUT01/CUT03 for larger shockwave reveal
- next_recommended_action: prepare short contact/hit-stop beat if needed; otherwise preserve CUT03 as current SHOT-02 shockwave highlight candidate
- next_review_required: CUT03 human review

## Local Extract Validation

- CUT01 path: productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT01_2p00_to_4p00_giant_shockwave_extract.mp4
- CUT01 exists: true
- CUT01 file_size: 1765998
- CUT01 sha256: fa66ad03e359e017e72d4ad1e9a605807d525ecf0904c60291d9ac2e1a204eb3
- CUT01 duration: 2.028985507246377
- CUT01 resolution: 1280x720
- CUT01 fps: 24.15
- CUT01 frame_count: 49
- CUT02 path: productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT02_2p00_to_3p50_tight_shockwave_extract.mp4
- CUT02 exists: true
- CUT02 file_size: 1301713
- CUT02 sha256: 121b16c364c91b71ce3ce07fb47c7b7dca9fe339e66d004376ef62d52c18e059
- CUT02 duration: 1.5320910973084887
- CUT02 resolution: 1280x720
- CUT02 fps: 24.15
- CUT02 frame_count: 37
- CUT03 path: productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4
- CUT03 exists: true
- CUT03 file_size: 1082032
- CUT03 sha256: bbffd3551e84c54cad210674d6bb1b03f07d649e55d7f698684c94cb24702a6b
- CUT03 duration: 1.3250517598343685
- CUT03 resolution: 1280x720
- CUT03 fps: 24.15
- CUT03 frame_count: 32
- CUT03 contact_sheet: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V006_CUT03/SHOT-02-V006_CUT03_contact_sheet.jpg
