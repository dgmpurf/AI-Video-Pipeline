# AI视频制作_动作家族校准实验综合与生产边界_V0.1

> 类型：P1 provisional experimental findings / cross-experiment synthesis  
> 证据范围：CAL-003 R1、CAL-004 R1、CAL-005 R1  
> 生成日期：2026-07-30  
> 激活判定：被用户手动加入 Project Source 后可作为 provisional evidence 读取。  
> **不是 stable production rule，不修改 Prompt Compiler，不授权 Dreamina、Provider、production、final 或 lock。**

---

## 0. Formal synthesis

```text
CURRENT_CAL003_CAL004_CAL005_EVIDENCE_SUPPORTS_REPEATABLE_PUSH_LIKE_DIFFERENTIATION_BUT_NOT_IMPACT_SPECIFIC_CONDITION_LEVEL_REPLICATION
```

Human bounded interpretation：

```text
PUSH_LIKE_SIGNATURES_WERE_MORE_REPEATABLE_THAN_IMPACT_SPECIFIC_SIGNATURES_ACROSS_THE_CURRENT_CAL003_CAL004_CAL005_SETUPS_WHILE_THE_UNIQUE_CAUSE_REMAINS_UNRESOLVED_AND_NO_PROVIDER_WIDE_BIAS_OR_UNIVERSAL_PROMPT_CAUSALITY_IS_CLAIMED
```

中文：在当前三组受控实验中，PUSH-like 特征比 IMPACT-specific 特征更可重复；但无法把原因唯一归结为 Provider、Prompt、reference、route、scene 或 actor prior。

## 1. Direct experiment evidence

### CAL-003 — Reference repeatability

```yaml
PUSH_family_gate: PASS
PUSH_passes: 3/3
PUSH_median_own_score: 12
PUSH_median_margin: 8
IMPACT_family_gate: FAIL
IMPACT_passes: 0/3
IMPACT_median_own_score: 6
IMPACT_median_margin: -6
ordinal_pair_gate: FAIL
ordinal_pairs_passed: 0/3
```

可直接陈述：CAL-003 内 PUSH reference 产生了 repeatable PUSH-like differentiation；IMPACT reference 未产生 IMPACT-specific differentiation。

### CAL-004 — Impact causal isolation

```yaml
condition_gates_passed: 0/6
sample_gates_passed: 1/18
five_of_six_condition_median_margins_negative: true
I0_condition_gate: FAIL
I0_median_IMPACT: 9
I0_median_margin: 1
I0_sample_passes: 1/3
I0_vs_N0_IMPACT_delta: 4
I0_vs_N0_PUSH_delta: 0
I0_vs_N0_margin_delta: 2
```

可直接陈述：I0 出现 partial text-only signal，但没有 condition-level PASS。

### CAL-005 — Text-only replication

```yaml
N0R_gate: FAIL
N0R_passes: 0/3
N0R_median_PUSH: 4
N0R_median_IMPACT: 0
N0R_median_margin: -4
I0R_gate: FAIL
I0R_passes: 0/3
I0R_median_PUSH: 9
I0R_median_IMPACT: 7
I0R_median_margin: -3
I0R_vs_N0R_IMPACT_delta: 7
I0R_vs_N0R_PUSH_delta: 5
I0R_vs_N0R_margin_delta: 1
directional_partial_signal: false
```

Formal outcome：

```text
CAL005_R1_TEXT_ONLY_IMPACT_SIGNAL_NOT_CONDITION_GATE_REPLICATED
```

## 2. Provisional findings

### P01 — Cross-experiment asymmetry

```text
PUSH-like differentiation was more repeatable than IMPACT-specific differentiation
across the current CAL-003 through CAL-005 setups.
```

限制：setup-bounded、非 Provider-wide、无统计显著性声明。

### P02 — ACTION_REF_PUSH_02

```text
ACTION_REF_PUSH_02 has positive repeatability evidence inside CAL-003,
but is not production-stable and does not authorize production use.
```

不得把 CAL-003 的 3/3 PASS 直接变成 production approval。

### P03 — Current IMPACT recipes

```text
The current IMPACT reference and text-only IMPACT-hard recipes do not have
condition-level replication evidence sufficient for stable promotion.
```

这不证明 IMPACT generation 不可能；也不禁止未来使用不同 scene、actor blocking、camera、route、reference construction 或 Prompt decomposition 继续研究。

## 3. Unique-cause status

```yaml
unique_cause_identified: false
```

未解决候选原因：

- Provider/model behavior；
- Prompt wording 与动作分解；
- reference content 与 motion quality；
- command route / reference conditioning；
- scene / actor prior；
- review framework sensitivity；
- small replicate count。

本文件不对这些原因排序。

## 4. Gate precedence

- I0 的 median uplift 不覆盖 CAL-004 Gate FAIL；
- I0R-01 的 near-threshold sample 不覆盖 CAL-005 Gate FAIL；
- CAL-003 PUSH family PASS 不覆盖跨实验 production replication 要求。

正式规则由 Validator/Governance V0.2 管理。

## 5. Rejected overclaims

禁止：

1. `The Provider is universally biased toward PUSH.`
2. `IMPACT generation is impossible.`
3. `The IMPACT-hard Prompt is universally ineffective.`
4. `ACTION_REF_PUSH_02 is production-approved.`
5. `CAL-003 alone proves a stable production rule.`
6. `A higher median IMPACT score alone proves replication.`

## 6. Production implications

```yaml
current_IMPACT_recipe_promoted: false
ACTION_REF_PUSH_02_production_approved: false
main_production_line: paused
CAL006_authorized: false
production_reentry_authorized: false
```

未来恢复生产必须先：

- 完成 Project Source 人工应用与核验；
- 进行 production-context recovery；
- 将 action calibration evidence 与作品具体叙事、镜头和动作目标重新绑定；
- 取得有效 Provider access；
- fresh runtime verification；
- fresh human authorization。

## 7. Evidence anchors

```yaml
repository_head_after_synthesis: 2dfd67e6b6318133c0b342ebc99edb2dd32921c3
CAL003_decision_git_blob: b428c968b500e822e6f1a740aa01c222e82477fa
CAL004_decision_git_blob: 0b4eada2543b7cd08d02d44b344fac78c52a7445
CAL005_decision_git_blob: 7335e80ae7e1639cd685d188491dbd2d5b9fdc77
synthesis_report: reports/CAL003_CAL004_CAL005_CROSS_EXPERIMENT_SYNTHESIS_AND_SOURCE_UPDATE_EVIDENCE_PACK.md
```

## 8. Authority boundary

本文件仅为 provisional evidence。它不授权新实验、Dreamina、Provider、Source write、production re-entry、final master 或 lock。
