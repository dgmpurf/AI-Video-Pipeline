# CAL-001 P3D W01 P1-R1 Seven-Family Bounded Live Wave Result

## Required summary fields

- executed: false
- status: `W01_stopped_authority_closed_requires_human_decision`
- starting_head: `f27c3a22636d4402d47536ccb9b8edbf6f9711ee`
- activation_verified: true
- authorization_sha256: `983ea0c8f95ef018b3171e41bc97a93235f8199796225335190f0156047e7141`
- wave_id: `W01`
- prompt_variant: `P1`
- run_id: `R1`
- planned_task_count: 7
- technically_completed_task_count: 0
- task_statuses: F01=`stopped_anomaly`; F02-F07=`pending_preflight`
- submit_count: 0
- query_count: 0
- download_count: 0
- credit_cost: 0
- initial_live_credit: 5957 at the wave canary; 6045 at the F01 immediate pre-submit check
- final_live_credit: 6045
- credit_reconciliation_pass: not applicable because no submit occurred
- runtime_version: `2a20fff-dirty`
- runtime_help_verified: true
- command_binding_verified: true
- wrapper_tests_passed: true, 13 passed
- durable_evidence_pass: true for every command that ran
- result_count_gate_pass: false, not reached
- media_validation_pass_count: 0
- review_metadata_count: 0
- frame_set_count: 0
- contact_sheet_count: 0
- dataset_rows_updated: 0
- macro_state: `STOPPED_AUTHORITY_CLOSED`
- wave_state: `stopped`
- execution_authority_active: false
- remaining_noncanary_tasks_authorized: false
- next_wave_id: `W01`
- next_experiment_id: `CAL001-F01-P1-R1`
- CAL001B_authorized: false
- automatic_visual_scoring: false
- family_winner_selected: false
- global_prompt_winner_selected: false
- final_master: false
- locked: false
- sources_clean: true
- accepted_artifacts_unchanged: true
- media_staged: false
- recommended_next_phase: `CAL-001-P3D-W01_PREFLIGHT_FALSE_POSITIVE_REVIEW_AND_REAUTHORIZATION_DECISION`
- final_verdict: `CAL001_P3D_W01_STOPPED_AUTHORITY_CLOSED_REQUIRES_HUMAN_DECISION`

## 1. Phase summary

CAL-001-P3D-W01 was activated for one strict F01-F07 P1-R1 wave. The wave stopped during the F01 fresh bounded preflight, before the durable duplicate-prevention submit transition and before any submit. No generation task, query, download, media, review artifact, technical execution record, or dataset update was created.

The stop was a local validation false positive. The F01 immediate pre-submit balance was 6045, which passed the authorized threshold of 5950. A temporary driver additionally required that value to equal the earlier wave-canary observation of 5957. That equality rule was stricter than the authorization. It raised a local anomaly after the durable credit evidence was written, and the state contract then closed remaining authority as required.

## 2. Starting checkpoint and activation verification

- branch: `main`
- local HEAD: `f27c3a22636d4402d47536ccb9b8edbf6f9711ee`
- origin/main at preflight: `f27c3a22636d4402d47536ccb9b8edbf6f9711ee`
- staged files at preflight: none
- tracked diff at preflight: none
- sources status at preflight: clean
- P3C activation state before W01: `ACTIVATED_READY`
- execution_authority_active before W01: true
- remaining_noncanary_tasks_authorized before W01: true
- exact next experiment before W01: `CAL001-F01-P1-R1`

## 3. Immutable hash verification

- activation authorization record: `983ea0c8f95ef018b3171e41bc97a93235f8199796225335190f0156047e7141`
- remaining-77 wave plan: `b67b83f62cc6b146d6aee8a770031f7365dcc66afe08a8ae6ab7a7f9996e3748`
- fixed 84-task manifest: `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d`
- fixture registry: `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142`
- Prompt inventory: `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d`
- package inventory: `b71642dba3e22a286c832d61e175bf6adb3432a82793c89a6175fe1f57a06839`
- full inventory: `44825f76c8d5518d96722628bb94b6e6524d1ad202fe9907c7459b7756f60315`
- accepted artifacts changed: false

The seven W01 manifest-row, Prompt, package, provider-Prompt payload, fixture, and fixture-order bindings matched the committed plan.

## 4. Repaired-wrapper test and durable-evidence verification

`python -m pytest tests/test_dreamina_evidence_persistence.py -q` completed with 13 passing tests. Every Dreamina command in this phase ran through `execute_with_durable_evidence` and wrote its sanitized subprocess envelope before local parsing.

The F01 pre-submit credit command has both a sanitized envelope and a separate parsed credit record. No signed URL, token, cookie, auth/session value, Prompt body, or environment content is recorded.

## 5. Runtime version/login/credit/help canary

- executable: `C:/Users/msjpurf/bin/dreamina.exe`
- version: `2a20fff-dirty`
- commit: `2a20fff`
- build_time: `2026-06-26T06:36:39Z`
- wave-canary total_credit: 5957
- required minimum: 5950
- logger Access Denied: false
- login/auth failure: false
- command exit codes: all zero
- help contracts verified: `text2video`, `image2video`, `frames2video`, `multimodal2video`, `query_result`

The first local canary parser expected legacy `--resolution`/`--model` names and did not recognize `total_credit`. Existing envelopes were reparsed without rerunning Dreamina. Current help uses `--video_resolution` and `--model_version`; the corrected canary passed.

## 6. Seven-task command-binding audit

All seven in-memory submit argv arrays passed the pre-submit audit. The audit verified exact provider Prompt payload hashes, fixture hashes and order, task-type flag rules, `--poll 0`, no output/download/session/token submit fields, model `seedance2.0_vip`, duration 5, and video resolution 720p.

F01/F06/F07 use explicit 16:9. F02/F03/F04 omit ratio. F05 omits ratio and preserves first/last order. F06/F07 each repeat exactly three `--image` bindings in package order.

## 7. F01 execution

- experiment_id: `CAL001-F01-P1-R1`
- fresh preflight started: true
- immediate pre-submit `user_credit` invoked through wrapper: true
- observed live total_credit: 6045
- required threshold: 5950
- threshold passed: true
- local extra equality check expected: 5957
- local extra equality check result: false
- duplicate-prevention submit transition written: false
- submit_attempt_count: 0
- submit invoked: false
- submit_id: null
- logid: null
- task_state: `stopped_anomaly`

Stop reason recorded in durable state: `live credit continuity anomaly: expected 5957, observed 6045`. This text describes the driver's extra check, not a Dreamina provider failure and not a threshold failure.

## 8. F02 execution

Not executed. State remains `pending_preflight`; submit/query/download counts remain zero.

## 9. F03 execution

Not executed. State remains `pending_preflight`; submit/query/download counts remain zero.

## 10. F04 execution

Not executed. State remains `pending_preflight`; submit/query/download counts remain zero.

## 11. F05 execution

Not executed. State remains `pending_preflight`; submit/query/download counts remain zero.

## 12. F06 execution

Not executed. State remains `pending_preflight`; submit/query/download counts remain zero.

## 13. F07 execution

Not executed. State remains `pending_preflight`; submit/query/download counts remain zero.

## 14. Per-task credit reconciliation

No submit occurred and no credit was charged. Provider submit credit_count and pre/post-submit delta checks are therefore not applicable. Wave credit cost is 0. The only two balance observations were 5957 at the wave canary and 6045 at the later F01 pre-submit check.

## 15. Query-count and terminal-state summary

- created submit IDs: 0
- query count: 0
- terminal provider generation states: none
- F01 terminal local state: `stopped_anomaly`
- F02-F07 state: `pending_preflight`

## 16. Download and media-validation summary

No query reached success, no download command ran, and no provider media exists for W01. Media validation was not reached.

## 17. Review-artifact summary

No review metadata, timestamp frames, final readable frame, or contact sheet was created. No visual review or visual score was performed.

## 18. Dataset updates

`CAL001_experiment_results_template.csv` and `CAL001_visual_review_template.jsonl` were not modified. Dataset row counts remain 84/84 and W01 technical rows remain unpopulated.

## 19. Resumable state update

- activation_state: `STOPPED_AUTHORITY_CLOSED`
- W01 wave_state: `stopped`
- F01 task_state: `stopped_anomaly`
- execution_authority_active: false
- remaining_noncanary_tasks_authorized: false
- next_wave_id: `W01`
- next_experiment_id: `CAL001-F01-P1-R1`
- exact next action: new human decision required

The state was not reopened after identifying the false positive because the durable stop contract had already closed authority.

## 20. Source/media/Git boundary

- sources modified or staged: false
- Prompt/package/manifest/fixture modified or staged: false
- runtime/config/auth modified: false
- generated media created: false
- media staged: false
- retry/resubmit performed: false
- CAL001B run: false
- final_master: false
- locked: false
- tag created: false

Only the updated state contract, P3D-W01 sanitized JSON/text evidence, and this report are eligible for the bounded checkpoint commit.

## 21. Stop-condition status

Stop condition is active. It occurred before submit and is classified as a local pre-submit validation false positive / unclassified local execution anomaly. The authorized balance threshold itself passed. Under the current closed state, no additional submit, query, download, retry, resubmit, replacement, family skip, or later-wave execution is permitted.

## 22. Commit and push result

- checkpoint commit message: `chore: record CAL-001 W01 preflight stop`
- commit result: performed after this report snapshot; authoritative hash is returned in the final Codex response
- push target: `origin/main`
- push result: performed after the checkpoint commit; authoritative result is returned in the final Codex response
- tag: none

## 23. Recommended next phase

`CAL-001-P3D-W01_PREFLIGHT_FALSE_POSITIVE_REVIEW_AND_REAUTHORIZATION_DECISION`

The next human decision should explicitly determine whether to reopen W01 from F01 after removing only the unauthorized equality check. A future corrected run must preserve the current no-submit evidence and must not treat the stopped preflight as a prior submit attempt.

## 24. Final verdict

`CAL001_P3D_W01_STOPPED_AUTHORITY_CLOSED_REQUIRES_HUMAN_DECISION`

---

## Resumed Run After False-Positive Correction

This section records the separately authorized resumed run. The historical stop section above is retained as provenance and was not rewritten.

- historical_report_pre_resume_sha256: 456a2b2ecbe46b0ec3de0fe3688ccb4622c2c852b98dc363ebb8e215011679d0
- historical_wave_summary_preserved: f1d3e26de3440a0d190dce6644640dc76a74aa028970af352d54dda52023ec4d
- executed: true
- status: "W01_stopped_authority_closed"
- starting_head: "bc98270a64d32ab43aef94cb9964b0181226054a"
- correction_reauthorization_verified: true
- correction_authorization_text_sha256: "482b86f6be0feadbd245916474c14058ec4b3685b8eff17446085ab04e6fef44"
- prior_P3C_authorization_text_sha256: "73ae380b9af11656660d47755da1690b8ab234afcaf99795cf1743365bdd1392"
- authorization_record_file_sha256: "983ea0c8f95ef018b3171e41bc97a93235f8199796225335190f0156047e7141"
- historical_false_positive_preserved: true
- wider_failure_gate_passed: true
- wider_failure_classification: "PRE_EXISTING_UNRELATED_NONBLOCKING_BASELINE_FAILURES"
- activation_verified: true
- wave_id: "W01"
- prompt_variant: "P1"
- run_id: "R1"
- planned_task_count: 7
- technically_completed_task_count: 5
- task_statuses: {"CAL001-F01-P1-R1": "technically_completed", "CAL001-F02-P1-R1": "technically_completed", "CAL001-F03-P1-R1": "technically_completed", "CAL001-F04-P1-R1": "technically_completed", "CAL001-F05-P1-R1": "technically_completed", "CAL001-F06-P1-R1": "terminal_failure", "CAL001-F07-P1-R1": "pending_preflight"}
- task_submit_ids: {"CAL001-F01-P1-R1": "b1f101bb-cd4d-4fea-a12f-3437a09ab443", "CAL001-F02-P1-R1": "b17148c2-952d-435b-bf37-b6cf6c05121d", "CAL001-F03-P1-R1": "3c816474-3635-40a3-963c-f620994538ab", "CAL001-F04-P1-R1": "0a2f0dc1-730b-4079-acf1-6012b8e10639", "CAL001-F05-P1-R1": "53574aa3-4123-49f5-9ea2-692f3cec63c6", "CAL001-F06-P1-R1": "cabfa6ab-cc61-4d29-8630-da01dfdeef65", "CAL001-F07-P1-R1": null}
- task_logids: {"CAL001-F01-P1-R1": "202607190233031692540470081946861", "CAL001-F02-P1-R1": "2026071902375216925404700871857AC", "CAL001-F03-P1-R1": "2026071902425016925404700800563A8", "CAL001-F04-P1-R1": "202607190247571692540470086105CF2", "CAL001-F05-P1-R1": "20260719025305169254047008188821D", "CAL001-F06-P1-R1": null, "CAL001-F07-P1-R1": null}
- per_task_credit_count: {"CAL001-F01-P1-R1": 70, "CAL001-F02-P1-R1": 70, "CAL001-F03-P1-R1": 70, "CAL001-F04-P1-R1": 70, "CAL001-F05-P1-R1": 70, "CAL001-F06-P1-R1": null, "CAL001-F07-P1-R1": null}
- per_task_credit_delta: {"CAL001-F01-P1-R1": 70, "CAL001-F02-P1-R1": 70, "CAL001-F03-P1-R1": 70, "CAL001-F04-P1-R1": 70, "CAL001-F05-P1-R1": 70, "CAL001-F06-P1-R1": null, "CAL001-F07-P1-R1": null}
- per_task_credit_drift_classification: {"CAL001-F01-P1-R1": "no_pre_submit_credit_drift", "CAL001-F02-P1-R1": "no_pre_submit_credit_drift", "CAL001-F03-P1-R1": "no_pre_submit_credit_drift", "CAL001-F04-P1-R1": "no_pre_submit_credit_drift", "CAL001-F05-P1-R1": "no_pre_submit_credit_drift", "CAL001-F06-P1-R1": "no_pre_submit_credit_drift", "CAL001-F07-P1-R1": null}
- submit_count: 6
- query_count: 10
- per_task_query_counts: {"CAL001-F01-P1-R1": 2, "CAL001-F02-P1-R1": 2, "CAL001-F03-P1-R1": 2, "CAL001-F04-P1-R1": 2, "CAL001-F05-P1-R1": 2, "CAL001-F06-P1-R1": 0, "CAL001-F07-P1-R1": 0}
- download_count: 5
- credit_cost: 350
- confirmed_credit_cost: 350
- F06_credit_consumption: "unknown_due_immediate_terminal_submit_failure"
- initial_live_credit: 6045
- final_live_credit: 5695
- credit_reconciliation_pass: false
- runtime_version: "2a20fff-dirty"
- runtime_help_verified: true
- command_binding_verified: true
- wrapper_tests_passed: true
- focused_credit_tests_passed: true
- durable_evidence_pass: true
- result_count_gate_pass: false
- media_validation_pass_count: 5
- review_metadata_count: 5
- frame_set_count: 5
- contact_sheet_count: 5
- dataset_rows_updated: 6
- technically_completed_dataset_rows_updated: 5
- terminal_failure_dataset_rows_updated: 1
- provider_task_created_count: 6
- F06_failure_classification: "upload_transport_failure"
- F06_immediate_gen_status: "fail"
- F06_fail_reason: "upload resource productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png: upload image: upload phase, no file upload, please check log for more details"
- F06_submit_failure_record_path: "experiments/CAL-001/execution_records/P3D_W01/CAL001-F06-P1-R1/resume_submit_failure_classification.json"
- F06_submit_failure_record_sha256: "aeb9b04d68016b2159fd73b9b4980b19f193a9dfebf145177cd34d3a0c3d22e2"
- F06_query_count: 0
- F06_download_count: 0
- F07_submit_count: 0
- macro_state: "STOPPED_AUTHORITY_CLOSED"
- wave_state: "stopped"
- execution_authority_active: false
- remaining_noncanary_tasks_authorized: false
- next_wave_id: "W01"
- next_experiment_id: "CAL001-F06-P1-R1"
- CAL001B_authorized: false
- automatic_visual_scoring: false
- family_winner_selected: false
- global_prompt_winner_selected: false
- final_master: false
- locked: false
- sources_clean: true
- accepted_artifacts_unchanged: true
- media_staged: false
- stop_condition: "F06 immediate submit terminal failure: upload_transport_failure; provider task created with submit_id cabfa6ab-cc61-4d29-8630-da01dfdeef65; gen_status=fail; logid absent; credit_count absent; no query, download, retry, resubmit, replacement, skip, or F07 submit authorized."
- recommended_next_phase: "NEW_HUMAN_DECISION_REQUIRED"
- final_verdict: "CAL001_P3D_W01_STOPPED_AUTHORITY_CLOSED_REQUIRES_HUMAN_DECISION"
- technical_record_paths: ["experiments/CAL-001/execution_records/P3D_W01/CAL001-F01-P1-R1_technical_execution_record.json", "experiments/CAL-001/execution_records/P3D_W01/CAL001-F02-P1-R1_technical_execution_record.json", "experiments/CAL-001/execution_records/P3D_W01/CAL001-F03-P1-R1_technical_execution_record.json", "experiments/CAL-001/execution_records/P3D_W01/CAL001-F04-P1-R1_technical_execution_record.json", "experiments/CAL-001/execution_records/P3D_W01/CAL001-F05-P1-R1_technical_execution_record.json"]

No automatic visual score, family winner, global Prompt winner, final master, or lock is asserted by this run.
