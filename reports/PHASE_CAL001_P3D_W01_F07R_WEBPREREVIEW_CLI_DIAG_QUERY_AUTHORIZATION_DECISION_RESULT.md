# CAL-001 F07R Query Authorization Decision Result

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_QUERY_AUTHORIZATION_DECISION`
- Experiment: `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1`
- Recorded at: `2026-07-22T10:22:29.440936Z`
- Decision: `QUERY_AUTHORIZATION_DECISION_READY_EXECUTION`
- Execution mode: no-live decision and append-only route transition

This phase performed no Dreamina or provider command. It authorizes only a future, separately authorized G2 phase with at most one exact query call.

## 2. Authorization And Repository Preflight

The canonical authorization was independently verified without persisting its text or Base64:

| Fact | Value |
| --- | --- |
| Encoding | `UTF-8` |
| Byte length | `2807` |
| SHA-256 | `65e7e6cc1e5140ca3f47b4a330bfd4ad8220424d6b157a4ef61f588d50ea36fa` |
| Derived Base64 length | `3744` |
| Decode count | `1` |
| Round trip verified | `true` |
| BOM / CR / LF / trailing space / Markdown fence | `false / false / false / false / false` |
| Last byte | `2E` |
| Repository authorization verifier | `passed` |
| Checkpoint binding | `verified` |

Required checkpoint, local HEAD, and `origin/main` were all `6a576837a36d9b879f001c6083216055a812e74f`. Branch was `main`; tracked and staged diffs were empty; `sources/` was clean; exactly one primary worktree existed.

## 3. F Submit Commit Boundary

- F commit: `6a576837a36d9b879f001c6083216055a812e74f`
- Parent: `5a8b98412b4d69019f4dc279eff49bf5f8a7b9d3`
- Commit boundary: exactly `17` added paths, zero existing tracked-file modifications
- Media added: `false`
- Query artifacts or download artifacts in F: `false`

F result report:

- Path: `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_ONE_SUBMIT_ONLY_RESULT.md`
- Byte length: `14238`
- SHA-256: `a52764978dfc4c19017d47bec27ff9f42954daf2302dc05283cfce97b9b9c77b`
- Git blob: `28d84677ca22744a179fd9ea412d65e68ec5ce90`
- Decision: `ONE_SUBMIT_EXECUTION_STRICT_TASK_CREATED_PENDING_SEPARATE_QUERY_AUTHORIZATION`

## 4. Submit Evidence Manifest Audit

- Path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit/F07R-submit-001_evidence_manifest.json`
- Independently derived byte length: `9241`
- Independently derived SHA-256: `cf09cbf1935958a0609952c69df48b5bc853c04a2cdfb3128909db5c0705e4c7`
- Git blob: `81aca4821612dbfec86c567ca46fcc08b36a3ef3`
- Strict canonical JSON: `true`
- Artifact count: `16`
- Every listed path, byte length, and SHA-256 verified: `true`
- Every listed JSON canonical on reread: `true`
- F report identity verified: `true`
- Unsanitized raw output persisted: `false`
- Available-credit values restricted to parsed credit snapshots: `true`
- Self-hash present: `false`

## 5. Strict Task Creation Proof

- Bound submit ID: `8736259f-3e91-442e-9625-ed39145fff33`
- Bound logid: `202607221746551692540470082892BEA`
- Creation classification: `confirmed_created_nonterminal`
- Provider task created: `true`
- Provider task creation proven: `true`
- Created task count: `1`
- Provider credit count: `70`
- Pre/post credit delta: `70`
- Credit reconciliation: `EXACT_70_CREDIT_RECONCILED`
- Query count before this decision: `0`
- Download count: `0`
- Second submit permitted: `false`

No available-credit balance is reproduced in this report.

## 6. Starting Route And Sequence 6

- Sequence 6 byte length: `2319`
- Sequence 6 SHA-256: `e05150d74f1e4d5550d58458e9bc137ead086e9609f20287e4f0581550f1f24b`
- Sequence 6 Git blob: `1037c7c0acd655ce4cd49b9364ab3cc1650f4b88`
- Starting state: `SUBMITTED_PENDING_SEPARATE_QUERY_AUTHORIZATION`
- Submit allowance consumed: `true`
- Submit invocation count: `1`
- Task-created count: `1`
- Credit charged total: `70`
- Query invocation count: `0`
- Query/download/retry/resubmit/batch authorities before decision: `false`
- Chain through sequence 6: `valid=true`, findings `[]`

## 7. Query Authorization Decision And Sequence 7

All READY prerequisites passed. Sequence 7 was created append-only using the accepted support contract.

- Path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-query-authorized-007_transition.json`
- Byte length: `2100`
- SHA-256: `9dd83ba21a54277188e67b1cbd2e72ae6b3d9cf8194b873f428555baa7b87592`
- Git blob: `b6e8899739f33bec4172a19d628c6aa7c0b5593a`
- Sequence number: `7`
- Current state: `QUERY_AUTHORIZED_NOT_CONSUMED`
- Query authorization decision complete: `true`
- Query authorized: `true`
- Query invocation count: `0`
- Submit invocation count: `1`
- Task-created count: `1`
- Credit charged total: `70`
- Allowance consumed: `true`
- Download/retry/resubmit/batch authorized: `false`
- Complete chain through sequence 7: `valid=true`
- Terminal state: `QUERY_AUTHORIZED_NOT_CONSUMED`
- Findings: `[]`

`execution_authority_active=false` and `provider_command_allowed=false`; this decision does not itself execute or activate G2.

## 8. Dedicated Tests

Command: `python -m pytest -q tests/test_f07r_support_contract.py`

- Collected: `201`
- Passed: `200`
- Failed: `0`
- Skipped: `1`
- Skip reason: `POSIX permission bits are not stable on Windows`

## 9. Future G2 Contract

Future phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_QUERY_ONLY`.

The only future provider argv permitted after separate exact human authorization is:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 8736259f-3e91-442e-9625-ed39145fff33
```

Future maxima:

- Query: `1`
- Provider submit: `0`
- User credit: `0`
- Download: `0`
- Retry / resubmit / batch: `0 / 0 / 0`
- F08: `0`
- Login / relogin / logout / checklogin: `0 / 0 / 0 / 0`
- Shell: `false`
- Stdin: closed
- Polling loop: none
- Second query: forbidden
- Download directory or output option: forbidden

Possible G2 terminal states are `QUERY_SUCCEEDED_AWAITING_DOWNLOAD_AUTHORIZATION`, `QUERY_NONTERMINAL_AWAITING_FRESH_QUERY_AUTHORIZATION`, `CLOSED_QUERY_TERMINAL_FAILURE`, `CLOSED_QUERY_AMBIGUOUS_RESULT`, `CLOSED_QUERY_INVOCATION_FAILURE`, and `CLOSED_QUERY_EVIDENCE_PERSISTENCE_FAILURE`.

A successful future query does not authorize download. Any signed result URL must be sanitized.

## 10. Explicit Non-Actions And Final Verdict

- Dreamina called: `false`
- Provider called: `false`
- Query/download/submit/user_credit called: `false / false / false / false`
- Retry/resubmit/batch/F08/login operations: `0`
- Existing tracked files modified: `0`
- Sources, global state, binding, route anchor, package, manifest, Prompt, media, executable, authorization history, or historical evidence changed: `false`
- Final master: `false`
- Locked: `false`

Final verdict: `QUERY_AUTHORIZATION_DECISION_READY_EXECUTION`.

Next required phase: `RETURN_TO_CHATGPT_FOR_EXACT_ONE_QUERY_EXECUTION_AUTHORIZATION`.

Do not run G2 from this decision.
