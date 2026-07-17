# PHASE CAL-001-P1-R2 - Project-Wide Prompt Calibration No-Run Manifest and Schema Creation Result

## 1. Phase summary

- phase_id: CAL-001-P1-R2
- status: fixed_84_task_no_run_manifest_and_schema_created
- fixed_manifest_exists: true
- fixed_manifest_task_count: 84
- family_count: 7
- prompt_architecture_count: 4
- replicate_count: 3
- unique_prompt_count: 28
- package_count: 84
- fixed_manifest_human_reviewed: false
- fixed_manifest_human_accepted: false
- execution_authority_active: false
- final_master: false
- locked: false

## 2. Starting repository checkpoint

- branch: main
- starting_head: b2c43becc9be1c9d676d942b7c4515e8e142651f
- origin_main_at_preflight: b2c43becc9be1c9d676d942b7c4515e8e142651f
- head_origin_aligned_at_preflight: true
- no unrelated tracked or staged changes: true
- known untracked workspace noise was observed and excluded from staging.

## 3. Active Source and routing confirmation

- sources/AI视频制作_Source索引与使用优先级_V1.11.md: 47201316a3a433b3c8f31c7f52c53b219bc3be95bb775b3da84154d329da2769 (match=true)
- sources/AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md: b93d40902e2156dc6269d8df6b3d051c150ad77e0fd3b8c0e968693d49def062 (match=true)
- Active-state acceptance and stale-header metadata debt were carried forward exactly as instructed.
- Routing: Codex Local, high-effort fixed artifact generation; P0 and P0.25 governance preserved.

## 4. Source clean preflight

- sources_clean_preflight: true
- sources_staged_preflight: false
- sources_modified_by_phase: false
- Previous blocked report was read but not modified.

## 5. CAL-001A conditional authorization carry-forward

- authorization_language: English
- authorization_type: conditional_pre_authorization
- execution_authority_active: false
- submit_count_max_after_future_activation: 84
- query_count_max_per_created_submit_id_after_future_activation: 3
- retry_count_max: 0
- resubmit_count_max: 0
- batch_expansion: false
- credit_budget_max: 5880
- credit_floor: 560
- P1-R2 activates no live permission.

## 6. Fixed 7x4x3 design

The complete matrix contains 7 benchmark families, 4 semantically comparable prompt architectures, and 3 independent replicates per architecture. All 84 IDs from CAL001-F01-P1-R1 through CAL001-F07-P4-R3 are fixed before execution. No adaptive task, winner-dependent row, retry, replacement, or CAL-001B row exists.

## 7. Fixture selection and validation

- fixture_registry_entry_count: 11
- unique_physical_file_count: 6
- fixture_gap_present: false
- F01 is prompt-only and correctly has no media fixture.
- active_generation_input_allowed=true means internal eligibility only; it does not activate execution.

| Fixture ID | Family | Path | Dimensions | Bytes | SHA256 | Rights | Active input eligible | Validation |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| CAL001-F02-IDENTITY-01 | F02 | productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png | 1440x2560 | 1959523 | 83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f | project_generated_human_approved_locked_production_asset | true | pass |
| CAL001-F03-SCENE-01 | F03 | productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png | 2560x1440 | 4147285 | 831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452 | project_generated_human_approved_locked_scene_asset | true | pass |
| CAL001-F04-ENVIRONMENT-01 | F04 | productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png | 2560x1440 | 4160657 | 6a573b598ab813e8ac7997a387303326a9f4836c52cc1ae91ca33ed207db60c7 | project_generated_human_approved_locked_official_keyframe | true | pass |
| CAL001-F05-FIRST-01 | F05 | productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p15s.png | 1280x720 | 752739 | 82deaa75293ae75be3bd2b4d1b2da82ce3e4f263a5380ed2ed01a4ec5b3030df | project_generated_local_derived_frame_human_reviewed | true | pass |
| CAL001-F05-LAST-01 | F05 | productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V008_start_frame_candidates/SHOT-02-V008_start_candidate_1p30s.png | 1280x720 | 828011 | 56244830c24cb08c3d0e694af9e146a75ca342da680ccfd5c26a59b9168a5c09 | project_generated_local_derived_frame_human_reviewed_usable | true | pass |
| CAL001-F06-IDENTITY-A | F06 | productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png | 1440x2560 | 1959523 | 83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f | project_generated_human_approved_locked_production_asset | true | pass |
| CAL001-F06-IDENTITY-B | F06 | productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png | 1440x2560 | 3874061 | 15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11 | project_generated_human_approved_locked_identity_anchor | true | pass |
| CAL001-F06-SCENE-01 | F06 | productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png | 2560x1440 | 4147285 | 831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452 | project_generated_human_approved_locked_scene_asset | true | pass |
| CAL001-F07-IDENTITY-A | F07 | productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png | 1440x2560 | 1959523 | 83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f | project_generated_human_approved_locked_production_asset | true | pass |
| CAL001-F07-IDENTITY-B | F07 | productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png | 1440x2560 | 3874061 | 15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11 | project_generated_human_approved_locked_identity_anchor | true | pass |
| CAL001-F07-SCENE-01 | F07 | productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png | 2560x1440 | 4147285 | 831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452 | project_generated_human_approved_locked_scene_asset | true | pass |

F05 uses two existing 1280x720 frames from the same project-generated sequence: the human-ranked preferred 1.15s aftershock state and the human-reviewed usable, more-settled 1.30s state. No frame was extracted, cropped, resized, re-encoded, or copied in this phase.

## 8. Prompt architecture design

- P1_LEGACY_DESCRIPTIVE: legitimate conventional baseline, longer but not defective.
- P2_RESULT_FIRST_CONCISE: dominant visible result first, concise support and negatives.
- P3_RESULT_FIRST_WITH_DUTIES: same result plus explicit reference or subject/environment duties and forbidden duties.
- P4_RESULT_FIRST_TIMED_COMPACT: same result plus compact progression and end-state motion.
- Creative target, fixtures, task type, model, duration, resolution, ratio rule, and expected count remain fixed within each family.

## 9. Prompt inventory

- prompt_file_count: 28
- encoding_and_line_endings: UTF-8 with LF
- deterministic checkout policy: `experiments/CAL-001/.gitattributes` enforces `text eol=lf` inside the hash-locked experiment tree without changing root Git configuration.
- replicates reference one shared family/architecture prompt file.
- Each file embeds a provider-prompt payload SHA256 and metadata; the full prompt-file SHA256 is recorded in every package and manifest row to avoid self-hash circularity.
- prompt_inventory_sha256: 27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d

## 10. Package inventory

- package_count: 84
- package_json_parse_status: pass
- replicate fixed-field equality: pass
- distinct experiment/package/output identity: pass
- all no-submit, live-authority, final, and lock flags: pass
- package_inventory_sha256: b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c

## 11. Fixed manifest

- path: experiments/CAL-001/manifests/CAL001A_fixed_84_task_manifest.csv
- row_count_excluding_header: 84
- required_column_count: 40
- parse_status: pass via bundled artifact-tool CSV import
- unique_experiment_ids: 84
- duplicate_output_pairs: 0
- fixed_manifest_sha256: b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d

## 12. Dataset record schema

The technical record schema includes submit, query, generation, result-count, download, local-media, cost, stop-condition, all visual score, classification, reviewer, and candidate-status fields. Score fields accept only integer 0-5 or null. The results CSV has 84 preallocated unreviewed rows and assigns no score or visual outcome.

## 13. Scoring schema

The scoring schema defines 0 as absent/catastrophic, 1 weak, 2 partial, 3 acceptable, 4 strong, and 5 clear/reusable. Family-specific required dimensions and mandatory-null non-applicable dimensions are explicit.

## 14. Failure-label schema

The failure-label schema defines 27 labels covering package, preflight, command, upload, submit, remote generation, count, download, identity, structure, prompt, reference, spatial, camera, action, causal, reaction, environment, frame fidelity, temporal, style, timing, extra/duplicate subject, corruption, and route-reset failure classes.

## 15. Review-artifact plan

For a future successful downloaded video, the plan records metadata; frames at 0.00s, 1.00s, 2.00s, 3.00s, and 4.00s; a final readable frame; one 3x2 contact sheet; and input/output SHA256. No cut, final, or lock is planned by default. P1-R2 created no review artifact or media.

## 16. Budget plan

- user_reported_credits: 6447
- fixed_task_count: 84
- planned_unit_cost_assumption: 70
- planned_total_cost: 5880
- credit_floor: 560
- budget_plus_floor: 6440
- planning_residual: 7
- live_cost_verified: false
- Any later cost above the assumption must block activation or execution.

## 17. Human manifest review checklist

The human checklist covers counts, matrix integrity, fixture rights and eligibility, project-wide value, excluded action routes, budget, expected counts, no-submit flags, stop conditions, Source governance, CAL-001B exclusion, final, and lock. Acceptance fields remain blank or false.

## 18. P2 checklist

The independent checklist covers matrix, fixture legality, semantic equivalence, stored-help compatibility, package/manifest consistency, hashes, budget, permissions, stop conditions, no partial activation, and Source governance. P2 completion and pass fields remain false.

## 19. Matrix and README

The matrix lists all 84 IDs with family, architecture, replicate, fixture set, task type, prompt path, package path, and planned cost. README documents fixed versus adaptive scope, CAL-001A versus CAL-001B, directories, no-run state, activation sequence, result flow, human review, and final/lock boundaries.

## 20. Inventory hashes

- fixed_manifest_sha256: b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d
- fixture_registry_sha256: cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142
- prompt_inventory_sha256: 27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d
- package_inventory_sha256: b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c
- full_experiment_inventory_sha256: 448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138
- Inventory encoding: UTF-8, lexicographic experiment ordering, LF endings, and one final LF.

| Required artifact | SHA256 |
| --- | --- |
| experiments/CAL-001/.gitattributes | a79691a93b46e49ce460c26ef22afcc03d6eca1e63bf2edbc20e96159510f6c9 |
| experiments/CAL-001/README.md | c91803bb5a27149e8bf7e340c2ec08d50bb1ebfe41f464938e34cb8cfa106e3a |
| experiments/CAL-001/fixtures/CAL001_fixture_registry.json | cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142 |
| experiments/CAL-001/manifests/CAL001A_fixed_84_task_manifest.csv | b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d |
| experiments/CAL-001/schemas/CAL001_experiment_record.schema.json | b3b1797cccf5e974c161f770fdf14386ae8185512cbad0e2ae2738d017210cbb |
| experiments/CAL-001/schemas/CAL001_scoring.schema.json | 0ed3f3f1886b132cd44c125f3dc5a7f0dd0c198caa2fb217c4a5ee1a0600796e |
| experiments/CAL-001/schemas/CAL001_failure_labels.schema.json | aaa6baf1a91bae1953617c6b8070c646356859c3bd06dcaa64c8e03b5072359c |
| experiments/CAL-001/datasets/CAL001_experiment_results_template.csv | 95cdc5bea1445ea21346c61c666165a8b7cef15de7b75a8fcb6d48d132338eed |
| experiments/CAL-001/datasets/CAL001_visual_review_template.jsonl | d36b08bc1dd5ef6792676eac99cc3b2be07ff2edc32b7ef7cd81940a33d02869 |
| experiments/CAL-001/reviews/CAL001_human_manifest_review_checklist.md | cf7887b5fd610108dffef24eeaccf003cd908334643dddd0166ed13d25332e13 |
| experiments/CAL-001/reviews/CAL001_P2_independent_review_checklist.md | d8084f1236631cd60a9abe8e0604624d6450c7d53e7507cc0737e1478e338e8b |
| experiments/CAL-001/budget/CAL001_budget_plan.md | 41592ef135d11f49ac8bb158a7b60c2eab3e6bc79318c35217e42199b81def12 |
| experiments/CAL-001/matrices/CAL001_fixed_experiment_matrix.md | d047b9fc6a1b9e2a97598ad9d13383b9f8f2f173712b15941e866025593e3209 |

Individual prompt and package hashes are recorded in all applicable manifest rows and were recomputed during validation.

## 21. Validation results

- exact_7x4x3_matrix: pass
- unique_experiment_ids_84: pass
- prompt_files_28: pass
- package_json_files_84_parseable: pass
- manifest_rows_84_parseable: pass
- package_and_prompt_paths_exist: pass
- prompt_package_fixture_hashes_match: pass
- duplicate_output_dir_output_name_pairs: 0
- replicate_prompt_bytes_and_fixed_fields_identical: pass
- package_manifest_consistency: pass
- image2video_and_frames2video_ratio_omitted: pass
- stored_help_task_settings_compatible_at_no_run_level: pass
- all_authorization_flags_false: pass
- CAL001_media_files_created: 0
- deterministic_LF_checkout_policy: pass
- visual_scores_or_outcomes_assigned: false

## 22. No-run/no-submit gates

Dreamina execution, provider canaries, version, user_credit, help, submit, query, download, retry, resubmit, batch, CAL-001A activation, and CAL-001B creation all remained forbidden and did not occur. Every row remains planned_no_run.

## 23. Source governance

Official Source remained human-controlled and read-only. This phase created, edited, deleted, renamed, moved, staged, committed, and pushed no file under sources/. Final pre-commit Source cleanliness must still be rechecked.

## 24. Explicit non-actions

No Dreamina command, live provider call, credit consumption, media generation, crop, transcode, resize, edit, frame extraction, contact sheet, cut, visual review, scoring, source change, adaptive task, final, lock, or tag occurred.

## 25. Risks and unresolved issues

- The 70-credit unit cost and all runtime command facts remain planning-level until P3 live canaries.
- The F02 fixture is 9:16; ratio is intentionally inferred and no media alteration was allowed.
- F05 compatibility uses a same-sequence 1.15s-to-1.30s limited recovery transition; P2 should independently review this fixed pair.
- Shared physical identity and scene assets across F06 and F07 are intentional; reference duties differ by family.
- Active Source header wording remains nonblocking metadata debt and was not edited.
- Human manifest review and acceptance remain false, so execution authority remains inactive.

## 26. Recommended next phase

CAL-001-P2_INDEPENDENT_MANIFEST_PACKAGE_BUDGET_PERMISSION_REVIEW

## 27. Final verdict

CAL001_P1_R2_FIXED_84_TASK_NO_RUN_MANIFEST_AND_SCHEMAS_CREATED_READY_P2_INDEPENDENT_REVIEW

## Files read

- sources/AI视频制作_Source索引与使用优先级_V1.11.md
- sources/AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md
- sources/AI视频制作_自动化治理与Source权限规则_V0.1.md
- sources/AI视频制作_自动化宏流程与授权等级_V0.2.md
- sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md
- sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md
- sources/dreamina_cli_help_latest.md
- sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md
- sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md
- reports/PHASE_CAL001A_CONDITIONAL_BOUNDED_CALIBRATION_MACRO_AUTHORIZATION_DECISION.md
- reports/PHASE_CAL001_P1_PROJECT_WIDE_PROMPT_CALIBRATION_NO_RUN_MANIFEST_AND_SCHEMA_CREATION_RESULT.md
- productions/chi_yan_tian_qiong/assets/asset_registry.json
- productions/chi_yan_tian_qiong/assets/A-CH-B-IDENTITY-002_planning_record.json
- productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-002-R02_safe.csv
- productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V008.csv
- productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V008.json
- reports/PHASE_K12_SHOT02_V008_AFTERSHOCK_RAIN_RECOVERY_PACKAGE_REPORT.md
- reports/PHASE_K61_SHOT02_V014_R02_UPLOADSAFE_PACKAGE_REVIEW.md
