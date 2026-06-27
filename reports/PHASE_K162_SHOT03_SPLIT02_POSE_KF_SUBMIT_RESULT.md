# PHASE K162 - SHOT-03 SPLIT02_POSE_KF_01 Submit Result

## Purpose

Record the K162 human-authorized live-submit attempt boundary for `SPLIT02_POSE_KF_01_column_edge_guard_compression`.

K162 was authorized to submit exactly once only if all git, package, Dreamina canary/login, and image2image command-contract preflight checks passed.

## Git / Worktree Preflight

| Check | Result |
|---|---|
| Branch status | `main...origin/main` |
| `git status --short` | only `.vs/` untracked before K162 report creation |
| `sources/` status | clean |
| `.vs/` staged | no |
| Source modification allowed | no |
| Source modification observed | no |

## Package Validation Result

| Check | Result |
|---|---|
| Package JSON parse | pass |
| Manifest CSV read | pass |
| Manifest row count | 1 |
| Manifest required fields present | true |
| K160 pass decision present | true |
| K161 pass checklist present | true |
| Prompt file exists | true |
| Prompt SHA256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| Prompt SHA256 matches K161 expected value | true |
| All 5 primary refs exist | true |
| task_type | `image2image` |
| model_version | `4.7` |
| ratio | `16:9` |
| resolution_type | `2k` |
| submit_allowed | false |
| final_master | false |
| locked | false |

## Reference Set Checked

| Label | Path | Exists |
|---|---|---:|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | true |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | true |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | true |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | true |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | true |

## Dreamina Canary / Login / Contract Preflight

| Step | Command | Result |
|---|---|---|
| 1 | `C:/Users/msjpurf/bin/dreamina.exe version` | pass |
| 2 | `C:/Users/msjpurf/bin/dreamina.exe user_credit` | pass |
| 3 | `C:/Users/msjpurf/bin/dreamina.exe checklogin` | failed, exit code 1, no output returned |
| 4 | `C:/Users/msjpurf/bin/dreamina.exe image2image -h` | not run because checklogin preflight failed |

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

No auth/session/token/key contents were opened or printed.

## Submit Command Shape

No submit command was run.

Planned command shape, if a later phase is explicitly authorized after a passing preflight:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt"
C:/Users/msjpurf/bin/dreamina.exe image2image `
  --image "<@FENSHOU_IDENTITY_REF>" `
  --image "<@SHUANGJI_IDENTITY_REF>" `
  --image "<@V004_CORRIDOR_SCENE_REF>" `
  --image "<@SPLIT02_START_ANCHOR_CUT_B_START_03>" `
  --image "<@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01>" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio "16:9" `
  --resolution_type 2k `
  --poll 0
```

This planned command shape is informational only; it was not executed in K162.

## Submit Result

| Field | Value |
|---|---|
| submit attempted | no |
| submit count | 0 |
| failure position | Dreamina login/checklogin preflight |
| failure reason | `dreamina checklogin` returned exit code 1 with no output |
| submit_id | none |
| logid | none |
| gen_status | none |
| credit_count | none |
| fail_reason | preflight blocked before submit |

## Boundary Confirmation

- No query was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch execution was run.
- No media was created or edited.
- No media was staged.
- Package JSON was not modified.
- Manifest CSV was not modified.
- Prompt text was not modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `sources/` was not modified or staged.
- `final_master=false`.
- `locked=false`.

## Next Recommended Action

Before any future K162 retry or K163 live action, clarify the correct Dreamina login-check command for this CLI build. The user-requested top-level `dreamina checklogin` command failed even though `dreamina user_credit` succeeded.

A later human-authorized phase may choose either:

1. Treat successful `user_credit` as the login canary and use the CLI-supported login check command if documented locally.
2. Run a revised preflight that uses the correct login-check syntax for this Dreamina build.
3. Keep K162 blocked until a top-level `checklogin` command is available.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_BLOCKED_CHECKLOGIN_FAILED_NO_SUBMIT`
