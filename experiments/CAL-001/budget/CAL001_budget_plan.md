# CAL-001 Budget Plan

## Fixed arithmetic

| Field | Value |
| --- | ---: |
| user_reported_credits | 6447 |
| fixed_task_count | 84 |
| planned_unit_cost_assumption | 70 |
| planned_total_cost | 5880 |
| credit_floor | 560 |
| budget_plus_floor | 6440 |
| planning_residual | 7 |

Arithmetic: 84 x 70 = 5880; 5880 + 560 = 6440; 6447 - 6440 = 7.

## Gates

- The 70-credit unit cost is a planning assumption, not a live verified fact for every task type.
- Daily credits claimed after authorization are excluded from CAL-001A.
- CAL-001B requires separate English authorization.
- Live cost must be verified before activation.
- No task may be added, removed, replaced, or silently downgraded to fit the budget.
- No automatic model, resolution, or duration downgrade is allowed.
- If any live cost exceeds the approved assumption, activation or execution must stop.
- execution_authority_active=false; final_master=false; locked=false.
