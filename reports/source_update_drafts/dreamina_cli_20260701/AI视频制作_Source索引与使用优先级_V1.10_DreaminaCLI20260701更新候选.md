# AI视频制作_Source索引与使用优先级_V1.10_DreaminaCLI20260701更新候选

> 类型：Project Source index replacement candidate
> Intended action: replace V1.9 only after human review and manual application
> Status: not official Source until human-applied

## 1. Purpose

This candidate preserves the V1.9 P0/P1/P2/P3 structure while adding the Dreamina CLI 2026-07-01 update candidates to the recommended Source reading order.

Codex must not modify official `sources/`.

## 2. Recommended Source Priority

### P0: Hard Governance And Execution Boundary

Read first:

1. `AI视频制作_自动化治理与Source权限规则_V0.1.md`
2. `AI视频制作_自动化宏流程与授权等级_V0.2.md`
3. `dreamina_cli_help_latest.md` updated to 20260701
4. `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
5. `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
6. `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
7. `Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
8. `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`

P0 controls:

- Source authority
- Codex and automation boundary
- Dreamina canary / command-contract preflight
- submit/query/download/retry/resubmit/final/lock authorization
- live execution environment selection

### P0.5: Project Blueprint

Keep:

- `AI视频制作_项目蓝图与产品化路线_V0.1.md`

### P1: Prompt And Action Rules

Keep V1.9 structure. For SHOT-04 R02 / close dual-character combat, continue reading:

- `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- relevant action/reference/video review Sources

### P2: Multimodal, Reference, And Manifest Rules

Update DreaminaBatcher manifest source to:

- `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`

Keep multimodal and IP/reference safety Sources as needed.

### P3: Script, Art, Style, And Traditional Story Extensions

Keep V1.9 structure.

## 3. New Dreamina CLI Reading Rule

For any Dreamina task after the 2026-07-01 update:

1. Read this Source Index candidate if human-applied.
2. Read P0 hard governance.
3. Read the updated `dreamina_cli_help_latest.md`.
4. Read the updated Dreamina CLI execution contract supplement.
5. Read the workflow/schema files that match the task type.
6. Still run live canary/preflight during any future authorized live phase.

## 4. Conflict Rules

If Source Index conflicts with P0 governance, P0 governance wins.

If any Source file conflicts with current runtime `dreamina <command> -h`, runtime help wins for command facts.

If a task-specific human authorization is narrower than Source rules, the narrower human authorization wins.

## 5. Source Update Governance

Codex may:

- read Source files
- generate reports
- generate Source update candidates under `reports/`
- recommend manual Source application

Codex must not:

- create files under `sources/`
- edit files under `sources/`
- delete files under `sources/`
- rename or move files under `sources/`
- stage, commit, or push files under `sources/`
- upload or replace ChatGPT Project Source
- declare a Source candidate active without human action

## 6. Current Dreamina CLI State To Record

PowerShell live path:

```text
C:/Users/msjpurf/bin/dreamina.exe
```

Linux installed path:

```text
/home/ke/.local/bin/dreamina
```

Rule:

Use PowerShell CLI for live execution while Linux CLI login is pending. Linux CLI may be used for live execution only after `checklogin` and `user_credit` succeed in that environment.

## 7. Current SHOT-04 R02a Note

K266/K268 repeated empty submit failures happened on an older CLI evidence chain. The refreshed CLI materially changes command help and may affect future submit behavior, but no fix is proven until a future authorized submit succeeds.

K269D/K269 should remain human-authorized and one-submit-only if live execution is later chosen.
