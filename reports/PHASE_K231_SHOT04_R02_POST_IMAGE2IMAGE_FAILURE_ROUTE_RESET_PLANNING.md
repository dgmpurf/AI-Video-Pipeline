# PHASE K231 - SHOT-04 R02 Post-Image2Image-Failure Route Reset Planning

## 1. Purpose

K231 creates a text-only route reset planning report after K230F confirmed repeated remote final-generation failure for the SHOT-04 R02 micro-impact keyframe `image2image` route.

K230F final verdict:

`SHOT04_R02_REPEATED_IMAGE2IMAGE_FAILURE_REVIEW_READY_K231_ROUTE_RESET_PLANNING`

K230F route decision:

`K231_ROUTE_RESET_COMPARE_SOFTENED_IMAGE2IMAGE_VS_TEXT2IMAGE_NO_SUBMIT`

This report compares:

1. softened-contact `image2image`
2. prompt-only `text2image`
3. manual layout / rough compositional sketch route

K231 decides which no-submit package or planning phase should come next.

## 2. Authorization and Boundaries

Authorization level: `L0/L2 planning-only route reset`

Allowed:

- Read prior reports and package evidence.
- Read existing prompts, JSON packages, and manifests as evidence only.
- Read `sources/` as read-only reference material.
- Create one K231 text report.
- Include draft prompts inside this report only.
- Stage/commit/push only this K231 text report.

Forbidden and not performed:

- Dreamina submit/query/download/retry/resubmit/batch
- media generation
- frames/contact sheets
- prompt txt creation
- package JSON creation
- manifest CSV creation
- shot-record modification
- `sources/` modification
- runtime code modification
- `configs/providers.json` modification
- final / lock
- media staging
- auth/session/token/key/env access

## 3. Files Inspected

Latest repeated failure / route reset:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K230F_SHOT04_R02_REPEATED_IMAGE2IMAGE_FAILURE_REVIEW_AND_ROUTE_RESET.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K230_SHOT04_R02_MICRO_IMPACT_KEYFRAME_3REF_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K229_SHOT04_R02_MICRO_IMPACT_KEYFRAME_3REF_L3_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K228_SHOT04_R02_MICRO_IMPACT_KEYFRAME_3REF_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K227R_SHOT04_R02_MICRO_IMPACT_KEYFRAME_3REF_PACKAGE_READY.md`

Prior 4-ref `image2image` failure:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K226F_SHOT04_R02_MICRO_IMPACT_KEYFRAME_FAILURE_REVIEW_AND_ROUTE_DECISION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K226_SHOT04_R02_MICRO_IMPACT_KEYFRAME_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K225_SHOT04_R02_MICRO_IMPACT_KEYFRAME_L3_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K224_SHOT04_R02_MICRO_IMPACT_KEYFRAME_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K223_SHOT04_R02_MICRO_IMPACT_KEYFRAME_L2_PACKAGE_READY.md`

Route / visual failure background:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K222_SHOT04_R02_MICRO_IMPACT_KEYFRAME_BLUEPRINT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K221_SHOT04_R02_ROUTE_DECISION_AFTER_VISUAL_FAILURE.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220A_SHOT04_R02_REVIEW_ARTIFACTS_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K219_SHOT04_R02_DOWNLOAD_READY.md`

Existing package evidence only:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-MICRO-IMPACT-001_contact_keyframe_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_r02_kf_micro_impact_001_image2image_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-04-R02-KF-MICRO-IMPACT-001_no_submit.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-MICRO-IMPACT-001-R02_contact_keyframe_3ref_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_r02_kf_micro_impact_001_r02_3ref_image2image_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-04-R02-KF-MICRO-IMPACT-001-R02_3ref_no_submit.csv`

Sources inspected read-only:

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

Optional Source file listed by K231 but missing locally:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`

This is non-blocking for K231. No Source file was created, repaired, copied, modified, staged, or committed.

## 4. Source Governance Confirmation

`sources/` was checked before report creation and remained clean.

Source governance remains in force:

- Codex may read `sources/` as read-only reference material.
- Codex may create route planning and audit reports under `reports/`.
- Codex must not create, edit, delete, rename, move, stage, commit, or push files under `sources/`.
- Official Source updates require ChatGPT/human review and human manual application.

K231 did not modify or stage `sources/`.

## 5. K230F Carry-Forward

- `failure_classification=repeated_remote_generation_failure_after_valid_image2image_submits`
- K219 video failed visual review for the core SHOT-04 R02 wall-impact route.
- K225/K226 4-ref `image2image` valid submit failed remotely.
- K229/K230 3-ref `image2image` valid submit failed remotely.
- No usable keyframe output exists.
- No output image exists from either submit_id.
- No download URL exists from either submit_id.
- No download phase is available.
- No final/lock exists.
- No retry/resubmit is authorized.
- Reference-count simplification alone is insufficient.
- Prompt safety/quality softness may matter as much as prompt specificity.
- Current stage is route reset, not more submit.

## 6. Why This Is a Route Reset

This is a route reset because the same high-level method has now failed after two valid submits:

- first with a 4-ref package
- then with a simplified 3-ref R02 package

The evidence rejects the simplest explanations:

- not a package parse failure
- not a missing ref failure
- not a login/auth failure
- not a CLI logger failure
- not a query/download misuse
- not only reference count

Same-package retry is rejected because it repeats a valid-submit remote failure with no structural mitigation.

More blind ref stripping is rejected because reference-count simplification already failed once and further stripping increases identity/action drift without directly addressing content brittleness.

A model-version-only change is not primary because it does not address the suspected content/safety/close-contact failure mode.

The next attempt must reduce failure risk by changing the content language or generation route, not only by changing ref count.

The exact-damage wording may be too brittle for Dreamina `image2image`; therefore the next viable test should soften contact language and/or test geometry through prompt-only `text2image`.

## 7. Route Matrix

| Route | Remote failure risk | Body-wall contact control | Identity stability | Anatomy risk | Complexity | Review burden | Cost/time risk | Governance fit | Recommendation |
|---|---|---|---|---|---|---|---|---|---|
| A. Softened-contact `image2image`, 3 refs | medium-high | medium | high | high | medium | high | medium | good if no-submit package reviewed | secondary |
| B. Softened-contact `image2image`, 2 refs | medium | medium-low | medium-low for Fenshou | high | medium-low | high | medium | good if no-submit package reviewed | fallback |
| C. Prompt-only `text2image` softened contact keyframe | medium | medium | lower than ref routes | medium-high | low | medium-high | low-medium | strong as no-submit route reset | primary |
| D. Manual layout / rough compositional sketch route | lower after layout exists | high | depends on later refs/text | medium | higher setup | high | medium-high | requires separate media/layout authorization | strong support route |
| E. Model-version-only `image2image` variant | medium-high | same as prior route | same as prior route | high | low | high | medium | requires new no-submit package/review | not primary |
| F. Stop exact wall-impact route | none | none | none | none | low | low | low | governance-safe | human fallback |

Route A notes:

- Keeps wall ref, Fenshou identity, and Shuangji identity anchor.
- Uses softened wording: guarded wall contact, compressed crossed guard, rain splash, shallow wet pressure mark, wall remains intact.
- Avoids crack, splinter, break, hard hit, violent, and damage-heavy language.
- Still carries `image2image` and close-contact body-wall risk.

Route B notes:

- Uses wall ref plus Shuangji identity anchor only.
- Describes Fenshou in text.
- Reduces refs but increases Fenshou drift and may not improve body-wall blocking enough.

Route C notes:

- Uses no image refs.
- Tests whether the model can render softened body-wall contact geometry without image upload/reference-duty conflict.
- Identity stability is weaker, but K231 treats this as action-geometry viability, not final/lock material.

Route D notes:

- A layout sketch could anchor wall plane, body positions, contact point, and force direction better than prose.
- K231 does not create media. This route requires a separate human/tool authorization later.

Route E notes:

- A different model might help, but this is not structural enough after two content-similar remote failures.

Route F notes:

- Reserved for a future human decision if exact body-wall contact proves too costly or provider-fragile.

## 8. Softened-Contact Image2Image Prompt Draft

Draft only. No prompt txt file was created.

```text
Create one cinematic still keyframe of guarded wall contact in a rainy ancient temple side corridor. Fenshou presses from the left-midground into Shuangji's crossed guard with a compact shoulder-and-forearm drive. Shuangji is in the right-midground, knees bent, crossed guard compressed inward, upper back and shoulder resting firmly against the rain-soaked wooden wall panel. The wall remains intact.

Keep the exact contact zone readable between their bodies: Fenshou's shoulder line and forearm pressure, Shuangji's crossed guard, and her shoulder-back touching the wet panel. At that contact zone, show rainwater flicking outward, a shallow wet pressure mark on the wood, and small droplets sliding along the force direction. No broken wood, no hole, no falling debris.

Use the wall reference only for rainy side-corridor architecture, wet dark wooden panels, pillars, wet stone floor, and cold blue rain light. Use Fenshou's reference only for black-red armor and male warrior identity. Use Shuangji's identity anchor for her face, upper-body identity, silver-blue costume language, and female-coded silhouette.

Camera: medium-wide 16:9, three-quarter front-left, eye-level or slightly low. Action clarity comes before portrait beauty. No body-wall fusion, no embedding, no wall collapse, no energy blast, no shockwave, no wrestling hold, no pose-out, no duplicate bodies, no extra limbs, no text, no watermark.
```

Draft A summary:

- Future route: softened-contact `image2image`
- Reference count: likely 3 refs if selected
- Avoids hard-damage wording
- Preserves wall-contact objective
- Still high risk because `image2image` close-contact remains brittle

## 9. Prompt-Only Text2Image Softened Contact Prompt Draft

Draft only. No prompt txt file was created.

```text
One cinematic still keyframe in a rainy ancient temple side corridor: Fenshou, a black-red armored male warrior, drives from the left-midground into Shuangji's crossed guard with a compact shoulder-and-forearm press. Shuangji, a silver-blue armored female warrior, is in the right-midground with knees bent, crossed guard compressed inward, her upper back and right shoulder pressed against a rain-soaked wooden wall panel. The wall remains intact.

The action geometry must be clear: Fenshou's forward shoulder line, his forearm pressure, Shuangji's crossed guard absorbing the force, her rear foot skidding on the wet stone floor, and the exact wall contact zone visible behind her shoulder-back. At the contact zone, show rain splash, a shallow wet pressure mark on the wood, and droplets moving along the force direction.

Environment: wet dark wooden side-wall panels, temple pillars, cold gray-blue rain light, reflective stone floor, semi-realistic 3D wuxia film style. Camera: 16:9 medium-wide, three-quarter front-left angle, eye-level or slightly low.

This is an action keyframe, not a poster layout or character sheet. No wall collapse, no broken opening, no magic blast, no shockwave, no body-wall fusion, no embedding, no gore, no severe injury, no extra characters, no duplicate bodies, no extra limbs, no text, no watermark.
```

Draft B summary:

- Future route: prompt-only `text2image`
- No reference-duty prose
- Tests action-geometry viability first
- Identity continuity is weaker and must be treated as secondary in this route reset probe

## 10. Manual Layout Route Blueprint

No image or media was created in K231.

A future manual layout / rough compositional sketch would need:

- 16:9 canvas
- wall plane on the right side of frame
- Shuangji's shoulder-back / upper back touching the wall
- Fenshou on the left driving diagonally into Shuangji's crossed guard
- visible crossed guard block between the bodies
- foot skid direction on the wet floor
- force arrow from Fenshou into Shuangji and wall plane
- labeled contact zone behind Shuangji's shoulder-back
- labeled wall zone, floor zone, character silhouettes
- no detail/identity requirement in the layout itself
- no final art polish requirement

If later authorized, this layout could become a geometry reference for a revised package. It would not be a final frame or locked asset by itself.

## 11. Route Decision

`route_decision=K232_SOFTENED_TEXT2IMAGE_PROMPT_ONLY_CONTACT_KEYFRAME_PACKAGE_NO_SUBMIT`

Reason:

- Repeated `image2image` final-generation failures suggest the current image-ref route is provider-fragile for this exact contact.
- `text2image` is the cleanest viability test for whether the model can produce softened body-wall contact geometry at all.
- Removing image refs avoids image-upload/reference-duty attention conflict.
- Identity stability may be weaker, but K232 should be an action-geometry viability probe, not final asset lock.
- If `text2image` produces viable geometry, the output can later become a positive layout/reference candidate after human visual review.

Secondary route:

`K232B_SOFTENED_2REF_OR_3REF_IMAGE2IMAGE_PACKAGE_NO_SUBMIT`

Support route:

`K232L_MANUAL_LAYOUT_BLUEPRINT_OR_LAYOUT_ASSET_PLANNING`

## 12. Recommended K232

Recommended next phase:

`K232 = SHOT-04 R02 softened text2image prompt-only contact keyframe L2 no-submit package`

K232 should create:

- prompt txt
- package JSON
- manifest CSV
- report

Suggested task type:

`text2image`

Suggested model:

Use the current local Dreamina CLI help as source of truth in K232. Do not assume `image2image` model/resolution options apply to `text2image` without checking current local help.

K232 must not:

- run Dreamina
- submit
- query
- download
- final
- lock

## 13. Source Update Candidate Notes

Do not modify Source in K231. Preserve these notes as future Source evidence:

- Repeated `image2image` remote final-generation failures after valid submits should trigger route reset.
- For body-wall close-contact, soft contact language can be safer than exact damage language.
- `text2image` prompt-only can be used as an action-geometry viability probe after `image2image` failures.
- Identity continuity should be treated as secondary during a route-reset geometry probe.
- Do not assume `image2image` `1k` exists; local CLI help remains execution authority.
- Reference-count simplification alone is insufficient when both 4-ref and 3-ref valid submits fail remotely.

## 14. What Not To Do

- Do not retry K229/K230.
- Do not resubmit the same 3-ref R02 package.
- Do not submit a model-version-only variant without a new no-submit package and review.
- Do not continue ref stripping as the only mitigation.
- Do not create prompt/package/manifest files in K231.
- Do not create media or layout sketches in K231.
- Do not run Dreamina.
- Do not submit/query/download.
- Do not mark final.
- Do not lock.
- Do not modify Source.
- Do not stage media.

## 15. Safety Confirmation

- No Dreamina command was run.
- No submit/query/download/retry/resubmit/batch was run.
- No media was created.
- No frames/contact sheets were created.
- No prompt txt file was created.
- No package JSON file was created.
- No manifest CSV file was created.
- No shot record was modified.
- No runtime code was modified.
- `configs/providers.json` was not modified.
- `sources/` was read-only and not modified/staged.
- Auth/session/token/key/env files were not opened, copied, printed, staged, or committed.
- `final_master=false`.
- `locked=false`.

## 16. Final Verdict

`SHOT04_R02_ROUTE_RESET_PLANNING_READY_K232_SOFTENED_TEXT2IMAGE_PACKAGE`
