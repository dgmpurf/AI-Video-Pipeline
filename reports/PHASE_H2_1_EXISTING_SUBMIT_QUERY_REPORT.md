# Phase H2.1 Existing Submit Query Report

## 1) task_id and submit_id
- task_id: `SHOT-01-KF-001`
- submit_id: `ccff71eb-e233-4a43-8ddc-7c756d1161bf`

## 2) query command used
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "query_result",
  "--submit_id",
  "ccff71eb-e233-4a43-8ddc-7c756d1161bf"
]
```

## 3) query result
- query status: `success`
- query returncode: `0`
- query stdout summary: `{ "submit_id": "ccff71eb-e233-4a43-8ddc-7c756d1161bf", "prompt": "Locked keyframe reference for shot SHOT-01-KF-001: a wide establishing composition of the ancient temple courtyard under light rain, wet stone ground with clear reflections, `
- query stderr summary: `empty`

## 4) success download result
- raw_download_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\downloads\ccff71eb-e233-4a43-8ddc-7c756d1161bf_image_1.png`
- renamed_output_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\output\SHOT-01-KF-001_temple_courtyard_standoff_keyframe.png`
- file_size: `4405469`
- width: `2560`
- height: `1440`
- format: `PNG`
- sha256: `0009c865f3fd2e259a6f9bcd902d82d5f6179b963398f1b5ad77d8bb072bf919`
- Pillow status: `True`

## 5) updated artifacts
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001`
- query raw response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\raw_responses\query_response.json`
- download response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\raw_responses\download_response.json`
- completed_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\completed_tasks.csv`
- downloaded_files.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\downloaded_files.csv`
- job_store.json path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\job_store.json`
- execution_log.txt path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_064100_SHOT-01-KF-001\execution_log.txt`

## 6) safety proof
- No new submit happened.
- No retry command was executed.
- Query was executed only for `ccff71eb-e233-4a43-8ddc-7c756d1161bf`.
- All writes stayed inside the workspace root.
- providers.json dreamina_cli.allow_live_run before: `false`
- providers.json dreamina_cli.allow_live_run after: `false`

## 7) pytest result
- `python -m pytest -q`

## 8) Final verdict
- `PHASE_H2_1_SUCCESS_DOWNLOADED`
