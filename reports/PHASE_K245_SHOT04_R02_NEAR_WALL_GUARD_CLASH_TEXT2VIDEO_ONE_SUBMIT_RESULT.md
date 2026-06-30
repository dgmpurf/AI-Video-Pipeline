# PHASE K245 - SHOT-04 R02 Near-Wall Guard-Clash Text2Video One-Submit Result

## 1. Purpose

Record the human-authorized K245 L3 one-submit-only Dreamina `text2video` execution for the K243V/K244-approved SHOT-04 R02 near-wall guard-clash text2video package.

This phase records submit-only status. It does not query, download, review media, mark visual success, mark final, or lock the shot.

## 2. Human Authorization

Human authorization was explicit for K245:

- run corrected Dreamina live preflight;
- submit exactly one `text2video` task for `SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001`;
- do not query;
- do not download;
- do not retry;
- do not resubmit.

## 3. Boundaries

- Dreamina preflight was allowed and performed.
- Exactly one Dreamina `text2video` submit was performed.
- No `query_result` command was run.
- No `list_task` command was run.
- No download was performed.
- No retry or resubmit was performed.
- No batch execution was performed.
- No media, frames, or contact sheets were created.
- No media was staged.
- No `sources/` files were created, edited, deleted, renamed, moved, staged, committed, or pushed by Codex.
- No prompt txt file was modified.
- No package JSON file was modified.
- No manifest CSV file was modified.
- No shot record was modified.
- No runtime/config/auth/session/token/key/env file was modified or printed.
- `final_master=false`.
- `locked=false`.
- No visual success, final approval, or lock is claimed.

## 4. Git / Source Preflight

Commands run:

```powershell
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
```

Result:

- branch status: `## main...origin/main`
- `sources/`: clean
- known allowed workspace noise present:
  - `.vs/`
  - `reports/context_recovery/`
- no staged files before submit/report work

K245 was not blocked by dirty sources.

## 5. Source Files Inspected

All required Source files below existed and were readable:

- `sources/AI视频制作_Source索引与使用优先级_V1.8.md`
- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/dreamina_cli_help_latest.md`

Relevant Source conclusions:

- K245 remains a one-submit-only step requiring human authorization.
- Submit, query, download, retry, and resubmit remain separate authorization gates.
- `output_dir` / `output_name` are not submit parameters.
- Any output must still be queried/downloaded/reviewed only under later explicit authorization.
- `final_master=false` and `locked=false` remain required.

## 6. K243V / K244 Package Facts Verified

Primary package artifacts:

- K243V report requested by prompt as `_READY_NO_SUBMIT.md`: not present in the repo.
- Located authoritative K243V report referenced by K244: `reports/PHASE_K243V_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_READY.md`
- K244 review report: `reports/PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001_text2video_no_submit_prompt.txt`
- package JSON path: `productions/chi_yan_tian_qiong/prompts/shot_04_r02_v_near_wall_guard_clash_t2v_001_text2video_package_no_submit.json`
- manifest CSV path: `productions/chi_yan_tian_qiong/manifests/production_text2video_SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001_no_submit.csv`

Verified package facts:

- `asset_id=SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001`
- `task_type=text2video`
- `model_version=seedance2.0_vip`
- `ratio=16:9`
- `video_resolution=720p`
- `duration=5`
- `poll=0`
- `active_refs_count=0`
- prompt-only package
- no image/video/audio refs required
- `submit_allowed=false` in no-submit package metadata, overridden only by explicit K245 human L3 authorization for this one submit
- `query_allowed=false`
- `download_allowed=false`
- `retry_allowed=false`
- `resubmit_allowed=false`
- `final_master=false`
- `locked=false`
- K244 `package_review_status=pass_with_high_risk_notes_ready_for_human_K245_submit_authorization_decision`

Read / parse checks:

- prompt file exists and is UTF-8 readable
- package JSON parses
- manifest CSV reads
- no active refs are required
- no `output_dir` / `output_name` was passed to submit
- no `download_dir` was used

K243V recorded hashes matched local files:

- prompt sha256: `092757a60297391e467c2f402ae6173dda8cae87267d1f24f5b25ee2fcd15b82`
- package JSON sha256: `d1ef92d0d1ff9b8144c771e42debd190c2c3746e8ff9dc60fdf68df97157d4db`
- manifest CSV sha256: `f24502c5ac307c96febb2ff9eb57f689d7225f4b5ec6a1a7bbac1ac247ef6429`

## 7. Dreamina Executable Path

Project configuration explicitly points to:

```text
C:\Users\msjpurf\bin\dreamina.exe
```

`Get-Command dreamina` also resolved to:

```text
C:\Users\msjpurf\bin\dreamina.exe
```

K245 used this executable.

## 8. `dreamina version` Summary

Command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' version
```

Result: success.

Summary:

- version: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`

No logger Access denied was observed.

## 9. `dreamina user_credit` Summary

Command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' user_credit
```

Result: success.

Non-sensitive summary:

- total_credit: `1689`
- vip_level: `maestro`

No auth token, session token, cookie, key, or env value was printed in this report.

No missing login/auth failure was observed.

## 10. `dreamina text2video -h` Command-Contract Summary

Command:

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' text2video -h
```

Result: success.

Confirmed support:

- `--prompt`
- `--duration`
- `--ratio`
- `--video_resolution`
- `--model_version`
- `--poll`
- `seedance2.0_vip`
- ratio `16:9`
- `seedance2.0_vip` supports `720p`
- duration range includes `5`

K245 was not blocked by command contract.

## 11. Exact Submit Command Used

Prompt content was read from the verified prompt path. The prompt text is not reproduced here.

```powershell
$promptPath = 'productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001_text2video_no_submit_prompt.txt'
$prompt = Get-Content -LiteralPath $promptPath -Raw -Encoding UTF8
& 'C:\Users\msjpurf\bin\dreamina.exe' text2video --prompt $prompt --duration 5 --ratio '16:9' --video_resolution 720p --model_version seedance2.0_vip --poll 0
```

Submit command exclusions:

- no refs
- no `--image`
- no `--images`
- no `--video`
- no `--audio`
- no `--download_dir`
- no `--output_dir`
- no `--output_name`

## 12. Submit Response Summary

The single K245 submit command returned success at the CLI process level and produced an asynchronous task response:

```json
{
  "submit_id": "37d02a39-7ca3-4141-b5ce-3e578622843e",
  "logid": "202606301414371692540470086459864",
  "gen_status": "querying",
  "credit_count": 70
}
```

## 13. Returned Fields

- submit_id: `37d02a39-7ca3-4141-b5ce-3e578622843e`
- logid: `202606301414371692540470086459864`
- gen_status: `querying`
- credit_count: `70`
- fail_reason: not returned

## 14. Post-Submit Boundary Confirmation

- `no_query_confirmation=true`
- `no_download_confirmation=true`
- `retry_allowed=false`
- `resubmit_allowed=false`
- `final_master=false`
- `locked=false`
- visual success claimed: false
- final approval claimed: false

## 15. Recommended Next Step

Recommended next step:

`K246 query-only after human authorization`

Reason:

- K245 returned `gen_status=querying`.
- K245 did not query or download.
- The task may only be queried under a new explicit K246 query-only authorization.

If K246 later finds `gen_status=fail`, route to K245/K246 failure review rather than retrying or resubmitting automatically.

## 16. Final Verdict

`K245_TEXT2VIDEO_ONE_SUBMIT_ACCEPTED_READY_K246_QUERY_DECISION`
