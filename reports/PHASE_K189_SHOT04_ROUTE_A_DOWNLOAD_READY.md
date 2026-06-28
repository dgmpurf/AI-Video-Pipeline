# PHASE K189 - SHOT-04 Route A Download Ready

## 1. Purpose

Download the existing successful SHOT-04 Route A Dreamina result for human and ChatGPT visual review.

Existing submit id:

`39f10fdc-50c8-4d03-ae59-c1189447300b`

## 2. Authorization Level

Authorization level: `download-only for existing successful submit_id`

Allowed:

- download the existing successful result for the exact submit id
- validate the downloaded local MP4
- create this K189 download report

Forbidden:

- submit
- retry
- resubmit
- batch
- final decision
- lock decision
- Source modification
- media staging

## 3. Human Authorization Quote

The human authorized K189:

> 授权 K189：下载 SHOT-04 Route A 既有成功结果，submit_id=39f10fdc-50c8-4d03-ae59-c1189447300b。只下载这个已成功结果，不 submit，不 retry，不 resubmit，不 batch，不 final，不 lock。下载后校验本地 mp4 路径、sha256、尺寸、时长、fps、frame count，并创建 K189 下载报告。媒体不 stage，只 stage/commit/push 文本报告。

## 4. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K188_SHOT04_ROUTE_A_QUERY_STATUS.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K187_SHOT04_ROUTE_A_L3_ONE_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K186_SHOT04_ROUTE_A_PACKAGE_REVIEW_READY_FOR_HUMAN_SUBMIT_DECISION.md`

## 5. Source Governance Confirmation

- `sources/` was clean at preflight.
- `sources/` was not modified.
- `sources/` was not staged.
- Official Source authority remains with the human user.
- This report is evidence only, not official Source.

## 6. K188 Carry-Forward

| field | value |
|---|---|
| submit_id | `39f10fdc-50c8-4d03-ae59-c1189447300b` |
| K187_logid | `20260628134823169254047008236EE77` |
| K188_gen_status | `success` |
| K188_queue_status | `Finish` |
| K188_result_videos_count | `1` |
| K188_result_images_count | `0` |
| K188_download_url_present | true |
| K188_credit_count | `70` |

K188 video metadata returned by query:

| field | value |
|---|---|
| fps | `24` |
| width | `1280` |
| height | `720` |
| format | `mp4` |
| duration | `5.042` |

## 7. Exact Download Command Used

`--download_dir` was used. No submit command was used.

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 39f10fdc-50c8-4d03-ae59-c1189447300b --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-V001_routeA_20260628_134823/"
```

## 8. Download Result

| field | value |
|---|---|
| download_attempted | true |
| download_count | `1` |
| output_dir | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-V001_routeA_20260628_134823/` |
| downloaded_file_count | `1` |
| downloaded_path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-V001_routeA_20260628_134823/39f10fdc-50c8-4d03-ae59-c1189447300b_video_1.mp4` |
| download_success | true |
| gen_status | `success` |
| queue_status | `Finish` |
| credit_count | `70` |

Raw response summary, excluding prompt text and any remote URL:

```json
{
  "submit_id": "39f10fdc-50c8-4d03-ae59-c1189447300b",
  "gen_status": "success",
  "result_json": {
    "images": [],
    "videos": [
      {
        "path": "G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\productions\\chi_yan_tian_qiong\\runs\\live\\SHOT-04-V001_routeA_20260628_134823\\39f10fdc-50c8-4d03-ae59-c1189447300b_video_1.mp4",
        "fps": 24,
        "width": 1280,
        "height": 720,
        "format": "mp4",
        "duration": 5.042
      }
    ]
  },
  "credit_count": 70,
  "queue_info": {
    "queue_idx": 0,
    "priority": 1,
    "queue_status": "Finish",
    "queue_length": 0
  }
}
```

## 9. Local MP4 Validation

| field | value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-V001_routeA_20260628_134823/39f10fdc-50c8-4d03-ae59-c1189447300b_video_1.mp4` |
| exists | true |
| sha256 | `0d98b2db9a1674da5a2de706cd89b024777fa8ae1f13105a9caac0c6e071c53a` |
| size_bytes | `10773401` |
| format | `mp4` |
| width | `1280` |
| height | `720` |
| fps | `24.119601328903656` |
| duration | `5.016666666666667` |
| frame_count | `121` |
| metadata_source | `python_cv2` |

## 10. Boundary Confirmation

| boundary | value |
|---|---:|
| submit_run | false |
| retry_run | false |
| resubmit_run | false |
| batch_run | false |
| final_master | false |
| locked | false |
| media_staged | false |

## 11. Recommended Next Phase

K190 = human + ChatGPT visual review.

Recommended K190 review input:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-V001_routeA_20260628_134823/39f10fdc-50c8-4d03-ae59-c1189447300b_video_1.mp4`

The human should upload the downloaded MP4 to ChatGPT for review. K190 must not mark final or locked unless explicitly authorized after review.

## 12. What Not To Do

- Do not submit.
- Do not retry.
- Do not resubmit.
- Do not stage media.
- Do not mark final.
- Do not lock.
- Do not update Source.

## 13. Safety Confirmation

- Exactly one download command was run for the existing successful submit id.
- No submit was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
- No media was staged.
- No prompt/package/manifest/shot-record files were modified.
- `sources/` was not modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- Auth/session/token/key/env files were not opened or staged.
- `final_master=false`
- `locked=false`

## 14. Final Verdict

SHOT04_ROUTE_A_VIDEO_DOWNLOADED_READY_HUMAN_CHATGPT_K190_REVIEW
