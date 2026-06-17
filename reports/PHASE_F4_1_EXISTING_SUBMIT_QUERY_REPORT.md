# Phase F4.1 Existing Submit Query Report

## 1) submit_id
- `68d6ccb1-6554-4db7-bb81-829ec5701432`

## 2) Query command used
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "query_result",
  "--submit_id",
  "68d6ccb1-6554-4db7-bb81-829ec5701432"
]
```

## 3) Query status
- `success`
- Query returncode: `0`
- Query stdout summary: `{
  "submit_id": "68d6ccb1-6554-4db7-bb81-829ec5701432",
  "gen_status": "success",
  "result_json": {
    "images": [
      {
        "image_url": "https://p11-dreamina-sign.byteimg.com/tos-cn-i-tb4s082cfz/b25e9d690eba4ce9a8bf36ef68c192de~tplv-tb4s082cfz-aigc_resize:0:0.png?lk3s=7c3bb0db&x-expires=1781366400&x-signature=JgPSHKyLGZmvxihQUibt%2FKT1d30%3D&format=.png",
        "width": 2560,
        "height": 1440
      }
    ],
    "videos": []
  },
  "credit_count": 3,
  "queue_info": {
    "que...`
- Query stderr summary: ``

## 4) Success download result
- raw_download_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\downloads\68d6ccb1-6554-4db7-bb81-829ec5701432_image_1.png`
- renamed output path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\output\DREAMINA_PREFLIGHT_TEXT2IMAGE_001.png`
- file_size: `4072996`
- width: `2560`
- height: `1440`
- Pillow status: `openable=true, format=PNG`

## 5) Safety proof
- No new submit happened.
- No text2image command was run.
- No retry happened.
- No batch or parallel command happened.
- No auto-continue happened.
- No external path was touched; all writes stayed under the existing run directory and workspace reports directory.
- `configs/providers.json` was not modified.

## 6) Updated artifacts
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001`
- job_store.json: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\job_store.json`
- execution_log.txt: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\execution_log.txt`

## 7) Pytest result
- Result: passed with exit code 0.

## 8) Final verdict
- `PHASE_F4_1_SUCCESS_DOWNLOADED`

