# AI视频制作_当前项目状态与双轨切换_V0.3

> 类型：Rolling Current State / replaceable state capsule  
> 快照日期：2026-07-30  
> 激活判定：**本文件被用户手动加入或替换到 Project Source 后，即为当前 active capsule；正文不使用永久性的“待应用”状态标签。**  
> 本文件只记录当前状态，不产生 Provider、live、unblind、Source write、production、final 或 lock authority。

---

## 0. 当前项目锚点

```yaml
project: AI视频制作 / AI_VIDEO_PIPELINE
repository: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE
remote: dgmpurf/AI-Video-Pipeline
branch: main
head: 2dfd67e6b6318133c0b342ebc99edb2dd32921c3
origin_main: 2dfd67e6b6318133c0b342ebc99edb2dd32921c3
head_origin_aligned: true
current_phase: SOURCE_UPDATE_CANDIDATE_PACK_READY_FOR_HUMAN_MANUAL_APPLICATION
previous_phase: CAL003_CAL004_CAL005_SYNTHESIS_COMPLETE_SOURCE_CANDIDATE_GENERATION_HUMAN_DECISION
next_phase: HUMAN_MANUAL_PROJECT_SOURCE_APPLICATION_AND_POST_APPLICATION_VERIFICATION
```

当前 HEAD 对应：

```text
synthesize(cal): prepare CAL003-CAL005 source evidence
```

精确 repository evidence 优先于本 capsule；HEAD 变化后应替换本文件，而不是叠加修补旧状态。

## 1. 全局 authority 状态

```yaml
provider_authority: false
submit_authority: false
query_authority: false
download_authority: false
retry_authority: false
resubmit_authority: false
batch_authority: false
unblind_authority: false
source_write_authority_for_codex: false
production_reentry_authorized: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
automatic_CAL006: false
```

所有 CAL-003 至 CAL-005 的 submit/query/download/blind/freeze/unblind/recovery/human-decision/synthesis 授权均已消费且不可复用。

## 2. CAL-003 / CAL-004 / CAL-005 关闭状态

### 2.1 CAL-003 R1

```yaml
experiment: CAL-003
program: REFERENCE_CONTROL_REPEATABILITY_V1
round_closed: true
human_final_decision_complete: true
PUSH_family_gate: PASS
PUSH_sample_passes: 3/3
PUSH_median_own_score: 12
PUSH_median_margin: 8
IMPACT_family_gate: FAIL
IMPACT_sample_passes: 0/3
IMPACT_median_own_score: 6
IMPACT_median_margin: -6
ordinal_pair_gate: FAIL
passing_ordinal_pairs: 0/3
```

Bounded interpretation：PUSH reference 在 CAL-003 设置中产生可重复 PUSH-like differentiation；IMPACT reference 未产生 IMPACT-specific differentiation。不得泛化为 Provider-wide bias。

### 2.2 CAL-004 R1

```yaml
experiment: CAL-004
program: IMPACT_FAMILY_CAUSAL_ISOLATION_V1
round_closed: true
human_final_decision_complete: true
condition_gates_passed: 0/6
sample_gates_passed: 1/18
five_of_six_condition_median_margins_negative: true
formal_label: PROVIDER_OR_SCENE_PUSH_PRIOR_DOMINANT
```

I0 text-only/no-reference：

```yaml
condition_gate: FAIL
median_IMPACT: 9
median_margin: 1
sample_passes: 1/3
```

Human bounded interpretation：

```text
PUSH_LIKE_PRIOR_DOMINANT_IN_CURRENT_CAL004_SETUP_WITH_PARTIAL_TEXT_ONLY_IMPACT_SIGNAL_AND_UNRESOLVED_REFERENCE_COMMAND_ROUTE_CAUSATION
```

### 2.3 CAL-005 R1

```yaml
experiment: CAL-005
program: TEXT_ONLY_IMPACT_SIGNAL_REPLICATION_V1
round_closed: true
human_final_decision_complete: true
condition_analysis_complete: true
mapping_revealed_under_governed_unblinding: true
formal_outcome: CAL005_R1_TEXT_ONLY_IMPACT_SIGNAL_NOT_CONDITION_GATE_REPLICATED
```

N0R：

```yaml
condition_gate: FAIL
median_PUSH: 4
median_IMPACT: 0
median_margin: -4
sample_passes: 0/3
```

I0R：

```yaml
condition_gate: FAIL
median_PUSH: 9
median_IMPACT: 7
median_margin: -3
sample_passes: 0/3
```

Primary contrast `I0R versus N0R`：

```yaml
median_IMPACT_delta: 7
median_PUSH_delta: 5
median_margin_delta: 1
sample_pass_delta: 0
directional_partial_signal: false
```

I0R-01 是 near-threshold individual sample，不得覆盖 condition-level Gate。

## 3. Cross-experiment synthesis

Formal synthesis：

```text
CURRENT_CAL003_CAL004_CAL005_EVIDENCE_SUPPORTS_REPEATABLE_PUSH_LIKE_DIFFERENTIATION_BUT_NOT_IMPACT_SPECIFIC_CONDITION_LEVEL_REPLICATION
```

Bounded interpretation：

```text
PUSH_LIKE_SIGNATURES_WERE_MORE_REPEATABLE_THAN_IMPACT_SPECIFIC_SIGNATURES_ACROSS_THE_CURRENT_CAL003_CAL004_CAL005_SETUPS_WHILE_THE_UNIQUE_CAUSE_REMAINS_UNRESOLVED_AND_NO_PROVIDER_WIDE_BIAS_OR_UNIVERSAL_PROMPT_CAUSALITY_IS_CLAIMED
```

结论边界：

- 不代表 Provider-wide；
- 不代表 model-version universal；
- 不代表 scene/actor independent；
- 不代表 Prompt-universal；
- 没有统计显著性声明；
- 不证明 IMPACT generation 不可能；
- unique cause 未识别。

## 4. Source 分类状态

### 4.1 Stable governance candidates 已进入本次人工更新包

```text
S01 Gate precedence
S02 Cross-experiment replication before stable production promotion
S03 Setup-bounded interpretation
```

这些规则写入 Validator/Governance V0.2；只有用户手动应用后才成为 active Project Source。

### 4.2 Provisional experimental findings

```text
P01 当前 CAL-003 至 CAL-005 中 PUSH-like differentiation 更可重复
P02 ACTION_REF_PUSH_02 在 CAL-003 内有正向 repeatability evidence，但非 production-stable
P03 当前 IMPACT reference 与 text-only IMPACT-hard recipes 缺少 condition-level replication
```

保存在 `动作家族校准实验综合与生产边界_V0.1`，不得直接提升到 Prompt Compiler 或生产规则。

### 4.3 Not Source

以下仅保留在 repository evidence：

- alias → task mapping；
- sealed identities / commitment / salt-related identities；
- submit ID / signed URL；
- exact per-alias score；
- temporary helper 与 untracked inventory；
- 单次执行的内部 parser correction。

## 5. CAL-005 sealed / unblind 历史状态

```yaml
controlled_unblinding_complete: true
original_attempt_sealed_open_count: 1
recovery_attempt_sealed_open_count: 1
historical_cumulative_sealed_open_count: 2
current_unblind_authority: false
salt_persisted: false
raw_mapping_persisted: false
raw_equivalence_persisted: false
```

累计数是历史受控执行证据，不授权第三次打开，也不应作为 stable Source 规律。

## 6. 主作品生产线

《赤焰对天穹》当前：

```text
paused_for_calibration_synthesis_and_source_decision
```

恢复前必须：

1. 完成人工 Project Source 应用与验收；
2. 做 read-only production-context recovery；
3. 由人类决定是否回到生产、继续动作实验或保持暂停；
4. 若需 Provider live work，重新取得有效 access，并进行 fresh runtime verification 与 fresh human authorization。

当前没有 production re-entry authority。

## 7. 即梦订阅与 CLI（Rolling-only / human-reported）

```yaml
dreamina_auto_renewal_cancelled: true
paid_cli_access_expected_end: 2026-07-30T20:00:00+08:00
fact_source: HUMAN_REPORTED
provider_verified: false
```

- CLI 安装及本地治理资料可以继续保留；
- 订阅到期不要求删除 Dreamina CLI Source；
- 当前没有 live experiment 需要 CLI；
- 到期后的真实 access 状态不得猜测；未来使用前必须重新验证；
- 新订阅、有效 access 或剩余积分本身都不产生 submit authority。

## 8. CAL-002 / CAL-001

- CAL-002 Route A C02 已关闭；C03 未授权；原 R02 仍 blocked。
- CAL-002 action-family 结论继续受 Gate、replication 和 provisional/stable 边界约束。
- CAL-001 保持 `STOPPED_AUTHORITY_CLOSED`，不自动进入后续 fixed task。

## 9. 当前人工动作

```text
1. 审阅并手动应用 Source Update Pack
2. 核验 Project Source 文件清单与版本
3. 确认旧 V1.14 / V0.2 / Validator V0.1 已被替换
4. 确认新 provisional synthesis 已加入
5. 再决定 production-context recovery、继续暂停或新实验设计
```

不得自动创建 CAL-006。

## 10. 当前证据锚点

```yaml
CAL003_decision_path: experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_HUMAN_FINAL_DECISION_V0_1/human_final_decision.json
CAL003_decision_git_blob: b428c968b500e822e6f1a740aa01c222e82477fa
CAL004_decision_path: experiments/CAL-004/IMPACT_FAMILY_CAUSAL_ISOLATION_V1/R1_HUMAN_FINAL_DECISION_V0_1/human_final_decision.json
CAL004_decision_git_blob: 0b4eada2543b7cd08d02d44b344fac78c52a7445
CAL005_decision_path: experiments/CAL-005/TEXT_ONLY_IMPACT_SIGNAL_REPLICATION_V1/R1_HUMAN_FINAL_DECISION_V0_1/human_final_decision.json
CAL005_decision_git_blob: 7335e80ae7e1639cd685d188491dbd2d5b9fdc77
synthesis_commit: 2dfd67e6b6318133c0b342ebc99edb2dd32921c3
synthesis_report: reports/CAL003_CAL004_CAL005_CROSS_EXPERIMENT_SYNTHESIS_AND_SOURCE_UPDATE_EVIDENCE_PACK.md
```
