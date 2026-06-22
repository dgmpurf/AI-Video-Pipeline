# PHASE K34 Shuangji Identity Anchor Single Submit Result

Date: 2026-06-22

## Scope

- Submit `A-CH-B-IDENTITY-002` exactly once.
- Do not run `query_result`.
- Do not download.
- Do not retry, resubmit, batch, logout, or relogin.
- Do not mark final master or locked.

## Canary Result

Canary passed before submit.

- Dreamina executable: `C:\Users\msjpurf\bin\dreamina.exe`
- `dreamina version`: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`
- `dreamina user_credit`: succeeded
- total_credit before submit: `2621`
- user_id: `1611200923726843`
- vip_level: `maestro`

## Command-Contract Preflight Result

Preflight passed using:

`C:\Users\msjpurf\bin\dreamina.exe image2image -h`

Confirmed:

- task_type: `image2image`
- model_version `4.7` supported
- ratio `9:16` supported
- resolution_type `2k` supported
- input image count: `1`
- input image path exists: true
- command_contract_valid: true

## Package Used

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_A-CH-B-IDENTITY-002_shuangji_female_face_upper_body_identity_anchor_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/A-CH-B-IDENTITY-002_shuangji_identity_anchor_prompt.json`
- Manifest: `productions/chi_yan_tian_qiong/manifests/production_image2image_A-CH-B-IDENTITY-002.csv`
- Asset planning record: `productions/chi_yan_tian_qiong/assets/A-CH-B-IDENTITY-002_planning_record.json`
- Input image: `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- Input image sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`

## Exact Submit Command

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_A-CH-B-IDENTITY-002_shuangji_female_face_upper_body_identity_anchor_prompt.txt"
& 'C:\Users\msjpurf\bin\dreamina.exe' image2image `
  --images "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio 9:16 `
  --resolution_type 2k `
  --poll 0
```

## Submit Response Summary

- submit_id: `cfbfaa22-2a4e-40bc-b14e-987de51c3912`
- logid: `202606221604191692540470087516BB6`
- gen_status: `querying`
- queue_status: not returned
- credit_count: `1`

## Boundary Confirmation

- Exactly one `image2image` submit was run.
- No `query_result` was run after submit.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
- `final_master=false`
- `locked=false`
- Human review is still required after a future explicit query/download step.

## Next Step

Only query existing submit_id `cfbfaa22-2a4e-40bc-b14e-987de51c3912` after explicit user approval. Do not resubmit `A-CH-B-IDENTITY-002`.

Final verdict: `SHUANGJI_IDENTITY_ANCHOR_SUBMITTED_QUERYING_NO_DOWNLOAD`
