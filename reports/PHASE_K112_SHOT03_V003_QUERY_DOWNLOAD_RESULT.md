# PHASE K112 - SHOT-03 V003 Query / Download Result

## Human Authorization

- Scope: query and download existing SHOT-03-V003 submit_id only.
- Existing submit_id: `dd7aba19-c468-418a-bcf4-2e9aa0712f94`
- Existing logid: `2026062521030416925404700895796F1`
- No submit, retry, resubmit, batch, logout, or relogin was allowed.
- Final approval still requires human visual review.

## K111 Submit Context

- Package: SHOT-03-V003 upload-safe simplified exterior column corridor.
- Task type: `multimodal2video`
- Model: `seedance2.0_vip`
- Duration: 5
- Ratio: `16:9`
- Video resolution: `720p`
- Submit phase: `PHASE_K111`
- Submit status before this phase: `submitted_no_query`

## Canary Result

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Version command: passed
- User credit command: passed
- Dreamina version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- User credit at canary: `2042`
- VIP level: `maestro`
- Logger access denied: no
- Login/auth failure: no

## Query Commands Used

Status-only query command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id=dd7aba19-c468-418a-bcf4-2e9aa0712f94
```

Download command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id=dd7aba19-c468-418a-bcf4-2e9aa0712f94 --download_dir G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V003_20260625_210304/
```

## Query Response Summary

- Status-only query attempts: 1
- Final `gen_status`: `success`
- Queue status: `Finish`
- Queue index: 0
- Queue length: 0
- Fail reason: none
- Result available: yes
- Dreamina result duration: 5.042s
- Dreamina result resolution: 1280x720
- Dreamina result fps: 24

## Download Result

- Download attempted: yes, exactly once
- Run directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V003_20260625_210304/`
- Final local MP4: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V003_20260625_210304/SHOT-03-V003_uploadsafe_simplified_exterior_column_corridor.mp4`

## Local Validation Metadata

- Exists: yes
- File size bytes: 9792177
- SHA256: `d05175ab0ad04d72f6a96b53454e9bad52de092fd69168c1b3972d653eeebb8b`
- Duration: 5.016666666666667s
- Resolution: 1280x720
- FPS: 24.119601328903656
- Frame count: 121
- Validation tool: `python cv2 4.12.0 + hashlib`

## Review Assets

- Contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_contact_sheet.jpg`
- Review frames:
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_frame_00.jpg`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_frame_01.jpg`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_frame_02.jpg`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_frame_03.jpg`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_frame_04.jpg`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V003/SHOT-03-V003_frame_05.jpg`

## Boundaries Preserved

- New submit performed: no
- Retry performed: no
- Resubmit performed: no
- Status-only query attempts used: 1 of allowed maximum 3
- Download attempts used: 1 of allowed maximum 1
- Media staged: no
- `final_master`: false
- `locked`: false
- SHOT-02 / V013 / V018 records changed: no

## Next Step

Human visual review should inspect the contact sheet and/or downloaded MP4 before any usability, final-master, or lock decision.

Final verdict: `SHOT03_V003_DOWNLOADED_PENDING_HUMAN_REVIEW`
