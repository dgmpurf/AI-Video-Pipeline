# CAL-001 P3D W01 F07R Dreamina Help Refresh No-Provider Audit Result

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_DREAMINA_HELP_REFRESH_NO_PROVIDER_AUDIT`
- Starting checkpoint: `91f094ceccf86624349ea36192de23be58316925`
- Repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- Branch: `main`
- Scope: exactly three no-provider Dreamina version/help invocations, in-memory comparison, and this report
- Primary decision: `HELP_UNCHANGED_NO_UPLOAD_CONTROL_FOUND`
- Execution authority active: `false`
- Provider command allowed: `false`
- Final master: `false`
- Locked: `false`

No generation, account, login, credit, submit, query, download, retry, resubmit, batch, F08, web UI, executable-update, network-change, media, Source, or CAL-001 state authority was activated.

## 2. Canonical Authorization Verification

The exact canonical authorization was treated as one continuous UTF-8 string:

```text
APPROVE_CAL001_P3D_W01_F07R_DREAMINA_HELP_REFRESH_NO_PROVIDER_AUDIT_BIND_STARTING_HEAD_91F094CECCF86624349EA36192DE23BE58316925_AUTHORIZE_DREAMINA_VERSION_COUNT_1_DREAMINA_ROOT_HELP_COUNT_1_DREAMINA_MULTIMODAL2VIDEO_HELP_COUNT_1_ONLY_AND_READ_ONLY_COMPARISON_WITH_COMMITTED_DREAMINA_HELP_EXECUTION_CONTRACTS_AND_PRIOR_F07_HELP_EVIDENCE_TO_IDENTIFY_ANY_CHANGED_COMMANDS_OPTIONS_DEFAULTS_UPLOAD_TIMEOUT_CONCURRENCY_BATCH_PARALLEL_PREUPLOAD_RESOURCE_CACHE_ASSET_REUSE_REVIEW_OR_FILE_HANDLING_SEMANTICS_REQUIRE_NO_PROVIDER_NO_SUBMIT_NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_LOGIN_NO_CHECKLOGIN_NO_USER_CREDIT_NO_BATCH_EXECUTION_NO_F08_NO_WEB_UI_OPERATION_NO_EXECUTABLE_INSTALL_UPDATE_REPLACE_PATCH_OR_RENAME_NO_NETWORK_PROXY_FIREWALL_DNS_CREDENTIAL_SESSION_MEDIA_SOURCE_STATE_DATASET_PROMPT_PACKAGE_MANIFEST_OR_HISTORY_CHANGE_ALLOW_ONE_BOUNDED_HELP_REFRESH_AUDIT_REPORT_COMMIT_AND_PUSH_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

Independent Python standard-library verification, completed before invoking Dreamina:

| Fact | Result |
| --- | --- |
| Encoding | UTF-8 |
| Byte length | `918` |
| SHA-256 | `12fc7646e0f7cc1f3ba0653aee4251e00308d591773380c9ad079b0c77edc4d7` |
| Locally derived Base64 length | `1224` |
| Base64 decode count | `1` |
| Byte-for-byte round trip | `true` |
| BOM / CR / LF | `false / false / false` |
| Trailing space / Markdown fence | `false / false` |
| Last character / byte | `period / 2E` |

Accepted repository compiler/verifier result over the same bytes:

- Serialization profile valid: `true`
- Authorization evidence verified: `true`
- Authorization verified: `true`
- Checkpoint binding verified: `true`
- Required checkpoint, local HEAD, and `origin/main`: all `91f094ceccf86624349ea36192de23be58316925`
- Eligibility output activated: `false`
- Execution authority active: `false`
- Provider command allowed: `false`
- Provider command invocation count: `0`
- Authorized operation count consumed: `0`

The authorization admitted only the three named local version/help invocations. It did not activate provider authority.

## 3. Repository And F07 Route-Stop Preflight

Preflight passed before any Dreamina invocation:

- Repository and branch correct: `true`
- Local HEAD equals required checkpoint: `true`
- `origin/main` equals required checkpoint: `true`
- Staged files: none
- Unexpected tracked modifications: none
- `sources/` clean: `true`
- Worktrees: one primary worktree only
- Unrelated untracked workspace noise: left untouched
- Provider operation after the bound checkpoint: none recorded
- Original experiment: `CAL001-F07-P1-R1`
- F07 task state: `recovery_submit_failed_route_reset_required`
- F07 total submit attempts: `2`
- F07 recovery submit attempts: `1`
- Query / download / retry / resubmit counts: `0 / 0 / 0 / 0`
- F07 CLI submit route stopped: `true`
- Route reset required: `true`
- Third F07 submit permitted: `false`
- F07 authorized: `false`
- Execution authority active: `false`

The CAL-001 state file SHA-256 remained:

`54ff10de1d68cd82f4522c1984eb6f19fa30f8a6beececa618968d6ba30bee92`

Both orphaned handles remained quarantined:

| Handle | Provider task created | Query eligible | Download eligible | Reuse authorized |
| --- | --- | --- | --- | --- |
| `5a69007b-ac19-4cef-86bc-41d19792149f` | `false` | `false` | `false` | `false` |
| `d5fa2ba3-f4b4-4a8f-9591-5b22b1fac463` | `false` | `false` | `false` | `false` |

## 4. Executable Binding Before Invocation

Only ordinary filesystem metadata was inspected. The executable was not reverse-engineered or changed.

- Path: `C:/Users/msjpurf/bin/dreamina.exe`
- Exists and is a regular non-symlink file: `true`
- Bytes: `31879680`
- SHA-256: `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- Creation time UTC: `2026-07-01T08:36:08.166147Z`
- Modification time UTC: `2026-07-01T08:36:12.584658Z`
- Prior expected bytes/hash match: `true`
- Executable hash changed: `false`

## 5. Exact Runtime Invocation Receipt

All commands used argument-vector process invocation with `shell=false`. Output was captured in memory. No command was retried, aliased, or substituted.

| Count | Exact argument vector | Started UTC | Completed UTC | Duration | Exit | Raw stdout | Raw stdout SHA-256 | Raw stderr | Sensitive content |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | `C:/Users/msjpurf/bin/dreamina.exe version` | `2026-07-20T14:17:01.523189Z` | `2026-07-20T14:17:04.779278Z` | `3256.089 ms` | `0` | `96 bytes` | `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0` | `0 bytes` | `false` |
| 1 | `C:/Users/msjpurf/bin/dreamina.exe -h` | `2026-07-20T14:17:04.779278Z` | `2026-07-20T14:17:07.318718Z` | `2539.440 ms` | `0` | `2673 bytes` | `a7730ec92f51b4c992605d008e5533ea984c0c799b25a8490048a8b372883c81` | `0 bytes` | `false` |
| 1 | `C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h` | `2026-07-20T14:17:07.319716Z` | `2026-07-20T14:17:09.845514Z` | `2525.798 ms` | `0` | `2739 bytes` | `fb3aa97d2d33b1d745a52519eac529c4a21a2d90aef9f1f6a452442fcf884277` | `0 bytes` | `false` |

For all three commands:

- Sanitized output bytes and hashes equal the raw output bytes and hashes because no redaction was required.
- Raw and sanitized stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Timeout: `false`.
- No user-specific path, token, cookie, session value, signed URL, credential, device code, or private information was present.

Exact invocation counters after closure:

- `dreamina version`: `1 / 1`
- `dreamina -h`: `1 / 1`
- `dreamina multimodal2video -h`: `1 / 1`
- Total Dreamina commands: `3`
- All other Dreamina commands: `0`

## 6. Current Version Result

Normalized version result:

| Field | Current | Prior committed | Change |
| --- | --- | --- | --- |
| Version | `2a20fff-dirty` | `2a20fff-dirty` | `UNCHANGED` |
| Commit | `2a20fff` | `2a20fff` | `UNCHANGED` |
| Build time | `2026-06-26T06:36:39Z` | `2026-06-26T06:36:39Z` | `UNCHANGED` |

The current version-output SHA-256 exactly matches prior committed version evidence. Version changed: `false`.

## 7. Normalized Root Help

Invocation behavior:

- Usage: `dreamina [flags]`
- Exit code: `0`
- Stderr empty: `true`
- Positional arguments: none documented
- Root-specific flags: none documented in this output
- Help behavior: use `dreamina <subcommand> -h`

Built-in commands:

| Command | Normalized purpose |
| --- | --- |
| `help` | Display command help |
| `list_task` | List saved tasks and result summaries |
| `login` | Establish local OAuth device-flow login |
| `logout` | Clear local OAuth login state |
| `query_result` | Query an asynchronous generation task |
| `relogin` | Clear login state and force fresh OAuth login |
| `session` | Create/list/search/rename/delete sessions |
| `user_credit` | Show account credit balance |
| `version` | Print build version and commit |

Generator commands:

`frames2video`, `image2image`, `image2video`, `image_upscale`, `multiframe2video`, `multimodal2video`, `text2image`, `text2video`.

The command names, categories, and normalized descriptions are unchanged from the committed post-update root-help snapshot.

## 8. Normalized Multimodal2video Help

Invocation behavior and input contract:

- Usage: `dreamina multimodal2video [flags]`
- Exit code: `0`
- Stderr empty: `true`
- Inputs: any mix of image, video, and audio
- At least one image or video is required
- Local files are uploaded automatically before submit
- Limits: image `<=9`, video `<=3`, audio `<=3`; audio duration `2-15 seconds`
- Task is asynchronous; `--poll` can wait before falling back to `query_result`

Normalized options:

| Option | Type | Required/repeatable/default | Current semantics | Comparison |
| --- | --- | --- | --- | --- |
| `--image` | `stringArray` | Repeatable; one image or video required collectively | Local image path | `UNCHANGED` |
| `--video` | `stringArray` | Repeatable; one image or video required collectively | Local video path | `UNCHANGED` |
| `--audio` | `stringArray` | Repeatable; optional | Local audio path | `UNCHANGED` |
| `--prompt` | `string` | Optional | Multimodal edit prompt | `UNCHANGED` |
| `--duration` | `int` | Optional; default `5` | Range `4-15` seconds | `UNCHANGED` |
| `--ratio` | `string` | Optional; no default stated | `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9` | `UNCHANGED` |
| `--video_resolution` | `string` | Optional; no default stated | VIP: `720p`, `1080p`, `4k`; others: `720p` | `UNCHANGED` |
| `--model_version` | `string` | Optional; no default stated | `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini` | `UNCHANGED` |
| `--session` | `int` | Optional; default `0` | Session identifier | `UNCHANGED` |
| `--poll` | `int` | Optional; `0` disables polling | Poll at one-second intervals for up to N seconds | `UNCHANGED` |
| `-h`, `--help` | boolean | Optional alias pair | Display command help | `UNCHANGED` |
| `--version` | boolean global | Optional | Print build version | `UNCHANGED` |

The help does not state that repeated images are processed in ordered or unordered form. Repeatability is explicit; ordering semantics are not.

## 9. Exact And Semantic Comparison

Comparison targets:

- `sources/dreamina_cli_help_latest.md`
- Committed Dreamina CLI contracts V1.2, V1.3, and V1.4
- Committed Dreamina CLI workflow V1.2
- Committed macro authorization guidance V0.2
- `reports/diagnostics/DREAMINA_CLI_HELP_SNAPSHOT_AFTER_UPDATE_20260701.md`
- Initial and recovery F07 help evidence
- F07 CLI route-reset report

Exact-output comparison:

- Root help current SHA-256 `a7730ec...3c81` exactly matches the extracted committed post-update root-help bytes. `exact_changed=false`.
- Current multimodal2video SHA-256 is `fb3aa97...84277`.
- The initial F07 envelope persisted a sanitized hash `50b2137c...308d` after replacing the harmless example prompt text with `<redacted_prompt>`. Reapplying the known original example to that evidence yields `2739` bytes and current SHA-256 `fb3aa97...84277` exactly.
- Against the initial F07 runtime evidence under the same sanitizer normalization, `exact_changed=false`.
- The July 1 Markdown snapshot differs from the current multimodal2video bytes only by one trailing space after the `--session` description. That is whitespace-only snapshot normalization, not a semantic change.
- The recovery F07 envelope stores a normalized contract summary rather than exact raw help, so it is exact-output `UNCOMPARABLE` but semantically consistent.

Semantic comparison:

| Category | Result |
| --- | --- |
| Root commands added/removed | none / none |
| Multimodal2video options added/removed | none / none |
| Options renamed | none |
| Defaults changed | none |
| Allowed values changed | none |
| Required/optional status changed | none |
| Repeatability changed | none |
| Descriptions materially changed | none |
| Examples materially changed | none |
| Help/exit behavior changed | none |

Root semantic change: `false`. Multimodal2video semantic change: `false`.

## 10. Upload-Relevant Capability Search

| Capability | Result | Exact current evidence or limitation |
| --- | --- | --- |
| Upload | `FOUND_EXPLICIT_DESCRIPTION` | Local files are uploaded automatically before submit. |
| Upload timeout | `NOT_FOUND` | No option or description. |
| Request timeout | `NOT_FOUND` | No option or description. |
| Total command timeout | `NOT_FOUND` | `--poll` controls post-submit polling only. |
| Deadline / session lifetime | `NOT_FOUND` | No upload deadline or session-lifetime contract. |
| Concurrency / concurrent / parallel upload | `NOT_FOUND` | No option or description. |
| Batch upload | `NOT_FOUND` | No option or description. |
| Repeated image behavior | `FOUND_EXPLICIT_OPTION` | `--image stringArray`, repeat for each local path. |
| Repeated image ordering | `AMBIGUOUS` | Repeatability is documented; ordering is not. |
| Pre-upload / upload-only | `NOT_FOUND` | No command or option. |
| Resource ID / URI / asset ID | `NOT_FOUND` | Local paths only. |
| Cached asset / cache / deduplication / reuse | `NOT_FOUND` | No command or option. |
| Review | `FOUND_EXPLICIT_DESCRIPTION` | Root help says `list_task` can review saved tasks; this is not upload or media reuse. |
| Audit / moderation | `NOT_FOUND` | No option or reusable artifact contract. |
| Approval | `FOUND_EXPLICIT_DESCRIPTION` | Some models may require web authorization confirmation; this is not upload control. |
| File preprocessing | `NOT_FOUND` | No preprocessing controls documented. |
| MIME / format | `NOT_FOUND` | No MIME or format contract documented. |
| Maximum file size | `NOT_FOUND` | Count limits only. |
| Total input size | `NOT_FOUND` | No byte-size limit documented. |
| Image count | `FOUND_EXPLICIT_DESCRIPTION` | Image count limit is `9`. |
| Local path handling | `FOUND_EXPLICIT_DESCRIPTION` | Local images/videos/audio are auto-uploaded. |
| Direct remote URL/resource input | `NOT_FOUND` | No remote input option. |
| Polling | `FOUND_EXPLICIT_OPTION` | `--poll`; `0` disables, positive N polls one-second intervals. |
| Asynchronous submit behavior | `FOUND_EXPLICIT_DESCRIPTION` | Help states task submission is asynchronous. |

No option name was treated as proof of undocumented internal behavior.

## 11. Focused Questions

1. Version changed from `2a20fff-dirty`: **No, directly proven unchanged.**
2. Executable byte count or SHA-256 changed: **No, directly proven unchanged.**
3. Root command list changed: **No, directly proven unchanged against the committed snapshot.**
4. Multimodal2video option set changed: **No, directly proven semantically unchanged.**
5. New upload timeout, command timeout, parallel/concurrent upload, batch upload, pre-upload, upload-only, resource/asset reuse, cached reuse, review/moderation reuse, or direct remote-resource input: **None found.**
6. Repeated `--image` support remains: **Yes, directly proven.**
7. Ordered versus unordered repeated-image handling documented: **No; `UNKNOWN` beyond repeatability.**
8. Defaults changed: **No.** Duration remains `5`; poll `0` still disables polling; model, ratio, and resolution defaults remain unstated in this help.
9. Newly documented mechanism addressing the approximately `93.1 s` F07 cluster without changing media/network: **`NOT_SUPPORTED`; none is present.**
10. Current help materially changes the route-reset recommendation: **`NOT_SUPPORTED`; it does not.**

## 12. Decision And Route Implication

Primary decision:

`HELP_UNCHANGED_NO_UPLOAD_CONTROL_FOUND`

Classification confidence: `HIGH`

Basis:

- Same executable binding and version.
- Root command list and multimodal2video semantic contract unchanged.
- No upload timing, concurrency, pre-upload, cache/reuse, upload-only, or remote-resource control exists in current help.
- No current help mechanism addresses the approximately 93.1-second failure cluster.

Limitations:

- CLI help documents public options, not internal uploader implementation or provider/network behavior.
- The prior initial F07 exact help evidence used deterministic prompt-example redaction; comparison normalized that known transformation.
- The recovery F07 evidence retained a semantic contract summary rather than full raw bytes.
- No provider call was permitted, so no behavior beyond version/help presence was tested.

Recommended next phase:

`F07R_ROUTE_SELECTION_AFTER_HELP_REFRESH`

That future decision may compare human web-upload evidence formalization, a new hashed-media optimization route, a human-controlled network-path route, and a separately validated CLI build/session route. This report authorizes none of them. Any future provider operation requires a new experiment identity and fresh checkpoint-bound human authorization; it cannot be a third `CAL001-F07-P1-R1` submit.

## 13. Boundary And Integrity Confirmation

- Dreamina called: `true`, exactly three authorized local version/help calls
- Dreamina total command count: `3`
- User credit / provider / submit / query / download: `false / false / false / false / false`
- Retry / resubmit / login / checklogin / batch / F08: all `false`
- Web UI operated: `false`
- Executable installed, updated, replaced, patched, renamed, or modified: `false`
- Network/proxy/firewall/VPN/DNS changed: `false`
- Media modified: `false`
- `sources/` touched: `false`
- CAL-001 state changed: `false`
- Datasets changed: `false`
- Prompt/package/manifest changed: `false`
- Historical execution evidence changed: `false`
- Original F07 CLI route remains closed: `true`
- Third original F07 submit permitted: `false`
- Both orphaned handles remain quarantined and non-queryable: `true`
- Final master: `false`
- Locked: `false`

## 14. Final Verdict

`CAL001_P3D_W01_F07R_DREAMINA_HELP_REFRESH_NO_PROVIDER_AUDIT_COMPLETE_HELP_UNCHANGED_NO_UPLOAD_CONTROL_FOUND`
