# PHASE K107 - SHOT-03 V002 Query And Download Result

## Human Authorization

The human explicitly approved K107 to query and download the existing SHOT-03 V002 submit only:

> K106 already manually committed and pushed successfully. K107 is approved to query SHOT-03 V002 submit_id 0a5768c4-2813-477f-99b3-cadaf39924b0 and download if successful. Codex may run up to three query_result status checks, about 60 seconds apart, and if gen_status=success may run one query_result --download_dir download. Do not retry, do not resubmit, do not create a new submit. Keep final_master=false and locked=false.

## K106 Submit Context

- shot_id: SHOT-03
- version_id: SHOT-03-V002
- variant_id: uploadsafe_continuity_fix_exterior_veranda_stairs_eaves
- submit_id: 0a5768c4-2813-477f-99b3-cadaf39924b0
- logid: 20260625194028169254047008725D8D6
- credit_count: 70
- gen_status at submit time: querying
- task_type: multimodal2video
- model_version: seedance2.0_vip
- duration: 5
- ratio: 16:9
- video_resolution: 720p
- K106 query_result performed: false
- K106 download performed: false

## Canary Result

- Command: C:/Users/msjpurf/bin/dreamina.exe version
- Result: passed.
- Version: 46b5b0e-dirty.
- Commit: 46b5b0e.
- Build time: 2026-06-03T19:39:25Z.
- Command: C:/Users/msjpurf/bin/dreamina.exe user_credit
- Result: passed.
- Total credit at canary: 2112.
- VIP level: maestro.
- Logger Access denied: not observed.
- Login/auth failure: not observed.

## Query Commands Used

Status-only query_result commands without --download_dir:

1. C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id=0a5768c4-2813-477f-99b3-cadaf39924b0

Download query_result commands with --download_dir:

1. C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id=0a5768c4-2813-477f-99b3-cadaf39924b0 --download_dir G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V002_20260625_194028/

Status-only query attempt count: 1.
Download attempt count: 1.

## Query Response Summary

- submit_id: 0a5768c4-2813-477f-99b3-cadaf39924b0
- gen_status: success
- queue_status: Finish
- queue_idx: 0
- queue_length: 0
- result availability: video result available
- fail reason: none returned
- result metadata from Dreamina status response: 1280x720, mp4, fps=24, duration=5.042 seconds.

## Download And Local Validation

- Download happened: true.
- Local MP4 path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V002_20260625_194028/SHOT-03-V002_uploadsafe_continuity_fix_exterior_veranda_stairs_eaves.mp4
- Exists: true.
- SHA256: a01568319cf80d9901be695c9323b9e8c853a825d243d352ac176d11f9eb59c3
- file_size_bytes: 9748979
- duration_seconds: 5.016666666666667
- resolution: 1280x720
- fps: 24.119601328903656
- avg_frame_rate: 24.119601328903656
- frame_count: 121
- video codec: unknown_cv2_backend
- validation tool used: python cv2 4.12.0 + hashlib

Review assets:

- Contact sheet: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V002/SHOT-03-V002_contact_sheet.jpg
- Review frames directory: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V002/
- Review frames:
  - frame_00.jpg at 0.00s
  - frame_01.jpg at 1.00s
  - frame_02.jpg at 2.00s
  - frame_03.jpg at 3.00s
  - frame_04.jpg at 4.00s
  - frame_05.jpg at last valid frame, approximately 4.98s

## Boundaries

- No new submit was run.
- No retry was run.
- No resubmit was run.
- Status-only query count did not exceed 3.
- Download command count did not exceed 1.
- No media was staged.
- Upload-safe JPGs were not staged.
- .vs/ was not staged.
- final_master=false.
- locked=false.
- SHOT-02 / V013 / V018 lock states were not changed.

## Next Required Step

Human visual review of the downloaded MP4 and contact sheet is required before any final, lock, or downstream quality decision.

Final verdict: SHOT03_V002_DOWNLOADED_PENDING_HUMAN_REVIEW
