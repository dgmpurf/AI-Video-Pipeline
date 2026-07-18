# CAL-001 P3D W01 Preflight False-Positive Review, Fix, and Reauthorization Result

## Required summary fields

- executed: true
- status: `W01_false_positive_corrected_reauthorized_ready_resume_F01`
- starting_head: `7c86367a3d7ca17bb63e8ad148144b3075f4dab7`
- authorization_decision: `PASS_REVIEW_CORRECT_AND_REAUTHORIZE_W01_AFTER_LOCAL_CREDIT_CONTINUITY_FALSE_POSITIVE`
- authorization_byte_length: 5685
- authorization_text_sha256: `482b86f6be0feadbd245916474c14058ec4b3685b8eff17446085ab04e6fef44`
- authorization_base64_verified: true
- authorization_round_trip_verified: true
- historical_W01_stop_verified: true
- canonical_hashes_verified: true
- accepted_bytes_unchanged: true
- local_credit_equality_defect_found: true
- credit_continuity_validator_corrected: true
- Dreamina_run: false
- Dreamina_command_count: 0
- credits_consumed: 0
- media_created: false
- datasets_modified: false
- sources_clean: true
- historical_evidence_modified: false
- resumable_state_reopened: true
- final_master: false
- locked: false
- recommended_next_phase: `CAL-001-P3D-W01_P1_R1_SEVEN_FAMILY_BOUNDED_LIVE_WAVE_RESUME_AFTER_FALSE_POSITIVE_CORRECTION`
- final_verdict: `CAL001_P3D_W01_FALSE_POSITIVE_CORRECTED_REAUTHORIZED_READY_RESUME_F01`

## 1. Phase summary

This strictly no-live phase verified the human correction authorization, proved the historical W01 stop created no provider task or charge, reconciled all accepted P3C digests, replaced the temporary equality behavior with centralized credit-continuity semantics, added focused tests, and reopened only W01/F01 in the mutable state contract. No Dreamina command was run.

## 2. Starting checkpoint

- required branch: `main`
- local HEAD before correction: `7c86367a3d7ca17bb63e8ad148144b3075f4dab7`
- origin/main before correction: `7c86367a3d7ca17bb63e8ad148144b3075f4dab7`
- staged files before correction: none
- tracked diff before correction: none
- sources status: clean
- known untracked workspace noise was left untouched

The historical W01 report SHA-256 was exactly `456a2b2ecbe46b0ec3de0fe3688ccb4622c2c852b98dc363ebb8e215011679d0`, and its verdict was `CAL001_P3D_W01_STOPPED_AUTHORITY_CLOSED_REQUIRES_HUMAN_DECISION`.

## 3. Authorization fingerprint

The Base64 authorization was authoritatively decoded exactly once. The decoded text was UTF-8 with LF line endings, no BOM, no trailing newline, 5685 bytes, and SHA-256 `482b86f6be0feadbd245916474c14058ec4b3685b8eff17446085ab04e6fef44`. The opening, single decision token, ending, Base64 encoding check, and byte-for-byte round trip all passed.

The exact text and canonical continuous Base64 are preserved in:

`experiments/CAL-001/authorizations/CAL001_P3D_W01_false_positive_correction_reauthorization.json`

Prior bindings remain separate and unchanged:

- authorization_text_sha256: `73ae380b9af11656660d47755da1690b8ab234afcaf99795cf1743365bdd1392`
- authorization_record_file_sha256: `983ea0c8f95ef018b3171e41bc97a93235f8199796225335190f0156047e7141`
- remaining ordered-list SHA-256: `783cb601ce9f33f20defadce9b37aff33698dcf492b9b71273a023e4deb0e291`

## 4. Historical stop verification

At the historical stop:

- macro state: `STOPPED_AUTHORITY_CLOSED`
- W01 wave state: `stopped`
- F01 task state: `stopped_anomaly`
- submit/query/download counts: `0 / 0 / 0`
- credit cost: `0`
- F01 submit_attempt_count: `0`
- F01 submit_id/logid: `null / null`
- execution authority flags: false
- next wave/experiment: `W01 / CAL001-F01-P1-R1`
- final_master/locked: `false / false`

The mutable state at the starting checkpoint and the immutable stop artifacts agree on these facts.

## 5. No-submit/no-credit proof

Only the F01 pre-submit `user_credit` envelope and parsed balance record exist under the historical W01 task directory. There is no submit envelope, submit record, submit ID, log ID, query evidence, download evidence, provider media, technical execution record, or W01 dataset update. The duplicate-prevention transition was never entered, so the false-positive stop is not a submit attempt, retry, or resubmit.

Historical evidence hashes are preserved in the new authorization and correction records.

## 6. Five canonical digest recomputation

All accepted values recomputed exactly:

- fixed_manifest_sha256: `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d`
- fixture_registry_sha256: `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142`
- prompt_inventory_sha256: `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d`
- package_inventory_sha256: `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c`
- full_experiment_inventory_sha256: `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138`

Manifest rows and unique experiment IDs were `84 / 84`. Prompt, package, and fixture byte mismatch counts were `0 / 0 / 0`.

## 7. Historical inventory-hash discrepancy diagnosis

The exact canonical input set is the fixed manifest and fixture registry raw files plus the 28 unique Prompt files, 84 package files, and 6 unique fixture files selected by the accepted manifest. Referenced files were first verified against their recorded SHA-256 values.

Canonical derived inventories use:

- Prompt: `family_id|prompt_architecture|prompt_path|prompt_sha256`
- package: `experiment_id|package_path|package_sha256`
- full: `experiment_id|prompt_sha256|package_sha256|fixture_sha256s`

Lines are lexicographically sorted, paths remain repository-relative forward-slash paths exactly as recorded, bytes are UTF-8, fields use `|`, records use LF, and one final LF is present. Manifest and registry digests hash raw file bytes; inventory digests hash the derived canonical text objects.

The historical report instead wrote package `b71642dba3e22a286c832d61e175bf6adb3432a82793c89a6175fe1f57a06839` and full `44825f76c8d5518d96722628bb94b6e6524d1ad202fe9907c7459b7756f60315`.

Local operation-trace reconstruction proved the temporary driver contained no package/full inventory aggregation. These two strings first appeared as literal constants in the Markdown report creation patch. Therefore their alternate digest input file set is empty; ordering, path normalization, delimiter, newline, and raw-versus-derived rules are not applicable. The discrepancy is a report-field defect, not a different valid aggregation and not an accepted-byte change.

Classification for both: `CANONICAL_BYTES_UNCHANGED_REPORT_OR_ALGORITHM_DEFECT`.

## 8. Accepted-byte integrity decision

The five canonical values match P3C, all 84 manifest rows remain unique, and all referenced Prompt/package/fixture bytes match. The prior P3C authorization, wave plan, fixed manifest, Prompt files, packages, fixtures, inventories, and datasets were not modified.

Decision: accepted bytes unchanged; reauthorization integrity gate passed.

## 9. Local equality defect

The defect was in the deleted, temporary, untracked historical file:

`experiments/CAL-001/execution_records/P3D_W01/_cal001_p3d_w01_runtime_driver.py`

Inside `execute_task`, after `6045 >= 5950` passed, an added condition computed `expected_pre_credit = initial_credit - (order_index - 1) * 70` and required `pre_credit == expected_pre_credit`. For F01 this compared 6045 with 5957 and raised `StopCondition`.

Call path:

`main -> execute_task -> execute_dreamina(user_credit) -> durable envelope -> parse_credit -> threshold pass -> extra equality failure -> StopCondition -> close_authority`

The failure occurred before `update_state_preflight` and `update_state_submit_started`. That is why durable credit evidence exists while `submit_attempt_count` remains zero.

## 10. Corrected credit semantics

The permanent, pure local validators are now centralized in `app/ai_video_pipeline/execution/dreamina_evidence.py`:

- `validate_pre_submit_credit_continuity`
- `validate_post_submit_credit_reconciliation`

They require numeric balances and the dynamic threshold. Positive drift without an intervening CAL-001 submit passes as `positive_nonspend_credit_drift` when the threshold is met, records the drift, and never enlarges scope or budget. No drift passes when the threshold is met. Unexplained negative drift without an authorized submit stops.

After a submit, immediate pre-minus-post balance and provider `credit_count` must both equal exactly 70. Missing, nonnumeric, ambiguous, unreconciled, or non-70 evidence stops. The invariant `live_total_credit >= (84 - c) * 70 + 560` is unchanged. Durable wrapper semantics were not changed.

## 11. Field-name correction

New and future W01/P3D evidence uses two unambiguous fields:

- `authorization_text_sha256` = `73ae380b9af11656660d47755da1690b8ab234afcaf99795cf1743365bdd1392`
- `authorization_record_file_sha256` = `983ea0c8f95ef018b3171e41bc97a93235f8199796225335190f0156047e7141`

Historical report fields were not rewritten.

## 12. Focused tests

`python -m pytest tests/test_cal001_credit_continuity.py -q`

Result: 11 passed. This covers the required positive drift, below-threshold, negative drift, no-drift, exact 70 reconciliation, invalid provider charge, nonmutation, and historical zero-attempt cases. Tests use local data only and invoke no Dreamina command.

## 13. Regression tests

`python -m pytest tests/test_dreamina_evidence_persistence.py -q`

Result: 13 passed.

A bounded all-tests regression, deselecting 10 known unrelated baseline failures, passed all remaining 456 tests. A wider exploratory run confirmed those 10 baseline failures are confined to missing legacy `review_records*.jsonl`/template files and one unrelated stale production-status assertion. No out-of-scope file was created or modified to mask them.

## 14. Historical evidence preservation

The historical report, wave summary, stop record, pre-submit envelope, and parsed credit record remain byte-for-byte unchanged. The historical W01 report remains the authoritative record of why authority closed at that checkpoint; this phase adds a correction record instead of rewriting history.

Correction record:

`experiments/CAL-001/execution_records/P3D_W01_REAUTH/CAL001_P3D_W01_false_positive_correction_record.json`

Correction record SHA-256 at report creation: `c4b12d08d694e016eaabd87c909c0f8f2043e8946f476aeea777164f2597ec2b`.

## 15. State reopening

The mutable state contract now records:

- activation_state: `ACTIVATED_READY`
- macro_state: `ACTIVATED_READY`
- W01 wave_state: `pending`
- F01 task_state: `pending_preflight`
- F01 submit_attempt_count: `0`
- submit_id/logid: `null / null`
- W01 submit/query/download/credit counts: all zero
- execution_authority_active: true
- remaining_noncanary_tasks_authorized: true
- next wave/experiment: `W01 / CAL001-F01-P1-R1`
- stop_condition: `null`

F02-F07 remain `pending_preflight` with zero live counters and no submit IDs. Reopening becomes operationally effective only after this correction commit is pushed and local HEAD equals origin/main.

## 16. Reauthorized W01 scope

Authority is limited to one separately executed W01 P1-R1 bounded live-wave Goal, seven tasks in strict F01-F07 order, beginning at `CAL001-F01-P1-R1`. The static P3C wave plan and all task bindings remain unchanged.

## 17. Unauthorized scope

This phase does not authorize W02 or later waves, retry, resubmit, duplicate submit, task replacement, Prompt/package/fixture/manifest/inventory changes, Source modification, CAL001B, visual scoring, winner selection, media finalization, final master, lock, or tag.

## 18. Source/dataset/media boundary

- Dreamina commands: 0
- credits consumed: 0
- media created/downloaded/extracted: false
- datasets modified: false
- sources modified or staged: false
- accepted media staged: false

## 19. Git scope

Authorized changes are limited to the central evidence/credit validator, one focused test file, the mutable state contract, the new exact reauthorization record, the new correction record, and this report. Historical stop evidence and accepted artifacts are excluded from staging.

## 20. Commit/push result

The authorized commit message is `fix: correct CAL-001 W01 credit continuity gate`, followed by `git push origin main`. Because a report cannot contain the hash of the commit that contains itself without a self-reference loop, authoritative commit/push results are the Git history and final Codex response. Reopened authority is ineffective until commit, push, and HEAD/origin alignment all succeed.

## 21. Recommended next phase

`CAL-001-P3D-W01_P1_R1_SEVEN_FAMILY_BOUNDED_LIVE_WAVE_RESUME_AFTER_FALSE_POSITIVE_CORRECTION`

That phase must be a separately executed bounded live-wave Goal and must begin again with the full repository, Source, hash, package, Prompt, fixture, runtime, login, credit, help, command-binding, and duplicate-submit preflight.

## 22. Final verdict

`CAL001_P3D_W01_FALSE_POSITIVE_CORRECTED_REAUTHORIZED_READY_RESUME_F01`
