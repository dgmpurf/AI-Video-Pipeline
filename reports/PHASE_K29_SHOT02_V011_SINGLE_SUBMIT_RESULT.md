# PHASE K29 SHOT-02 V011 Single Submit Result

Date: 2026-06-22

## Scope

- Submit the reviewed `SHOT-02-V011` `multimodal2video` package exactly once.
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
- total_credit before submit: `2677`
- user_id: `1611200923726843`
- vip_level: `maestro`

## Command-Contract Preflight Result

Preflight passed using:

`C:\Users\msjpurf\bin\dreamina.exe multimodal2video -h`

Confirmed:

- task_type: `multimodal2video`
- model_version `seedance2.0_vip` supported
- duration range includes `4`
- video_resolution `720p` supported for `seedance2.0_vip`
- ratio `16:9` supported
- input image count: `5`
- image limit supports up to `9`
- all 5 image paths exist
- package `command_contract_valid=true`

## Exact Submit Command

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V011_multimodal_identity_locked_followup_attack_prompt.txt'
& 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V010/frame_06.jpg' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png' `
  --prompt $prompt `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --ratio '16:9' `
  --poll 0
```

## Submit Response Summary

- submit_id: `8a387d83-a9a6-453a-81be-2a8dc93f1c1c`
- logid: `202606221452501692540470086931054`
- gen_status: `querying`
- queue_status: not returned
- credit_count: `56`

## Boundaries Confirmed

- Exactly one `multimodal2video` submit was run.
- No `query_result` was run after submit.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
- `final_master=false`
- `locked=false`
- Human review is still required after a future explicit query/download step.

## Next Step

Only query existing submit_id `8a387d83-a9a6-453a-81be-2a8dc93f1c1c` after explicit user approval. Do not resubmit V011.

Final verdict: `SHOT_02_V011_SUBMITTED_QUERYING_NO_DOWNLOAD`
