# PHASE K270B - SHOT-04 R02a Static/Dynamic Burst Two-Shot Route Planning

## 1. Phase summary

- phase_id: K270B_SHOT04_R02A_STATIC_DYNAMIC_BURST_TWO_SHOT_ROUTE_PLANNING_NO_SUBMIT
- purpose: create a no-submit planning report for the SHOT-04 R02a static/dynamic burst two-shot route after K270A.
- mode: planning/report-only
- planning_recorded: true
- recommended_route: recommend_static_contact_cut_plus_new_dynamic_flyout_package_planning
- recommended_next_phase: K270C_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_AUTHORIZATION_DECISION
- final_master: false
- locked: false

## 2. K270A route decision carry-forward

- K270A_final_verdict: K270A_STATIC_DYNAMIC_BURST_ROUTE_DECISION_READY_K270B_TWO_SHOT_PLANNING_NO_SUBMIT
- K270A_recommended_route: recommend_two_shot_static_dynamic_burst_route
- K270A_recommended_next_phase: K270B_SHOT04_R02A_STATIC_DYNAMIC_BURST_TWO_SHOT_ROUTE_PLANNING_NO_SUBMIT
- key_static_dynamic_insight: use existing Variant A cut material as the static/contact hit-stop beat, then design a separate fast dynamic fly-out beat with visible displacement.
- selected_static_contact_cut: CONTACT_HITSTOP_SHORT
- dynamic_flyout_need: separate explosive displacement shot with speed, visible distance, body travel, rain/water/debris response, and no sustained contact.

## 3. K269Z static/dynamic insight carry-forward

- overall_conclusion: cut_candidate_worth_testing_in_edit
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

Creative correction carried forward:

- impact force needs contrast between static and dynamic.
- static beat can be charge, tension, short hold, contact, impact moment, or slow-motion impact detail.
- dynamic beat must show the opponent flying away quickly over visible distance.
- current cuts can provide contact/hit-stop material.
- a new fast-flyout or explosive displacement shot is still needed.
- extending sustained contact is not a solution.

## 4. Existing static-contact material selection

- primary_static_contact_cut: CONTACT_HITSTOP_SHORT
- primary_time_window: 0.50s-1.00s
- primary_sha256: `ace57b50c6e3b28aecff8c495ced690aa560b4c3744f95812487f1fcd48d8ab8`
- primary_function: close-range guard impact, hit-stop, and held impact moment.
- primary_status: supporting insert only, not primary/final.
- primary_limitation: does not contain fly-out or real explosive displacement.

- alternate_static_contact_cut: CONTACT_HITSTOP_PADDED
- alternate_time_window: 0.50s-1.25s
- alternate_sha256: `ce00c6fba08406ce04220bb2a41d0ee97a6aacbc0bc6fb25ade782458e7c168f`
- alternate_function: slightly longer static beat if the edit needs more breathing room.
- alternate_limitation: begins to increase sustained-pressure risk.

Other cut material:

- LATE_REACTION_EVIDENCE, 3.75s-4.50s, `1de952c841eb8505b64d8488218ba2d7ea48ad6dd2151d27174541b106271f8f`: reaction reference only, not final burst.
- CONTACT_EVIDENCE_LONGER, 0.50s-1.50s, `e55b55368837519f063ef525654ae0847c365a154f19b6eaac8933073a398a49`: diagnostic evidence only; reintroduces sustained pressure.

Input source video:

- `productions/chi_yan_tian_qiong/downloads/SHOT-04-R02A/K269S_VARIANT_A_SIMPLIFIED_M2V/df668f21-6bf2-416e-964f-7dfc73995518_video_1.mp4`
- source_video_sha256: `e463971bf481e0cf17550a1c2d1ab279e91d3fbf0e54c5c43aeb400a1cebe9c0`

## 5. Dynamic fly-out beat requirements

The future dynamic beat must show:

- Shuangji suddenly launched away from the impact.
- visible travel distance, preferably multiple body lengths or a clear floor-distance gap.
- fast body displacement within the first useful second.
- hair, sash, cloth, armor ribbons, and limbs trailing with acceleration.
- wet floor splash, rain spray, dust, debris, or broken droplets reacting to force.
- Fenshou may appear in foreground or edge of frame in follow-through pose, but should not remain locked in prolonged contact.
- camera wide enough or tracking enough to show displacement distance.
- motion reading as explosive launch, not shove, drift, hover, or walk-back.

Strict negatives for the dynamic beat:

- no sustained pressure
- no slow hold
- no gentle backstep
- no delayed reaction
- no static aftermath only
- no prolonged guard clash
- no stuck arms
- no grappling
- no floating slowly
- no camera too tight to show displacement
- no identity swap

## 6. Two-shot continuity rules

- Beat A ends on static hit-stop/contact.
- Beat B begins with immediate release/flyout, not another long push.
- Direction should stay consistent: Fenshou left/near side, Shuangji launched right/backward.
- Environment remains rainy dark temple / wet stone floor unless a later deliberate map transition is authorized.
- Costume colors remain Fenshou black-red and Shuangji blue-white-silver.
- Perfect frame continuity is not required; later edit logic may use impact flash, sound hit, water burst, or a motion cut.
- LATE_REACTION_EVIDENCE is not the actual dynamic beat; it is only reaction reference.
- No current cut is final or locked.

## 7. Candidate dynamic beat framing options

### B1 wide_side_flyout_result_shot

- side or 3/4 wide framing.
- Fenshou at left or near side in follow-through.
- Shuangji blasts right/backward across wet temple floor.
- visible distance and water spray make speed readable.
- likely safest for displacement readability.

### B2 impact_detail_then_acceleration

- begins near contact or just after contact.
- brief slow-motion impact detail: water droplets, dust, armor vibration, face tension.
- immediately shifts to fast/real speed launch.
- visually strong but harder to control inside one generated shot.

### B3 result_only_flyout_after_hit

- begins after hit-stop, with Shuangji already being thrown backward.
- no need to show contact again.
- focuses entirely on fast body travel, sliding/flying, floor splash, and distance.
- may be easiest for a future AI generation because it avoids modeling the precise contact moment again.

### B4 wall_or_column_impact_result

- Shuangji flies into a wall/column or near-wall impact.
- strong if it works.
- riskier because previous wall-impact routes were brittle.
- optional only, not the first requirement.

## 8. Recommended dynamic beat direction

- primary_recommendation: B3 result_only_flyout_after_hit
- secondary_recommendation: B1 wide_side_flyout_result_shot
- reason: both prioritize readable distance and speed rather than forcing the model to solve contact and launch in the same shot.
- B2_status: visually attractive but harder to control; consider later if B3/B1 planning is insufficient.
- B4_status: optional high-risk extension only; do not make wall/column impact the first requirement.

Recommended Beat B design sentence:

After the static CONTACT_HITSTOP_SHORT beat, cut to Shuangji already releasing from the impact and flying backward across the rain-slick stone floor, with clear multi-body-length displacement, trailing cloth/hair/limbs, water spray and debris reacting instantly, while Fenshou remains only as a brief follow-through presence and no prolonged contact occurs.

## 9. Future package strategy, report-only

This report does not create prompt files, package JSON, or manifest CSV. It only records future package direction.

Likely future task:

- dynamic fly-out M2V or text2video package, no-submit first.

Likely model:

- seedance2.0_vip if continuing the Dreamina route.

Likely reference strategy:

- prefer the same two identity refs if M2V is chosen, because Variant A proved two-ref M2V preserves identity better than prompt-only.

Possible prompt focus:

- result-first fast flyout.
- wide distance.
- wet-floor splash and force feedback.
- immediate release after impact.
- no contact hold.

Possible negative prompt / constraints:

- no prolonged guard clash.
- no slow shove.
- no stuck arms.
- no grappling.
- no delayed reaction.
- no gentle stepping backward.
- no floating slowly.
- no static aftermath only.
- no camera too tight to show displacement.
- no identity swap.

## 10. Route options comparison

| option | description | value | risk | K270B decision |
|---|---|---|---|---|
| 1 static_contact_cut_plus_new_dynamic_flyout_package | Use CONTACT_HITSTOP_SHORT as Beat A and later create a no-submit dynamic flyout package as Beat B | Directly uses strongest existing material and targets missing displacement | Requires later package authorization and continuity planning | Recommended main direction |
| 2 local_assembly_test_first | Locally assemble CONTACT_HITSTOP_SHORT plus LATE_REACTION_EVIDENCE for diagnostic comparison | No Dreamina spend, may clarify edit timing | Does not solve true fast displacement | Optional later diagnostic, not main |
| 3 single_revised_burst_first_m2v | One future generated shot includes strike, hit-stop, and fly-out | Direct and simple if it works | Model may revert to sustained pressure | Fallback/parallel, not preferred |
| 4 pause_R02a_and_plan_R02b | Redefine R02a as contact/hit-stop and move flyout to R02b | Clear segmentation possible | R02a must not pretend to be complete | Possible only with explicit segmentation |

## 11. Recommended route

- recommended_route: recommend_static_contact_cut_plus_new_dynamic_flyout_package_planning
- Beat_A: CONTACT_HITSTOP_SHORT, 0.50s-1.00s, static/contact/hit-stop supporting insert.
- Beat_A_alternate: CONTACT_HITSTOP_PADDED, 0.50s-1.25s, if slightly more breathing room is needed.
- Beat_B: new dynamic fly-out / explosive displacement shot, preferably B3 result-only flyout after hit or B1 wide side flyout result shot.
- LATE_REACTION_EVIDENCE: reaction reference only.
- CONTACT_EVIDENCE_LONGER: diagnostic only.
- current_cuts_final: false
- current_route_locked: false

## 12. Recommended next phase

- recommended_next_phase: K270C_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_AUTHORIZATION_DECISION

K270C should be report-only and decide whether the human authorizes a later no-submit package creation phase for the dynamic fly-out beat. K270C should not run Dreamina, submit, query, download, cut, create media, final, or lock.

## 13. Source governance confirmation

- Official Project Source files remain human-controlled.
- Codex read Source context only.
- sources_modified: false
- source_updates_created: false
- source_updates_staged: false
- this_report_is_official_Source: false

Files read for K270B:

- `reports/PHASE_K270A_SHOT04_R02A_STATIC_DYNAMIC_BURST_ROUTE_DECISION.md`
- `reports/PHASE_K269Z_SHOT04_R02A_VARIANT_A_CUT_WINDOW_VISUAL_REVIEW.md`
- `reports/PHASE_K269Y_SHOT04_R02A_VARIANT_A_CUT_WINDOW_DIAGNOSTICS_ONLY_RESULT.md`
- `reports/PHASE_K269X_SHOT04_R02A_VARIANT_A_CUT_WINDOW_AUTHORIZATION_DECISION.md`
- `reports/PHASE_K269V_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_VISUAL_REVIEW.md`
- `reports/PHASE_K269U_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_REVIEW_ARTIFACTS_ONLY_RESULT.md`
- `reports/PHASE_K269S_SHOT04_R02A_VARIANT_A_SIMPLIFIED_M2V_DOWNLOAD_ONLY_RESULT.md`
- `reports/PHASE_K269M_SHOT04_R02A_POST_VARIANT_C_VISUAL_ROUTE_DECISION.md`
- `reports/PHASE_K269L_SHOT04_R02A_VARIANT_C_TEXT2VIDEO_VISUAL_REVIEW.md`
- `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001_multimodal2video_no_submit_prompt.txt`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A-safe-variant-set/K269B/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-SIMPLIFIED-001_package.json`
- read-only Source context under `sources/`

## 14. Explicit non-actions

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
- cuts_assembled: false
- video_modified: false
- mp4_modified: false
- frames_extracted: false
- contact_sheets_created: false
- prompt_file_created: false
- prompt_file_modified: false
- package_json_created: false
- package_json_modified: false
- manifest_csv_created: false
- manifest_csv_modified: false
- sources_modified: false
- generated_cuts_staged: false
- review_artifacts_staged: false
- final_master: false
- locked: false
- tag_created: false

## 15. Safety flags

- no_current_cut_is_final: true
- no_primary_insert_yet: true
- Beat_A_supporting_insert_only: true
- Beat_B_requires_future_authorization: true
- future_package_creation_requires_human_authorization: true
- future_live_action_requires_separate_authorization: true
- final_master: false
- locked: false

## 16. Final verdict

K270B_TWO_SHOT_STATIC_DYNAMIC_BURST_PLANNING_READY_K270C_DYNAMIC_FLYOUT_PACKAGE_AUTHORIZATION_DECISION
