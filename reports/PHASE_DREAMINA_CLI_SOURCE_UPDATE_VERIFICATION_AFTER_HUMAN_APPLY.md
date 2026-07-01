# PHASE_DREAMINA_CLI_SOURCE_UPDATE_VERIFICATION_AFTER_HUMAN_APPLY

## 1. Phase summary

Purpose: verify the human-applied Dreamina CLI 20260701 Source update and V1.10.1 Source completion.

Verification result: content verification passed, but local `sources/` remains dirty because the human-applied Source changes are not yet committed.

Recommended next phase: `HUMAN_SOURCE_COMMIT_REQUIRED_BEFORE_K269D`.

## 2. Authorization and boundaries

Authorization level: L0 read-only verification report.

Codex was authorized to read `sources/` and create this evidence report only. Official Source remains human-controlled.

Boundaries observed:

- no Dreamina execution
- no `dreamina version`
- no `dreamina user_credit`
- no Dreamina help command
- no submit
- no query
- no download
- no retry or resubmit
- no media creation
- no prompt/package/manifest modification
- no `sources/` modification by Codex
- no `sources/` staging, committing, or pushing by Codex
- no final/lock/tag action

## 3. Git/source preflight

Commands run:

```text
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
git -c core.quotepath=false diff --name-only -- sources/
git -c core.quotepath=false diff --cached --name-only -- sources/
```

Branch status:

```text
## main...origin/main
```

Known untracked noise outside `sources/`:

```text
?? .vs/
?? productions/chi_yan_tian_qiong/edits/
?? reports/context_recovery/
```

Dirty `sources/` paths:

```text
 D sources/AI视频制作_Source索引与使用优先级_V1.9.md
 D sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
 D sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
 M sources/dreamina_cli_help_latest.md
?? sources/AI视频制作_Source索引与使用优先级_V1.10.md
?? sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md
?? sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md
?? sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md
```

Staged `sources/` paths: none.

## 4. Source file inventory verification

All required current Source files exist in the worktree:

- `sources/AI视频制作_Source索引与使用优先级_V1.10.md`
- `sources/dreamina_cli_help_latest.md`
- `sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
- `sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`
- `sources/AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md`
- `sources/AI视频制作_项目蓝图与产品化路线_V0.1.md`
- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`

Inventory status: pass.

## 5. Removed/old files verification

The following replaced active old files do not exist in the worktree:

- `sources/AI视频制作_Source索引与使用优先级_V1.9.md`
- `sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
- `sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `sources/README_手动应用说明.md`

The following valid rule-library files still exist and were not confused with replaced files:

- `sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`

Old files removed status: yes, in worktree. They remain uncommitted deletions.

## 6. Source Index V1.10 content check

`sources/AI视频制作_Source索引与使用优先级_V1.10.md` includes the required P0 Dreamina CLI references:

- `dreamina_cli_help_latest.md` 20260701
- `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
- `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
- `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`

Content status: pass.

## 7. dreamina_cli_help_latest content check

`sources/dreamina_cli_help_latest.md` records:

- binary version `2a20fff-dirty`
- commit `2a20fff`
- build_time `2026-06-26T06:36:39Z`
- installer metadata `v1.4.10 / 2026-06-26`
- PowerShell live path `C:/Users/msjpurf/bin/dreamina.exe`
- Linux path `/home/ke/.local/bin/dreamina`
- Linux login pending status
- `generate_num` for `text2image` and `image2image`
- `seedance2.0_vip` 4k support
- `seedance2.0mini` where shown
- Seedance 1.x model naming changes

Content status: pass.

## 8. Dreamina CLI V1.4 contract content check

`sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md` confirms:

- PowerShell CLI is the preferred live path while Linux login is pending.
- Linux CLI must not be used for live submit unless `checklogin` and `user_credit` succeed in that same Linux environment.
- K266/K268 repeated empty submit failures happened on an older CLI evidence chain.
- The CLI update materially changes command help but does not prove the old failure is fixed.
- Future submit still requires a fresh canary/preflight and explicit human authorization.

Content status: pass.

## 9. Workflow V1.2 content check

`sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md` confirms:

- current runtime `dreamina <command> -h` remains the highest command fact source
- submit, query, download, retry, resubmit, final, and lock remain separate gates
- `text2image` and `image2image` support `generate_num 1-10`
- `text2video seedance2.0_vip` supports `720p`, `1080p`, or `4k` where help shows it
- `multimodal2video` supports repeated `--image`, `--video`, and `--audio` where help shows it

Content status: pass.

## 10. Manifest schema V1.2 content check

`sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md` confirms:

- `generate_num` field exists
- `output_dir` is not a submit flag
- download remains `query_result --download_dir`
- `video_resolution 4k` is allowed where help shows it
- model allow lists include updated Seedance names, including `seedance2.0mini` where shown

Content status: pass.

## 11. V1.10.1 content check

`sources/AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md` confirms:

- image2image can over-preserve old oblique composition
- viewpoint rebuild should prefer `text2image` or weak-reference strategy when old composition is locking the image
- short, hard, result-oriented prompts are preferred for the verified viewpoint-rebuild route
- map switching is treated as visual chapter / style switching while preserving identity and world anchors
- CTRL-CAM has usage decision guidance and is treated as control reference, not project footage
- Codex prompt generation must read the Source index and relevant rules first

Content status: pass.

## 12. Source cleanliness / human-applied changes status

`sources/` clean: no.

The Source update appears manually applied in the worktree but not committed. Codex did not stage, commit, or push any `sources/` path.

Dirty Source files:

```text
 D sources/AI视频制作_Source索引与使用优先级_V1.9.md
 D sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
 D sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
 M sources/dreamina_cli_help_latest.md
?? sources/AI视频制作_Source索引与使用优先级_V1.10.md
?? sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md
?? sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md
?? sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md
```

## 13. Impact on next SHOT-04 R02a K269D

Verification supports using the human-applied Source content for future command planning, especially:

- updated Dreamina CLI command facts
- PowerShell vs Linux execution distinction
- updated `generate_num` and model allow-list rules
- preservation of submit/query/download/retry/resubmit/final/lock gates
- V1.10.1 prompt-generation rule that Codex must read Source index and relevant rules before generating prompts

However, K269D should not proceed as a clean Source-governed phase until the human-applied `sources/` changes are committed by the human or otherwise made clean in the repo.

## 14. Recommended next phase

Because content verification passed but `sources/` is dirty:

`HUMAN_SOURCE_COMMIT_REQUIRED_BEFORE_K269D`

After the human commits the Source update, rerun a short source-clean verification. If clean, the next operational phase can be:

`K269D_HUMAN_DECISION_SAFE_VARIANT_SUBMIT_AUTHORIZATION`

## 15. Explicit non-actions

Codex did not:

- run Dreamina
- run `dreamina version`
- run `dreamina user_credit`
- run Dreamina help
- submit
- query
- download
- retry
- resubmit
- create media
- edit prompt/package/manifest files
- edit `sources/`
- stage `sources/`
- commit `sources/`
- push `sources/`
- set `final_master=true`
- set `locked=true`

## 16. Final verdict

`DREAMINA_CLI_SOURCE_UPDATE_VERIFICATION_PASSED_BUT_HUMAN_SOURCE_COMMIT_REQUIRED_BEFORE_K269D`
