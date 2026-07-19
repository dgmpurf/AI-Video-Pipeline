# CAL-001 P3D W01 F06 Recovery Readiness and Budget Review Result

## 1. Phase summary

- executed: true
- status: F06_recovery_readiness_and_budget_review_completed_proposal_inactive
- starting_head: 0273eea8895548ad46f1e23ce8ef3f0304646e94
- authorization_decision: APPROVE_CAL001_F06_RECOVERY_READINESS_AND_BUDGET_REVIEW_RECORD_ONLY_VERIFY_UNCHANGED_BINDINGS_DESIGN_85_TOTAL_SUBMIT_INVOCATION_CAP_70_CREDIT_CONTINGENCY_AND_5670_PRE_SUBMIT_BALANCE_GATE_COMMIT_PUSH_NO_DREAMINA_NO_RECOVERY_SUBMIT.
- authorization_byte_length: 230
- authorization_text_sha256: 699986e09949ef45dc290010b6fd21c6f24287d252eb41c97ee7d5728472e43f
- authorization_base64_verified: true
- authorization_round_trip_verified: true
- parser_correction_verified: true
- old_handle_quarantine_verified: true
- accepted_hashes_verified: true
- accepted_F06_binding_unchanged: true
- fixed_task_count: 84
- technically_completed_fixed_task_count: 12
- confirmed_created_or_completed_submit_count: 12
- historical_submit_invocation_count_including_orphan: 13
- remaining_fixed_task_count: 72
- normal_remaining_task_credit: 5040
- credit_floor: 560
- base_required_live_balance: 5600
- old_F06_credit_consumption_classification: credit_consumption_unresolved
- old_F06_confirmed_credit_cost: null
- proposed_transport_loss_contingency_credit_max: 70
- proposed_recovery_pre_submit_minimum_live_balance: 5670
- current_active_total_submit_invocation_cap: 84
- proposed_total_submit_invocation_cap: 85
- current_active_credit_budget_max: 5880
- proposed_absolute_credit_ceiling: 5950
- proposal_active: false
- recovery_submit_authorized: false
- proposed_recovery_submit_count_max: 1
- proposed_submit_only_query_count_max: 0
- proposed_submit_only_download_count_max: 0
- fresh_live_credit_required_later: true
- historical_5695_accepted_as_live_preflight: false
- F01_F05_preserved: true
- F07_preserved: true
- Dreamina_run: false
- Dreamina_command_count: 0
- credits_consumed: 0
- media_created: false
- datasets_modified: false
- sources_clean: true
- active_hard_limits_modified: false
- macro_state: STOPPED_AUTHORITY_CLOSED
- activation_state: STOPPED_AUTHORITY_CLOSED
- execution_authority_active: false
- remaining_noncanary_tasks_authorized: false
- next_wave_id: W01
- next_experiment_id: CAL001-F06-P1-R1
- final_master: false
- locked: false

## 2. Checkpoint and authorization

Local `main`, local HEAD, and `origin/main` all matched `0273eea8895548ad46f1e23ce8ef3f0304646e94`. The index was empty, tracked files were clean, and `sources/` was clean. The six required parser-correction checkpoint files matched their supplied SHA-256 values. The exact 230-byte authorization was decoded once, matched SHA-256 `699986e09949ef45dc290010b6fd21c6f24287d252eb41c97ee7d5728472e43f`, and passed exact-token and Base64 round-trip verification.

## 3. Parser correction and quarantine verification

The centralized creation classifier, `fail_reason` preservation, orphaned prequeue-upload classification, corrected existing-record loader, and conservative duplicate guard remain present at the current HEAD. Thirty-six affected no-live tests passed. Loading the superseding F06 record returns `provider_task_created=false`, `created_task_count=0`, `query_recovery_eligible=false`, and `submit_handle_state=orphaned_after_upload_transport_failure`. The duplicate guard still rejects an ordinary submit. Any future recovery requires a separate exact human override.

## 4. Accepted hashes and remaining order

The five canonical accepted digests matched: manifest `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d`, fixture registry `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142`, Prompt inventory `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d`, package inventory `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c`, and full inventory `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138`. The accepted remaining-order hash was `783cb601ce9f33f20defadce9b37aff33698dcf492b9b71273a023e4deb0e291`. Manifest rows and unique IDs were 84/84; Prompt, package, and fixture mismatch counts were 0/0/0. No task replacement or manifest expansion occurred.

## 5. Unchanged F06 binding

`CAL001-F06-P1-R1` remains `multimodal2video`, `seedance2.0_vip`, 5 seconds, `16:9`, and `720p`, with expected counts 0 images, 1 video, 1 output and normal cost 70. Prompt SHA-256 remains `1672ee6ba29d82c844af6e4700607582410a323c24409697916b28e56a8b76f0`; package SHA-256 remains `4f0f8356b2d0c04f03f1eb6d3f403259795e24b413031c883491856d25366710`. The package, manifest, fixture-inspection evidence, and rendered command evidence agree on Fenshou, Shuangji, then scene. All three fixture hashes match. No recovery package or replacement upload asset was created.

## 6. Accounting semantics

Completed fixed technical tasks are 12: seven canaries and W01 F01-F05. Confirmed costs remain 490 canary, 350 W01, and 840 total CAL-001A. `confirmed_created_or_completed_submit_count=12`. The orphaned F06 invocation is not counted as a created provider task, but is retained in historical invocation accounting, so `historical_submit_invocation_count_including_orphan=13`. There are 72 fixed technical tasks remaining.

## 7. Budget arithmetic

- Remaining fixed tasks: `84 - 12 = 72`.
- Normal remaining task credit: `72 * 70 = 5040`.
- Base required live balance: `5040 + 560 = 5600`.
- Proposed unresolved transport-loss reserve: `70`.
- Proposed recovery pre-submit minimum: `5600 + 70 = 5670`.
- Base CAL-001A budget: `84 * 70 = 5880`.
- Proposed absolute credit ceiling: `5880 + 70 = 5950`.

The value 5670 is a design gate, not a live balance observation. The historical 5695 observation is stale and cannot satisfy a later preflight. A later submit-only phase must obtain a fresh `user_credit` result. Refunds, grants, or positive drift do not enlarge task scope.

## 8. Active versus proposed limits

Active limits remain 84 total submit invocations and 5880 credits. The proposal is `reviewed_not_activated`, with `proposal_active=false` and `recovery_submit_authorized=false`. The design proposes cap 85 solely as 84 accepted fixed-task invocations plus at most one transport-loss recovery invocation for the same fixed F06 task, with a maximum 70-credit contingency and absolute ceiling 5950. It adds no task, manifest row, replacement, batch expansion, or second recovery.

## 9. Future submit-only design and stop conditions

A future `CAL-001-P3D-W01_F06_SINGLE_RECOVERY_SUBMIT_ONLY` phase may be activated only by a separate exact human authorization. Its design permits preflight, current Dreamina canary/help, one fresh pre-submit credit check, one new F06 submit invocation, and one immediate post-submit credit check. It permits zero query, zero download, zero F07 submits, zero retries, and zero additional recovery submits.

Mandatory stops include balance below 5670; Source/hash/binding mismatch; old handle activity or duplicate-provider evidence; CLI/auth/logger failure; upload failure; missing or reused submit ID; classifier failure to prove task creation; `gen_status=fail`; missing logid; missing, nonnumeric, or non-70 credit count; non-70 immediate balance delta; or any unclassified anomaly. On stop, no query, download, retry, further submit, or F07 action is allowed.

## 10. F01-F05 and F07 preservation

F01-F05 remain technically completed and their five technical-record hashes match. Their datasets, media references, frames, contact sheets, and review records were not modified. F07 remains `pending_preflight`, with `submit_attempt_count=0`, `submit_id=null`, and no authority.

## 11. No-live proof

No Dreamina executable or command was invoked. There were no provider calls, submits, queries, downloads, retries, resubmits, credit consumption, media creation, or dataset changes. Source remained read-only and clean. Active caps and budgets were not changed. `final_master=false` and `locked=false`.

## 12. Mutable state update

The mutable state contract received only a non-active F06 recovery-readiness review block and the corresponding record-only next action. The active 84/5880 hard limits, closed macro/activation state, old-handle quarantine, F07 state, and all execution-authority flags remain unchanged. The exact next action is: `A separate exact human authorization may activate one F06 recovery submit-only phase. No Dreamina action is currently authorized.`

## 13. Files and Git result

Created: one authorization JSON, one readiness/budget review JSON, and this report. Modified: only the mutable execution-state contract. No optional design artifact was required. The authorized commit message is `docs: review CAL-001 W01 F06 recovery readiness`; the final Codex response records the resulting commit hash and push result because this report is part of that commit.

## 14. Next phase and verdict

- stop_condition: Proposal reviewed but inactive; recovery submit remains unauthorized and execution authority remains closed pending exact human reauthorization.
- recommended_next_phase: CAL-001-P3D-W01_F06_SINGLE_RECOVERY_SUBMIT_ONLY_REAUTHORIZATION_RECORD_ONLY
- final_verdict: CAL001_P3D_W01_F06_RECOVERY_READINESS_REVIEW_PASSED_PROPOSAL_INACTIVE_REQUIRES_HUMAN_REAUTHORIZATION
