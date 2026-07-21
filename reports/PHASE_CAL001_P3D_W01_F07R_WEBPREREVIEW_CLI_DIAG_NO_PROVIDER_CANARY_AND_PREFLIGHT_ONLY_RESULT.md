# CAL-001 P3D W01 F07R No-Provider Canary And Preflight Result

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_NO_PROVIDER_CANARY_AND_PREFLIGHT_ONLY`
- Experiment: `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1`
- Starting checkpoint: `8b64aef7ac8eadb32e474c9e1ce682c0be348b93`
- Completion classification: `COMPLETE with pass`
- Decision: `NO_PROVIDER_CANARY_AND_PREFLIGHT_ONLY_PASSED_AWAITING_SUBMIT_AUTHORIZATION`
- Next required phase: `RETURN_TO_CHATGPT_FOR_ONE_SUBMIT_AUTHORIZATION_DECISION`

This phase executed only four separately authorized read-only Dreamina CLI
commands. It did not activate submission authority and did not create or contact
a generation task.

## 2. Human Authorization Verification

The canonical authorization was independently encoded as UTF-8 and verified
before any Dreamina CLI invocation.

| Check | Result |
| --- | --- |
| Byte length | `3373` |
| SHA-256 | `f1af8cc334d5da10120cb6cddcd8e1785979435d1e7f424896688a00074e2343` |
| Locally derived Base64 length | `4500` |
| Decode count | `1` |
| Byte-for-byte round trip | `true` |
| BOM / CR / LF / trailing space / Markdown fence | all `false` |
| Final byte | `2E` |
| Repository verifier | `PASS` |
| Checkpoint binding | `PASS` |

The authorization text and derived Base64 were not persisted in the D2
artifacts. Authorization verification did not activate provider authority.

## 3. Repository And D1 Binding

Preflight required and confirmed:

- repository root `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`;
- branch `main`;
- local HEAD and `origin/main` both equal the required checkpoint;
- no staged or unrelated tracked changes;
- `sources/` clean;
- exactly one worktree;
- unrelated untracked workspace noise left untouched;
- every D2 output path absent before this phase;
- no F07R submit claim, provider invocation, task, output, or terminal provider
  transition existed.

D1 decision binding:

| Field | Value |
| --- | --- |
| Commit | `8b64aef7ac8eadb32e474c9e1ce682c0be348b93` |
| Report | `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_NO_PROVIDER_CANARY_AND_PREFLIGHT_AUTHORIZATION_DECISION_RESULT.md` |
| Report bytes | `16116` |
| Report SHA-256 | `330135492c3ab7bd802176a288e6e1ccb0d3f9fae0200372e80de3089a0400fd` |
| Report Git blob | `23b72ec1fbba6d4da4990998e34b5aeee4dda445` |
| Decision | `NO_PROVIDER_CANARY_AND_PREFLIGHT_AUTHORIZATION_DECISION_READY_EXECUTION` |

Sequence 2 remained byte-stable at SHA-256
`fb09592ba1503ea090158bee4e22e9a9f2c8b1cd32e6d7f6363e2be7130e1037`
and Git blob `bec5ad3f0240f01b95170bf457ff9da94d315df1`. The complete
starting route chain was valid, had no findings, and terminated at
`PREFLIGHT_DESIGNED_NOT_RUN`.

## 4. Static And Duplicate-Prevention Gates

All static gates passed before the first Dreamina CLI invocation:

- immutable execution binding and all deep references;
- initial route state, C2 creation evidence, accepted audit, sequence 1, and
  sequence 2;
- package, external acceptance, Prompt hash, and provider-payload hash;
- three fixtures and their exact order;
- parser and support-contract object identities;
- fixed accounting references;
- full and redacted provider argv hashes;
- Dreamina executable path, byte length, and SHA-256;
- reconstructed provider argv count and `shell_interpolation=false`.

`command_binding.json` and `duplicate_prevention_snapshot.json` were created
exclusively, durably persisted, re-read, and hashed before any CLI invocation.
The duplicate decision was `DUPLICATE_PREVENTION_CLEAR`.

The fixed manifest contained zero F07R rows. Original F07 accounting remained
two submits and one recovery submit; both historical handles remained
quarantined and ineligible for query, download, or reuse. The F07R allowance
remained unconsumed and all provider-route counters remained zero.

## 5. Authorized CLI Execution

The executable was `C:/Users/msjpurf/bin/dreamina.exe`. Each vector was invoked
exactly once, in order, with `shell=false`, exact repository cwd, closed stdin,
and the inherited environment unchanged.

| Order | Authorized command | Exit | Gate |
| --- | --- | --- | --- |
| 1 | `dreamina version` | `0` | `PASS` |
| 2 | `dreamina -h` | `0` | `PASS` |
| 3 | `dreamina multimodal2video -h` | `0` | `PASS` |
| 4 | `dreamina user_credit` | `0` | `PASS` |

Total Dreamina CLI invocation count was `4`. No command was retried or invoked
more than once.

For every command, raw stdout and stderr were captured separately, byte-counted,
and SHA-256 hashed before UTF-8 replacement decoding. Unsanitized raw bytes were
not persisted. Each sanitized envelope was durably written and re-read before
its parsed evidence record was created.

## 6. Version And Help Results

Version output matched the bound `96`-byte baseline and SHA-256
`25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`.
The version was `2a20fff-dirty`, commit `2a20fff`, build time
`2026-06-26T06:36:39Z`. Stderr was empty and no UTF-8 replacement occurred.

Root help matched the bound `2673`-byte baseline and SHA-256
`a7730ec92f51b4c992605d008e5533ea984c0c799b25a8490048a8b372883c81`.
All required built-in and generator commands were present. `checklogin` was not
a top-level Built-in Command.

An initial local whole-text token probe matched the nested example
`dreamina login checklogin`. The exact output hash already matched the accepted
baseline, so the generated parsed record was corrected to scope root-command
presence to the Built-in Commands section. The root help command was not
reinvoked. The record now separately states that the nested login example is
documented while the top-level root command is absent.

Multimodal2video help matched the bound `2739`-byte baseline and SHA-256
`fb3aa97d2d33b1d745a52519eac529c4a21a2d90aef9f1f6a452442fcf884277`.
The required repeatable image/video/audio inputs, Prompt, duration `4-15` with
default `5`, ratio `16:9`, `720p`, `seedance2.0_vip`, session, `--poll 0`, help,
and version contracts were present. No unexpected upload-timeout, concurrency,
preupload, upload-only, cache, reuse, or direct remote-input control appeared.

## 7. Account Viability And Credit Gate

`user_credit` completed successfully using the existing session. The output was
parseable and contained a numeric available-credit value. No login, relogin,
logout, checklogin, or authentication repair was invoked.

Accounting was re-derived from current bound evidence:

| Field | Value |
| --- | --- |
| Fixed manifest task count | `84` |
| Completed fixed task count | `13` |
| Post-submit reserve floor | `560` |
| Fixed macro threshold | `5530` |
| One-operation reserve threshold | `630` |
| Stricter current threshold | `5530` |
| Required pre-submit credit | `5530` |
| Credit gate | `PASS` |

The numeric live balance exists only in
`F07R-account-viability-001.parsed_account_viability.json`. It is absent from
the sanitized envelope, this report, the preflight summary, and the final
receipt. No account identifier or account name was persisted in D2 evidence.

## 8. Support Tests

Command:

`python -m pytest -q tests/test_f07r_support_contract.py`

Actual result:

- collected: `201`;
- passed: `200`;
- failed: `0`;
- skipped: `1`;
- skip reason: `POSIX permission bits are not stable on Windows`.

Support tests gate: `PASS`.

## 9. Provider And Authority State

The following counts remain zero:

- provider submit;
- provider task created;
- query;
- download;
- retry;
- resubmit;
- batch;
- provider credit charged;
- login, relogin, logout, and checklogin;
- F08.

The provider submit allowance remains unconsumed. `provider_eligibility=true`
means only that the bounded no-provider preflight passed. It does not grant
submission permission.

These flags remain false:

`binding_authorized`, `binding_active`, `package_authorized`, `package_active`,
`execution_authority_active`, `provider_command_allowed`, `submit_authorized`,
`query_authorized`, `download_authorized`, `retry_authorized`,
`resubmit_authorized`, `batch_authorized`, `final_master`, and `locked`.

## 10. Explicit Non-Actions

- No provider task was created or contacted.
- No submit, query, download, retry, resubmit, batch, or F08 action occurred.
- No login or authentication repair occurred.
- No web UI was opened or operated.
- No real claim, execution record, runtime integration, or media was created.
- No Source, CAL-001 global state, binding, existing route state, package,
  manifest, Prompt, fixture, media, executable, authorization history, or
  historical evidence was modified.
- Unrelated untracked workspace noise was not staged or altered.

## 11. Final Decision

All static, duplicate-prevention, executable, version, root-help,
multimodal2video-help, account-viability, credit, and support-test gates passed.

Decision:

`NO_PROVIDER_CANARY_AND_PREFLIGHT_ONLY_PASSED_AWAITING_SUBMIT_AUTHORIZATION`

This phase does not authorize a submit. The next required phase is:

`RETURN_TO_CHATGPT_FOR_ONE_SUBMIT_AUTHORIZATION_DECISION`
