# CAL-001 P3B-R2-T1 Post-Submit Evidence Persistence Triage and Repair

## 1. Phase summary

- executed: true
- status: `wrapper_evidence_persistence_repaired_existing_F01_query_recovery_ready`
- phase mode: no-live engineering repair
- starting_head: `5503b24d52755dd8bdea98c28081b21e126ec37b`
- Dreamina_run: false
- submit_count: 0
- query_count: 0
- download_count: 0
- credits_consumed: 0
- accepted_CAL001_artifacts_modified: false
- sources_clean: true
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- final_master: false
- locked: false

This phase diagnosed the CAL001-F01-P2-R1 post-submit evidence loss and added a reusable, no-live-tested persistence layer for future Dreamina subprocess operations. It did not contact Dreamina or alter the historical CAL-001 evidence.

## 2. Starting checkpoint

- required branch: `main`
- observed branch: `main`
- required local/origin checkpoint: `5503b24d52755dd8bdea98c28081b21e126ec37b`
- observed local HEAD before repair: `5503b24d52755dd8bdea98c28081b21e126ec37b`
- observed `origin/main` before repair: `5503b24d52755dd8bdea98c28081b21e126ec37b`
- local/origin aligned before repair: true
- staged files before repair: none
- unrelated tracked modifications before repair: none
- `sources/` dirty or staged before repair: false

Known untracked workspace noise was left untouched and excluded from staging: `.vs/`, `productions/chi_yan_tian_qiong/edits/`, `productions/chi_yan_tian_qiong/review_artifacts/`, `reports/context_recovery/`, and `reports/investor/`.

## 3. P3B-R2 stopped-state verification

The committed source of truth remains:

`reports/PHASE_CAL001_P3B_R2_SEVEN_FAMILY_FIXED_TASK_LIVE_CANARY_EXECUTION_RESULT.md`

- report SHA256: `483a29baef25a04407e39f030d5e79544c435c4952c9a013be5b6f1abb1dad7a`
- final verdict: `CAL001_P3B_R2_SEVEN_FAMILY_LIVE_CANARY_STOPPED_NO_RETRY_NO_REMAINING_TASK_AUTHORITY`
- submit_attempt_count: 1
- created_task_count: 1
- query_only_count: 0
- download_count: 0
- completed_canary_count: 0
- observed_total_credit_delta: 70
- F02 through F07 attempted: false
- retry_count: 0
- resubmit_count: 0
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false

The report and all seven P3B-R2 technical records remain byte-for-byte unchanged.

## 4. Existing F01 remote-task evidence

Independent read of `experiments/CAL-001/execution_records/P3B_R2/CAL001-F01-P2-R1_technical_record.json` established:

| Field | Committed value |
| --- | --- |
| experiment_id | `CAL001-F01-P2-R1` |
| existing_F01_submit_created | true |
| submit_id | `4e4588dd-a0e1-4539-8390-692cb9bf80f8` |
| logid | `20260718154849169254047008489C358` |
| submit timestamp | `2026-07-18T07:48:49Z` |
| last known remote state | `querying` |
| submit response credit_count | 70 |
| pre-submit balance | 6447 |
| post-submit/final recorded balance | 6377 |
| observed credit delta | 70 |
| command type | `text2video` |
| fixture set | none |
| query count already used | 0 |
| download count already used | 0 |

Package evidence:

- path: `experiments/CAL-001/packages/F01/CAL001-F01-P2-R1_package.json`
- SHA256: `f8763f6cf62aa7893b6f0026544f5865eec5fcc6b2c288c809cdd7b5eab5e310`

Prompt evidence:

- path: `experiments/CAL-001/prompts/F01/CAL001-F01-P2_prompt.txt`
- SHA256: `e18bd22187c34bf38cd6cd8c793b0093968f94b263c12ff683987ea0d26f5368`

No later technical record claims a second submit. F02 through F07 remain unattempted. The existing remote task is not classified as failed or successful because no query evidence exists.

## 5. Missing evidence fields

The historical F01 record explicitly leaves these fields unavailable:

- Dreamina subprocess exit code
- sanitized stdout
- sanitized stderr
- stdout SHA256
- stderr SHA256
- queue status

The first five were not persisted before the local wrapper exception. `queue_status` was not returned or recovered. This phase does not reconstruct, infer, or backfill any of them.

## 6. Root cause

- root_cause_identified: true
- root_cause_summary: the one authorized Dreamina command returned and produced remote task-creation evidence, but the ephemeral CAL-001 PowerShell orchestration attempted a malformed chained `-ireplace` sanitization expression before any subprocess envelope was durably written. PowerShell then raised `The -ireplace operator allows only two elements to follow it, not 6.` The exact exception class was not durably recorded.

The failure occurred during post-command sanitization, not during Dreamina execution, parsing of a terminal result, credit reconciliation, or remote task creation. The returned output and process status necessarily existed in wrapper memory at the post-command step, but their exact values were lost when sanitization raised before persistence. The unique submit ID and non-sensitive task facts were later preserved in the committed technical record; the missing subprocess fields remain missing.

The failing CAL-001 orchestration was an ad hoc PowerShell wrapper, not a tracked repository function, so there is no historical wrapper file to edit. The repository's tracked live reference path had the same transaction-order risk: a runner returned before ordinary response recording and business-state mutation. The prior `write_json` implementation also wrote directly to its destination rather than using an atomic replace.

## 7. Affected code paths

Repair and reference integration:

- `app/ai_video_pipeline/execution/dreamina_evidence.py:238` - new shared `execute_with_durable_evidence` boundary around a runner call.
- `app/ai_video_pipeline/execution/dreamina_evidence.py:190` - same-directory temporary file, flush, fsync, and atomic replace.
- `app/ai_video_pipeline/execution/dreamina_evidence.py:84` - separate post-processing failure record.
- `app/ai_video_pipeline/execution/dreamina_evidence.py:399` - task-creation evidence parsing.
- `app/ai_video_pipeline/execution/dreamina_evidence.py:486` - read-only existing-submit recovery.
- `app/ai_video_pipeline/execution/dreamina_evidence.py:552` - duplicate-submit guard.
- `app/ai_video_pipeline/execution/dreamina_f4_live.py:270` - submit integration.
- `app/ai_video_pipeline/execution/dreamina_f4_live.py:294` - query integration.
- `app/ai_video_pipeline/execution/dreamina_f4_live.py:318` - download integration.
- `app/ai_video_pipeline/execution/recorder.py:27` - existing direct JSON writer remains for later business artifacts, now downstream of the durable envelope in the integrated path.

The provider command builder in `app/ai_video_pipeline/providers/dreamina_cli.py` is not responsible for subprocess evidence persistence and was not changed.

## 8. Risk of recurrence

Before repair, the failure class could recur after submit, query, or download whenever sanitization, parsing, serialization, path handling, reconciliation, dataset mutation, or later validation raised before the response was safely recorded. Evidence persistence and business validation effectively formed one non-atomic transaction. That could erase the local distinction between:

- no command result returned; and
- a command result returned, a remote task may exist, but local post-processing failed.

The new boundary persists the sanitized subprocess envelope before parsing or business mutation. A separate failure-state record preserves the second condition. Returned query and download operations are also counted before downstream post-processing.

## 9. Repair design

- wrapper_repair_applied: true
- durable_subprocess_envelope_added: true
- atomic_evidence_write_added: true
- postprocessing_failure_preserves_task_evidence: true
- sanitization_verified: true
- recovery_read_path_added: true

### Durable envelope

After a runner returns, the shared layer sanitizes and atomically persists:

- operation and experiment IDs
- command and operation type
- start and completion timestamps
- subprocess exit code
- sanitized stdout and stderr
- SHA256 of the sanitized streams
- command structure with Prompt bodies and secrets redacted
- evidence persistence timestamp

This happens before parsing, reconciliation, dataset mutation, or later validation.

### Atomic write

JSON evidence is written to a temporary file in the destination directory, flushed, fsynced where supported, and installed with `os.replace`. Interrupted replacement leaves no valid-looking partial target and preserves an existing valid target.

### Post-processing failure state

The guard writes a separate atomic record with:

- `remote_task_creation_state=created_or_possible_created` when a submit ID is present or a successful submit return may have created a task
- `local_postprocessing_status=failed`
- failure stage and sanitized exception text
- parsed submit ID, log ID, status, queue status, and credit count when available
- submit/query/download/retry/resubmit counters reflecting the operation already returned

### Parsed task evidence

For submit operations, parsed task evidence is persisted separately immediately after the envelope. It does not depend on later dataset or reconciliation writes.

### Sanitization

The implementation redacts Prompt bodies, token/API-key/secret/session fields, cookies, Authorization headers, signed or other HTTP(S) URLs, sensitive command arguments, and explicit caller-supplied secret values. It preserves submit ID, log ID, numeric credit count, generation status, queue status, exit code, and non-sensitive error text.

### Existing-submit recovery

The read-only loader accepts an existing JSON record and returns experiment ID, submit ID, log ID, last known state, recorded cost, used query/download counts, duplicate-submit status, and query-recovery eligibility. It never invokes a subprocess. The pre-subprocess guard raises `DuplicateSubmitForbidden` before runner invocation for an experiment with an existing created submit.

## 10. Files changed

- added `app/ai_video_pipeline/execution/dreamina_evidence.py`
- modified `app/ai_video_pipeline/execution/dreamina_f4_live.py`
- added `tests/test_dreamina_evidence_persistence.py`
- modified `tests/test_phase_f4.py`
- added `reports/PHASE_CAL001_P3B_R2_T1_POST_SUBMIT_EVIDENCE_PERSISTENCE_TRIAGE_AND_REPAIR_NO_LIVE_RESULT.md`

No other tracked path was changed.

## 11. Focused tests

Command:

```text
python -m pytest tests/test_dreamina_evidence_persistence.py tests/test_phase_f4.py -q
```

Result: `26 passed`.

The evidence module contributes 13 passing cases, including two parameterized query/download counter cases. The F4 reference path contributes 13 passing tests. Coverage includes:

1. successful return, parsing, envelope, and parsed evidence;
2. post-processing failure after task creation;
3. interrupted atomic replace with no partial target;
4. interrupted replace preserving an existing valid record;
5. sanitization and operational-field preservation;
6. duplicate-submit block before runner invocation;
7. read-only F01 recovery with subprocess invocation forbidden;
8. explicit F01 duplicate-submit rejection;
9. pre-result runner failure distinguished from post-creation failure;
10. dataset mutation failure preserving the envelope;
11. returned query/download operation counters preserved before later failure;
12. caller-supplied secret values redacted from later failure records; and
13. F4 submit envelope present before query invocation.

- focused_tests_pass: true
- Dreamina invoked by tests: false

## 12. Regression tests

Command:

```text
python -m pytest tests/test_phase_g2.py tests/test_phase_f6.py tests/test_phase_h2.py tests/test_phase_h4.py -q
```

Result: `47 passed`.

These focused adjacent suites verify that unrelated submit/query/download authorization gates remain unchanged.

- regression_tests_pass: true
- unnecessarily broad full suite run: false

## 13. Existing-submit duplicate-prevention result

- duplicate_submit_forbidden: true
- existing F01 record loaded read-only: true
- runner invocation attempted by duplicate-guard test: false
- retry allowed: false
- resubmit allowed: false
- replacement task allowed: false

The guard rejected another submit for `CAL001-F01-P2-R1` using the committed submit ID before any subprocess callback could run.

## 14. Query-recovery eligibility

- query_recovery_eligible: true
- basis: unique non-empty submit ID, last known state `querying`, existing query count 0, existing download count 0
- recovery operation performed in T1: false
- separate human authorization required: true
- automatic query added: false

Eligibility is a local routing conclusion only. It does not claim remote success, remote failure, or terminal state.

## 15. Existing submit_id and logid

- existing_F01_submit_id_available: true
- existing_F01_submit_id: `4e4588dd-a0e1-4539-8390-692cb9bf80f8`
- existing_F01_logid_available: true
- existing_F01_logid: `20260718154849169254047008489C358`
- existing_F01_last_known_remote_state: `querying`
- existing_F01_recorded_cost: 70

## 16. Current query/download counters

Historical F01 counters remain:

- existing_F01_query_count: 0
- existing_F01_download_count: 0
- existing_F01_retry_count: 0
- existing_F01_resubmit_count: 0

T1 counters are independently:

- submit_count: 0
- query_count: 0
- download_count: 0
- credits_consumed: 0

## 17. CAL-001 immutable-artifact verification

Direct SHA256 verification after repair:

| Artifact | SHA256 | Match/preserved |
| --- | --- | --- |
| fixed 84-task manifest | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` | true |
| fixture registry | `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142` | true |
| H1 acceptance record | `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7` | true |
| human checklist | `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3` | true |
| P3B-R2 authorization record | `3a298fec89baef96f36a3810897164033d55bfdfc20202399010a350e1d6b33d` | true |
| P3B-R2 report | `483a29baef25a04407e39f030d5e79544c435c4952c9a013be5b6f1abb1dad7a` | true |
| F01 technical record | `37f822b78bac71d39111a551ea16a5945cc33ff031ee0e8b0294cf7de227fed5` | true |

The six unattempted technical-record hashes also remain unchanged:

- F02: `2eadd5591f524bcaf571d3e20134003434ecba74f98e22968a3bac1831a38e51`
- F03: `6530536ab4e6b2198aaaf0ee6bb9c4c2624abac4930fac4d6464f7358a12cd20`
- F04: `07c9cd7127239e32d15ee692fa617c8bf7576dc671840549e894df52455df551`
- F05: `7297ecbe48a504ef25c34207a5eaaea9919171379e2cec7b7fe3da59580a5e37`
- F06: `dcd473d6269f09fa86701c6bd5f9914e7f50a1c375b158e27252f40dec9a2635`
- F07: `fb7c447c1982b71a23fbcc13d9272c828faa9622440a29647dcf95ff424279a7`

Accepted aggregate digest values remain unchanged because no manifest, fixture, Prompt, package, schema, matrix, budget, README, checklist, acceptance record, dataset, or historical execution record differs from the starting Git checkpoint:

- prompt_inventory_sha256: `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d`
- package_inventory_sha256: `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c`
- full_experiment_inventory_sha256: `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138`

`git diff` and `git diff --cached` over `experiments/CAL-001/`, the prior P3A/P3B-R2 reports, and `sources/` were empty.

## 18. Source governance

- sources read for mutation: false
- sources modified: false
- sources staged: false
- sources clean: true

Official Project Source remains controlled by the human user.

## 19. Explicit non-actions

- Dreamina version/user_credit/help run: false
- Dreamina generation run: false
- submit: false
- query existing F01 task: false
- download: false
- retry: false
- resubmit: false
- replacement F01 task: false
- F02-F07 attempted: false
- media created or modified: false
- visual scores assigned: false
- accepted CAL-001 artifacts modified: false
- historical technical evidence amended: false
- Source modified: false
- remaining task authority activated: false
- final_master set true: false
- locked set true: false
- tag created: false

## 20. Recommended next phase

`CAL-001-P3B-R2-T2_EXISTING_F01_QUERY_DOWNLOAD_RECOVERY_AUTHORIZATION`

That phase is an authorization decision only. Any live query and any later download must remain separately bounded by explicit human authorization. This T1 report grants no live execution authority.

## 21. Final verdict

- status: `wrapper_evidence_persistence_repaired_existing_F01_query_recovery_ready`
- final_verdict: `CAL001_P3B_R2_WRAPPER_REPAIRED_EXISTING_F01_READY_BOUNDED_QUERY_RECOVERY_AUTHORIZATION`
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- no Dreamina: confirmed
- no retry: confirmed
- no resubmit: confirmed
