# CAL-001 P3D W01 F06 Single Recovery Submit-Only Reauthorization Result

## 1. Phase summary

- executed: true
- status: F06_single_recovery_submit_only_reauthorized_ready_no_live
- starting_head: fc1b025548cf982711d3790a7f2ac883b3d1d479
- authorization_decision: APPROVE_CAL001_F06_SINGLE_RECOVERY_SUBMIT_ONLY_REAUTHORIZATION_RECORD_ONLY_ACTIVATE_85_TOTAL_SUBMIT_INVOCATION_CAP_70_CREDIT_TRANSPORT_LOSS_CONTINGENCY_5950_ABSOLUTE_CREDIT_CEILING_5670_FRESH_PRE_SUBMIT_BALANCE_GATE_AUTHORIZE_EXACTLY_ONE_FUTURE_F06_RECOVERY_SUBMIT_ONLY_KEEP_OLD_HANDLE_QUARANTINED_NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_SECOND_RECOVERY_NO_F07_COMMIT_PUSH_NO_DREAMINA_IN_THIS_RECORD_ONLY_PHASE.
- authorization_byte_length: 404
- authorization_text_sha256: 35af5a5ed0dbabf7bf03ab0967a3eb2cf9c13a191c5eebe9ab2f1a4125b1fa33
- authorization_base64_verified: true
- authorization_round_trip_verified: true
- prior_readiness_verified: true
- old_handle_quarantine_verified: true
- accepted_hashes_verified: true
- accepted_F06_binding_unchanged: true
- fixed_task_count: 84
- technically_completed_fixed_task_count: 12
- confirmed_created_or_completed_submit_count: 12
- historical_submit_invocation_count_including_orphan: 13
- active_total_submit_invocation_cap: 85
- active_base_credit_budget_max: 5880
- active_transport_loss_contingency_credit_max: 70
- active_absolute_credit_ceiling: 5950
- active_recovery_pre_submit_minimum_live_balance: 5670
- old_F06_credit_consumption_classification: credit_consumption_unresolved
- old_F06_confirmed_credit_cost: null
- recovery_submit_authorized: true
- recovery_submit_count_max: 1
- recovery_submit_count: 0
- recovery_query_authorized: false
- recovery_download_authorized: false
- recovery_retry_authorized: false
- second_recovery_submit_authorized: false
- F07_authorized: false
- Dreamina_run: false
- Dreamina_command_count: 0
- credits_consumed: 0
- media_created: false
- datasets_modified: false
- sources_clean: true
- macro_state: ACTIVATED_READY_FOR_F06_RECOVERY_SUBMIT_ONLY
- activation_state: ACTIVATED_READY_FOR_F06_RECOVERY_SUBMIT_ONLY
- execution_authority_active: true
- remaining_noncanary_tasks_authorized: false
- next_wave_id: W01
- next_experiment_id: CAL001-F06-P1-R1
- final_master: false
- locked: false

## 2. Starting checkpoint

Local `main`, HEAD, and `origin/main` matched `fc1b025548cf982711d3790a7f2ac883b3d1d479`. The index and tracked worktree were clean, `sources/` was clean, and only known longstanding untracked workspace noise remained.

## 3. Exact authorization fingerprint

The exact 404-byte UTF-8 authorization was decoded once. SHA-256, exact token equality, single-token count, Base64 equality, and byte-for-byte round trip all passed. No normalization, translation, trimming, or regeneration was used.

## 4. Prior readiness-review verification

The readiness authorization, record, report, and state contract existed and parsed. The prior status was `F06_recovery_readiness_and_budget_review_completed_proposal_inactive`; the prior verdict was `CAL001_P3D_W01_F06_RECOVERY_READINESS_REVIEW_PASSED_PROPOSAL_INACTIVE_REQUIRES_HUMAN_REAUTHORIZATION`. Before this phase, the proposal and recovery authority were false, active submit cap was 84, and base credit budget was 5880.

## 5. Old-handle quarantine verification

The old submit ID `cabfa6ab-cc61-4d29-8630-da01dfdeef65` remains preserved and quarantined. It has one historical invocation, four historical queries, zero downloads, `provider_task_created=false`, `created_task_count=0`, and no query/download/reuse authority. The new recovery authority does not reinterpret or reactivate it.

## 6. Accepted immutable hashes

The fixed manifest, fixture registry, Prompt inventory, package inventory, full inventory, and remaining-order SHA-256 values matched the accepted values. Manifest and unique experiment counts were 84/84; Prompt, package, and fixture mismatch counts were 0/0/0. No task or manifest expansion occurred.

## 7. Unchanged F06 binding

The recovery remains the same fixed `CAL001-F06-P1-R1` task: `multimodal2video`, `seedance2.0_vip`, 5 seconds, `16:9`, `720p`, expected 0 images/1 video/1 output, and 70 credits. Prompt, package, three fixture paths, hashes, and order are unchanged. No recovery package or replacement asset was created.

## 8. Accounting semantics

Fixed tasks remain 84, technically completed tasks 12, and remaining tasks 72. Confirmed-created-or-completed submits remain 12. Historical submit invocations including the orphan are 13. Recovery submit invocation count is 0 before the future live Goal. Confirmed CAL-001A cost remains 840; old F06 confirmed cost remains null.

## 9. Active 85-invocation cap

The active total CAL-001A submit-invocation cap is now 85: 84 accepted fixed-task invocations plus at most one transport-loss recovery invocation for the same F06 task. This does not add a fixed task, manifest row, batch member, replacement, or second recovery.

## 10. Active 70-credit contingency

The active transport-loss contingency and unresolved old-F06 reserve are 70 credits. This reserve remains separate from confirmed cost until later conclusive reconciliation.

## 11. Active 5880 base budget and 5950 absolute ceiling

The base accepted-task credit budget remains 5880. The active absolute ceiling is 5950, consisting of the 5880 base plus the bounded 70-credit transport-loss contingency. Positive drift or refunds do not enlarge task scope.

## 12. Active 5670 fresh live-balance gate

The future recovery submit requires a fresh live balance of at least 5670. Historical balance 5695 is stale and cannot satisfy the future preflight.

## 13. Exactly one future recovery submit-only authority

Exactly one future F06 recovery submit-only Goal is authorized. Recovery submit count is 0 of 1. Query, download, retry, second recovery, F07, W02+, and CAL001B are not authorized.

## 14. Future live Goal contract

`CAL-001-P3D-W01_F06_SINGLE_RECOVERY_SUBMIT_ONLY` may verify repository and bindings, run current environment canary/help, obtain one fresh pre-submit credit value, perform one durable F06 submit, obtain one immediate post-submit credit value, reconcile evidence, close authority, commit, and push. It may not query, download, execute F07, retry, perform another submit, create media, update datasets, or mark technical completion.

## 15. Success criteria

A valid provider task requires a new submit ID different from the old handle, classifier-proven creation, `created_task_count=1`, valid created/nonterminal status, no upload failure, present logid, numeric provider credit count exactly 70, immediate balance delta exactly 70, and durable envelope/parsed evidence. Submit success does not authorize query or download.

## 16. Stop conditions

Any repository, Source, hash, binding, parser, quarantine, runtime, canary, authentication, logger, balance, upload, submit-ID, creation-proof, logid, credit, cap, ceiling, or unclassified anomaly stops the future Goal. No stop branch may query, download, retry, submit again, or execute F07.

## 17. Authority-closing behavior

The future live Goal must close authority immediately after its one submit attempt and immediate post-submit credit reconciliation, regardless of success or failure. A separate human authorization is required before querying any new recovery submit ID.

## 18. F01-F05 preservation

F01-F05 remain technically completed; their records, datasets, media, frames, contact sheets, and review artifacts are unchanged.

## 19. F07 preservation

F07 remains `pending_preflight`, with zero submit attempts, null submit ID, and no authority.

## 20. No-live proof

This phase ran no Dreamina command, provider action, submit, query, download, credit operation, or media operation. `Dreamina_command_count=0`, credits consumed are 0, and no media or dataset was created.

## 21. Source/dataset/media boundary

Source, Prompt, package, fixture, manifest, inventory, schema, dataset, parser, tests, and media remained unchanged. No sensitive log was staged.

## 22. Files created/modified

Created: one reauthorization JSON, one activation JSON, and this report. Modified: only the mutable execution-state contract.

## 23. Git scope

Only the four authorized record/state paths may be staged. No Source, accepted artifact, parser/test, historical evidence, dataset, media, sensitive log, or unrelated path is included.

## 24. Commit and push result

The authorized commit message is `docs: authorize CAL-001 W01 F06 recovery submit`. This report is part of that commit; the final Codex response records the resulting commit hash and push alignment.

## 25. Recommended next phase

- recommended_next_phase: CAL-001-P3D-W01_F06_SINGLE_RECOVERY_SUBMIT_ONLY

## 26. Final verdict

- stop_condition: none at activation; future mandatory stop conditions remain binding.
- final_verdict: CAL001_P3D_W01_F06_SINGLE_RECOVERY_SUBMIT_ONLY_REAUTHORIZED_READY_FOR_SEPARATE_LIVE_GOAL
