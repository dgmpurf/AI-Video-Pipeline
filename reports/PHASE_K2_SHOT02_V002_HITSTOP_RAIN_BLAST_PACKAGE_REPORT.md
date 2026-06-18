# PHASE K2: SHOT-02-V002 Hit-Stop Rain Blast Image2Video Package Report

Date: 2026-06-18

## Scope

- Create SHOT-02-V002 image2video package only.
- Use the locked official SHOT-02 keyframe as the only input image.
- Create a short 2-second action highlight clip centered on the existing arm contact / near-contact point.
- Do not submit, query, download, generate media, lock output, or auto-continue.
- Do not modify Source files, runtime code, or configs/providers.json.

## Input

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source: SHOT-02-KF-002-R02_safe
- Planning reference: reports/PHASE_K1_COMBAT_RHYTHM_AND_CAMERA_REQUIREMENTS.md
- Purpose: hit-stop rainwater reaction beat; not long slow push-in; not a new combo.

## Dreamina Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 2
- duration policy: integer-based 2-second action highlight clip
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image

## Command Contract Re-Audit

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
- historical note: the old duration=2 prompt/package is preserved, but it must not be submitted through the current CLI image2video path.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V002_hitstop_rain_blast_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V002_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Natural timing language: 前半秒 / 中间一秒 / 最后半秒.
- Avoid decimal timestamp wording.
- Avoid weapon wording in the prompt body.
- Avoid magical-effect wording in the prompt body.
- Ground the visual effect in physical rainwater, droplets, puddles, ripples, and wet stone reflections.
- Keep the locked keyframe composition and two-character contact pose stable.

## Command Preview Only

Historical command preview only. Do not run this command via current CLI because duration=2 is command-contract-invalid:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V002_hitstop_rain_blast_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 2 `
  --video_resolution 720p `
  --poll 0
```

## Risk Notes

- V002 should not create a new fight sequence or second exchange.
- V002 should not use a long slow push-in.
- Keep camera locked or nearly locked with only very light handheld vibration.
- Preserve the main hall frontal axis because SHOT-02 continuity depends on it.
- Do not emphasize hand objects or introduce new props.
- The source keyframe's accepted minor risks remain: chain/whip-like hand element and slight horizontal-duel tendency.

## Validation Result

- JSON parse: pass
  - productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V002.json
  - productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V002.json
- Manifest CSV parse: pass
  - productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V002.csv
  - task_id: SHOT-02-V002
  - duration: 2
- Input image path existence: pass
  - productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Prompt forbidden-term check: pass
  - no forbidden prompt body terms found for: 爆炸, 能量波, 魔法冲击, 武器

## Decision

SHOT_02_V002_HITSTOP_RAIN_BLAST_PACKAGE_READY_NO_SUBMIT
SHOT_02_V002_COMMAND_CONTRACT_INVALID_DO_NOT_SUBMIT_VIA_CLI
