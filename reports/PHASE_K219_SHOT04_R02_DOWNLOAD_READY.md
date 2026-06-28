# PHASE K219 - SHOT-04 R02 Download Ready

## 1. Purpose

Download the existing successful K217/K218 SHOT-04 R02 video result.

This phase is download-only for an existing successful submit_id. It does not submit, retry, resubmit, batch, create contact sheets, create review frames, mark final, or lock.

## 2. Authorization Level

Authorization level: download-only for existing successful submit_id.

Authorized submit_id:

`bb29761f-bc0a-49a0-88d3-f7b91579ddb6`

## 3. Human Authorization Quote

The human authorized K219 to download only the existing successful K217/K218 SHOT-04 R02 remote video result for submit_id:

`bb29761f-bc0a-49a0-88d3-f7b91579ddb6`

No submit, retry, resubmit, batch, final, or lock was authorized.

## 4. Files Inspected

- `reports/PHASE_K218_SHOT04_R02_SUBMIT_STATUS_QUERY_RESULT_NO_DOWNLOAD.md`
- `reports/PHASE_K217_SHOT04_R02_L3_DREAMINA_RESUBMIT_RESULT.md`
- `reports/PHASE_K216_SHOT04_R02_UPLOAD_SAFE_PACKAGE_SUBMIT_READINESS_REVIEW_NO_SUBMIT.md`
- `reports/PHASE_K215_SHOT04_R02_UPLOAD_SAFE_REFERENCE_PACKAGING_NO_SUBMIT.md`
- `reports/PHASE_K214_SHOT04_R02_SUBMIT_FAILURE_TRIAGE_UPLOAD_PATH_REMEDIATION_PLANNING.md`
- `reports/PHASE_K213_SHOT04_R02_L3_DREAMINA_SUBMIT_RESULT.md`

## 5. Source Governance Confirmation

- `sources/` was checked before download and was clean.
- `sources/` was read-only for this phase.
- No `sources/` file was created, modified, deleted, renamed, moved, staged, committed, or pushed.
- No official Source update was performed.

## 6. K218 Carry-Forward

K218 confirmed:

- submit_id: `bb29761f-bc0a-49a0-88d3-f7b91579ddb6`
- gen_status: `success`
- queue_status: `Finish`
- result_videos_count: `1`
- download_url_present: `true`
- remote format: `mp4`
- remote width: `1280`
- remote height: `720`
- remote fps: `24`
- remote duration: `5.042` seconds
- no download before K219
- no retry/resubmit
- final_master: `false`
- locked: `false`

K218 final verdict:

`SHOT04_R02_SUBMIT_QUERY_SUCCESS_READY_K219_DOWNLOAD_AUTHORIZATION_REQUEST_NO_DOWNLOAD`

## 7. Corrected Dreamina Download Preflight

Dreamina executable:

`C:/Users/msjpurf/bin/dreamina.exe`

Version:

- version: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`

User credit:

- user_credit succeeded
- total_credit before download: `1689`
- user_id: `1611200923726843`
- vip_level: `maestro`

`query_result -h`:

- supports `--submit_id`
- supports `--download_dir`

Download preflight result: passed.

## 8. Exact Download Command Used

Command shape:

```powershell
$downloadDir = "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_wall_panel_shoulder_check_rebound_20260629_002125"
New-Item -ItemType Directory -Force -Path $downloadDir | Out-Null
dreamina query_result --submit_id=bb29761f-bc0a-49a0-88d3-f7b91579ddb6 --download_dir "$downloadDir"
```

No signed URLs are recorded in this report.

## 9. Download Result

- download_attempted: `true`
- download_count: `1`
- submit_id: `bb29761f-bc0a-49a0-88d3-f7b91579ddb6`
- local_download_dir: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_wall_panel_shoulder_check_rebound_20260629_002125`
- downloaded_files_count: `1`
- downloaded_video_path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_wall_panel_shoulder_check_rebound_20260629_002125/bb29761f-bc0a-49a0-88d3-f7b91579ddb6_video_1.mp4`
- filename: `bb29761f-bc0a-49a0-88d3-f7b91579ddb6_video_1.mp4`
- exists: `true`
- size_bytes: `11134997`
- sha256: `bb69c736d5a9d1d6af10cebd265da3cf25ec150e840b2a6724fe89b42cd43a15`
- format: `mp4`
- width: `1280`
- height: `720`
- fps: `24.119601328903656`
- duration: `5.016666666666667`
- frame_count: `121`
- metadata_source: `python_cv2`
- validation_pass: `true`

Metadata note:

- `ffprobe` was unavailable in the local environment, so Python/OpenCV was used.
- Remote K218 metadata reported fps `24` and duration `5.042`.
- Local OpenCV metadata reports fps `24.119601328903656` and duration `5.016666666666667`.
- This slight difference is recorded as metadata interpretation variance and did not trigger a retry.

## 10. Boundary Confirmation

- submit_run: `false`
- retry_run: `false`
- resubmit_run: `false`
- batch_run: `false`
- unrelated_query_run: `false`
- second_download_run: `false`
- media_staged: `false`
- final_master: `false`
- locked: `false`
- sources_modified: `false`
- prompt_modified: `false`
- package_modified: `false`
- manifest_modified: `false`
- runtime_code_modified: `false`
- configs/providers.json_modified: `false`
- auth/session/token/key/env_opened_or_staged: `false`
- context_recovery_files_staged: `false`

## 11. Recommended Next Phase

K220 = human + ChatGPT visual review for SHOT-04 R02 wall-panel shoulder-check rebound video.

The user should upload the downloaded MP4 to ChatGPT:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_wall_panel_shoulder_check_rebound_20260629_002125/bb29761f-bc0a-49a0-88d3-f7b91579ddb6_video_1.mp4`

No final or lock decision should happen before human visual review.

## 12. What Not To Do

- do not submit
- do not retry
- do not resubmit
- do not mark final
- do not lock
- do not update Source
- do not stage media
- do not stage context recovery handoff files

## 13. Safety Confirmation

- corrected Dreamina download preflight was run
- exactly one `query_result --download_dir` was run for the existing successful submit_id
- no submit
- no retry
- no resubmit
- no batch
- no unrelated query
- no query loop
- no unrelated download
- no contact sheet created
- no review frames created
- no media staged
- no prompt/package/manifest modified
- no shot record modified
- no Source modified
- no runtime code modified
- no `configs/providers.json` modified
- no auth/session/token/key/env file opened, copied, printed, staged, or committed
- `final_master=false`
- `locked=false`

## 14. Final Verdict

SHOT04_R02_VIDEO_DOWNLOADED_READY_K220_VISUAL_REVIEW
