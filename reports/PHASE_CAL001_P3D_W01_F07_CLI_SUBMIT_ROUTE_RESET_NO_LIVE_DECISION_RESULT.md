# CAL-001 P3D W01 F07 CLI Submit Route-Reset No-Live Decision Result

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07_CLI_SUBMIT_ROUTE_RESET_NO_LIVE_DECISION`
- Decision status: `COMPLETE`
- Starting checkpoint: `cb413bc53ff7f05585d556377a9ba813ab3495ff`
- Repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- Branch: `main`
- Scope: committed-evidence analysis and one report only
- Execution authority active: `false`
- Provider command allowed: `false`
- Final master: `false`
- Locked: `false`

The original `CAL001-F07-P1-R1` CLI submit route remains closed. This decision does not authorize a third submit, a query, a download, a provider call, an executable change, a network change, or a media change.

## 2. Canonical Authorization Verification

Canonical human authorization, treated as one continuous UTF-8 string:

```text
APPROVE_CAL001_P3D_W01_F07_CLI_SUBMIT_ROUTE_RESET_NO_LIVE_DECISION_BIND_STARTING_HEAD_CB413BC53FF7F05585D556377A9BA813AB3495FF_AUTHORIZE_READ_ONLY_AUDIT_OF_COMMITTED_F07_FIRST_AND_RECOVERY_SUBMIT_ENVELOPES_F06_SUCCESS_ENVELOPE_CURRENT_DREAMINA_EXECUTABLE_METADATA_AND_COMMITTED_CLI_HELP_AND_INSTALL_GUIDANCE_TO_TEST_FIXED_UPLOAD_DEADLINE_HYPOTHESIS_COMPARE_TOTAL_DURATIONS_FAILURE_INPUT_POSITIONS_FILE_SIZES_AND_SUCCESS_THRESHOLD_DESIGN_EXACT_BOUNDED_ROUTE_RESET_OPTIONS_FOR_CLI_BUILD_REFRESH_HUMAN_NETWORK_PATH_CHANGE_WEB_UPLOAD_BYPASS_AND_NEW_HASHED_MEDIA_OPTIMIZATION_VARIANT_WITHOUT_EXECUTING_OR_CHANGING_ANY_ROUTE_REQUIRE_NO_THIRD_F07_SUBMIT_NO_DREAMINA_NO_PROVIDER_NO_SUBMIT_NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_LOGIN_NO_CHECKLOGIN_NO_EXECUTABLE_INSTALL_OR_UPDATE_NO_NETWORK_PROXY_FIREWALL_OR_DNS_CHANGE_NO_MEDIA_SOURCE_STATE_DATASET_PROMPT_PACKAGE_MANIFEST_OR_HISTORY_CHANGE_ALLOW_ONE_BOUNDED_ROUTE_RESET_DECISION_REPORT_COMMIT_AND_PUSH_AND_INCLUDE_ONE_MINIMAL_DURABLE_SOURCE_RULE_CANDIDATE_IN_THE_REPORT_FOR_SEPARATE_HUMAN_APPROVAL_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

Independent Python standard-library derivation, performed before route evidence inspection:

| Check | Result |
| --- | --- |
| Encoding | UTF-8 |
| Byte length | `1080` |
| SHA-256 | `cfa7ad6e9ea31b3ffbb2c97ae4295a246f8441e7c5e45b5577029c3f5bbbdf93` |
| Locally derived Base64 length | `1440` characters |
| Base64 decode count | `1` |
| Byte-for-byte round trip | `true` |
| Decoded SHA-256 verified | `true` |
| BOM / CR / LF | `false / false / false` |
| Trailing space / Markdown fence | `false / false` |
| Last character / last byte | `period / 2E` |

Accepted compiler/verifier result over the same canonical bytes:

- Serialization profile valid: `true`
- Authorization evidence verified: `true`
- Authorization verified: `true`
- Required checkpoint binding verified: `true`
- Local HEAD binding verified: `true`
- `origin/main` binding verified: `true`
- Eligibility calculation: `true`
- Authority activation: `false`
- Execution authority active: `false`
- Provider command allowed: `false`
- Provider command invocation count: `0`
- Authorized operation count consumed: `0`

Eligibility was used only to validate the no-live report scope. It did not activate execution authority.

## 3. Repository And Route-Stop Preflight

Preflight passed:

- Local HEAD: `cb413bc53ff7f05585d556377a9ba813ab3495ff`
- `origin/main`: `cb413bc53ff7f05585d556377a9ba813ab3495ff`
- Local and remote aligned before analysis: `true`
- Staged files before analysis: none
- Unexpected tracked modifications: none
- `sources/` clean: `true`
- Temporary worktree residue: none; only the primary worktree exists
- Unrelated untracked workspace noise: left untouched
- Provider operation after the bound checkpoint: none found in committed state/evidence
- Query or download after the bound checkpoint: none
- Third F07 submit: none
- Authority closed: `true`

Verified CAL-001 state contract:

- State path: `experiments/CAL-001/execution_state/CAL001_P3C_remaining_77_resumable_execution_state_contract.json`
- SHA-256 before analysis: `54ff10de1d68cd82f4522c1984eb6f19fa30f8a6beececa618968d6ba30bee92`
- F07 task state: `recovery_submit_failed_route_reset_required`
- F07 submit attempts: `2`
- F07 recovery submit attempts: `1`
- Total submit count: `15`
- F07 query count: `0`
- F07 download count: `0`
- Retry count: `0`
- Resubmit count: `0`
- Completed fixed tasks: `13`
- Remaining fixed tasks: `71`
- F07 CLI submit route stopped: `true`
- Route reset required: `true`
- Third F07 submit permitted: `false`
- F07 authorized: `false`
- Execution authority active: `false`

Quarantined handles:

| Attempt | Handle | Provider task created | Query eligible | Download eligible | Reuse authorized |
| --- | --- | --- | --- | --- | --- |
| Initial | `5a69007b-ac19-4cef-86bc-41d19792149f` | `false` | `false` | `false` | `false` |
| Recovery | `d5fa2ba3-f4b4-4a8f-9591-5b22b1fac463` | `false` | `false` | `false` | `false` |

Neither handle may be queried, downloaded, reused, or treated as evidence of provider task creation.

## 4. Evidence Scope

The analysis used only the authorized committed subprocess envelopes, parsed task-creation records, phase reports, command bindings, package/manifest references, fixture files, state contract, and committed CLI guidance. Private Dreamina logs, credentials, sessions, executable contents, and media pixels were not inspected.

The directly compared invocation envelopes were:

- F07 initial submit: `experiments/CAL-001/execution_records/P3D_W01/CAL001-F07-P1-R1/evidence/F07-submit-001.subprocess_envelope.json`
- F07 recovery submit: `experiments/CAL-001/execution_records/P3D_W01_F07_RECOVERY_SUBMIT/CAL001-F07-P1-R1/evidence/F07-recovery-submit-001.subprocess_envelope.json`
- F06 successful recovery: `experiments/CAL-001/execution_records/P3D_W01_F06_RECOVERY_SUBMIT/CAL001-F06-P1-R1/evidence/recovery-submit-001.subprocess_envelope.json`

## 5. Independent Duration Comparison

Durations were calculated from committed UTC timestamps before any rounding.

| Invocation | Start | Completion | Exact duration | Outcome |
| --- | --- | --- | ---: | --- |
| F07 initial | `2026-07-20T09:53:34.026264Z` | `2026-07-20T09:55:07.188173Z` | `93161.909 ms` | Prequeue upload failure on input 3, `SCENE` |
| F07 recovery | `2026-07-20T13:01:39.354529Z` | `2026-07-20T13:03:12.478830Z` | `93124.301 ms` | Prequeue upload failure on input 2, `IDENTITY_B` |
| F06 successful recovery | `2026-07-19T14:28:55.589628Z` | `2026-07-19T14:30:17.676158Z` | `82086.530 ms` | Provider task created; nonempty logid; `gen_status=querying`; credit count `70` |

Exact differences:

- F07 initial minus F07 recovery: `37.608 ms`
- F07 initial minus F06 success: `11075.379 ms`
- F07 recovery minus F06 success: `11037.771 ms`

Rounded interpretation:

- Both F07 failures ended at approximately `93.1 s`, within approximately `0.038 s` of each other.
- The successful F06 task creation completed at approximately `82.1 s`, about `11.0 s` below the F07 failure cluster.
- The F07 timing is strongly consistent with a repeatable global deadline or upload-session lifetime near 90 seconds plus wrapper/cleanup overhead.
- The timing does not directly prove an internal 90-second implementation timeout or identify which system imposed it.

The narrow committed diagnostic additionally records that the first F07 invocation completed input 1 at about `29.974 s`, completed input 2 at about `87.974 s`, and failed on input 3 by `93.162 s`. It exposes no HTTP status, provider error code, exception, timeout marker, network marker, authentication/signature failure, MIME failure, or decode failure. That absence is material.

## 6. Fixture And Failure-Position Comparison

Only ordinary file metadata and hashes were inspected. Pixels were not exported or transformed.

| Order / duty | Path | Bytes | SHA-256 | Metadata | Cumulative bytes | Share |
| --- | --- | ---: | --- | --- | ---: | ---: |
| 1 / `IDENTITY_A` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `1959523` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | PNG, 1440x2560, RGB, no alpha, no ICC, no EXIF | `1959523` | `19.633%` |
| 2 / `IDENTITY_B` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `3874061` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | PNG, 1440x2560, RGB, no alpha, no ICC, no EXIF | `5833584` | `38.815%` |
| 3 / `SCENE` | `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | `4147285` | `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452` | PNG, 2560x1440, RGB, no alpha, no ICC, no EXIF | `9980869` | `41.552%` |

- Total input bytes: `9980869`
- F07 initial failed input: `3 / SCENE`
- F07 recovery failed input: `2 / IDENTITY_B`
- Failure-position shift verified: `true`
- Same fixture paths, order, byte counts, and hashes verified across the compared route evidence: `true`
- All three fixtures historically uploaded in the successful F06 recovery: `true`

The shifted failure location does not correlate consistently with a particular fixture. It correlates more plausibly with the input active when elapsed serial-upload time approaches the observed failure cluster. Since the same exact fixture hashes all uploaded successfully in F06, the evidence does not support a deterministic media defect. It also does not prove that media size is irrelevant: smaller deterministic variants could still test whether transfer duration is causal.

The F06 and F07 executions share the same executable hash, fixture set/order, model, and material invocation structure. Their complete prompt bindings differ, so an assertion that their full command binding is byte-identical is not supported.

## 7. Fixed Upload-Deadline Hypothesis

Overall classification: `STRONGLY_SUPPORTED`

Directly proven: `false`

| Proposition | Classification | Basis |
| --- | --- | --- |
| 1. The two F07 failures have nearly identical total durations. | `DIRECTLY_PROVEN` | Exact envelope timestamps differ by only `37.608 ms`. |
| 2. The failed input position shifted. | `DIRECTLY_PROVEN` | Initial failed on input 3; recovery failed on input 2. |
| 3. The same fixtures and command binding succeeded previously. | `NOT_SUPPORTED` as stated | The same fixtures/order and material parameters succeeded, but the complete F06 and F07 prompt/command bindings are not identical. |
| 4. The successful invocation completed materially below the failure cluster. | `DIRECTLY_PROVEN` | F06 completed `11037.771-11075.379 ms` earlier. |
| 5. A fixed deadline is documented in committed help or guidance. | `NOT_SUPPORTED` | No upload-deadline option or stated fixed deadline was found. |
| 6. A fixed deadline is visible in committed implementation or wrapper evidence. | `NOT_SUPPORTED` | No committed implementation exposes one; internal behavior remains unknown. |
| 7. A specific provider upload service caused the failure. | `UNKNOWN` | No HTTP/provider code or service-level error evidence exists. |
| 8. A specific network path caused the failure. | `UNKNOWN` | No controlled network comparison or network error marker exists. |
| 9. A specific fixture caused the failure. | `NOT_SUPPORTED` | Failure position shifted and all three hashes previously uploaded successfully. |
| 10. The current `2a20fff-dirty` build caused the failure. | `UNKNOWN` | The same build succeeded for F06; no causal build comparison exists. |

The repeatable duration cluster is evidence for a deadline-like mechanism, not proof of where that mechanism lives. A provider defect, network defect, CLI defect, or exact timeout value cannot be claimed from the available evidence.

## 8. Current Dreamina Executable Metadata

The binary was inspected as a file only and was not executed, decoded, decompiled, patched, updated, or replaced.

- Path: `C:/Users/msjpurf/bin/dreamina.exe`
- Exists: `true`
- Bytes: `31879680`
- SHA-256: `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- Creation time UTC: `2026-07-01T08:36:08.1661465Z`
- Last-write time UTC: `2026-07-01T08:36:12.5846580Z`
- Ordinary file version metadata: unavailable
- Committed execution version string: `2a20fff-dirty`
- Committed build timestamp: `2026-06-26T06:36:39Z`
- `dirty` semantic origin explained by committed documentation: `false`
- `dirty` proves corruption or local modification: `false`

The same executable hash/build produced the successful F06 task creation, so the current evidence does not support a deterministic-binary-corruption conclusion.

## 9. Committed Help And Update Findings

Findings from the committed latest help, V1.2-V1.4 execution guidance, workflow guidance, macro-authorization guidance, and the July 1 update snapshots:

- Documented update-first command: `curl -fsSL https://jimeng.jianying.com/cli | bash`
- Documented observed shell form: `bash -lc "curl -fsSL https://jimeng.jianying.com/cli | bash"`
- The documented update installed a Linux binary side by side at `/home/ke/.local/bin/dreamina`; it did not replace `C:/Users/msjpurf/bin/dreamina.exe`.
- A trusted official Windows replacement/update command is not documented in the committed guidance.
- Explicit rollback instructions are not documented.
- Version, help, and login/credit readiness must be revalidated after a future authorized update.
- A changed executable requires a new byte/hash binding and fresh checkpoint-bound human authorization.
- Linux live execution guidance requires login-state and `user_credit` readiness checks; those checks remain disallowed in this phase.
- Current multimodal help supports repeated local `--image` inputs and automatic upload, but no documented upload-timeout setting was found.
- No documented upload-concurrency control was found.
- No documented pre-upload-only CLI operation was found.
- No official documented option was found that can address this failure without changing either the executable route, network path, web route, or media bytes.

The Windows executable and the documented Linux V1.4.10 snapshot share the same commit/build identity. A simple refresh therefore has low demonstrated likelihood of fixing the issue, and no claim can be made without a newly authorized comparison.

## 10. Route A: CLI Build Refresh

Status: `DESIGNED_NOT_AUTHORIZED_NOT_EXECUTED`

Bounded design:

1. Obtain fresh human authorization for maintenance, non-live verification, and at most one later provider submit under a new experiment identity.
2. Record current executable path, byte count, SHA-256, timestamps, and version evidence. Preserve a side-by-side verified backup before any replacement.
3. Verify the installer source, target platform, expected path, release identity, and rollback path without executing the installer.
4. Use only the documented official command for the documented Linux target. Safe-block any Windows replacement until a trusted official Windows procedure and rollback instructions are supplied.
5. After an authorized update, bind the new executable path, byte count, and SHA-256; then revalidate version/help. Run login/checklogin or `user_credit` only when separately authorized and required for that environment, without recording credentials.
6. Revalidate task, package, Prompt hash, input order, fixture hashes, model parameters, and invocation cap.
7. Use a new route-reset experiment/package identity. Never reuse either orphaned handle or count the operation as a third `CAL001-F07-P1-R1` submit.
8. Maximum future provider operation: one submit only, under fresh checkpoint-bound authorization; no implicit query/download/retry/resubmit.
9. Technical success: new bound build passes non-live contract checks and a separately authorized submit creates one provider task. Safe-block on untrusted installer/path, missing rollback, binding drift, auth failure, contract drift, or any unexpected state change.

Classification:

- Diagnostic value: medium
- Likelihood of addressing failure: low to unknown
- Governance risk: medium-high
- Reproducibility: medium
- Cost: zero credits for maintenance; a later submit may cost `70`
- User effort: medium-high
- Reversibility: conditional on a verified backup/rollback path

## 11. Route B: Human Network-Path Change

Status: `DESIGNED_NOT_AUTHORIZED_NOT_EXECUTED`

Bounded design:

1. A human selects exactly one path variable, preferably the current connection versus a stable wired Ethernet path. If already wired, choose one other human-approved network path. Do not combine VPN, proxy, firewall, DNS, and path changes.
2. Record only a coarse path label, observation timestamp, link stability, and a small set of non-sensitive continuity/latency observations. Do not record credentials, full IP configuration, session data, or complete environment dumps.
3. Require stable connectivity for an agreed observation window before any later submit; record disconnects, large latency swings, or packet-loss observations without changing system settings through automation.
4. Use a new route-reset experiment identity and fresh checkpoint-bound authorization. Preserve the exact original fixture hashes/order and a newly bound package copy if a provider submit is later approved.
5. Maximum future provider operation: one submit only; no query/download/retry/resubmit unless separately authorized later.
6. A success only on the changed path would support a network-sensitive cause. A repeat failure near `93.1 s` would show that the chosen path change did not resolve the deadline-like behavior. Neither result alone identifies a specific provider or network component.

Classification:

- Diagnostic value: medium-high
- Likelihood of addressing failure: unknown
- Governance risk: medium
- Reproducibility: medium-low
- Cost: a later submit may cost `70`
- User effort: medium
- Reversibility: high

## 12. Route C: Manual Web-Upload Bypass

Status: `DESIGNED_NOT_AUTHORIZED_NOT_EXECUTED`

### Purpose A: Upload-Only Diagnostic

1. Under a new human authorization and experiment identity, the human opens the web UI and selects the same three original files in the same duty/order.
2. Record whether each file reaches a visible completed-upload state, the upload order, approximate start/completion elapsed time per file, and any non-sensitive visible error class.
3. Stop before generation whenever the UI permits. This is not a CLI reproduction and must not be recorded as automated CLI success.
4. Prefer structured notes and timings. Any screenshot must be sanitized and must exclude account identity, balances, credentials, session details, cookies, signed URLs, or unrelated private UI.
5. If all three uploads complete, the result supports a CLI/session/route-sensitive issue and prioritizes CLI diagnostics or an explicitly authorized human fallback. If web upload fails similarly, prioritize common media/network/provider hypotheses.
6. No provider generation or credit consumption is expected when the UI permits a stop before generation, but the human must treat any UI action that may trigger generation as credit-bearing and stop without separate authorization.

### Purpose B: Human Fallback Generation

1. This is a separate route requiring separate human authorization, evidence protocol, duplicate check, and credit acknowledgment.
2. It must be recorded as human web execution, never as CLI provenance.
3. It must not silently mark the CAL-001 fixed task successful or rewrite the original F07 history.
4. Before generation, verify no active provider task exists for either quarantined handle and no other authorized route is running. Do not query those handles; use the committed quarantine state.

Classification for the selected Purpose A diagnostic:

- Diagnostic value: high
- Likelihood of separating competing causes: high
- Governance risk: low to medium
- Reproducibility: medium
- Provider credit risk: low if generation is not triggered
- User effort: medium
- Reversibility: high

## 13. Route D: New Hashed Media Optimization Variant

Status: `DESIGNED_NOT_AUTHORIZED_NOT_CREATED`

Bounded design:

1. Keep all three locked originals immutable. Create variants only under new paths, with new SHA-256 values and explicit derivative status.
2. Preserve reference duty, identity, composition, framing, scene meaning, and input order. Never claim a derivative is an original locked reference.
3. Use deterministic, recorded tool versions and settings. Candidate formats are lossless optimized PNG first, or high-quality JPEG/WebP only after format acceptance is independently verified.
4. Preserve current dimensions for the first comparison. A long-edge reduction such as 1920 pixels requires separate review. Convert deterministically to RGB/sRGB; use no alpha unless required; remove or explicitly normalize ICC, EXIF, and other metadata.
5. Proposed target ranges: identity A `0.8-1.2 MB`, identity B `1.2-1.8 MB`, scene `1.4-2.0 MB`, total `3.4-5.0 MB`.
6. Against the current `9980869` bytes, the target represents an approximate `49.9%-65.9%` byte reduction. Under a purely linear transfer-time assumption, only the byte-transfer component could fall by the same percentage. This is not a measured throughput result and does not forecast total invocation duration.
7. Validate dimensions, format, color mode/profile, alpha, metadata, decodability, byte counts, hashes, and deterministic reproducibility.
8. Require ChatGPT Pro plus human side-by-side visual comparison before acceptance, especially for identity, composition, facial detail, framing, and scene geometry.
9. If accepted, create a new package, binding, experiment identity, and manifest/adaptation record under separate authorization. Any later provider submit is one newly authorized operation, never a hidden third F07 attempt.

Classification:

- Diagnostic value: medium
- Likelihood of addressing deadline-like behavior: medium if transfer duration is causal
- Governance risk: high
- Reproducibility: high
- Cost: zero credits until a later provider submit; then potentially `70`
- User effort: high
- Reversibility: high because originals remain immutable

## 14. Decision Matrix

| Criterion | CLI build refresh | Human network path | Web upload bypass, Purpose A | New hashed media variant |
| --- | --- | --- | --- | --- |
| Evidence addressed | Build-specific behavior | Path sensitivity | CLI/session route versus broader upload behavior | Byte-volume/media sensitivity |
| Diagnostic value | Medium | Medium-high | High | Medium |
| Provider credit risk | None for refresh; `70` for later submit | `70` for later submit | Low if stopped before generation | None until later submit; then `70` |
| Human effort | Medium-high | Medium | Medium | High |
| Engineering effort | Medium-high | Low-medium | Low | High |
| Reproducibility | Medium | Medium-low | Medium | High |
| Reversibility | Conditional | High | High | High |
| Governance complexity | Medium-high | Medium | Low-medium | High |
| New artifacts | Binary binding, checks, new package/experiment for submit | Path note, new binding/package/experiment | Diagnostic record and new experiment | Derivatives, hashes, review, package, manifest adaptation, experiment |
| Human review | Installer/route approval | Path choice and evidence review | Required UI observation | Required technical and ChatGPT Pro visual review |
| Future provider operation required | Yes for causal submit test | Yes | Yes for upload transport; generation not required | Yes for causal submit test |
| Separates competing causes | Partly | Partly | Best first separation of CLI route from common upload path | Tests media-size contribution |
| Stop conditions | Untrusted Windows update, no rollback, binding drift | Multiple variables changed, unstable path, evidence gap | UI may generate without authorization, sensitive capture risk, duplicate risk | Visual drift, nondeterminism, format rejection, missing new governance artifacts |

## 15. Selected Route

Selected exactly:

`PRIMARY_ROUTE_WEB_UPLOAD_BYPASS`

Selected purpose: Purpose A, upload-only diagnostic.

Reason: this is the smallest reversible diagnostic that can meaningfully separate CLI/session-route behavior from a broader media/network/provider-upload issue before provider generation. It preserves the executable, network configuration, original media, package, manifest, and historical state. It has low credit risk when the UI permits stopping before generation.

This selection is decision support only. It does not authorize opening the web route, uploading files, generating media, or consuming credits.

- Selected route requires a future provider/upload operation: `true`
- Selected route requires provider generation: `false`
- Selected route requires human observation/review: `true`
- Selected route requires generated-media visual approval: `false`
- Selected route requires a new experiment identity: `true`
- Selected route requires a new package for upload-only diagnosis: `false`
- Any later fallback generation requires a new package/binding and separate authorization: `true`

## 16. Proposed Route Identities And Governance

These names are proposals only. No record, package, manifest row, directory, state field, or counter was created.

- Route-reset decision ID: `CAL-001-P3D-W01_F07_CLI_SUBMIT_ROUTE_RESET_NO_LIVE_DECISION`
- CLI build diagnostic: `CAL001-F07R-CLI-DIAG-P1-R1`
- Human network diagnostic: `CAL001-F07R-NET-DIAG-P1-R1`
- Web upload diagnostic: `CAL001-F07R-WEB-UPLOAD-DIAG-P1-R1`
- Hashed-media adaptation: `CAL001-F07R-MEDIAOPT-P1-R1`
- Optional later web fallback generation: `CAL001-F07R-WEB-FALLBACK-P1-R1`
- Proposed evidence-root pattern: `experiments/CAL-001/execution_records/P3D_W01_F07_ROUTE_RESET/<experiment_id>/`
- Proposed package pattern when a route actually needs generation: `<experiment_id>_package.json`
- Proposed separate counters: `F07_route_reset_diagnostic_count` and `F07_route_reset_provider_submit_count`

Relationship to F07:

- The original F07 remains unresolved with two immutable failed submit records.
- A future route-reset experiment may inform the F07 route decision through explicit linkage, but it must not rewrite either failure or increment the old experiment as a third attempt.
- The fixed 84-task manifest remains unchanged until a separate human decision.
- Both orphaned handles remain quarantined, non-queryable, non-downloadable, and non-reusable.

## 17. Minimal Durable Source-Rule Candidate

Status: `SOURCE_RULE_CANDIDATE_ONLY_NOT_APPLIED`

> When an initial submit and one separately human-authorized recovery submit both fail during prequeue upload without creating a provider task, close that experiment's CLI submit route; forbid a third submit under the same experiment identity; keep both orphaned handles non-queryable and non-downloadable; and require any future provider operation to use a materially changed route, a new experiment and package identity, and fresh checkpoint-bound human authorization. Acceptable changed routes include a validated CLI build, a human-controlled network path, an explicit web bypass, or a newly hashed media variant.

This is the only Source-rule candidate in this report. It was not applied to `sources/` or any human-managed Source mirror.

## 18. Next Required Human Decision

Recommended next decision phase:

`CAL-001-P3D-W01_F07_WEB_UPLOAD_BYPASS_DIAGNOSTIC_AUTHORIZATION_DECISION`

That decision should bind a new checkpoint and the proposed `CAL001-F07R-WEB-UPLOAD-DIAG-P1-R1` identity, authorize only the human upload-only observation protocol, explicitly forbid generation, and define a safe stop if the UI cannot guarantee no generation.

## 19. No-Live And Integrity Confirmation

- Dreamina called: `false`
- Provider called: `false`
- Submit/query/download: `false / false / false`
- Retry/resubmit: `false / false`
- Login/checklogin: `false / false`
- Executable installed, updated, replaced, or executed: `false`
- Network/proxy/firewall/VPN/DNS changed: `false`
- Media created, decoded, transformed, or overwritten: `false`
- `sources/` touched: `false`
- CAL-001 state changed: `false`
- Datasets changed: `false`
- Prompt/package/manifest changed: `false`
- Historical execution evidence changed: `false`
- Final master: `false`
- Locked: `false`

## 20. Final Verdict

`CAL001_P3D_W01_F07_CLI_SUBMIT_ROUTE_RESET_NO_LIVE_DECISION_COMPLETE_PRIMARY_ROUTE_WEB_UPLOAD_BYPASS_NO_EXECUTION`
