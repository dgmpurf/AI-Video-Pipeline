# PHASE K76 - SHOT-02-V016 Query Download Result

## Human Authorization

The human explicitly approved bounded query and download-if-success:

> 批准 K76 查询并在成功时下载 V016 submit_id：d51a3b18-7320-4d2a-9890-f0e0e74e2297。允许最多 query_result 3 次，每次间隔 60 秒；如果 gen_status=success，允许 query_result --download_dir 下载一次，并允许本地校验、生成 contact sheet 和 review frames。不允许 retry，不允许 resubmit，不允许修改 V013 锁定状态，不允许标记 V016 final/locked。

## K75 Submit Context

- Shot: `SHOT-02-V016`
- Submit id: `d51a3b18-7320-4d2a-9890-f0e0e74e2297`
- Logid: `202606242128201692540470089189AD9`
- Credit count: `70`
- Gen status at submit time: `querying`
- Queue status at submit time: not returned
- K75 boundaries: exactly one submit, no query, no download, no retry, no resubmit.

## Canary Result

- Command: `C:\Users\msjpurf\bin\dreamina.exe version`
- Result: passed
- Version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- Command: `C:\Users\msjpurf\bin\dreamina.exe user_credit`
- Result: passed
- User credit summary: user_id `1611200923726843`, vip_level `maestro`, total_credit `2392`
- Logger Access denied: no
- Login/auth failure: no

## Query Commands Used

Status-only query commands run: `1`

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id=d51a3b18-7320-4d2a-9890-f0e0e74e2297
```

Download commands run: `1`

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id=d51a3b18-7320-4d2a-9890-f0e0e74e2297 --download_dir 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V016_20260624_212820/'
```

The download command was run only after the status-only query returned `gen_status=success`.

## Query Response Summary

- Submit id: `d51a3b18-7320-4d2a-9890-f0e0e74e2297`
- Gen status: `success`
- Queue status: `Finish`
- Queue index: `0`
- Queue length: `0`
- Result availability: one MP4 video result
- Result metadata from Dreamina: `1280x720`, `fps=24`, `duration=5.042`, `format=mp4`
- Fail reason: none returned

## Downloaded Media

- Download happened: yes
- Download directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V016_20260624_212820/`
- Generic downloaded file renamed within the same run directory to the standard output name.
- Local MP4 path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V016_20260624_212820/SHOT-02-V016_uploadsafe_hand_foot_line_steal.mp4`
- Exists: true
- SHA256: `f76f163f2faaafe08e908ab1cbb5f3d24ef000cc28793e09a04759e0b15b7658`
- File size bytes: `9688817`
- Video stream duration seconds: `5.016667`
- Container duration seconds: `5.085011`
- Resolution: `1280x720`
- Average frame rate: `7260/301`
- Frame count: `121`
- Video codec: `h264`

## Review Assets

- Contact sheet path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V016/SHOT-02-V016_contact_sheet.jpg`
- Review frames directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V016/`
- Review frames created:
  - `frame_00.jpg`
  - `frame_01.jpg`
  - `frame_02.jpg`
  - `frame_03.jpg`
  - `frame_04.jpg`
  - `frame_05.jpg`

These review assets are media files and must remain unstaged.

## Boundaries Confirmed

- No retry was run.
- No resubmit was run.
- No new submit was run.
- Status-only query commands used: `1`, within the authorized maximum of `3`.
- Download commands used: `1`, within the authorized maximum of `1`.
- No media was staged.
- Upload-safe JPG files were not staged.
- `.vs/` was not staged.
- V013 lock state was not modified.
- V014-R02 shot record was not modified.
- V015 shot record was not modified.
- V016 `final_master=false`.
- V016 `locked=false`.
- Human visual review is still required.

## Next Required Step

Human visual review of the downloaded MP4 and contact sheet:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V016_20260624_212820/SHOT-02-V016_uploadsafe_hand_foot_line_steal.mp4`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V016/SHOT-02-V016_contact_sheet.jpg`

Do not mark V016 final, locked, or replacement for V013 CUT01 without future explicit human approval.

## Final Verdict

SHOT_02_V016_DOWNLOADED_PENDING_HUMAN_REVIEW
