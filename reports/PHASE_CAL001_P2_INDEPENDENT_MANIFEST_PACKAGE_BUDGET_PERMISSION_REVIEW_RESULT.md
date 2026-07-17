# PHASE CAL-001-P2 - Independent Manifest, Package, Budget, and Permission Review Result

## 1. Phase summary

- phase_id: CAL-001-P2
- executed: true
- status: independent_review_passed_with_nonblocking_notes
- starting_head: aeea1614fa1e5fe9d2a6669d8e3d0b3832ee8176
- raw_audit_completed_before_report_comparison: true
- matrix_integrity_pass: true
- prompt_semantic_equivalence_pass: true
- family_target_review_pass: true
- fixture_audit_pass: true
- package_audit_pass: true
- manifest_audit_pass: true
- stored_help_compatible: true
- runtime_contract_verified: false
- schema_dataset_audit_pass: true
- all_reported_hashes_independently_match: true
- budget_audit_pass: true
- permission_audit_pass: true
- human_acceptance_ready: true
- fixed_manifest_human_reviewed: false
- fixed_manifest_human_accepted: false
- execution_authority_active: false
- Dreamina_run: false
- submit_count: 0
- query_count: 0
- download_count: 0
- sources_clean: true
- blocking_finding_count: 0
- nonblocking_note_count: 4
- recommended_next_phase: CAL-001-H1_HUMAN_FIXED_MANIFEST_REVIEW_AND_ACCEPTANCE
- final_verdict: CAL001_P2_INDEPENDENT_REVIEW_PASSED_WITH_NONBLOCKING_NOTES_READY_HUMAN_FIXED_MANIFEST_ACCEPTANCE

This review passes the committed CAL-001 fixed definition for human acceptance. It does not activate CAL-001A and does not verify current live runtime, login, credits, or provider cost.

## 2. Starting repository checkpoint

- branch: main
- HEAD at preflight: `aeea1614fa1e5fe9d2a6669d8e3d0b3832ee8176`
- origin/main at preflight: `aeea1614fa1e5fe9d2a6669d8e3d0b3832ee8176`
- HEAD and origin/main aligned: true
- tracked working-tree changes: none
- staged changes: none
- `sources/` modified or staged: false

Known untracked workspace noise was observed and excluded:

- `.vs/`
- `productions/chi_yan_tian_qiong/edits/`
- `productions/chi_yan_tian_qiong/review_artifacts/`
- `reports/context_recovery/`
- `reports/investor/`

## 3. Independence protocol

The audit used two ordered passes.

Pass A was completed before reading the P1-R2 result report. It directly inspected the committed CAL-001 tree, all 28 provider prompts, all 84 package JSON files, the 84-row manifest, all 11 fixture registry entries and 6 physical fixture files, the schemas, both dataset templates, the budget, the checklists, stored CLI help, Source governance, and the CAL-001A authorization report. The two F05 frames were also viewed directly at original resolution. Raw findings were frozen before comparison.

Pass B then read:

`reports/PHASE_CAL001_P1_R2_PROJECT_WIDE_PROMPT_CALIBRATION_NO_RUN_MANIFEST_AND_SCHEMA_CREATION_RESULT.md`

P1-R2 claims were treated as claims, not as inputs to the Pass A decision. Aggregate inventory construction was regenerated from the documented canonical line formats after the constituent file hashes had already been independently verified.

## 4. Active Source and authorization state

The required Project Source files were read as read-only governance and technical context. Current Source hashes independently match the P1-R2 checkpoint for the two explicitly hash-bound routing files:

- `sources/AI视频制作_Source索引与使用优先级_V1.11.md`: `47201316a3a433b3c8f31c7f52c53b219bc3be95bb775b3da84154d329da2769`
- `sources/AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md`: `b93d40902e2156dc6269d8df6b3d051c150ad77e0fd3b8c0e968693d49def062`

The known Source-header status wording debt remains contextual metadata only. P2 did not modify Source.

CAL-001A authorization remains:

- authorization_type: conditional_pre_authorization
- fixed task scope after future activation: exactly 84
- submit_count_max after future activation: 84
- query_count_max_per_created_submit_id after future activation: 3
- retry_count_max: 0
- resubmit_count_max: 0
- batch_expansion: false
- credit_budget_max: 5880
- credit_floor: 560
- execution_authority_active: false
- final_master: false
- locked: false

## 5. Raw matrix audit

| Check | Independent result |
| --- | --- |
| Fixed design | 7 families x 4 architectures x 3 replicates |
| Manifest rows | 84 |
| Experiment IDs | 84 unique, exact ordered range `CAL001-F01-P1-R1` through `CAL001-F07-P4-R3` |
| Prompt files | 28 unique UTF-8 LF files |
| Package files | 84 unique parseable JSON files |
| Replicates per family/architecture cell | exactly 3 |
| Replicate prompt bytes | identical inside every cell |
| Replicate fixtures/order/settings/cost | identical inside every cell |
| Replicate experiment/package/output identities | distinct inside every cell |
| Adaptive, CAL-001B, retry, or replacement rows | 0 |
| Duplicate output directory/name pairs | 0 |
| Media under `experiments/CAL-001/` | 0 |
| Future `runs/` directory already created | false |

Matrix integrity passes without a missing or extra cell.

## 6. Prompt semantic-equivalence audit

All 28 provider prompts were read. The comparison used the provider payload between the explicit markers, not the surrounding CAL-001 metadata.

| Family | semantic_equivalence_pass | architecture_difference_isolated | baseline_is_fair | P2_is_truly_concise | P3_duties_do_not_change_target | P4_timing_does_not_change_action_complexity | negative_constraint_load_comparable | reference_order_constant | unintended_difficulty_difference_present |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F01 | true | true | true | true | true | true | true | true | false |
| F02 | true | true | true | true | true | true | true | true | false |
| F03 | true | true | true | true | true | true | true | true | false |
| F04 | true | true | true | true | true | true | true | true | false |
| F05 | true | true | true | true | true | true | true | true | false |
| F06 | true | true | true | true | true | true | true | true | false |
| F07 | true | true | true | true | true | true | true | true | false |

Supporting findings:

- P1 is a legitimate conventional descriptive baseline in every family and is not a deliberately weak strawman.
- P2 is the shortest prompt in every family: 41-61 words versus P1 at 62-90 words.
- P3 adds duties and forbidden duties without changing the creative target, action, camera, environment, or end state.
- P4 adds timing to the existing action rather than adding choreography. F06's word `synchronized` makes explicit the already shared `both ... while` step and does not add a separate action.
- Negative lists vary in compression but preserve the material safety and target-isolation constraints.
- No architecture adds an easier subject count, removes the defining action, strengthens impact/displacement, adds transformation, or changes to a different camera task.

## 7. Family-target review

| Family | Required target | Independent finding | Result |
| --- | --- | --- | --- |
| F01 | one subject, one shutter-closing action, one shot | One adult courier closes one shutter; no second action or cut | pass |
| F02 | one image identity and one simple motion | One black-red male identity takes one grounded step; ratio is inferred from a 1440x2560 input | pass with note |
| F03 | one camera move and stable empty scene | One frontal-axis push-in; no pan, orbit, cut, subject, or geometry change | pass |
| F04 | causal environment response without destruction | One planted weight shift causes one small splash; no strike, wall event, or structural damage | pass |
| F05 | controlled same-sequence state transition | 1.15s and 1.30s frames preserve identities, scene, frontal framing, and ordering; energy settles directionally | pass with note |
| F06 | two identities and spatial blocking without combat | Fenshou remains left/foreground and Shuangji right/midground during one measured step; no contact | pass |
| F07 | safe force/reaction causality | One controlled guard pressure causes one grounded half-step and wet-floor feedback; no injury, airborne motion, wall contact, or external action reference | pass |

Direct F05 image inspection found the same two figures, same rainy courtyard, same frontal camera, and nearly identical spatial layout. The 1.15s frame has slightly stronger mist/aftershock energy; the 1.30s frame is slightly more settled. The pair is compatible and directional, although deliberately low-amplitude.

## 8. Fixture audit

Every registry path was opened as bytes, each PNG signature and dimensions were checked, file size and SHA256 were recomputed, and provenance evidence paths were confirmed to exist.

| Fixture ID | Dimensions | Bytes | Recomputed SHA256 | Eligibility and rights | Result |
| --- | ---: | ---: | --- | --- | --- |
| CAL001-F02-IDENTITY-01 | 1440x2560 | 1959523 | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | active=true; project-generated locked production asset | pass with ratio note |
| CAL001-F03-SCENE-01 | 2560x1440 | 4147285 | `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452` | active=true; project-generated locked scene | pass |
| CAL001-F04-ENVIRONMENT-01 | 2560x1440 | 4160657 | `6a573b598ab813e8ac7997a387303326a9f4836c52cc1ae91ca33ed207db60c7` | active=true; project-generated locked keyframe | pass |
| CAL001-F05-FIRST-01 | 1280x720 | 752739 | `82deaa75293ae75be3bd2b4d1b2da82ce3e4f263a5380ed2ed01a4ec5b3030df` | active=true; project-generated human-reviewed frame | pass with low-amplitude note |
| CAL001-F05-LAST-01 | 1280x720 | 828011 | `56244830c24cb08c3d0e694af9e146a75ca342da680ccfd5c26a59b9168a5c09` | active=true; project-generated reviewed usable frame | pass with low-amplitude note |
| CAL001-F06-IDENTITY-A | 1440x2560 | 1959523 | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | active=true; identity only | pass |
| CAL001-F06-IDENTITY-B | 1440x2560 | 3874061 | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | active=true; human-approved identity anchor | pass |
| CAL001-F06-SCENE-01 | 2560x1440 | 4147285 | `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452` | active=true; scene layout only | pass |
| CAL001-F07-IDENTITY-A | 1440x2560 | 1959523 | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | active=true; acting identity only | pass |
| CAL001-F07-IDENTITY-B | 1440x2560 | 3874061 | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | active=true; receiving identity only | pass |
| CAL001-F07-SCENE-01 | 2560x1440 | 4147285 | `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452` | active=true; environment/layout only | pass |

Additional fixture findings:

- Registry entries: 11.
- Unique physical files: 6.
- F06 and F07 intentionally reuse the same three physical files in the same order; family duties differ and remain explicit.
- No external, K271A, or K270Q media is an active fixture.
- No fixture was copied, modified, resized, re-encoded, or moved into the CAL-001 tree.
- `active_generation_input_allowed=true` records internal fixture eligibility only and grants no execution authority.

## 9. Package audit

All 84 package JSON files parse and match their corresponding manifest row in both directions for identity, family, architecture, replicate, task type, model, duration, ratio/rule, resolution, poll, prompt path/hash, fixture IDs/paths/hashes, expected result counts, cost, output identity, scoring dimensions, status, and authority flags.

- provider payload hashes independently verified: 84/84
- package file hashes independently verified: 84/84
- reference-duty count and order match fixture count and order: 84/84
- fixture duty and forbidden-duty text present: 84/84
- `no_submit=true`: 84/84
- submit/query/download/retry/resubmit/batch authority false: 84/84
- package and review-plan final/lock false: 84/84
- current review action: `plan_only_no_artifact_creation` for 84/84
- signed URL, token, bearer credential, or secret pattern found: 0

Task-input mapping is unambiguous but implicit: `image2video` has one ordered image, `frames2video` has FIRST then LAST, and `multimodal2video` has repeated ordered images. A future runner must convert those ordered fixtures to current CLI argument names during P3/runtime validation.

## 10. Manifest audit

- path: `experiments/CAL-001/manifests/CAL001A_fixed_84_task_manifest.csv`
- artifact-tool import range: `A1:AN85`
- columns: 40
- data rows: 84
- unique experiment IDs: 84
- unique prompt paths: 28
- unique package paths: 84
- expected images per row: 0
- expected videos per row: 1
- expected total output per row: 1
- status per row: `planned_no_run`
- planned cost per row: 70
- ratio rules: explicit for F01/F06/F07; input-inferred for F02-F05
- authority leakage: none
- signed URL or secret pattern: none

The manifest is complete, deterministic, and non-adaptive.

## 11. Stored-help compatibility audit

No Dreamina command was run. Compatibility is based only on the committed 2026-07-01 help snapshot and Source contracts.

| Families | Task type | Planned settings | Stored-help result |
| --- | --- | --- | --- |
| F01 | text2video | `seedance2.0_vip`, 5s, 720p, 16:9, poll=0 | compatible |
| F02-F04 | image2video | one image, `seedance2.0_vip`, 5s, 720p, inferred ratio, poll=0 | compatible |
| F05 | frames2video | first+last images, `seedance2.0_vip`, 5s, 720p, inferred ratio, poll=0 | compatible |
| F06-F07 | multimodal2video | three repeated images, `seedance2.0_vip`, 5s, 720p, 16:9, poll=0 | compatible |

Stored help supports all task types, the model, 4-15 second duration, 720p, explicit 16:9 where used, inferred ratio where required, repeated multimodal image inputs, and poll=0. Current runtime help, login, account credits, and unit cost were not queried.

- stored_help_compatible: true
- runtime_contract_verified: false

## 12. Schema and dataset audit

All three schema files parse as JSON and are internally coherent with the two templates.

- experiment record required fields: 35
- experiment record properties: 35
- experiment-results CSV columns: 35
- scoring dimensions: 14
- applicable and mandatory-null dimensions cover every score exactly once per family
- score type/range: integer 0-5 or null
- failure labels: 27, with matching primary enum, secondary enum, and definitions
- candidate-status values: 8
- results CSV rows: 84, all pristine and unreviewed
- visual JSONL rows: 84, all parseable, all scores null, no outcomes assigned
- CSV/template experiment IDs and ordering match the fixed manifest

This audit used JSON parsing plus exhaustive required/property/header, enum/definition, applicability, and template-state cross-checks. It did not assign scores or outcomes.

## 13. Hash and deterministic inventory audit

All 28 prompt file hashes, 84 package file hashes, 11 registry fixture hashes, and the required static artifact hashes were independently recomputed from current bytes. Every reported value matches.

Canonical aggregate construction used UTF-8, LF, lexicographic experiment ordering, and one final LF:

- prompt lines: `family_id|prompt_architecture|prompt_path|prompt_sha256`
- package lines: `experiment_id|package_path|package_sha256`
- full lines: `experiment_id|prompt_sha256|package_sha256|fixture_sha256s`

Independently recomputed acceptance digest:

| Digest | SHA256 | Match |
| --- | --- | --- |
| fixed_manifest_sha256 | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` | true |
| fixture_registry_sha256 | `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142` | true |
| prompt_inventory_sha256 | `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d` | true |
| package_inventory_sha256 | `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c` | true |
| full_experiment_inventory_sha256 | `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138` | true |

Required static artifact hashes also match P1-R2:

| Artifact | SHA256 |
| --- | --- |
| `.gitattributes` | `a79691a93b46e49ce460c26ef22afcc03d6eca1e63bf2edbc20e96159510f6c9` |
| `README.md` | `c91803bb5a27149e8bf7e340c2ec08d50bb1ebfe41f464938e34cb8cfa106e3a` |
| `CAL001_experiment_record.schema.json` | `b3b1797cccf5e974c161f770fdf14386ae8185512cbad0e2ae2738d017210cbb` |
| `CAL001_scoring.schema.json` | `0ed3f3f1886b132cd44c125f3dc5a7f0dd0c198caa2fb217c4a5ee1a0600796e` |
| `CAL001_failure_labels.schema.json` | `aaa6baf1a91bae1953617c6b8070c646356859c3bd06dcaa64c8e03b5072359c` |
| `CAL001_experiment_results_template.csv` | `95cdc5bea1445ea21346c61c666165a8b7cef15de7b75a8fcb6d48d132338eed` |
| `CAL001_visual_review_template.jsonl` | `d36b08bc1dd5ef6792676eac99cc3b2be07ff2edc32b7ef7cd81940a33d02869` |
| `CAL001_human_manifest_review_checklist.md` | `cf7887b5fd610108dffef24eeaccf003cd908334643dddd0166ed13d25332e13` |
| `CAL001_P2_independent_review_checklist.md` | `d8084f1236631cd60a9abe8e0604624d6450c7d53e7507cc0737e1478e338e8b` |
| `CAL001_budget_plan.md` | `41592ef135d11f49ac8bb158a7b60c2eab3e6bc79318c35217e42199b81def12` |
| `CAL001_fixed_experiment_matrix.md` | `d047b9fc6a1b9e2a97598ad9d13383b9f8f2f173712b15941e866025593e3209` |

The experiment tree contains 125 files. All are free of CR bytes and every text artifact ends with one LF. `.gitattributes` is exactly `* text eol=lf` plus one LF.

## 14. Budget audit

| Field | Value |
| --- | ---: |
| fixed task count | 84 |
| planned unit cost assumption | 70 |
| planned total | 5880 |
| credit floor | 560 |
| budget plus floor | 6440 |
| user-reported planning balance | 6447 |
| planning residual | 7 |

Arithmetic independently passes:

- `84 x 70 = 5880`
- `5880 + 560 = 6440`
- `6447 - 6440 = 7`

The 70-credit value remains a planning assumption. Any higher live cost must block activation or execution; no model, duration, resolution, or row may be silently downgraded or removed to fit the budget.

## 15. Permission and stop-condition audit

Every row and package remains no-run with all live authority false. CAL-001A remains inactive pending human acceptance and P3.

The conditional authorization report contains every required stop condition:

1. `sources/` modified or staged.
2. Prompt, package, or manifest hash mismatch.
3. Dreamina command-contract change.
4. Actual per-task cost above the approved assumption.
5. Three consecutive submits fail to create a task.
6. Returned result count differs from the manifest.
7. Remaining credits fall below 560.
8. Any unclassified login, upload, provider, or safety-boundary anomaly.
9. Completion of all 84 fixed experiments.

No retry, resubmit, batch expansion, automatic prompt rewrite, adaptive replacement, silent downgrade, CAL-001B use, final, or lock route is authorized.

## 16. Human acceptance readiness

- human_acceptance_ready: true
- fixed_manifest_human_reviewed: false
- fixed_manifest_human_accepted: false
- execution_authority_active: false

The human checklist supports one explicit decision over counts, matrix completeness, fixture eligibility, target value, excluded routes, budget, result counts, no-submit flags, stop conditions, Source governance, CAL-001B exclusion, final, and lock.

The exact digest to bind in the human decision is:

```text
fixed_manifest_sha256=b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d
fixture_registry_sha256=cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142
prompt_inventory_sha256=27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d
package_inventory_sha256=b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c
full_experiment_inventory_sha256=448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138
```

Human acceptance must remain a separate explicit act. This report does not fill or modify the committed checklist.

## 17. P1-R2 report comparison

| P1-R2 claim group | P2 classification | Comparison result |
| --- | --- | --- |
| Starting commit, branch, and Source hashes | independently_confirmed | Current start and bound Source hashes match |
| 7x4x3 matrix, 84 IDs, 28 prompts, 84 packages | independently_confirmed | Exact counts and ordered IDs reproduced |
| 11 registry entries and 6 physical fixtures | independently_confirmed | Bytes, PNG metadata, rights evidence, and hashes reproduced |
| Prompt architecture design and fairness | independently_confirmed_with_new_semantic_audit | All 28 prompts read; no strawman or target substitution found |
| Package parse, fixed fields, and authority flags | independently_confirmed | 84/84 match manifest and no authority leakage exists |
| Manifest 40 columns and 84 rows | independently_confirmed | artifact-tool imported `A1:AN85` |
| Schema and template claims | independently_confirmed | Counts, mappings, null states, and enums agree |
| Five inventory digests and 13 static hashes | independently_confirmed | Every reported value reproduced independently |
| Budget arithmetic and planning-only cost | independently_confirmed | 5880 total, 560 floor, 7 residual |
| No Dreamina, media, Source, final, or lock action | independently_confirmed | No repository evidence or current mutation contradicts the claim |
| Current runtime command, login, credit, and cost facts | not_claimed_as_verified_by_P1_R2 | P2 also leaves runtime_contract_verified=false |

No P1-R2 claim was contradicted. F02 and F05 risk notes were independently observed and remain nonblocking.

## 18. Blocking findings

None.

- blocking_finding_count: 0
- correction phase required before human acceptance: false
- CAL-001-P1-R3 authorization needed: false

## 19. Nonblocking notes

1. F02 uses a 1440x2560 identity fixture, so `image2video` infers a 9:16 output. This is technically correct and fair within F02, but the human should accept the portrait family intentionally.
2. F05 uses same-sequence frames only 0.15 seconds apart. Direct inspection confirms a compatible aftershock-to-recovery direction, but the low-amplitude state difference may reduce the family's power to distinguish architectures.
3. Package input binding is represented by `task_type`, fixture IDs, paths, roles, and order rather than explicit executable CLI argument keys. The mapping is unambiguous at no-run level and must be revalidated against current runtime help in P3.
4. The committed human checklist intentionally leaves acceptance and hash fields blank and contains dedicated slots for the manifest, package inventory, and full inventory. The five-hash digest in Section 16 supplies the complete binding for the human decision without modifying the checklist.

These notes do not require artifact mutation before human acceptance.

## 20. Explicit non-actions

- Dreamina commands run: none, including version, credit, or help
- submit/query/download/retry/resubmit/batch: none
- credits consumed: 0
- media generated, scanned, extracted, resized, copied, or modified: none
- review frames, contact sheets, cuts, or visual output scores created: none
- `experiments/CAL-001/**` modified: false
- `sources/**` modified, staged, committed, or pushed: false
- existing prompt/package/manifest/schema/dataset/checklist/report modified: false
- human review or acceptance recorded: false
- CAL-001A activated: false
- CAL-001B created: false
- final_master set true: false
- locked set true: false
- tag created: false

## 21. Recommended next phase

`CAL-001-H1_HUMAN_FIXED_MANIFEST_REVIEW_AND_ACCEPTANCE`

The human should review the fixed matrix, the four nonblocking notes, and the five-hash digest, then explicitly accept or reject the exact committed definition. A pass here does not itself grant live authority. After human acceptance, CAL-001-P3 must still verify every activation precondition, including current runtime help, login/account state, live credits, and unit cost.

## 22. Final verdict

`CAL001_P2_INDEPENDENT_REVIEW_PASSED_WITH_NONBLOCKING_NOTES_READY_HUMAN_FIXED_MANIFEST_ACCEPTANCE`
