# SHOT-01-KF-003 Branch B Package Report

## Package Result
- task_id: `SHOT-01-KF-003`
- branch: `Branch B`
- status: `draft_ready`
- needs_generation: `true`
- locked: `false`
- task_type: `image2image`
- provider: `dreamina_cli`

## Changed Files
- `productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-01_prompt_branch_review.md`
- `productions/chi_yan_tian_qiong/prompts/shot_01_keyframe_prompt_SHOT-01-KF-003.json`
- `productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-01-KF-003.csv`
- `productions/chi_yan_tian_qiong/prompts/prompt_manifest.json`
- `productions/chi_yan_tian_qiong/shots/shot_01_keyframe_record_SHOT-01-KF-003.json`
- `productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-01-KF-003_branch_b_review.md`
- `reports/SHOT-01-KF-003_BRANCH_B_PACKAGE_REPORT.md`

## Locked Reference Resolution
- `A-SC-TEMPLE-COURTYARD-001` -> `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png`
- `A-CH-A-SUBJECT-001` -> `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- `A-CH-B-SUBJECT-001` -> `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`

## Validation
- JSON artifacts loaded successfully.
- Manifest parsed successfully with project `parse_manifest_csv`.
- All three registry-resolved locked references exist.
- `python -m pytest -q`: passed.

## Safety
- No Dreamina command was executed.
- No submit/query/download happened.
- No runtime code was modified.

## Later Manual Submit Action
Run only after explicit user approval for a single `SHOT-01-KF-003` image2image submit:

```powershell
$prompt = (Get-Content -Raw "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\shot_01_keyframe_prompt_SHOT-01-KF-003.json" | ConvertFrom-Json).prompt_text
C:/Users/msjpurf/bin/dreamina.exe image2image `
  --model_version 5.0 `
  --ratio 16:9 `
  --prompt $prompt `
  --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png" `
  --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" `
  --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png" `
  --resolution_type 2k
```
