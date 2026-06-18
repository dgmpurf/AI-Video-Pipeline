# PHASE K6: SHOT-02-KF-003 Peak Spherical Rain Shockwave Image2Image Package Report

Date: 2026-06-18

## Scope

- Create SHOT-02-KF-003 image2image package only.
- Build a peak-impact keyframe from the official locked SHOT-02 keyframe.
- Do not submit Dreamina.
- Do not query, download, batch, retry, generate media, lock output, or auto-continue.
- Preserve all SHOT-02-KF-002 / V003 / V004 history.

## Goal

Create a peak-impact SHOT-02 keyframe: Fenshou and Shuangji collide at the central contact point, and a large spherical shockwave pushes heavy rain outward into a circular rain curtain.

## References

- Primary composition/reference image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Optional effect reference source: manual_imports/effect_refs/jimeng_spherical_shockwave_example.mp4
- Optional effect reference present locally: false
- Effect reference still extracted: false
- Effect reference still used: false

The optional effect reference video was not present locally at package time, so no still was extracted. The locked SHOT-02 keyframe remains the only image reference and the primary scene, character, and composition anchor.

## Dreamina Settings

- task_type: image2image
- provider: dreamina_cli
- model_version: 4.7
- ratio: 16:9
- resolution_type: 2k
- image input count: 1
- poll: 0 when submitted later

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-003_peak_spherical_rain_shockwave_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-003.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-003.csv
- Shot record: productions/chi_yan_tian_qiong/shots/shot_02_keyframe_record_SHOT-02-KF-003.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-KF-003_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Short, direct, result-oriented wording.
- No previous long over-explained prompt structure.
- Preserve the official locked SHOT-02 keyframe as the composition anchor.
- Emphasize a complete spherical shockwave and circular rain curtain originating from the central arm/fist contact point.
- Avoid making the effect only ground splash or foot-level water.

## Command Preview Only

Do not run this command until explicit live-submit approval is given:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-003_peak_spherical_rain_shockwave_prompt.txt"
dreamina image2image `
  --images "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio 16:9 `
  --resolution_type 2k `
  --poll 0
```

## Submission State

- status: success_downloaded_review_required
- submit_id: 1065e52f-abd8-4c97-a1d5-dd289906b7b1
- logid: 202606190009131692540470083719378
- credit_count: 1
- command_contract_valid: true
- first_query_status: success
- queue_status: Finish
- downloaded: true
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-003_20260619_004518
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-003_20260619_004518/SHOT-02-KF-003_peak_spherical_rain_shockwave.png
- output_dimensions: 2560x1440
- output_size_bytes: 5051484
- output_sha256: 5D5D25B6398071E17DD1CD9E9E69961A1132E133BB79DF298D37CCBB07B08CFD
- official_keyframe: false
- locked: false
- human_review_required_after_download: true

## Risk Notes

- The prompt asks for a large spherical rain shockwave, which may still read as a stylized water ring or shield; human review is required after generation.
- The official keyframe has accepted minor risks: chain/whip-like hand element and slight horizontal-duel tendency.
- Because the optional effect reference video is absent, this package has no external effect still to guide the exact spherical rain-shell shape.
- Do not lock or mark as preferred/final without human review.

## Human Review Result

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

## Validation Result

- JSON parse: passed for prompt JSON and shot record.
- CSV read: passed for image2image manifest.
- Primary input image path exists: true.
- Optional effect reference path exists: false.
- Effect reference used: false.
- Output file exists: true.
- Downloaded output size: 5051484.
- Downloaded output sha256: 5D5D25B6398071E17DD1CD9E9E69961A1132E133BB79DF298D37CCBB07B08CFD.
- Downloaded output dimensions: 2560x1440.

## Decision

SHOT_02_KF_003_HUMAN_REVIEW_TARGET_MISS_OVER_EFFECT

