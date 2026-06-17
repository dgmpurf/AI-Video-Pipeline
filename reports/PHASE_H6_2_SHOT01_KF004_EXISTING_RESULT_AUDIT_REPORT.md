# SHOT-01-KF-004 Existing Result Audit Report

## Existing Submit
- task_id: `SHOT-01-KF-004`
- submit_id: `36066c66-ab0b-4826-a60e-1d83b1b92877`
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_222650_SHOT-01-KF-004`
- query command: `C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id "36066c66-ab0b-4826-a60e-1d83b1b92877"`
- query_status: `success`
- download_happened: `true`
- download command: `C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id "36066c66-ab0b-4826-a60e-1d83b1b92877" --download_dir "G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_222650_SHOT-01-KF-004\downloads"`
- output_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_222650_SHOT-01-KF-004\output\SHOT-01-KF-004_branch_b_model_4_7_direction_fix_keyframe.png`
- integrity: `exists=True; file_size=4169476; sha256=fede0c5c9b32590dcd507d690adaa9403b8c973beae21d19917c60b7ac5b0c2d; openable=True; width=2560; height=1440; format=PNG`

## Prompt Audit
- manual prompt txt: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\manual_SHOT-01-KF-004_branch_b_model_4_7_direction_fix_prompt.txt`
- provider_requests.jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_222650_SHOT-01-KF-004\provider_requests.jsonl`
- prompt matched manual verified version: `true`
- provider parse error: ``
- Branch B direction-fix wording present: `true`
- banned center-anchor terms absent: `true`

## Duplicate Character Review
- duplicate male characters observed: `pending_visual_review`
- rerun decision: `pending_visual_review`

## Safety
- No rerun has been submitted by this audit step.
- No runtime code was modified.
- configs/providers.json was not modified.
- All writes stayed inside `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE`.

## Interim Verdict
- `SHOT01_KF004_EXISTING_SUCCESS_NEEDS_REVIEW`

## Visual Audit And Controlled Rerun
- duplicate male characters observed: `true`
- observation: `existing result contains the intended left black-red male plus an additional small red-black human silhouette in the left-background area`
- rerun_name: `SHOT-01-KF-004-rerun-02`
- rerun_run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_224008_SHOT-01-KF-004-rerun-02`
- rerun_submit_id: `df7642fd-f89f-4e1f-8d42-5844abb8f0b6`
- rerun_query_status: `querying`
- rerun_download_happened: `false`
- rerun_output_path: ``
- rerun_integrity: `not_run`
- rerun_exact_command_file: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_224008_SHOT-01-KF-004-rerun-02\reports\exact_rerun_command_used.ps1.txt`

## Final Verdict
- `SHOT01_KF004_PROMPT_MATCHED_RERUN_SUBMITTED_QUERYING`

