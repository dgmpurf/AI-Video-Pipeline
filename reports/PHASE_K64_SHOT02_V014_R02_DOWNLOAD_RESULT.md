# PHASE K64 - SHOT-02-V014-R02 Download Result

Date: 2026-06-24
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Human Authorization

The human explicitly approved K64 download for SHOT-02-V014-R02 submit_id:

`26508110-29da-4edc-abd2-5b0cf4b0afa0`

Boundaries:

- Run exactly one `query_result --download_dir` download command.
- Do not retry.
- Do not resubmit.
- Do not run a new generation command.
- Do not modify V013 shot record.
- Do not mark V014-R02 final or locked.
- Human visual review is required after download.

## K62/K63 Context

| Field | Value |
|---|---|
| submit_id | 26508110-29da-4edc-abd2-5b0cf4b0afa0 |
| logid | 20260624143551172018000001869F5DF |
| K63 gen_status | success |
| K63 queue_status | Finish |
| K63 expected metadata | 1280x720, 24 fps, 4.042s |
| K63 download | not run |

V013 CUT01 remains the locked current SHOT-02 passed segment. V014-R02 remains optional enhancement only and cannot replace V013 CUT01 unless the human explicitly approves a future replacement.

## Canary Result

Dreamina canary passed before download.

| Check | Result |
|---|---|
| dreamina version | success |
| version | 46b5b0e-dirty |
| commit | 46b5b0e |
| build_time | 2026-06-03T19:39:25Z |
| dreamina user_credit | success |
| user_id | 1611200923726843 |
| vip_level | maestro |
| total_credit_before_download | 2532 |
| logger Access denied | no |
| login/auth failure | no |

## Download Command Used

Exactly one download command was run:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id=26508110-29da-4edc-abd2-5b0cf4b0afa0 --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V014-R02_20260624_143551/"
```

No second query/download command was run.

## Download Result

Dreamina downloaded the generic MP4:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V014-R02_20260624_143551/26508110-29da-4edc-abd2-5b0cf4b0afa0_video_1.mp4

The file was copied within the same run directory to the canonical output name:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V014-R02_20260624_143551/SHOT-02-V014-R02_uploadsafe_legwork_hand_foot_combo.mp4

## Local Validation

Validation was performed locally with imageio-ffmpeg/Pillow tooling because ffprobe was not available on PATH in this environment.

| Field | Value |
|---|---|
| exists | true |
| local MP4 path | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V014-R02_20260624_143551/SHOT-02-V014-R02_uploadsafe_legwork_hand_foot_combo.mp4 |
| sha256 | 85FD208BC78C2DA7E3157D7D5E052B418A05FE808EF9A718FA7FF8925C136F08 |
| file_size_bytes | 8815553 |
| duration_seconds | 4.09 |
| container_duration_seconds | 4.09 |
| resolution | 1280x720 |
| fps / avg_frame_rate | 24.15 |
| frame_count | 97 |
| video_codec | h264 |

These exact local values are close to the K63 returned metadata of 1280x720, 24 fps, and 4.042s.

## Contact Sheet And Review Frames

Review directory:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/

Contact sheet:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/SHOT-02-V014-R02_contact_sheet.jpg

Contact sheet SHA256:

`9A805C4BB46FAD01FA4D773F63F8CD43F83362ACE691F9AE04B20527132618F5`

Review frames:

| Frame | Timestamp | Path |
|---|---:|---|
| frame_00 | 0.000s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/frame_00.jpg |
| frame_01 | 0.787s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/frame_01.jpg |
| frame_02 | 1.615s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/frame_02.jpg |
| frame_03 | 2.402s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/frame_03.jpg |
| frame_04 | 3.188s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/frame_04.jpg |
| frame_05 | 3.975s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/frame_05.jpg |

## Boundaries Confirmation

- Exactly one `query_result --download_dir` command was run.
- No retry happened.
- No resubmit happened.
- No new generation command was run.
- No media files were staged.
- The downloaded MP4 was not staged.
- The contact sheet and review frame JPGs were not staged.
- Generated upload-safe JPGs were not staged.
- `.vs/` was not staged.
- V013 lock state was unchanged.
- V014-R02 final_master=false.
- V014-R02 locked=false.

## Next Required Step

The next required step is human visual review of the MP4/contact sheet.

Optional Codex visual review should happen only if the human asks.

No final/lock decision is allowed without explicit human approval.

Final verdict:
SHOT_02_V014_R02_DOWNLOADED_PENDING_HUMAN_REVIEW
