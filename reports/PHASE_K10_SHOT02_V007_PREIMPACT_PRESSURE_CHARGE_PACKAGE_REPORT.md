# PHASE K10: SHOT-02-V007 Preimpact Pressure Charge Image2Video Package Report

Date: 2026-06-19

## Scope

- Prepare SHOT-02-V007 image2video package only.
- Do not submit Dreamina, query, download, generate media, lock, mark final master, or auto-continue.
- Do not modify Source files, runtime code, or configs/providers.json.

## Context

- SHOT-02 has a usable shockwave edit candidate:
  - TEST_B: preferred_impact_edit_candidate.
  - CUT03: preferred_full_shockwave_short_extract_candidate.
- Problem: CUT03 begins after the shockwave has already formed.
- V007 purpose: create a short pre-impact pressure build-up source clip before TEST_B / CUT03.

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Use the official locked SHOT-02 first-clash keyframe as the only input image.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 0.4-0.8s
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image
- command_contract_valid: true

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V007_preimpact_pressure_charge_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V007.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V007.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V007.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V007_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Strong but controlled.
- Build hit-stop tension and contact-point rain-particle abnormality.
- Avoid full shockwave reveal, water wall, circular large water curtain, and over-effect poster reading.
- Preserve the locked SHOT-02 keyframe composition and two-character contact relationship.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V007_preimpact_pressure_charge_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- The model may trigger the large shockwave too early; prompt says this is pre-impact only and forbids complete giant spherical shockwave.
- If the clip is too static, use only the strongest 0.4-0.8s pressure segment in edit.
- If water behavior becomes too large, reject sections that become water wall, circular large water curtain, or ground-only splash.
- The camera must remain stable enough to preserve the main-hall axis and current contact composition.

## Validation Result

- JSON parse: passed for prompt JSON and shot video record.
- CSV read: passed for image2video manifest.
- Input image path exists: true.
- duration=4 recorded: true.
- ratio omitted: true.
- image_input_count=1: true.
- command_contract_valid=true: true.
- final_edit_target=0.4-0.8s: true.

## Decision

SHOT_02_V007_PREIMPACT_PRESSURE_CHARGE_PACKAGE_READY_NO_SUBMIT
