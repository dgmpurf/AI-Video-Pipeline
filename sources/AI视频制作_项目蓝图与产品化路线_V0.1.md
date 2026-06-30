# AI视频制作_项目蓝图与产品化路线_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Blueprint Source / 产品化路线 / 系统架构规则  
> 版本：V0.1 Draft  
> 生成日期：2026-06-30  
> 生成方：ChatGPT Pro Extended  
> 来源：Project Source 全量阅读 + GitHub repo 远端阅读 + PHASE_PROJECT_TOTAL_STATE_CONTEXT_RECOVERY_REPORT + 上一条 chat 交接说明 + AI_VIDEO_PIPELINE_PROJECT_BLUEPRINT_V0.1 对话综合  
> 应用方式：建议作为**新增 Source** 手动上传 / 应用。不要替换现有 Source。  
> 替换建议：**新增，不替换**。本文件补充“项目级目标、系统架构、半自动/GUI/产品化路线”，不替代治理、Prompt Compiler、失败台账、动作规则或 Dreamina CLI 执行契约。  

---

## 0. 一句话定义

```text
AI_VIDEO_PIPELINE 是一个以《赤焰对天穹》为高压测试项目，
逐步搭建的可审计、可复盘、可半自动化扩展的 AI 视频生产系统。
```

它不是单纯 prompt 工程，也不是单个 Dreamina CLI wrapper。它的目标是把：

```text
剧本 / 小说 / 一句话想法
→ 生产剧本
→ 分镜
→ 资产规划
→ prompt / package / manifest
→ Dreamina submit / query / download
→ review artifacts
→ 人类 + ChatGPT Pro 审片
→ failure ledger / success ledger
→ route reset
→ Source 更新候选
→ 剪辑成片
```

组织成一条可追踪、可授权、可中断、可复盘的流水线。

---

## 1. 项目三层结构

### 1.1 作品层

当前代表作品：

```text
《赤焰对天穹》
```

它承担具体内容生产：

```text
角色
场景
打斗
运镜
环境互动
剪辑
最终成片
```

但它不是项目全部。

---

### 1.2 流水线层

当前已经形成的生产链：

```text
K-phase planning
→ no-submit package
→ package review
→ human authorization
→ one-submit
→ one-query
→ download-only
→ review artifacts
→ human / ChatGPT Pro visual review
→ failure classification
→ route reset
→ Source update candidates
```

这条流水线的核心价值是：

```text
证据明确
边界明确
失败可复盘
成功不被误判为 final
```

---

### 1.3 产品层

长期目标：

```text
AI 视频制作操作系统 / 半自动生产平台 / GUI 工具
```

未来用户应能通过界面或结构化输入完成：

```text
输入剧本或想法
自动拆解镜头
自动规划资产
自动生成 package
自动执行授权范围内任务
自动生成审片材料
自动沉淀失败和成功
```

但“自动”必须是 gated macro-run，不是无脑一键到底。

---

## 2. 系统目标

AI_VIDEO_PIPELINE 的目标是解决：

```text
1. 从自然语言创意到可执行 AI 视频任务的编译。
2. 角色、场景、道具、动作、镜头、声音的资产级规划。
3. 多平台 / 多模型生成任务的 package / manifest / prompt 管理。
4. Dreamina CLI 等执行层的安全调用。
5. submit / query / download / retry / final / lock 的授权边界。
6. 图像 / 视频审片证据链。
7. 失败分类、路线重置、Source 进化。
8. 最终面向短剧、vlog、AI 剧集、广告片、角色 IP 短片等生产形态。
```

非目标：

```text
不是让 Codex 无限制自动花费积分。
不是 submit 成功就自动 query/download。
不是下载成功就自动 final。
不是让 reports 直接替代 Source。
不是让 Source 自动被 Codex 修改。
不是无人值守 final/lock。
```

---

## 3. 当前已完成能力

### 3.1 规则层

已经具备：

```text
Source Index
Source governance
自动化宏流程与授权等级
Prompt Compiler
失败台账与路线重置
动作密度与环境破坏因果规则
多模态参考职责规则
Dreamina CLI 执行契约
动作参考视频库与审片标准
```

这些规则已经足以支撑高风险动作镜头的 no-submit package、package review、live authorization 判断和 route reset。

---

### 3.2 报告层

已经具备：

```text
K-phase reports
package review reports
submit/query/download reports
visual review reports
local cut diagnostic reports
failure ledger
success / partial success ledger
prompt outcome dataset
source update candidates
context recovery report
```

reports 是证据，不是 Source，但它们已经是系统复盘和 Source synthesis 的主要输入。

---

### 3.3 代码层

当前 Python skeleton 已经覆盖：

```text
PathPolicy
Manifest parser / validator
TaskSpec / AssetRecord / ShotRecord / ReviewRecord 等 data models
Dreamina CLI command argv builder
media integrity / sha256
internal staging
dry-run / mock-run
fake live provider
job store
run plan
run context
path scan
pytest coverage
```

当前代码层仍不等同于完整生产自动化。

---

### 3.4 生产层

《赤焰对天穹》已经验证：

```text
no-submit package creation
package review
Dreamina canary / preflight
one-submit-only
one-query-only
download-only
metadata / sha256 validation
review artifacts
ChatGPT Pro visual review
human creative correction
route reset
```

---

## 4. 当前未完成 / 高风险能力

### 4.1 真实 Dreamina live runner

当前真实 Dreamina live submit/query/download 主要依赖 Codex 按 phase prompt 手动执行和报告。

Python runner 中已有 live skeleton / fake provider，但真实 Dreamina live provider execution 尚未成为稳定 production runner。

---

### 4.2 GUI / 产品层

当前没有成熟 GUI / 前端产品层。

未来需要设计：

```text
Project Dashboard
Source Panel
Story / Script Compiler
Asset Planner
Prompt / Package Panel
Authorization Panel
Dreamina Execution Panel
Review Panel
Human Review Panel
Failure Ledger Panel
Route Reset Panel
Source Candidate Panel
```

---

### 4.3 复杂视觉生成能力

仍然高风险：

```text
双人近身战斗
身份稳定 + 动作稳定同时成立
墙体接触 / 破墙 / 穿墙
hit-stop 后爆发击飞
湿地滑步 / 雨水反馈因果
多 refs reference attention conflict
```

系统可以更好地诊断这些失败，但不能保证模型一次成功。

---

## 5. 标准系统模块

AI_VIDEO_PIPELINE 应长期收敛为以下模块：

```text
A. Input / Story Compiler
B. Script / Shot Compiler
C. Asset Planner
D. Reference Duty Planner
E. Prompt Compiler
F. Package Builder
G. Independent Package Review
H. Human Authorization Gate
I. Dreamina Execution Layer
J. Query / Download Layer
K. Review Artifact Builder
L. Human + Pro Visual Review Recorder
M. Failure / Success Ledger Writer
N. Source Update Recommender
O. Edit / Export Planner
P. GUI / Product Interface
```

其中：

```text
Source Loader = read-only
Source Update Recommender = report/draft only
Official Source Writer = 不存在于 Codex/automation 中
Official Source Application = human only
```

---

## 6. 人机分工

### 6.1 ChatGPT Think

用于：

```text
Codex 回执判断
report-only
package review
submit/query/download 授权判断
路线规划
给 Codex 写 prompt
```

---

### 6.2 ChatGPT Pro

用于：

```text
上传图片 / 视频 / contact sheet 后做视觉审查
动作成败判断
人物身份判断
edit candidate 判断
是否可作为 primary / failure evidence / final candidate
```

---

### 6.3 ChatGPT Pro Extended

用于：

```text
Source synthesis
大规模规则库更新
宏流程重构
长期项目架构整理
项目蓝图 / GUI / 产品化规划
```

---

### 6.4 Codex

Codex 负责：

```text
读取 sources/ 和 reports/
检查 git status
创建 prompt/package/manifest/report
校验 JSON/CSV/hash/path
执行授权范围内的 Dreamina 命令
本地下载校验
抽帧/contact sheet
本地 cut diagnostic
stage/commit/push 允许的 text report
```

Codex 不负责：

```text
决定 final/lock
擅自 retry/resubmit
擅自改 Source
擅自 stage media
擅自自动花费积分
替用户做最终审美判断
```

---

### 6.5 Human user

人类负责：

```text
授权 live 操作
审查图片 / 视频 / review artifacts
决定 creative direction
决定 final/lock
手动应用 official Source update
决定长期产品路线
```

---

## 7. 宏流程原则

### 7.1 一键式定义

```text
一键式 = gated macro-run
不是无限自动化
```

它必须：

```text
带授权边界
带内部 gate
可中断
可审计
可复盘
可回滚
```

---

### 7.2 授权等级

```text
L0：纯规划/报告
L1：本地 artifacts
L2：no-submit package
L3：单项 live：one-submit / one-query / download-only
L4：bounded macro-run
L5：future production macro-run
```

默认：

```text
final/lock 永远需要人类明确确认。
```

---

### 7.3 强制 Stop Gates

macro-run 必须在以下情况停止：

```text
sources/ 脏
package defect
command contract 不匹配
需要 submit 授权
submit-only 完成
query-only 完成
success 但 download 未授权
media 存在但未 visual review
remote failure 重复
路线重大变化
final/lock
Source update
```

---

## 8. GUI 产品蓝图

未来 GUI 不应只是 prompt 输入框，而应是 production cockpit。

建议模块：

### 8.1 Project Dashboard

显示：

```text
project
shot
phase
current route
final_master
locked
next recommended phase
```

### 8.2 Source Panel

显示：

```text
active Source index
P0/P1/P2/P3
dirty source warning
source update candidates
manual upload status
```

### 8.3 Story / Script Compiler

输入：

```text
小说
剧本
一句话
世界观
镜头想法
```

输出：

```text
beats
shots
characters
actions
dialogue
sound
locations
risks
```

### 8.4 Asset Planner

管理：

```text
A
L
C
HC
CTRL
SHOT
locked_refs
working_refs
evidence_only_assets
```

### 8.5 Prompt / Package Panel

显示：

```text
prompt txt
package JSON
manifest CSV
refs
excluded refs
risk labels
no_submit flags
```

### 8.6 Authorization Panel

分开授权：

```text
submit
query
download
retry
resubmit
media creation
final
lock
```

### 8.7 Execution Panel

显示：

```text
Dreamina version
user_credit
target command help
submit_id
logid
gen_status
download_url_present
sha256
metadata
```

### 8.8 Review Panel

展示：

```text
video
contact sheet
frames
metadata
cut candidates
visual review fields
```

### 8.9 Failure Ledger Panel

沉淀：

```text
remote final-generation failure
visual execution failure
prompt priority failure
reference attention conflict
identity drift
route reset
```

### 8.10 Route Reset Panel

比较：

```text
Option A
Option B
Option C
risk
cost
next package
review criteria
```

---

## 9. 当前生产线状态：SHOT-04 R02

当前事实：

```text
SHOT-04 R02 未 final。
locked=false。
K261 判定 CUT_A / CUT_B 不适合作为 primary。
K262 推荐 two-shot edit route。
```

当前路线：

```text
SHOT-04-R02a：contact / brief hit-stop
SHOT-04-R02b：fast knockback / wall impact aftermath
```

当前生产线下一步：

```text
K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE
```

K263 只应：

```text
创建 prompt txt
创建 package JSON
创建 manifest CSV
创建 K263 report
```

K263 禁止：

```text
Dreamina
submit
query
download
retry
resubmit
batch
media
cut
frames
contact sheets
sources/ modification
final/lock
```

---

## 10. 当前 30 / 60 / 90 天路线

### 10.1 30 天

目标：

```text
继续《赤焰对天穹》作为压力测试。
完成 K263 / K264 / 后续授权链。
建立 project status index / shot state index。
把 K244S / K261 / K262 / Project Context Recovery 继续沉淀为 Source candidates。
```

### 10.2 60 天

目标：

```text
固化 macro-run v0.3。
把 L0-L4 macro-run 做成可重复模板。
建立镜头类型库：
- 空镜
- 对峙
- contact / hit-stop
- knockback / impact aftermath
- reaction close-up
- insert
- transition
```

### 10.3 90 天

目标：

```text
设计 GUI 原型。
建立 project dashboard / source panel / package panel / authorization panel / review panel / failure ledger panel。
开始把部分 K-phase 操作产品化。
```

---

## 11. 当前不应做的事

不要：

```text
无人值守 live submit
自动 query/download
自动 retry/resubmit
自动 final/lock
Codex 自动改 Source
把 reports 当 Source
把 K255/K257 下载成功当最终成功
继续把 K260 CUT_A/CUT_B 当 primary
在 K263 一次解决 R02a + R02b + wall destruction + identity + continuity
```

---

## 12. Source 关系

本文件不替代：

```text
AI视频制作_Source索引与使用优先级
AI视频制作_自动化治理与Source权限规则
AI视频制作_自动化宏流程与授权等级
AI视频制作_Prompt编译器与结果优先动作语法
AI视频制作_实测规则库_V1.12
AI视频制作_实测规则库_V1.11
Dreamina CLI 执行契约
```

本文件只新增：

```text
项目级定义
系统层级
产品化方向
GUI 模块
长期路线
《赤焰对天穹》在系统中的测试职责
```

---

## 13. 使用方式

### 新 chat 项目恢复

先读：

```text
AI视频制作_Source索引与使用优先级_V1.9.md
AI视频制作_项目蓝图与产品化路线_V0.1.md
```

再读 P0/P1/P2/P3 对应 Source。

### Codex repo-wide context recovery

必须读取本文件作为项目级目标，但仍以 P0 治理 Source 决定权限边界。

### K-phase production

常规生产任务可以不每次全文读取本文件，但涉及以下情况时必须读取：

```text
macro-run
GUI
全自动 / 半自动讨论
项目结构调整
context recovery
Source synthesis
长期路线决策
```

---

## 14. Final Verdict

```text
PROJECT_BLUEPRINT_AND_PRODUCTIZATION_ROUTE_V0_1_READY_AS_NEW_SOURCE
```
