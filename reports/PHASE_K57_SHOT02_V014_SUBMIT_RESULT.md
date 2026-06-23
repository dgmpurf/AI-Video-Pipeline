# PHASE K57 - SHOT-02-V014 Submit Result

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass executed the human-approved SHOT-02-V014 live submit boundary.

Human authorization:

> 批准 V014 单次 submit。允许 Codex 先跑 Dreamina canary 和 multimodal2video command-contract preflight；通过后只 submit 一次。不要 query，不要 download，不要 retry，不要 resubmit。

Boundaries:

- Dreamina canary was run.
- multimodal2video command-contract preflight was run.
- Exactly one multimodal2video submit command was attempted.
- No query_result was run.
- No download was run.
- No retry was attempted.
- No resubmit was attempted.
- No batch command was run.
- No media was created, moved, deleted, staged, or committed.
- V013 lock state was not changed.
- V014 final_master=false.
- V014 locked=false.

## Canary Result

Result: pass

Command:

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

Submit attempted: yes, exactly once.

Result: failed before valid task creation.

Raw non-sensitive error:

```text
authsdk: refresh failed: protocol transport: do request
```

Returned task metadata:

- submit_id: none returned
- logid: none returned
- credit_count: none returned
- gen_status / queue_status / status: failed before task acceptance

Because no submit_id was returned, no valid Dreamina V014 queued task exists from this attempt.

## Boundaries Confirmed

- exactly one submit attempted
- no query_result
- no download
- no retry
- no resubmit
- no media created or staged
- V013 lock state unchanged
- V014 final_master=false
- V014 locked=false
- submit_id is not final success; in this case no submit_id was returned at all

## Next Required Step

There is no existing V014 submit_id to query.

Any future V014 submit requires explicit human approval because the authorized single submit attempt has already been used and failed before task creation.

## Final Verdict

SHOT_02_V014_SUBMIT_FAILED_NO_RETRY
