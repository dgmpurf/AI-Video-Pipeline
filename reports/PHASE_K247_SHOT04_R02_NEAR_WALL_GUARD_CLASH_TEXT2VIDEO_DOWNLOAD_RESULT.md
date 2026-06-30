# PHASE K247 - SHOT-04 R02 Near-Wall Guard-Clash Text2Video Download Result

## 1. Purpose

Record the human-authorized K247 L3 download-only action for the existing successful K245/K246 Dreamina `text2video` result.

This phase downloads the already successful K245 result only. It does not submit, retry, resubmit, batch, create review frames, create contact sheets, claim visual success, mark final, or lock the shot.

## 2. Human Authorization

The human explicitly authorized K247 to download the existing successful Dreamina result for submit_id:

```text
37d02a39-7ca3-4141-b5ce-3e578622843e
```

This authorization was download-only.

## 3. Boundaries

- No submit was run.
- No retry was run.
- No resubmit was run.
- No batch execution was run.
- No new generation task was created.
- No `list_task` command was run.
- Exactly one download command was run for the existing successful submit_id.
- No review frames were created.
- No contact sheets were created.
- Downloaded media was not staged.
- No `sources/` files were created, edited, deleted, renamed, moved, staged, committed, or pushed by Codex.
- No prompt txt file was modified.
- No package JSON file was modified.
- No manifest CSV file was modified.
- No shot record was modified.
- No runtime/config/auth/session/token/key/env file was modified or printed.
- No signed download URL is printed in this report.
- `final_master=false`.
- `locked=false`.
- `visual_success_claimed=false`.
- No final approval is claimed.

## 4. Git / Source Preflight

Commands run:

```powershell
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
```

Result:

- branch status: `## main...origin/main`
- `sources/`: clean
- known allowed workspace noise present:
  - `.vs/`
  - `reports/context_recovery/`

K247 was not blocked by dirty sources.

## 5. K245 / K246 Submit and Query Verification

Read:

- `reports/PHASE_K245_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_ONE_SUBMIT_RESULT.md`
- `reports/PHASE_K246_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_QUERY_RESULT_NO_DOWNLOAD.md`

Verified:

- submit_id: `37d02a39-7ca3-4141-b5ce-3e578622843e`
- K245 logid: `202606301414371692540470086459864`
- K245 gen_status: `querying`
- K245 `no_query_confirmation=true`
- K245 `no_download_confirmation=true`
- K246 gen_status: `success`
- K246 queue_status: `Finish`
- K246 result_images_count: `0`
- K246 result_videos_count: `1`
- K246 download_url_present: `true`
- K246 `no_download_confirmation=true`
- `final_master=false`
- `locked=false`

## 6. Source Files Inspected

The required source/reference files existed and were readable:

- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/dreamina_cli_help_latest.md`

Relevant Source conclusions:

- download-only requires explicit authorization.
- submit, query, download, retry, and resubmit remain separate gates.
- download success does not equal visual success.
- visual success does not equal final or lock.
- `final_master=false` and `locked=false` remain required.

## 7. Dreamina Executable Path

K247 used the explicitly authorized Dreamina executable:

```text
C:\Users\msjpurf\bin\dreamina.exe
```

## 8. `dreamina version` Summary

Command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' version
```

Result: success.

Summary:

- version: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`

No logger Access denied was observed.

## 9. `dreamina user_credit` Summary

Command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' user_credit
```

Result: success.

Non-sensitive summary:

- total_credit: `1619`
- vip_level: `maestro`

No auth token, session token, cookie, key, or env value was printed in this report.

No missing login/auth failure was observed.

## 10. `dreamina query_result -h` Summary

Command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result -h
```

Result: success.

Confirmed:

- `query_result` accepts `--submit_id`
- `query_result` accepts `--download_dir`
- `--download_dir` is the download parameter and was only used in K247 because K246 already returned success and the human authorized download-only.

## 11. Exact Download Command Used

```powershell
$downloadDir = 'productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437'
New-Item -ItemType Directory -Force -Path $downloadDir | Out-Null
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id 37d02a39-7ca3-4141-b5ce-3e578622843e --download_dir $downloadDir
```

Command exclusions:

- no submit command
- no retry
- no resubmit
- no batch
- no `list_task`
- no second `query_result`
- no review frame/contact sheet command

## 12. Download Directory

```text
productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437
```

## 13. Downloaded File

Downloaded local file:

```text
productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437/37d02a39-7ca3-4141-b5ce-3e578622843e_video_1.mp4
```

Absolute local file:

```text
G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437\37d02a39-7ca3-4141-b5ce-3e578622843e_video_1.mp4
```

## 14. File Size and SHA-256

- file exists: true
- file size bytes: `11431647`
- sha256: `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418`
- extension: `.mp4`
- last_write: `2026-06-30T14:28:46`

## 15. Media Metadata

`ffprobe` availability:

- `ffprobe_unavailable=true`

Local metadata validation is partial because `ffprobe` was not available in PATH.

Dreamina download response metadata for the downloaded video:

- fps: `24`
- width: `1280`
- height: `720`
- format: `mp4`
- duration: `5.042`

## 16. Signed URL Redaction Confirmation

- signed URL present in earlier K246 raw query response: true
- signed URL printed in this report: false
- signed URL printed in final report fields: false

## 17. Post-Download Boundary Confirmation

- no retry: true
- no resubmit: true
- no batch: true
- no review frames created: true
- no contact sheets created: true
- media_not_staged=true
- `final_master=false`
- `locked=false`
- `visual_success_claimed=false`
- final approval claimed: false

## 18. Recommended Next Step

Recommended next step:

`K248 local review artifacts / contact sheet after human authorization`

Reason:

- K247 downloaded one mp4 successfully.
- No visual review artifact was created in K247.
- No visual success is claimed.

## 19. Final Verdict

`K247_TEXT2VIDEO_DOWNLOAD_SUCCESS_READY_K248_REVIEW_ARTIFACTS_DECISION`
