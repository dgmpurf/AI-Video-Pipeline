# CAL-001 P3D W01 F07R Binding And Route-State Creation Attestation No-Live Result

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_EXECUTION_BINDING_AND_ROUTE_STATE_CREATION_ATTESTATION_NO_LIVE`
- Repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- Branch: `main`
- Starting checkpoint: `0a4fb8bc55d6503a99cffe120f53caec9a4a752a`
- Mode: bounded C2 no-live creation attestation
- Pairing decision: `BINDING_AND_ROUTE_STATE_CREATION_ATTESTED_PENDING_INDEPENDENT_AUDIT`
- Provider or account operation authorized: `false`

This phase attests the immutable C1 execution binding and initial route state. It creates only this report and the canonical creation-evidence manifest. It does not modify either C1 artifact or create a route transition.

## 2. Exact Authorization Verification

The canonical authorization was independently extracted as one continuous UTF-8 line and verified without persisting the raw authorization line or Base64 value.

| Fact | Verified value |
| --- | --- |
| Encoding | `UTF-8` |
| Byte length | `2917` |
| SHA-256 | `eae8d157a64cd18d0744634a1536524b2c17aa47033efd1d2dae0f4de19f5b3b` |
| Locally derived Base64 character count | `3892` |
| Base64 decode count | `1` |
| Byte-for-byte round trip | `true` |
| Last byte | `2E` |
| BOM / CR / LF / trailing space / Markdown fence | `false / false / false / false / false` |
| Repository compiler serialization profile valid | `true` |
| Repository verifier authorization verified | `true` |
| Checkpoint binding verified | `true` |
| Eligible for authority activation | `false` |

The compiler and verifier kept execution authority inactive, provider commands forbidden, provider invocation count zero, and authorized-operation consumption zero.

## 3. Repository And C1 Boundary

Repository preflight passed after refreshing `origin`:

- Local `HEAD`, `origin/main`, and required checkpoint: `0a4fb8bc55d6503a99cffe120f53caec9a4a752a`
- Branch: `main`
- Staged files before C2: none
- Existing tracked modifications before C2: none
- `sources/` clean: `true`
- Worktrees: exactly one primary worktree
- Unrelated untracked workspace noise: left untouched
- Both C2 output paths initially absent: `true`

C1 was independently verified:

| Fact | Value |
| --- | --- |
| C1 commit | `0a4fb8bc55d6503a99cffe120f53caec9a4a752a` |
| C1 parent | `13cc1e0dadd83ab6857d3ff34f4b3c6b56650ae4` |
| C1 tree SHA | `ab735b53c0bbddbe647a9bb1bc67c9ee98693b4a` |
| Commit count after parent | `1` |
| Changed-path count | `2` |

The exact C1 paths are:

1. `experiments/CAL-001/execution_bindings/F07R/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_execution_binding.json`
2. `experiments/CAL-001/execution_state/F07R/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_route_state_contract.json`

No third C1 path exists.

## 4. Immutable Binding Verification

| Fact | Verified value |
| --- | --- |
| Path | `experiments/CAL-001/execution_bindings/F07R/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_execution_binding.json` |
| Schema version | `CAL001_F07R_EXECUTION_BINDING_V1` |
| Record type | `CAL001_F07R_IMMUTABLE_EXECUTION_BINDING` |
| Object ID | `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1::EXECUTION_BINDING::V1` |
| Byte length | `20808` |
| SHA-256 | `52ac7c5aefb1f89993b511796b7fe58a40c030b475188750584b1b53a30e618d` |
| Git blob | `ffc52ae728bdaa7b05cc34afaabab0bcfb79a2b4` |
| Strict JSON reread | `true` |
| Canonical byte equality | `true` |
| Working tree equals `HEAD` | `true` |
| Immutable | `true` |
| Modified during C2 | `false` |
| Contains its own SHA-256 | `false` |
| Contains route-state content SHA-256 | `false` |
| Contains C1 commit SHA | `false` |

## 5. Immutable Route-State Verification

| Fact | Verified value |
| --- | --- |
| Path | `experiments/CAL-001/execution_state/F07R/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_route_state_contract.json` |
| Schema version | `CAL001_F07R_ROUTE_STATE_V1` |
| Record type | `CAL001_F07R_IMMUTABLE_INITIAL_ROUTE_STATE` |
| Object ID | `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1::ROUTE_STATE::V1` |
| Byte length | `8489` |
| SHA-256 | `e4886450dc0017aa92fa35ee37f1f39f4a3ebd85aa350e624aac78dd954827a9` |
| Git blob | `9004b52a6b4313bd70deae77dc0616f36449eedb` |
| Strict JSON reread | `true` |
| Canonical byte equality | `true` |
| Working tree equals `HEAD` | `true` |
| Immutable | `true` |
| Modified during C2 | `false` |
| Contains its own SHA-256 | `false` |
| Contains C1 commit SHA | `false` |

## 6. Pairing And Zero-Transition Validation

| Check | Result |
| --- | --- |
| Binding expected route path/schema/type/object ID match | `true` |
| Route-state binding path/schema/type/object ID match | `true` |
| Route-state binding byte length and SHA-256 match | `true` |
| Noncircular pair valid | `true` |
| Neither artifact claims the other is absent | `true` |
| Precreation status absent | `true` |
| Zero-transition anchor valid | `true` |
| Ordered transition paths | `[]` |
| Terminal state | `BINDING_CREATED_NOT_AUDITED` |
| Finding details | `[]` |

## 7. Unchanged Route Snapshot

```text
route_status_code=BINDING_CREATED_NOT_AUDITED
route_status=binding_created_not_audited
binding_exists=true
route_state_exists=true
binding_audit_complete=false
binding_audit_accepted=false
preflight_executed=false
provider_eligibility=false
route_provider_submit_allowance_consumed=false
route_provider_submit_invocation_count=0
route_provider_task_created_count=0
route_query_invocation_count=0
route_download_invocation_count=0
route_retry_invocation_count=0
route_resubmit_invocation_count=0
route_batch_invocation_count=0
route_credit_charged_total=0
```

All top-level and nested operation counters agree and remain zero.

## 8. Canonical Creation-Evidence Manifest

| Fact | Value |
| --- | --- |
| Path | `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/attestation/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_binding_route_state_creation_evidence_manifest.json` |
| Schema version | `CAL001_F07R_BINDING_ROUTE_STATE_CREATION_EVIDENCE_MANIFEST_V1` |
| Record type | `CAL001_F07R_IMMUTABLE_CREATION_EVIDENCE_MANIFEST` |
| Object ID | `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1::BINDING_ROUTE_STATE_CREATION_EVIDENCE_MANIFEST::V1` |
| Byte length | `8167` |
| SHA-256 | `b8d4c27b790d0303b990bb58ee0a7532a6f4469a26bac63556173bae64046c1b` |
| Git blob | `9bfbc434e64eeb3c55363c1bc8a6a5848edaf658` |
| Strict canonical JSON verified | `true` |
| Contains self-hash | `false` |
| Contains future C2 commit SHA | `false` |
| Contains report byte length/hash/blob | `false` |
| Contains wall-clock timestamp | `false` |
| Contains raw authorization or Base64 | `false` |

The manifest was finalized before this report and records the report path only.

## 9. Dedicated Support Test

Command:

`python -m pytest -q -rs tests/test_f07r_support_contract.py`

Actual result:

```text
collected=201
passed=200
failed=0
skipped=1
skip_reason=POSIX permission bits are not stable on Windows
```

## 10. No-Live And Protected-State Confirmation

No-live facts:

```text
Dreamina_called=false
provider_called=false
submit_called=false
query_called=false
download_called=false
retry_called=false
resubmit_called=false
batch_called=false
F08_called=false
login_called=false
checklogin_called=false
user_credit_called=false
web_UI_operated=false
```

Artifact and protected-state facts:

```text
binding_modified=false
route_state_modified=false
route_state_transition_created=false
runtime_integration_created=false
real_claim_created=false
real_transition_created=false
execution_record_created=false
evidence_root_created=false
command_binding_created=false
preflight_artifact_created=false
canary_artifact_created=false
subprocess_envelope_created=false
provider_artifact_created=false
sources_touched=false
CAL001_global_state_changed=false
package_modified=false
manifest_modified=false
Prompt_modified=false
media_modified=false
executable_modified=false
authorization_history_modified=false
historical_evidence_modified=false
```

Authority remains inactive:

```text
binding_authorized=false
binding_active=false
package_authorized=false
package_active=false
execution_authority_active=false
provider_command_allowed=false
submit_authorized=false
query_authorized=false
download_authorized=false
retry_authorized=false
resubmit_authorized=false
batch_authorized=false
final_master=false
locked=false
```

## 11. C2 Decision

`BINDING_AND_ROUTE_STATE_CREATION_ATTESTATION_READY_INDEPENDENT_AUDIT`

## 12. Next Required Phase

`CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_EXECUTION_BINDING_AND_ROUTE_STATE_INDEPENDENT_NO_LIVE_AUDIT`

This attestation grants no execution authority. The next phase must be separately authorized and must remain no-live.

## 13. Final Verdict

C2 creation attestation is complete and ready for the separately authorized independent no-live audit.
