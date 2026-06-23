# PHASE K58 - SHOT-02-V014 Second Submit Result

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass executed the second explicit human-authorized SHOT-02-V014 single submit attempt after the K57 authsdk transport failure.

Human authorization:

> 批准 V014 第二次单次 submit。原因是 K57 在没有返回 submit_id 前因 authsdk transport refresh 失败，没有创建有效任务。允许 Codex 重新跑 Dreamina canary 和 multimodal2video command-contract preflight；通过后只 submit 一次。不要 query，不要 download，不要 retry，不要 resubmit。

Boundaries:

- Dreamina canary was run.
- multimodal2video command-contract preflight was run.
- Exactly one second-submit attempt was made in this phase.
- No query_result was run.
- No download was run.
- No retry was attempted.
- No resubmit was attempted.
- No batch command was run.
- No media was created, moved, deleted, staged, or committed.
- V013 lock state was not changed.
- V014 final_master=false.
- V014 locked=false.

## K57 Context

K57 result:

- Canary passed.
- Command-contract preflight passed.
- Exactly one submit was attempted.
- Submit failed before valid task creation.
- Error: `authsdk: refresh failed: protocol transport: do request`
- No submit_id, logid, or credit_count was returned.
- No valid queued Dreamina task existed from K57.
- No query/download/retry/resubmit happened.

This K58 pass is a second explicit human-authorized single submit attempt, not an automatic retry.

## Canary Result

Result: pass

Commands:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' version
& 'C:\Users\msjpurf\bin\dreamina.exe' user_credit
```

Version summary:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

User credit summary:

```json
{
  "total_credit": 2508,
  "user_id": 1611200923726843,
  "vip_level": "maestro"
}
```

No logger Access denied was observed. No login/auth failure was observed during canary.

## Command-Contract Preflight Result

Result: pass

Command checked:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video -h
```

Confirmed from local CLI help:

- task_type: multimodal2video
- image inputs are allowed and repeatable
- at least one --image or --video is required
- image count limit: <=9
- selected image count: 3
- model_version seedance2.0_vip is supported
- duration 4 is supported by the 4-15s range
- ratio 16:9 is supported
- video_resolution 720p is supported for seedance2.0_vip
- no audio/video reference is required
- all 3 reference file paths exist
- command_contract_valid=true

## Exact Reference List Used

1. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
2. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
3. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png

No V009/V010/V011/V012/V013 frames or media were used as visual references.

## Submit Command Summary

The submit command used the manual prompt file body and exactly the 3 selected image references:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V014_multimodal_legwork_hand_foot_combo_prompt.txt'
& 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png' `
  --prompt $prompt `
  --duration 4 `
  --ratio '16:9' `
  --video_resolution '720p' `
  --model_version 'seedance2.0_vip'
```

No `--poll` argument was passed.

## Submit Response Summary

Submit attempted: yes, exactly once in this phase.

Result: failed during reference image upload.

Returned task metadata:

- submit_id: 489a4946-6365-42f2-a942-bddb725ddc8d
- logid: none returned
- credit_count: none returned
- gen_status: fail
- queue_status: none returned

Raw non-sensitive error:

```text
upload resource "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png": upload image: apply phase, ApplyImageUpload: do request, Get "http://imagex.bytedanceapi.com/?Action=ApplyImageUpload&NeedFallback=true&ServiceId=tb4s082cfz&UploadNum=1&Version=2018-08-01": context deadline exceeded
```

The response includes a submit_id, but the returned `gen_status=fail` means this is not a successful queued or completed generation and not final success.

## Boundaries Confirmed

- exactly one second-submit attempt in this phase
- no query_result
- no download
- no retry
- no resubmit
- no media created or staged
- V013 lock state unchanged
- V014 final_master=false
- V014 locked=false

## Next Required Step

Because the second submit returned `gen_status=fail`, no download is available from this pass.

Future actions require separate explicit human approval:

- Future query of returned submit_id `489a4946-6365-42f2-a942-bddb725ddc8d`, if desired, only after human approval.
- Any further submit attempt requires new human authorization.

## Final Verdict

SHOT_02_V014_SECOND_SUBMIT_FAILED_NO_RETRY
