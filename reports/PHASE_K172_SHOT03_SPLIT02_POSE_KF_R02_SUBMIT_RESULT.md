# PHASE K172 - SHOT-03 SPLIT02_POSE_KF_01 R02 Submit Result

## Purpose

Human-authorized live Dreamina image2image submit for `SPLIT02_POSE_KF_01_R02_identity_repair`.

This phase submitted the K170/K171-passed R02 3-ref image2image package exactly once. It did not query, download, retry, resubmit, batch, create media, or mark final/locked.

## Human Authorization

Exact K172 authorization line:

> 授权 K172：对 SPLIT02_POSE_KF_01_R02_identity_repair 使用 K170/K171 通过的 3-ref image2image package 执行一次 Dreamina image2image submit。允许 Codex 先跑 corrected preflight：dreamina version、dreamina user_credit、dreamina image2image -h；不要使用顶层 dreamina checklogin。只 submit 一次；不要 query，不要 download，不要 retry，不要 resubmit。保持 final_master=false、locked=false。

## Files Inspected

| File | Status |
|---|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K171_SHOT03_SPLIT02_POSE_KF_R02_FINAL_PRE_SUBMIT_CHECKLIST.md` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K170_SHOT03_SPLIT02_POSE_KF_R02_PACKAGE_REVIEW.md` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K169_SHOT03_SPLIT02_POSE_KF_R02_NO_SUBMIT_PACKAGE_READY.md` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K168_SHOT03_SPLIT02_POSE_KF_R02_PROMPT_AUDIT.md` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K167_SHOT03_SPLIT02_POSE_KF_R02_IDENTITY_REPAIR_PROMPT_DRAFT.md` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_split02_pose_kf_01_R02_identity_repair_image2image_package_no_submit.json` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_SPLIT02_POSE_KF_01_R02_identity_repair_no_submit.csv` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_R02_identity_repair_DRAFT_prompt.txt` | exists |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md` | read-only inspected |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md` | read-only inspected |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md` | read-only inspected |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md` | read-only inspected |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md` | read-only inspected |

## Source Governance Confirmation

- `sources/` was read-only reference material.
- `git status --short -- sources/` returned clean.
- No file under `sources/` was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Official Source update requires ChatGPT generation/review and human manual action.

## K170 / K171 Carry-Forward

- K170 package review passed.
- K171 final pre-submit checklist passed.
- R02 3-ref package validated.
- Package files still record `submit_allowed=false`, but explicit human K172 authorization is present for one live submit.
- `final_master=false`.
- `locked=false`.

## Git / Worktree Preflight

| Check | Result |
|---|---|
| branch status before submit | `main...origin/main` |
| git status summary before submit | only `.vs/` untracked |
| sources/ clean | true |
| `.vs/` staged | false |

## Package Validation

| Check | Result |
|---|---:|
| package JSON parse | pass |
| package JSON SHA256 | `96781c671873b6f25732fe58b96f51a9547b57e18c8ff781e76375943f535679` |
| package JSON SHA256 matches expected | true |
| manifest CSV read | pass |
| manifest CSV SHA256 | `5d35e4fbe03c4b14140ce9de340f61440f740ee6d122ce7bd757969cfcd3b435` |
| manifest CSV SHA256 matches expected | true |
| manifest row count | 1 |
| prompt SHA256 | `47739cb33850d2d692ee13479dde8c13822acab34bc6ff94f55c4ecec06de853` |
| prompt SHA256 matches expected | true |
| all 3 primary refs exist | true |
| primary refs exactly match expected 3-ref route | true |
| V004/CUT_B/CUT_C excluded from primary submit | true |
| task_type | `image2image` |
| model_version | `4.7` |
| ratio | `16:9` |
| resolution_type | `2k` |
| final_master | false |
| locked | false |

Primary refs used:

- `@SHUANGJI_IDENTITY_REF`
- `@FENSHOU_IDENTITY_REF`
- `@K164_FAILED_IMAGE_COMPOSITION_ONLY`

## Corrected Dreamina Preflight

### Version

Command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe version
```

Result:

- version: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`

### User Credit

Command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe user_credit
```

Result:

- user_credit succeeded.
- vip_level: `maestro`
- total_credit_before_submit: `1831`
- user_id: `1611200923726843`

### image2image Help

Command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe image2image -h
```

Result:

- image2image help succeeded.
- Supported `model_version`: `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`.
- Supported `ratio`: includes `16:9`.
- Supported `resolution_type`: `2k`, `4k`.
- Repeated image reference flag: `--images`.
- Prompt flag: `--prompt`.
- No-poll flag: `--poll`; help states `0 disables polling`.

Top-level `dreamina checklogin` was not run.
`dreamina login`, `dreamina login checklogin`, logout, relogin, and headless login commands were not run.

## Command Contract

| Contract Item | Selected Flag / Value | Result |
|---|---|---:|
| repeated image reference input | `--images` repeated 3 times | pass |
| prompt input | `--prompt` | pass |
| model_version | `--model_version 4.7` | pass |
| ratio | `--ratio 16:9` | pass |
| resolution_type | `--resolution_type 2k` | pass |
| no-poll/no-download strategy | `--poll 0` | pass |
| command contract safe for submit-only | yes | pass |

## Submit Command Shape

Sanitized command shape:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "<R02 prompt file>"
C:/Users/msjpurf/bin/dreamina.exe image2image `
  --images "<@SHUANGJI_IDENTITY_REF>" `
  --images "<@FENSHOU_IDENTITY_REF>" `
  --images "<@K164_FAILED_IMAGE_COMPOSITION_ONLY>" `
  --prompt $prompt `
  --model_version 4.7 `
  --ratio 16:9 `
  --resolution_type 2k `
  --poll 0
```

Reference labels used:

- `@SHUANGJI_IDENTITY_REF`
- `@FENSHOU_IDENTITY_REF`
- `@K164_FAILED_IMAGE_COMPOSITION_ONLY`

No auth/session/token/key material is included in the command or report.

## Submit Result

| Field | Value |
|---|---|
| submit_attempted | yes |
| submit_count | 1 |
| submit_id | `b7756ff1-2530-4f49-ac86-e69fd35f4786` |
| logid | `20260627234035169254047008071FAB6` |
| gen_status | `querying` |
| credit_count | `1` |
| fail_reason | none returned |
| raw status field names returned | `submit_id`, `prompt`, `logid`, `gen_status`, `credit_count` |

Sanitized stdout/stderr summary:

- Dreamina returned a JSON object containing a valid `submit_id`.
- `gen_status=querying`.
- `credit_count=1`.
- No `fail_reason` was returned.
- The CLI echoed the prompt text in stdout; this report stores only a sanitized summary and command shape.

## Boundary Confirmation

- No query was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
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

Recommend K173 query authorization phase.

K173 must not auto-query unless the human authorizes it. K173 should only query status first, and download only if explicitly authorized or if the human authorizes query+download together.

## Source Update Recommendation

Do not update official Source in K172.

Wait until the R02 submit/query/download/visual-review cycle resolves before proposing Source updates.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_R02_SUBMITTED_NO_QUERY_NO_DOWNLOAD_PENDING_K173_AUTHORIZATION`
