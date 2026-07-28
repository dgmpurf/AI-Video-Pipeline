# CAL-004 R1 Controlled Unblinding And Condition Analysis Result

## 1. Decision

- Goal: `CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_R1_CONTROLLED_UNBLINDING_AND_CONDITION_ANALYSIS_V0_1`
- Starting checkpoint: `194809d01825e2a3408f0dcda4d21ac44a5dfa4a`
- Decision: `CAL004_R1_CONTROLLED_UNBLINDING_AND_CONDITION_ANALYSIS_COMPLETE`
- Proposed outcome: `PROVIDER_OR_SCENE_PUSH_PRIOR_DOMINANT`
- Outcome status: `PROPOSED_PENDING_FRESH_HUMAN_FINAL_DECISION`
- Automatic decision / expansion: `false / false`
- Fresh human final decision required: `true`

## 2. Authorization And Preactivation

- Canonical authorization: `2404` bytes, SHA-256 `51de25465a9fd9a637516e6999a6cc4dca1cce1e3f33b1534126bfb56c1b3dc8`, Base64 `3208` characters
- Direct human recovery authorization: `1228` bytes, SHA-256 `ddb78d721fed479e347000b4616d1898d0850b22f6e51309a3372eacc25aa469`, one-time non-reusable
- Accepted prior failures: blanket postwrite member-name rejection and prewrite raw-occurrence undercount; all prior partial outputs were cleaned
- Review-freeze ZIP validation: `PASS`; opens `1`; 21 members; CRC `PASS`; SHA256SUMS `20/20 PASS`
- Frozen review coverage and byte identity: `18/18 PASS`
- Global frozen material-sentinel count: `3`
- Producer schema source: same-chat archived creator implementation, SHA-256 `ab6a5adf184ee5a9ed0383bf7fc037b0acf6987d361266f0f5bd843f4a20342f`
- Preactivation schema correction: the immutable producer mapping has 16 fields; public persistence remains the authorized 13-field projection plus batch assignment
- Synthetic tests: `12/12 PASS`
- Structured in-memory sensitive-data validation before writing: `PASS`

## 3. Sealed Package

- Sealed ZIP opens: `1`
- Each exact member read count: `1`
- Order / CRC / SHA256SUMS: `PASS / PASS / 5/5 PASS`
- Salt syntax: `PASS` (value not disclosed or persisted)
- Mapping / equivalence / batch-assignment coverage: `18/18 / 18/18 / 18/18`
- Four-way commitment equality: `PASS`
- Raw equivalence, sealed bytes and framemd5 values persisted: `false`

## 4. Verified Mapping

| Alias | Task | Condition | Prompt | Reference | Replicate | Route |
|---|---|---|---|---|---:|---|
| B01 | IP-03 | IP | I | P | 3 | multimodal2video |
| B02 | NI-02 | NI | N | I | 2 | multimodal2video |
| B03 | II-03 | II | I | I | 3 | multimodal2video |
| B04 | I0-01 | I0 | I | 0 | 1 | text2video |
| B05 | NP-01 | NP | N | P | 1 | multimodal2video |
| B06 | II-02 | II | I | I | 2 | multimodal2video |
| B07 | NI-03 | NI | N | I | 3 | multimodal2video |
| B08 | N0-03 | N0 | N | 0 | 3 | text2video |
| B09 | I0-03 | I0 | I | 0 | 3 | text2video |
| B10 | II-01 | II | I | I | 1 | multimodal2video |
| B11 | NI-01 | NI | N | I | 1 | multimodal2video |
| B12 | NP-03 | NP | N | P | 3 | multimodal2video |
| B13 | IP-01 | IP | I | P | 1 | multimodal2video |
| B14 | N0-02 | N0 | N | 0 | 2 | text2video |
| B15 | N0-01 | N0 | N | 0 | 1 | text2video |
| B16 | I0-02 | I0 | I | 0 | 2 | text2video |
| B17 | NP-02 | NP | N | P | 2 | multimodal2video |
| B18 | IP-02 | IP | I | P | 2 | multimodal2video |

## 5. Frozen Sample Scores And Gates

| Alias | Task | Condition | Rep | PUSH | IMPACT | Margin | Sentinel | Ref applicable | Gate |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| B01 | IP-03 | IP | 3 | 11 | 4 | -7 | 1 | true | FAIL |
| B02 | NI-02 | NI | 2 | 8 | 10 | 2 | 0 | true | FAIL |
| B03 | II-03 | II | 3 | 10 | 5 | -5 | 1 | true | FAIL |
| B04 | I0-01 | I0 | 1 | 8 | 9 | 1 | 0 | false | FAIL |
| B05 | NP-01 | NP | 1 | 11 | 4 | -7 | 0 | true | FAIL |
| B06 | II-02 | II | 2 | 6 | 4 | -2 | 0 | true | FAIL |
| B07 | NI-03 | NI | 3 | 10 | 6 | -4 | 0 | true | FAIL |
| B08 | N0-03 | N0 | 3 | 3 | 8 | 5 | 0 | false | FAIL |
| B09 | I0-03 | I0 | 3 | 6 | 11 | 5 | 0 | false | PASS |
| B10 | II-01 | II | 1 | 11 | 6 | -5 | 1 | true | FAIL |
| B11 | NI-01 | NI | 1 | 10 | 6 | -4 | 0 | true | FAIL |
| B12 | NP-03 | NP | 3 | 12 | 5 | -7 | 0 | true | FAIL |
| B13 | IP-01 | IP | 1 | 3 | 2 | -1 | 0 | true | FAIL |
| B14 | N0-02 | N0 | 2 | 6 | 5 | -1 | 0 | false | FAIL |
| B15 | N0-01 | N0 | 1 | 9 | 5 | -4 | 0 | false | FAIL |
| B16 | I0-02 | I0 | 2 | 6 | 7 | 1 | 0 | false | FAIL |
| B17 | NP-02 | NP | 2 | 11 | 4 | -7 | 0 | true | FAIL |
| B18 | IP-02 | IP | 2 | 10 | 5 | -5 | 0 | true | FAIL |

No-reference conditions preserve frozen reference observations but apply the authorized effective-false rule for Gate arithmetic.

## 6. Condition Gates

| Condition | PUSH values / median | IMPACT values / median | Margin values / median | Sample PASS | Sentinels | Gate |
|---|---|---|---|---:|---|---|
| N0 | [9, 6, 3] / 6 | [5, 5, 8] / 5 | [-4, -1, 5] / -1 | 0/3 | [0, 0, 0] | FAIL |
| NI | [10, 8, 10] / 10 | [6, 10, 6] / 6 | [-4, 2, -4] / -4 | 0/3 | [0, 0, 0] | FAIL |
| NP | [11, 11, 12] / 11 | [4, 4, 5] / 4 | [-7, -7, -7] / -7 | 0/3 | [0, 0, 0] | FAIL |
| I0 | [8, 6, 6] / 6 | [9, 7, 11] / 9 | [1, 1, 5] / 1 | 1/3 | [0, 0, 0] | FAIL |
| II | [11, 6, 10] / 10 | [6, 4, 5] / 5 | [-5, -2, -5] / -5 | 0/3 | [1, 0, 1] | FAIL |
| IP | [3, 10, 11] / 10 | [2, 5, 4] / 4 | [-1, -5, -7] / -5 | 0/3 | [0, 0, 1] | FAIL |

All six conditions retain exactly three replicates. Governed rights and provenance validation is `PASS`.

## 7. Pre-Registered Contrasts

| ID | Comparison | Classification | IMPACT delta | PUSH delta | Margin delta | PASS delta | Gate pair |
|---|---|---|---:|---:|---:|---:|---|
| C01 | NI versus NP | PRIMARY_WITHIN_COMMAND_CONTRAST | 2 | -1 | 3 | 0 | FAIL / FAIL |
| C02 | II versus IP | PRIMARY_WITHIN_COMMAND_CONTRAST | 1 | 0 | 0 | 0 | FAIL / FAIL |
| C03 | I0 versus N0 | PRIMARY_WITHIN_COMMAND_CONTRAST | 4 | 0 | 2 | 1 | FAIL / FAIL |
| C04 | II versus I0 | REFERENCE_PLUS_COMMAND_ROUTE_BUNDLE_CONTRAST | -4 | 4 | -6 | -1 | FAIL / FAIL |
| C05 | IP versus I0 | REFERENCE_PLUS_COMMAND_ROUTE_BUNDLE_CONTRAST | -5 | 4 | -6 | -1 | FAIL / FAIL |
| C06 | NI versus N0 | REFERENCE_PLUS_COMMAND_ROUTE_BUNDLE_CONTRAST | 1 | 4 | -3 | 0 | FAIL / FAIL |
| C07 | NP versus N0 | REFERENCE_PLUS_COMMAND_ROUTE_BUNDLE_CONTRAST | -1 | 5 | -6 | 0 | FAIL / FAIL |
| C08 | II versus NI | PRIMARY_WITHIN_COMMAND_CONTRAST | -1 | 0 | -1 | 0 | FAIL / FAIL |

`C04-C07` change both reference presence/family and command route. They are descriptive route bundles, not pure reference causal effects. No statistical-significance or generalized Provider-reliability claim is made from three replicates.

## 8. Outcome Patterns

- Reference pair neutral: `false`
- Reference pair IMPACT text: `false`
- Text pair no reference: `false`
- Text pair IMPACT reference: `false`
- PUSH-reference override pattern: `false`
- Conservative precedence branch: `6`
- Proposed outcome: `PROVIDER_OR_SCENE_PUSH_PRIOR_DOMINANT`

## 9. Boundaries

- Frozen review edits / semantic re-review / rescoring: `0 / false / false`
- Dreamina / Provider / credit operations: `0 / 0 / 0`
- Submit / query / download / retry / resubmit: `0 / 0 / 0 / 0 / 0`
- Media operations / randomness / Source changes: `0 / 0 / 0`
- Salt disclosed or persisted: `false`
- Raw equivalence disclosed or persisted: `false`
- `production_approved=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

## 10. Repository Scope

- New paths: exactly `15`
- Modified / deleted / renamed existing paths: `0 / 0 / 0`
- Unexpected paths: `0`
- Evidence manifest binds the other fourteen new outputs and all required committed and external inputs.

## 11. Next Phase

`CAL004_R1_UNBLINDED_CONDITION_RESULT_AND_HUMAN_FINAL_DECISION`
