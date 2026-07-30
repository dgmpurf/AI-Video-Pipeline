# CAL-003 / CAL-004 / CAL-005 Cross-Experiment Synthesis and Source Update Evidence Pack

## 1. Decision

Decision:
`CAL003_CAL004_CAL005_SYNTHESIS_COMPLETE_SOURCE_UPDATE_EVIDENCE_PACK_READY_FOR_CHATGPT_AND_HUMAN_REVIEW`

The three R1 rounds are closed. Their combined evidence supports a bounded
project-level synthesis, three stable Source governance candidates, and three
provisional experimental findings. It does not support a production recipe,
a unique-cause finding, or a live follow-on experiment.

No Official Source was modified or applied. The evidence pack is prepared for
ChatGPT synthesis and human manual application. No live experiment, production
re-entry or CAL-006 is authorized.

## 2. Repository and Evidence Anchors

- Starting repository HEAD: `24f6e6e30832c0473a4ef01bf11ebd7197fb6b1a`
- Starting `origin/main`: `24f6e6e30832c0473a4ef01bf11ebd7197fb6b1a`
- CAL-003 decision Git blob: `b428c968b500e822e6f1a740aa01c222e82477fa`
- CAL-004 decision Git blob: `0b4eada2543b7cd08d02d44b344fac78c52a7445`
- CAL-005 decision Git blob: `7335e80ae7e1639cd685d188491dbd2d5b9fdc77`
- All three decision worktree files equal their committed HEAD blobs.
- Canonical authorization: 2256 UTF-8 bytes, SHA-256
  `5c7abde065d499491e1fb6725482a5b11bd377579f2bc71d4f04b59bd03ca833`,
  Base64 length 3008, exact one-decode round trip PASS.

## 3. CAL-003 Accepted Result

CAL-003 `REFERENCE_CONTROL_REPEATABILITY_V1` R1 is closed.

| Evidence | Result |
|---|---:|
| PUSH family Gate | PASS |
| PUSH sample passes | 3/3 |
| PUSH median own score | 12 |
| PUSH median margin | 8 |
| IMPACT family Gate | FAIL |
| IMPACT sample passes | 0/3 |
| IMPACT median own score | 6 |
| IMPACT median margin | -6 |
| Ordinal-pair aggregate Gate | FAIL |
| Passing ordinal pairs | 0/3 |

Accepted bounded reading: the PUSH reference produced repeatable PUSH-like
differentiation; the IMPACT reference did not produce IMPACT-specific
differentiation; the six outputs showed asymmetric collapse toward PUSH-like
behavior. CAL-003 alone does not establish a universal Provider bias or a
stable production rule.

## 4. CAL-004 Accepted Result

CAL-004 `IMPACT_FAMILY_CAUSAL_ISOLATION_V1` R1 is closed.

- Condition Gates: `0/6 PASS`
- Sample Gates: `1/18 PASS`
- Conditions with negative median specificity margin: `5/6`
- I0: Gate `FAIL`, median IMPACT `9`, median margin `1`, samples `1/3 PASS`
- C03 I0 versus N0: IMPACT `+4`, PUSH `0`, margin `+2`, sample passes `+1`,
  Gate pair `FAIL / FAIL`

The accepted interpretation is
`PUSH_LIKE_PRIOR_DOMINANT_IN_CURRENT_CAL004_SETUP_WITH_PARTIAL_TEXT_ONLY_IMPACT_SIGNAL_AND_UNRESOLVED_REFERENCE_COMMAND_ROUTE_CAUSATION`.
The partial I0 signal does not override its failed condition Gate, and the
negative results do not identify one unique cause.

## 5. CAL-005 Accepted Result

CAL-005 `TEXT_ONLY_IMPACT_SIGNAL_REPLICATION_V1` R1 is closed.

| Condition | Gate | Median PUSH | Median IMPACT | Median margin | Passes |
|---|---|---:|---:|---:|---:|
| N0R | FAIL | 4 | 0 | -4 | 0/3 |
| I0R | FAIL | 9 | 7 | -3 | 0/3 |

CAL005-C01, I0R versus N0R, produced deltas of IMPACT `+7`, PUSH `+5`,
margin `+1`, and sample passes `0`; the Gate pair remained `FAIL / FAIL`.
The formal outcome is
`CAL005_R1_TEXT_ONLY_IMPACT_SIGNAL_NOT_CONDITION_GATE_REPLICATED`, and
`directional_partial_signal=false`. I0R-01 is only a near-threshold individual
sample, not a replicated condition result.

## 6. Cross-Experiment Synthesis

Formal synthesis label:

`CURRENT_CAL003_CAL004_CAL005_EVIDENCE_SUPPORTS_REPEATABLE_PUSH_LIKE_DIFFERENTIATION_BUT_NOT_IMPACT_SPECIFIC_CONDITION_LEVEL_REPLICATION`

Human bounded interpretation:

`PUSH_LIKE_SIGNATURES_WERE_MORE_REPEATABLE_THAN_IMPACT_SPECIFIC_SIGNATURES_ACROSS_THE_CURRENT_CAL003_CAL004_CAL005_SETUPS_WHILE_THE_UNIQUE_CAUSE_REMAINS_UNRESOLVED_AND_NO_PROVIDER_WIDE_BIAS_OR_UNIVERSAL_PROMPT_CAUSALITY_IS_CLAIMED`

中文解释：在当前 CAL-003、CAL-004 和 CAL-005 的受控设置中，PUSH-like
特征比 IMPACT-specific 特征表现得更可重复；但现有证据不能把原因唯一归结为
Provider、Prompt、参考视频、场景或演员先验，也不能形成 Provider 范围的普遍
偏置结论。

`unique_cause_identified=false`.

Unresolved candidates remain Provider/model behavior, Prompt wording and
action decomposition, reference content and motion quality, command route and
reference conditioning, scene and actor prior, review-framework sensitivity,
and small replicate count. The evidence does not rank them.

## 7. Direct Evidence Versus Bounded Inference

Direct evidence is limited to the committed Gate results, scores, deltas,
closure states and authority boundaries of each experiment. The cross-
experiment statement that PUSH-like signatures were more repeatable is an
explicit `BOUNDED_CROSS_EXPERIMENT_INFERENCE`, not a directly observed
Provider-wide fact.

Required limitations:

- not Provider-wide
- not model-version universal
- not scene-independent
- not actor-independent
- not Prompt-universal
- not statistical significance
- not proof that IMPACT generation is impossible

## 8. Source-Promotion Matrix

| Class | Count | IDs |
|---|---:|---|
| Stable Source candidate | 3 | S01, S02, S03 |
| Provisional experimental rule | 3 | P01, P02, P03 |
| Rolling-only fact | 8 | R01-R08 |
| Not Source | 7 | N01-N07 |
| Rejected overclaim | 6 | O01-O06 |

Every stable or provisional row has `official_application=false`. Human manual
application is required. Exact row support, limitations, destinations and
forbidden promotions are recorded in `source_promotion_matrix.json`.

## 9. Stable Source Candidates

S01, Gate precedence: a favorable sample, median uplift or directional delta
cannot override a failed pre-registered family or condition Gate.

S02, replication requirement: an action-family Prompt, reference or route
must not become stable production guidance until it passes its own Gate and
replicates across bounded comparable experiments.

S03, bounded interpretation: action-family calibration conclusions remain
setup-bounded unless separate evidence supports Provider-wide, model-wide or
universal causality.

These are governance and evidence-rule candidates only. They are not Official
Source in this Goal.

## 10. Provisional Experimental Findings

P01: PUSH-like differentiation was more repeatable than IMPACT-specific
differentiation across the current CAL-003 through CAL-005 setups.

P02: `ACTION_REF_PUSH_02` has positive repeatability evidence inside CAL-003,
but is not production-stable and does not authorize production use.

P03: the current IMPACT reference and text-only IMPACT-hard recipes lack
condition-level replication evidence sufficient for stable promotion.

All three remain provisional and setup-bounded.

## 11. Rolling-Only Facts

Rolling-only material includes the current repository checkpoint; the three
round-closure states; exact experiment outcomes and metrics; current phase;
all authority values; the paused production line; exact decision/report/blob
identities; and the human-reported subscription status.

Alias mappings, sealed-package identities, public commitments and salt-related
identities, submit IDs, signed URLs, per-alias scores, temporary helper paths,
and the current untracked workspace inventory are not Source.

## 12. Rejected Overclaims

The evidence explicitly rejects these claims:

1. The Provider is universally biased toward PUSH.
2. IMPACT generation is impossible.
3. The IMPACT-hard Prompt is universally ineffective.
4. ACTION_REF_PUSH_02 is production-approved.
5. CAL-003 alone proves a stable production rule.
6. A higher median IMPACT score alone proves replication.

## 13. Rolling Current State Replacement Evidence

Proposed replacement phase:
`CAL003_CAL004_CAL005_SYNTHESIS_COMPLETE_SOURCE_CANDIDATE_GENERATION_HUMAN_DECISION`.

The proposed capsule records all three rounds closed; Provider, submit, query,
download, retry, resubmit, batch, unblind and Codex Source-write authorities
false; production approval and re-entry false; final/fixed/lock false; and the
main production line `paused_for_calibration_synthesis_and_source_decision`.

Stale prior facts include HEAD `46bb02a...`, CAL-005 mapping/analysis/final-
decision incomplete flags, a current-total sealed-open count of zero, and the
controlled-unblinding phase. Historical attempt accounting must remain in its
phase evidence rather than being erased.

The local repository Source index is V1.12. It still points to old CAL-001
checkpoint `a838723b8824a1003b6abab220257d0e20fa31ad` and F07 pending state,
contains no CAL-003/CAL-004/CAL-005 current state, and has no separate Rolling
Current State file. Therefore repository Source differs from current evidence.
The active ChatGPT Project Source application state is
`UNKNOWN_REQUIRES_HUMAN_CONFIRMATION`.

## 14. Subscription and CLI Operational Status

The user reports:

- `dreamina_auto_renewal_cancelled=true`
- `paid_cli_access_expected_end=2026-07-30T20:00:00+08:00`
- source: `HUMAN_REPORTED`
- Provider verified: `false`
- classification: rolling-only volatile fact

CLI installation may remain after paid access ends. No current live experiment
requires CLI access. Any future live operation requires a new subscription or
valid access, fresh runtime verification, and fresh human authorization. This
Goal did not check the account.

## 15. Production Boundary

- Current IMPACT production recipe promoted: `false`
- `ACTION_REF_PUSH_02` production-approved: `false`
- Main production line: `paused_for_calibration_synthesis_and_source_decision`
- Production re-entry authorized: `false`
- Automatic CAL-006: `false`
- Fresh production-context recovery required before any production re-entry:
  `true`

## 16. Output and Git Evidence

The allowlist contains exactly six deterministic JSON files and this Markdown
report. `evidence_manifest.json` is self-excluded and binds all required
inputs plus the other six output identities. No existing file, Source file,
media file or sealed package is changed.

Authorized Git finalization is exactly one commit with message
`synthesize(cal): prepare CAL003-CAL005 source evidence`, followed by exactly
one `git push origin main`. The resulting commit and push identities are
reported in the terminal receipt rather than self-embedded in this report.

## 17. Next Phase

`CHATGPT_GENERATE_ROLLING_CURRENT_STATE_V0_3_AND_SOURCE_UPDATE_CANDIDATE_PACK_FOR_HUMAN_MANUAL_APPLICATION`

This Goal creates a Source Update Evidence Pack only. It does not modify or
apply Official Source. It does not authorize Dreamina access, CAL-006,
production re-entry, final master or lock.
