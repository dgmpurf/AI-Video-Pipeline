# Phase F6.1 Existing Submit Query Report

## 1) task_id
- `A-SC-TEMPLE-COURTYARD-001`

## 2) submit_id
- `821c2865-26da-4c70-939f-07b4eb5a96d8`

## 3) query command used
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "query_result",
  "--submit_id",
  "821c2865-26da-4c70-939f-07b4eb5a96d8"
]
```

## 4) query status
- `success`
- Query returncode: `0`

## 5) Success download results
- raw_download_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\downloads\821c2865-26da-4c70-939f-07b4eb5a96d8_image_1.png`
- renamed output path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\output\A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png`
- file_size: `3563257`
- width: `2560`
- height: `1440`
- format: `PNG`
- sha256: `f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0`
- Pillow status: `openable=True`

## 6) Safety proof
- No new submit happened during this phase.
- No retry command was executed.
- Query path was constrained to the existing run directory and workspace.
- `providers.json` was not modified.
- External path proof: all writes remain under `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE` (run directory plus reports).

## 7) Updated artifacts
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001`
- query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\raw_responses\query_response.json`
- provider responses path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\raw_responses\download_response.json`
- completed_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\completed_tasks.csv`
- downloaded_files.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\downloaded_files.csv`
- job_store.json path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\job_store.json`
- execution_log.txt path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\execution_log.txt`

## 8) pytest result
- Result: passed with exit code 0 (requested test command executed).

## 9) Final verdict
- `PHASE_F6_1_SUCCESS_DOWNLOADED`
