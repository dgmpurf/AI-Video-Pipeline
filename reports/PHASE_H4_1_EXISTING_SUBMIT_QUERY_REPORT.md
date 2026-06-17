# Phase H4.1 Existing Submit Query Report

## 1) task_id and submit_id
- task_id: `SHOT-01-KF-002`
- submit_id: `6530e396-3a79-44bf-8623-2bc2e6ecc12f`

## 2) query command used
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "query_result",
  "--submit_id",
  "6530e396-3a79-44bf-8623-2bc2e6ecc12f"
]
```

## 3) query status
- `success`

## 4) success download result
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\raw_responses\query_response.json`
- raw_download_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\downloads\6530e396-3a79-44bf-8623-2bc2e6ecc12f_image_1.png`
- renamed_output_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\output\SHOT-01-KF-002_temple_gate_courtyard_standoff_keyframe.png`
- file_size: `4446578`
- width: `2560`
- height: `1440`
- format: `PNG`
- sha256: `E2EBAA26AF27D8D58FDE19EC45AE4AFF691DECC11C6B20910E92A062D82F9C7D`
- Pillow status: `True`

## 5) updated artifacts
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002`
- completed_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\completed_tasks.csv`
- downloaded_files.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\downloaded_files.csv`
- job_store.json path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\job_store.json`
- execution_log.txt path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\execution_log.txt`
- raw_responses/download_response_h4_1.json path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_074829_SHOT-01-KF-002\raw_responses\download_response_h4_1.json`

## 6) safety proof
- No new submit happened for this phase.
- No retry command was executed.
- Query executed only for `6530e396-3a79-44bf-8623-2bc2e6ecc12f`.
- All writes stayed inside workspace root.
- `configs/providers.json` line shows `"allow_live_run": false`.

## 7) pytest result
- `python -m pytest -q`

## 8) final verdict
- `PHASE_H4_1_SUCCESS_DOWNLOADED`
