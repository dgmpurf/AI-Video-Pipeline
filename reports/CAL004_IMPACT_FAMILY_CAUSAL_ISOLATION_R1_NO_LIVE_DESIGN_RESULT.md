# CAL-004 Impact-Family Causal Isolation R1 No-Live Design Result

## Result

- Experiment: `CAL-004`
- Program: `IMPACT_FAMILY_CAUSAL_ISOLATION_V1`
- Round: `R1`
- Status: `NO_LIVE_DESIGN_ONLY`
- Conditions: `6`
- Replicates per condition: `3`
- Planned tasks: `18`
- Live authority: `false`

## Scientific Question

Under the same actor, scene, camera, duration, model-planning profile and
technical output contract, how do action-text specificity and motion-reference
family independently affect IMPACT-versus-PUSH signature behavior?

## Factorial Matrix

| Condition | Prompt | Reference | Replicates |
|---|---|---|---:|
| N0 | ACTION_NEUTRAL_MINIMAL | none | 3 |
| NI | ACTION_NEUTRAL_MINIMAL | ACTION_REF_IMPACT_02 | 3 |
| NP | ACTION_NEUTRAL_MINIMAL | ACTION_REF_PUSH_02 | 3 |
| I0 | IMPACT_CAUSAL_HARD | none | 3 |
| II | IMPACT_CAUSAL_HARD | ACTION_REF_IMPACT_02 | 3 |
| IP | IMPACT_CAUSAL_HARD | ACTION_REF_PUSH_02 | 3 |

No-reference conditions bind zero local motion references. Reference
conditions bind exactly one governed motion reference.

## Prompt Bindings

- `ACTION_NEUTRAL_MINIMAL`: 1978 bytes,
  `c15f93ee8ee55fccb827cbea8683c0538e13cefd138d0ae1a22761dce7c20ce0`
- `IMPACT_CAUSAL_HARD`: 2287 bytes,
  `c38e8bb135d6d9f29d510c2fb059b8f4a9ce7948626c19f43f98ad564b8422a5`
- Shared common block: 1763 bytes,
  `ce155b5d30650e38a889efcf8f81e644dc7b682756b50545b9033ab3ba78454b`

The common fixed-variable block is byte-identical across both Prompt files and
contains no action-family directive. No Prompt is executed in this phase.

## Pre-Registered Order And Analysis

The fixed deterministic submission order contains 18 tasks. Every six-task
block contains each condition once, strata are interleaved, positions vary,
and no randomness was generated.

Eight contrasts are pre-registered: NI/NP, II/IP, I0/N0, II/I0, IP/I0,
NI/N0, NP/N0, and II/NI. Future complete-MP4 review must be blinded; all 18
records must freeze before controlled mapping reveal. No permutation or salt
was created.

## Historical Budget Planning

- Human-reported balance on 2026-07-28: `2761` points
- Historical CAL-003 unit decrement: `140` points per video
- Planned 18-task decrement: `2520` points
- Historical arithmetic remainder: `241` points
- Stated expiry: `2026-07-30`
- Internal safety deadline: `2026-07-29`

These are historical planning inputs, not fresh runtime facts. Any live phase
requires fresh user_credit, current target-command help, actual unit-cost
confirmation, and a fresh human decision. Balanced future counts may be 6, 12,
or 18 only after that decision. Retry and resubmit maxima remain zero unless
separately authorized.

## Validation

- Exact new-path scope: 13 planned outputs
- Existing CAL-003 evidence changed: `false`
- Condition balance: `PASS`
- Prompt common-block identity: `PASS`
- Reference binding identity: `PASS`
- Submission-order count: `18`
- Contrast count: `8`
- Dreamina/Provider/credit operations: `0`
- Submit/query/download/retry/resubmit: `0/0/0/0/0`
- Media/reference operations: `0`
- Randomness: `0`
- Source changes: `0`
- Production/final/lock authority: `false/false/false`

## Next Phase

`CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_R1_NO_LIVE_DESIGN_REVIEW_AND_LIVE_ACTIVATION_HUMAN_DECISION`
