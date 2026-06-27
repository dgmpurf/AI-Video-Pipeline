# AI视频制作_自动化治理与Source权限规则 V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：自动化治理规则 / Source 权限规则 / 人机协作边界  
> 版本：V0.1  
> 生成日期：2026-06-27  
> 生成方：ChatGPT  
> 适用范围：Codex、Agent、本地自动化脚本、Dreamina CLI 工作流、ChatGPT Project Source 更新流程。  
> 重要说明：本文件为 official Source 候选，应由用户手动上传 / 应用。Codex / 自动化不得直接写入或修改 `sources/`。

---

## 0. 一句话结论

```text
Source 是项目规则，不是自动化输出物。
Official Source 只能由用户手动更新；正式内容最好由 ChatGPT 生成或审阅。
Codex / automation 可以读 Source、审计 Source、建议 Source update，但不能直接修改 Source。
```

---

## 1. 背景与生成依据

本规则来自 AI_VIDEO_PIPELINE 在《赤焰对天穹》SHOT-03 的真实协作复盘：

```text
V004：clean corridor combat 可用，但缺少 terrain-affordance。
V005：terrain idea visible，但 soft force / low burst rhythm。
V006：clause-level source-compliant prompt 仍失败，terrain anchor / force-chain choreography 不可靠。
K130：提出 source_read != source_compliance。
K139：比较 V004 / V005 / V006 后建议停止 prompt-only V007。
K140：人类确认主路线 B，fallback A+D。
```

这些复盘说明：

```text
1. Source 需要持续进化。
2. 自动化必须读取 Source，但不能直接管理 official Source。
3. 自动化不能只证明“读过 Source”，还必须证明“Source 规则已被具体落实”。
4. 最终路线、锁定、Source 更新，必须由人类控制。
```

---

## 2. Source 权限定义

### 2.1 Official Source

Official Source 指：

```text
ChatGPT Project Source 中上传的规则文件。
本地 AI_VIDEO_PIPELINE/sources/ 中作为 official reference mirror 的规则文件。
```

这些文件具有项目规则效力。

### 2.2 Draft / Recommendation / Evidence

以下不属于 official Source：

```text
K-phase reports
review reports
source update recommendation
reports/source_update_drafts/ 中的草稿
Codex 生成的候选规则
ChatGPT 对话中的未确认草案
```

它们只是 evidence / proposal，必须经过 ChatGPT 正式生成 / 审阅与用户手动应用，才可成为 official Source。

---

## 3. Human-only Official Source Rule

硬规则：

```text
Official Source authority = human user only.
```

用户可以：

```text
手动上传 Source 到 ChatGPT Project Source。
手动替换 ChatGPT Project Source。
手动复制 / 同步 Source 到本地 sources/。
手动删除旧 Source。
手动决定哪个 Source 是 active。
```

ChatGPT 可以：

```text
生成 official Source markdown 内容。
审阅 Source 草稿。
整合 K-phase reports 为 Source update。
输出可下载的 .md 文件。
提醒用户手动上传 / 替换。
```

Codex / automation 不可以：

```text
直接修改 official Source。
直接写入 sources/。
把 source draft 当 active Source。
自动提交 Source update。
```

---

## 4. Codex / Automation 允许与禁止事项

### 4.1 允许

Codex / automation 可以：

```text
读取 sources/。
读取 reports/。
读取 shot records。
读取 prompts / manifests。
读取 review artifacts 的 metadata。
根据 Source 做 prompt / package 审计。
生成 reports。
生成 source update recommendation。
在 reports/source_update_drafts/ 下生成 draft。
提醒 ChatGPT / human 需要 Source update。
```

### 4.2 禁止

Codex / automation 不得：

```text
create sources/*
edit sources/*
delete sources/*
rename sources/*
move sources/*
stage sources/*
commit sources/*
push sources/*
```

也不得：

```text
自动上传 ChatGPT Project Source。
自动把 draft 标记为 active Source。
自动替换 Source Index。
自动将 report 复制进 sources/。
```

---

## 5. Official Source 更新流程

标准流程：

```text
K-phase evidence / human review / ChatGPT visual review
→ ChatGPT 生成 official Source update markdown
→ 用户人工审阅
→ 用户手动上传到 ChatGPT Project Source
→ 用户手动决定是否同步到本地 sources/
→ 后续 Codex 只读使用
```

Source update 文件建议命名：

```text
AI视频制作_Source索引与使用优先级_Vx.x.md
AI视频制作_实测规则库_Vx.x_主题.md
AI视频制作_自动化治理与Source权限规则_Vx.x.md
```

---

## 6. Reports 是证据，不是 Source

K-phase reports 可以记录：

```text
人审结论
ChatGPT 视觉复核
Codex package review
Dreamina submit/query/download
失败原因
source update recommendation
```

但 reports 不能直接替代 Source。

报告进入 Source 的条件：

```text
1. 形成稳定规则或重要治理规则。
2. ChatGPT 生成或审阅 official Source 表述。
3. 用户手动应用。
```

---

## 7. Clause-level Source Compliance

后续 prompt 自动化必须区分：

```text
Source read
Source understood
Source operationalized
```

只记录 `files inspected` 不够。

每个关键 Source 规则必须被映射为具体 prompt clause：

| 字段 | 说明 |
|---|---|
| source_rule | 哪条 Source 规则 |
| prompt_clause | prompt 中哪句落实 |
| timing_location | 全局 / 时间段 / 结尾 / negative constraint |
| status | present / weak / missing |
| risk_if_missing | 缺失会导致什么失败 |

如果无法找到 prompt clause，应标记：

```text
source_rule_not_operationalized
```

这类情况下不得因为 Source 文件已经读取而放行。

---

## 8. Human Gate 规则

以下动作必须有用户明确授权：

```text
Dreamina submit
Dreamina query_result
Dreamina download
retry
resubmit
batch run
final_master=true
locked=true
official Source upload / replacement
```

提交与下载必须分开授权：

```text
K135 submit 授权 ≠ K136 query/download 授权。
K136 query/download 授权 ≠ final/lock 授权。
```

锁定必须显式人审：

```text
Codex / automation may generate candidates.
Codex / automation may generate reports.
Codex / automation may recommend.
Codex / automation must not lock.
```

---

## 9. AI_VIDEO_PIPELINE 自动化建议架构

未来全自动化应分为：

```text
1. Source Loader
2. Report / Evidence Loader
3. Shot State Loader
4. Prompt Compiler
5. Clause-level Source Compliance Auditor
6. Package Builder
7. Human Authorization Gate
8. Dreamina Execution Layer
9. Review Artifact Builder
10. Human Review Recorder
11. Source Update Recommender
```

其中：

```text
Source Loader = read-only
Source Update Recommender = report/draft only
Official Source Writer = 不存在于 Codex/automation 中
Official Source Application = human only
```

---

## 10. SHOT-03 Case Study：为什么需要本治理规则

SHOT-03 V005/V006 证明：

```text
1. Codex 可以读取 Source。
2. Codex 可以生成看似合规的 prompt。
3. 但如果没有 clause-level auditor，Source 规则可能只是被“概念性吸收”，没有成为强约束。
4. 即使 clause-level prompt 合规，模型生成结果仍可能失败。
5. 因此：Source compliance 是必要条件，不是成功保证。
```

K140 route decision 进一步确认：

```text
Stop pure prompt-only V007 for now.
Primary route = split terrain assist into multiple shorter edited shots.
Fallback = preserve V004 clean corridor baseline and move heavier architectural interaction to SHOT-04.
```

该结论应作为后续 Source 更新 evidence，但不是由 Codex 自动写入 Source。

---

## 11. Automation Invariants

```yaml
source_read_allowed: true
source_recommendation_allowed: true
source_draft_allowed: true
source_write_allowed: false
source_stage_allowed: false
source_commit_allowed: false
source_push_allowed: false

official_source_update_requires_chatgpt_generation_or_review: true
official_source_update_requires_human_manual_action: true

submit_requires_explicit_human_authorization: true
query_download_requires_separate_human_authorization: true
retry_resubmit_requires_explicit_human_authorization: true
final_master_requires_explicit_human_lock: true
locked_requires_explicit_human_lock: true

reports_are_evidence_not_source: true
source_drafts_are_not_official_until_human_applied: true
```

---

## 12. 给 Codex Prompt 的固定边界块

后续 Codex prompt 应固定加入：

```text
Source governance hard rule:
Official Project Source files are controlled only by the human user.
Codex and automation may read sources/ as read-only reference material.
Codex and automation may create source update recommendations inside reports/ only.
Codex and automation must not create, edit, delete, rename, move, stage, commit, or push files under sources/.
Official Source updates must be generated/reviewed by ChatGPT and manually applied/uploaded by the human user.

For this task:
source_read_allowed=true
source_recommendation_allowed=true
source_write_allowed=false
source_stage_allowed=false
official_source_update_requires_human_manual_action=true
```

---

## 13. Final Verdict

```text
AUTOMATION_GOVERNANCE_AND_SOURCE_PERMISSION_RULES_V0_1_READY
```
