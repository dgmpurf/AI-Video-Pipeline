# PHASE K41 SHOT-02 V012 Query/Download Result

Date: 2026-06-22

## Scope

Query existing `SHOT-02-V012` submit_id only and download through the single approved `query_result --download_dir` command.

No submit, resubmit, retry, batch, `multimodal2video`, logout, or relogin command was run in this pass. The prompt was not modified and no V009/V010/V011 frames were added.

Final approval still requires human review. `final_master=false` and `locked=false`.

## Canary Result

Canary passed before query.

- Dreamina executable: `C:\Users\msjpurf\bin\dreamina.exe`
- `dreamina version`: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`
- `dreamina user_credit`: succeeded
- total_credit before query: `2564`
- user_id: `1611200923726843`
- vip_level: `maestro`

## Exact Query Command

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id 86f7ae6d-4390-421a-abf1-a10f8efce430 --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V012_20260622_233335"
```

Exactly one `query_result` command was run.

## Query Result Summary

- submit_id: `86f7ae6d-4390-421a-abf1-a10f8efce430`
- logid: `20260622233335169254047008939BD14`
- gen_status: `success`
- queue_status: `Finish`
- queue_idx: `0`
- queue_length: `0`
- priority: `1`
- credit_count: `56`

## Download Result

Downloaded file from Dreamina:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V012_20260622_233335/86f7ae6d-4390-421a-abf1-a10f8efce430_video_1.mp4`

Canonicalized media path:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V012_20260622_233335/SHOT-02-V012_identity_locked_fast_staccato_combat.mp4`

The downloaded MP4 was renamed in place. No existing different file was overwritten.

## Validation Metadata

- exists: `true`
- file_size_bytes: `8693940`
- sha256: `9d35873ab9a40d774beb5169b041dcab04284c1734cf0f9adb6dbce4450f1192`
- stream_duration_seconds: `4.016667`
- format_duration_seconds: `4.062993`
- resolution: `1280x720`
- width: `1280`
- height: `720`
- fps: `24.149377593361`
- avg_frame_rate: `5820/241`
- r_frame_rate: `60/1`
- frame_count: `97`

Validation source:

- local file metadata
- `Get-FileHash`
- `C:\ffmpeg\bin\ffprobe.exe`

## Review Assets

Contact sheet:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_contact_sheet.jpg`

Contact sheet metadata:

- exists: `true`
- file_size_bytes: `194764`
- sha256: `ca9b3226749ae3253aa58674f477b7914a274cff4fe1f9e299c7f03f6d8cbe20`

Review frames:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_00_0p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_01_0p25s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_02_0p50s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_03_0p75s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_04_1p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_05_1p25s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_06_1p50s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_07_2p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_08_3p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_frame_09_last_4p00s.jpg`

Frame times:

- `0.00s`
- `0.25s`
- `0.50s`
- `0.75s`
- `1.00s`
- `1.25s`
- `1.50s`
- `2.00s`
- `3.00s`
- `4.00s / last valid frame`

## Shot Record State

`productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V012.json` was updated:

- status: `success_downloaded_pending_human_review`
- package_status: `success_downloaded_pending_human_review`
- human_review_status: `pending`
- final_master: `false`
- locked: `false`
- output_video_path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V012_20260622_233335/SHOT-02-V012_identity_locked_fast_staccato_combat.mp4`
- downloaded_mp4_validated: `true`
- contact_sheet_generated: `true`

## Boundary Confirmation

- Exactly one `query_result` command was run in this pass.
- No submit was run.
- No resubmit was run.
- No retry was run.
- No batch was run.
- No `multimodal2video` command was run.
- No V009/V010/V011 frames were added.
- Media files were created locally for review but were not staged.
- Human review remains required before any final/lock decision.

Final verdict: `SHOT_02_V012_SUCCESS_DOWNLOADED_REVIEW_READY`
