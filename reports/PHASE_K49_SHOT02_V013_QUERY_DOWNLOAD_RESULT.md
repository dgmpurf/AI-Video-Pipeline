# PHASE K49 - SHOT-02-V013 Query Download Result

## Scope

- Task: SHOT-02-V013
- Operation: query and download existing submit_id only
- Submit id: `97259c8d-36c1-4f7e-9da8-ea707db4ad58`
- Log id: `2026062312384417201800000187850E7`
- Credit count: 56
- Final master: false
- Locked: false
- Human review status: pending

No submit, resubmit, retry, batch execution, or new generation command was run in this pass.

## Canary Result

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Version result: `{"version":"46b5b0e-dirty","commit":"46b5b0e","build_time":"2026-06-03T19:39:25Z"}`
- User credit result: `{"total_credit":2508,"user_id":1611200923726843,"user_name":"","vip_level":"maestro"}`
- Canary status: passed

## Query Command

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id 97259c8d-36c1-4f7e-9da8-ea707db4ad58 --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V013_20260623_123844"
```

Exactly one `query_result` command was run for this submit id.

## Query Result

- Query status / gen_status: success
- Queue status: Finish
- Queue idx: 0
- Queue length: 0
- Priority: 1
- Download happened: yes

## Downloaded Output

- Run directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V013_20260623_123844`
- Final output path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V013_20260623_123844/SHOT-02-V013_identity_locked_2x_impact_combo.mp4`
- Original downloaded file name: `97259c8d-36c1-4f7e-9da8-ea707db4ad58_video_1.mp4`
- Normalized output name: `SHOT-02-V013_identity_locked_2x_impact_combo.mp4`

## Validation Metadata

- File exists: true
- File size bytes: 8151957
- SHA256: `851dffdc81880da5750fe125f721821589a55ab9ac05fdbb2f46ee062c08b72d`
- Stream duration seconds: 4.016667
- Format duration seconds: 4.087
- Resolution: 1280x720
- Width: 1280
- Height: 720
- Average frame rate: 5820/241, approximately 24.149 fps
- Nominal frame rate: 60/1
- Frame count: 97

## Review Assets

- Contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_contact_sheet.jpg`
- Contact sheet size bytes: 167966
- Contact sheet SHA256: `3b9038359085e0dc4f32219064134d225dd747cf254f3691b01e68c1cb6dedc2`

Review frames:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_00_0p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_01_0p20s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_02_0p40s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_03_0p60s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_04_0p80s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_05_1p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_06_1p25s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_07_1p50s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_08_2p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_09_3p00s.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V013/SHOT-02-V013_frame_10_last_4p00s.jpg`

## Metadata Update

- Shot record updated to: `success_downloaded_pending_human_review`
- Human review remains pending.
- `final_master=false`
- `locked=false`

## Next Step

Human review should inspect the SHOT-02-V013 contact sheet and downloaded video before any usable/final/lock decision.

## Final Verdict

SHOT_02_V013_SUCCESS_DOWNLOADED_REVIEW_READY
