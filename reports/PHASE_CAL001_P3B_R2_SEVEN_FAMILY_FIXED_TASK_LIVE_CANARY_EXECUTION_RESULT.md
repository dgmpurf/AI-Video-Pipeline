# CAL-001 P3B-R2 Seven-Family Fixed-Task Live Canary Execution Result

## 1. Phase summary

- phase_id: `CAL-001-P3B-R2`
- program_id: `CAL-001`
- macro_id: `CAL-001A`
- executed: true
- status: `seven_family_live_canary_stopped`
- starting_head: `7c6fb9cc4e68ee7fcd192922c6f7a917def24b21`
- corrected_reauthorization_sha256_match: true
- corrected_reauthorization_byte_length_match: true
- prior_invalid_authorization_superseded: true
- submit_attempt_count: 1
- created_task_count: 1
- query_only_count: 0
- download_count: 0
- completed_canary_count: 0
- initial_live_credit: 6447
- final_live_credit: 6377
- observed_total_credit_delta: 70
- per_task_costs: `CAL001-F01-P2-R1=70`
- all_observed_task_costs_at_or_below_70: true
- all_credit_reconciliations_match: true
- all_result_counts_match: not_evaluable
- all_downloaded_media_valid: not_applicable
- review_artifacts_created_count: 0
- stop_condition_triggered: true
- stop_condition_reason: `submit_evidence_capture_anomaly`
- A15_actual_per_task_cost_status: `partial_single_task_reconciled_at_70_no_seven_family_conclusion`
- A16_provider_behavior_status: `partial_submit_creation_confirmed_query_and_download_not_evaluated_due_to_stop`
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- retry_count: 0
- resubmit_count: 0
- CAL001B_authorized: false
- visual_scores_assigned: false
- final_master: false
- locked: false
- sources_clean: true
- accepted_artifacts_unchanged: true
- recommended_next_phase: `CAL-001-P3B_R2_STOP_TRIAGE_AND_POST_CANARY_DECISION`
- final_verdict: `CAL001_P3B_R2_SEVEN_FAMILY_LIVE_CANARY_STOPPED_NO_RETRY_NO_REMAINING_TASK_AUTHORITY`

The first and only authorized submit created a trackable Dreamina task and consumed 70 credits. A local PowerShell post-processing expression then failed before it persisted the Dreamina subprocess exit code and sanitized stdout/stderr. The submit ID, log ID, querying state, and numeric credit count were recovered unambiguously from the newest row in the local Dreamina task database using read-only SQLite access. Because the strict valid-created-task evidence contract also requires the subprocess exit code and captured sanitized output, the whole canary stopped without querying, downloading, retrying, resubmitting, or advancing to the next task.

## 2. Starting checkpoint

- branch: `main`
- local HEAD: `7c6fb9cc4e68ee7fcd192922c6f7a917def24b21`
- origin/main: `7c6fb9cc4e68ee7fcd192922c6f7a917def24b21`
- local HEAD aligned with origin/main: true
- staged files before execution: none
- unrelated tracked modifications before execution: none
- sources/ clean before execution: true
- known unrelated untracked workspace noise was not staged.

## 3. Prior blocked attempt confirmation

The prior P3B blocked report remains unchanged:

`reports/PHASE_CAL001_P3B_SEVEN_FAMILY_FIXED_TASK_LIVE_CANARY_EXECUTION_RESULT.md`

- recomputed SHA256: `9884ce41a5134a069cdd70de84a810d4ee847a95da0ba9cc0a9b9763b39443f7`
- required prior verdict present: `CAL001_P3B_LIVE_CANARY_BLOCKED_BEFORE_SUBMIT_NO_CREDITS_CONSUMED`
- prior submit_attempt_count: 0
- prior created_task_count: 0
- prior query_only_count: 0
- prior download_count: 0
- prior completed_canary_count: 0
- prior observed_total_credit_delta: 0
- prior technical execution records: none
- prior CAL-001 run media: none
- prior dataset updates: none

## 4. Corrected reauthorization verification

The corrected Base64 authorization was decoded as raw bytes before any Dreamina command.

- encoding: UTF-8, strict decode
- decoded byte length: 3557
- required byte length: 3557
- LF-only line endings: true
- CR bytes present: false
- terminal LF present: false
- decoded SHA256: `a7f9afdfbf117f2ce29dd4b641d6dd324b9836f8a941ca873bfbf64db7a41fbb`
- expected SHA256 match: true
- exact prefix `I reauthorize CAL-001-P3B`: true
- seven experiment IDs present in exact order: true
- hard limits and stop conditions present: true
- `execution_authority_active=false`: confirmed
- `retry_count_max=0`: confirmed
- `resubmit_count_max=0`: confirmed
- `final_master=false`: confirmed
- `locked=false`: confirmed
- `CAL001B_authorized=false`: confirmed

The prior invalid expected hash `055b128d906d6793a0386d1a76bc096876264fdb2805d7b857d1e70cf1a25d8a` and prior decoded hash `9e1999d6e661d9c740a7deac4c159f192e63ab79b9f98d10f97141f626b0873e` were explicitly superseded and were not used.

The required authorization record was created before the first Dreamina command:

`experiments/CAL-001/reviews/CAL001_P3B_R2_seven_family_live_canary_reauthorization_record.json`

Its temporary scope was closed after the stop condition; `authorization_scope_active=false`.

## 5. Accepted artifact revalidation

| Artifact or aggregate | Recomputed SHA256 | Match |
| --- | --- | --- |
| fixed manifest | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` | true |
| fixture registry | `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142` | true |
| prompt inventory | `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d` | true |
| package inventory | `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c` | true |
| full experiment inventory | `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138` | true |
| H1 acceptance record | `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7` | true |
| human checklist | `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3` | true |

The fixed manifest contains 84 rows. All seven canary IDs exist in order. Each selected package, prompt file, provider-prompt payload, fixture path, fixture order, and fixture SHA256 matched its committed definition. H1 still records `fixed_manifest_human_reviewed=true` and `fixed_manifest_human_accepted=true`.

## 6. Runtime preflight

Preferred executable:

`C:/Users/msjpurf/bin/dreamina.exe`

- executable SHA256: `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- `dreamina version`: exit 0
- version: `2a20fff-dirty`
- commit: `2a20fff`
- build time: `2026-06-26T06:36:39Z`
- `dreamina user_credit`: exit 0
- initial total credit: 6447
- VIP level: `maestro`
- logger Access denied: absent
- login/auth failure: absent
- `dreamina text2video -h`: exit 0
- required flags present: `--prompt --duration --ratio --video_resolution --model_version --poll`
- current live Web/safety confirmation requirement: not returned
- task-1 required minimum: 6440
- task-1 credit threshold met: true

The help text includes a generic note that some high-risk models may require first-use Web confirmation. No such live response was returned during the canary preflight or submit evidence.

## 7. Authorized task order

1. `CAL001-F01-P2-R1`
2. `CAL001-F02-P2-R1`
3. `CAL001-F03-P2-R1`
4. `CAL001-F04-P2-R1`
5. `CAL001-F05-P2-R1`
6. `CAL001-F06-P2-R1`
7. `CAL001-F07-P2-R1`

No task was reordered, skipped forward, replaced, retried, or resubmitted.

## 8. Counter and budget ledger

| Counter | Allowed maximum | Observed |
| --- | ---: | ---: |
| submit attempts | 7 | 1 |
| created tasks | 7 | 1 |
| query-only checks per created submit ID | 3 | 0 |
| total query-only checks | 21 | 0 |
| downloads | 7 | 0 |
| retries | 0 | 0 |
| resubmits | 0 | 0 |
| cumulative canary credits | 490 | 70 |
| per-task credits | 70 | 70 |

The remaining 77 fixed-manifest tasks were not activated.

## 9. Per-task execution

| Order | Experiment ID | Attempted | Created | Queries | Download | Technical status |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | `CAL001-F01-P2-R1` | true | true | 0 | not attempted | `created_querying_then_canary_stopped_due_to_submit_evidence_capture_anomaly` |
| 2 | `CAL001-F02-P2-R1` | false | false | 0 | not attempted | `not_attempted_due_to_prior_stop` |
| 3 | `CAL001-F03-P2-R1` | false | false | 0 | not attempted | `not_attempted_due_to_prior_stop` |
| 4 | `CAL001-F04-P2-R1` | false | false | 0 | not attempted | `not_attempted_due_to_prior_stop` |
| 5 | `CAL001-F05-P2-R1` | false | false | 0 | not attempted | `not_attempted_due_to_prior_stop` |
| 6 | `CAL001-F06-P2-R1` | false | false | 0 | not attempted | `not_attempted_due_to_prior_stop` |
| 7 | `CAL001-F07-P2-R1` | false | false | 0 | not attempted | `not_attempted_due_to_prior_stop` |

## 10. Submit evidence

Exactly one submit command was invoked:

```text
C:/Users/msjpurf/bin/dreamina.exe text2video --prompt <verified_provider_prompt sha256=47da84130c17af6eb3d79e5360ad2905acc81729e1e56d51771573e2ecc54ee9 chars=391> --duration 5 --ratio 16:9 --video_resolution 720p --model_version seedance2.0_vip --poll 0
```

Recovered non-sensitive task evidence:

- experiment_id: `CAL001-F01-P2-R1`
- submit_id: `4e4588dd-a0e1-4539-8390-692cb9bf80f8`
- logid: `20260718154849169254047008489C358`
- gen_status: `querying`
- queue_status: not returned/recovered
- fail_reason: none
- numeric credit_count: 70
- task DB create_time: Unix `1784360929`
- task DB update_time: Unix `1784360932`
- task DB evidence source: `C:/Users/msjpurf/.dreamina_cli/tasks.db`, opened read-only
- request and result payloads from the task DB were not printed.

The local wrapper failed only after Dreamina returned, on a malformed PowerShell chained replacement expression:

```text
The -ireplace operator allows only two elements to follow it, not 6.
```

Consequences:

- Dreamina subprocess exit code was not persisted.
- Sanitized stdout/stderr was not persisted.
- No second submit was issued.
- Missing evidence was not invented or normalized.
- The strict valid-created-task evidence gate was treated as incomplete and activated the stop condition.

## 11. Query evidence

- query_only_count: 0
- `query_result` calls: none
- query history: empty
- current recorded state: `querying_unqueried_after_stop`

The stop condition occurred immediately after submit evidence recovery. No query was used to compensate for the missing submit-output capture.

## 12. Result-count gates

No terminal result was queried.

- result_images_count: unknown
- result_videos_count: unknown
- output_count: unknown
- result_count_match: not evaluated
- exact single-video download gate: not reached

## 13. Download and validation

- download_count: 0
- download command invoked: false
- download directory used: none
- local media created: none
- MP4 validation performed: false
- media technical validity: not applicable

## 14. Credit reconciliation

| Experiment ID | Pre-submit | Submit credit_count | Post-submit/final | Observed delta | Match | At or below 70 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `CAL001-F01-P2-R1` | 6447 | 70 | 6377 | 70 | true | true |

- cumulative observed credit delta: 70
- cumulative limit for one created task: 70
- cumulative canary budget maximum: 490
- reconciliation anomaly: none
- stale-credit recheck used: false

## 15. Review artifacts

No review artifacts were created because no successful download or media validation occurred.

- metadata JSON: none
- extracted frames: none
- contact sheet: none
- cuts: none
- visual scores: none
- winner selection: none

## 16. Dataset updates

Only the technical fields for `CAL001-F01-P2-R1` were updated in:

`experiments/CAL-001/datasets/CAL001_experiment_results_template.csv`

Changed fields:

- `submit_attempted=true`
- `submit_created_task=true`
- `submit_id=4e4588dd-a0e1-4539-8390-692cb9bf80f8`
- `submit_status=task_created`
- `final_gen_status=querying`
- `actual_credit_cost=70`
- `stop_condition_triggered=true`

The existing `query_count=0` and `download_status=not_attempted` values already represented the stopped state and therefore did not require a byte change. All visual score fields, labels, reviewer notes, best usable window, and candidate classifications remain empty/unreviewed. `human_review_status` remains `not_started`. The other 83 result rows are byte-for-byte unchanged. The visual-review JSONL was not modified.

## 17. Stop evaluation

- stop_condition_triggered: true
- stop_condition_class: `submit_evidence_capture_anomaly`
- stopping experiment: `CAL001-F01-P2-R1`
- stopping point: after one created submit and exact credit reconciliation, before any query
- reason: the Dreamina subprocess exit code and sanitized stdout/stderr required by the submit evidence contract were not persisted because the local wrapper failed after the command returned.
- response: no query, no download, no next submit, no retry, no resubmit, no replacement, no prompt rewrite, and no manifest expansion.
- authorization_scope_active after stop: false
- execution_authority_active after stop: false

## 18. Completed and unattempted canaries

- completed_canary_count: 0
- completed canary IDs: none
- attempted but incomplete canary: `CAL001-F01-P2-R1`
- unattempted_canary_count: 6
- unattempted_canary_ids: `CAL001-F02-P2-R1`, `CAL001-F03-P2-R1`, `CAL001-F04-P2-R1`, `CAL001-F05-P2-R1`, `CAL001-F06-P2-R1`, `CAL001-F07-P2-R1`

## 19. A15 actual-cost conclusion

`A15_actual_per_task_cost_status=partial_single_task_reconciled_at_70_no_seven_family_conclusion`

One fixed task produced exact, reconciled evidence of a 70-credit charge. This supports the planned upper bound for that single task only. It does not validate seven-family aggregate cost behavior and does not activate the remaining tasks.

## 20. A16 provider-behavior conclusion

`A16_provider_behavior_status=partial_submit_creation_confirmed_query_and_download_not_evaluated_due_to_stop`

The provider accepted one fixed `text2video` task, assigned a submit ID and log ID, and recorded `gen_status=querying`. Terminal provider behavior, result count, downloadable output behavior, and media validity were not evaluated because the evidence-capture anomaly required an immediate stop.

## 21. Remaining-task authority

- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- remaining seven-canary tasks authorized after stop: false
- remaining 77 fixed-manifest tasks authorized: false
- CAL001B_authorized: false
- automatic prompt rewrite: false
- automatic manifest expansion: false
- batch expansion: false
- retry_count_max: 0
- resubmit_count_max: 0

## 22. Media/Git boundary

- generated video files: none
- extracted frames: none
- contact sheets: none
- binary artifacts staged: none
- media committed: none
- only authorized technical text evidence is eligible for staging.
- sources/, manifests, prompts, packages, fixtures, schemas, matrix, budget, README, checklist, H1 record, P3A report, and prior P3B report remain outside the staged scope.

## 23. Explicit non-actions

- no query
- no download
- no retry
- no resubmit
- no replacement
- no batch
- no concurrent task execution
- no prompt rewrite
- no manifest expansion
- no Source modification
- no package, prompt, fixture, schema, matrix, or budget modification
- no visual review or scoring
- no winner selection
- no final-master action
- no lock action
- no CAL-001B authorization
- no tag

## 24. Recommended next phase

`CAL-001-P3B_R2_STOP_TRIAGE_AND_POST_CANARY_DECISION`

The next phase should review the local submit-output capture failure and decide whether a separately authorized query-only action is appropriate for the existing submit ID. It must not treat any future attempt as an implicit retry or resubmit, and this report grants no live authority.

## 25. Final verdict

`CAL001_P3B_R2_SEVEN_FAMILY_LIVE_CANARY_STOPPED_NO_RETRY_NO_REMAINING_TASK_AUTHORITY`
