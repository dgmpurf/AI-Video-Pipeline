# PHASE K269O - SHOT-04 R02A Variant A Simplified M2V One-Submit Result

## 1. Phase summary

Phase: `K269O_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_ONE_SUBMIT_ONLY`

Purpose: execute exactly one Dreamina `multimodal2video` submit for SHOT-04 R02A Variant A simplified two-reference M2V diagnostic.

Authorization level: L3 one-submit-only.

Execution result:

- submit_executed: `true`
- submit_count: `1`
- command_exit_code: `0`
- status: `submit_success`
- final_master: `false`
- locked: `false`

Final verdict:

```text
K269O_VARIANT_A_M2V_SUBMIT_SUCCESS_READY_K269P_QUERY_AUTHORIZATION_DECISION
```

## 2. Human authorization carry-forward

K269M recommended existing Variant A as the next diagnostic M2V/ref-upload route.

K269N recorded human one-submit-only authorization for Variant A.

K269N final verdict:

```text
K269N_VARIANT_A_M2V_ONE_SUBMIT_AUTHORIZATION_RECORDED_READY_K269O
```

K269O is the actual one-submit-only live phase. K269O did not authorize or perform query, download, retry, resubmit, batch, final, or lock.

## 3. Selected Variant A

Selected route:

```text
existing Variant A simplified two-ref M2V diagnostic
```

Package variant id:

```text
VARIANT_A_SIMPLIFIED_TWO_REF_M2V
```

Semantic label:

```text
VARIANT_A_SIMPLIFIED_M2V_IDENTITY_PRESERVING
```

Asset id:

```text
SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001
```

Task type:

```text
multimodal2video
```

Command parameters:

- refs_count: `2`
- model_version: `seedance2.0_vip`
- duration: `5`
- ratio: `16:9`
- video_resolution: `720p`
- poll: `0`

## 4. Diagnostic intent

Variant A is diagnostic, not final-oriented.

It tests:

- whether refreshed PowerShell CLI can create an M2V task with two local image refs
- whether the old M2V/ref-upload/provider boundary still fails
- whether two refs can later improve identity continuity compared with prompt-only Variant C

Submit success is not query success.

Submit success is not download success.

Submit success is not visual success.

Query/download require later separate authorization.

## 5. Git/source preflight

Preflight commands run before Dreamina canary:

```text
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
git -c core.quotepath=false diff --name-only
git -c core.quotepath=false diff --cached --name-only
```

Observed branch status:

```text
## main...origin/main
?? .vs/
?? productions/chi_yan_tian_qiong/edits/
?? productions/chi_yan_tian_qiong/review_artifacts/
?? reports/context_recovery/
```

`sources/` status output: empty.

Tracked working tree diff output: empty.

Staged diff output: empty.

Known untracked workspace noise remained:

- `.vs/`
- `productions/chi_yan_tian_qiong/edits/`
- `productions/chi_yan_tian_qiong/review_artifacts/`
- `reports/context_recovery/`

K269O was not blocked by dirty sources, staged sources, unexpected tracked changes, or unrelated staged changes.

## 6. Files read

Required reports read:

- `reports/PHASE_K269N_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_SUBMIT_AUTHORIZATION_DECISION.md`
- `reports/PHASE_K269M_SHOT04_R02A_POST_VARIANT_C_VISUAL_ROUTE_DECISION.md`
- `reports/PHASE_K269L_SHOT04_R02A_VARIANT_C_TEXT2VIDEO_VISUAL_REVIEW.md`
- `reports/PHASE_K269C_SHOT04_R02A_SAFE_VARIANT_PACKAGE_SET_REVIEW.md`
- `reports/PHASE_K269B_SHOT04_R02A_NO_SUBMIT_SAFE_VARIANT_PACKAGE_SET.md`
- `reports/PHASE_K269A_SHOT04_R02A_NO_SUBMIT_SAFE_VARIANT_PLANNING.md`
- `reports/PHASE_K268F_SHOT04_R02A_REPEAT_SUBMIT_FAILURE_ROUTE_DECISION.md`
- `reports/PHASE_K268E_SHOT04_R02A_SUBMIT_INVOCATION_AND_LOG_EVIDENCE.md`

Variant A files read:

- `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001_multimodal2video_no_submit_prompt.txt`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A-safe-variant-set/K269B/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001_package.json`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A-safe-variant-set/K269B/SHOT-04-R02A-K269B_safe_variant_set_manifest.csv`
- `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`

Read-only Source context:

- `sources/AI视频制作_Source索引与使用优先级_V1.10.md`
- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/dreamina_cli_help_latest.md`
- `sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
- `sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`

K269O did not read or print token, cookie, session, auth, key, env, or signed URL contents.

## 7. Dreamina executable path

Dreamina executable used:

```text
C:/Users/msjpurf/bin/dreamina.exe
```

Linux CLI was not used:

```text
/home/ke/.local/bin/dreamina
```

## 8. Canary/preflight results

Canary command 1:

```text
C:/Users/msjpurf/bin/dreamina.exe version
```

Result:

- exit_code: `0`
- version: `2a20fff-dirty`
- commit: `2a20fff`
- build_time: `2026-06-26T06:36:39Z`

Canary command 2:

```text
C:/Users/msjpurf/bin/dreamina.exe user_credit
```

Result:

- exit_code: `0`
- user_credit_success: `true`
- vip_level: `maestro`
- total_credit: `6447`
- user_id: redacted
- no logger Access denied observed
- no auth/login failure observed

Canary command 3:

```text
C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h
```

Result:

- exit_code: `0`
- help_success: `true`
- repeated `--image`: supported
- at least one `--image` or `--video`: required and satisfied by Variant A
- `seedance2.0_vip`: supported
- duration `4-15`: supported; Variant A uses `5`
- ratio `16:9`: supported
- video_resolution `720p`: supported for `seedance2.0_vip`
- `--poll`: supported

Canary/preflight status:

```text
pass
```

## 9. Reference validation

Reference validation was performed before submit.

| Ref | Absolute path | Exists | Readable | Size bytes | SHA-256 | Expected match |
|---|---|---:|---:|---:|---|---:|
| `@FENSHOU_LOCKED_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `true` | `true` | `1959523` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | `true` |
| `@SHUANGJI_LOCKED_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `true` | `true` | `3874061` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | `true` |

Refs were not modified.

## 10. Command-contract verification

Runtime command-contract verification result:

```text
pass
```

Verified against `C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h`:

- command exists
- repeated `--image` accepted
- at least one image/video required; Variant A used two images
- image input count `2` is within image limit `<=9`
- no video/audio inputs used
- model `seedance2.0_vip` supported
- duration `5` within `4-15`
- ratio `16:9` supported
- video_resolution `720p` supported for `seedance2.0_vip`
- `--poll 0` supported
- no `--download_dir` used
- no `output_dir` passed as a submit flag

Package/hash verification:

| Artifact | SHA-256 | Expected match |
|---|---|---:|
| Variant A prompt | `dbb2e0881d8ba8d18d8b88b092e24e88824841e8f10392649e2b4cfb7510c9b8` | `true` |
| Variant A package | `9679649d2c68f4fa1d6addc4ff4e7277c85c4b15e3f36962283a2422227399ac` | `true` |
| K269B manifest | `052d925b377e886bd3b332be91453e9a157cbca8bde5fff6b1545b208baf7693` | `true` |

## 11. Submit command summary

Invocation style:

```text
powershell_argv_array
```

Submit command shape:

```text
C:/Users/msjpurf/bin/dreamina.exe multimodal2video
  --prompt <contents of Variant A prompt_path>
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png"
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png"
  --duration 5
  --ratio 16:9
  --video_resolution 720p
  --model_version seedance2.0_vip
  --poll 0
```

Submit command omissions:

- no `--download_dir`
- no query command
- no download command
- no `output_dir` submit flag
- no retry/resubmit/batch flag

## 12. Submit execution result

Submit executed exactly once.

Result:

- command_exit_code: `0`
- parseable_json: `true`
- submit_id_returned: `true`
- logid_returned: `true`
- gen_status_returned: `true`
- credit_count_returned: `true`

Returned fields:

- submit_id: `df668f21-6bf2-416e-964f-7dfc73995518`
- logid: `20260701231448169254047008411529F`
- gen_status: `querying`
- credit_count: `70`

Interpretation:

K269O created a remote async task and stopped immediately after submit result capture. `gen_status=querying` is not visual success, not query success, not download success, and not final approval.

## 13. Raw sanitized stdout/stderr summary

Sanitized submit response summary:

```json
{
  "submit_id": "df668f21-6bf2-416e-964f-7dfc73995518",
  "logid": "20260701231448169254047008411529F",
  "gen_status": "querying",
  "credit_count": 70
}
```

The raw submit response also echoed the Variant A prompt text. No signed URL was returned. No token, cookie, session, auth, key, env, or signed URL content was printed in this report.

## 14. Parsed returned fields

| Field | Value |
|---|---|
| `submit_id` | `df668f21-6bf2-416e-964f-7dfc73995518` |
| `logid` | `20260701231448169254047008411529F` |
| `gen_status` | `querying` |
| `credit_count` | `70` |
| `fail_reason` | empty / not returned |

## 15. Submit count confirmation

- submit_count: `1`
- query_count: `0`
- download_count: `0`
- retry_count: `0`
- resubmit_count: `0`
- batch_count: `0`
- final_master: `false`
- locked: `false`

## 16. Explicit non-actions

K269O did not:

- run more than one submit
- query_result
- list_task
- download
- pass `--download_dir`
- retry
- resubmit
- batch
- create media review artifacts
- cut video
- extract frames
- create contact sheets
- run K269P
- modify `sources/`
- modify prompt files
- modify package JSON
- modify manifest CSV
- modify refs
- modify runtime/config/auth/session/token/key/env files
- print tokens/cookies/session/auth/env contents
- print signed URLs
- stage media
- stage `.vs/`
- stage `reports/context_recovery/`
- stage `productions/chi_yan_tian_qiong/edits/`
- stage `productions/chi_yan_tian_qiong/downloads/`
- stage `productions/chi_yan_tian_qiong/review_artifacts/`
- set `final_master=true`
- set `locked=true`
- tag
- claim visual success

## 17. Boundary confirmations

Source governance:

- official Project Source files are human-controlled
- K269O read `sources/` as read-only context
- K269O did not create, edit, delete, rename, move, stage, commit, or push anything under `sources/`

Prompt/package/manifest governance:

- prompt files were not modified
- package JSON files were not modified
- manifest CSV files were not modified

Media governance:

- no media was downloaded
- no local review artifacts were created
- no frames/contact sheets were created
- refs were read-only and not modified

Approval governance:

- query requires later separate human authorization
- download requires later separate human authorization
- final/lock requires later separate human approval

## 18. Outcome classification

Outcome classification:

```text
submit_success
```

Supporting facts:

- Dreamina canary/preflight passed
- command contract passed
- Variant A prompt/package/manifest/ref validation passed
- exactly one submit executed
- process exit code was `0`
- parseable JSON returned
- `submit_id` returned
- `gen_status=querying`

K269O does not claim remote final success, download success, media quality, visual success, final, or lock.

## 19. Recommended next phase

Recommended next phase:

```text
K269P_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_QUERY_AUTHORIZATION_DECISION
```

K269P should be a report-only human authorization decision phase for a later query-only action against:

```text
df668f21-6bf2-416e-964f-7dfc73995518
```

K269P should not query, download, retry, resubmit, batch, final, or lock.

If K269P authorizes query, the later query-only phase should not include `--download_dir` unless separately authorized.

## 20. Final verdict

```text
K269O_VARIANT_A_M2V_SUBMIT_SUCCESS_READY_K269P_QUERY_AUTHORIZATION_DECISION
```
