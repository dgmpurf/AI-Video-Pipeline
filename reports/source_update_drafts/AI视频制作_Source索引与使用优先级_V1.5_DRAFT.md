# AI视频制作_Source索引与使用优先级 V1.5_DRAFT

> 状态：DRAFT，仅供人工审阅。  
> 重要说明：本文件不是正式 `sources/` 修改，也不是 live Project Source。  
> 输出位置：`reports/source_update_drafts/`。  
> 生成依据：本地 Source V1.1-V1.3 索引、V1.2 / V1.8 / V1.9 / V1.10 / V1.10.1、Seedance V0.3、SHOT-02 / SHOT-03 真实复盘。  
> 使用建议：人工确认后，可由用户手动复制到正式 Source 或上传到 ChatGPT Project Source。

---

## 0. Draft Update Note

This is a draft index update only.

- `sources/` was read read-only.
- No file under `sources/` was created, edited, renamed, moved, deleted, or staged.
- This draft should be manually reviewed before becoming official Source.
- For Codex tasks, local `sources/` is read-only reference material unless the human separately authorizes source modification.
- Generated source-update drafts belong under `reports/source_update_drafts/`.

---

## 1. Existing Source Hierarchy Observed

The latest local official source index found was:

```text
sources/AI视频制作_Source索引与使用优先级_V1.3.md
```

V1.3 active source hierarchy includes:

```text
AI视频制作_实测规则库_V1.1.md
AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md
AI视频制作_实测规则库_V1.3_外部案例观察与关键帧规则增补稿.md
AI视频制作_实测规则库_V1.4_外部知识库与商业视觉模板增补稿.md
AI视频制作_实测规则库_V1.5_剧本美术与分镜设计增补稿.md
AI视频制作_实测规则库_V1.6_分镜模板与风格词库增补稿.md
AI视频制作_实测规则库_V1.7_中国传统故事与神话改编增补稿.md
AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md
AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md
AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md
AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md
Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
dreamina_cli_help.md
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
```

V1.3 also states that current local `dreamina <command> -h` remains the highest execution-layer fact source.

---

## 2. Proposed New Active Draft Source

Add this draft as the latest project-tested combat prompt rule supplement:

```text
AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
```

Draft path:

```text
reports/source_update_drafts/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿_DRAFT.md
```

Purpose:

- Continuous combat action density.
- Contact-beat scheduling.
- Actor-specific attack-defense causality.
- Environmental damage causality.
- Idle-tail prevention.
- Speed-up applicability boundary.
- ChatGPT prompt content audit gate before combat submit.

---

## 3. Content-Creation Priority Recommendation

For content and prompt writing:

```text
Source Index / task router
> V1.11 continuous combat action-density supplement for combat/action prompts
> V1.2 action / impact / hit-stop / fight physics rules
> V1.9 spatial blocking / character placement / foot landing rules
> V1.10 / V1.10.1 scene anchor / viewpoint / CTRL-CAM rules
> V1.8 multimodal reference-duty rules
> Seedance V0.3 workflow and Composition Matrix
> older project source supplements
> external tutorials / untested cases
```

V1.11 should be used after general Source index, Dreamina CLI help, and Seedance constraints are understood, and before writing new combat/action prompts.

---

## 4. Execution-Layer Priority Remains Separate

For Dreamina CLI execution, do not let V1.11 override command facts.

Execution-layer priority remains:

```text
current local dreamina <command> -h
> dreamina_cli_help.md
> Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
> Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
> DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
> other general workflow Source
```

V1.11 is a prompt/content rule supplement, not a CLI contract.

---

## 5. When To Read V1.11

Read V1.11 before:

- SHOT-03 V004 or later combat package writing.
- Any fast hand-to-hand combat prompt.
- Any prompt involving architecture / props breaking during combat.
- Any prompt where the ending risks becoming a pose / readable endpoint.
- Any prompt relying on speed-up to solve rhythm.
- Any prompt with footwork / legwork emphasis.

Do not rely on V1.11 alone for:

- non-combat scene anchors
- pure image2image character assets
- Dreamina command syntax
- IP safety
- reference-pack duties
- final edit lock policy

---

## 6. Operational Note For Codex

For Codex tasks:

- Local `sources/` is read-only reference material unless human explicitly authorizes source modification.
- Drafts should be written under `reports/source_update_drafts/`.
- Do not stage files under `sources/` unless the user explicitly asks to modify official source.
- Do not treat a draft as live Project Source.
- Do not modify ChatGPT Project Source directly from Codex unless separately authorized by the human.

---

## 7. Proposed Source Index V1.5 Change Summary

If promoted from draft, V1.5 should:

- Add V1.11 as latest B-level project-tested combat prompt supplement.
- Mark SHOT-03 V003 failure as the trigger evidence.
- Note that SHOT-02 V018 speed diagnostics define when speed-up is valid.
- Require action prompts to pass ChatGPT content audit in addition to Codex package review.
- Preserve V1.3 execution-layer priority for Dreamina CLI.
- Preserve existing V1.9/V1.10/V1.10.1 spatial and scene-anchor rules.

---

## 8. Human Review Requirement

This draft should be manually reviewed before:

- copying into `sources/`
- uploading to ChatGPT Project Source
- using it as an official rule gate

Recommended next after approval:

```text
Prepare SHOT-03 V004 package under V1.11 contact-beat audit rule.
```

---

## 9. One-Line Summary

```text
V1.5 should add V1.11 as the combat-action-density supplement while keeping CLI help as the execution truth and keeping reports/source_update_drafts as the Codex-safe staging area for draft Source updates.
```
