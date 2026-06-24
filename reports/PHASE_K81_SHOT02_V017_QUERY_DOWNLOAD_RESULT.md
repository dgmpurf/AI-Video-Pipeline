# PHASE K81 - SHOT-02-V017 Query and Download Result

## Human Authorization

The user authorized a bounded query and download-if-success pass for the existing `SHOT-02-V017` submit only.

Authorized submit ID:

- `8ffd960c-e1df-41dd-89a1-c18c9c1a12e7`

Boundaries:

- No new submit.
- No retry.
- No resubmit.
- No batch.
- Up to three status-only `query_result` commands.
- Download exactly once only after a status-only query returned `gen_status=success`.
- Do not mark final master.
- Do not lock.
- Human visual review is required after download.

## K80 Submit Context

- `submit_id`: `8ffd960c-e1df-41dd-89a1-c18c9c1a12e7`
- `logid`: `20260624222858169254047008970B607`
- `credit_count`: `70`
- `gen_status` at submit time: `querying`
- K80 ran no `query_result`.
- K80 ran no download.
- K80 ran no retry/resubmit.

## Canary Result

Result: pass.

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Dreamina version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- `user_credit`: succeeded
- `total_credit`: `2322`
- `user_id`: `1611200923726843`
- `vip_level`: `maestro`
- No logger access denied error.
- No login/auth failure.

## Query Commands Used

Status-only query count: `1`

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id=8ffd960c-e1df-41dd-89a1-c18c9c1a12e7
```

Download command count: `1`

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id=8ffd960c-e1df-41dd-89a1-c18c9c1a12e7 --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V017_20260624_222858/"
```

## Query Response Summary

- `submit_id`: `8ffd960c-e1df-41dd-89a1-c18c9c1a12e7`
- `gen_status`: `success`
- `queue_status`: `Finish`
- `queue_idx`: `0`
- `queue_length`: `0`
- Result availability: video result available
- Fail reason: none returned

Dreamina result metadata:

- `fps`: `24`
- `width`: `1280`
- `height`: `720`
- `format`: `mp4`
- `duration`: `5.042`

## Downloaded Media

Generic downloaded file was renamed within the same run directory to the canonical V017 output name.

- Local MP4 path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V017_20260624_222858/SHOT-02-V017_uploadsafe_fast_upperbody_refined_particles.mp4`
- Exists: `true`
- SHA256: `b8d71b4aa530ab5d5439f23976395f0b2cb517c871d4673cc789c53fcf4f3ddd`
- File size bytes: `9853031`
- Duration seconds: `5.016666666666667`
- Resolution: `1280x720`
- FPS / avg frame rate: `24.119601328903656`
- Frame count: `121`
- Video codec: not probed by ffprobe because `ffmpeg/ffprobe` were not available in PATH; OpenCV/PIL were used for local validation and review-frame generation.

## Review Assets

- Contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V017/SHOT-02-V017_contact_sheet.jpg`
- Review frames directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V017/`

Extracted review frames:

- `frame_00.jpg`
- `frame_01.jpg`
- `frame_02.jpg`
- `frame_03.jpg`
- `frame_04.jpg`
- `frame_05.jpg`

## Boundary Confirmation

- No retry was run.
- No resubmit was run.
- No new submit was run.
- No batch command was run.
- Media files were not staged.
- Upload-safe JPG files were not staged.
- `.vs/` was not staged.
- V013 lock state was not changed.
- V013 shot record was not modified.
- V014-R02 shot record was not modified.
- V015 shot record was not modified.
- V016 shot record was not modified.
- V017 `final_master=false`.
- V017 `locked=false`.

## Current Policy State

- `SHOT-02-V013-CUT01-LOCKED` remains the locked current SHOT-02 passed segment.
- `SHOT-02-V014-R02_uploadsafe` remains the stronger positive enhancement candidate.
- `SHOT-02-V015_uploadsafe` remains rejected and is only a failure reference.
- `SHOT-02-V016_uploadsafe` remains positive-with-notes / possible edit-insert candidate.
- `SHOT-02-V017` is an optional correction experiment only.
- V017 cannot overwrite, downgrade, or replace V013 CUT01 unless the human explicitly approves a future replacement.

## Next Required Step

Human visual review of the V017 MP4 and contact sheet.

Do not mark V017 final or locked before human review.

## Final Verdict

SHOT_02_V017_DOWNLOADED_PENDING_HUMAN_REVIEW
