# PHASE K162R - SHOT-03 SPLIT02_POSE_KF_01 Corrected-Contract Submit Result

## Purpose

Corrected-contract K162R live Dreamina image2image submit for `SPLIT02_POSE_KF_01_column_edge_guard_compression`.

This phase was authorized for exactly one Dreamina image2image submit using the K160/K161-passed 5-ref package. No query or download was authorized.

## Human Authorization

The human explicitly authorized K162R:

> 授权 K162R：修正 checklogin 契约后，对 SPLIT02_POSE_KF_01 使用 K160/K161 通过的 5-ref image2image package 执行一次 Dreamina image2image submit。preflight 使用 dreamina version、dreamina user_credit、dreamina image2image -h；不要再使用顶层 dreamina checklogin。允许只 submit 一次；不要 query，不要 download，不要 retry，不要 resubmit。保持 final_master=false、locked=false。

## Files Inspected

| File | Status | Size Bytes |
|---|---:|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K162_SHOT03_SPLIT02_POSE_KF_SUBMIT_RESULT.md` | exists | 5487 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K161_SHOT03_SPLIT02_POSE_KF_FINAL_PRE_SUBMIT_CHECKLIST.md` | exists | 7640 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K160_SHOT03_SPLIT02_POSE_KF_PACKAGE_REVIEW.md` | exists | 11275 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K159_SHOT03_SPLIT02_POSE_KF_NO_SUBMIT_PACKAGE_READY.md` | exists | 9046 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_split02_pose_kf_01_image2image_package_no_submit.json` | exists | 5179 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_SPLIT02_POSE_KF_01_no_submit.csv` | exists | 1488 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` | exists | 1933 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md` | exists | 25217 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md` | exists | 7944 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md` | exists | 5454 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md` | exists | 9151 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md` | exists | 10075 |

## Source Governance Confirmation

- `sources/` was read-only.
- `git status --short -- sources/` returned clean.
- No `sources/` file was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Official Source update requires ChatGPT generation/review and human manual action.

## K162 Block Carry-Forward

- Previous K162 was blocked before submit.
- Previous submit count was 0.
- Previous failure was top-level `dreamina checklogin` exit code 1 with no output.
- K162R corrected the preflight and removed top-level `checklogin`.
- K162R did not run `dreamina checklogin`.
- K162R did not run `dreamina login checklogin`.
- K162R did not run login, logout, relogin, or headless login.

## Git / Worktree Preflight

| Check | Result |
|---|---|
| Branch status | `main...origin/main` |
| `git status --short` before report creation | only `.vs/` untracked |
| `sources/` clean | true |
| `.vs/` staged | false |

## Package Validation

| Check | Result |
|---|---|
| Package JSON parse | pass |
| Manifest CSV read | pass |
| Manifest row count | 1 |
| Prompt SHA256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| Prompt SHA256 matches expected | true |
| All 5 refs exist | true |
| task_type | `image2image` |
| model_version | `4.7` |
| ratio | `16:9` |
| resolution_type | `2k` |
| final_master | false |
| locked | false |
| human_submit_authorization_required | true |
| K160 decision present | true |
| K161 verdict present | true |
| K162 submit-count-0 block report present | true |

## Corrected Dreamina Preflight

| Step | Command | Result |
|---|---|---|
| 1 | `C:/Users/msjpurf/bin/dreamina.exe version` | pass |
| 2 | `C:/Users/msjpurf/bin/dreamina.exe user_credit` | pass |
| 3 | `C:/Users/msjpurf/bin/dreamina.exe image2image -h` | pass |

Dreamina version output:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

Dreamina user_credit output summary:

```json
{
  "total_credit": 1832,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

Top-level `checklogin` was not run. `login`, `logout`, `relogin`, `headless login`, and `login checklogin` were not run.

## Command Contract

From `dreamina image2image -h`:

- Repeated image reference input: `--images strings`
- Prompt input: `--prompt string`
- Model version flag: `--model_version string`
- Ratio flag: `--ratio string`
- Resolution type flag: `--resolution_type string`
- No-poll/no-download strategy: `--poll 0`
- Supported model versions include `4.7`.
- Supported ratios include `16:9`.
- Supported resolution types include `2k`.
- Help states image2image is asynchronous and `--poll 0` disables polling.

Command contract was safe for submit-only execution.

## Submit Command Shape

Sanitized command shape:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "<prompt file>"
C:/Users/msjpurf/bin/dreamina.exe image2image `
  --images "<@FENSHOU_IDENTITY_REF>" `
  --images "<@SHUANGJI_IDENTITY_REF>" `
  --images "<@V004_CORRIDOR_SCENE_REF>" `
  --images "<@SPLIT02_START_ANCHOR_CUT_B_START_03>" `
  --images "<@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01>" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio "16:9" `
  --resolution_type 2k `
  --poll 0
```

Reference labels used:

1. `@FENSHOU_IDENTITY_REF`
2. `@SHUANGJI_IDENTITY_REF`
3. `@V004_CORRIDOR_SCENE_REF`
4. `@SPLIT02_START_ANCHOR_CUT_B_START_03`
5. `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01`

No auth/session/token/key material was opened or printed.

## Submit Result

| Field | Value |
|---|---|
| submit_attempted | yes |
| submit_count | 1 |
| submit_id | `83628bbc-88bc-4c04-9e7c-11697c84fd95` |
| logid | `20260627202259169254047008060F141` |
| gen_status | `querying` |
| credit_count | 1 |
| fail_reason | none returned |

Sanitized stdout summary:

```json
{
  "submit_id": "83628bbc-88bc-4c04-9e7c-11697c84fd95",
  "logid": "20260627202259169254047008060F141",
  "gen_status": "querying",
  "credit_count": 1
}
```

The response also echoed the prompt text. No query or download was run after submit.

## Boundary Confirmation

- No query was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch execution was run.
- No media was manually created.
- No frames/contact sheets/cuts were created.
- No media was staged.
- Package JSON was not modified.
- Manifest CSV was not modified.
- Prompt txt was not modified.
- Shot record JSON was not created or modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `sources/` was untouched.
- `final_master=false`.
- `locked=false`.

## Recommended Next Phase

K163 should be a separate query authorization phase.

K163 must not auto-query unless the human explicitly authorizes. K163 should query the existing `submit_id` only. Download should happen only if explicitly authorized, or if the human authorizes query+download together in that phase.

## Source Update Recommendation

Do not update official Source in K162R.

The corrected checklogin contract should be considered for future Source update only after this submit/query cycle is resolved.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_SUBMITTED_NO_QUERY_NO_DOWNLOAD_PENDING_K163_AUTHORIZATION`
