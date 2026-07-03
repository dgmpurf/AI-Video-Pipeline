# Audit Sampling Policy V0.1

本策略用于参考库批量粗标后的抽查和规则回写。

## 1. 基本原则

- 抽查不是为了追求形式合格，而是为了发现标签口径漂移。
- 任何 active input、prompt_ready、风险规则冲突都必须保守处理。
- Codex 自动候选只能进入 review queue，不能直接成为 final label。

## 2. 抽查比例

### 随机抽查

- 随机抽查 5%。
- 覆盖不同 source_type、标签簇、文件来源和导入批次。

### 低置信度

- 低置信度 100% 抽查。
- 建议阈值：`confidence < 0.70`。

### Codex 与规则冲突

- Codex 与 tag_rules / alias_rules / risk_rules 冲突 100% 抽查。
- 冲突样本不得自动通过。

### active input 候选

- active input 候选 100% 抽查。
- 只有人工确认后才允许 `active_input_allowed=true`。

### prompt_ready 候选

- prompt_ready 候选 100% 抽查。
- 只有人工确认后才允许 `prompt_ready=true`。

### 高风险 source_type

- 高风险 source_type 抽查 20%-30%。
- 包括疑似版权敏感、肖像明显、品牌明显、影视/游戏/广告高相似来源、过近复制风险片段。

### 新标签 / 新来源批次

- 新标签或新来源批次抽查 20%。
- 目标是确认标签定义和来源边界没有漂移。

### 高复用标签

- 高复用标签抽查 10%。
- 重点检查标签是否被过度泛化，是否需要拆分或改名。

## 3. 抽查输出

每次抽查应输出：

- sampled_ref_ids
- sampling_reason
- accepted_labels
- rejected_labels
- corrected_aliases
- corrected_risk_tags
- rule_update_candidates
- needs_gold_adjudication

## 4. 规则回写

抽查结论用于更新候选规则：

- tag_rules
- alias_rules
- risk_rules
- do_not_copy templates
- reference_duty templates
- ChatGPT structured review template
- Codex auto suggestion schema

任何进入 official Source 的规则仍需用户人工确认。
