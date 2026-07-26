# CAL002 Route A V0.2 C01 Query-Only Result

## 1. Actual Decision

- Decision: `CAL002_ROUTE_A_V0_2_C01_QUERY_STOPPED_HELP_CONTRACT_FAILURE`
- Query execution ID: `CAL002-ROUTE-A-V0-2-C01-QUERY-ONLY-V0-1`
- Matched-pair ID: `CAL002-ROUTE-A-V0-2-C01-MATCHED-PAIR`
- Result: stopped during Help-contract validation before either task query.

## 2. Starting Checkpoint

- Branch: `main`
- HEAD and `origin/main`: `1efbf521635b61df26bab834ce987be47f0ce6b2`
- Parent: `962ad751cef9b4a51f1aafe91c3e5ba76c3d13da`
- Commit message: `live(cal002): submit Route A V0.2 matched-pair canaries`
- Staged files: 0
- Tracked modifications: 0
- Pre-existing untracked paths: 26; preserved untouched.

## 3. Approval and Lifecycle

- Goal identity: `CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_MAX_TWO_QUERY_ONLY_V0_1`
- Approval bytes: 3005
- Approval SHA-256: `39efdf04458e6c9c692cfac6f42ff720da558bcd3e8f5b0c1b86451c0bcb1b9d`
- Authorization activated / consumed / reusable: true / true / false
- Maximum CLI calls: 3
- Authorized order: Help, PUSH query, IMPACT query
- Version, user-credit, download, retry, resubmit, batch, and R02 authority: false

## 4. Bound Live Evidence

- Live report: `reports/CAL002_RA_V02_C01_LIVE_RESULT.md`, 8320 bytes, SHA-256 `5e1062cf4fb8142467166981138ca5307046ed62a99772fdbb29834300b03d13`
- Live evidence manifest: 7193 bytes, SHA-256 `e3a0ef6c8292230ac3b088b4c425f01cf3235a0d8866df8088be00499b652b4a`
- PUSH submit receipt: 2795 bytes, SHA-256 `9ab7cbd4e184c3e02a4e4eb47f1af93c36608e5c72c2ddd9b6a57e5c261f8a81`
- IMPACT submit receipt: 2808 bytes, SHA-256 `c358190eabd6c7e03e561cda92b13e68adbf29e6c2fd0a9821e119493ff5ebc6`
- Live execution record: 2518 bytes, SHA-256 `a620e1975cba3654b39734aaf736ea16c383a72543f069687d04ab4a9e5db99a`
- PUSH submit ID: `5ff0ba35-5a2c-445a-8343-c95f31caaf4a`
- IMPACT submit ID: `4c8b6184-7c0a-4b41-95f5-e215e35f195b`
- Every committed input matched both worktree content and the starting HEAD blob.

## 5. Literal Parser Self-Test

- Tests / passes: 12 / 12
- Regex used: false
- Self-test Dreamina calls / repository writes: 0 / 0
- Parser: 14000 bytes, SHA-256 `3a6aefb22da4e704f1ce50f7871f32b11d44667c817f57ad069c3e89daaf94db`

## 6. Fresh Query Help

- Help called: true
- Argv elements / SHA-256: 3 / `df236cb901d90a36378c507ece687e0bae2f1e12dc273b3afeeac12aec8c3026`
- Start / end UTC: `2026-07-26T11:43:27.409651Z` / `2026-07-26T11:43:29.925776Z`
- Elapsed / exit / timeout: 2.515 seconds / 0 / false
- Stdout: 388 bytes, SHA-256 `74f728cc4d3ae36fb3dcf773e85ed003637c28d048d1cad77a29b59b9bd4b171`, UTF-8 PASS
- Stderr: 0 bytes, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, UTF-8 PASS
- Required literals `query_result`, `--submit_id`, and `--download_dir`: all found
- `--download_dir` optional and omitted: true
- Raw Help persisted: false

The required Help process and literal-token checks passed. Valid Help contains `--submit_id` twice, once in usage and once in its flag description. The local parser added a non-required exact-one-line condition, causing a local false positive rather than a Dreamina Help defect.

## 7. Exact CLI Calls

- Maximum / actual: 3 / 1
- Actual order: `query_result_help`
- PUSH / IMPACT query calls: 0 / 0
- No second Help call and no task query occurred after authority consumption.

## 8. PUSH Query

- Called: false
- Bound submit ID: `5ff0ba35-5a2c-445a-8343-c95f31caaf4a`
- Query argv elements / SHA-256: 4 / `26ec5f92b50f3774cf6b132629e3542b5792b54fd41c348e3eea544e71c3ed0e`
- Not-called reason: Help literal tokens all matched, but the local parser's non-required exact-one-submit-line condition rejected the valid two-line occurrence; consumed authority forbids proceeding to PUSH query.
- Response submit ID, Provider status, queue status, normalized status, and result counts: not observed
- Task terminal: not established
- Provider generation success / download ready: false / false (not established)
- Sanitization: not applicable because no query process ran

## 9. IMPACT Query

- Called: false
- Bound submit ID: `4c8b6184-7c0a-4b41-95f5-e215e35f195b`
- Query argv elements / SHA-256: 4 / `fb8451414c0fddc66f8e9a5a9bf8088bff46ba2af74a51c4f859d038b79ba11a`
- Not-called reason: PUSH query was not called because the consumed Help gate stopped on a local parser false positive; the IMPACT query gate was never reached.
- Response submit ID, Provider status, queue status, normalized status, and result counts: not observed
- Task terminal: not established
- Provider generation success / download ready: false / false (not established)
- Sanitization: not applicable because no query process ran

## 10. Decision Routing

The local aggregate Help gate was the first failure. One-time authority had already activated and was consumed, so continuing to either submit ID would violate the stop boundary. The decision is `CAL002_ROUTE_A_V0_2_C01_QUERY_STOPPED_HELP_CONTRACT_FAILURE`.

Successful / nonterminal / failed / download-ready task counts: 0 / 0 / 0 / 0. These are phase observation counts and do not classify the unqueried Provider tasks.

## 11. No-Download and No-Requery

- Download called / URL opened: false / false
- Query loop / implicit requery: false / false
- Retry / resubmit / batch / new submit: false / false / false / false
- Version / user credit: false / false

## 12. Protected State

- Media changed: false
- Sources changed: false
- Existing Prompt, package, manifest, review, submit, prior report, and protected files changed: false
- Original R02 executed / authorized: false / false
- Original R02 blocked: true

## 13. Sanitization

- Sensitive fields detected / persisted: false / false
- Raw Help / raw query output persisted: false / false
- Signed URL value persisted: false
- Only bounded identifiers, placeholders, counts, hashes, and governance metadata were retained.

## 14. Exact Write Set

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_QUERY/authorization.json`
2. `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_QUERY/runtime/query_help.json`
3. `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_QUERY/queries/push.json`
4. `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_QUERY/queries/impact.json`
5. `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_QUERY/execution.json`
6. `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_QUERY/evidence_manifest.json`
7. `reports/CAL002_RA_V02_C01_QUERY_RESULT.md`

No other repository path was created, modified, deleted, or renamed.

## 15. Governance Boundaries

- Download and retry/resubmit authorized: false
- Provider motion-only behavior verified: false
- Route A capability proven: false
- Production re-entry authorized / production approved: false / false
- Fixed-task completion / final master / locked: false / false / false
- Actual commit hash and push outcome are returned by the terminal receipt.

## 16. Next Phase

`CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_QUERY_FAILURE_HUMAN_DECISION`
