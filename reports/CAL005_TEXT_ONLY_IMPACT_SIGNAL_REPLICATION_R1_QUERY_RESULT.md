# CAL-005 R1 Bounded Query-Only Result

## Decision

- Decision: `CAL005_R1_QUERY_COMPLETE_ALL_SIX_REMOTE_SUCCESS`
- Execution ID: `CAL005-R1-BOUNDED-QUERY-07B129D2`
- Starting checkpoint: `464c737ad46fdf1265b35f54db359e72757c79a7`
- Authorization activated/consumed/reusable: `true / true / false`

## Query Execution

- Query rounds used/max: `1 / 24`
- Query invocations used/max: `6 / 144`
- Minimum inter-round delay: `300` seconds
- Delay compliance: `true`
- All six Provider terminal: `true`
- All six resolved for Goal: `true`

| Position | Task | Condition | Replicate | Submit ID | Queries | Final state | Governed status | Terminal | Videos |
|---:|---|---|---:|---|---:|---|---|---|---:|
| 1 | `N0R-01` | `N0R` | 1 | `5dc990df-da16-40f6-87e1-7aa1922df108` | 1 | `success` | `SUCCESS` | `true` | `1` |
| 2 | `I0R-01` | `I0R` | 1 | `9fb9feb9-688c-44c5-b850-0cb90b98ee67` | 1 | `success` | `SUCCESS` | `true` | `1` |
| 3 | `I0R-02` | `I0R` | 2 | `8c5e91a6-cee0-4401-bf4a-c1a3450b0d8d` | 1 | `success` | `SUCCESS` | `true` | `1` |
| 4 | `N0R-02` | `N0R` | 2 | `46042e22-266f-4cb5-9c57-29aa2bc8934e` | 1 | `success` | `SUCCESS` | `true` | `1` |
| 5 | `N0R-03` | `N0R` | 3 | `79d78266-f8c4-483a-aada-efece59f389b` | 1 | `success` | `SUCCESS` | `true` | `1` |
| 6 | `I0R-03` | `I0R` | 3 | `45efc667-7831-4657-9249-f60a80966b07` | 1 | `success` | `SUCCESS` | `true` | `1` |

## Counts And Boundaries

- Success/remote failure/other terminal/unknown/querying: `6 / 0 / 0 / 0 / 0`
- Submit/query/download/retry/resubmit: `0 / 6 / 0 / 0 / 0`
- Credits queried or consumed: `false`
- Signed URLs persisted: `false`
- Media accessed: `false`
- Visual success claimed: `false`
- Scientific result derived: `false`
- Sources changed: `false`
- `production_approved=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

Next phase: `CAL005_R1_ALL_MEDIA_REMOTE_SUCCESS_DOWNLOAD_AUTHORIZATION_HUMAN_DECISION`.
