# SHOT-02-KF-001 Image2Image Submit Report

## Result

- task_id: SHOT-02-KF-001
- run_dir: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001
- submit_id: 0b46db3e-af4e-43fd-8014-df587d76ef29
- query_status: querying
- download_happened: False
- output_path: 
- final_verdict: SHOT02_KF001_SUBMITTED_QUERYING

## Exact CLI command used

`powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\manual_SHOT-02-KF-001_combat_keyframe_prompt.txt"
C:\Users\msjpurf\bin\dreamina.exe image2image --model_version 4.7 --ratio 16:9 --resolution_type 2k --prompt "$prompt" --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png" --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png"
`

## Files

- provider_requests_jsonl: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001\provider_requests.jsonl
- provider_responses_jsonl: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001\provider_responses.jsonl
- job_store: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001\job_store.json
- execution_log: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001\execution_log.txt
- raw_submit_response: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001\raw_submit_response.txt
- raw_query_response: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_205320_SHOT-02-KF-001\raw_query_response.txt
- raw_download_response: not applicable

## Integrity summary

- not applicable; no download happened

## Visual audit

- not applicable; no download happened

## Safety confirmations

- retry: no
- resubmit: no
- batch: no
- parallel: no
- auto_continue: no
- runtime_code_modified: no
- configs_providers_json_modified: no
- source_files_modified: no
- writes_outside_workspace: no
