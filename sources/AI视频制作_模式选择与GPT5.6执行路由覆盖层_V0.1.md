# AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Source 候选 / 模式、模型、Effort 与执行环境覆盖层  
> 版本：V0.1  
> 生成日期：2026-07-18  
> 状态：待人类审阅并手动应用  
> 适用范围：Chat、ChatGPT Work、Codex、Sites，以及 GPT-5.6 模型族在本项目中的任务路由  
> 重要说明：本文件不替代授权、安全、Dreamina CLI、Prompt Compiler、失败台账或 final/lock 规则。Codex / automation 不得直接写入 `sources/`。

---

## 0. 本 Source 的定位

本 Source 只负责四件彼此独立的选择：

1. **Surface / Agent**：Chat、Work、Codex、Sites。
2. **Model**：当前账号和当前界面实际可用的模型。
3. **Effort / Speed**：Light、Medium、High、Extra High、Max、Ultra，以及 Standard / Fast。
4. **Execution Environment**：none、Local、Worktree、Cloud。

不得把它们压缩成一条“越高越强”的单一等级轴。

本 Source 不覆盖以下更高优先级规则：

- official Source 只能由人类手动应用；
- Dreamina submit / query / download / retry / resubmit / batch / final / lock 的授权边界；
- 当前本地 `dreamina <command> -h` 的命令事实；
- 媒体不得自动 stage / commit；
- `final_master=true` 与 `locked=true` 只能由人类明确批准。

---

## 1. 项目画像

AI_VIDEO_PIPELINE 是一个以本地媒体、仓库证据、Prompt 结果记忆和人工审片为核心的半自动 AI 视频制作系统。

常见任务族：

- 创意方向、剧本、分镜、镜头目标和 Prompt 设计；
- Source 综合、失败分析、路线重置和宏授权设计；
- 图片 / 视频 / contact sheet 的视觉审查；
- prompt / package / manifest / dataset / report 创建与核验；
- Dreamina CLI submit / query / download / metadata / 抽帧；
- Pipeline、GUI、runner、索引器和测试的工程实现；
- 长期 Prompt Calibration、Reference Library 和 Prompt Outcome Dataset；
- 汇报、商业材料和展示页面。

主要事实源：

```text
项目对话与人类授权
> official Project Source
> 当前仓库 / commit / report
> 本地媒体、refs、packages、manifests、datasets
> 当前运行时 Dreamina CLI help / canary / result
> 外部调研与校准材料
```

高风险边界：

- 付费生成与点数预算；
- 外部 provider 行为；
- 本地媒体和不可复现资产；
- official Source 权限；
- 自动 retry / resubmit / manifest expansion；
- final / lock；
- 版权、IP、隐私和对外发布。

---

## 2. 核心选择原则

### 2.1 按当前任务选择，不按项目永久绑定

同一个 AI 视频项目会在创意、资料综合、Prompt 设计、CLI 执行、工程实现、视觉审查和汇报之间切换。

每一轮先回答：

```text
当前主要验收物是什么？
事实源在哪里？
错误代价多高？
是否需要操作本地仓库、媒体或 CLI？
```

### 2.2 选择离事实源最近的环境

- 事实源是本地媒体、锁定参考图、未提交文件、Dreamina 登录态和 CLI：优先 **Codex Local**。
- 事实源是当前 Git branch / commit，且依赖和数据可在干净环境复现：可考虑 **Worktree / Cloud**。
- 事实源是多份文档、研究资料、表格和报告：优先 **Work**，前提是当前账号和界面可用。
- 事实源是本轮对话与少量附件：优先 **Chat**。
- 目标只是发布成熟的轻量网页成果：考虑 **Sites**。

### 2.3 用足够而不过量的能力

最高模型和最高 Effort 不是永久默认。

升级信号：

- 需求含糊且跨多个 Source；
- 多轮返工仍遗漏约束；
- 需要跨项目或跨阶段综合；
- 付费执行、Source 更新、重大路线重置或最终风险判断；
- 问题可拆成多个真正独立的只读审查子任务。

降级信号：

- schema 固定；
- 输入输出清楚；
- 可自动或抽样验收；
- 重复 metadata、hash、分类、格式转换；
- 前一档已稳定通过多轮。

### 2.4 阶段变化时重新路由

研究转实现、实现转执行、下载转审片、审片转 final、单次试验转批量宏流程时，必须重新选择 Surface、Model、Effort 和 Environment。

---

## 3. 项目专属默认路由

| 当前任务 | Surface | Model / Effort 默认倾向 | Environment |
|---|---|---|---|
| 创意方向、剧本、分镜、镜头目的、Prompt 路线 | Chat | GPT-5.6 Sol / High | none |
| 复杂 Prompt Compiler、重大失败分析、路线重置、宏授权设计 | Chat | GPT-5.6 Sol / Extra High；极难且强耦合时考虑 Sol Pro | none |
| official Source 候选综合与多文件规则重构 | Chat 或 Work | GPT-5.6 Sol / Extra High；关键版本可用 Sol Pro 独立复核 | cloud or desktop materials |
| 图片、视频、contact sheet 的视觉审查 | Chat | GPT-5.6 Sol / High 或 Extra High | uploaded media |
| 长研究、报告、表格、演示、Prompt Outcome Dataset 汇总 | Work（当前账号可用时） | GPT-5.6 Sol / High 或 Extra High | Web / Desktop 按事实源 |
| prompt/package/manifest/hash/report 创建与核验 | Codex | 当前可用 Sol 或 Terra / Medium–High | Local |
| Dreamina CLI、下载、metadata、抽帧、contact sheet | Codex | 当前可用 Sol 或 Terra / Medium–High | Local |
| 规则明确的大批量 metadata、hash、分类、格式转换 | Codex | Terra 或 Luna / Medium；先小批验证 | Local |
| Pipeline、GUI、runner、索引器、测试、Git 闭环 | Codex | Sol / High；明确小改可降低 Effort | Local / isolated Worktree |
| Codex Cloud | Codex | 按任务选择 | 仅当 Git、依赖、数据和命令均可复现 |
| 作品展示页或轻量 Demo | Sites | Sites 不是推理档位 | 内容和交互稳定后 |

补充规则：

- 标准 Chat 中实际可见的模型选项优先于旧 Source 名称。
- Terra / Luna 仅在当前 Work / Codex / API 界面确实可用时选择。
- Work 处于分阶段开放时，Source 只写“可用时倾向”，不得假定必然存在。
- 模型不可用时，保持任务边界不变，选择当前界面中足够可靠的替代组合。

---

## 4. Plan、Goal 与 Scheduled

### Plan

适用：

- 方法、范围、manifest、风险或验收仍未确定；
- 只允许只读检查、设计和候选文件；
- 需要先由人类审查再激活执行。

### Goal

适用：

- 目标、输入、边界、停止条件和验收物清楚；
- 允许在限定工作区持续推进；
- 所有外部写入和付费动作仍受显式授权限制。

### Scheduled

仅在以下条件都满足后使用：

- 人工流程已跑通；
- Prompt 和 schema 稳定；
- 输入可验证；
- 失败处理、权限和通知规则已明确；
- 不涉及未经确认的 final / lock / 外部不可逆动作。

---

## 5. AI 视频项目的固定分工

### Human

负责：

- 创意目标与路线选择；
- 付费执行授权；
- 视觉判断；
- Source 手动应用；
- final / lock；
- 版权与商业用途的最终判断。

### Chat / Work

负责：

- 创意与 Prompt 设计；
- Source 正式候选；
- 复杂失败分析；
- 宏流程和授权文本；
- 多来源研究与汇总；
- 视觉审查和下一路线判断。

### Codex

负责：

- 本地仓库和媒体操作；
- git/source preflight；
- prompt/package/manifest/dataset 创建；
- CLI 执行；
- metadata、hash、抽帧、contact sheet；
- 报告、测试、diff、commit / push。

Codex 不负责：

- official Source 直接写入；
- 无界 retry / resubmit / manifest expansion；
- 最终视觉批准；
- final / lock。

---

## 6. 正式授权文本语言

从本版起，**正式授权文本默认使用英文**。

适用对象：

- submit / query / download / retry / resubmit / batch 授权；
- macro-run 授权；
- Source update 授权；
- final / lock 授权；
- 任何需要 Base64 / SHA256 记录的 canonical authorization。

允许：

- 项目讨论、解释和审片继续使用中文；
- Codex 执行 Prompt 可中英混合；
- 报告可保留中文说明。

除非人类用户明确改变规则，canonical authorization text 必须为英文。

---

## 7. Legacy 标签迁移

历史记录中的：

```text
Think
Pro
Pro Extended
Codex High
Codex Extra High
```

保持原样，不回写历史。

过渡期建议双标注：

```text
当前建议 ChatGPT mode: Think
迁移标注：
Surface: Chat
Model: GPT-5.6 Sol
Effort: High
Execution: none
```

新 Source 和新宏流程优先写四轴字段：

```yaml
surface:
model:
effort:
execution_environment:
task_mode:
```

不得写成：

```text
Pro = Ultra
Think = Medium
有代码 = Cloud
所有复杂任务 = Sol Pro
```

---

## 8. CAL-001 Prompt Calibration 路由

当前 CAL-001A 状态：

```yaml
authorization_type: conditional_pre_authorization
execution_authority_active: false
fixed_manifest_target_count: 84
credit_budget_max: 5880
credit_floor: 560
retry_count_max: 0
resubmit_count_max: 0
batch_expansion: false
final_master: false
locked: false
```

激活前必须完成：

1. CAL-001-P1：84 条固定 no-run manifest、packages、dataset schema、scoring schema 和预算计划；
2. CAL-001-P2：独立只读 package / budget / permission / stop-condition 审查；
3. 人类 manifest 接受；
4. CAL-001-P3：activation-precondition audit；
5. live Dreamina canary、成本和命令契约通过；
6. 所有 13 项 activation preconditions 为 true。

在此之前：

```text
Dreamina execution forbidden
submit/query/download forbidden
automatic task expansion forbidden
execution_authority_active=false
```

CAL-001B 不由 CAL-001A 隐含授权，必须使用独立英文授权文本。

---

## 9. 自我纠偏

遇到以下情况，先修正环境或任务拆分，不要只提高 Effort：

- Work / Codex 看不到事实源；
- Cloud 缺少本地媒体或未提交状态；
- 多 agent 同时修改同一核心文件；
- Prompt 任务与 CLI 执行混在一轮；
- 单一会话同时承担研究、实现、批量执行和最终发布。

连续出现以下信号时升级模型或 Effort：

- 关键约束被遗漏；
- 失败分类相互冲突；
- 多 Source 冲突无法收敛；
- 宏授权或预算边界存在解释歧义；
- 需要重大路线重置。

连续稳定通过并可抽样验收时，可降低模型或 Effort。

---

## 10. 冲突与维护

优先级：

```text
人类当前明确授权
> P0 治理与安全
> 当前运行时 CLI / 当前 UI 实际能力
> 本覆盖层
> 旧模式标签和历史经验
```

维护规则：

- 当前 UI 与本文不一致时，以当前账号实际可用选项为准；
- OpenAI 产品、模型、Work / Codex 能力变化时，先更新本覆盖层，不机械重写全部项目 Source；
- Dreamina、模型成本和 CLI 行为变化不写入本文件，由对应 CLI / 平台 Source 管理；
- 本文件只记录长期有效的选择逻辑和项目特有边界。
