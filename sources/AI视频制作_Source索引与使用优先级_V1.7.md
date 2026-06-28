# AI视频制作_Source索引与使用优先级 V1.7

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Source 总索引 / 调用优先级 / Source 治理规则索引 / Prompt Compiler 索引  
> 版本：V1.7  
> 生成日期：2026-06-28  
> 生成方：ChatGPT  
> 适用范围：ChatGPT Project Source、AI_VIDEO_PIPELINE 本地 `sources/` 只读参考库、Codex / Agent / 本地自动化执行边界。  
> 重要说明：本文件应由用户手动上传 / 替换到 ChatGPT Project Source；如需同步到本地 `sources/`，也必须由用户手动处理。Codex / automation 不得直接修改、stage、commit、push official Source 文件。

---

## 0. V1.7 更新结论

V1.7 在 V1.6 基础上新增一类核心 active Source：

```text
AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md
```

新增原因：

```text
1. SHOT-04 Route A V001 证明：package review 和 clause-level Source compliance 通过，并不保证视觉结果成功。
2. K190 视觉审核确认：Route A 核心动作失败，结果读成 sustained pushing / wrestling tendency。
3. K191 确认：SHOT-04 R02 应从 audit-oriented prompt 改为 result-first prompt，核心为 wooden wall-panel slam / back-first rebound。
4. K191P 确认：当前半自动 pipeline 工程治理健康，但 prompt-priority / Prompt Compiler 层不足。
5. K192 确认：SHOT-04 R02 不应盲目直接 prompt-only 重包；应先补 wall-panel / side-wall visual target reference，再考虑 contact keyframe。
```

V1.7 的新增硬规则：

```text
Source compliance 不是 rule inclusion，而是 visible-result prioritization。
高风险动作 / 建筑互动 prompt 必须先通过 Prompt Compiler / Prompt Director 审计，再进入 L2 package。
Prompt Priority Audit、Visual Result Compliance、Negative Constraint Compression Audit、Reference Duty Attention Audit 应成为高风险动作 prompt 的 package 前置表。
```

V1.7 当前路线记录：

```yaml
SHOT04_R02_route_decision: B_FIRST_WALL_PANEL_REFERENCE_THEN_C_CONTACT_KEYFRAME
direct_prompt_only_R02: high_risk_only_if_human_explicitly_accepts
rainy_temple_scene_ref_role: world_atmosphere_only
wall_panel_target_ref_required_or_recommended: true
contact_keyframe_after_wall_panel_ref: recommended
```

---

## 1. 当前 active source 应包括

### 1.1 Source Index / 治理 / 宏流程 / Prompt Compiler

```text
AI视频制作_Source索引与使用优先级_V1.7.md
AI视频制作_自动化治理与Source权限规则_V0.1.md
AI视频制作_自动化宏流程与授权等级_V0.1.md
AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md
```

### 1.2 实测规则库

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
AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
```

可选 / 若项目中已存在：

```text
AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md
```

### 1.3 Seedance / Dreamina / Batcher 执行层 Source

```text
Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
dreamina_cli_help.md
dreamina_cli_help_latest.md
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
```

如果本地 `sources/` 中暂时缺少某个文件，以 ChatGPT Project Source 或用户手动提供的最新文件为准。  
如果执行层命令事实冲突，以当前运行时 `dreamina <command> -h` 为最高事实来源。

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

### 2.2 自动化宏流程优先级

凡涉及 Codex / Agent / Dreamina / local automation 的阶段，必须先看：

```text
AI视频制作_自动化治理与Source权限规则_V0.1.md
AI视频制作_自动化宏流程与授权等级_V0.1.md
```

核心边界：

```yaml
source_write_allowed: false
source_stage_allowed: false
source_commit_allowed: false
source_push_allowed: false
submit_requires_explicit_human_authorization: true
query_download_requires_separate_human_authorization: true
retry_resubmit_requires_explicit_human_authorization: true
final_master_requires_explicit_human_lock: true
locked_requires_explicit_human_lock: true
```

### 2.3 执行层优先级

Dreamina CLI 的真实执行能力，以当前本地命令输出为最高事实源：

```text
当前运行时 dreamina <command> -h
> dreamina_cli_help_latest.md
> dreamina_cli_help.md
> Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
> Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
> Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
> DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
> 其他通用工作流 Source
```

执行层不得只根据网页端能力或旧经验推断 CLI 能力。  
任何 live work 前必须执行 corrected preflight：

```text
dreamina version
dreamina user_credit
dreamina <target_command> -h
```

### 2.4 高风险动作 / 建筑互动 prompt 优先级

对战斗 / 动作 / 武打 / 建筑互动 / 撞墙 / 撞栏杆 / 地形借力 prompt，建议调用顺序为：

```text
Source Index / task router
> 自动化治理与Source权限规则_V0.1
> 自动化宏流程与授权等级_V0.1
> Prompt编译器与结果优先动作语法_V0.1
> V1.11 连续战斗动作密度与环境破坏因果规则
> V1.2 动作 / 打击感 / hit-stop / fight physics
> V1.9 空间调度 / 角色站位 / 脚下落点
> V1.10 / V1.10.1 场景锚点 / 视角纠偏 / CTRL-CAM
> V1.8 多模态参考职责 / IP 安全
> Seedance V0.3 三层描述 / Composition Matrix
> V1.5 / V1.6 剧本分镜与词库规则
> V1.3 / V1.4 外部案例与知识库吸收规则
> 外部未验证教程
```

关键变化：

```text
Prompt Compiler V0.1 应位于 V1.11 之前。
原因：V1.11 负责 contact-beat / damage causality / no idle tail；
Prompt Compiler 负责先判断“哪个视觉结果必须占据 prompt 最高优先级”。
```

### 2.5 剧本 / 美术 / 分镜 / 传统故事类优先级

对非 combat 的剧本、美术、分镜、传统故事、广告、产品、角色资产等任务，建议调用：

```text
Source Index / task router
> 自动化治理与Source权限规则_V0.1（若涉及 automation）
> V1.5 剧本美术与分镜设计
> V1.6 分镜模板与风格词库
> V1.7 中国传统故事与神话改编
> V1.4 外部知识库与商业视觉模板
> V1.3 外部案例观察与关键帧规则
> Seedance V0.3 三层描述 / Composition Matrix
> V1.1 基础实测规则
> 外部未验证教程
```

---

## 3. Prompt Compiler / Result-first Action Grammar 调用规则

### 3.1 什么时候必须调用 Prompt Compiler

以下情况必须调用 `AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md`：

```text
近身格斗
建筑 / 地形互动
撞墙 / 撞栏杆 / 撞门框
木格 / 木墙板 / 侧廊墙接触
短爆发身体冲撞
武器或身体导致环境局部反馈
双人动作 blocking
需要身份、动作、场景、接触因果同时成立的复杂 prompt
```

尤其是以下失败后：

```text
动作读成推搡 / pushing
动作读成 wrestling hold
建筑反馈没有因果
主动作出现太晚
reference duties 抢走 prompt 前段注意力
negative constraints 太长
package review 通过但 visual result 失败
```

### 3.2 Pre-L2 高风险动作 prompt 必须具备

进入 L2 no-submit package 前，必须具备：

```text
1. Result-first prompt blueprint
2. Prompt Priority Audit
3. Visual Result Compliance
4. Clause-level Source Compliance
5. Negative Constraint Compression Audit
6. Reference Duty Attention Audit
7. Prompt risk register
8. prompt-only high-risk label（如果缺少视觉目标参考）
9. ChatGPT prompt-director review
10. human package creation authorization
```

### 3.3 Prompt Priority Audit 硬规则

```text
P0 主结果句必须出现在 prompt 前 1–2 句或前 50–80 words。
P0 任一关键项为 0，不应进入 L2 package。
如果 dominant visual result 出现在长 reference / scene / camera block 之后，必须标记 rewrite_needed=true。
```

P0 至少包括：

```text
dominant visual result sentence
physical hit path
environmental consequence
rebound / continuation
```

### 3.4 Visual Result Compliance 与 Source Compliance 分离

必须区分：

```text
clause-level Source compliance
visual result compliance
```

Source compliance 检查：

```text
Source 规则有没有被 prompt clause 落实。
```

Visual Result Compliance 检查：

```text
生成后观众是否真的能看到目标结果。
```

对 SHOT-04 R02，visual result 必须能验收：

```text
Shuangji back-first hits wooden wall panel
wall panel local flex / shallow dent appears after contact only
rainwater / tiny splinters burst outward in force direction
Shuangji rebounds and counters
final frame cuts mid-exchange
```

### 3.5 Prompt-only high-risk label

当目标物 / 接触姿态缺视觉参考时，必须标记：

```yaml
prompt_only_high_risk: true
missing_visual_target_ref: true
requires_human_acceptance_of_risk: true
```

适用例子：

```text
只靠文字写 wooden wall-panel slam；
现有 scene ref 不清楚显示 wall-panel target；
需要精确 body-wall contact；
需要双人身份 + blocking + 建筑反馈同时成立。
```

---

## 4. 当前项目路线记录

### 4.1 SHOT-03 路线继承记录

当前 SHOT-03 已停止普通 prompt-only 继续硬冲地形力链。

继承 V1.6 路线原则：

```text
Primary route:
Split terrain assist into multiple shorter edited shots, using clean corridor combat baseline as foundation.

Fallback route:
Preserve clean corridor combat baseline and move heavier architectural interaction / building impact escalation to SHOT-04.
```

同时：

```text
ordinary image2image is not reliably solving:
dual-character identity
precise close-contact blocking
corridor/column composition
all at once
```

### 4.2 SHOT-04 Route A / R02 记录

K190 / K191 / K191P / K192 后，当前 SHOT-04 状态为：

```yaml
Route_A_V001_visual_status: failed_core_action
identity_status: partially_passed
architecture_interaction_status: failed
damage_causality_status: weak_or_failed
action_status: failed_static_push_wrestling_tendency
usable_as_SHOT04_primary: false
final_master: false
locked: false
```

R02 新方向：

```text
wooden wall-panel slam / back-first rebound
```

R02 result-first core sentence：

```text
Fenshou lands one explosive shoulder-check into Shuangji's crossed guard and slams her back-first into a wooden wall panel.
```

K192 route decision：

```text
route_decision = B_FIRST_WALL_PANEL_REFERENCE_THEN_C_CONTACT_KEYFRAME
```

### 4.3 SHOT-04 R02 禁止直接盲目 prompt-only 重包

不得默认执行：

```text
直接用现有三 refs + result-first prompt 做 R02 package
```

除非：

```text
human_explicitly_accepts_high_risk_prompt_only_test=true
```

原因：

```text
当前 RAINY_TEMPLE_SCENE_REF 对雨中古寺、湿石板、氛围很强；
但 wall_panel_target_support=weak；
单靠文字写 wooden wall panel 仍可能再次生成 soft pushing / generic corridor pressure。
```

### 4.4 SHOT-04 推荐下一步

默认 K193：

```text
SHOT-04 wall-panel / side-wall architecture reference planning or no-submit package planning
```

K193 边界建议：

```text
L0/L2 only
no Dreamina unless separately authorized
no submit/query/download
no final/lock
keep character identity separate from wall-panel reference
search/choose/plan wall-panel / side-wall / wooden lattice wall target reference
```

若 K193 找到强 wall-panel ref：

```text
K194 可准备 R02 video package，必须使用 Prompt Compiler Pre-L2 checklist。
```

若 K193 找不到强 wall-panel ref：

```text
K194 应考虑 architecture-ref generation 或 contact keyframe plan，再进入 video package。
```

---

## 5. Clause-level Source Compliance 规则保留

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

## 6. Prompt Compiler 审计表优先于 package ready 声明

对高风险动作 / 建筑互动任务，Codex 不得只凭以下内容声明 package ready：

```text
prompt txt exists
package JSON parses
manifest CSV exists
refs sha256 valid
source files inspected
submit_allowed=false
```

还必须证明：

```text
dominant visual result 已前置
P0 result_strength_score 合格
negative constraints 未压过 positive action
reference duties 未抢占动作主句
visual result compliance 可验收
prompt-only risk 已标记
```

否则只能标记：

```text
package_structurally_ready_but_prompt_priority_not_audited
```

不能标记：

```text
ready_for_submit_decision
```

---

## 7. Reports 是证据，不是 Source

K-phase reports 可以记录：

```text
人审结论
ChatGPT 视觉复核
Codex package review
Dreamina submit/query/download
失败原因
source update recommendation
Prompt Priority Audit
Visual Result Compliance
route decision
```

但 reports 不能直接替代 Source。

报告进入 Source 的条件：

```text
1. 形成稳定规则或重要治理规则。
2. ChatGPT 生成或审阅 official Source 表述。
3. 用户手动应用。
```

---

## 8. Codex / 自动化 sources/ 只读规则

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

---

## 9. Official Source 更新工作流

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

## 10. 给 Codex Prompt 的固定边界块

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

## 11. 给高风险动作 package 的固定 Prompt Compiler 边界块

后续高风险动作 / 建筑互动 L2 package prompt 应固定加入：

```text
Prompt Compiler hard rule:
This package cannot be marked ready for submit decision unless the prompt has passed:
1. Result-first prompt blueprint
2. Prompt Priority Audit
3. Visual Result Compliance
4. Clause-level Source Compliance
5. Negative Constraint Compression Audit
6. Reference Duty Attention Audit
7. prompt-only high-risk label if visual target ref is missing

The dominant visual result must appear before long reference-duty, scene, camera, or negative-constraint blocks.
Clause-level Source compliance is necessary but not sufficient.
```

---

## 12. 何时使用 Pro / 高推理模式

建议使用 Pro / 高推理模式的场景：

```text
Source 正式生成 / 更新
Source Index 更新
Prompt Compiler 规则生成 / 修改
macro-run 指令生成
跨多个 K-phase 的路线裁决
多源规则合并
复杂镜头 prompt 设计
复杂失败复盘
视觉审核后的策略判断
```

普通 Thinking / medium 可用于：

```text
单一 K-phase report
本地 artifact 生成
简单 package review
metadata validation
执行结果确认
```

---

## 13. 未来可能的 Source 拆分

当前 Prompt Compiler V0.1 可以作为单一 Source 使用。  
如果后续规则膨胀，可拆为：

```text
AI视频制作_视觉结果合规表与Prompt优先级审计_V0.1.md
AI视频制作_引用职责注意力与负面约束压缩规则_V0.1.md
AI视频制作_Prompt Outcome Dataset与失败归因字段_V0.1.md
```

---

## 14. Final Verdict

```text
SOURCE_INDEX_V1_7_READY_WITH_PROMPT_COMPILER_PRIORITY
```
