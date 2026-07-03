# AI视频制作_模仿参考库Calibration流程_V0.1

## 1. 目的

Calibration V0.1 用于在正式批量索引前，先建立一套稳定、可复核、可人工裁决的参考库标注口径。

目标不是一次性把所有参考片段深度标完，而是先用小样本 gold set 校准三件事：

- 什么标签能稳定描述画面、动作、剪辑、FX、构图、环境反馈和风格。
- 哪些用户主观词可以映射到 controlled tags。
- 哪些风险或使用限制必须阻止 active input 或 prompt_ready。

## 2. 为什么不全量三方深标

不建议一开始对全库做 user / ChatGPT / Codex 三方深标，原因如下：

- 成本过高：视觉拆解、人工感受、结构化标签和裁决都需要时间。
- 口径未校准：未建立规则前，全量深标会放大早期标签混乱。
- 标签会变动：前 100-200 条样本常会暴露缺失标签、重名标签、粒度不一致和风险规则漏洞。
- Codex 只能给候选：Codex 自动建议不能替代人工视觉判断，也不能确认 active input。
- ChatGPT 视觉分析也需要锚点：如果没有用户感受和 controlled tag 字典，结构化 review 容易产生风格相近但不可检索的标签。

因此 V0.1 采用小样本校准，然后再批量粗标和抽查。

## 3. Gold set 范围

先做 100-200 条 gold set。

建议覆盖：

- 动作参考：推、撞、滑、飞出、格挡、踢、摔、停顿、反弹。
- 运镜参考：固定机位、跟随、手持、推拉、侧向追踪、低机位。
- FX 参考：火、烟、尘、碎片、水花、湿地反光、冲击波。
- 剪辑节奏：hit stop、慢动作、快切、尾段 pose out。
- 环境反馈：墙面、地面、水面、碎片、光影变化。
- 风险样本：版权疑似、人物肖像、品牌标识、过近复制、不可做 active input。

Gold set 的目标是校准规则，不是追求覆盖整个库。

## 4. 三方角色

### 用户

用户负责主观感受和最终裁决。

用户记录：

- 我看到什么。
- 我觉得哪里有用。
- 想搜索时会用什么词。
- 是否直觉上可以做 active input。
- 风险直觉。

用户的判断是 final label、prompt_ready 和 active_input_allowed 的最终依据。

### ChatGPT / ChatGPT Pro

ChatGPT 负责视觉拆解和结构化 review。

ChatGPT 输出：

- visual_summary
- controlled_tags
- impression_tags_mapped
- reference_duty
- do_not_copy
- prompt_words
- review_criteria
- risk_tags
- usage_class recommendation
- active_input recommendation
- uncertainty

ChatGPT 的输出是结构化候选，不自动成为 final label。

### Codex

Codex 负责本地文件路径、元数据、命名、规则冲突、候选标签和批量一致性检查。

Codex 可以输出 auto suggestion，但必须保留为候选：

- Codex auto suggestion 不是 final label。
- Codex 不确认 visual truth。
- Codex 不确认 active_input_allowed。
- Codex 不确认 prompt_ready。
- Codex 发现规则冲突时必须标记 needs_human_review=true。

## 5. User impression tags 与 controlled tags

### User impression tags

User impression tags 是用户自然语言感受词。

例子：

- "很重"
- "像撞到墙"
- "湿地滑出去"
- "节奏很猛"
- "不适合当参考"
- "像游戏动作"

特点：

- 可以主观。
- 可以重复。
- 可以混合中文、英文、项目黑话。
- 适合搜索入口和 alias_rules。

### Controlled tags

Controlled tags 是参考库内部用于稳定检索和规则判断的受控标签。

例子：

- action.guard_clash
- motion.backward_flyout
- environment.wet_floor_feedback
- edit.hit_stop
- camera.locked_side_view
- risk.active_input_blocked

特点：

- 命名稳定。
- 含义单一。
- 可以被数据库、索引器和审计规则使用。
- 必须经 gold adjudication 通过后进入正式 tag_rules。

## 6. Codex auto suggestion 边界

Codex auto suggestion 只是候选，不是 final label。

Codex 可以根据文件名、目录、已有 manifest、已有标签、文本备注和规则表推断候选，但不能替代视觉审片。

必须保留：

- `active_input_allowed_must_remain_false=true`
- `needs_human_review=true`，除非后续规则明确允许低风险字段自动通过。
- `confidence` 只表示候选可靠度，不表示视觉真值。

## 7. active_input_allowed 与 prompt_ready

### active_input_allowed

`active_input_allowed` 必须人工确认。

默认值：

```text
active_input_allowed=false
offline_grammar_only=true
```

只有当用户确认版权、安全、肖像、品牌、复制风险、用途边界都可接受时，才可以进入 active input 候选。

### prompt_ready

`prompt_ready` 必须人工确认。

一个片段即使适合离线学习动作语法，也不等于可以直接影响 prompt。

prompt_ready 需要确认：

- 可抽象成动作、运镜、节奏、构图或环境反馈规则。
- 不会诱导复制具体角色、品牌、镜头构图或风格资产。
- 有明确 reference_duty 和 do_not_copy。

## 8. 校准输出规则

Gold set 完成后，应形成三类规则。

### tag_rules

用于定义 controlled tags：

- 标签名。
- 标签定义。
- 可用例。
- 反例。
- 是否可自动候选。
- 是否需要人工确认。

### alias_rules

用于把用户自然语言感受映射到 controlled tags：

- impression phrase。
- normalized alias。
- mapped controlled tag。
- confidence。
- examples。

### risk_rules

用于限制使用方式：

- risk_tag。
- source_type。
- blocked usage。
- active_input_allowed 默认值。
- prompt_ready 默认值。
- 审核要求。

## 9. 后续批量粗标

校准完成后，才进入批量粗标。

推荐流程：

1. Codex 或本地索引器生成候选记录。
2. 根据 tag_rules 生成 suggested_tags。
3. 根据 alias_rules 连接用户搜索词。
4. 根据 risk_rules 设置风险候选。
5. 所有 active input 候选保持人工审核。
6. 所有 prompt_ready 候选保持人工审核。
7. 把低置信度和规则冲突样本放入审计队列。

## 10. 抽查闭环

抽查结果反向更新：

- tag_rules
- alias_rules
- risk_rules
- do_not_copy 模板
- reference_duty 模板
- ChatGPT review prompt
- Codex auto suggestion schema

抽查不是形式检查，而是持续修正参考库语义边界。
