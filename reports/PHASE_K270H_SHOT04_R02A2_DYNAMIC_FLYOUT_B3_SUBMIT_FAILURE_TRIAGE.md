# PHASE K270H - SHOT-04 R02A2 Dynamic Fly-Out B3 Submit Failure Triage

## 1. Phase summary

- phase_id: K270H_SHOT04_R02A2_DYNAMIC_FLYOUT_B3_SUBMIT_FAILURE_TRIAGE_NO_QUERY_REPORT_ONLY
- purpose: record report-only failure triage after K270G B3 one-submit-only returned exit code 1 with no submit_id.
- mode: report-only failure triage
- live_execution_authorized: false
- Dreamina_run_in_K270H: false
- submit_count_in_K270H: 0
- query_count_in_K270H: 0
- download_count_in_K270H: 0
- failure_triage_recorded: true
- final_master: false
- locked: false

## 2. K270G failure carry-forward

- K270G_phase: K270G_SHOT04_R02A2_DYNAMIC_FLYOUT_B3_ONE_SUBMIT_ONLY
- selected_variant_submitted: B3_RESULT_ONLY_FLYOUT_AFTER_HIT
- selected_asset_id: SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001
- submit_executed: true
- submit_count: 1
- B1_submit_executed: false
- command_exit_code: 1
- submit_id: none returned
- logid: none returned
- gen_status: none returned
- credit_count: none returned
- stdout_present: false
- stderr_present: false
- outcome_status: submit_failed_no_task_created
- K270G_recommended_next_phase: K270G_FAILURE_TRIAGE_NO_QUERY

Triage interpretation: K270G stopped correctly after the single authorized submit attempt. No remote task was confirmed because the process returned no submit_id, logid, gen_status, or credit_count.

## 3. Successful preflight evidence

K270G recorded these checks as passed before submit:

- git/source preflight passed.
- `sources/` was clean.
- Dreamina executable path: `C:/Users/msjpurf/bin/dreamina.exe`
- version canary passed: version `2a20fff-dirty`, commit `2a20fff`, build_time `2026-06-26T06:36:39Z`
- `user_credit` passed with vip_level `maestro`
- `multimodal2video -h` passed
- command contract passed
- B3 prompt/package/manifest/review-notes hashes matched
- two locked refs existed, were readable, and hash-matched
- no `--download_dir` was used
- `--poll 0` was used
- no query/download/retry/resubmit/batch was performed

K270H did not rerun Dreamina or canary commands.

## 4. B3 package evidence

| artifact | path | expected_sha256 | actual_sha256 | bytes | result |
|---|---|---|---|---:|---|
| B3 prompt | `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001_multimodal2video_no_submit_prompt.txt` | `b730505bf810fcb4e66e008aafd723412ff22ffd1cc404fd3401241250ee53f0` | `b730505bf810fcb4e66e008aafd723412ff22ffd1cc404fd3401241250ee53f0` | 1472 | pass |
| B3 package | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001_package.json` | `34b23610029f4d40da22d3c4595e0de1c185bff382f6fd30f915dfb8cddcb3d8` | `34b23610029f4d40da22d3c4595e0de1c185bff382f6fd30f915dfb8cddcb3d8` | 4367 | pass |
| manifest | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-K270D_dynamic_flyout_no_submit_manifest.csv` | `379d1a248d3f8eb9ff06686f2e418bf85fcc13dc152a97949b2487658c5be100` | `379d1a248d3f8eb9ff06686f2e418bf85fcc13dc152a97949b2487658c5be100` | 1638 | pass |
| review notes | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-K270D_dynamic_flyout_no_submit_review_notes.md` | `76927359d8962ae4e4e1d39038042fade3fa18d777dbcd2059a0e7471fa7b671` | `76927359d8962ae4e4e1d39038042fade3fa18d777dbcd2059a0e7471fa7b671` | 2815 | pass |
| @FENSHOU_LOCKED_REF | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | 1959523 | pass |
| @SHUANGJI_LOCKED_REF | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | 3874061 | pass |

B3 package fields:

- task_type: multimodal2video
- model_version: seedance2.0_vip
- duration: 5
- ratio: 16:9
- video_resolution: 720p
- poll: 0
- refs_count: 2
- active_refs_count: 2
- no_submit: true
- submit_authorized: false in package metadata before K270F/K270G authorization chain
- query_authorized: false
- download_authorized: false
- retry_authorized: false
- resubmit_authorized: false
- batch_authorized: false
- final_master: false
- locked: false

## 5. Prior successful Variant A M2V comparison

Earlier Variant A simplified two-ref M2V chain:

- K269O one-submit-only executed exactly one `multimodal2video` submit.
- K269O command_exit_code: 0
- K269O submit_id: `df668f21-6bf2-416e-964f-7dfc73995518`
- K269O logid: `20260701231448169254047008411529F`
- K269O gen_status: `querying`
- K269O credit_count: 70
- K269Q query-only returned `gen_status=success`, queue_status `Finish`, result_videos_count `1`, download_url_present `true`.
- K269S download-only downloaded one local mp4 and verified local metadata/hash.

Common factors between successful Variant A and failed B3:

- CLI family: PowerShell Dreamina `multimodal2video`
- executable family: `C:/Users/msjpurf/bin/dreamina.exe`
- refs_count: 2
- reference files: same Fenshou and Shuangji locked refs
- model_version: seedance2.0_vip
- duration: 5
- ratio: 16:9
- video_resolution: 720p
- poll: 0
- no `--download_dir` during submit
- submit/query/download separated by phase authorization

Material differences:

- Variant A prompt/package path and asset id differ from B3.
- Variant A diagnostic centered contact/hit-stop M2V identity-preserving behavior.
- B3 prompt is result-only dynamic fly-out after hit-stop, emphasizing launched/sliding backward, multi-body-length displacement, explosive launch, force path, and strict negatives against re-solving contact.

Conclusion: K270G does not prove global M2V is broken. The same two-ref M2V command family succeeded earlier in K269O/K269Q/K269S.

## 6. B3 vs B1 comparison

| field | B3 primary | B1 backup |
|---|---|---|
| variant_id | B3_RESULT_ONLY_FLYOUT_AFTER_HIT | B1_WIDE_SIDE_FLYOUT_RESULT_SHOT |
| asset_id | SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001 | SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B1-WIDE-SIDE-M2V-001 |
| priority | primary | secondary |
| prompt_sha256 | `b730505bf810fcb4e66e008aafd723412ff22ffd1cc404fd3401241250ee53f0` | `da7cf66aef229418b08d8c60b4ea3b79213abfb80ba106cd557d2c424500c6c9` |
| package_sha256 | `34b23610029f4d40da22d3c4595e0de1c185bff382f6fd30f915dfb8cddcb3d8` | `2260f53984a047b9ab953b61cf585f3a79ed508cf8b49dc3e8ea25f99555e477` |
| route focus | result-only fly-out after hit; avoid contact re-solving | wide side or three-quarter result shot with readable distance |
| staging burden | narrower contact burden, more abstract/result-only motion | more explicit side/left-right staging burden |
| K270E status | selected primary for future authorization | backup with nonblocking wording notes |
| K270G status | submitted once, failed before task id | not submitted |
| submit authorization now | consumed by K270G one-submit-only | not authorized |

Both prompts share the same task type, model, duration, ratio, resolution, poll, refs, strict negatives, and static/dynamic Beat A to Beat B strategy. B1 may behave differently, but it was not authorized and has higher staging/composition risk.

## 7. Failure class analysis

Ruled out or likely false:

- canary_failed: false; K270G recorded version/user_credit/help success.
- command_contract_block: likely false; K270G recorded command-contract pass against `multimodal2video -h`.
- ref_missing_or_hash_mismatch: false; both refs existed and hash-matched.
- package_defect: not supported by current evidence; JSON/manifest/prompt hashes and package flags matched.
- global_m2v_route_broken: likely false; Variant A M2V submitted, queried, downloaded, and produced media earlier.
- no_query_possible: true; no submit_id exists.

Possible but not proven:

- b3_prompt_or_content_boundary_possible: true. B3 uses intense/result-only action wording around impact release, launch, displacement, force, debris, and strict negatives. This may be more provider-sensitive than Variant A.
- package_specific_invocation_failure_possible: true. The package path, asset id, prompt text, and dynamic intent differ materially from Variant A even though the command family and refs match.
- transient_m2v_provider_boundary_possible: true. Empty stdout/stderr plus exit code 1 can be consistent with a provider/upload/transport edge that did not produce a structured CLI error.
- local_cli_process_failure_possible: possible but not primary. Canary and prior M2V success reduce confidence in this as a global local CLI failure.
- content_safety_or_provider_rejection_possible: possible but unproven. There is no returned error text, status body, or provider rejection code to assert this.
- upload_transport_failure: possible but unconfirmed. No submit_id or upload error string was returned, so this cannot be classified with the same confidence as prior explicit upload-timeout evidence.

Primary triage classification:

```text
submit_failed_no_task_created_with_empty_output
```

Likely next investigation target:

```text
B3-specific prompt/package/provider boundary, not global M2V failure
```

## 8. Log/diagnostic metadata if inspected

K270H did not inspect auth/session/token/key/env files and did not read or print sensitive runtime configuration.

Non-sensitive local capture metadata inspected:

| capture | path | exists | bytes | last_write |
|---|---|---:|---:|---|
| K270G stdout capture | `C:\Users\msjpurf\AppData\Local\Temp\k270g_dreamina_stdout.txt` | true | 0 | 2026-07-02 15:50:12 |
| K270G stderr capture | `C:\Users\msjpurf\AppData\Local\Temp\k270g_dreamina_stderr.txt` | true | 0 | 2026-07-02 15:50:12 |

Interpretation: the local capture files confirm the K270G report's empty stdout/stderr summary. No signed URL, token, cookie, session, auth, env, or user-secret material was printed.

## 9. Query impossibility and authorization boundary

- no valid submit_id exists from K270G.
- no logid exists from K270G.
- no gen_status exists from K270G.
- query would have no valid target.
- query is also not authorized in K270H.
- download is impossible and not authorized.
- retry/resubmit are not authorized.
- B1 submit is not authorized.

Boundary conclusion:

```text
no_query_possible=true
```

Any future live action requires a separate human authorization phase.

## 10. Route options

### Option A: create_B3_safe_simplified_no_submit_revision

- description: create a later no-submit revised B3-safe package that keeps result-only flyout but simplifies language, reduces violent/impact wording, and emphasizes cinematic displacement, rain spray, body travel, and recovery trajectory instead of forceful harm.
- value: may avoid provider/content/prompt boundary while preserving the B3 route.
- risk: requires new authorization and package creation; later submit remains uncertain.
- K270H assessment: preferred.

### Option B: consider_B1_backup_authorization_later

- description: use existing B1 wide-side backup as a future separate authorization candidate.
- value: B1 has more staging context and may behave differently than B3.
- risk: B1 has higher composition/staging burden and was not authorized for submit.
- K270H assessment: valid later fallback, not current recommendation.

### Option C: one_later_controlled_retry_of_same_B3

- description: authorize a later same-B3 retry only if triage strongly indicates transient provider issue.
- value: no package change.
- risk: could repeat empty failure and consume another attempt without learning much.
- K270H assessment: not recommended from current evidence.

### Option D: switch_to_text2video_dynamic_flyout_diagnostic

- description: create a future T2V diagnostic for fast flyout without image refs.
- value: bypasses M2V/ref-upload/provider path.
- risk: identity continuity likely weaker; diagnostic only.
- K270H assessment: useful fallback if B3-safe revision or B1 are rejected.

### Option E: pause_dynamic_flyout_submit_route

- description: stop live generation and retain package/failure evidence.
- value: no more spend/risk.
- risk: no dynamic flyout candidate.
- K270H assessment: valid stop option, not preferred if the shot still needs a dynamic fly-out beat.

## 11. Recommended route

Recommended route:

```text
recommend_B3_safe_simplified_no_submit_revision_before_any_retry_or_B1_submit
```

Reasoning:

- K270G failed before task creation with no submit_id, so query is impossible.
- K269O/K269Q/K269S prove that two-ref M2V can still work in this environment.
- B3's route concept remains aligned with K269Z/K270A/K270B static/dynamic insight, but the wording may be too intense or provider-sensitive.
- A blind retry of the same B3 package would test little and may repeat the empty failure.
- B1 remains backup-only and not authorized; it also has higher staging risk.
- A safer B3 no-submit revision can preserve the result-only fly-out concept while reducing prompt/content/provider-boundary risk.

## 12. Recommended next phase

- recommended_next_phase: K270I_SHOT04_R02A2_DYNAMIC_FLYOUT_B3_SAFE_REVISION_AUTHORIZATION_DECISION

K270I should be report-only and ask whether the human authorizes a later no-submit B3-safe/simplified package revision.

K270I must not:

- run Dreamina
- submit
- query
- download
- retry
- resubmit
- batch
- create media
- create prompt/package/manifest files unless explicitly authorized in a later package-creation phase
- final
- lock

## 13. Source governance confirmation

- Official Project Source files remain human-controlled.
- Codex read `sources/` as read-only context only.
- `sources/` status was clean before K270H report creation.
- sources_modified: false
- source_updates_created: false
- source_updates_staged: false
- this_report_is_official_Source: false

Read-only Source context included:

- `sources/AI视频制作_Source索引与使用优先级_V1.10.md`
- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`
- `sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/dreamina_cli_help_latest.md`
- `sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
- `sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`

## 14. Explicit non-actions

K270H did not:

- run Dreamina
- run `dreamina version`
- run `dreamina user_credit`
- run Dreamina help
- submit
- query_result
- list_task
- download
- retry
- resubmit
- batch
- submit B1
- create media
- cut video
- assemble cuts
- modify any mp4
- extract frames
- create contact sheets
- create prompt files
- create package JSON
- create manifest CSV
- modify prompt files
- modify package JSON files
- modify manifest CSV files
- modify review notes
- modify sources/
- stage media
- stage generated cuts
- stage review artifacts
- set final_master=true
- set locked=true
- tag
- print token/cookie/session/auth/env/signed URL contents

## 15. Safety flags

- no_Dreamina: true
- no_submit: true
- no_query: true
- no_download: true
- no_retry_resubmit: true
- no_batch: true
- no_media_created: true
- no_video_cut: true
- no_video_modified: true
- no_frames_contact_sheets_created: true
- no_prompt_package_manifest_modified: true
- no_sources_modified: true
- B1_submit_authorized: false
- B1_submit_executed: false
- no_valid_submit_id_exists: true
- no_query_possible: true
- final_master: false
- locked: false

## 16. Final verdict

K270H_B3_SUBMIT_FAILURE_TRIAGE_RECORDED_READY_K270I_SAFE_REVISION_AUTHORIZATION_DECISION
