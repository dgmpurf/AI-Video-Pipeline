# A-SC-TEMPLE-COURTYARD-003 Submit + Single Query Report

- task_id: `A-SC-TEMPLE-COURTYARD-003`
- target_asset: `A-SC-TEMPLE-COURTYARD-003_main_hall_frontal_axis_stage`
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_233709_A-SC-TEMPLE-COURTYARD-003`
- submit_id: `93594be1-b21d-4f01-accb-de27d5357c98`
- query_status: `querying`
- download_happened: `false`
- provider_requests_jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_233709_A-SC-TEMPLE-COURTYARD-003\provider_requests.jsonl`
- provider_responses_jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_233709_A-SC-TEMPLE-COURTYARD-003\provider_responses.jsonl`
- job_store: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_233709_A-SC-TEMPLE-COURTYARD-003\job_store.json`
- execution_log: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_233709_A-SC-TEMPLE-COURTYARD-003\execution_log.txt`

## Commands

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\manual_A-SC-TEMPLE-COURTYARD-003_main_hall_frontal_axis_stage_prompt.txt"
C:/Users/msjpurf/bin/dreamina.exe image2image --model_version 4.7 --ratio 16:9 --resolution_type 2k --prompt "$prompt" --images "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_141522_A-SC-TEMPLE-COURTYARD-002\output\A-SC-TEMPLE-COURTYARD-002_main_hall_front_combat_stage.png"
```

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id "93594be1-b21d-4f01-accb-de27d5357c98"
```

## Compliance

- one_submit_only: `true`
- one_query_only: `true`
- no_download: `true`
- no_retry: `true`
- no_resubmit: `true`
- no_batch: `true`
- no_parallel: `true`
- no_auto_continue_to_SHOT_02_KF_002: `true`
- runtime_code_modified: `false`
- configs/providers_json_modified: `false`
- source_files_modified: `false`
- approved_prompt_changed: `false`

## Final Verdict

`A_SC_TEMPLE_COURTYARD_003_SUBMITTED_QUERYING`
