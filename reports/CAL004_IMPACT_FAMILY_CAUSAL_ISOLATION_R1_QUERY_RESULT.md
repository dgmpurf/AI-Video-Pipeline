# CAL-004 Impact-Family Causal Isolation R1 Query Result

## Decision

- Decision: `CAL004_R1_QUERY_COMPLETE_ALL_EIGHTEEN_REMOTE_SUCCESS`
- Starting HEAD: `c62a347f6835820ddbb0a0c96326f009da413204`
- Authorization: bytes `1362`; SHA-256 `1ffb509b8abe972641d9b614309ceb94b91e586147381cae2fab2a34e18b4626`; Base64 characters `1816`
- Authorization activated/consumed/reusable: `true / true / false`
- Query rounds used: `1 / 24`
- Total query invocations: `18 / 432`
- All terminal: `true`

## Preflight

- Branch: `main`
- HEAD/origin aligned: `true`
- Tracked/staged/Source changes: `0 / 0 / 0`
- Exact committed task and submit-ID bindings: `PASS`
- Task IDs unique: `true`
- Submit IDs unique: `true`
- Prior query/download/retry/resubmit counts: `0 / 0 / 0 / 0`
- `dreamina query_result -h`: `PASS`
- `user_credit` called: `false`

One local pre-activation compatibility correction replaced an unavailable
PowerShell static SHA-256 API with the compatible `SHA256.Create` path. It did
not consume a query call or change scope.

## Task Results

| Position | Task | Condition | Route | submit_id | Queries | Final status | Terminal | Result present |
|---:|---|---|---|---|---:|---|---|---|
| 1 | N0-01 | N0 | text2video | `5ede7644-ecec-42bb-ac80-46eec0b4e539` | 1 | success | true | true |
| 2 | II-01 | II | multimodal2video | `9f794478-badd-4c96-ace0-269b6a249217` | 1 | success | true | true |
| 3 | NP-01 | NP | multimodal2video | `f85812b1-d3f3-4a11-979d-af869db66beb` | 1 | success | true | true |
| 4 | I0-01 | I0 | text2video | `52b93a7b-a2bc-408c-924a-e49324ddee9b` | 1 | success | true | true |
| 5 | NI-01 | NI | multimodal2video | `2c6ac89a-f197-43a6-99d0-a960c64aa097` | 1 | success | true | true |
| 6 | IP-01 | IP | multimodal2video | `a7803e10-d5d2-4e72-bd72-938a77c36c14` | 1 | success | true | true |
| 7 | IP-02 | IP | multimodal2video | `8d56d2d8-85ef-4c63-ba1a-5a8981907294` | 1 | success | true | true |
| 8 | NI-02 | NI | multimodal2video | `a6639903-0c38-4013-886e-a3648385c1b7` | 1 | success | true | true |
| 9 | I0-02 | I0 | text2video | `b30ff9af-932c-4654-b1d1-239ac6144edc` | 1 | success | true | true |
| 10 | NP-02 | NP | multimodal2video | `f99be447-8edb-406a-82ba-fa577ec20aab` | 1 | success | true | true |
| 11 | II-02 | II | multimodal2video | `fac76984-627a-440a-93ab-f588ff90a8fe` | 1 | success | true | true |
| 12 | N0-02 | N0 | text2video | `59cb2e47-7162-4317-94df-764a3f1eaec8` | 1 | success | true | true |
| 13 | NP-03 | NP | multimodal2video | `83a4a012-09b9-40b5-bd64-1ed4c169e843` | 1 | success | true | true |
| 14 | I0-03 | I0 | text2video | `0fbe85c5-3509-4e45-b52a-6208b8911964` | 1 | success | true | true |
| 15 | NI-03 | NI | multimodal2video | `e1d1353d-b17e-432f-b233-e3126474fe08` | 1 | success | true | true |
| 16 | IP-03 | IP | multimodal2video | `189041c8-274c-47e4-9b82-8a3181c51f0c` | 1 | success | true | true |
| 17 | N0-03 | N0 | text2video | `43b1cc9e-3958-4604-89b3-b92124ed61c5` | 1 | success | true | true |
| 18 | II-03 | II | multimodal2video | `f88d080b-167d-44be-ab21-a60e78d74ab7` | 1 | success | true | true |

Every task returned one video result indication and a result URL in memory.
No URL is printed or persisted. This is remote technical availability only,
not visual success.

## Batch Summary

- Success tasks: `18`
- Remote-failure tasks: `0`
- Still-querying tasks: `0`
- Unknown tasks: `0`
- Other-terminal tasks: `0`
- Balanced condition terminal coverage: `true`

| Condition | Tasks | Success | Remote failure | Querying | Unknown |
|---|---:|---:|---:|---:|---:|
| N0 | 3 | 3 | 0 | 0 | 0 |
| I0 | 3 | 3 | 0 | 0 | 0 |
| NI | 3 | 3 | 0 | 0 | 0 |
| NP | 3 | 3 | 0 | 0 | 0 |
| II | 3 | 3 | 0 | 0 | 0 |
| IP | 3 | 3 | 0 | 0 | 0 |

- text2video route: `6/6 success`
- multimodal2video route: `12/12 success`

## Boundaries

- Submit/download/retry/resubmit: `0 / 0 / 0 / 0`
- Credits queried or consumed: `false / false`
- Historical ending balance `661` was not refreshed or asserted as current.
- Media accessed: `false`
- Visual success claimed: `false`
- Scientific result derived: `false`
- Signed URLs persisted or disclosed: `false`
- Sources changed: `false`
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## Evidence

- Query evidence root: `experiments/CAL-004/IMPACT_FAMILY_CAUSAL_ISOLATION_V1/R1_QUERY_V0_1`
- Task status records: `18`
- Evidence manifest binds the other twenty-two new outputs plus committed design
  and submit identity evidence.
- Temporary recovery attempts used: `1`

## Next Phase

`CAL004_R1_QUERY_COMPLETE_DOWNLOAD_SELECTION_HUMAN_DECISION`
