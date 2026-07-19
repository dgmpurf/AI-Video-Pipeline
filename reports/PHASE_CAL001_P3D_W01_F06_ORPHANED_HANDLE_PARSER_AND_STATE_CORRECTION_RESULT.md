# CAL-001 P3D W01 F06 Orphaned-Handle Parser and State Correction Result

## 1. Phase summary

- executed: true
- status: `F06_orphaned_handle_parser_and_state_corrected_recorded`
- starting_head: `0d3a9258cc71dc7ec37b3c95c850087ada6543e0`
- authorization_decision: `APPROVE_F06_ORPHANED_HANDLE_PARSER_AND_STATE_CORRECTION_RECORD_ONLY_PRESERVE_RAW_HISTORY_ADD_REGRESSION_TESTS_COMMIT_PUSH_NO_DREAMINA_NO_RECOVERY_SUBMIT.`
- authorization_byte_length: 153
- authorization_text_sha256: `2d02d54c289dfc0f31b652f4261593704718b4e2ff0347b2594b1bafc4f7d0c2`
- authorization_base64_verified: true
- authorization_round_trip_verified: true
- bounded_dirty_scope_verified: true
- manual_fourth_query_verified: true
- manual_fourth_query_evidence_committed: true after the authorized commit completes
- raw_submit_envelope_verified: true
- historical_parsed_record_verified: true
- parser_defect_confirmed: true
- fail_reason_parsing_added: true
- central_creation_classifier_added: true
- execute_submit_classification_corrected: true
- postprocessing_failure_classification_corrected: true
- existing_submit_loader_corrected: true
- duplicate_guard_remains_conservative: true
- orphaned_regression_case_passed: true
- normal_querying_creation_case_passed: true
- created_terminal_failure_case_passed: true
- ambiguous_failure_case_passed: true
- focused_tests_passed: true
- wrapper_tests_passed: true
- regression_tests_passed: true for the bounded affected scope
- human_web_ui_observation_recorded: true
- provider_task_created: false
- created_task_count: 0
- submit_handle_state: `orphaned_after_upload_transport_failure`
- old_submit_quarantined: true
- query_recovery_eligible: false
- continuing_query_authority: false
- duplicate_submit_forbidden: true
- recovery_submit_authorized: false
- historical_evidence_modified: false
- fourth_query_historical_report_modified: false
- fourth_query_addendum_created: true
- accepted_hashes_verified: true
- F01_F05_preserved: true
- F07_preserved: true
- Dreamina_run: false
- Dreamina_command_count: 0
- credits_consumed: 0
- media_created: false
- datasets_modified: false
- sources_clean: true
- macro_state: `STOPPED_AUTHORITY_CLOSED`
- activation_state: `STOPPED_AUTHORITY_CLOSED`
- execution_authority_active: false
- remaining_noncanary_tasks_authorized: false
- next_wave_id: `W01`
- next_experiment_id: `CAL001-F06-P1-R1`
- final_master: false
- locked: false
- stop_condition: the old F06 handle is quarantined, provider task creation is not proven, duplicate submit remains blocked, and no live authority exists
- recommended_next_phase: `CAL-001-P3D-W01_F06_RECOVERY_READINESS_AND_BUDGET_REVIEW_RECORD_ONLY`
- final_verdict: `CAL001_P3D_W01_F06_ORPHANED_HANDLE_PARSER_STATE_CORRECTED_READY_RECOVERY_READINESS_REVIEW`

## 2. Starting checkpoint and bounded dirty scope

Branch `main`, local HEAD, and `origin/main` all matched `0d3a9258cc71dc7ec37b3c95c850087ada6543e0`. The index was empty and `sources/` was clean. The only phase-owned pre-existing differences were the exact five fourth-query files plus the mutable state update. Longstanding untracked `.vs/`, old evidence, edits/review artifacts, context-recovery, and investor-report workspace noise was excluded and not modified or staged.

All five fourth-query file hashes matched the required values. The result record and historical report matched their uploaded-copy hashes. No sensitive raw log was included.

## 3. Authorization fingerprint

The canonical Base64 authorization was decoded authoritatively exactly once. UTF-8 decoding, 153-byte length, SHA-256, absence of BOM and trailing newline, exact token equality, one-token count, Base64 equality, and byte-for-byte round trip all passed.

## 4. Raw submit evidence

The raw submit envelope SHA-256 matched `5c6d24116d756b60eb706f7fdc9dddc382604e1e923bab95a588c87b3940a73c`. It records process exit 0, submit ID `cabfa6ab-cc61-4d29-8630-da01dfdeef65`, `gen_status=fail`, the Shuangji path, and `upload phase, no file upload`. Logid, queue status, and credit count are absent.

## 5. Historical parser defect

The historical parsed record SHA-256 matched `ebd2896d3d2951292ad9eaa452004cf046af665542ddfbea5df06c489d2cf3b9`. It incorrectly wrote `remote_task_creation_state=created` and `created_task_count=1` because the response contained a submit ID despite the immediate prequeue upload failure.

## 6. Human Web UI observation

The user reported manually opening the Dreamina Web UI after query #4 and seeing no corresponding F06 video or active generation task. The observation is recorded as `human_manual_web_ui_observation`, with `machine_verified=false` and `provider_api_proof=false`. It supports, but does not independently prove through an API, the orphan classification.

## 7. Centralized classifier design

One centralized classifier now separates submit invocation, handle presence, and provider task creation. It distinguishes confirmed nonterminal creation, confirmed success or terminal provider-task creation, orphaned handles after prequeue upload failure, and unresolved terminal or ambiguous creation. A submit ID alone is never sufficient to prove provider task creation.

## 8. Code changes

`parse_task_creation_evidence` now preserves `fail_reason`. Submit parsing, postprocessing-failure persistence, existing-record loading, query-recovery eligibility, and duplicate-submit metadata use the same classifier. Created-task count is no longer derived from handle presence alone.

## 9. Historical compatibility

Legacy records with `remote_task_creation_state=created` but `gen_status=fail` are reclassified from raw fields instead of blindly trusted. If fail reason and provider-task evidence are absent, classification remains unresolved. A correction record can provide a bounded `classification_evidence` overlay without rewriting legacy bytes.

Duplicate-submit blocking stays conservative for confirmed tasks, orphaned handles, and unresolved prior invocations. The correction does not silently authorize another submit.

## 10. Focused regression tests

Focused tests cover querying and success creation, orphaned upload failure including exit code 0, terminal failure with provider evidence, ambiguous failure, historical-loader compatibility, duplicate-submit blocking, postprocessing-failure classification, fail-reason parsing, and normal canary-style compatibility. All passed with fake runners and temporary files only.

## 11. Existing wrapper/regression tests

`tests/test_dreamina_evidence_persistence.py` collected 25 tests and passed. Together with `tests/test_cal001_credit_continuity.py`, 36 directly affected tests passed.

A broader repository run collected 477 tests: 467 passed and 10 unrelated legacy tests failed because old production review template/record files are absent or an old status assertion is stale. Those failures do not import the touched classifier and their required files are outside this authorization. No unrelated fix was attempted.

## 12. F06 superseding classification

F06 is now classified as:

`ORPHANED_SUBMIT_HANDLE_AFTER_PREQUEUE_UPLOAD_TRANSPORT_FAILURE_WITH_HUMAN_NO_VISIBLE_WEB_TASK_OBSERVATION`

The submit invocation and historical handle remain recorded. `provider_task_created=false`, `created_task_count=0`, and the handle is quarantined. Historical query count remains 4. Query recovery, download, retry, resubmit, and recovery submit remain unauthorized. Credit consumption remains unresolved and confirmed F06 cost remains null.

## 13. Fourth-query addendum

The addendum preserves query #4 as historical execution evidence while superseding only its task-creation interpretation. Four later `querying` responses cannot upgrade the orphaned handle into a proven provider generation task.

## 14. Raw-history preservation

The raw submit envelope, historical parsed-task record, four query envelopes and parsed results, prior result records, and every historical report remain byte-for-byte unchanged. The new correction record and addendum provide the superseding interpretation.

## 15. Mutable state correction

Only the mutable execution-state contract received the classification overlay. F06 remains `stopped_anomaly` with one historical submit invocation, the historical submit ID, four historical queries, and zero downloads. The overlay records orphan quarantine, no provider task creation, no query/download eligibility, conservative duplicate blocking, and no recovery-submit authority.

Global activation and macro state remain `STOPPED_AUTHORITY_CLOSED`; execution authority remains false.

## 16. F01-F05 preservation

F01 through F05 remain `technically_completed`. Their five technical-record SHA-256 values match the prior checkpoint. Confirmed W01 cost remains 350 and confirmed CAL-001A cost remains 840.

## 17. F07 preservation

F07 remains `pending_preflight` with submit-attempt count 0, null submit ID, query count 0, and download count 0.

## 18. No-live proof

This phase ran zero Dreamina commands. No version, credit, help, login, submit, query, download, list-task, or session operation ran. No provider/network call was made by the phase, no credits were consumed, and no media was created.

## 19. Source/dataset/media boundary

The five accepted canonical digests matched exactly: fixed manifest, fixture registry, Prompt inventory, package inventory, and full experiment inventory. All 84 manifest rows and file bindings verified with zero Prompt, package, or fixture mismatches. Sources, datasets, schemas, accepted artifacts, and media were not modified.

## 20. Files created/modified

Created: one correction authorization record, one parser/state correction record, one human Web UI observation, one fourth-query addendum, and this main report. Modified: `dreamina_evidence.py`, its focused test file, and the mutable execution-state contract. The exact five previously uncommitted fourth-query historical files are included unchanged.

## 21. Git scope

The authorized staged scope contains exactly 13 files: five historical fourth-query files, the mutable state contract, the implementation, one focused test file, and five new correction/report files. Raw submit/history evidence, prior queries, F01-F05, accepted artifacts, datasets, Source, media, sensitive logs, and unrelated workspace noise are excluded.

## 22. Commit and push result

The reserved commit message is `fix: classify Dreamina upload-failure submit handles`. Commit hash, push result, and final HEAD alignment are reported in the final Codex response after staged-name and cached-diff validation. No tag is created.

## 23. Recommended next phase

The next permissible phase is record-only:

`CAL-001-P3D-W01_F06_RECOVERY_READINESS_AND_BUDGET_REVIEW_RECORD_ONLY`

It may design a later recovery decision but must not inherit live authority from this correction.

## 24. Final verdict

`CAL001_P3D_W01_F06_ORPHANED_HANDLE_PARSER_STATE_CORRECTED_READY_RECOVERY_READINESS_REVIEW`
