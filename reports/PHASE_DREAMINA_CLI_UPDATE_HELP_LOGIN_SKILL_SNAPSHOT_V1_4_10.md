# PHASE DREAMINA CLI UPDATE HELP LOGIN SKILL SNAPSHOT V1.4.10

## 1. Phase Summary

This phase refreshed the local Dreamina CLI evidence after the official v1.4.10 update note, captured a sanitized help snapshot, inspected the newly installed Dreamina `SKILL.md`, and checked login/account state.

This phase is separate from SHOT-04 R02a K269D.

No generation, query, download, retry, resubmit, batch, media creation, Source modification, final, or lock action was performed.

Final phase status:

`login_pending_user_action`

## 2. Authorization And Boundaries

Authorization level:

`CLI maintenance / help snapshot / login canary only`

Allowed actions used:

- run current CLI version/help/user_credit checks
- run official update command
- run help-only commands
- inspect non-sensitive installer metadata
- inspect installed Dreamina `SKILL.md`
- run headless login and checklogin
- create one report
- create one sanitized help snapshot

Explicitly not authorized and not performed:

- text2image generation
- image2image generation
- text2video generation
- image2video generation
- frames2video generation
- multiframe2video generation
- multimodal2video submit
- image_upscale generation
- query_result
- list_task execution beyond `-h`
- download
- retry
- resubmit
- batch
- media creation
- `sources/` modification
- media staging
- token/cookie/session/auth/env printing
- signed URL printing
- full `user_id` printing in this report
- logout or relogin
- final
- lock

## 3. Git/Source Preflight

Commands run:

```text
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
git -c core.quotepath=false diff --name-only
git -c core.quotepath=false diff --cached --name-only
```

Preflight result:

```text
## main...origin/main
?? .vs/
?? productions/chi_yan_tian_qiong/edits/
?? reports/context_recovery/
```

`sources/` status output was empty.

Tracked diff was empty before this phase.

Staged diff was empty before this phase.

Known untracked noise remained:

- `.vs/`
- `productions/chi_yan_tian_qiong/edits/`
- `reports/context_recovery/`

## 4. Pre-Update CLI Snapshot

PowerShell command:

```text
where.exe dreamina
```

Result:

```text
C:\Users\msjpurf\bin\dreamina.exe
```

PowerShell `dreamina version` result:

```json
{
  "version": "2a20fff-dirty",
  "commit": "2a20fff",
  "build_time": "2026-06-26T06:36:39Z"
}
```

This means the PowerShell-visible local CLI was already newer than the K268 old known version:

```text
46b5b0e-dirty / commit 46b5b0e / build_time 2026-06-03T19:39:25Z
```

PowerShell `dreamina -h` succeeded.

PowerShell `dreamina user_credit` succeeded. Sensitive `user_id` was not recorded here.

Non-sensitive account fields:

- `vip_level`: `maestro`
- `total_credit`: `1637`

## 5. Update Command Result

Command executed:

```text
curl -fsSL https://jimeng.jianying.com/cli | bash
```

Execution form:

```text
bash -lc "curl -fsSL https://jimeng.jianying.com/cli | bash"
```

Exit code: `0`

Installer result:

- downloaded Linux Dreamina CLI binary
- downloaded `SKILL.md`
- downloaded `version.json`
- installed binary to `/home/ke/.local/bin/dreamina`
- downloaded skill to `/home/ke/.dreamina_cli/dreamina/SKILL.md`
- wrote `/home/ke/.local/bin` PATH guidance into `/home/ke/.bashrc`
- printed instruction to run `export PATH="/home/ke/.local/bin:$PATH"` or reopen terminal

Environment note:

The installer ran in the bash/Linux environment. It did not replace the PowerShell-visible executable at `C:\Users\msjpurf\bin\dreamina.exe`.

## 6. Post-Update CLI Version

Linux installed binary:

```text
/home/ke/.local/bin/dreamina
```

File type:

```text
ELF 64-bit LSB executable, x86-64, dynamically linked
```

Linux installed binary `version` output:

```json
{
  "version": "2a20fff-dirty",
  "commit": "2a20fff",
  "build_time": "2026-06-26T06:36:39Z"
}
```

Installer metadata file:

```text
/home/ke/.dreamina_cli/version.json
```

Metadata content:

```json
{
  "version": "1.4.10",
  "release_date": "2026-06-26",
  "release_notes": "text2image、image2image 支持通过 generate_num 参数一次生成 1-10 张图片；\n新增对 seedance2.0_vip 4k 分辨率的支持；\n修复图片超清任务结果查询失败的问题；\n修复 image2video 在部分情况下生成失败的问题；调整视频模型名称，将原本的 3.x 模型名改为 Seedance 1.x 模型名称，与Web端保持命名一致。\n更新命令：curl -fsSL https://jimeng.jianying.com/cli | bash"
}
```

Update changed the bash/Linux installed CLI metadata to v1.4.10 and installed the Linux binary. The PowerShell-visible executable was already at the same commit/build and remained located under `C:\Users\msjpurf\bin`.

## 7. Post-Update Help Snapshot Summary

Sanitized help snapshot created:

`reports/diagnostics/DREAMINA_CLI_HELP_SNAPSHOT_AFTER_UPDATE_20260701.md`

Captured commands:

- `dreamina version`
- `dreamina -h`
- `dreamina login -h`
- `dreamina login checklogin -h`
- `dreamina user_credit -h`
- `dreamina query_result -h`
- `dreamina list_task -h`
- `dreamina session -h`
- `dreamina session create -h`
- `dreamina session list -h`
- `dreamina session search -h`
- `dreamina session rename -h`
- `dreamina session delete -h`
- `dreamina text2image -h`
- `dreamina image2image -h`
- `dreamina text2video -h`
- `dreamina image2video -h`
- `dreamina frames2video -h`
- `dreamina multiframe2video -h`
- `dreamina multimodal2video -h`
- `dreamina image_upscale -h`

All captured commands were help/version only. No generation command was submitted.

Key help snapshot findings:

- `text2image` supports `--generate_num` with range `1-10`.
- `image2image` supports `--generate_num` with range `1-10`.
- `text2video` supports `seedance2.0_vip`, `duration 4-15`, `ratio 16:9`, and `video_resolution 720p, 1080p, or 4k`.
- `image2video` supports `seedance2.0_vip` with `video_resolution 720p, 1080p, or 4k`.
- `frames2video` supports `seedance2.0_vip` with `video_resolution 720p, 1080p, or 4k`.
- `multimodal2video` supports repeated `--image` via `--image stringArray`.
- `multimodal2video` supports `seedance2.0_vip`, `seedance2.0mini`, `duration 4-15`, `ratio 16:9`, and `video_resolution 720p, 1080p, or 4k`.
- Video model names now include `seedance1.0fast`, `seedance1.0`, and `seedance1.5pro` for image/video routes where relevant.
- Several video help pages warn that some high content safety risk models may require first-use authorization on Dreamina Web before retrying after `AigcComplianceConfirmationRequired`.

## 8. Installed SKILL.md Summary

Installed skill path:

```text
/home/ke/.dreamina_cli/dreamina/SKILL.md
```

Status: present

Size:

```text
6518 bytes
```

SHA-256:

```text
869f6a1e4664688b2224c26e0b086dc2191c35f56b382e5d2679e46c11d030a9
```

Operational summary:

- Treat `dreamina -h` and `dreamina <subcommand> -h` as the primary reference for exact flags and supported combinations.
- Reuse current login state unless the user explicitly asks for `login`, `relogin`, `logout`, or `checklogin`.
- Warn before running commands that may consume credits.
- Be explicit about whether a task is help-only inspection, real submit, or query follow-up.
- For async generation, do not rely on shell exit code alone; treat submit success as requiring `submit_id` plus `gen_status=querying` or `gen_status=success`.
- If `gen_status=fail`, inspect `fail_reason`.
- Use `query_result` only when a `submit_id` exists.
- Use `list_task` for saved task history only when authorized.
- Some models may require web-side compliance authorization.

Priority note:

The installed `SKILL.md` is useful operational guidance, but current `dreamina -h` and subcommand help remain the authoritative command surface.

## 9. Login/Account Verification Result

PowerShell-visible CLI:

- `dreamina user_credit` succeeded before update.
- `vip_level`: `maestro`
- `total_credit`: `1637`
- `user_id`: returned by CLI but redacted from this report.

Linux installed CLI:

- `dreamina login --headless` returned OAuth Device Flow authorization material.
- `verification_uri` and `user_code` were shown to the human in the Codex conversation, not persisted in this report.
- `device_code` was used only for `checklogin` and is redacted from this report.
- `dreamina login checklogin --poll=120` timed out with: `等待登录超时，请重试`
- `dreamina user_credit` after the timed-out Linux checklogin failed with: `未检测到有效登录态，请先执行 dreamina login`

Login status for the newly installed Linux CLI:

`pending`

Phase status:

`login_pending_user_action`

## 10. Version/Help Delta Versus Previous Known CLI

Previous known K268 local CLI:

```text
version: 46b5b0e-dirty
commit: 46b5b0e
build_time: 2026-06-03T19:39:25Z
```

Current CLI binary version:

```text
version: 2a20fff-dirty
commit: 2a20fff
build_time: 2026-06-26T06:36:39Z
```

Installer metadata:

```text
version: 1.4.10
release_date: 2026-06-26
```

Delta answers:

| Question | Answer |
|---|---|
| Does `text2image` support `generate_num`? | yes, `1-10` |
| Does `image2image` support `generate_num`? | yes, `1-10` |
| Does `seedance2.0_vip` now support `4k` video_resolution anywhere? | yes, in `text2video`, `image2video`, `frames2video`, and `multimodal2video` help |
| Did video model names change from 3.x to Seedance 1.x? | yes, image/video route help now uses `seedance1.0fast`, `seedance1.0`, and/or `seedance1.5pro` where relevant |
| Does `multimodal2video` help differ from previous snapshot? | yes; it adds `seedance2.0mini` and `4k` for `seedance2.0_vip` |
| Does `image2video` help mention changed model names/fixes? | help now lists Seedance 1.x model names; installer metadata says image2video partial generation failure was fixed |
| Does `multimodal2video` still support repeated `--image`? | yes, `--image stringArray` |
| Does `text2video` still support `seedance2.0_vip`, duration `4-15`, ratio `16:9`, 720p/1080p/4k? | yes |
| Does `user_credit` work after update/login? | PowerShell-visible CLI works; newly installed Linux CLI is pending user login and `user_credit` fails until login is completed |

## 11. Relevance To K266/K268 Repeated Empty Submit Failure

K266 and K268 both failed on an older CLI generation path with:

- exit code `1`
- empty stdout/stderr
- no JSON
- no `submit_id`

Those attempts used the previous known local version:

`46b5b0e-dirty / 2026-06-03T19:39:25Z`

Current evidence shows:

- the PowerShell-visible CLI is now `2a20fff-dirty / 2026-06-26T06:36:39Z`
- the official installer metadata is v1.4.10 from 2026-06-26
- help has materially changed for image/video model support and 4k support
- `multimodal2video` still supports repeated `--image`
- PowerShell-visible `user_credit` succeeds
- Linux-installed CLI still needs user login completion

Interpretation:

The repeated empty K266/K268 submit failure may have been related to the old CLI build or an old multimodal upload/provider issue. This phase cannot prove the failure is fixed because no generation submit was authorized or run.

Any future K269D/K269 submit decision should re-check command-contract help from this refreshed snapshot and run a fresh canary/login preflight in the actual execution environment before any one-submit-only phase.

## 12. Recommended Next Phase

Because the newly installed Linux CLI login remains pending:

`DREAMINA_CLI_CHECKLOGIN_AFTER_USER_AUTH`

After login is completed or if the project chooses to use the PowerShell-visible CLI that already has working `user_credit`, the SHOT-04 R02a route can continue separately with:

`K269D_HUMAN_DECISION_SAFE_VARIANT_SUBMIT_AUTHORIZATION`

K269D should remain report-only and should not run Dreamina, submit, query, download, retry, resubmit, final, or lock.

## 13. Explicit Non-Actions

This phase did not:

- run `text2image` generation
- run `image2image` generation
- run `text2video` generation
- run `image2video` generation
- run `frames2video` generation
- run `multiframe2video` generation
- run `multimodal2video` submit
- run `image_upscale` generation
- run `query_result`
- run `list_task` except help-only `list_task -h`
- download
- retry
- resubmit
- batch
- create media
- modify `sources/`
- stage media
- print tokens/cookies/session/auth/env contents
- print signed URLs
- persist full `user_id`
- run logout
- run relogin
- final
- lock

## 14. Safety Flags

- no_generation_submit: `true`
- no_query: `true`
- no_download: `true`
- no_retry: `true`
- no_resubmit: `true`
- no_batch: `true`
- no_media_created: `true`
- sources_modified: `false`
- tokens_cookies_session_auth_env_printed_in_report: `false`
- signed_urls_printed: `false`
- user_id_redacted: `true`
- final_master: `false`
- locked: `false`

## 15. Final Verdict

`DREAMINA_CLI_LOGIN_PENDING_USER_ACTION_HELP_SNAPSHOT_CREATED`
