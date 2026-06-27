# PHASE K164 - SHOT-03 SPLIT02_POSE_KF_01 Download Ready

## Purpose

Download existing successful `SPLIT02_POSE_KF_01_column_edge_guard_compression` image2image result.

This phase downloaded the already-successful Dreamina image result for local human/ChatGPT review. It does not make a final visual pass/fail judgment.

## Human Authorization

The human explicitly authorized K164:

> 授权 K164：下载 SPLIT02_POSE_KF_01 的 Dreamina image2image 成功结果，submit_id=83628bbc-88bc-4c04-9e7c-11697c84fd95。只下载这个已有成功结果，不 submit 新任务，不 retry，不 resubmit，不重新 query 多次。下载后校验本地图片、记录路径/sha256/尺寸，创建 K164 下载报告。保持 final_master=false、locked=false，不做最终通过判定。

## Files Inspected

| File | Status | Size Bytes |
|---|---:|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K163_SHOT03_SPLIT02_POSE_KF_QUERY_STATUS.md` | exists | 5245 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K162R_SHOT03_SPLIT02_POSE_KF_SUBMIT_RESULT.md` | exists | 7789 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K162_SHOT03_SPLIT02_POSE_KF_SUBMIT_RESULT.md` | exists | 5487 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K161_SHOT03_SPLIT02_POSE_KF_FINAL_PRE_SUBMIT_CHECKLIST.md` | exists | 7640 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K160_SHOT03_SPLIT02_POSE_KF_PACKAGE_REVIEW.md` | exists | 11275 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md` | exists | 25217 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md` | exists | 7944 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md` | exists | 9151 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md` | exists | 10075 |

## Source Governance Confirmation

- `sources/` was read-only.
- `git status --short -- sources/` returned clean.
- No `sources/` file was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Official Source update requires ChatGPT generation/review and human manual action.

## K163 Carry-Forward

| Field | Value |
|---|---|
| keyframe_id | `SPLIT02_POSE_KF_01_column_edge_guard_compression` |
| task_type | `image2image` |
| submit_id | `83628bbc-88bc-4c04-9e7c-11697c84fd95` |
| K163 query_count | 1 |
| gen_status/status | `success` |
| result image count | 1 |
| expected width | 2560 |
| expected height | 1440 |
| download_url_present | true |
| K163 downloaded | false |
| K163 retry/resubmit | false |
| final_master | false |
| locked | false |

## Git / Worktree Preflight

| Check | Result |
|---|---|
| Branch status | `main...origin/main` |
| `git status --short` before report creation | only `.vs/` untracked |
| `sources/` clean | true |
| `.vs/` staged | false |

## Download Command Shape

Sanitized download command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result `
  --submit_id 83628bbc-88bc-4c04-9e7c-11697c84fd95 `
  --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/"
```

Download execution rules observed:

- `submit_id` used: `83628bbc-88bc-4c04-9e7c-11697c84fd95`
- `download_dir`: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/`
- Exactly one download command was executed.
- No separate status-only query was run before download.
- No second download command was run.
- No submit/retry/resubmit/batch was run.

## Download Result

| Field | Value |
|---|---|
| download_attempted | yes |
| download_count | 1 |
| submit_id | `83628bbc-88bc-4c04-9e7c-11697c84fd95` |
| output_dir | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/` |
| file count downloaded | 1 |
| CLI gen_status | `success` |
| CLI queue_status | `Finish` |
| fail_reason | none returned |

Downloaded local image:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/83628bbc-88bc-4c04-9e7c-11697c84fd95_image_1.png`

## Local Image Validation

| File Path | Exists | Size Bytes | SHA256 | Format | Width | Height | Color / Mode Info | Dimensions Match K163 Expected |
|---|---:|---:|---|---|---:|---:|---|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/83628bbc-88bc-4c04-9e7c-11697c84fd95_image_1.png` | true | 4285884 | `d328bc4fb0e8f630925d9d9508ecb1394b55de023313900ec50ba2e4e4fa9284` | PNG | 2560 | 1440 | `Format24bppRgb` | true |

## Boundary Confirmation

- No submit was run.
- No new Dreamina task was created.
- No retry was run.
- No resubmit was run.
- No batch execution was run.
- No unrelated result was downloaded.
- No media was staged.
- Package JSON was not modified.
- Manifest CSV was not modified.
- Prompt txt was not modified.
- Shot record JSON was not created or modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `sources/` was untouched.
- `final_master=false`.
- `locked=false`.
- No final visual pass/fail judgment was made.

## Recommended Next Phase

K165 should be a human + ChatGPT visual review phase.

K165 should review the downloaded image and decide:

- usable as `SPLIT02_POSE_KF_01` candidate
- needs local contact/review sheet
- needs fallback 4-ref repackaging
- needs prompt revision
- abandon SPLIT-02 and use `CUT_B -> CUT_C` continuity

K165 must not mark final/locked unless the human explicitly authorizes.

## Source Update Recommendation

Do not update official Source in K164.

Wait until the visual review cycle resolves before proposing Source V1.12 material.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_IMAGE_DOWNLOADED_READY_HUMAN_CHATGPT_K165_REVIEW`
