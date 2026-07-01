# DREAMINA CLI SOURCE UPDATE CANDIDATE 20260701

## 1. Phase Summary

This report-only phase creates Source update candidates after the Dreamina CLI v1.4.10 / 2026-06-26 help refresh.

These files are not official Source. They are candidate drafts for human and ChatGPT Project Source review.

Final verdict:

`DREAMINA_CLI_SOURCE_UPDATE_CANDIDATE_20260701_READY_FOR_HUMAN_MANUAL_SOURCE_REVIEW`

## 2. Authorization And Boundaries

Authorization level:

`L0 report-only / Source candidate drafting only`

This phase did not run Dreamina, `dreamina version`, `dreamina user_credit`, `dreamina -h`, subcommand help, submit, query, list_task, download, retry, resubmit, batch, or media generation.

Official Project Source remains human-controlled. Codex created only reports under `reports/`.

## 3. Git/Source Preflight

Commands run:

```text
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
git -c core.quotepath=false diff --name-only
git -c core.quotepath=false diff --cached --name-only
```

Observed status:

```text
## main...origin/main
?? .vs/
?? productions/chi_yan_tian_qiong/edits/
?? reports/context_recovery/
```

`sources/` status was empty. Tracked diff and staged diff were empty before drafting.

## 4. Evidence Files Read

- `reports/PHASE_DREAMINA_CLI_UPDATE_HELP_LOGIN_SKILL_SNAPSHOT_V1_4_10.md`
- `reports/diagnostics/DREAMINA_CLI_HELP_SNAPSHOT_AFTER_UPDATE_20260701.md`
- `sources/AI视频制作_Source索引与使用优先级_V1.9.md`
- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
- `sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `sources/dreamina_cli_help_latest.md`

## 5. Current Official Source Files Affected

Recommended replacement candidates:

- `sources/dreamina_cli_help_latest.md`
- `sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
- `sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `sources/AI视频制作_Source索引与使用优先级_V1.9.md`

Recommended addition candidate:

- `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`

## 6. Required Replacement/Addition List

| Candidate | Intended official Source action |
|---|---|
| `dreamina_cli_help_latest.md` | replace current help snapshot |
| `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md` | add as new execution-contract supplement |
| `Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md` | replace V1.1 workflow/spec |
| `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md` | replace V1.1 manifest schema |
| `AI视频制作_Source索引与使用优先级_V1.10_DreaminaCLI20260701更新候选.md` | replace Source Index V1.9 after human review |

## 7. Candidate File Inventory

Draft directory:

`reports/source_update_drafts/dreamina_cli_20260701/`

Files:

- `dreamina_cli_help_latest.md`
- `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
- `Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
- `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`
- `AI视频制作_Source索引与使用优先级_V1.10_DreaminaCLI20260701更新候选.md`

## 8. Summary Of Key CLI Changes

- PowerShell-visible CLI: `2a20fff-dirty / commit 2a20fff / build_time 2026-06-26T06:36:39Z`
- Installer metadata: `v1.4.10 / 2026-06-26`
- `text2image` now supports `--generate_num` range `1-10`.
- `image2image` now supports `--generate_num` range `1-10`.
- `seedance2.0_vip` now supports `video_resolution 4k` in `text2video`, `image2video`, `frames2video`, and `multimodal2video`.
- `seedance2.0mini` appears in video command model lists where shown by help.
- `image2video` and `frames2video` use updated Seedance 1.x model naming where shown by help.
- `multimodal2video` still supports repeated `--image` via `--image stringArray`.
- Submit/query/download/retry/resubmit/final/lock remain separate gates.

## 9. PowerShell vs Linux CLI Environment Distinction

Preferred live execution path for now:

`C:/Users/msjpurf/bin/dreamina.exe`

Reason:

- PowerShell-visible CLI returned version `2a20fff-dirty`.
- PowerShell-visible CLI `user_credit` succeeded with `vip_level=maestro` and `total_credit=1637`.

Linux installed path:

`/home/ke/.local/bin/dreamina`

Status:

- Installed by the official update command.
- Same binary build/version output.
- Login remains `login_pending_user_action`.
- Do not use Linux CLI for live submit unless `checklogin` and `user_credit` succeed in that environment.

## 10. Impact On SHOT-04 R02a K269D/K269 Submit Planning

K266/K268 repeated empty submit failures happened on an older CLI evidence chain. The refreshed CLI materially changes command help and may affect future submit behavior, but no fix is proven until a future authorized submit succeeds.

Future K269D/K269 planning should:

- treat this Source update package as evidence only until human-applied
- prefer PowerShell CLI for live execution while Linux CLI login is pending
- re-run canary/preflight in the actual live phase
- keep one-submit-only boundaries explicit
- avoid automatic query/download/retry/resubmit

## 11. Human Manual Application Instructions

The human user should:

1. Review candidate drafts under `reports/source_update_drafts/dreamina_cli_20260701/`.
2. Optionally ask ChatGPT Project / ChatGPT Pro Extended to rewrite or compress the drafts into official Source style.
3. Manually upload or replace the approved files in ChatGPT Project Source.
4. Manually sync approved files into local `sources/` if desired.
5. After applying, future Codex tasks should read the new Source Index V1.10 and updated Dreamina CLI sources.

Codex must not perform the official Source replacement step.

## 12. Files Not To Replace Yet

Do not replace these based on this phase alone:

- prompt compiler Source files
- action/failure ledger Source files
- SHOT-04 R02 visual review or route reset Source files
- any prompt, package, manifest, media, runtime, config, auth, session, token, key, or env files

## 13. Risks And Open Questions

- Linux CLI login remains pending.
- PowerShell and Linux environments now both have a Dreamina binary, but only PowerShell has proven account credit access.
- v1.4.10 metadata and help changes do not prove K266/K268 empty submit failure is fixed.
- Official Source update should be reviewed by the human before any local `sources/` sync.
- The generated help candidate is a snapshot, not a rules explanation.

## 14. Recommended Next Human Action

Review the draft Source candidates and choose whether to manually apply them to ChatGPT Project Source and/or local `sources/`.

Recommended follow-up after manual application:

`DREAMINA_CLI_SOURCE_UPDATE_VERIFICATION_AFTER_HUMAN_APPLY`

## 15. Explicit Non-Actions

This phase did not:

- run Dreamina
- run help/version/user_credit commands
- submit
- query
- list_task
- download
- retry
- resubmit
- batch
- create media
- modify prompt/package/manifest files
- modify `sources/`
- stage `sources/`
- modify runtime/config/auth/session/token/key/env files
- print tokens/cookies/session/auth/env contents
- print signed URLs
- final
- lock
- tag

## 16. Safety Flags

- no_dreamina: `true`
- no_submit: `true`
- no_query: `true`
- no_download: `true`
- no_retry_resubmit: `true`
- no_media: `true`
- sources_modified: `false`
- final_master: `false`
- locked: `false`

## 17. Final Verdict

`DREAMINA_CLI_SOURCE_UPDATE_CANDIDATE_20260701_READY_FOR_HUMAN_MANUAL_SOURCE_REVIEW`
