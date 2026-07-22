# CAL-001 F07R Download Authorization Decision Result

## Phase Summary

- phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_AUTHORIZATION_DECISION`
- phase type: no-live decision and append-only route transition
- execution result: `COMPLETE`
- decision: `DOWNLOAD_AUTHORIZATION_DECISION_READY_EXECUTION`
- starting HEAD: `821140f93bdd37302b685c0c6186e090de1f8bf9`
- branch: `main`

This H1 phase records download authorization readiness only. It does not execute the future H2 download command. H2 requires a separate, fresh, exact human authorization.

## Authorization Verification

- authority source: exact canonical authorization text supplied by the human
- encoding: `UTF-8`
- byte length: `3087`
- SHA-256: `e3c62cafe40a9928d7182bbb0623df7787f31b86c95449370ca40f2581ffa005`
- locally derived Base64 character count: `4116`
- Base64 decode count: `1`
- byte-for-byte round trip verified: `true`
- repository authorization verifier: `passed`
- checkpoint binding verified: `true`
- BOM / CR / LF / trailing space / Markdown fence: `false`
- last byte: `2E`

The canonical authorization line and its Base64 value are not persisted in this report.

## Repository And G2 Boundary

- repository root verified: `true`
- branch verified as `main`: `true`
- local HEAD / `origin/main` / required checkpoint aligned: `true`
- G2 commit: `821140f93bdd37302b685c0c6186e090de1f8bf9`
- G2 parent: `e6179c683a7c04afdabc0a29ef6a886b63098037`
- G2 commit boundary: exactly 10 added paths and zero existing tracked-file modifications
- staged files before H1: `0`
- unexpected tracked modifications before H1: `0`
- `sources/` clean: `true`
- primary worktree count: `1`
- unrelated untracked workspace noise touched: `false`
- H1 output paths absent before creation: `true`
- F07R downloaded-media directory absent: `true`

## G2 Result Binding

G2 report:

- path: `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_QUERY_ONLY_RESULT.md`
- byte length: `6977`
- SHA-256: `0d060c13a76ca1e545b6fd554c2e4aeaa450f4f203dd9e4d8eba659bc0de61e1`
- Git blob: `f71c91b01a5b5512423e6cbf9986dcdb574c81db`
- decision: `QUERY_SUCCEEDED_AWAITING_DOWNLOAD_AUTHORIZATION`
- query outcome: `provider_success_download_not_authorized`

Bound result:

- submit ID: `8736259f-3e91-442e-9625-ed39145fff33`
- `gen_status`: `success`
- `queue_status`: `Finish`
- fail reason absent: `true`
- images count: `0`
- videos count: `1`
- outputs count: `1`
- download URL present: `true`
- signed URL count: `1`
- signed URL values persisted: `false`
- media downloaded: `false`
- video metadata: `1280x720`, `24 fps`, `mp4`, `5.042 seconds`

No signed URL or raw provider output is included in this report.

## Query Evidence Manifest

- path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/query/F07R-query-001_evidence_manifest.json`
- byte length: `3518`
- SHA-256: `618443559429bd41a05af150f0ee7da92e7bbb22ac68661e6f90ca03063eb4f4`
- Git blob: `4ed53239306bb4f7386bd9649bd3d73d476d4322`
- schema: `CAL001_F07R_QUERY_EVIDENCE_MANIFEST_V1`
- record type: `CAL001_F07R_QUERY_EVIDENCE_MANIFEST`
- listed artifacts: `9`
- expected G2 files including manifest: `10`
- all listed paths, byte lengths, and SHA-256 values independently verified: `true`
- self hash included: `false`
- signed URL values persisted: `false`
- unsanitized raw output persisted: `false`
- media downloaded: `false`

## Sequence 9 And Starting Route

- sequence 9 byte length: `2345`
- sequence 9 SHA-256: `05fb924a672cd5a36df5dbfa47b603ed9c7df2fcf4746f46d4f5af5842a8af2d`
- sequence 9 Git blob: `fb1efb7fb7221e5e40d40e6bd18e97c1156ed50c`
- sequence number: `9`
- starting route state: `QUERY_SUCCEEDED_AWAITING_DOWNLOAD_AUTHORIZATION`
- complete route chain through sequence 9 valid: `true`
- sequence 9 terminal state matched: `true`
- sequence 9 findings: `[]`
- all live authorities before H1: `false`

Preserved counters before and after H1:

- provider submit invocation count: `1`
- task-created count: `1`
- credit charged total: `70`
- query invocation count: `1`
- download invocation count: `0`
- retry / resubmit / batch invocation counts: `0 / 0 / 0`
- submit allowance consumed: `true`

## Download Authorization Decision

Every G2 identity, result-shape, manifest, route-chain, sensitive-data, repository, and no-media check passed. The decision is therefore:

`DOWNLOAD_AUTHORIZATION_DECISION_READY_EXECUTION`

This decision permits only a separately authorized future H2 phase. It does not activate execution authority in H1.

## Sequence 10

- path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-download-authorized-010_transition.json`
- byte length: `2164`
- SHA-256: `cc0920546fec92fc9e4a3c834a1f15d21f4e661ab049335c5c4fcf592d169f32`
- Git blob: `4ca9e341dff82f83891640de409a743ed4ec7be3`
- sequence number: `10`
- predecessor: exact sequence 9 path and SHA-256
- current state: `DOWNLOAD_AUTHORIZED_NOT_CONSUMED`
- download authorization decision complete: `true`
- download authorized: `true`
- download invocation count: `0`
- execution authority active: `false`
- provider command allowed: `false`
- submit / query / retry / resubmit / batch authorities: `false`
- provider eligibility: `false`
- final master: `false`
- locked: `false`
- complete route chain through sequence 10 valid: `true`
- terminal state: `DOWNLOAD_AUTHORIZED_NOT_CONSUMED`
- findings: `[]`

## Future H2 Contract

- future phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_ONLY`
- separate fresh human authorization required: `true`
- maximum download invocation count: `1`
- provider submit maximum: `0`
- query-only maximum: `0`
- user-credit maximum: `0`
- retry / resubmit / batch / F08 maxima: `0`
- login / relogin / logout / checklogin maxima: `0`
- automatic retry: `false`
- second download: `false`
- overwrite: `false`
- polling loop: `false`

The only future H2 provider argv is bound as text, not executed in H1:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 8736259f-3e91-442e-9625-ed39145fff33 --download_dir G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/experiments/CAL-001/runs/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1
```

This future command is classified as one download operation, not a query-only operation.

Future bound final media path:

`experiments/CAL-001/runs/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_result.mp4`

H2 must require exactly one new MP4, no overwrite, exact byte length and SHA-256, read-only ffprobe validation, technical media evidence, local review artifacts, and human visual-review handoff. H2 success may enter `DOWNLOAD_SUCCEEDED_AWAITING_HUMAN_REVIEW` but may not set final, lock, or fixed-task completion.

## Tests And Explicit Non-Actions

- dedicated command: `python -m pytest -q tests/test_f07r_support_contract.py`
- collected: `201`
- passed: `200`
- failed: `0`
- skipped: `1`
- skip reason: POSIX permission bits are not stable on Windows
- Dreamina called: `false`
- provider called: `false`
- query called: `false`
- download called: `false`
- submit called: `false`
- user-credit called: `false`
- media created or modified: `false`
- existing sources, global state, route anchor, binding, package, production manifest, Prompt, executable, authorization history, and historical evidence modified: `false`

## H1 File Boundary

Exactly two new files belong to this H1 phase:

1. `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_AUTHORIZATION_DECISION_RESULT.md`
2. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-download-authorized-010_transition.json`

No existing tracked file was modified.

## Final Verdict

`CAL001_F07R_DOWNLOAD_AUTHORIZATION_DECISION_READY_H2_AUTHORIZATION_REQUIRED`

Next required phase: `RETURN_TO_CHATGPT_FOR_EXACT_ONE_DOWNLOAD_EXECUTION_AUTHORIZATION`

Do not execute H2 without a new, separate human authorization.
