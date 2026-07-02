# PHASE K270C - SHOT-04 R02A2 Dynamic Fly-Out No-Submit Package Authorization Decision

## 1. Phase summary

- phase_id: K270C_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_AUTHORIZATION_DECISION
- purpose: record human authorization scope for a future SHOT-04 R02A2 dynamic fly-out no-submit package creation route after K270B.
- mode: report-only authorization record
- authorization_recorded: true
- authorization_reconstructed_from_base64: true
- future_package_created_in_K270C: false
- final_master: false
- locked: false

## 2. UTF-8 authorization reconstruction and SHA256 verification

- authorization_source: AUTHORIZATION_TEXT_UTF8_BASE64 from the K270C request
- decoded_as: UTF-8
- expected_sha256: `5c332d79318a2cd45867c13d7e5097bf62a101a0c358165111a210463d11b999`
- actual_decoded_utf8_sha256: `5c332d79318a2cd45867c13d7e5097bf62a101a0c358165111a210463d11b999`
- decoded_authorization_sha256_match: true
- decoded_text_begins_with: `我授权 K270C`
- required_phrases_present: true
- forbidden_mojibake_markers_present: false

## 3. Human authorization text

```text
我授权 K270C：对 K270B 推荐的 SHOT-04 R02A2 dynamic fly-out no-submit package creation 路线进入授权记录。只允许下一阶段记录未来创建动态飞出段 no-submit package 的授权范围，方向以 B3 result_only_flyout_after_hit 为主、B1 wide_side_flyout_result_shot 为备选；不允许创建 prompt/package/manifest 文件，不允许生成媒体，不允许 Dreamina submit/query/download/retry/resubmit/batch，不允许 final/lock。
```

## 4. Authorization interpretation

- K270C records authorization only.
- K270C does not create prompt files.
- K270C does not create package JSON.
- K270C does not create manifest CSV.
- K270C does not generate media.
- K270C does not run Dreamina.
- K270C does not execute K270D.
- Future K270D may create no-submit package materials for the dynamic fly-out beat only.
- Future submit/query/download/retry/resubmit/batch remain unauthorized and require separate human authorization.
- final_master remains false.
- locked remains false.

## 5. K270B planning carry-forward

- K270B_final_verdict: K270B_TWO_SHOT_STATIC_DYNAMIC_BURST_PLANNING_READY_K270C_DYNAMIC_FLYOUT_PACKAGE_AUTHORIZATION_DECISION
- recommended_route: recommend_static_contact_cut_plus_new_dynamic_flyout_package_planning
- selected_static_contact_cut: CONTACT_HITSTOP_SHORT
- alternate_static_contact_cut: CONTACT_HITSTOP_PADDED
- recommended_dynamic_beat_direction: prefer B3 result_only_flyout_after_hit, with B1 wide_side_flyout_result_shot as secondary.
- future_package_strategy_summary: future no-submit dynamic flyout M2V/T2V planning only, likely seedance2.0_vip, preferably same two identity refs if M2V, focused on result-first fast flyout, wide distance, wet-floor splash, and no contact hold.

## 6. Static Beat A carry-forward

- Beat_A_primary: CONTACT_HITSTOP_SHORT
- Beat_A_primary_time_window: 0.50s-1.00s
- Beat_A_primary_role: static/contact/hit-stop supporting insert
- Beat_A_alternate: CONTACT_HITSTOP_PADDED
- Beat_A_alternate_time_window: 0.50s-1.25s
- Beat_A_alternate_role: slightly longer static beat if more breathing room is needed
- current_cuts_final: false
- current_cuts_locked: false

## 7. Dynamic Beat B authorization scope

Future K270D is authorized to create a no-submit package set for the dynamic fly-out beat only.

Authorized future K270D scope:

- prompt text file(s)
- package JSON file(s)
- manifest CSV or manifest markdown
- no-submit execution notes
- package review notes
- report only

Future K270D remains prohibited from:

- running Dreamina
- submit
- query
- download
- retry
- resubmit
- batch
- creating media
- final
- lock

## 8. Primary B3 result-only flyout direction

- primary_direction: B3 result_only_flyout_after_hit
- concept: begins after the hit-stop, with Shuangji already being thrown backward.
- contact_requirement: no need to show contact again.
- focus: fast body travel, visible displacement, wet-floor splash, and distance.
- rationale: likely easiest future AI generation direction because it avoids modeling the precise contact moment again.

## 9. Secondary B1 wide-side flyout direction

- secondary_direction: B1 wide_side_flyout_result_shot
- concept: side or 3/4 wide framing.
- Fenshou_position: left or near side in follow-through.
- Shuangji_motion: blasts right/backward across wet temple floor.
- readability_goal: visible distance and water spray make speed readable.
- rationale: safe for displacement readability.

## 10. Future K270D no-submit package creation scope

- project_segment: SHOT-04 R02A2 dynamic fly-out / explosive displacement beat
- purpose: provide Beat B after existing Variant A CONTACT_HITSTOP_SHORT static/contact beat.
- preferred_route: M2V if using the same two identity refs, because Variant A proved two-ref M2V preserves identity better than prompt-only.
- possible_fallback: T2V diagnostic only if M2V package planning is blocked.
- likely_model: seedance2.0_vip
- likely_duration: 4-5s or shortest allowed practical duration according to current Dreamina help/source.
- likely_resolution: 720p first unless later explicitly changed.
- likely_ratio: 16:9

Future K270D should preserve:

- Fenshou: black-red armor, attacker, follow-through presence only.
- Shuangji: blue-white-silver armor, defender launched away, visible body travel.
- environment: rainy dark temple / wet stone floor.
- motion_direction: Fenshou left/near side, Shuangji launched right/backward unless K270D gives a clear reason to adjust.
- continuity: Beat A ends on static contact/hit-stop; Beat B begins with immediate release/flyout.

## 11. Future dynamic fly-out requirements

Future dynamic fly-out must show:

- Shuangji suddenly launched away from the impact.
- visible travel distance, preferably multiple body lengths or a clear floor-distance gap.
- fast body displacement within the first useful second.
- hair, sash, cloth, armor ribbons, and limbs trailing with acceleration.
- wet floor splash, rain spray, dust, debris, or broken droplets reacting to force.
- Fenshou may appear in foreground or edge of frame in follow-through pose.
- no prolonged contact.
- camera wide enough or tracking enough to show displacement distance.
- motion reads as explosive launch, not shove, drift, hover, or walk-back.

## 12. Strict negatives

- no sustained pressure
- no slow hold
- no gentle shove
- no gentle backstep
- no delayed reaction
- no static aftermath only
- no prolonged guard clash
- no stuck arms
- no grappling
- no floating slowly
- no camera too tight to show displacement
- no identity swap
- no re-solving the contact moment as a long clash
- no drifting without ground/water feedback
- no tiny displacement

## 13. Reference strategy

If future K270D chooses M2V, prefer the same two locked identity refs used by Variant A:

- Fenshou ref: `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- Shuangji ref: `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`

K270C does not verify or hash these refs. K270C records the future authorization scope only.

## 14. Explicitly forbidden actions

Forbidden in K270C:

- run Dreamina
- run dreamina version/user_credit/help
- submit
- query
- download
- retry
- resubmit
- batch
- create media
- cut video
- assemble cuts
- modify any mp4
- extract frames
- create contact sheets
- create prompt files
- create package JSON
- create manifest CSV
- modify sources/
- stage media
- stage generated cuts
- stage review artifacts
- set final_master=true
- set locked=true
- tag
- print token/cookie/session/auth/env/signed URL contents

## 15. Git/source preflight

- branch_status: `## main...origin/main`
- sources_status: clean
- tracked_diff_preflight: none
- staged_diff_preflight: none
- known_untracked_noise_present: `.vs/`, `productions/chi_yan_tian_qiong/edits/`, `productions/chi_yan_tian_qiong/review_artifacts/`, `reports/context_recovery/`
- block_status: not blocked

## 16. Files read

- `reports/PHASE_K270B_SHOT04_R02A_STATIC_DYNAMIC_BURST_TWO_SHOT_ROUTE_PLANNING.md`
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
- read-only Source context under `sources/`, including `sources/dreamina_cli_help_latest.md`, Dreamina CLI workflow/source context, and DreaminaBatcher manifest schema context.

## 17. Encoding verification

- visible_authorization_line_may_be_corrupted: true
- base64_decoded_text_used_as_source_of_truth: true
- decoded_text_preserved_readably: true
- decoded_authorization_sha256_match: true
- actual_decoded_utf8_sha256: `5c332d79318a2cd45867c13d7e5097bf62a101a0c358165111a210463d11b999`
- required_dynamic_direction_terms_present: true
- required_no-action_terms_present: true
- forbidden_mojibake_markers_present: false

## 18. Source governance confirmation

- Official Project Source files remain human-controlled.
- Codex read Source context only.
- sources_modified: false
- source_updates_created: false
- source_updates_staged: false
- this_report_is_official_Source: false

## 19. Risk acknowledgement

- K270C does not create the package.
- Future K270D no-submit package creation is still not media generation.
- B3/B1 may still fail visually later.
- Future package creation does not authorize submit.
- Future submit/query/download require separate human authorizations.
- Existing CONTACT_HITSTOP_SHORT is supporting static beat only, not final.
- Dynamic fly-out must still be visually reviewed later.
- Final/lock remains false.

## 20. Safety flags

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
- no_prompt_package_manifest_created_or_modified: true
- no_sources_modified: true
- future_live_action_requires_separate_authorization: true
- final_master: false
- locked: false

## 21. Recommended next phase

- recommended_next_phase: K270D_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_CREATION

K270D should:

- create no-submit package material only.
- likely include B3 primary and B1 secondary variants if feasible.
- include prompt/package/manifest/report.
- not run Dreamina.
- not submit/query/download.
- not create media.
- not final/lock.

## 22. Final verdict

K270C_DYNAMIC_FLYOUT_PACKAGE_AUTHORIZATION_RECORDED_READY_K270D_NO_SUBMIT_PACKAGE_CREATION
