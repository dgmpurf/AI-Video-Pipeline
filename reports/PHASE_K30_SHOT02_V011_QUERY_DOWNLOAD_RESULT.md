# PHASE K30 SHOT-02 V011 Query/Download Result

Date: 2026-06-22

## Scope

- Query existing `SHOT-02-V011` submit_id only.
- Do not submit, resubmit, retry, batch, logout, or relogin.
- Download is allowed only through the single `query_result --download_dir` command in this pass.
- Do not mark final master or locked.

## Canary Result

Canary passed before query.

- Dreamina executable: `C:\Users\msjpurf\bin\dreamina.exe`
- `dreamina version`: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`
- `dreamina user_credit`: succeeded
- total_credit before query: `2621`
- user_id: `1611200923726843`
- vip_level: `maestro`

## Exact Query Command

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id 8a387d83-a9a6-453a-81be-2a8dc93f1c1c --download_dir 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V011_20260622_145250'
```

## Query Result Summary

- submit_id: `8a387d83-a9a6-453a-81be-2a8dc93f1c1c`
- logid: `202606221452501692540470086931054`
- gen_status: `success`
- queue_status: `Finish`
- queue_idx: `0`
- queue_length: `0`
- priority: `1`
- credit_count: `56`

## Download Result

Downloaded and canonicalized media path:

`productions/chi_yan_tian_qiong/runs/live/SHOT-02-V011_20260622_145250/SHOT-02-V011_multimodal_identity_locked_followup_attack.mp4`

## Validation Metadata

- exists: `true`
- file_size_bytes: `6399405`
- sha256: `cf4f872531daa3524198f80d228bcaa5d082460c08f28a12743a772adf6c1ced`
- duration_seconds: `4.016667`
- resolution: `1280x720`
- fps: `24.149377593360995`
- frame_count: `97`

## Review Assets

Contact sheet:

`productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_contact_sheet.jpg`

Review frames:

- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_00.jpg`
- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_01.jpg`
- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_02.jpg`
- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_03.jpg`
- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_04.jpg`
- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_05.jpg`
- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_frame_06.jpg`

Frame times:

- `0.00s`
- `0.50s`
- `1.00s`
- `1.50s`
- `2.00s`
- `3.00s`
- `4.00s / last valid frame`

## Shot Record State

`productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V011.json` was updated:

- status: `success_downloaded_pending_human_review`
- package_status: `success_downloaded_pending_human_review`
- human_review_status: `pending`
- final_master: `false`
- locked: `false`
- downloaded_mp4_validated: `true`

## Boundary Confirmation

- Exactly one `query_result` command was run in this pass.
- No submit/resubmit/retry/batch was run.
- Media was not staged.
- Human review remains required before any final/lock decision.

Final verdict: `SHOT_02_V011_SUCCESS_DOWNLOADED_REVIEW_READY`
