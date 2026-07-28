# CAL-004 Impact-Family Causal Isolation R1 Conditional Balanced Submit-Only Result

## Decision

- Decision: `CAL004_R1_CONDITIONAL_BALANCED_SUBMIT_ONLY_COMPLETE`
- Execution ID: `CAL004-R1-CONDITIONAL-BALANCED-SUBMIT-8D8CEBD5`
- Starting HEAD: `89a51bff9cd68e87d7bef1b46361781de62bd545`
- Selected balanced target: `18`
- Attempted tasks: `18`
- Accepted submits: `18`
- Failed submits: `0`

## Fresh Runtime Preflight

- Dreamina version: `2a20fff-dirty` (`2a20fff`, build `2026-06-26T06:36:39Z`)
- Fresh starting balance: `2761`
- text2video help: `PASS`
- multimodal2video help: `PASS`
- Prompt bindings: `PASS`
- Governed reference bindings: `PASS`

No private account identifiers, session material, signed URLs, or raw provider
output are persisted.

## Route Contract

- N0 and I0: `text2video`, zero motion reference.
- NI, NP, II and IP: `multimodal2video`, exactly one governed video reference.
- Formal text2video canary: `N0-01`.
- Formal multimodal2video canary: `II-01`.
- Both accepted canaries remain valid experimental samples.

Primary within-command contrasts are NI/NP, II/IP, I0/N0 and II/NI.
II/I0, IP/I0, NI/N0 and NP/N0 are
`REFERENCE_PLUS_COMMAND_ROUTE_BUNDLE_CONTRASTS`, not pure reference causal
effects.

## Balanced Target Selection

- Observed text2video unit cost: `70`
- Observed multimodal2video unit cost: `140`
- Complete six-condition block cost: `700`
- Selected target: `18`
- Partial six-condition block intentionally selected: `false`

## Submit Receipts

| Position | Task | Route | submit_id | Credit | Result |
|---:|---|---|---|---:|---|
| 1 | N0-01 | text2video | 5ede7644-ecec-42bb-ac80-46eec0b4e539 | 70 | PASS |
| 2 | II-01 | multimodal2video | 9f794478-badd-4c96-ace0-269b6a249217 | 140 | PASS |
| 3 | NP-01 | multimodal2video | f85812b1-d3f3-4a11-979d-af869db66beb | 140 | PASS |
| 4 | I0-01 | text2video | 52b93a7b-a2bc-408c-924a-e49324ddee9b | 70 | PASS |
| 5 | NI-01 | multimodal2video | 2c6ac89a-f197-43a6-99d0-a960c64aa097 | 140 | PASS |
| 6 | IP-01 | multimodal2video | a7803e10-d5d2-4e72-bd72-938a77c36c14 | 140 | PASS |
| 7 | IP-02 | multimodal2video | 8d56d2d8-85ef-4c63-ba1a-5a8981907294 | 140 | PASS |
| 8 | NI-02 | multimodal2video | a6639903-0c38-4013-886e-a3648385c1b7 | 140 | PASS |
| 9 | I0-02 | text2video | b30ff9af-932c-4654-b1d1-239ac6144edc | 70 | PASS |
| 10 | NP-02 | multimodal2video | f99be447-8edb-406a-82ba-fa577ec20aab | 140 | PASS |
| 11 | II-02 | multimodal2video | fac76984-627a-440a-93ab-f588ff90a8fe | 140 | PASS |
| 12 | N0-02 | text2video | 59cb2e47-7162-4317-94df-764a3f1eaec8 | 70 | PASS |
| 13 | NP-03 | multimodal2video | 83a4a012-09b9-40b5-bd64-1ed4c169e843 | 140 | PASS |
| 14 | I0-03 | text2video | 0fbe85c5-3509-4e45-b52a-6208b8911964 | 70 | PASS |
| 15 | NI-03 | multimodal2video | e1d1353d-b17e-432f-b233-e3126474fe08 | 140 | PASS |
| 16 | IP-03 | multimodal2video | 189041c8-274c-47e4-9b82-8a3181c51f0c | 140 | PASS |
| 17 | N0-03 | text2video | 43b1cc9e-3958-4604-89b3-b92124ed61c5 | 70 | PASS |
| 18 | II-03 | multimodal2video | f88d080b-167d-44be-ab21-a60e78d74ab7 | 140 | PASS |

Failed tasks: `none`

Unattempted tasks: `none`

## Credit Accounting

- Fresh starting balance: `2761`
- Total observed credit decrement: `2100`
- Ending balance, derived from provider credit evidence:
  `661`
- Additional user_credit calls after preflight: `0`

## Boundaries

- Query/download: `0/0`
- Retry/resubmit: `0/0`
- Randomness: `0`
- Semantic review/unblinding: `0/0`
- Media creation or download: `0`
- Source changes: `0`
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## Next Phase

`CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_R1_QUERY_AUTHORIZATION_HUMAN_DECISION`
