# Phase G2.1 Existing Submit Query Report

- task_id: A-CH-A-SUBJECT-001
- submit_id: a97f7551-b598-4929-9314-ceac79f37f5a
- query_command: C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id a97f7551-b598-4929-9314-ceac79f37f5a
- query_status: success
- run_dir: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001

## Success branch details

- raw_response_path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/raw_responses/query_response_g2_1.json
- raw_download_path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/downloads/a97f7551-b598-4929-9314-ceac79f37f5a_image_1.png
- renamed_output_path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/output/A-CH-A-SUBJECT-001_fenshou_full_body_subject.png
- file_size: 1959523
- width: 1440
- height: 2560
- format: png
- openable: True
- sha256: 83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F

## Updated artifacts

- completed_tasks.csv: updated with completed row
- downloaded_files.csv: updated with downloaded artifact metadata
- provider_responses.jsonl: appended success entry
- raw_responses/query_response.json: updated to latest query success payload
- raw_responses/query_response_g2_1.json: latest query success payload
- raw_responses/download_response_g2_1.json: latest download payload
- job_store.json: task status set to completed and last_event set to g2_success_downloaded
- execution_log.txt: appended G2.1 success and download lines

## Safety proofs

- No new submit happened in this pass.
- No retry was performed.
- No external path was touched; all updated files and outputs remain under G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE.
- providers.json was not modified by this phase; allow_live_run remains false.

## Execution log tail

2026-06-14T00:26:49.046+08:00 phase=G2.1 mode=live status=success submit_id=a97f7551-b598-4929-9314-ceac79f37f5a query_command="C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id "a97f7551-b598-4929-9314-ceac79f37f5a"" raw_query_path=G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_162002_A-CH-A-SUBJECT-001\raw_responses\query_response_g2_1.json
2026-06-14T00:26:49.046+08:00 status=downloaded raw_download_path=G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/downloads/a97f7551-b598-4929-9314-ceac79f37f5a_image_1.png output_path=G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_162002_A-CH-A-SUBJECT-001\output\A-CH-A-SUBJECT-001_fenshou_full_body_subject.png file_size=1959523 openable=True width=1440 height=2560 format=png sha256=83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F

## Pytest

- Command: python -m pytest -q
- Result: python -m pytest -q -> passed

## Final verdict

PHASE_G2_1_SUCCESS_DOWNLOADED

