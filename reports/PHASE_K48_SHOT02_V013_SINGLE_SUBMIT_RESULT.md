# PHASE K48 SHOT-02 V013 Single Submit Result

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This report records the single approved Dreamina multimodal2video submit for SHOT-02-V013.

Boundaries:

- Exactly one submit was run.
- No query_result was run.
- No download was run.
- No retry, resubmit, or batch action happened.
- No prompt text was changed.
- No V009/V010/V011/V012 frames were added.
- No V012 cut/speed frames were added.
- final_master=false.
- locked=false.
- Human review is still required after any future download.

## Canary Result

Canary status: ok

Dreamina version:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

Dreamina user_credit:

```json
{
  "total_credit": 2564,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

## Command-Contract Preflight Result

Preflight status: passed

Checked command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video -h
```

Confirmed from local help:

- task_type: multimodal2video
- model_version includes seedance2.0_vip
- duration supported range: 4-15s
- video_resolution for seedance2.0_vip: 720p or 1080p
- ratio supports 16:9
- input images are accepted through repeated --image
- image input limit allows 3 images

Package preflight:

- input image count=3
- all 3 image paths exist
- no V009/V010/V011/V012 frame path included
- no V012 cut/speed test path included
- command_contract_valid=true

## Exact Submit Command

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V013_multimodal_identity_locked_2x_impact_combo_prompt.txt"; & 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png" --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png" --prompt "$prompt" --model_version seedance2.0_vip --duration 4 --video_resolution 720p --ratio "16:9" --poll 0
```

## Submit Response Summary

Submit status: accepted/querying

- submit_id: 97259c8d-36c1-4f7e-9da8-ea707db4ad58
- logid: 2026062312384417201800000187850E7
- credit_count: 56
- gen_status: querying
- queue_status: not returned

Raw response summary:

```json
{
  "submit_id": "97259c8d-36c1-4f7e-9da8-ea707db4ad58",
  "logid": "2026062312384417201800000187850E7",
  "gen_status": "querying",
  "credit_count": 56
}
```

## Reference Confirmation

Submitted references:

1. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
2. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
3. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png

Not added:

- V009 frames
- V010 frames
- V011 frames
- V012 frames
- V012 cut/speed frames
- V012 contact sheets
- V012 downloaded video frames

## Post-Submit Boundaries

- No query_result was run after submit.
- No download was run after submit.
- No retry/resubmit/batch happened.
- The task is not final.
- The task is not locked.
- Future query/download requires explicit user approval and must use this exact submit_id only.

Final verdict:
SHOT_02_V013_SUBMITTED_QUERYING_NO_DOWNLOAD
