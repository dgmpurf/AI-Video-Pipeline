# PHASE K270A - SHOT-04 R02a Static/Dynamic Burst Route Decision

## 1. Phase summary

- phase_id: K270A_SHOT04_R02A_STATIC_DYNAMIC_BURST_ROUTE_DECISION_REPORT_ONLY
- purpose: record the route decision after K269Z cut-window visual review.
- mode: report-only
- route_decision_recorded: true
- recommended_route: recommend_two_shot_static_dynamic_burst_route
- recommended_next_phase: K270B_SHOT04_R02A_STATIC_DYNAMIC_BURST_TWO_SHOT_ROUTE_PLANNING_NO_SUBMIT
- final_master: false
- locked: false

## 2. K269Z cut-window visual review carry-forward

- K269Z_final_verdict: K269Z_VARIANT_A_CUT_WINDOW_VISUAL_REVIEW_RECORDED_READY_K270A_STATIC_DYNAMIC_BURST_ROUTE_DECISION
- K269Z_overall_conclusion: cut_candidate_worth_testing_in_edit
- best_cut_candidate_exists: true
- best_cut_id: CONTACT_HITSTOP_SHORT
- best_cut_time_window: 0.50s-1.00s
- usable_as_SHOT04_R02A_primary_insert: false
- usable_as_supporting_edit_insert: true

K269Z cut ranking:

1. CONTACT_HITSTOP_SHORT
2. CONTACT_HITSTOP_PADDED
3. LATE_REACTION_EVIDENCE
4. CONTACT_EVIDENCE_LONGER

K269Z failure/caveat labels carried forward:

- insufficient_static_to_dynamic_contrast
- insufficient_fast_displacement_distance
- sustained_contact_not_converted_to_velocity
- impact_without_true_explosive_followthrough
- reaction_exists_but_not_enough_burst
- contact_cut_needs_following_flyout_shot
- no_primary_insert_yet
- final_master_false
- locked_false

K269Z positive evidence labels carried forward:

- usable_contact_hitstop_short_candidate
- identity_continuity_good_in_cuts
- contact_readability_pass
- cut_windows_reduce_sustained_pressure
- late_reaction_has_some_received_force_feeling
- static_dynamic_design_direction_identified
- edit_test_worthwhile

## 3. Static/dynamic burst insight carry-forward

The key creative correction from K269Z is that impact force needs contrast between a static or held impact beat and a fast dynamic displacement beat.

- static portion: charge, tension, short hold, impact moment, or slow-motion impact detail.
- dynamic portion: the opponent must fly away quickly over visible distance.
- current Variant A cuts can provide contact/hit-stop material.
- a later fast-flyout or explosive displacement shot is still needed.
- a longer sustained contact shot is not the same as burst force.

## 4. Current route state

- source_video: `productions/chi_yan_tian_qiong/downloads/SHOT-04-R02A/K269S_VARIANT_A_SIMPLIFIED_M2V/df668f21-6bf2-416e-964f-7dfc73995518_video_1.mp4`
- source_video_sha256: `e463971bf481e0cf17550a1c2d1ab279e91d3fbf0e54c5c43aeb400a1cebe9c0`
- current_best_static_contact_cut: CONTACT_HITSTOP_SHORT
- alternate_static_contact_cut: CONTACT_HITSTOP_PADDED
- reaction_reference_only: LATE_REACTION_EVIDENCE
- diagnostic_only_cut: CONTACT_EVIDENCE_LONGER
- current_cuts_are_final: false
- primary_insert_ready: false

K269Y cut evidence:

| cut_id | time_window | sha256 | current role |
|---|---:|---|---|
| CONTACT_HITSTOP_SHORT | 0.50s-1.00s | `ace57b50c6e3b28aecff8c495ced690aa560b4c3744f95812487f1fcd48d8ab8` | best static/contact/hit-stop candidate |
| CONTACT_HITSTOP_PADDED | 0.50s-1.25s | `ce00c6fba08406ce04220bb2a41d0ee97a6aacbc0bc6fb25ade782458e7c168f` | alternate static beat with more breathing room |
| CONTACT_EVIDENCE_LONGER | 0.50s-1.50s | `e55b55368837519f063ef525654ae0847c365a154f19b6eaac8933073a398a49` | diagnostic evidence only |
| LATE_REACTION_EVIDENCE | 3.75s-4.50s | `1de952c841eb8505b64d8488218ba2d7ea48ad6dd2151d27174541b106271f8f` | reaction reference only, not final burst |

## 5. Option A local edit assembly / compare cut

- option_id: local_edit_assembly_compare_cut
- description: use existing Variant A cut clips to create a local diagnostic assembly or compare edit, with CONTACT_HITSTOP_SHORT or CONTACT_HITSTOP_PADDED as the static/contact beat and LATE_REACTION_EVIDENCE as reaction support.
- value: no Dreamina credits, tests whether existing cut material can create a convincing edit illusion, uses strongest identity/contact evidence, and can compare the 0.50s-1.00s beat against the 0.50s-1.25s beat.
- risk: LATE_REACTION_EVIDENCE still lacks true explosive displacement, causality may remain weak, and the assembly may only prove supporting evidence rather than a complete action solution.
- decision_tendency: useful as optional local diagnostic, but not enough as the main route by itself.
- K270A_action_taken: none; no edit assembly created in this phase.

## 6. Option B revised burst-first M2V package

- option_id: revised_burst_first_m2v_package
- description: create a future no-submit M2V prompt/package focused on short hard impact and immediate fly-out within one generated clip.
- value: directly targets missing explosion, fast displacement, and static/dynamic contrast; can encode negatives against sustained pressure and slow hold; may produce a cleaner one-clip R02a candidate.
- risk: a single continuous AI video may again turn impact into sustained pressure, it would consume future Dreamina credits if submitted later, and precise temporal contrast may remain difficult for the model.
- decision_tendency: important fallback or parallel later route, but should not be the only next step.
- K270A_action_taken: none; no prompt or package created in this phase.

## 7. Option C two-shot static/dynamic burst route

- option_id: two_shot_static_dynamic_burst_route
- description: split SHOT-04 R02a into two beats:
  - static/contact/hit-stop beat from existing CONTACT_HITSTOP_SHORT or CONTACT_HITSTOP_PADDED.
  - dynamic fast-flyout/explosive displacement beat as a separate future shot or package.
- possible_structure: R02a contact/hit-stop insert from Variant A cut plus R02a2 or R02b fast fly-out, wall-impact, through-wall, or distance-displacement result shot.
- value: directly follows the human creative correction, reduces the burden on one AI generation, preserves strongest current evidence, narrows the next generation goal to fast displacement after impact, and can later combine with local edit assembly if authorized.
- risk: requires planning a new dynamic fly-out shot, continuity between the two beats must be controlled carefully, may need future generation authorizations, and remains non-final without later visual review.
- decision_tendency: recommended main route.
- K270A_action_taken: route recommendation only; no media or package created.

## 8. Option D keep current cuts as diagnostic evidence only

- option_id: keep_current_cuts_as_diagnostic_evidence_only
- description: stop active R02a cut-window exploration and preserve current cuts only as evidence.
- value: avoids further work and spending, and preserves findings for later prompt revision.
- risk: does not create a viable action solution, ignores a clear static/dynamic route insight, and stops before exploiting the strongest current direction.
- decision_tendency: not recommended as the next main route.
- K270A_action_taken: not selected as main route.

## 9. Comparative risk/value table

| option | value | risk | decision |
|---|---|---|---|
| A local_edit_assembly_compare_cut | No Dreamina credits; tests edit illusion with existing cuts | Weak causality and no true fly-out | Optional diagnostic, not main route |
| B revised_burst_first_m2v_package | Directly targets burst force in one generated clip | May repeat sustained-pressure failure inside one shot | Useful fallback/parallel route |
| C two_shot_static_dynamic_burst_route | Splits static impact and dynamic displacement into solvable beats | Requires continuity planning and later authorization | Recommended main route |
| D keep_current_cuts_as_diagnostic_evidence_only | Stops spending and preserves evidence | Produces no viable action solution | Not recommended |

## 10. Recommended route

- recommended_route: recommend_two_shot_static_dynamic_burst_route
- selected_static_contact_cut: CONTACT_HITSTOP_SHORT
- alternate_static_contact_cut: CONTACT_HITSTOP_PADDED
- reaction_reference_only: LATE_REACTION_EVIDENCE
- diagnostic_only_cut: CONTACT_EVIDENCE_LONGER
- dynamic_flyout_need: a separate fast-flyout or explosive displacement beat with visible travel distance, clear speed, body displacement, rain/water/debris response, and no sustained contact.
- current_cuts_final: false
- lock_status: false

Route rule:

Use existing Variant A cut material as the static/contact/hit-stop beat, but do not treat any current cut as the complete action solution. The main next route should design the dynamic fly-out beat separately.

## 11. Recommended next phase

- recommended_next_phase: K270B_SHOT04_R02A_STATIC_DYNAMIC_BURST_TWO_SHOT_ROUTE_PLANNING_NO_SUBMIT

K270B should be no-submit/report-or-planning only and should:

- design the two-shot static/dynamic burst structure.
- define the static beat from existing cuts.
- define dynamic fly-out beat requirements.
- propose prompt/package direction for the dynamic fly-out shot.
- include strict negatives:
  - no sustained pressure
  - no slow hold
  - no gentle shove
  - no delayed reaction
  - no weak displacement
  - no static aftermath only
- not run Dreamina.
- not submit/query/download.
- not create media.
- not final/lock.

## 12. Source governance confirmation

- Official Project Source files remain human-controlled.
- Codex read Source context only.
- sources_modified: false
- source_updates_created: false
- source_updates_staged: false
- this_report_is_official_Source: false

Files read for K270A:

- `reports/PHASE_K269Z_SHOT04_R02A_VARIANT_A_CUT_WINDOW_VISUAL_REVIEW.md`
- `reports/PHASE_K269Y_SHOT04_R02A_VARIANT_A_CUT_WINDOW_DIAGNOSTICS_ONLY_RESULT.md`
- `reports/PHASE_K269X_SHOT04_R02A_VARIANT_A_CUT_WINDOW_AUTHORIZATION_DECISION.md`
- `reports/PHASE_K269W_SHOT04_R02A_VARIANT_A_POST_VISUAL_ROUTE_DECISION.md`
- `reports/PHASE_K269V_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_VISUAL_REVIEW.md`
- `reports/PHASE_K269U_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_REVIEW_ARTIFACTS_ONLY_RESULT.md`
- `reports/PHASE_K269S_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_DOWNLOAD_ONLY_RESULT.md`
- `reports/PHASE_K269M_SHOT04_R02A_POST_VARIANT_C_VISUAL_ROUTE_DECISION.md`
- `reports/PHASE_K269L_SHOT04_R02A_VARIANT_C_TEXT2VIDEO_VISUAL_REVIEW.md`
- `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001_multimodal2video_no_submit_prompt.txt`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A-safe-variant-set/K269B/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001_package.json`
- read-only Source context under `sources/`

## 13. Explicit non-actions

- Dreamina_run: false
- dreamina_version_run: false
- dreamina_user_credit_run: false
- dreamina_help_run: false
- submit_count: 0
- query_count: 0
- download_count: 0
- retry_count: 0
- resubmit_count: 0
- batch_count: 0
- media_created: false
- video_cut: false
- video_modified: false
- frames_extracted: false
- contact_sheets_created: false
- prompt_created: false
- prompt_modified: false
- package_created: false
- package_modified: false
- manifest_created: false
- manifest_modified: false
- sources_modified: false
- generated_cuts_staged: false
- review_artifacts_staged: false
- final_master: false
- locked: false
- tag_created: false

## 14. Safety flags

- no_current_cut_is_final: true
- no_primary_insert_yet: true
- supporting_edit_insert_possible: true
- future_visual_review_required: true
- future_live_action_requires_separate_authorization: true
- final_master: false
- locked: false

## 15. Final verdict

K270A_STATIC_DYNAMIC_BURST_ROUTE_DECISION_READY_K270B_TWO_SHOT_PLANNING_NO_SUBMIT
