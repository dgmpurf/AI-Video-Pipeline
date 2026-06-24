# PHASE K86 - SHOT-02-V018 Query, Download, and Review Prep Result

## Human Authorization

The human explicitly authorized K86 to query and download-if-success for the existing V018 submit only:

- Submit id: `9a29b16f-e1a5-4d48-bb60-6d8dcabcca77`
- Maximum status-only query attempts: `3`
- Wait about 60 seconds between status-only queries if still querying/running
- Download exactly once only if a status-only query returns `gen_status=success`
- No retry
- No resubmit
- Do not modify V013 locked state
- Do not mark V018 final or locked

## K85 Submit Context

- K85 report: `reports/PHASE_K85_SHOT02_V018_SUBMIT_RESULT.md`
- Submit id: `9a29b16f-e1a5-4d48-bb60-6d8dcabcca77`
- Log id: `202606242353591692540470088626B09`
- Credit count: `70`
- Gen status at submit time: `querying`
- K85 query_result run: no
- K85 download run: no
- K85 retry/resubmit: no

## Canary Result

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- `dreamina version`: passed
- Version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- `dreamina user_credit`: passed
- User id: `1611200923726843`
- VIP level: `maestro`
- Total credit before query/download: `2252`
- Logger Access denied: not observed
- Login/auth failure: not observed

## Query Commands Used

Status-only query commands run: `1`

```powershell
& 'C:/Users/msjpurf/bin/dreamina.exe' query_result --submit_id=9a29b16f-e1a5-4d48-bb60-6d8dcabcca77
```

The first status-only query returned `gen_status=success`, so no second or third status-only query was run.

Download command used: yes, exactly once

```powershell
& 'C:/Users/msjpurf/bin/dreamina.exe' query_result --submit_id=9a29b16f-e1a5-4d48-bb60-6d8dcabcca77 --download_dir 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V018_20260624_235359/'
```

## Query Response Summary

- Submit id: `9a29b16f-e1a5-4d48-bb60-6d8dcabcca77`
- Gen status: `success`
- Queue status: `Finish`
- Queue idx: `0`
- Queue length: `0`
- Result availability: one MP4 result
- Reported video duration: `5.042s`
- Reported video resolution: `1280x720`
- Reported video fps: `24`
- Fail reason: none returned

## Download and Local Validation

- Download directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V018_20260624_235359/`
- Downloaded generic path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V018_20260624_235359/9a29b16f-e1a5-4d48-bb60-6d8dcabcca77_video_1.mp4`
- Normalized MP4 path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V018_20260624_235359/SHOT-02-V018_uploadsafe_hard_impact_fast_upperbody.mp4`
- Exists: true
- SHA256: `623877afb9beb6e83d36900507969051884f21239e372d42726c5e52f533b701`
- File size bytes: `10147944`
- Duration seconds by OpenCV: `5.016666666666667`
- Container/result duration seconds from Dreamina response: `5.042`
- Resolution: `1280x720`
- FPS / avg frame rate: `24.119601328903656`
- Frame count: `121`
- Video codec: `unknown_cv2_backend`
- Validation tool used: `OpenCV cv2.VideoCapture (ffprobe unavailable)`

## Review Assets

- Contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018/SHOT-02-V018_contact_sheet.jpg`
- Review frames directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018/`
- Review frames:
  - `frame_00.jpg` at `0.000s`
  - `frame_01.jpg` at `1.000s`
  - `frame_02.jpg` at `2.000s`
  - `frame_03.jpg` at `3.000s`
  - `frame_04.jpg` at `4.000s`
  - `frame_05.jpg` at `4.975s`

Generated media files are local review assets only and must not be staged.

## Boundaries Confirmed

- New submit run: no
- Retry run: no
- Resubmit run: no
- Status-only query_result commands run: `1`
- Download query_result commands run: `1`
- Media staged: no
- Upload-safe JPGs staged: no
- `.vs/` staged: no
- V013 lock state unchanged
- V014-R02 shot record unchanged
- V015 shot record unchanged
- V016 shot record unchanged
- V017 shot record unchanged
- V018 `final_master=false`
- V018 `locked=false`
- Human visual review is still required.

## Next Required Step

Human visual review of the downloaded MP4 and contact sheet:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V018_20260624_235359/SHOT-02-V018_uploadsafe_hard_impact_fast_upperbody.mp4`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018/SHOT-02-V018_contact_sheet.jpg`

Do not mark V018 final or locked without explicit future human approval.

## Final Verdict

SHOT_02_V018_DOWNLOADED_PENDING_HUMAN_REVIEW
