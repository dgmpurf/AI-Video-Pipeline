# CAL-001 P3D W01 F07R One-Submit Authorization Decision

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_ONE_SUBMIT_AUTHORIZATION_DECISION`
- Experiment: `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1`
- Starting checkpoint: `4d1d376bd0e7588c6675b947ec698b5e75e81456`
- Phase type: decision and append-only route transition only
- Decision: `ONE_SUBMIT_AUTHORIZATION_DECISION_READY_EXECUTION`
- Authorized state: `SUBMIT_AUTHORIZED_NOT_CONSUMED`
- Next required phase: `RETURN_TO_CHATGPT_FOR_EXACT_ONE_SUBMIT_EXECUTION_AUTHORIZATION`

This phase records a bounded future one-submit authorization decision. It does
not authorize or execute Dreamina in this phase, does not create a submit claim,
and does not consume the one-submit allowance.

## 2. Exact Authorization Verification

The exact canonical authorization was extracted as one continuous line and
verified independently with Python standard-library UTF-8, SHA-256, and Base64
operations before the repository compiler/verifier was consulted.

| Fact | Result |
| --- | --- |
| Encoding | `UTF-8` |
| Byte length | `3410` |
| SHA-256 | `07cda7a21d883f3704531063723f6388661993f09c855ca2742b57d1736f3861` |
| Locally derived Base64 character count | `4548` |
| Base64 decode count | `1` |
| Byte-for-byte round trip | `true` |
| Decoded SHA-256 equals original | `true` |
| BOM / CR / LF / trailing space / Markdown fence | all `false` |
| Last byte | `2E` |
| Raw authorization persisted | `false` |
| Base64 value persisted | `false` |

The accepted repository verifier independently returned:

```text
serialization_profile_valid=true
authorization_evidence_verified=true
authorization_verified=true
record_representations_consistent=true
record_serialization_facts_match=true
checkpoint_binding_verified=true
eligible_for_authority_activation=true
execution_authority_active=false
provider_command_allowed=false
provider_command_invocation_count=0
authorized_operation_count_consumed=0
```

Eligibility is an evidence result only. No provider command authority is active.

## 3. Repository And D2 Commit Boundary

Repository preflight confirmed:

- repository root `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`;
- branch `main`;
- local HEAD and `origin/main` both equal the required checkpoint;
- no staged or unexpected tracked change;
- `sources/` clean;
- exactly one primary worktree;
- both authorized output paths initially absent;
- unrelated untracked workspace noise left untouched.

D2 commit audit:

| Field | Value |
| --- | --- |
| Commit | `4d1d376bd0e7588c6675b947ec698b5e75e81456` |
| Parent | `8b64aef7ac8eadb32e474c9e1ce682c0be348b93` |
| Added paths | `14` |
| Existing tracked-file modifications | `0` |

D2 result report binding:

| Field | Value |
| --- | --- |
| Path | `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_NO_PROVIDER_CANARY_AND_PREFLIGHT_ONLY_RESULT.md` |
| Byte length | `8987` |
| SHA-256 | `e9d6601969296a3ba51e3c82f72a411a29530ef58a6d403584c78c78b7e78c3e` |
| Git blob | `538b778d26b152b98295f140b35981dc3f0940af` |
| Decision | `NO_PROVIDER_CANARY_AND_PREFLIGHT_ONLY_PASSED_AWAITING_SUBMIT_AUTHORIZATION` |

The D2 report confirms exactly four read-only Dreamina CLI calls, all preflight
gates passed, no provider task, no submit/query/download, allowance unconsumed,
no live-balance disclosure, and return for this authorization decision.

## 4. D2 Evidence Binding

Preflight summary:

| Field | Value |
| --- | --- |
| Path | `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/preflight/no_provider_preflight_summary.json` |
| Byte length | `6709` |
| SHA-256 | `0d49c7e15627889827d2d053f8e5cd9ae904bf47c861933fd015cd3cb60f63e4` |
| Git blob | `ef15a53d292611f7d25143559478f92bb1126c1f` |
| Decision | `NO_PROVIDER_PREFLIGHT_PASSED_AWAITING_SUBMIT_AUTHORIZATION` |
| Failure reasons | `[]` |

The summary records `preflight_executed=true`, `preflight_passed=true`,
`preflight_safe_blocked=false`, `provider_eligibility=true`, and
`submit_authorized=false`. Required pre-submit credit is `5530`; the D2 credit
gate passed. The numeric available credit is not reproduced here.

Preflight evidence manifest:

| Field | Independently derived value |
| --- | --- |
| Path | `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/preflight/no_provider_preflight_evidence_manifest.json` |
| Byte length | `4246` |
| SHA-256 | `99247f8d08bd2040a22c958f73d2b0f2eeffc7e35bcc431c51d7f5287d9cc32a` |
| Git blob | `71b646b534712ec852a4a90f6ffe1f84b69997bf` |
| Listed evidence entries | `11` |

The manifest is strict canonical JSON. All listed paths, byte lengths, and
SHA-256 values independently match. All listed JSON is readable and canonical;
unsanitized raw persistence is false. The manifest has no self-hash and no
report or transition hash circularity.

## 5. Route Chain And Sequence 3

Sequence 3 binding:

| Field | Value |
| --- | --- |
| Path | `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-preflight-result-003_transition.json` |
| Byte length | `2039` |
| SHA-256 | `f352e8481960d944c4defe030f4dfc1dd77d24556c7fea3776023a757cba5da7` |
| Git blob | `c87225933874e9a686cf85edac45caddb1308ec4` |
| Sequence | `3` |
| State | `PREFLIGHT_PASSED_AWAITING_SUBMIT_AUTHORIZATION` |

The existing anchor through sequence 3 validates with `valid=true`, terminal
state `PREFLIGHT_PASSED_AWAITING_SUBMIT_AUTHORIZATION`, and no findings.
Preflight executed and passed; provider eligibility is true. Submit remains
unauthorized, allowance is unconsumed, and every provider-route counter is zero.

## 6. Decision Prerequisites

All READY prerequisites independently passed:

- immutable execution binding and 23 deep references remain exact;
- route-state anchor, C2 manifest, accepted binding audit, and sequences 1-3
  remain stable;
- support contract remains accepted;
- package remains immutable, inactive, and no-submit;
- Prompt is `1976` bytes with SHA-256
  `094a01dee03f49b65badf1864873f2b85a74a9b801f6a26621a84fb0c409f681`;
- extracted provider payload is `519` bytes with SHA-256
  `ca90c5b50b7d244b6264b8ed3f23d4043bf490d25d672e2d05cfad49b487594a`;
- all three fixtures remain exact and ordered;
- executable identity remains exact without execution;
- parser and support-contract identities remain exact;
- provider argv has `20` arguments, full SHA-256
  `e79a1d40c9b1e31e019fceb138fe42c455e7235325f1a7b5bc9ebb58e2e956f5`,
  redacted SHA-256
  `22b8de54f2de0f8f5d4543ccb649d6bf2bc291126ab5f6de1b4d798b89f11e14`,
  and `shell_interpolation=false`;
- duplicate decision remains `DUPLICATE_PREVENTION_CLEAR`;
- no claim, provider invocation, F07R task, output, or completed provider
  transition exists;
- original F07 route remains closed and both handles remain quarantined;
- the fixed 84-task manifest contains zero F07R rows;
- allowance remains unconsumed and all provider-route counters remain zero;
- D2 credit gate passed against the required threshold `5530`;
- no tracked drift exists.

No `user_credit` refresh was performed in this decision phase.

## 7. Protected State

The following remain false:

`binding_authorized`, `binding_active`, `package_authorized`, `package_active`,
`execution_authority_active`, `provider_command_allowed`, `query_authorized`,
`download_authorized`, `retry_authorized`, `resubmit_authorized`,
`batch_authorized`, `final_master`, and `locked`.

This decision sets only `submit_authorization_decision_complete=true` and
`submit_authorized=true` in the new append-only sequence-4 transition. The
state remains not consumed: allowance false and submit invocation count zero.

## 8. Future F Execution Contract

Future phase:

`CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_ONE_SUBMIT_ONLY`

The future F phase requires a separate exact human authorization bound to its
future checkpoint. Maximum actual commands under that future authority are:

| Command | Maximum |
| --- | --- |
| Fresh immediate pre-submit `dreamina user_credit` | `1` |
| Bound `multimodal2video` provider submit | `1` |
| Fresh immediate post-submit `dreamina user_credit` | `1` |
| `query_result` / download / retry / resubmit / batch | `0` each |
| F08 / login / relogin / logout / checklogin | `0` each |

Provider submit allowance maximum is `1`; expected maximum provider credit cost
is `70`. No automatic retry or second submit is permitted.

Immediately before provider start, future F must revalidate the complete chain,
immutable bindings, and duplicate prevention; perform one fresh pre-submit
credit check; require the fresh governing threshold; durably create the
exclusive allowance-consumption claim; persist and validate the consumption
transition; then invoke exactly the bound 20-argument vector with `shell=false`.

Once the claim exists, any later runner, subprocess, evidence, or parsing
failure must never restore the allowance. Future F may perform exactly one
post-submit credit check, but no query or download.

## 9. Dedicated Tests

Command:

`python -m pytest -q tests/test_f07r_support_contract.py`

Actual result:

- collected: `201`;
- passed: `200`;
- failed: `0`;
- skipped: `1`;
- skip reason: `POSIX permission bits are not stable on Windows`.

## 10. No-Live Confirmation

- `Dreamina_called=false`
- `user_credit_called=false`
- `provider_called=false`
- `submit_called=false`
- `query_called=false`
- `download_called=false`
- `retry_called=false`
- `resubmit_called=false`
- `batch_called=false`
- `F08_called=false`
- `login_called=false`
- `checklogin_called=false`
- `web_UI_operated=false`
- `real_claim_created=false`
- `allowance_consumed=false`
- `runtime_integration_created=false`
- `provider_task_created=false`
- `media_created=false`

No Source, global CAL-001 state, existing binding, existing route-state object,
package, manifest, Prompt, media, executable, authorization history, or
historical evidence was modified.

## 11. Decision

Every prerequisite passed. The one decision is:

`ONE_SUBMIT_AUTHORIZATION_DECISION_READY_EXECUTION`

This decision authorizes only the append-only state
`SUBMIT_AUTHORIZED_NOT_CONSUMED`. It does not authorize a Dreamina invocation
inside this phase and does not consume the allowance.

Next required phase:

`RETURN_TO_CHATGPT_FOR_EXACT_ONE_SUBMIT_EXECUTION_AUTHORIZATION`
