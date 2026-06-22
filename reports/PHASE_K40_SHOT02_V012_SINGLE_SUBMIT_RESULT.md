# PHASE K40 SHOT-02 V012 Single Submit Result

Date: 2026-06-22

## Scope

Submit the already-reviewed `SHOT-02-V012` `multimodal2video` package exactly once.

No `query_result` was run. No download was run. No retry, resubmit, or batch command happened.

No runtime code, `configs/providers.json`, Project Source file, prompt body, or media file was modified.

## Canary Result

Canary status: pass.

Dreamina version:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

Dreamina user credit:

```json
{
  "total_credit": 2620,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

## Command-Contract Preflight Result

Preflight status: passed.

`C:\Users\msjpurf\bin\dreamina.exe multimodal2video -h` confirmed:

- task type: `multimodal2video`
- supported model includes `seedance2.0_vip`
- supported duration range: `4-15s`
- `duration=4` is supported
- `seedance2.0_vip` supports `video_resolution=720p`
- supported ratio includes `16:9`
- input can include repeated `--image`
- image input limit is `image<=9`
- V012 uses exactly 3 images

Local package preflight confirmed:

- all 3 selected image paths exist
- no V009/V010/V011 frame path is included
- no `V010 frame_06` is included
- `command_contract_valid=true`

## Exact Submit Command

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V012_multimodal_identity_locked_fast_staccato_combat_prompt.txt"; & 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png" --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png" --prompt "$prompt" --model_version seedance2.0_vip --duration 4 --video_resolution 720p --ratio "16:9" --poll 0
```

## Submit Response Summary

Submit status: accepted / asynchronous querying.

```json
{
  "submit_id": "86f7ae6d-4390-421a-abf1-a10f8efce430",
  "logid": "20260622233335169254047008939BD14",
  "gen_status": "querying",
  "credit_count": 56
}
```

- submit_id: `86f7ae6d-4390-421a-abf1-a10f8efce430`
- logid: `20260622233335169254047008939BD14`
- credit_count: `56`
- gen_status: `querying`
- queue_status: not returned in submit response

## Boundary Confirmation

- Exactly one `multimodal2video` submit command was run.
- No `query_result` was run after submit.
- No download was run after submit.
- No retry happened.
- No resubmit happened.
- No batch happened.
- V009/V010/V011 frames were not added.
- Prompt body was not changed.
- `final_master=false`
- `locked=false`
- Human review is still required after future download.

## Updated Text Records

- `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V012.json`
- `reports/PHASE_K40_SHOT02_V012_SINGLE_SUBMIT_RESULT.md`

## Next Allowed Step

Only with explicit user approval: query/download this exact submit id.

Do not submit another V012 task unless the user explicitly requests a new package/retry path.

Final verdict: `SHOT_02_V012_SUBMITTED_QUERYING_NO_DOWNLOAD`
