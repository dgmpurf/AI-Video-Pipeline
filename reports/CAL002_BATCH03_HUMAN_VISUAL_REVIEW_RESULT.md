# CAL002 Batch03 Human Visual Review Result

## Phase Summary

- Phase: `CAL002_BATCH03_HUMAN_VISUAL_REVIEW_AND_RULE_UPDATE_NO_LIVE`
- Repository checkpoint: `4452195509812c1a56fb14728b5ac4a4ac873065`
- Batch: `CAL002-ACTION-CALIBRATION-BATCH03-ACTION-CAUSALITY-V1`
- Review source: human-supplied full-video visual findings
- Review scope: A01 and A04 Control/Candidate comparisons
- Decision: `GENERIC_APPENDED_ACTION_CAUSALITY_LAYER_NOT_SUPPORTED`
- Confidence: `MEDIUM`
- Official Source status: `false`
- Production approved: `false`
- `final_master`: `false`
- `locked`: `false`

This report records the supplied human visual review. It does not perform a new media review, create or modify media, call a provider, or create execution authority.

## Bound Evidence

| Evidence | Bytes | SHA-256 |
| --- | ---: | --- |
| `reports/CAL002_BATCH03_DOWNLOAD_EXECUTION_RESULT.md` | 6186 | `a465a4a445f1c01a2ddb1b26b5bf04ba46b52f7703810e8a4c5e65b6044034b9` |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH03_EXECUTION/execution_records/CAL002-BATCH03-LIVE-39934EE/review/CAL002_BATCH03_HUMAN_VISUAL_REVIEW_HANDOFF.md` | 3971 | `8ed49be984138eef40ec61dcbe9a83f2c53dd4fb4e66c07caa3ba6e7d7e604c7` |

| Reviewed output | SHA-256 |
| --- | --- |
| A01 Control | `18ef49f87e8304a283b18c1edb649a1ae74011dd633fafa8a50ba9a8355b1caa` |
| A01 Candidate | `e7e15b933b7c22331938fe413ac19af2fce13249442065da1269a5bae9e7a573` |
| A04 Control | `b47eaf84b0f2019f779cf6a59e6616c8985b8ab57cbd87fcec725bbc9d5967f2` |
| A04 Candidate | `d5cde476d59bf753b1802464fd9fcb8d73dcc46174284bbbe8540b279abfee2c` |

All bound byte lengths and hashes were independently verified before this report was created.

## Scoring Rubric

Each dimension uses a five-point scale:

- `1`: absent, unreadable, or severely unstable
- `2`: weak
- `3`: partial but readable
- `4`: clear
- `5`: strong and unambiguous

For `identity/camera/fixed-variable stability`, a higher score means less drift. These scores encode only the supplied human observations and are not statistical model-quality estimates.

## Review Scores

| Output | Initiation | Contact timing | Post-contact consequence | Body response | Recovery / stabilization | Identity / camera / fixed-variable stability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A01 Control | 4 | 4 | 2 | 2 | 3 | 2 |
| A01 Candidate | 3 | 4 | 1 | 1 | 2 | 2 |
| A04 Control | 4 | 4 | 3 | 3 | 3 | 2 |
| A04 Candidate | 1 | 1 | 1 | 1 | 1 | 2 |

The shared stability scores reflect the supplied cross-pair finding that costume, scene, and framing drift limits causal attribution. The evidence does not support assigning a more precise per-output drift difference.

## A01 Push Review

### A01 Control

- Approach and action initiation are clear.
- Visible upper-torso contact occurs around `0.75-1.00s`.
- Contact is prolonged while torso response remains weak.
- A delayed but readable foot adjustment occurs around `3.50-4.00s`.
- The sequence shows partial causal progression but weak force transfer.

### A01 Candidate

- Contact is established around `0.75-1.00s`.
- Contact remains prolonged and largely static.
- Only a small, late foot adjustment is visible.
- Torso yield and backward displacement are not clearer than Control.
- No reliable visible gain over Control is established.

### A01 Pair Decision

`NO_CLEAR_CAUSALITY_GAIN_CONTROL_SLIGHTLY_BETTER`

The generic appended Action Causality Layer did not produce a clear A01 improvement. Control is slightly better in the supplied full-video judgment, but the difference remains narrow and subject to generation variance.

## A04 Impact Review

### A04 Control

- Initiation and forward lunge are clear.
- Visible contact occurs around `1.00-1.25s`.
- Receiver body and foot response follow contact.
- Partial recovery and stabilization are readable.
- The action reads partly as a sustained push rather than a brief impact.
- Causal progression nevertheless remains visibly readable.

### A04 Candidate

- The first frame already contains contact.
- No readable initiation or moment of contact is present.
- The attacker mainly withdraws the arm.
- The receiver remains essentially stationary.
- No visible consequence, backward response, or recovery chain is established.

### A04 Pair Decision

`CAUSALITY_CANDIDATE_REGRESSION_CONTROL_CLEARLY_BETTER`

The A04 Candidate regressed substantially. The generic suffix did not preserve the readable causal sequence present in Control.

## Cross-Pair Assessment

- The generic appended Action Causality Layer did not create a consistent gain.
- A01 produced no clear improvement.
- A04 Candidate regressed substantially.
- Costume, scene, and framing drift limit clean causal attribution.
- One sample per treatment is insufficient for a broad model rule.
- This result does not disprove action-specific causality wording.
- Generic meta-instructions must be distinguished from concrete, result-first causal syntax.

## Prompt Structure Effect

The Batch02 conclusion remains provisional: structured organization can improve readability. Batch03 does not overturn that finding.

Batch03 instead shows that appending abstract causality reminders to an already structured prompt is not reliably sufficient. Labels and meta-instructions do not themselves compile a visible physical sequence. The next design should test action-specific, result-first causal clauses as a separate variable.

## Decision

- Decision: `GENERIC_APPENDED_ACTION_CAUSALITY_LAYER_NOT_SUPPORTED`
- Confidence: `MEDIUM`
- Supported narrow claim: the tested generic appended causality suffix did not provide a consistent visible gain across these two single-sample pairs.
- Unsupported broad claim: action-specific causal prompting never works.
- Human visual review completed: `true`
- Production approval granted: `false`

## Limitations

- Each treatment has only one generated sample.
- Generated costume, scene, and framing variables drifted.
- Pairwise differences may include generation variance.
- The experiment tested a generic appended meta-instruction, not a fully compiled action-specific causality beat.
- No conclusion should be generalized to all actions, prompts, or Seedance outputs.

## Governance And Non-Actions

- Dreamina called: `false`
- Provider called: `false`
- Submit called: `false`
- Query called: `false`
- Download called: `false`
- Retry or resubmit called: `false`
- Media created or modified: `false`
- Batch01 modified: `false`
- Batch02 modified: `false`
- Batch03 package or design modified: `false`
- CAL-001 modified: `false`
- Official Source modified: `false`
- Official Source status: `false`
- Execution authority created: `false`
- `final_master`: `false`
- `locked`: `false`

## Recommended Next Design Only

`CAL002_BATCH04_RESULT_FIRST_ACTION_CAUSALITY_DESIGN_NO_LIVE`

No Batch04 design files are created by this phase.

## Final Verdict

`CAL002_BATCH03_HUMAN_VISUAL_REVIEW_RECORDED_GENERIC_CAUSALITY_SUFFIX_NOT_SUPPORTED`
