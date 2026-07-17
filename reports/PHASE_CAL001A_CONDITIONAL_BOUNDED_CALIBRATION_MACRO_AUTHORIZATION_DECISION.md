# PHASE CAL-001A - Conditional Bounded Calibration Macro Authorization Decision

## 1. Phase summary

This phase records the user's conditional pre-authorization for a future bounded CAL-001A calibration macro. It does not activate or execute that macro.

- phase_id: CAL-001A
- operation: report-only authorization record
- authorization_recorded: true
- authorization_language: English
- authorization_type: conditional_pre_authorization
- execution_authority_active: false
- macro_execution_allowed_in_this_phase: false
- fixed_manifest_task_count_authorized: 84
- fixed_manifest_exists: false
- fixed_manifest_human_reviewed: false
- submit_count: 0
- query_count: 0
- download_count: 0
- retry_count: 0
- resubmit_count: 0
- batch_count: 0
- media_created: false
- sources_modified: false
- final_master: false
- locked: false

The fixed 84-task manifest was not found in the repository and no human-review acceptance evidence was found. The conditional authorization therefore remains inactive.

## 2. User English-authorization preference

The user requires all future formal authorization texts to use English. The English text in Section 3 is the canonical semantic-equivalent authorization for CAL-001A.

- formal_authorization_language_preference: English
- canonical_authorization_language: English
- Chinese authorization superseded for formal recording: true

## 3. Canonical English authorization text

```text
I authorize CAL-001A to execute a bounded calibration macro against the fixed manifest for the project-wide Prompt Calibration Sprint after that manifest has passed human review.

The authorization scope is limited to the 84 experiment tasks explicitly listed in the manifest.

Allowed:
1. Execute one submit per task.
2. For each successfully created submit_id, execute up to 3 bounded queries and stop immediately on success or fail.
3. Download once only when gen_status=success and the returned result count matches the manifest.
4. Generate basic metadata, review frames, contact sheets, and structured experiment reports.
5. Update the CAL-001 experiment dataset and reports.

Hard limits:
- submit_count_max=84;
- retry_count_max=0;
- resubmit_count_max=0;
- batch_expansion=false;
- credit_budget_max=5880;
- credit_floor=560;
- no automatic addition of manifest tasks;
- no automatic prompt rewriting or resubmission after failure;
- no modification of sources/;
- no generated media committed to Git;
- final_master=false;
- locked=false.

Stop conditions:
- sources/ is modified or staged;
- any prompt/package/manifest hash mismatch;
- Dreamina command contract changes;
- actual per-task cost exceeds the approved cost;
- 3 consecutive submits fail to create a task;
- returned result count does not match the manifest;
- remaining credits fall below credit_floor;
- any unclassified login, upload, provider, or safety-boundary anomaly occurs.

Stop immediately after all 84 fixed experiments are completed. Remaining credits and newly claimed daily credits may only be used under a separate CAL-001B adaptive follow-up authorization.
```

## 4. Base64 and SHA256 verification

The supplied Base64 payload was decoded directly as UTF-8 bytes and independently hashed.

- decoded_byte_count: 1647
- decoded_character_count: 1647
- UTF-8 Base64 round-trip: pass
- decoded text begins with `I authorize CAL-001A`: true
- expected_sha256: `63c06ede96a1a0ff708d8dc21c469675f6edea55ba356c20693ce165c4621705`
- actual_sha256: `63c06ede96a1a0ff708d8dc21c469675f6edea55ba356c20693ce165c4621705`
- canonical_authorization_sha256_match: true

Required decoded markers were all present:

- `84 experiment tasks`
- `submit_count_max=84`
- `retry_count_max=0`
- `resubmit_count_max=0`
- `batch_expansion=false`
- `credit_budget_max=5880`
- `credit_floor=560`
- `no modification of sources/`
- `no generated media committed to Git`
- `final_master=false`
- `locked=false`
- `separate CAL-001B adaptive follow-up authorization`

## 5. Authorization interpretation

The authorization is valid as a recorded conditional pre-authorization. It does not grant current Dreamina, submit, query, download, artifact-generation, package-generation, manifest-generation, or dataset-generation authority.

The authorization may activate only after every condition in Section 10 passes independently and the activation state is recorded. CAL-001B is outside this authorization and requires a separate English authorization.

## 6. Conditional versus active state

| State | Value | Meaning |
| --- | --- | --- |
| authorization_recorded | true | The user's bounded future scope is preserved. |
| authorization_type | conditional_pre_authorization | Permission is contingent on later evidence. |
| execution_authority_active | false | No external or local execution action is permitted now. |
| fixed_manifest_exists | false | No CAL-001 fixed 84-task manifest was found. |
| fixed_manifest_human_reviewed | false | No human manifest-acceptance evidence was found. |
| fixed_manifest_task_count_authorized | 84 | Future scope may contain exactly 84 reviewed rows. |
| fixed_manifest_task_count_verified | 0 | No manifest rows exist to verify in this phase. |

Until activation, all execution and artifact counts remain zero.

## 7. Current credit and budget arithmetic

- user_reported_current_credits: 6447
- evidence_class: user-reported planning evidence only
- credit_budget_max: 5880
- credit_floor: 560
- budget_plus_floor: 6440
- residual_at_user_reported_balance: 7
- live_credit_canary_run_in_this_phase: false

K270M recorded a 70-credit charge for one 5-second, 720p, `seedance2.0_vip` multimodal-to-video task. That historical result does not establish a universal 70-credit CAL-001 task cost because the future manifest may contain different task shapes. Activation requires a fresh command-contract, account, live-credit, and per-task cost canary.

## 8. Fixed macro limits

- fixed_manifest_task_count: 84
- submit_count_max: 84
- query_count_max_per_created_submit_id: 3
- download_count_max_per_successful_matching_task: 1
- retry_count_max: 0
- resubmit_count_max: 0
- batch_expansion: false
- credit_budget_max: 5880
- credit_floor: 560
- automatic_prompt_rewrite: false
- automatic_manifest_expansion: false
- sources_modified: false
- generated_media_committed_to_git: false
- final_master: false
- locked: false

One submit is allowed per fixed task only after activation. Each created `submit_id` may receive at most three queries, stopping immediately on `success` or `fail`. Download is allowed once only after `gen_status=success` and exact result-count agreement with the manifest.

## 9. Stop conditions

After activation, the macro must stop before its next external action when any of the following is detected:

1. `sources/` is modified or staged.
2. Any prompt, package, or manifest hash differs from the approved record.
3. The Dreamina command contract changes.
4. Actual per-task cost exceeds the approved cost.
5. Three consecutive submits fail to create a task; stop after the third failure.
6. Returned result count differs from the manifest; stop the task and macro before download.
7. Remaining credits fall below `credit_floor`; perform no further submit or download.
8. An unclassified login, upload, provider, or safety-boundary anomaly occurs.
9. All 84 fixed experiments are complete.

Unclassified anomalies require human triage and must not be automatically normalized. Remaining or newly claimed credits cannot be used for adaptive follow-up without separate CAL-001B authorization.

## 10. Activation preconditions

Every item below must pass and be recorded before `execution_authority_active` can become true:

1. A fixed manifest exists.
2. The manifest contains exactly 84 task rows.
3. Every row has a stable `experiment_id`.
4. Every row identifies its prompt, package, task type, model, duration, ratio, resolution, reference inputs, and expected output count.
5. Prompt, package, and manifest hashes are recorded.
6. The experiment dataset schema and scoring schema exist.
7. An independent package, budget, permission, and stop-condition review passes.
8. The user performs or explicitly accepts human review of the fixed manifest.
9. Project Source remains clean.
10. The worktree has no unexpected tracked or staged changes.
11. Dreamina command-contract and login/account canaries pass in a separately authorized phase.
12. Projected approved maximum cost plus `credit_floor` does not exceed the live credit balance.
13. No unresolved provider, upload, login, safety, or result-count anomaly remains.

Current activation result: failed closed because the fixed manifest and its human review do not yet exist.

## 11. Current forbidden actions

This phase forbids:

- Dreamina execution, including version, user-credit, help, submit, query, download, retry, resubmit, list, or batch commands
- CAL-001A or CAL-001B execution
- creation of the 84-task manifest
- creation of calibration packages
- creation of the experiment dataset or scoring dataset
- prompt, package, or manifest modification
- review-frame, contact-sheet, metadata, or media creation
- Source creation, modification, deletion, movement, staging, commit, or push
- generated-media commit
- `final_master=true`
- `locked=true`
- tag creation

Current counters:

- submit_count: 0
- query_count: 0
- download_count: 0
- review_frame_count: 0
- contact_sheet_count: 0

## 12. Source governance

Official Project Source remains controlled only by the human user. Codex used `sources/` as read-only context and did not create, edit, delete, rename, move, stage, commit, or push any Source file.

The uploaded cross-project calibration pack, if later made available, is external adaptation input and is not official Project Source. No such repository file was available in this phase.

## 13. Git/source preflight

Preflight result: pass.

- branch: `main`
- upstream: `origin/main`
- branch relation before report creation: synchronized
- `git status --short -- sources/`: clean
- tracked working-tree diff before report creation: none
- staged diff before report creation: none
- unrelated tracked changes: none
- unrelated staged changes: none
- sources_clean: true

Untracked workspace entries observed and excluded from this phase:

- `.vs/`
- `productions/chi_yan_tian_qiong/edits/`
- `productions/chi_yan_tian_qiong/review_artifacts/`
- `reports/context_recovery/`
- `reports/investor/`

## 14. Files read

Project Source, read-only:

- `sources/AI视频制作_Source索引与使用优先级_V1.10.md`
- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/dreamina_cli_help_latest.md`
- `sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`

Prior gated-execution evidence:

- `reports/PHASE_K270M_SHOT04_R02A2_B3_SAFE_REVISION_ONE_SUBMIT_RESULT.md`
- `reports/PHASE_K270O_SHOT04_R02A2_B3_SAFE_REVISION_QUERY_ONLY_RESULT.md`
- `reports/PHASE_K270Q_SHOT04_R02A2_B3_SAFE_REVISION_DOWNLOAD_ONLY_RESULT.md`

Authorization input:

- user-provided CAL-001A instruction attachment in the current conversation

Unavailable input:

- `Cross_Project_Mode_Selection_Calibration_2026-07-09.md` was not found in repository context and was not read.

## 15. Safety flags

- report_only: true
- conditional_pre_authorization_only: true
- execution_authority_active: false
- no_dreamina: true
- no_submit: true
- no_query: true
- no_download: true
- no_retry: true
- no_resubmit: true
- no_batch: true
- no_manifest_created: true
- no_package_created: true
- no_dataset_created: true
- no_media_created: true
- no_sources_modified: true
- no_existing_prompt_package_manifest_modified: true
- no_generated_media_committed: true
- final_master: false
- locked: false

## 16. Recommended preparation sequence

1. Generate and review the AI-video GPT-5.6 mode-routing Source candidates outside Codex Source write authority.
2. Run `CAL-001-P1_PROJECT_WIDE_PROMPT_CALIBRATION_NO_RUN_MANIFEST_AND_SCHEMA_CREATION` to create the no-run 84-task manifest, packages, dataset schema, scoring schema, and budget plan.
3. Run CAL-001-P2 as an independent read-only manifest, package, budget, permission, and stop-condition review.
4. Obtain explicit human acceptance of the fixed manifest.
5. Run CAL-001-P3 as the activation-precondition audit.
6. Execute CAL-001A only if every precondition passes and activation is recorded.
7. Require a separate English authorization for any CAL-001B adaptive follow-up.

## 17. Recommended next phase

`CAL-001-P1_PROJECT_WIDE_PROMPT_CALIBRATION_NO_RUN_MANIFEST_AND_SCHEMA_CREATION`

This next phase is preparation-only. It does not inherit live Dreamina execution authority from this report.

## 18. Final verdict

`CAL001A_CONDITIONAL_BOUNDED_MACRO_AUTHORIZATION_RECORDED_INACTIVE_PENDING_FIXED_MANIFEST_REVIEW`
