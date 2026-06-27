# AI视频制作_Source索引与使用优先级 V1.6

> 项目：AI视频制作  
> 类型：Project Source 总索引 / 调用优先级 / Source 治理规则索引  
> 版本：V1.6  
> 生成日期：2026-06-27  
> 生成方：ChatGPT  
> 适用范围：ChatGPT Project Source、AI_VIDEO_PIPELINE 本地 `sources/` 只读参考库、Codex / 自动化执行边界。  
> 重要说明：本文件应由用户手动上传 / 替换到 ChatGPT Project Source；如需同步到本地 `sources/`，也必须由用户手动处理。Codex / 自动化不得直接修改、stage、commit、push official Source 文件。

---

## 0. V1.6 更新结论

V1.6 在 V1.5 基础上新增一类**自动化治理 / Source 权限规则**：

```text
AI视频制作_自动化治理与Source权限规则_V0.1.md
```

新增原因：

```text
1. SHOT-03 V005 / V006 证明：Codex 读取 Source 不等于已经把 Source 规则转译成有效 prompt 约束。
2. K130 审计提出：后续自动化必须做 clause-level source compliance，而不是只记录 source files inspected。
3. 用户明确要求：official Source 只能由用户手动更新，最好由 ChatGPT 生成正式 Source 内容。
4. K140 已确认 SHOT-03 路线：停止 prompt-only V007；主路线改为 split terrain assist into multiple shorter edited shots；fallback 为保留 V004 clean corridor baseline，并把建筑互动升级移到 SHOT-04。
```

V1.6 的新增硬规则：

```text
Official Source authority = human user only.
Official Source generation/review path = ChatGPT.
Official Source application/upload/sync = human manual action.
Codex / automation = read-only source consumer + report/draft generator only.
Codex / automation must never create/edit/delete/rename/move/stage/commit/push files under sources/.
```

---

## 1. 当前 active source 应包括

```text
AI视频制作_Source索引与使用优先级_V1.6.md
AI视频制作_自动化治理与Source权限规则_V0.1.md

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
AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md

Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
dreamina_cli_help.md
dreamina_cli_help_latest.md
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
```

如果本地 `sources/` 中暂时缺少其中某个文件，以 ChatGPT Project Source 或用户手动提供的最新文件为准；如果执行层命令事实冲突，以当前本地 `dreamina <command> -h` 为准。

---

## 2. 总优先级规则

### 2.1 Source 权限与治理优先级

对 official Source 的创建、修改、替换、上传、同步，优先级为：

```text
Human manual action
> ChatGPT-generated / ChatGPT-reviewed official Source content
> Codex report / automation draft / local evidence
```

硬规则：

```text
Codex / automation 对 official Source 没有写权限。
Codex / automation 即使读到 source update recommendation，也只能写进 reports/ 或 reports/source_update_drafts/。
Codex / automation 不得直接改 sources/。
```

### 2.2 执行层优先级

Dreamina CLI 的真实执行能力，以当前本地命令输出为最高事实源：

```text
当前本地 dreamina <command> -h
> dreamina_cli_help_latest.md
> dreamina_cli_help.md
> Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
> Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
> Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
> DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
> 其他通用工作流 Source
```

### 2.3 内容创作与 prompt 规则优先级

对战斗 / 动作 / 武打 / 环境交互 prompt，建议调用：

```text
Source Index / task router
> 自动化治理与Source权限规则_V0.1（仅治理和自动化边界）
> V1.11 连续战斗动作密度与环境破坏因果规则
> V1.2 动作 / 打击感 / hit-stop / fight physics
> V1.9 空间调度 / 角色站位 / 脚落地
> V1.10 / V1.10.1 场景锚点 / 视角 / CTRL-CAM / 短硬 prompt
> V1.8 多模态参考职责 / IP 安全
> Seedance V0.3 三层描述 / Composition Matrix
> 旧项目规则和一般美术分镜规则
> 外部未验证教程
```

---

## 3. Codex / 自动化 sources/ 只读规则

本地目录：

```text
G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/
```

在任何 Codex / 自动化任务中，该目录都是 official Source 的只读参考库。

Codex / automation 可以：

```text
读取 sources/ 理解项目规则。
用 sources/ 校验 prompt / package / workflow。
在 report 中记录 source update recommendation。
在 reports/source_update_drafts/ 中生成 draft 或 evidence summary。
```

Codex / automation 不可以：

```text
新增 sources/ 文件。
修改 sources/ 文件。
删除 sources/ 文件。
重命名 sources/ 文件。
移动 sources/ 文件。
stage sources/ 文件。
commit sources/ 文件。
push sources/ 文件。
把 draft 当作 official Source。
```

即使用户要求生成 Source 更新，Codex / automation 也只能生成 draft / recommendation，不能直接应用到 `sources/`。

---

## 4. Official Source 更新工作流

正式 Source 更新必须走以下路径：

```text
1. K-phase reports / human review / ChatGPT review 形成 evidence。
2. ChatGPT 根据 evidence 生成 official Source markdown 内容或可下载文件。
3. 用户人工检查。
4. 用户手动上传到 ChatGPT Project Source。
5. 如需本地同步，用户手动复制 / 替换到 local sources/。
6. Codex 后续只读取，不改写。
```

禁止路径：

```text
Codex 根据 report 直接写 sources/。
Codex 自动生成 official Source 并 commit。
自动化检测到规则变化后自动替换 Source。
把 reports/ 中的 draft 直接视为 official Source。
```

---

## 5. Clause-level Source Compliance 规则

K130 / V005 / V006 复盘提出：

```text
source_read != source_compliance
```

以后 combat/action prompt 自动化不能只记录：

```text
files inspected: V1.2, V1.11, Source Index
```

必须生成 clause-level compliance table：

| 字段 | 说明 |
|---|---|
| source_rule | 来源规则 |
| required_behavior | 这条规则要求模型做什么 |
| prompt_clause | prompt 中哪一句落实了它 |
| timing_location | 它出现在全局、某个时间段，还是结尾限制 |
| status | present / weak / missing |
| failure_risk_if_omitted | 缺失后可能失败在哪里 |

如果 Source 规则没有对应 prompt clause，则应视为：

```text
source_rule_not_operationalized
```

这类问题不能因为“Source 已读取”而放行。

---

## 6. SHOT-03 K140 路线决策记录

K140 已确认：

```text
Primary route:
B. Split terrain assist into multiple shorter edited shots, using V004-style clean corridor combat as the baseline.

Fallback route:
A + D. Preserve V004 as the SHOT-03 clean corridor baseline/fallback, and move heavier architectural interaction / building impact escalation to SHOT-04.
```

同时确认：

```text
Stop pure prompt-only V007 for now.
Do not keep trying to solve precise column-base force-chain choreography in one 5-second pure-text multimodal2video shot.
V004 remains valuable as clean corridor baseline/fallback.
V005 and V006 remain learning cases.
Future terrain-assisted combat should use split-shot design, action/pose references, or narrower micro-goals.
Architectural interaction should be planned as a later SHOT-04 family, not forced into SHOT-03 V007 immediately.
```

---

## 7. V1.12 候选，不在本 V1.6 中正式固化

K139 / K140 形成了 V1.12 候选主题：

```text
AI视频制作_实测规则库_V1.12_地形借力拆镜与Prompt-only限制增补稿.md
```

候选内容包括：

```text
1. Clause-level prompt compliance 不保证最终 choreography quality。
2. 单条 5 秒纯文字 prompt 不适合同时硬控：稳定身份、稳定场景、精确地形触发、完整发力链、密集 contact beats、重身体后果。
3. 柱基 / 柱脚 / 地形借力容易被模型误生为随机踏点、石头、pose-like action。
4. 复杂 terrain-assisted combat 应优先拆镜头、使用动作参考视频、pose/keyframe 支持，或降低为 narrower micro-goal。
```

是否生成正式 V1.12，应由 ChatGPT 在后续根据 K141 / human decision 生成，用户手动上传。

---

## 8. 未来自动化 Pipeline 必须内置的硬边界

```yaml
source_read_allowed: true
source_recommendation_allowed: true
source_draft_allowed: true
source_write_allowed: false
source_stage_allowed: false
source_commit_allowed: false
official_source_update_requires_chatgpt_generation_or_review: true
official_source_update_requires_human_manual_action: true

submit_requires_explicit_human_authorization: true
query_download_requires_separate_human_authorization: true
final_master_requires_explicit_human_lock: true
locked_requires_explicit_human_lock: true
```

---

## 9. Final Verdict

```text
SOURCE_INDEX_V1_6_READY_WITH_AUTOMATION_GOVERNANCE_AND_SHOT03_ROUTE_DECISION
```
