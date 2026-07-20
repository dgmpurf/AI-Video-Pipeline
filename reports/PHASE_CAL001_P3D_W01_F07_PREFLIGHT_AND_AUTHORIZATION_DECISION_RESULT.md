# CAL-001 P3D W01 F07 Preflight And Authorization Decision

## 1. Phase Summary

- phase: `CAL-001-P3D-W01_F07_PREFLIGHT_AND_AUTHORIZATION_DECISION`
- execution mode: bounded no-live, report-only
- starting checkpoint: `9cea10a41157c69967ce6b9235ba08942251bacf`
- decision: `READY_FOR_HUMAN_F07_AUTHORIZATION`
- decision meaning: offline readiness is established; F07 remains unauthorized and no live action may occur from this report
- proposed authorization status: `PROPOSED_ONLY_NOT_AUTHORIZED`
- F07 authorized: `false`
- execution authority active: `false`
- final_master: `false`
- locked: `false`

This phase called neither Dreamina nor a provider. It did not submit, query,
download, retry, resubmit, batch, execute F07, create media, or activate
authority.

## 2. Repository Preflight

| Check | Result |
| --- | --- |
| repository | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE` |
| branch | `main` |
| required starting HEAD | `9cea10a41157c69967ce6b9235ba08942251bacf` |
| starting local HEAD | `9cea10a41157c69967ce6b9235ba08942251bacf` |
| starting origin/main | `9cea10a41157c69967ce6b9235ba08942251bacf` |
| starting HEAD/origin alignment | `PASS` |
| staged files | none |
| unrelated tracked modifications | none |
| `git status --short -- sources/` | no output |
| temporary worktree residue | none |

Known unrelated untracked workspace noise was left untouched:

- `.vs/`
- `experiments/CAL-001/execution_records/P3B_R2_T2/evidence/`
- `experiments/CAL-001/execution_records/P3B_R2_T4/evidence/`
- `productions/chi_yan_tian_qiong/edits/`
- `productions/chi_yan_tian_qiong/review_artifacts/`
- `reports/context_recovery/`
- `reports/investor/`

## 3. Active Source Reconciliation

Both active Source files exist at the required checkpoint and were read without
normalization or mutation.

| Source file | Bytes | SHA-256 | UTF-8 | BOM | CR | LF | Final byte |
| --- | ---: | --- | --- | --- | ---: | ---: | --- |
| `sources/AI视频制作_Source索引与使用优先级_V1.12.md` | 11038 | `e13a98c4a12fab8ba3267b3074acf103e1458798fb865b6363ee3e732d275022` | strict valid | absent | 0 | 384 lone LF | `0A` |
| `sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md` | 9221 | `f5471b851c6966e6de73ea552b42f4cd00d06af6aec5164ccf47beb373368572` | strict valid | absent | 0 | 401 lone LF | `0A` |

The prior path `sources/AI视频制作_Source索引与使用优先级_V1.11.md` is absent and
is not active. The active V1.12 Source confirms:

- F06 is technically completed;
- `completed_fixed_task_count=13`;
- `remaining_fixed_task_count=71`;
- `next_experiment_id=CAL001-F07-P1-R1`;
- `F07_authorized=false`;
- historical credit balance `5625` is not a fresh F07 preflight;
- F06 success does not imply F07 authorization.

## 4. Authoritative Evidence Read

The audit read, at minimum:

- `sources/AI视频制作_Source索引与使用优先级_V1.12.md`
- `sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md`
- `sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/dreamina_cli_help_latest.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `docs/reference_library_v0_1/calibration/AI视频制作_模仿参考库Calibration流程_V0.1.md`
- `experiments/CAL-001/execution_state/CAL001_P3C_remaining_77_resumable_execution_state_contract.json`
- `experiments/CAL-001/manifests/CAL001A_fixed_84_task_manifest.csv`
- `experiments/CAL-001/matrices/CAL001_fixed_experiment_matrix.md`
- `experiments/CAL-001/prompts/F07/CAL001-F07-P1_prompt.txt`
- `experiments/CAL-001/packages/F07/CAL001-F07-P1-R1_package.json`
- `experiments/CAL-001/datasets/CAL001_experiment_results_template.csv`
- `experiments/CAL-001/datasets/CAL001_visual_review_template.jsonl`
- both W01 command-binding audit records
- F06 recovery visual-review and technical-completion records
- current authorization compiler implementation, CLI, focused tests, and latest independent audit

Protected artifact hashes remained:

| Artifact | SHA-256 |
| --- | --- |
| resumable execution state | `e42e92700d63e9f78a9ac9fb564f3d7410d94f4160dd6e047ab02eeaa02c205b` |
| experiment-results CSV | `f1d183267b24997bb848ff83abd9231b53d84ae82e715d9e4d9b5c2b3de3ff3b` |
| visual-review JSONL | `6f86873a445021f88503625008550c99e7a2ef323acde500d38ccd6a5e5c693a` |
| fixed 84-task manifest | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` |

## 5. Exact F07 Task Contract

### Identity And Purpose

- task ID / accepted manifest row identity: `CAL001-F07-P1-R1`
- experiment ID: `CAL001-F07-P1-R1`
- wave: `W01`
- current decision phase: `CAL-001-P3D-W01_F07_PREFLIGHT_AND_AUTHORIZATION_DECISION`
- fixed-definition package phase: `CAL-001-P1-R2`
- family: `F07 MULTIMODAL_FORCE_REACTION_CAUSALITY`
- prompt architecture: `P1_LEGACY_DESCRIPTIVE`
- replicate index: `1`
- actual operation type: `multimodal2video`
- purpose: test readable force-to-reaction causality while preserving two identities, grounded spatial staging, and restrained rainy-environment feedback

### Exact Provider Prompt

```text
In the rainy frontal temple, preserve Fenshou's black-red male identity and Shuangji's silver-blue female identity as two separate grounded subjects. Fenshou applies one short controlled forearm pressure to Shuangji's raised guard; the pressure causes Shuangji to yield one grounded half-step, with a small wet-floor response and natural sleeve and rain motion, then both recover in place. No injury, gore, airborne flyout, body-wall contact, wall damage, magic blast, identity swap, extra subject, or static pose-out.
```

- prompt file bytes: `1976`
- prompt file SHA-256: `094a01dee03f49b65badf1864873f2b85a74a9b801f6a26621a84fb0c409f681`
- extracted provider-prompt characters: `519`
- extracted provider-prompt SHA-256: `ca90c5b50b7d244b6264b8ed3f23d4043bf490d25d672e2d05cfad49b487594a`

The prompt is the fixed P1 descriptive calibration baseline. No prompt rewrite,
result-first conversion, or timing rewrite is authorized by this phase.

### Required Inputs

| Fixture | Reference duty | Local path | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| `CAL001-F07-IDENTITY-A` | acting-subject identity only; not force choreography or scene | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | 1959523 | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` |
| `CAL001-F07-IDENTITY-B` | receiving-subject identity only; not reaction choreography or scene | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | 3874061 | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` |
| `CAL001-F07-SCENE-01` | rainy environment and grounded layout only; not identity or wall interaction | `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | 4147285 | `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452` |

All three files exist, are readable, occur in the required order, and match
the manifest, package, state contract, and command-binding hashes. F07 requires
no video or audio input.

### Generation Parameters And Limits

| Field | Required value |
| --- | --- |
| executable environment | Windows PowerShell-visible CLI |
| executable path | `C:/Users/msjpurf/bin/dreamina.exe` |
| executable presence | exists; inspected only, not called |
| executable bytes | `31879680` |
| executable SHA-256 | `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10` |
| model | `seedance2.0_vip` |
| duration | `5` seconds |
| ratio | `16:9`, explicit |
| video resolution | `720p` |
| poll | `0` |
| input images | `3` repeated `--image` arguments |
| candidate / expected output count | `1` video, `0` images |
| planned provider credit cost | `70` |
| maximum future provider operation count | exactly `1` submit invocation, only after new human authorization |
| query | forbidden |
| download | forbidden |
| retry | forbidden |
| resubmit | forbidden |
| batch | forbidden |

The fixed command structure was independently consistent in both historical
W01 command-binding audits. It is evidence of argument construction only and
is not current authority:

```text
C:/Users/msjpurf/bin/dreamina.exe multimodal2video
  --model_version seedance2.0_vip
  --ratio 16:9
  --prompt <exact extracted provider prompt>
  --duration 5
  --video_resolution 720p
  --image productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
  --image productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
  --image productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
  --poll 0
```

Historical redacted argv SHA-256:
`e79a1d40c9b1e31e019fceb138fe42c455e7235325f1a7b5bc9ebb58e2e956f5`.

### Expected Output And Evidence Scope

The package reserves these later-use paths:

- output directory: `experiments/CAL-001/runs/CAL001-F07-P1-R1`
- planned output name: `CAL001-F07-P1-R1_result.mp4`
- submit evidence root: `experiments/CAL-001/execution_records/P3D_W01/CAL001-F07-P1-R1/`
- technical execution record: `experiments/CAL-001/execution_records/P3D_W01/CAL001-F07-P1-R1_technical_execution_record.json`

Neither the output directory nor the exact F07 execution-record directory
exists now. A future submit-only phase may persist sanitized canary/help,
pre-submit credit, one-submit, post-submit credit-reconciliation, and authority-
closure evidence under the bounded F07 evidence root. It may not create media,
query evidence, download evidence, review frames, or a contact sheet.

The package's later review plan applies only after separately authorized query
success and download: metadata, frames at 0/1/2/3/4 seconds, a final readable
frame, and a 3x2 contact sheet. That later artifact plan is not authorized now.

## 6. F07 Readiness Matrix

| Dependency | Classification | Evidence and interpretation |
| --- | --- | --- |
| repository path, branch, and starting checkpoint | `PASS` | local HEAD and origin/main both matched the required checkpoint |
| Source worktree cleanliness | `PASS` | no tracked or staged Source change |
| active Source reconciliation | `PASS` | V1.12 and authorization V0.1 exact bytes/hashes verified; V1.11 inactive |
| F06 technical completion | `PASS` | technical `PASS`, visual `PASS_WITH_LIMITATIONS`, calibration `BASELINE_SUCCESS_CASE` |
| fixed-task counters | `PASS` | completed `13`, remaining `71`, remaining-wave completed `6`; unchanged |
| next fixed task | `PASS` | state and active Source both identify `CAL001-F07-P1-R1` |
| F07 duplicate-operation state | `PASS` | pending_preflight; submit attempts `0`; submit_id/logid null; query/download counts `0` |
| current F07 provider operation count | `PASS` | `0`; no F07 execution/output/evidence directory exists |
| retry/resubmit count | `PASS` | `0`; both remain forbidden |
| F07 result and visual dataset rows | `PASS` | not_attempted/not_queried/not_started/unreviewed |
| prompt file and payload | `PASS` | path, file hash, extracted payload hash, and fixed architecture match |
| package | `PASS` | file hash and all task, input, parameter, count, cost, and permission fields match |
| manifest row | `PASS` | 84-row manifest hash verified; exact F07 row SHA-256 `84461634b31d8bfa7007376cbbe0c017be4a282abc3048872445e4a1fa9efab6` |
| identity A input | `PASS` | path, order, duty, existence, bytes, and SHA-256 match |
| identity B input | `PASS` | path, order, duty, existence, bytes, and SHA-256 match |
| scene input | `PASS` | path, order, duty, existence, bytes, and SHA-256 match |
| offline command binding | `PASS` | both W01 audits agree and all binding checks passed |
| current runtime command contract | `REQUIRES_FRESH_LIVE_PREFLIGHT` | runtime `multimodal2video -h` outranks the historical snapshot and was not called here |
| fresh canary | `REQUIRES_FRESH_LIVE_PREFLIGHT` | future live phase must run `dreamina version` and `dreamina user_credit` |
| fresh login viability | `REQUIRES_FRESH_LIVE_PREFLIGHT` | successful `user_credit` is the normal login/account gate; no historical login inference is allowed |
| conditional `checklogin` | `HUMAN_DECISION_REQUIRED` | only if login is missing; stop and require separately authorized human-assisted `login --headless` plus `login checklogin --device_code=...` rather than silently repairing login |
| fresh credit balance | `REQUIRES_FRESH_LIVE_PREFLIGHT` | historical `5625` is stale; pre-submit balance must be freshly read |
| dynamic credit floor | `PASS` as an offline derivation | `(84 - 13) * 70 + 560 = 5530`; future fresh balance must be at least `5530` |
| current-checkpoint F07 authorization | `HUMAN_DECISION_REQUIRED` | no authorization binds the post-report checkpoint; historical broad/F06 records are stale, consumed, closed, or explicitly exclude F07 |
| human visual review in submit-only phase | `NOT_APPLICABLE` | no media is available or authorized |
| later human visual review | `HUMAN_DECISION_REQUIRED` | required after separately authorized successful query/download before any final use |

No offline repair or missing-input creation is required. The fresh-live items are
mandatory gates inside a later separately authorized one-submit phase; they do
not authorize that phase and they do not convert this decision into live
authority.

## 7. Future Live Preflight Contract

A future exact human authorization should allow only these non-provider checks
before the one provider submit:

1. Reconfirm the bound checkpoint, branch, origin alignment, clean Source, zero
   duplicate-operation state, and all accepted hashes.
2. Run `dreamina version` exactly once.
3. Run pre-submit `dreamina user_credit` exactly once; require no logger,
   login, auth, or permission failure and require numeric total credit at least
   `5530`.
4. Run `dreamina multimodal2video -h` exactly once and rebind every package
   field to current runtime help.
5. If login is missing, stop without submit. A headless login/checklogin flow
   requires a separate human authorization and device-code interaction.
6. Persist sanitized preflight evidence atomically before continuing.
7. Invoke the exact F07 `multimodal2video` command at most once.
8. Persist the raw sanitized subprocess envelope before parsing.
9. Run post-submit `dreamina user_credit` at most once for credit
   reconciliation, even if the submit response is ambiguous.
10. Close authority after the single submit invocation, regardless of outcome.

The one-submit phase succeeds technically only if the response unambiguously
proves provider task creation and yields the required non-sensitive identifiers,
including a nonempty submit_id and logid, a numeric provider `credit_count=70`,
and an exact pre/post balance delta of `70`. Submit success does not mean
generation success. No query or download is permitted in that phase.

Technical stop conditions include:

- checkpoint, Source, accepted hash, path, order, or duplicate-state mismatch;
- logger, login, auth, permission, canary, account, or help mismatch;
- fresh balance below `5530`;
- inability to persist durable sanitized evidence atomically;
- local file/upload/transport failure;
- missing, malformed, ambiguous, or contradictory task-creation evidence;
- absent or mismatched submit_id, logid, credit_count, or credit delta;
- any attempt to exceed one provider submit or invoke query/download/retry/
  resubmit/batch.

Every stop closes authority, preserves non-sensitive evidence, performs no
retry or resubmit, and requires a new human decision.

## 8. Authorization Compiler Readiness

The independently accepted compiler/verifier remains available:

- library: `app/ai_video_pipeline/governance/authorization_serialization.py`
- CLI: `tools/authorization_compiler.py`
- focused tests: `tests/test_authorization_serialization.py` and
  `tests/test_authorization_compiler_cli.py`
- latest independent audit:
  `reports/PHASE_CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_STRICT_VALIDATION_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md`

Current focused validation result:

```text
124 passed in 1.82s
```

An independent in-memory boundary probe at the starting checkpoint confirmed:

| Combination | authorization verified | checkpoint verified | eligible | execution active | provider allowed |
| --- | --- | --- | --- | --- | --- |
| compile only | false | absent | false | false | false |
| compile result plus valid checkpoint | false | true | false | false | false |
| verified evidence without checkpoint | true | absent | false | false | false |
| checkpoint without verified evidence | false | true | false | false | false |
| verified noncontradictory evidence plus valid checkpoint | true | true | true | false | false |

All combinations preserved provider invocation count `0` and authorized
operation count consumed `0`. Eligibility does not activate authority.

## 9. Checkpoint-Bound Proposed Authorization

Status: `PROPOSED_ONLY_NOT_AUTHORIZED`.

The exact canonical phrase must bind the commit that contains this report.
That commit SHA cannot be embedded inside this tracked report without changing
the commit SHA again. Therefore:

- this report records the complete clause set and construction rule;
- the post-push receipt emits the one exact continuous canonical phrase with
  the actual ending HEAD substituted;
- only that post-push phrase is the proposed canonical text;
- neither this template nor the post-push phrase activates authority.

Non-canonical construction template:

```text
APPROVE_CAL001_P3D_W01_F07_ONE_MULTIMODAL2VIDEO_SUBMIT_ONLY_BIND_STARTING_HEAD_{POST_REPORT_HEAD}_AUTHORIZE_NO_PROVIDER_PREFLIGHT_DREAMINA_VERSION_COUNT_1_DREAMINA_USER_CREDIT_COUNT_MAX_2_DREAMINA_MULTIMODAL2VIDEO_HELP_COUNT_1_AND_PROVIDER_MULTIMODAL2VIDEO_SUBMIT_COUNT_1_ONLY_FOR_TASK_CAL001-F07-P1-R1_EXPERIMENT_CAL001-F07-P1-R1_WAVE_W01_MODEL_SEEDANCE2.0_VIP_DURATION_5_RATIO_16_9_VIDEO_RESOLUTION_720P_USING_ONLY_THE_EXACT_ACCEPTED_PROMPT_PACKAGE_MANIFEST_AND_THREE_ORDERED_IMAGE_INPUT_HASHES_REQUIRE_EXISTING_LOGIN_VALIDATED_BY_PRE_SUBMIT_USER_CREDIT_NO_LOGGER_AUTH_LOGIN_OR_PERMISSION_FAILURE_REQUIRE_FRESH_PRE_SUBMIT_TOTAL_CREDIT_AT_LEAST_5530_AND_POST_SUBMIT_EXACT_70_CREDIT_RECONCILIATION_IF_LOGIN_IS_MISSING_STOP_FOR_SEPARATE_HUMAN_ASSISTED_LOGIN_HEADLESS_AND_CHECKLOGIN_AUTHORIZATION_PERSIST_ONLY_SANITIZED_F07_PREFLIGHT_SUBMIT_CREDIT_RECONCILIATION_AUTHORITY_CLOSURE_AND_BOUNDED_STATE_EVIDENCE_CLOSE_AUTHORITY_AFTER_ONE_SUBMIT_INVOCATION_REGARDLESS_OF_RESULT_NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_F08_NO_SOURCE_DATASET_PROMPT_PACKAGE_MANIFEST_OR_MEDIA_CHANGE_NO_STATE_CHANGE_OUTSIDE_THE_EXACT_F07_SUBMIT_EVIDENCE_SCOPE_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

The template is not valid authorization because `{POST_REPORT_HEAD}` is not a
checkpoint. The final receipt must replace it with the exact lowercase 40-hex
post-report HEAD and mark the resulting text `PROPOSED_ONLY_NOT_AUTHORIZED`.

## 10. Protected State And Explicit Non-Actions

At the decision boundary:

```yaml
F06_technically_completed: true
completed_fixed_task_count: 13
remaining_fixed_task_count: 71
remaining_completed_task_count: 6
next_wave_id: W01
next_experiment_id: CAL001-F07-P1-R1
F07_task_state: pending_preflight
F07_submit_attempt_count: 0
F07_submit_id: null
F07_query_count: 0
F07_download_count: 0
F07_authorized: false
execution_authority_active: false
remaining_noncanary_tasks_authorized: false
provider_command_invocation_count_this_phase: 0
retry_count_this_phase: 0
resubmit_count_this_phase: 0
final_master: false
locked: false
```

This phase made no change to:

- official Source;
- CAL-001 execution state or counters;
- datasets;
- Prompt files;
- packages;
- manifests;
- authorization history;
- media or review artifacts.

## 11. Decision

`READY_FOR_HUMAN_F07_AUTHORIZATION`

Rationale: F06 completion, task order, counters, prompt/package/manifest
bindings, all three media inputs, fixed parameters, planned cost, command
structure, Source reconciliation, and authorization-compiler fail-closed
behavior are internally consistent. F07 has never been submitted. The only
remaining gates are intentionally live and must be rerun after a fresh exact
human authorization bound to the post-report checkpoint.

This is decision support only. It does not authorize Dreamina, provider access,
F07, login repair, submit, query, download, retry, resubmit, batch, final, or
lock.

## 12. Final Verdict

`CAL001_P3D_W01_F07_PREFLIGHT_COMPLETE_READY_FOR_HUMAN_F07_AUTHORIZATION_NO_LIVE_AUTHORITY`
