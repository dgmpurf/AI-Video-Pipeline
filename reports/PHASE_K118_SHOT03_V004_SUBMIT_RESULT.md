# PHASE K118 - SHOT-03 V004 Submit Result

## Purpose

SHOT-03 V004 live submit only.

This phase runs the allowed Dreamina canary, command-contract preflight, and exactly one Dreamina `multimodal2video` submit for `SHOT-03-V004`.

## Human Authorization

The human explicitly approved K118 submit.

## Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K117_SHOT03_V004_PACKAGE_READY_AFTER_CHATGPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V004_uploadsafe.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.5.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`

The requested V1.3 Dreamina CLI source path was checked but was not present locally:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`

No `sources/` file was modified or staged.

## Preflight Git Status

Initial `git status --short` showed only:

```text
?? .vs/
```

`sources/` had no git status changes, so K118 was allowed to proceed.

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
  "total_credit": 2042,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

No auth/session/token/key/env contents were opened or printed.

## Command-Contract Preflight

Command checked:

```text
C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h
```

Preflight result: passed.

Verified contract:

- executable path: `C:/Users/msjpurf/bin/dreamina.exe`
- version: `46b5b0e-dirty`, commit `46b5b0e`, build time `2026-06-03T19:39:25Z`
- command help checked: `multimodal2video -h`
- task_type: `multimodal2video`
- supports repeated `--image`
- requires at least one `--image` or `--video`
- image limit: `image<=9`
- input count: `3`
- model_version: `seedance2.0_vip`
- duration: `5`, within supported `4-15`
- ratio: `16:9`, supported
- video_resolution: `720p`, supported for `seedance2.0_vip`
- `--poll=0` disables polling
- command_contract_valid: `true`

Input paths existed:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

Prompt file existed:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage_prompt.txt`

## Exact Submit Command Used

Sanitized PowerShell command shape:

```powershell
$exe = "C:/Users/msjpurf/bin/dreamina.exe"
$promptPath = "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage_prompt.txt"
$img1 = "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg"
$img2 = "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg"
$img3 = "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg"
$prompt = Get-Content -Raw -Encoding UTF8 $promptPath
& $exe multimodal2video --image $img1 --image $img2 --image $img3 --prompt $prompt --duration=5 --ratio=16:9 --video_resolution=720p --model_version=seedance2.0_vip --poll=0
```

No auth/session/token/key/env value is included.

## Submit Response

Submit command exit code: `0`

Response summary:

- submit_id: `6dd3f859-eb0c-4907-b6bf-0d576c1d8920`
- logid: `202606261501501692540470084823B1D`
- gen_status: `querying`
- credit_count: `70`
- fail_reason: `null`

## No-Query / No-Download Confirmation

- `query_result` was not run.
- No download command was run.
- No media was created.
- No contact sheet was created.
- No ffmpeg command was run.
- No retry was run.
- No resubmit was run.

## Updated Files

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K118_SHOT03_V004_SUBMIT_RESULT.md`

## Safety

- Exactly one Dreamina submit was run.
- No query_result was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No media was created, edited, or staged.
- `sources/` was not modified or staged.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `.vs/` was not staged.
- `final_master=false`.
- `locked=false`.

## Next Step

K119 query/download requires separate human authorization for this exact submit_id:

```text
6dd3f859-eb0c-4907-b6bf-0d576c1d8920
```

## Final Verdict

`SHOT03_V004_SUBMITTED_NO_QUERY_NO_DOWNLOAD_PENDING_K119_AUTHORIZATION`
