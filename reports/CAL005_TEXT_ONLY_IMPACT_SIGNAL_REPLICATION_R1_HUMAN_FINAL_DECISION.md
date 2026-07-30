# CAL005 Text-Only Impact Signal Replication R1 Human Final Decision

## 1. Human Final Decision

CAL-005 R1 is closed. The human final decision is complete. No new live experiment is authorized, no Source promotion is authorized, and the main production line remains paused.

## 2. Accepted Formal Outcome

`CAL005_R1_TEXT_ONLY_IMPACT_SIGNAL_NOT_CONDITION_GATE_REPLICATED`

## 3. Human Bounded Interpretation

`CAL005_R1_TEXT_ONLY_IMPACT_HARD_PROMPT_INCREASED_BOTH_IMPACT_AND_PUSH_SIGNATURES_BUT_DID_NOT_REPLICATE_AN_IMPACT_SPECIFIC_CONDITION_LEVEL_SIGNAL_IN_THE_CURRENT_TEXT2VIDEO_NO_REFERENCE_SETUP`

在当前 text2video、无图像/视频/音频参考、每个条件仅三次重复的 CAL-005 设置中，IMPACT-hard Prompt 提高了部分 IMPACT 表现，但也显著提高了 PUSH 表现，未形成通过预注册 condition gate 的 IMPACT 特异性复现信号。

## 4. Accepted N0R Evidence

- Condition Gate: `FAIL`
- PUSH values and median: `[6, 1, 4]`, median `4`
- IMPACT values and median: `[0, 5, 0]`, median `0`
- Margins and median: `[-6, 4, -4]`, median `-4`
- Sample passes: `0/3`

## 5. Accepted I0R Evidence

- Condition Gate: `FAIL`
- PUSH values and median: `[1, 9, 10]`, median `9`
- IMPACT values and median: `[7, 1, 7]`, median `7`
- Margins and median: `[6, -8, -3]`, median `-3`
- Sample passes: `0/3`

## 6. Primary Contrast

`CAL005-C01` compares I0R with N0R and remains a `PRIMARY_WITHIN_COMMAND_CONTRAST`.

- Median IMPACT delta: `+7`
- Median PUSH delta: `+5`
- Median specificity-margin delta: `+1`
- Sample-pass-count delta: `0`
- Condition Gate pair: `I0R FAIL / N0R FAIL`
- Directional partial signal: `false`

## 7. Why the Higher I0R IMPACT Median Is Not Replication Success

The IMPACT-hard Prompt raised the median IMPACT signature, but it also raised the median PUSH signature substantially. The median specificity margin remained negative, all six sample Gates failed, and both condition Gates failed. The result therefore does not establish an IMPACT-specific condition-level replicated signal.

## 8. I0R-01 Near-Threshold Sample Limitation

I0R-01 recorded PUSH `1`, IMPACT `7`, and margin `6`. It remained a sample-Gate `FAIL` because the IMPACT score did not reach `8`. This individual observation does not override the condition result and is not promoted to a replicated signal, stable Prompt rule, or universal causal result.

## 9. Causal and Statistical Limitations

The evidence is limited to the current committed CAL-005 setup, the text2video route, no active reference, the committed model/run design, three replicates per condition, and the frozen PUSH/IMPACT signature framework. No statistical significance, causal certainty, Provider-wide reliability, universal Prompt causality, or production readiness is claimed.

## 10. Round Closure

- `CAL005_R1_human_final_decision_complete = true`
- `CAL005_R1_round_closed = true`
- `automatic_expansion = false`
- `future_live_experiment_requires_fresh_human_design_and_authorization = true`
- `future_source_promotion_requires_separate_source_synthesis_and_human_manual_application = true`
- `main_production_line_remains_paused = true`

## 11. Authority Boundary

- Next live experiment authorized: `false`
- Source promotion authorized: `false`
- Production re-entry authorized: `false`
- Production approved: `false`
- Fixed task completion: `false`
- Final master: `false`
- Locked: `false`

This record does not define CAL-006 and does not reopen CAL-003 or CAL-004.

## 12. Git and Output Evidence

This record-only phase creates exactly four governed paths. The self-excluded evidence manifest binds all eleven committed inputs and the three nonself outputs. The authorized commit message is `close(cal005): record R1 human final decision`.

No sealed ZIP, MP4, diagnostic media, Dreamina state, Provider state, or Project Source was accessed or changed.

## 13. Next Recommended Phase

`CAL005_R1_CLOSED_ROLLING_STATE_UPDATE_AND_CAL003_CAL004_CAL005_SYNTHESIS_HUMAN_DECISION`
