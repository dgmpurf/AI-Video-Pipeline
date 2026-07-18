# PHASE CAL-001-P3A - Activation-Precondition Runtime Audit, No Submit

## 1. Phase summary

- phase_id: CAL-001-P3A
- program_id: CAL-001
- macro_id: CAL-001A
- executed: true
- status: activation_preconditions_passed_except_live_cost_and_provider_canaries
- starting_head: `2085cbd78f8b98acb8b9220ecefd995296fa237c`
- H1_acceptance_record_verified: true
- fixed_manifest_human_reviewed: true
- fixed_manifest_human_accepted: true
- accepted_immutable_digests_match: true
- sources_clean: true
- worktree_preflight_pass: true
- dreamina_executable_path: `C:/Users/msjpurf/bin/dreamina.exe`
- dreamina_version_success: true
- dreamina_user_credit_success: true
- dreamina_runtime_canary_pass: true
- live_total_credit: 6447
- minimum_balance_required: 6440
- balance_precondition_pass: true
- runtime_help_audited: true
- runtime_contract_verified: true
- command_binding_audit_pass: true
- command_binding_tasks_checked: 84
- actual_per_task_cost_verified: false
- activation_conditions_passed: 14 (`A01-A14`)
- activation_conditions_pending: 2 (`A15-A16`)
- activation_conditions_failed: 0
- seven_family_canary_proposal_ready: true
- seven_family_canary_ids: `CAL001-F01-P2-R1`, `CAL001-F02-P2-R1`, `CAL001-F03-P2-R1`, `CAL001-F04-P2-R1`, `CAL001-F05-P2-R1`, `CAL001-F06-P2-R1`, `CAL001-F07-P2-R1`
- execution_authority_active: false
- Dreamina_generation_run: false
- submit_count: 0
- query_count: 0
- download_count: 0
- credits_consumed: 0
- CAL001_artifacts_modified: false
- blocking_finding_count: 0
- nonblocking_note_count: 6
- recommended_next_phase: `CAL-001-P3B_SEVEN_FAMILY_FIXED_TASK_LIVE_CANARY_AUTHORIZATION`
- final_verdict: `CAL001_P3A_RUNTIME_AND_PRE_SUBMIT_AUDIT_PASSED_PENDING_SEVEN_FAMILY_LIVE_CANARY_AUTHORIZATION`

P3A completed only the no-submit portion of the activation audit. It confirms the current CLI syntax, login/account canary, budget threshold, and all 84 local command bindings. It does not activate CAL-001A.

## 2. Starting checkpoint

- required branch: `main`
- starting HEAD: `2085cbd78f8b98acb8b9220ecefd995296fa237c`
- starting `origin/main`: `2085cbd78f8b98acb8b9220ecefd995296fa237c`
- HEAD and `origin/main` aligned: true
- tracked working-tree modifications: none
- staged files: none
- `sources/` modified or staged: false
- P3A report already existed: false

Known unrelated untracked workspace noise was present and excluded:

- `.vs/`
- `productions/chi_yan_tian_qiong/edits/`
- `productions/chi_yan_tian_qiong/review_artifacts/`
- `reports/context_recovery/`
- `reports/investor/`

## 3. H1 acceptance verification

- H1 acceptance record: `experiments/CAL-001/reviews/CAL001_H1_human_fixed_manifest_acceptance_record.json`
- expected SHA256: `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7`
- recomputed SHA256: `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7`
- acceptance-record hash match: true
- updated human checklist: `experiments/CAL-001/reviews/CAL001_human_manifest_review_checklist.md`
- expected checklist SHA256: `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3`
- recomputed checklist SHA256: `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3`
- checklist hash match: true
- H1 final verdict verified: `CAL001_H1_HUMAN_FIXED_MANIFEST_ACCEPTANCE_RECORDED_READY_P3_ACTIVATION_AUDIT`
- `fixed_manifest_human_reviewed=true`: verified
- `fixed_manifest_human_accepted=true`: verified
- `execution_authority_active=false`: verified
- authorization language: English
- authorization type: conditional pre-authorization

Neither H1 artifact was modified.

## 4. Accepted immutable digest verification

| Digest | Recomputed SHA256 | Match |
| --- | --- | --- |
| fixed_manifest_sha256 | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` | true |
| fixture_registry_sha256 | `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142` | true |
| prompt_inventory_sha256 | `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d` | true |
| package_inventory_sha256 | `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c` | true |
| full_experiment_inventory_sha256 | `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138` | true |

Independent scope and byte checks:

- manifest rows: 84
- families: 7
- prompt architectures: 4
- replicate values: 3
- stable unique experiment IDs: 84/84
- exact ordered ID set from `CAL001-F01-P1-R1` through `CAL001-F07-P4-R3`: true
- unique prompt files: 28
- unique package files: 84
- prompt byte-hash mismatches: 0
- package byte-hash mismatches: 0
- package parse failures: 0
- package-to-manifest mismatches: 0
- fixture registry entries: 11
- missing fixtures: 0
- fixture byte-hash mismatches: 0
- package authorization/final/lock failures: 0
- fixed-setting failures: 0
- fixture binding-shape failures: 0
- accepted immutable digests match: true

## 5. Activation-condition ledger

| ID | Description | Evidence | Status | Blocking | Remediation or next phase |
| --- | --- | --- | --- | --- | --- |
| A01 | Fixed manifest exists | `CAL001A_fixed_84_task_manifest.csv` opened and hashed | pass | true | None |
| A02 | Fixed manifest contains exactly 84 rows | CSV parse returned 84 data rows | pass | true | None |
| A03 | All experiment IDs are stable and unique | 84 unique IDs; exact canonical order matched | pass | true | None |
| A04 | Every row contains required task and fixture fields | 84 packages matched manifest; task-specific fixture-shape failures=0 | pass | true | None |
| A05 | Accepted prompt/package/manifest/fixture hashes match | Five aggregate digests match; prompt/package/fixture mismatches=0 | pass | true | None |
| A06 | Dataset and scoring schemas exist and validate | 3 schemas parse; results CSV=84 rows; visual JSONL=84 parseable rows | pass | true | None |
| A07 | P2 independent review passed | P2 status and final verdict remain committed | pass | true | None |
| A08 | H1 human review and acceptance are recorded | H1 record and checklist hashes match; both human flags true | pass | true | None |
| A09 | `sources/` is clean | Source-scoped git status empty before and after runtime checks | pass | true | None |
| A10 | Worktree has no unexpected tracked or staged changes | tracked diff and index empty; only known untracked noise | pass | true | None |
| A11 | Actual execution-environment Dreamina canary passes | version and user_credit exit 0; five required help commands exit 0; no logger/auth anomaly | pass | true | None |
| A12 | Current live balance supports budget plus floor | 6447 >= 5880 + 560 = 6440 | pass | true | Preserve fixed budget and stop gates |
| A13 | Current runtime command contracts support every accepted task | Current help supports all four task types and accepted settings | pass | true | None |
| A14 | Exact CLI input binding for every task family is valid | 84 in-memory argv renderings checked; failures=0 | pass | true | Future runner must use repo root as cwd |
| A15 | Actual per-task cost has been verified | No current help or documented no-cost estimator proves live charge | pending | true | P3B seven-family fixed-task canary authorization |
| A16 | No unresolved login, upload, provider, safety, or result-count anomaly exists | Login passes, but upload/provider/safety/result-count behavior is untested without submit | pending | true | P3B bounded canaries with immediate stop gates |

Summary: 14 pass, 2 pending, 0 fail. Pending conditions do not activate execution authority.

## 6. Source/worktree preflight

- Source governance: read-only
- `sources/` clean at starting preflight: true
- `sources/` clean after non-generative runtime checks: true
- accepted `experiments/CAL-001/**` modified: false
- unrelated tracked modifications: none
- staged files before report creation: none
- command-contract Source compared: `sources/dreamina_cli_help_latest.md`
- current runtime help remains the higher command-fact authority
- Source modified, staged, committed, or repaired: false

## 7. Dreamina environment and canary

- executable path: `C:/Users/msjpurf/bin/dreamina.exe`
- executable exists: true
- Linux CLI used: false
- version exit code: 0
- version success: true
- sanitized binary version: `2a20fff-dirty`
- commit: `2a20fff`
- build time: `2026-06-26T06:36:39Z`
- version matches active stored help snapshot: true
- user_credit exit code: 0
- user_credit success: true
- user_id: `1611200923726843`
- vip_level: `maestro`
- total_credit: 6447
- logger Access Denied: false
- login/auth failure: false
- sensitive key/value material returned in captured metadata: false

Authorized help checks:

| Command | Exit code | Result |
| --- | ---: | --- |
| `dreamina text2video -h` | 0 | pass |
| `dreamina image2video -h` | 0 | pass |
| `dreamina frames2video -h` | 0 | pass |
| `dreamina multimodal2video -h` | 0 | pass |
| `dreamina query_result -h` | 0 | pass |

- dreamina_runtime_canary_pass: true
- command_contract_changed: false

## 8. Live credit and budget audit

- user_reported_planning_balance: 6447
- live_total_credit: 6447
- balance_difference_from_planning_evidence: 0
- credit_budget_max: 5880
- credit_floor: 560
- minimum_balance_required: 6440
- balance headroom above minimum: 7
- balance_precondition_pass: true
- observed_daily_credit_effect: not inferable from one same-value snapshot
- credits consumed by P3A generation: 0

The extra 7 credits are not added to CAL-001A's fixed 5880-credit budget. No task count, model, resolution, or duration was changed.

## 9. Current runtime help summary

### text2video

- supported models include `seedance2.0_vip`
- duration range: 4-15 seconds
- ratios include `16:9`
- `seedance2.0_vip` resolutions: 720p, 1080p, 4k
- `--prompt`, `--duration`, `--ratio`, `--video_resolution`, `--model_version`, and `--poll` are supported

### image2video

- exactly one local input uses `--image`
- ratio is inferred from the input image and no `--ratio` flag exists
- `seedance2.0_vip`, duration 5, resolution 720p, and poll 0 are supported
- F02 portrait input therefore remains a valid inferred portrait output route

### frames2video

- first and last frames use `--first` and `--last`
- ratio is inferred from the first frame and no `--ratio` flag exists
- `seedance2.0_vip`, duration 5, resolution 720p, and poll 0 are supported

### multimodal2video

- repeated `--image`, `--video`, and `--audio` flags are supported
- at least one image or video is required
- limits: image<=9, video<=3, audio<=3
- `seedance2.0_vip`, 16:9, duration 5, resolution 720p, and poll 0 are supported
- accepted F06/F07 packages use three images and no video/audio input

### query_result

- `--submit_id` queries one asynchronous task
- `--download_dir` adds download behavior
- query without `--download_dir` is query-only

All generation help warns that some higher-safety-risk model use may require prior Web confirmation. No such runtime error occurred in P3A because no generation command was run.

## 10. Runtime command-contract audit

All 84 accepted packages use:

- model_version: `seedance2.0_vip`
- duration: 5
- video_resolution: `720p`
- poll: 0

Task-family checks:

- F01 text2video: prompt plus explicit 16:9 ratio; pass
- F02/F03/F04 image2video: one `--image`, inferred ratio, no `--ratio`; pass
- F05 frames2video: one `--first`, one `--last`, correct order, inferred ratio; pass
- F06/F07 multimodal2video: three repeated `--image` values in package order, explicit 16:9, below image limit; pass
- unsupported task types: 0
- unsupported models, durations, resolutions, or ratios: 0
- output directory/name used as submit flags: 0
- query/download/session/token arguments mixed into submit argv: 0
- signed URL or credential pattern found: 0

- runtime_contract_verified: true

This verifies current command syntax and accepted settings only. It is not submit authorization.

## 11. Exact local command-binding audit

The audit rendered argv arrays in memory from all 84 committed packages. No temporary repository or external script file was created. Prompt file bytes were hashed before extraction; the exact text between provider-prompt markers was loaded; its canonical payload hash was verified; fixture files and order were verified; then the future argv was assembled without executing it.

Coverage:

- text2video: 12
- image2video: 36
- frames2video: 12
- multimodal2video: 24
- total checked: 84
- failures: 0

Sanitized representative argv structures follow. Prompt bodies are replaced by verified hash/length placeholders.

`CAL001-F01-P2-R1`:

```text
["C:/Users/msjpurf/bin/dreamina.exe","text2video","--prompt","<provider_prompt sha256=47da84130c17af6eb3d79e5360ad2905acc81729e1e56d51771573e2ecc54ee9 chars=391>","--duration","5","--ratio","16:9","--video_resolution","720p","--model_version","seedance2.0_vip","--poll","0"]
```

`CAL001-F02-P2-R1`:

```text
["C:/Users/msjpurf/bin/dreamina.exe","image2video","--image","productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png","--prompt","<provider_prompt sha256=bb57321493c78b4e81bc4042fe409cfebe841725108f8cebdfd404274fa69a39 chars=313>","--duration","5","--video_resolution","720p","--model_version","seedance2.0_vip","--poll","0"]
```

`CAL001-F05-P2-R1`:

```text
["C:/Users/msjpurf/bin/dreamina.exe","frames2video","--first","productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png","--last","productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p30s.png","--prompt","<provider_prompt sha256=516c3547965e1cb4a327540f37d4607120a2fba570903c881660547a8b9ba1f9 chars=321>","--duration","5","--video_resolution","720p","--model_version","seedance2.0_vip","--poll","0"]
```

`CAL001-F06-P2-R1`:

```text
["C:/Users/msjpurf/bin/dreamina.exe","multimodal2video","--image","productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png","--image","productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png","--image","productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png","--prompt","<provider_prompt sha256=73edd1828c24d54d14409836ffa65d3ff8c07e63a2682c59de05e5f2d639feb0 chars=309>","--duration","5","--ratio","16:9","--video_resolution","720p","--model_version","seedance2.0_vip","--poll","0"]
```

- command_binding_audit_pass: true
- command_binding_tasks_checked: 84

## 12. Actual-cost verification result

Current runtime help exposes no cost-estimation or dry-run charge command. Repository search found only the committed budget statement that 70 credits is a planning assumption, not a live verified fact for every task type. `user_credit` proves only the current balance.

- undocumented command used: false
- cost inferred solely from historical K270M: false
- generation task submitted: false
- actual_per_task_cost_verified: false
- activation_condition_A15: pending

Actual charge requires separately authorized fixed-manifest canaries. Any observed charge above 70 must stop the canary macro without replacement, retry, downgrade, or expansion.

## 13. Seven-family fixed-task canary proposal

Exactly one accepted P2-R1 row from each family is proposed. All seven exist in the fixed 84-row manifest.

| Experiment | Task type | Package SHA256 | Prompt SHA256 | Expected result | Planned cost | Output path |
| --- | --- | --- | --- | --- | ---: | --- |
| `CAL001-F01-P2-R1` | text2video | `f8763f6cf62aa7893b6f0026544f5865eec5fcc6b2c288c809cdd7b5eab5e310` | `e18bd22187c34bf38cd6cd8c793b0093968f94b263c12ff683987ea0d26f5368` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F01-P2-R1/CAL001-F01-P2-R1_result.mp4` |
| `CAL001-F02-P2-R1` | image2video | `33d70a828db0ed1bcc849e2b8de2195f1f4817206fc14b1e23be6eb962d5f8d4` | `7260aad9976851a4f94a93774f4a910e98d9c204ffb64eafbc10a8774e98618c` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F02-P2-R1/CAL001-F02-P2-R1_result.mp4` |
| `CAL001-F03-P2-R1` | image2video | `c7518b0581f4ea784b4addc334deb01118d69759e819c87a64ad2a879dfe78d6` | `abe0c0048da5b32bd4d8dce7664c7383c72346049911ab9bf58d11dd63b2f004` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F03-P2-R1/CAL001-F03-P2-R1_result.mp4` |
| `CAL001-F04-P2-R1` | image2video | `f8d588cf4778679080bf4a795ebee91d216f56acd8ee8a786ae4d106881d7be0` | `d237e50e930a2786641646b35ed4357b6b12945e2f6d2cc987360eb662c69a3d` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F04-P2-R1/CAL001-F04-P2-R1_result.mp4` |
| `CAL001-F05-P2-R1` | frames2video | `632c69ee4bd6be1baccf944ea729b6bbbdddabaae0fadc40bc091e9d47bd7709` | `3b22eed98f8165c441b58c45b4285dbf40a37d4979f3d1f27c87b43e43698056` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F05-P2-R1/CAL001-F05-P2-R1_result.mp4` |
| `CAL001-F06-P2-R1` | multimodal2video | `d6e89fbb02fc86096e43f8caecb934c3f7e0eb7912cc676d07c116f8bcd8d9dd` | `4d0d3d5ff85da699f60434cf0eb431c76b0c45836bb87700eebfb4406c58b20b` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F06-P2-R1/CAL001-F06-P2-R1_result.mp4` |
| `CAL001-F07-P2-R1` | multimodal2video | `6894a333900b6ac5fbef0272d8f59e7952a5556e1e878f5e1b5b707a833359e9` | `1564bdba4707cf2bbe6eb6608b8f3bb7831e65ef9747ae0bd87df65dd72591ba` | 0 images, 1 video | 70 | `experiments/CAL-001/runs/CAL001-F07-P2-R1/CAL001-F07-P2-R1_result.mp4` |

Package paths:

- `CAL001-F01-P2-R1`: `experiments/CAL-001/packages/F01/CAL001-F01-P2-R1_package.json`
- `CAL001-F02-P2-R1`: `experiments/CAL-001/packages/F02/CAL001-F02-P2-R1_package.json`
- `CAL001-F03-P2-R1`: `experiments/CAL-001/packages/F03/CAL001-F03-P2-R1_package.json`
- `CAL001-F04-P2-R1`: `experiments/CAL-001/packages/F04/CAL001-F04-P2-R1_package.json`
- `CAL001-F05-P2-R1`: `experiments/CAL-001/packages/F05/CAL001-F05-P2-R1_package.json`
- `CAL001-F06-P2-R1`: `experiments/CAL-001/packages/F06/CAL001-F06-P2-R1_package.json`
- `CAL001-F07-P2-R1`: `experiments/CAL-001/packages/F07/CAL001-F07-P2-R1_package.json`

Fixture sets:

- `CAL001-F01-P2-R1`: none
- `CAL001-F02-P2-R1`: `CAL001-F02-IDENTITY-01` -> `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- `CAL001-F03-P2-R1`: `CAL001-F03-SCENE-01` -> `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png`
- `CAL001-F04-P2-R1`: `CAL001-F04-ENVIRONMENT-01` -> `productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png`
- `CAL001-F05-P2-R1`: `CAL001-F05-FIRST-01` -> `productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png`; `CAL001-F05-LAST-01` -> `productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p30s.png`
- `CAL001-F06-P2-R1`: `CAL001-F06-IDENTITY-A`, `CAL001-F06-IDENTITY-B`, `CAL001-F06-SCENE-01` -> the three ordered paths recorded in the F06 package
- `CAL001-F07-P2-R1`: `CAL001-F07-IDENTITY-A`, `CAL001-F07-IDENTITY-B`, `CAL001-F07-SCENE-01` -> the three ordered paths recorded in the F07 package

Any future P3B authorization must state:

- these are fixed-manifest tasks and not additional tasks;
- the seven submits count against `submit_count_max=84`;
- their charges count against `credit_budget_max=5880`;
- no task may be replaced, retried, or resubmitted;
- query is bounded to at most 3 per created submit ID;
- download is success-only and at most once per matching task;
- the macro stops if any observed charge exceeds 70;
- the macro stops on any input-binding, upload, provider, safety, or result-count anomaly.

P3A records this proposal only. It does not create P3B authorization.

## 14. Remaining pending conditions

### A15 - actual per-task cost

Pending because no official no-cost runtime mechanism proves charge across the four task types. The 70-credit value remains a planning assumption.

### A16 - live provider behavior

Pending because P3A did not submit, upload through a generation command, query a task, download media, or observe result counts. Login and command syntax pass, but provider-side execution remains untested.

- execution_authority_active: false
- activation complete: false

## 15. Blocking findings

None at the no-submit preflight layer.

- blocking_finding_count: 0
- activation-precondition failures: 0
- unresolved conditions: A15 and A16 pending, not passed

## 16. Nonblocking notes

1. The live balance passes by only 7 credits; fixed stop conditions and the 560-credit floor remain essential.
2. No supported no-cost cost estimator exists in the audited help, so the 70-credit assumption remains unverified.
3. Upload, provider-generation, safety-confirmation, and result-count behavior remain pending until bounded live canaries.
4. Current help warns that some higher-safety-risk use may require prior Web confirmation; any such response must stop the future canary.
5. Fixture and prompt paths are repository-relative; a future runner must execute from `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE` or resolve them to equivalent absolute paths without changing package order or bytes.
6. The human-accepted F02 portrait-ratio and F05 subtle-transition notes remain design notes and are not silently corrected in P3A.

- nonblocking_note_count: 6

## 17. Explicit non-actions

- Dreamina generation commands run: none
- only Dreamina `version`, `user_credit`, and the five authorized help commands run: true
- submit: none
- experiment query: none
- download: none
- retry or resubmit: none
- batch: none
- generation credits consumed: 0
- CAL-001A activated: false
- execution_authority_active changed: false
- accepted CAL-001 artifact modified: false
- Source modified: false
- fixture, prompt, package, manifest, schema, dataset, matrix, budget, checklist, or H1 record modified: false
- media, frame, contact sheet, or cut created: false
- experiment result row updated: false
- CAL-001B created or authorized: false
- P3B authorization created: false
- final_master set true: false
- locked set true: false
- tag created: false

## 18. Recommended next phase

`CAL-001-P3B_SEVEN_FAMILY_FIXED_TASK_LIVE_CANARY_AUTHORIZATION`

The human must separately authorize the exact seven fixed tasks and bounded submit/query/success-only-download behavior described in Section 13. P3A itself grants no live generation authority.

## 19. Final verdict

`CAL001_P3A_RUNTIME_AND_PRE_SUBMIT_AUDIT_PASSED_PENDING_SEVEN_FAMILY_LIVE_CANARY_AUTHORIZATION`
