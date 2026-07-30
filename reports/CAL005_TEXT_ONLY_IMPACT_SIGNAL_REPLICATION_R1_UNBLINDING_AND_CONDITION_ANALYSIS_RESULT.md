# CAL005 R1 Controlled Unblinding Schema Recovery Result

## Decision

`CAL005_R1_CONTROLLED_UNBLINDING_SCHEMA_RECOVERY_COMPLETE`

The controlled unblinding analysis is complete and remains a proposed bounded result pending a fresh human final CAL-005 decision.

## Recovery Checkpoint

- Recovery starting HEAD: `557e1ca35e0239a1f72dfb3faa08f4b2b265baa6`
- Prior blocked commit: `557e1ca35e0239a1f72dfb3faa08f4b2b265baa6`
- Prior failure: `SEALED_MANIFEST_MEMBER_RECORD_CONTAINER`
- Existing blocked outputs verified byte-identical to HEAD: `7/7 PASS`
- Missing success outputs verified absent before activation: `7/7 PASS`

## Producer-Bound Schema Recovery

- Producer logical path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\_cal005_blind_package_v01_executor.py`
- Producer bytes: `76034`
- Producer SHA-256: `ad8700c9e3d87ceb3a7920645f5b3c4525cff9ca1f65ee47450e032d2555fb8d`
- Exact sealed manifest container: `member_bindings`.
- Exact member binding fields: `bytes`, `path`, `sha256`.
- Exact equivalence fields validated: `canonical_prefix_equal`, `duration_equal`, `stream_counts_equal`, `complete_decode.exit_code`, `audio_framemd5.equal`, `video_framemd5.equal`.
- Producer-shaped positive fixtures: `2/2 PASS`.
- Producer-shaped negative fixtures: `6/6 PASS`.
- Recovery post-activation parser correction count: `0`.

## Attempt Accounting

- Prior sealed opens/member reads: `1 / 6`.
- Recovery sealed opens/member reads: `1 / 6`.
- Cumulative sealed opens/member reads: `2 / 12`.
- Prior/recovery/cumulative pre-activation corrections: `3 / 2 / 5`.

## Integrity

- Review-freeze validation: `PASS`.
- Sealed member order / CRC / SHA256SUMS: `PASS / 6/6 PASS / 5/5 PASS`.
- Mapping / equivalence / batch-assignment coverage: `6/6 / 6/6 / 6/6`.
- Four-way commitment equality: `PASS`.
- Salt, raw mapping/equivalence, raw sealed bytes and framemd5 values persisted: `false / false / false / false`.

## Sanitized Mapping

| Alias | Task | Condition | Prompt | Replicate | Position | Route |
|---|---|---|---|---:|---:|---|
| B01 | I0R-02 | I0R | IMPACT_CAUSAL_HARD | 2 | 3 | text2video |
| B02 | I0R-01 | I0R | IMPACT_CAUSAL_HARD | 1 | 2 | text2video |
| B03 | N0R-01 | N0R | ACTION_NEUTRAL_MINIMAL | 1 | 1 | text2video |
| B04 | N0R-02 | N0R | ACTION_NEUTRAL_MINIMAL | 2 | 4 | text2video |
| B05 | N0R-03 | N0R | ACTION_NEUTRAL_MINIMAL | 3 | 5 | text2video |
| B06 | I0R-03 | I0R | IMPACT_CAUSAL_HARD | 3 | 6 | text2video |

## Sample Gates

| Task | Alias | PUSH | IMPACT | Margin | Gate | Failed predicates |
|---|---|---:|---:|---:|---|---|
| N0R-01 | B03 | 6 | 0 | -6 | FAIL | impact_score_at_least_8, impact_minus_push_margin_at_least_3, action_family_failure_false |
| N0R-02 | B04 | 1 | 5 | 4 | FAIL | impact_score_at_least_8, action_family_failure_false |
| N0R-03 | B05 | 4 | 0 | -4 | FAIL | impact_score_at_least_8, impact_minus_push_margin_at_least_3, action_family_failure_false |
| I0R-01 | B02 | 1 | 7 | 6 | FAIL | impact_score_at_least_8 |
| I0R-02 | B01 | 9 | 1 | -8 | FAIL | impact_score_at_least_8, impact_minus_push_margin_at_least_3 |
| I0R-03 | B06 | 10 | 7 | -3 | FAIL | impact_score_at_least_8, impact_minus_push_margin_at_least_3 |

## Condition Gates

| Condition | PUSH values / median | IMPACT values / median | Margins / median | Passes | Gate |
|---|---|---|---|---:|---|
| N0R | [6, 1, 4] / 4 | [0, 5, 0] / 0 | [-6, 4, -4] / -4 | 0/3 | FAIL |
| I0R | [1, 9, 10] / 9 | [7, 1, 7] / 7 | [6, -8, -3] / -3 | 0/3 | FAIL |

## Primary Contrast

- Contrast: `CAL005-C01`, I0R versus N0R.
- Classification: `PRIMARY_WITHIN_COMMAND_CONTRAST`.
- Median IMPACT / PUSH / margin deltas: `7 / 5 / 1`.
- Sample-pass delta: `0`.

## Proposed Outcome

`CAL005_R1_TEXT_ONLY_IMPACT_SIGNAL_NOT_CONDITION_GATE_REPLICATED`

- Directional partial signal: `false`.
- Automatic decision: `false`.
- Fresh human final decision required: `true`.
- Statistical significance and Provider-wide reliability claimed: `false / false`.

## Boundaries

- Dreamina / Provider / credits: `0 / 0 / 0`.
- Submit / query / download / retry / resubmit: `0 / 0 / 0 / 0 / 0`.
- Media operation / semantic rereview / rescoring / randomness: `0 / 0 / 0 / 0`.
- Source changes: `false`.
- production_approved / fixed_task_completion / final_master / locked: `false / false / false / false`.

## Git Scope

- Existing blocked records modified: `7`.
- Newly completed analysis records created: `7`.
- Total governed output paths: `14`.
- Commit message: `recover(cal005): complete R1 controlled unblinding analysis`.

## Next Phase

`CAL005_R1_UNBLINDED_CONDITION_RESULT_AND_HUMAN_FINAL_DECISION`
