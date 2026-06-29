# PHASE K238 - SHOT-04 R02 Alternate Guard-Clash Route Decision

## 1. Purpose

K238 creates a text-only route decision report after K237A designed the revised SHOT-04 R02 alternate near-wall guard-clash beat.

K237A final verdict:

`SHOT04_R02_ALTERNATE_GUARD_CLASH_PLANNING_READY_K238_ROUTE_DECISION`

K237A route:

`Option B = alternate near-wall guard-clash action beat`

K238 decides the best next package/planning route. It does not create package files and does not run Dreamina.

## 2. Authorization and Boundaries

Authorization level: `L0 planning-only route decision`

Allowed:

- Read prior reports and package evidence.
- Read `sources/` as read-only reference material.
- Create one K238 text report.
- Include route comparison, package route recommendation, future prompt direction, and risk register inside this report only.

Forbidden:

- No Dreamina command.
- No submit/query/download.
- No retry/resubmit/batch.
- No media generation.
- No frames/contact sheets.
- No prompt txt creation.
- No package JSON creation.
- No manifest CSV creation.
- No shot-record modification.
- No `sources/` modification.
- No runtime/config modification.
- No final or lock decision.
- No media staging.

## 3. Files Inspected

Latest alternate-beat planning:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K237A_SHOT04_R02_ALTERNATE_NEAR_WALL_GUARD_CLASH_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K236_SHOT04_R02_HUMAN_ROUTE_DECISION_PLANNING_AFTER_TRIPLE_FAILURE.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K235F_SHOT04_R02_TRIPLE_REMOTE_FAILURE_ROUTE_DECISION.md`

Failed wall-contact route evidence:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K235_SHOT04_R02_SOFTENED_TEXT2IMAGE_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K234_SHOT04_R02_SOFTENED_TEXT2IMAGE_L3_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K233_SHOT04_R02_SOFTENED_TEXT2IMAGE_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K232_SHOT04_R02_SOFTENED_TEXT2IMAGE_KEYFRAME_PACKAGE_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K231_SHOT04_R02_POST_IMAGE2IMAGE_FAILURE_ROUTE_RESET_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K230F_SHOT04_R02_REPEATED_IMAGE2IMAGE_FAILURE_REVIEW_AND_ROUTE_RESET.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K230_SHOT04_R02_MICRO_IMPACT_KEYFRAME_3REF_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K229_SHOT04_R02_MICRO_IMPACT_KEYFRAME_3REF_L3_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K226_SHOT04_R02_MICRO_IMPACT_KEYFRAME_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K225_SHOT04_R02_MICRO_IMPACT_KEYFRAME_L3_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220A_SHOT04_R02_REVIEW_ARTIFACTS_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K219_SHOT04_R02_DOWNLOAD_READY.md`

Existing package evidence only:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-SOFT-CONTACT-T2I-001_text2image_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_r02_kf_soft_contact_t2i_001_text2image_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_text2image_SHOT-04-R02-KF-SOFT-CONTACT-T2I-001_no_submit.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-MICRO-IMPACT-001-R02_contact_keyframe_3ref_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_r02_kf_micro_impact_001_r02_3ref_image2image_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-04-R02-KF-MICRO-IMPACT-001-R02_3ref_no_submit.csv`

Sources inspected read-only as needed:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.7.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化宏流程与授权等级_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`

## 4. Source Governance Confirmation

Preflight confirmed `sources/` was clean.

- Source files were read-only reference material.
- No Source file was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- No official Source update was performed.

Source governance remains:

- `source_read_allowed=true`
- `source_recommendation_allowed=true`
- `source_draft_allowed=true`
- `source_write_allowed=false`
- `source_stage_allowed=false`
- `source_commit_allowed=false`
- `official_source_update_requires_human_manual_action=true`

## 5. K237A Carry-Forward

- Human selected Option B.
- Exact body-wall contact route is stopped for now.
- New route: alternate near-wall guard-clash.
- Wall is spatial pressure / background danger, not collision target.
- Main contact is guard-to-forearm/shoulder, not body-to-wall.
- Shuangji skids backward near wall but does not touch it.
- Physical proof comes from crossed guard compression, wet floor skid, rain spray, cloak/hair/armor reaction.
- Useful edit target is `1.0s-1.5s`.
- No final/lock.
- No Dreamina action authorized.

## 6. Current State Confirmation

Current state:

- SHOT-04 R02 exact wall-contact route is stopped for now.
- Human chose alternate near-wall guard-clash.
- K237A created a viable planning blueprint.
- No package exists yet for the alternate beat.
- The next step should choose a package route only, not live submit.

The route decision should preserve the newly removed constraints. The failed body-wall collision requirement must not leak back into future prompts.

## 7. Revised Beat Restatement

Fenshou drives from the left into Shuangji's crossed guard near a rainy wooden corridor wall. Shuangji skids backward on wet stone, shoulder close to but not touching the wall. Rain sprays from floor and guard pressure. The wall frames danger behind her but is not a collision target. Shuangji absorbs the pressure and coils into counter-readiness.

Core intent:

- Keep the rainy side-corridor pressure.
- Keep Fenshou's offensive drive.
- Keep Shuangji's resistance and counter-readiness.
- Shift the main visual proof from wall impact to guard compression and wet-floor skid.

## 8. Removed Constraints From Old Route

Hard removals:

- No exact body-wall contact.
- No wall hit.
- No wall damage.
- No wall crack.
- No splinters.
- No wall dent.
- No embedding.
- No body-wall fusion.
- No wall contact mark.
- No need for body-to-wall collision.

These removed constraints are part of the new route design, not merely negative prompt wording.

## 9. Route Comparison Table

| Route | Description | Pros | Cons | Best use |
| --- | --- | --- | --- | --- |
| A. `K238T` / text2image keyframe package | Prompt-only `text2image` still keyframe for the near-wall guard-clash beat. | Simplest route after removing provider-fragile wall-contact; avoids image2image upload/ref fragility; good geometry probe; fast to package and review; no refs means lower setup complexity. | Identity drift likely; wall/costume continuity weaker; still image may posterize. | First geometry / composition probe for alternate beat. |
| B. `K238V` / video package planning | Plan legal 4-5s video generation with useful action front-loaded into 1.0s-1.5s edit window. | Tests motion directly; avoids still-image posterization; closer to final output goal. | Prior video route had slow reaction and pose-out; without a still/keyframe anchor action may drift; more expensive; harder to debug. | After a keyframe or still concept confirms the new geometry. |
| C. `K238I` / image2image limited-ref keyframe package | Use limited refs for identity and wall continuity. | Better identity and environment continuity. | Image2image repeatedly failed remotely in exact-contact route; reintroduces reference conflict; higher provider fragility. | Only after text2image or manual layout proves beat geometry. |
| D. `K238L` / manual layout support planning | Create or plan a simple layout if even near-wall guard-clash needs geometry support. | Most control over character positions and force line. | Adds manual/tool cost; may be unnecessary now that body-wall contact is removed. | Fallback if text2image geometry probe fails or user wants stronger control. |

## 10. Route Decision

`route_decision=K238T_TEXT2IMAGE_NEAR_WALL_GUARD_CLASH_KEYFRAME_PACKAGE_NO_SUBMIT`

Meaning:

- Build a no-submit `text2image` package next.
- It is a still keyframe geometry probe for the alternate beat.
- Do not use active refs in this first package.
- Identity continuity is secondary.
- Focus on crossed guard, near-wall pressure, wet floor skid, rain spray, and counter-readiness.
- Use no body-wall contact language.
- Use no wall damage language.
- Do not run Dreamina until a later human authorization and independent package review.

Rationale:

- The exact wall-contact constraint has been removed, so the prompt-only route is no longer repeating the failed body-wall target.
- `text2image` is the fastest way to test whether the simpler near-wall guard-clash composition reads.
- Avoiding active refs prevents the known image2image/reference-upload fragility from re-entering too early.
- If the keyframe geometry works, later phases can decide whether identity support, video generation, or manual layout is needed.

## 11. Recommended K238T

Recommended next phase:

`K238T = SHOT-04 R02 near-wall guard-clash text2image keyframe no-submit package`

K238T should create:

- prompt txt
- package JSON
- manifest CSV
- package report

Suggested asset ID:

`SHOT-04-R02-KF-NEAR-WALL-GUARD-CLASH-T2I-001`

Suggested task type:

`text2image`

Suggested settings:

| Field | Value |
| --- | --- |
| `model_version` | `5.0` |
| `ratio` | `16:9` |
| `resolution_type` | `2k` |
| `poll` | `0` |
| active refs | none |
| package status | no-submit |
| submit/query/download | false |
| final_master | false |
| locked | false |

K238T must not:

- Run Dreamina.
- Submit/query/download.
- Retry/resubmit.
- Mark final/locked.
- Stage media.

## 12. Draft Future Prompt Concept

This is a planning concept only, not a prompt file.

> One cinematic action keyframe in a rainy ancient temple side corridor: Fenshou, a black-red armored male warrior, drives from center-left toward Shuangji with compact shoulder-and-forearm pressure. Shuangji, a silver-blue armored female warrior, braces in center-right near a dark wooden corridor wall, close to the wall but not touching it. Their crossed guard is compressed at the center of the frame; Shuangji's rear foot skids across the wet stone floor, rain sprays from the floor and guard contact, her cloak, hair, and armor edges react to the pressure, and she twists into counter-readiness. The wall stays intact as background danger only. No wall hit, no wall damage, no wall crack, no splinter, no wall dent, no body-wall contact, no embedding, no magic blast, no shockwave, no poster pose.

Prompt strategy:

- Action geometry first.
- Identity descriptors broad and secondary.
- Wall remains near/background, not active collision.
- Main contact is crossed guard / forearm / shoulder pressure.
- Visible physical proof: skid, rain spray, compression, cloth/hair/armor reaction.

## 13. Risk Register

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| Text2image identity drift | high | Treat output as geometry probe; later identity-support route can be planned if geometry works. |
| Guard clash becomes hand-push | medium | Emphasize compact shoulder-and-forearm body drive, not palm push. |
| Action becomes static pose | medium | Use result-first action keyframe, compressed guard, wet-floor skid, counter-readiness. |
| Wall disappears or loses pressure | medium | Keep wall behind/right of Shuangji as visible background danger. |
| Shuangji accidentally touches wall | medium | Explicitly state near wall but not touching; no body-wall contact. |
| Too much caution weakens action | medium | Preserve guard compression, rain spray, skid, and body drive. |
| Rain/floor skid not visible | medium | Make wet stone skid path and spray part of the primary visual result. |
| Future video may still pose-out | medium | Later video route must front-load useful action into 1.0s-1.5s edit window. |
| Package route may need later image/video refinement | high | K238T is only the first geometry probe, not a final solution. |

## 14. Source Update Candidate Notes

Do not modify Source in K238. The following are evidence notes only for future ChatGPT/human Source update:

- After abandoning exact wall-contact, the first alternate-beat probe should be a simpler geometry package before video.
- For provider-fragile exact contact, a near-wall guard-clash can preserve drama while removing the failed collision requirement.
- Explicitly listing removed constraints helps prevent old failure terms from leaking into new prompts.
- If the first simplified alternate-beat probe succeeds, later phases can reintroduce identity/environment support gradually.

## 15. What Not To Do

- Do not run Dreamina from K238.
- Do not submit/query/download.
- Do not create prompt/package/manifest files in K238.
- Do not reintroduce body-wall contact language.
- Do not use wall damage language.
- Do not stage media.
- Do not update Source.
- Do not mark final.
- Do not lock.

## 16. Safety Confirmation

- No Dreamina command was run.
- No submit/query/download/retry/resubmit/batch occurred.
- No media was created.
- No frames/contact sheets were created.
- No prompt/package/manifest/shot-record/runtime/config/Source file was modified.
- No media was staged.
- No auth/session/token/key/env file was opened, printed, staged, or committed.
- `final_master=false`
- `locked=false`

## 17. Final Verdict

`SHOT04_R02_ALTERNATE_GUARD_CLASH_ROUTE_DECISION_READY_K238T_TEXT2IMAGE_PACKAGE`
