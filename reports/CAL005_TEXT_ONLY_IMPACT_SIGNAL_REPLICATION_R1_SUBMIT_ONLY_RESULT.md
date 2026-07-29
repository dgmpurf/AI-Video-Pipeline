# CAL-005 R1 Conditional Balanced Submit-Only Result

## Decision

- Decision: `CAL005_R1_CONDITIONAL_BALANCED_SUBMIT_ONLY_COMPLETE`
- Execution ID: `CAL005-R1-CONDITIONAL-BALANCED-SUBMIT-A9D86918`
- Starting checkpoint: `b01515e7a1980ba687dd55eb9d3303e972d6f3e7`
- Authorization activated/consumed/reusable: `true / true / false`

## Accepted Runtime Preflight

- Dreamina executable: `C:\Users\msjpurf\bin\dreamina.EXE`
- Version/commit/build: `2a20fff-dirty / 2a20fff / 2026-06-26T06:36:39Z`
- Successful `user_credit` accepted as account authentication evidence by direct recovery authorization: `true`
- Fresh starting balance: `741`
- `login checklogin` device-code command mismatch accepted: `true`
- Version/login-check/user-credit/help reruns after recovery authorization: `0`
- `text2video` semantics: `PASS`
- Poll flag passed: `false`

## Conditional Execution

- Canary task: `N0R-01`
- Canary accepted: `true`
- Canary credit count: `70`
- Full-block required cost: `420`
- Full-block continuation authorized: `true`
- Full-block continuation performed: `true`
- Submit attempted/accepted/failed: `6 / 6 / 0`
- Derived credit decrement: `420`
- Derived ending balance: `321`
- Second `user_credit` call: `false`
- Stop reason: `none`

## Task Receipts

| Position | Task | Condition | Replicate | State | Submit ID | Provider state | Credit |
|---:|---|---|---:|---|---|---|---:|
| 1 | `N0R-01` | `N0R` | `1` | `ACCEPTED` | `5dc990df-da16-40f6-87e1-7aa1922df108` | `querying` | `70` |
| 2 | `I0R-01` | `I0R` | `1` | `ACCEPTED` | `9fb9feb9-688c-44c5-b850-0cb90b98ee67` | `querying` | `70` |
| 3 | `I0R-02` | `I0R` | `2` | `ACCEPTED` | `8c5e91a6-cee0-4401-bf4a-c1a3450b0d8d` | `querying` | `70` |
| 4 | `N0R-02` | `N0R` | `2` | `ACCEPTED` | `46042e22-266f-4cb5-9c57-29aa2bc8934e` | `querying` | `70` |
| 5 | `N0R-03` | `N0R` | `3` | `ACCEPTED` | `79d78266-f8c4-483a-aada-efece59f389b` | `querying` | `70` |
| 6 | `I0R-03` | `I0R` | `3` | `ACCEPTED` | `45efc667-7831-4657-9249-f60a80966b07` | `querying` | `70` |

## Boundaries

- Query/download/retry/resubmit: `0 / 0 / 0 / 0`
- Media accessed: `false`
- Generation completion known: `false`
- Visual success known: `false`
- Scientific result derived: `false`
- Source changed: `false`
- `production_approved=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

Next phase: `CAL005_R1_SUBMIT_COMPLETE_QUERY_AUTHORIZATION_HUMAN_DECISION`.
