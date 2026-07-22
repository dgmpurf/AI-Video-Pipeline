# CAL-001 F07R One-Query-Only Result

## Phase Summary

- phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_QUERY_ONLY`
- execution result: `COMPLETE`
- decision: `QUERY_SUCCEEDED_AWAITING_DOWNLOAD_AUTHORIZATION`
- query outcome classification: `provider_success_download_not_authorized`
- starting checkpoint: `e6179c683a7c04afdabc0a29ef6a886b63098037`
- branch: `main`
- starting local HEAD and `origin/main` were aligned at the required checkpoint.

Exactly one authorized `query_result` invocation was executed for the existing F07R task. No submit, user-credit lookup, download, retry, resubmit, batch, F08, login, browser, or web-UI operation was executed.

## Authorization Verification

- encoding: `UTF-8`
- byte length: `2260`
- SHA-256: `043c89b0e2c872da16b8dd2438531ae68dd8a8a2df4aaec439136331e3e76606`
- locally derived Base64 character count: `3016`
- Base64 decode count: `1`
- byte-for-byte round trip: `true`
- checkpoint binding verified: `true`
- repository authorization verifier: `passed`
- BOM / CR / LF / trailing space / Markdown fence: `false`
- final byte: `2E`

## G1 And Task Binding

- G1 commit: `e6179c683a7c04afdabc0a29ef6a886b63098037`
- G1 parent: `6a576837a36d9b879f001c6083216055a812e74f`
- G1 report byte length: `6874`
- G1 report SHA-256: `b1f825ea207695753b5534ce52ebbce85ef460961382e37165fe67d85cc5fce4`
- G1 report Git blob: `dc1247e2ca73ca949ad77e8df9aed58cfcc6ec62`
- G1 decision: `QUERY_AUTHORIZATION_DECISION_READY_EXECUTION`
- starting route state: `QUERY_AUTHORIZED_NOT_CONSUMED`
- sequence 7 SHA-256: `9dd83ba21a54277188e67b1cbd2e72ae6b3d9cf8194b873f428555baa7b87592`
- sequence 7 Git blob: `b6e8899739f33bec4172a19d628c6aa7c0b5593a`
- bound submit ID: `8736259f-3e91-442e-9625-ed39145fff33`
- bound logid: `202607221746551692540470082892BEA`
- strict task creation proven: `true`
- prior submit invocation count: `1`
- prior task-created count: `1`
- reconciled task credit charge: `70`
- prior query and download counts: `0`

The dedicated support-contract test gate passed with `200 passed`, `0 failed`, and `1 skipped`. The Windows-only skip records that POSIX permission bits are not stable on Windows.

## Query Invocation Boundary

The exact four-element argv was:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 8736259f-3e91-442e-9625-ed39145fff33
```

- shell: `false`
- stdin: `closed`
- timeout: `120 seconds`
- `--download_dir` present: `false`
- automatic retry: `false`
- maximum query invocation count: `1`
- second query permitted: `false`
- command binding SHA-256: `872b406daaa8590ada65645c5684a55e72a93734a886a7e3fc7d76b7e5642785`
- exclusive claim byte length: `598`
- exclusive claim SHA-256: `f0bfed5ad617e5afadbbc7babc83a08761e2b1b5b145732d7657b5e4937e5881`
- exclusive claim Git blob: `2b831fb0131aaa3ef4fa54173b61a91d71cc28b1`
- sequence 8 SHA-256: `40f5f1450acbe893bf1a5c6cc5d3d2a98a60e1bafb51f0ac69290714bd776701`
- sequence 8 Git blob: `2f58afd02c76e0523e17d2423a593f984242406b`

## Query Result

- process started: `true`
- exit classification: `zero_exit`
- exit code: `0`
- timed out: `false`
- returned submit ID present: `true`
- returned submit ID matched: `true`
- `gen_status`: `success`
- `queue_status`: `Finish`
- fail reason present: `false`
- result structure present: `true`
- images count: `0`
- videos count: `1`
- outputs count: `1`
- expected result shape matched: `true`
- download URL present: `true`
- signed URL count: `1`
- signed URL values persisted: `false`

Nonsensitive video metadata:

- fps: `24`
- width: `1280`
- height: `720`
- format: `mp4`
- duration: `5.042 seconds`

No download was attempted or performed.

## Sanitized Evidence

- raw stdout byte count: `1821`
- raw stdout SHA-256 before decode: `aee70fc1fd624692829fee4880d9b930343bdc5bbfc0ae987d96bf1c701e8921`
- raw stderr byte count: `0`
- raw stderr SHA-256 before decode: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- stdout UTF-8 replacement events: `0`
- stderr UTF-8 replacement events: `0`
- unsanitized raw output persisted: `false`
- full result URL replacement token: `<redacted_url>`
- subprocess envelope SHA-256: `866e2cf94523ac5340321c0b134b1c2880848b3ef431916dfae9d6ac39f1b9e0`
- parsed result SHA-256: `2471b6f18be09342c889ebbb69ad50a09626689fe34ca6015486a5dd27bec5a5`

No signed URL, URL parameter, token, signature, cookie, credential, raw stdout/stderr, full Prompt, or account balance is included in this report.

## Route Transition And Authority Closure

- sequence 9 state: `QUERY_SUCCEEDED_AWAITING_DOWNLOAD_AUTHORIZATION`
- sequence 9 SHA-256: `05fb924a672cd5a36df5dbfa47b603ed9c7df2fcf4746f46d4f5af5842a8af2d`
- sequence 9 Git blob: `fb1efb7fb7221e5e40d40e6bd18e97c1156ed50c`
- complete transition chain through sequence 9 valid: `true`
- terminal state: `QUERY_SUCCEEDED_AWAITING_DOWNLOAD_AUTHORIZATION`
- chain findings: `[]`
- route closed: `false`

Post-query authority state:

- query authorized: `false`
- download authorized: `false`
- submit authorized: `false`
- retry authorized: `false`
- resubmit authorized: `false`
- batch authorized: `false`
- execution authority active: `false`
- provider command allowed: `false`
- provider eligibility: `false`
- final master: `false`
- locked: `false`

Any download requires a separate human authorization. Any later query would require a fresh human authorization.

## Operation Counters And Boundaries

- submit invocation count: `1` total, with `0` new submits in this phase
- task-created count: `1`
- query invocation count: `1`
- download invocation count: `0`
- retry / resubmit / batch invocation counts: `0 / 0 / 0`
- user-credit calls in this phase: `0`
- Dreamina called: `true`, for the one exact query only
- provider called: `true`, for the one exact query only
- media created or downloaded: `false`
- sources touched: `false`
- CAL-001 global state changed: `false`
- existing binding, package, dataset, Prompt, production/package manifest, media, executable, authorization history, and historical evidence modified: `false`

## G2 Artifacts

The bounded G2 commit contains only these new phase artifacts:

1. `query/F07R-query-001_command_binding.json`
2. `query_claims/F07R-query-001_invocation_claim.json`
3. `route_transitions/F07R-query-invocation-started-008_transition.json`
4. `evidence/F07R-query-001.subprocess_envelope.json`
5. `evidence/F07R-query-001.parsed_query_result.json`
6. `query/F07R-query-001_execution_summary.json`
7. `query/F07R-query-001_authority_closure_record.json`
8. `route_transitions/F07R-query-result-009_transition.json`
9. `query/F07R-query-001_evidence_manifest.json`
10. `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_QUERY_ONLY_RESULT.md`

No existing tracked file was modified.

## Final Verdict

`CAL001_F07R_QUERY_SUCCESS_AWAITING_SEPARATE_DOWNLOAD_AUTHORIZATION`

Next required phase: `RETURN_TO_CHATGPT_FOR_DOWNLOAD_AUTHORIZATION_DECISION`

Do not proceed to download without a new, separate human authorization.
