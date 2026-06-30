# AI视频制作_Source索引与使用优先级_V1.9

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Source 总索引 / 调用优先级 / 当前状态入口  
> 版本：V1.9 Draft  
> 生成日期：2026-06-30  
> 生成方：ChatGPT Pro Extended  
> 来源：V1.8 Source Index + PHASE_PROJECT_TOTAL_STATE_CONTEXT_RECOVERY_REPORT + K261/K262 SHOT-04 R02 route reset evidence + 项目蓝图综合  
> 应用方式：建议由用户手动上传 / 替换 `AI视频制作_Source索引与使用优先级_V1.8.md`。如需同步到本地 `sources/`，也必须由用户手动处理。Codex / automation 不得直接修改、stage、commit、push official Source 文件。  
> 替换建议：**替换 V1.8**。V1.8 的 Source 优先级仍基本有效，但其中 SHOT-04 R02 当前状态停留在 K244S/K245 前后，已被 K261/K262 和项目总状态报告更新。  

---

## 0. 本版更新目的

V1.9 在 V1.8 基础上做三类更新：

```text
1. 保留 V1.8 的 P0/P1/P2/P3 Source 优先级结构。
2. 更新 SHOT-04 R02 当前主线：从 near-wall guard-clash / sustained push 路线，转入 hit-stop + explosive knockback / wall-impact two-shot 路线。
3. 新增 Project Blueprint Source 入口：AI视频制作_项目蓝图与产品化路线_V0.1.md。
```

本版不替代任何单项动作规则、Dreamina CLI 契约、Prompt Compiler、失败台账或宏流程规则；它只负责“当前应先读什么、冲突时听谁、项目当前处在哪条主线”。

---

## 1. 推荐 Source 优先级

### P0：硬治理与执行边界

必须优先读取：

1. `AI视频制作_自动化治理与Source权限规则_V0.1.md`
2. `AI视频制作_自动化宏流程与授权等级_V0.2.md`
3. `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
4. `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
5. `Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
6. `dreamina_cli_help_latest.md`

P0 处理：

```text
Source 权限
Codex / automation 边界
submit/query/download/retry/resubmit/final/lock 授权
Dreamina CLI canary / command-contract preflight
media / sources / reports / edits staging 规则
```

硬规则继续有效：

```text
Codex 不修改 official sources/。
submit/query/download/retry/resubmit 必须分开授权，除非用户明确 macro 授权。
download success 不等于 visual success。
visual success 不等于 final/lock。
final/lock 必须人类明确批准。
```

---

### P0.5：项目蓝图与产品化路线

新增推荐 Source：

1. `AI视频制作_项目蓝图与产品化路线_V0.1.md`

适用场景：

```text
新 chat 项目恢复
长期架构讨论
半自动 / 全自动流程设计
GUI / 小软件规划
从单个视频制作升级到生产系统设计
macro-run 与 K-phase 关系判断
```

读取位置：

```text
常规生产 K-phase：可在 P0 后按需读取。
项目架构 / Pro Extended synthesis：P0 后必须读取。
Codex repo-wide context recovery / macro-run planning：P0 后建议读取。
```

该文件不替代 P0 硬治理，也不提供 Dreamina CLI 命令事实。

---

### P1：Prompt 与动作规则

必须按任务读取：

1. `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
2. `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
3. `AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
4. `AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
5. `AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
6. `AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`

P1 处理：

```text
result-first prompt
P0 / P1 / P2 prompt priority
action causality
contact / hit-stop / beat schedule
route reset
close-combat brittleness
空间调度 / 站位 / 视角 / 场景锚点
```

对于 SHOT-04 R02 / 双人近身战斗，P1 必须优先读取 Prompt Compiler V0.2、V1.12、V1.11、V1.2、V1.8 多模态规则和动作参考视频库规则。

---

### P2：多模态、IP 安全、参考体系

1. `AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
2. `AI视频制作_动作参考视频库与审片标准_V0.1.md`
3. `DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`

P2 处理：

```text
reference duty
identity ref / scene ref / action ref / camera ref / audio ref 分工
动作参考视频作为 action grammar，而不是默认 active input
manifest schema
IP / 外部资料安全吸收
```

---

### P3：剧本、美术、传统故事、风格扩展

保留既有 V1.3–V1.7 等规则库，按具体任务需要读取：

```text
AI视频制作_实测规则库_V1.3_外部案例观察与关键帧规则增补稿.md
AI视频制作_实测规则库_V1.4_外部知识库与商业视觉模板增补稿.md
AI视频制作_实测规则库_V1.5_剧本美术与分镜设计增补稿.md
AI视频制作_实测规则库_V1.6_分镜模板与风格词库增补稿.md
AI视频制作_实测规则库_V1.7_中国传统故事与神话改编增补稿.md
```

P3 处理：

```text
故事目标
角色动机
美术圣经
分镜表
传统故事 / 神话改编
风格词库
商业视觉模板
```

---

## 2. Evidence Pack 与 Reports 地位

以下仍是证据，不是 official Source：

```text
reports/
reports/evidence_consolidation/
K-phase reports
review reports
Codex source update candidates
ChatGPT 对话中未确认的草案
```

K244S evidence pack、K261/K262 reports、PHASE_PROJECT_TOTAL_STATE_CONTEXT_RECOVERY_REPORT 都可以作为 Source synthesis evidence，但不能直接替代 Source。

Codex 可以：

```text
读取 reports/
读取 evidence packs
在 reports/source_update_drafts/ 或指定 report 中生成 Source candidate
提醒用户需要 Source update
```

Codex 不可以：

```text
把 reports/ 内容直接复制进 sources/
自动替换 Source Index
自动提交 Source update
```

---

## 3. 当前项目状态入口

### 3.1 AI_VIDEO_PIPELINE 总体状态

当前项目不再只是 Phase A Python skeleton。它同时是：

```text
1. AI 视频生产 pipeline Python skeleton。
2. 《赤焰对天穹》生产 evidence repository。
3. Source / report / prompt / package / manifest / review artifacts / failure ledger 的操作仓库。
4. 未来半自动 / GUI / gated macro-run 系统的原型仓库。
```

项目当前已经具备：

```text
Source governance
K-phase 报告链
no-submit package workflow
package review
submit/query/download 分离
review artifacts
ChatGPT Pro / human visual review
failure ledger
route reset
Source update candidates
```

项目仍未完全具备：

```text
真实 Dreamina live 的 Python runner 自动化
完整 GUI / frontend
稳定双人近身动作生成
无人值守 final/lock
成熟 production macro-run
```

---

### 3.2 SHOT-04 R02 当前主线状态

截至 K262 / Project Total State Context Recovery：

```text
旧路线已停止：
near-wall guard-clash pressure without wall contact / sustained push route

停止原因：
K260 CUT_A / CUT_B 身份有进步，但动作读成 sustained pressure / slow push，不符合用户想要的 “piu 一下” hit-stop + burst。

当前新目标：
hit-stop + explosive knockback / wall impact / wall hole / through-wall result

推荐路线：
two-shot edit route

R02a：
contact / brief hit-stop

R02b：
fast knockback / wall impact aftermath

当前推荐下一阶段：
K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE
```

当前状态必须保持：

```text
final_master=false
locked=false
no automatic submit
no automatic query
no automatic download
no automatic retry/resubmit
no automatic final/lock
```

---

## 4. 当前推荐工作顺序

### 4.1 常规 Codex 执行顺序

Codex 任务建议读取顺序：

```text
1. Source Index V1.9
2. P0 硬治理 / 宏流程 / Dreamina 契约
3. Project Blueprint V0.1（如果任务涉及系统设计、context recovery、macro-run、GUI、长期架构）
4. Prompt Compiler V0.2
5. 对应动作 / 多模态 / 失败台账 Source
6. task-specific reports/evidence
7. prompt/package/manifest/asset files
```

### 4.2 SHOT-04 R02 K263 任务顺序

当前生产线下一步：

```text
K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE
```

K263 只允许：

```text
prompt txt
package JSON
manifest CSV
K263 report
```

K263 禁止：

```text
Dreamina
submit
query
download
retry
resubmit
media
cut
frames
contact sheets
sources/ modification
final/lock
```

K263 后续：

```text
K264_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE_REVIEW
```

K264 仍然不自动 submit。

---

## 5. 冲突处理

如果本 Source Index 与较旧 Source Index 冲突：

```text
以 V1.9 为当前索引。
```

如果本 Source Index 与 P0 硬治理冲突：

```text
以 P0 硬治理为准。
```

如果本 Source Index 与当前本地 Dreamina CLI help 冲突：

```text
以当前运行时 dreamina <command> -h 为准。
```

如果本 Source Index 与某个 task-specific report 冲突：

```text
task-specific report 可作为当前 shot 状态证据；
但 official Source 规则仍以已确认 Source 为准。
```

如果 K262 / Project Context Recovery 与 V1.8 中 K244S 状态冲突：

```text
以 K262 / Project Context Recovery 的当前状态为准。
V1.8 中的 K244S/K245 状态已过时。
```

---

## 6. Source 更新周期建议

每当出现以下情况，应生成 Source update candidate：

```text
连续失败 / 成功形成稳定模式
重大 route reset
用户明确改变创意目标
macro-run 需求发生变化
Dreamina CLI help / command contract 改变
project architecture / GUI / productization 进入新阶段
```

每完成一个重要 shot 阶段，或出现连续失败，应继续生成：

```text
failure ledger
success ledger
prompt outcome dataset
source update candidates
```

official Source 仍由：

```text
ChatGPT 生成 / 审阅
human 手动上传 / 替换 / 同步
```

Codex 仍保持 read-only Source consumer。

---

## 7. 当前推荐 active Source 列表摘要

### 必备

```text
AI视频制作_Source索引与使用优先级_V1.9.md
AI视频制作_项目蓝图与产品化路线_V0.1.md
AI视频制作_自动化治理与Source权限规则_V0.1.md
AI视频制作_自动化宏流程与授权等级_V0.2.md
AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md
AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md
AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
AI视频制作_动作参考视频库与审片标准_V0.1.md
Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
dreamina_cli_help_latest.md
```

### 按任务补充

```text
Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md
AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md
AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md
AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md
AI视频制作_实测规则库_V1.3-V1.7 系列
```

---

## 8. Final Verdict

```text
SOURCE_INDEX_V1_9_READY_TO_REPLACE_V1_8
```
