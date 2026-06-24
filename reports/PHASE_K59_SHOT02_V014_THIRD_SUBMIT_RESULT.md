# PHASE K59 - SHOT-02-V014 Third Submit Result

Date: 2026-06-24
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass executed the third explicit human-authorized SHOT-02-V014 single submit attempt after main VPN recovery.

Human authorization:

> 我的主vpn好了，继续吧

Interpretation:

The human approved continuing with a V014 third single submit because the main VPN was restored.

Boundaries:

- Dreamina canary was run.
- multimodal2video command-contract preflight was run.
- Exactly one third-submit attempt was made in this phase.
- No query_result was run.
- No download was run.
- No retry was attempted.
- No resubmit was attempted.
- No batch command was run.
- No media was created, moved, deleted, staged, or committed.
- V013 lock state was not changed.
- V014 final_master=false.
- V014 locked=false.

## K57 And K58 Context

K57:

- Canary passed.
- Command-contract preflight passed.
- One submit attempted.
- Failed before valid task creation.
- Error: authsdk refresh failed / protocol transport request failure.
- No submit_id returned.

K58:

- Canary passed.
- Command-contract preflight passed.
- One submit attempted.
- Returned submit_id: 489a4946-6365-42f2-a942-bddb725ddc8d
- gen_status: fail
- Failure occurred during reference image upload to imagex.bytedanceapi.com.
- No valid queued generation was created.
- No query/download/retry/resubmit happened.

No successful queued generation exists from K57 or K58.

This K59 pass is a third explicit human-authorized single submit attempt after main VPN recovery, not an automatic retry.

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
  "total_credit": 2588,
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

Result: failed during scene reference image upload.

Returned task metadata:

- submit_id: 436fc5ef-24ed-4166-bb85-2df60c5437a5
- logid: none returned
- credit_count: none returned
- gen_status: fail
- queue_status: none returned

Raw non-sensitive error:

```text
upload resource "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png": upload image: upload phase, no file upload, please check log for more details
```

The response includes a submit_id, but the returned `gen_status=fail` means this is not a successful queued or completed generation and not final success.

## Boundaries Confirmed

- exactly one third-submit attempt in this phase
- no query_result
- no download
- no retry
- no resubmit
- no media created or staged
- V013 lock state unchanged
- V014 final_master=false
- V014 locked=false

## Next Required Step

Because the third submit returned `gen_status=fail`, no download is available from this pass.

Future actions require separate explicit human approval:

- Future query of returned submit_id `436fc5ef-24ed-4166-bb85-2df60c5437a5`, if desired, only after human approval.
- Any further submit attempt requires new human authorization.

## Final Verdict

SHOT_02_V014_THIRD_SUBMIT_FAILED_NO_RETRY
