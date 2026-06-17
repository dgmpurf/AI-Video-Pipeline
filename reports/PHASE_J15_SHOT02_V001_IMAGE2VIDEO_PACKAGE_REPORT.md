# PHASE J15: SHOT-02-V001 Image2Video Package Report

Date: 2026-06-17

## Scope

- Create SHOT-02-V001 image2video package only.
- Use the locked official SHOT-02 keyframe as the only input image.
- Do not submit, query, download, generate media, lock output, or auto-continue to video generation.

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Purpose: stable motion extension of the first close-range contact keyframe.

## Dreamina Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 5
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V001_image2video_stable_first_clash_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V001.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V001.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V001.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V001_image2video_readiness_review.md

## Command Preview Only

Do not run this command until explicit live-submit approval is given:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V001_image2video_stable_first_clash_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 5 `
  --video_resolution 720p `
  --poll 0
```

## Decision

SHOT_02_V001_SUBMITTED_QUERYING_METADATA_RECORDED

## Submit Metadata (recorded)
- submit_id: b3c0d827-29e7-4c1c-b928-c044b765b15b
- logid: 202606172244121692540470081522881
- submit status: querying
- query status: querying
- queue status: Generating
- credit_count: 70


