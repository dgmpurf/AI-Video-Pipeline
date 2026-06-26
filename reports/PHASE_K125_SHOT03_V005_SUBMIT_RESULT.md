# PHASE K125 - SHOT-03 V005 Submit Result

## Purpose

SHOT-03 V005 live submit only.

This phase was authorized only for Dreamina canary, command-contract preflight, and exactly one `multimodal2video` submit with `--poll=0`.

## Human Authorization

The human explicitly approved K125 submit.

## Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K124_SHOT03_V005_PACKAGE_READY_AFTER_CHATGPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V005_uploadsafe_terrain_rebound_attack_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V005_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V005_uploadsafe.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V005_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.5.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`

Optional source checked and absent locally:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`

`sources/` was read-only. No file under `sources/` was modified or staged.

## Canary Result

Dreamina executable:

```text
C:/Users/msjpurf/bin/dreamina.exe
```

`dreamina version` succeeded:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

`dreamina user_credit` succeeded:

```json
{
  "total_credit": 1972,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

No auth/session/token/key/env contents were opened or printed.

## Command-Contract Preflight

Command checked:

```powershell
C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h
```

Preflight result: passed.

- executable path: `C:/Users/msjpurf/bin/dreamina.exe`
- version: `46b5b0e-dirty`
- task_type: `multimodal2video`
- repeated `--image`: supported
- at least one image/video required: true
- image limit: `image<=9`
- input count: `3`
- model_version: `seedance2.0_vip`
- duration: `5`, valid because supported range is `4-15`
- ratio: `16:9`, supported
- video_resolution: `720p`, supported for `seedance2.0_vip`
- `--poll=0`: disables polling
- all three input image paths exist: true
- prompt file exists: true
- command_contract_valid: true

## Exact Submit Command Used

Sanitized PowerShell command:

```powershell
$promptPath = "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V005_uploadsafe_terrain_rebound_attack_prompt.txt"
$prompt = Get-Content -Raw -Encoding UTF8 $promptPath
& "C:/Users/msjpurf/bin/dreamina.exe" multimodal2video `
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg" `
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg" `
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg" `
  --prompt $prompt `
  --duration=5 `
  --ratio=16:9 `
  --video_resolution=720p `
  --model_version=seedance2.0_vip `
  --poll=0
```

## Submit Response

- submit_id: `95fc3d24-405b-45e7-b2ac-bf7d47b02782`
- logid: `202606262044131692540470088936D2F`
- gen_status: `querying`
- credit_count: `70`
- fail_reason: `null`

Submit classification:

`submitted_querying_no_query_no_download`

## No-Query / No-Download Confirmation

- `query_result` was not run.
- Download was not run.
- No retry was run.
- No resubmit was run.
- No batch command was run.
- No media was created.
- No contact sheet or review frame was created.

## Updated Files

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V005_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K125_SHOT03_V005_SUBMIT_RESULT.md`

## Safety

- No retry.
- No resubmit.
- No query_result.
- No download.
- No media.
- `sources/` was not modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `final_master=false`.
- `locked=false`.
- SHOT-02 / V013 / V018 / V004 lock states were not touched.

## Next Step

K126 query/download requires separate human authorization. Do not query or download this submit_id from K125.

## Final Verdict

SHOT03_V005_SUBMITTED_NO_QUERY_NO_DOWNLOAD_PENDING_K126_AUTHORIZATION
