# PHASE K242V - SHOT-04 R02 Near-Wall Guard-Clash Video Route Planning

## 1. Purpose

Create a text-only video route planning report after K241F confirmed that the SHOT-04 R02 near-wall guard-clash prompt-only `text2image` package also failed remotely.

This phase decides how to move from failed still-keyframe routes into a video-first route for the alternate near-wall guard-clash beat.

K241F final verdict:

`SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_FAILURE_REVIEW_READY_K242V_VIDEO_ROUTE_PLANNING`

## 2. Authorization and Boundaries

Authorization level: L0 planning-only video route decision.

This phase did not run:

- Dreamina
- submit
- query
- download
- retry
- resubmit
- batch

This phase did not create:

- media
- frames
- contact sheets
- prompt TXT files
- package JSON files
- manifest CSV files

This phase did not modify:

- shot records
- `sources/`
- runtime code
- `configs/providers.json`
- prompt/package/manifest files

No final or lock state was set.

## 3. Files Inspected

### Latest Text2Image Failure Review

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K241F_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_FAILURE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K241_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K240_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_L3_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K239_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K238T_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_PACKAGE_READY.md`

### Alternate Beat Planning and Route Decision

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K238_SHOT04_R02_ALTERNATE_GUARD_CLASH_ROUTE_DECISION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K237A_SHOT04_R02_ALTERNATE_NEAR_WALL_GUARD_CLASH_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K236_SHOT04_R02_HUMAN_ROUTE_DECISION_PLANNING_AFTER_TRIPLE_FAILURE.md`

### Original Video Evidence

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220A_SHOT04_R02_REVIEW_ARTIFACTS_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K219_SHOT04_R02_DOWNLOAD_READY.md`

### Package Evidence

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-NEAR-WALL-GUARD-CLASH-T2I-001_text2image_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_r02_kf_near_wall_guard_clash_t2i_001_text2image_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_text2image_SHOT-04-R02-KF-NEAR-WALL-GUARD-CLASH-T2I-001_no_submit.csv`

### Sources Read Only

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

All listed Source files were present. No Source file was modified.

## 4. Source Governance Confirmation

`sources/` was checked and was clean.

Codex read Source files as reference material only. No Source file was created, edited, deleted, renamed, moved, staged, committed, or pushed.

Notes in this report are evidence and planning only. They are not official Source.

## 5. K241F Carry-Forward

- `failure_classification=fourth_valid_submit_remote_final_generation_failure_for_SHOT04_R02_keyframe_routes`
- `latest_failure_classification=alternate_near_wall_guard_clash_prompt_only_text2image_remote_final_generation_failure`
- exact wall-contact route failed repeatedly
- alternate near-wall guard-clash `text2image` also failed remotely
- no result image
- no download URL
- no final/lock
- no retry/resubmit authorized
- K242 download impossible because no result exists
- same K238T/K240 `text2image` package should not be retried

## 6. Current State Summary

- SHOT-04 R02 still-keyframe routes are blocked for now.
- `text2image` should not be retried immediately.
- The alternate near-wall guard-clash beat remains the chosen creative direction.
- The next production route should test video motion, not another still keyframe.
- K242V is planning-only and does not run Dreamina.

## 7. Video Route Rationale

The video route is now recommended because:

- K219 proved video generation can produce downloadable media in this account/project environment.
- K220B shows the earlier video failed visually for action quality, not because the remote video task failed.
- Text2image/keyframe routes now show repeated provider-side final-generation failure.
- Video allows motion-first prompting, which better matches guard pressure, skid, rain spray, and counter-readiness.
- The useful output can be designed for a 1.0s-1.5s edit window instead of requiring the full 5s clip to work.
- The revised beat no longer requires exact body-wall contact, reducing the hardest geometry burden from the failed wall-impact route.

## 8. Revised Video Beat

Fenshou drives from center-left into Shuangji's crossed guard inside a rainy ancient temple side corridor. Shuangji is center-right near a dark wooden wall but does not touch it. The primary contact is shoulder-and-forearm pressure into crossed guard. Shuangji skids backward on wet stone, rain sprays from the floor, guard compression is visible, her cloak/hair/armor react to the pressure, then she twists into counter-readiness. The wall remains intact behind her as spatial danger only.

This is a near-wall guard-clash action beat, not a wall-impact beat.

## 9. Hard Removals From Failed Routes

Future video route must continue removing:

- body-wall contact
- wall hit
- wall damage
- wall crack
- splinter
- wall dent
- wall mark
- embedding
- body-wall fusion
- body-to-wall collision

These are not target duties and should not be reintroduced as positive action goals.

## 10. Video Timing Design

Target useful edit window: 1.0s-1.5s, even if the generated clip is 5s.

| Time | Beat |
| --- | --- |
| `0.00s-0.10s` | Already in close range. No long approach. Fenshou is already driving from center-left. |
| `0.10s-0.35s` | Shoulder-and-forearm pressure meets Shuangji's crossed guard. |
| `0.35s-0.65s` | Shuangji skids backward on wet stone, near the wall but not touching it. Rain/floor spray and guard compression are visible. |
| `0.65s-1.00s` | Brief pressure lock / hit-stop. Knees bend, armor and cloak react. |
| `1.00s-1.35s` | Shuangji twists out of the pressure and coils for a counter. |
| `1.35s-1.50s` | Best cut window. Cut mid-exchange before static pose-out. |
| `1.50s onward` | If the source continues, keep motion alive through rain occlusion, guard separation, footwork adjustment, camera shake, or Shuangji counter-initiation. Avoid static tail. |

## 11. Route Options Comparison

| Route | Description | Pros | Cons | Recommendation |
| --- | --- | --- | --- | --- |
| A. Prompt-only `text2video` package | No active image refs; pure motion-first video prompt. | Avoids image2image/text2image ref and keyframe failure modes; simplest video route; tests whether video model can produce the action; lower setup complexity. | Identity drift likely; wall/costume continuity weaker; action may drift or become generic. | Recommended default. |
| B. `multimodal2video` or image-ref-supported video package | Limited identity/environment refs if supported by current CLI contract. | Better identity/environment continuity; may anchor characters and corridor. | Reintroduces reference complexity; prior ref-heavy routes failed in image2image; may increase remote fragility. | Secondary after text2video route planning or if identity becomes top priority. |
| C. Manual layout first, then video | Create manual layout before a video package. | Stronger spatial control. | Slower; may be unnecessary because exact wall contact is removed. | Fallback if prompt-only video cannot preserve geometry. |
| D. Single-character video insert route | Shuangji skid/counter or Fenshou drive insert instead of two-character clash. | Reduces dual-character contact burden. | Loses direct guard-clash proof; changes shot grammar. | Creative fallback if two-character video still fails visually. |

## 12. Route Decision

`route_decision=K243V_TEXT2VIDEO_NEAR_WALL_GUARD_CLASH_NO_SUBMIT_PACKAGE`

Meaning:

- Next phase creates a no-submit `text2video` package.
- No active image refs in the first video attempt.
- Prompt-only video route tests whether video generation can produce the revised action.
- Identity continuity is secondary for this first video probe.
- Action must be front-loaded into the first 1.0s-1.5s.
- No body-wall contact or wall damage language should be used as positive targets.
- No submit should happen until independent package review and human L3 authorization.

## 13. Recommended K243V Package Settings

Recommended only. K242V does not create these files.

- `asset_id=SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001`
- `task_type=text2video`
- `provider=dreamina_cli`
- `model_version=seedance2.0_vip`
- `ratio=16:9`
- `video_resolution=720p`
- `duration=5`
- `poll=0`
- `active_refs_count=0`
- `package_status=package_ready_no_submit`
- `submit_allowed=false`
- `query_allowed=false`
- `download_allowed=false`
- `retry_allowed=false`
- `resubmit_allowed=false`
- `final_master=false`
- `locked=false`
- `human_submit_authorization_required=true`
- `package_review_required=true`

Recorded local help supports `text2video` with `--prompt`, `--duration`, `--ratio`, `--video_resolution`, `--model_version`, and `--poll`. It also records `seedance2.0_vip`, `ratio=16:9`, `duration=4-15`, and `video_resolution=720p` as valid. K243V must still obey the current live/recorded CLI help and should not submit.

## 14. Draft Future Video Prompt Concept

Draft only. Do not treat this as a prompt file.

```text
A cinematic rainy ancient temple side-corridor combat shot. From the first frame, Fenshou, a black-red armored male warrior, is already close in center-left, driving forward with compact shoulder-and-forearm pressure into Shuangji's crossed guard. Shuangji, a silver-blue armored female warrior, braces center-right near a dark wooden wall but does not touch it.

The action starts immediately with no long approach. Fenshou's body line pushes left to right. Shuangji's crossed guard compresses under the pressure; her rear foot skids across the wet stone floor; rain sprays from the floor and guard contact; her cloak, hair, and armor edges snap from the force.

After a brief pressure lock, Shuangji twists out of the pressure and coils into counter-readiness while still near the wall. The wall remains intact behind her as background danger only. Keep motion alive after the main contact with guard separation, footwork adjustment, rain occlusion, and counter-initiation.

No body-wall contact, no wall hit, no wall damage, no wall crack, no splinter, no wall dent, no wall mark, no embedding, no body-wall fusion, no long approach, no static pose-out, no poster pose, no magic blast, no shockwave, no extra characters, no duplicate bodies, no extra limbs, no text, no watermark.
```

## 15. Video Prompt Priority Audit Plan

### P0

- first frame already in close range
- immediate guard clash
- shoulder/forearm pressure into crossed guard
- wet-floor skid
- rain spray
- Shuangji counter-ready twist
- no body-wall contact
- no wall damage
- no static pose-out

### P1

- rainy temple side corridor
- wall as background pressure
- black-red Fenshou / silver-blue Shuangji broad identity
- 16:9 medium / medium-wide angle

### P2

- negatives against poster pose
- negatives against extra limbs and duplicate bodies
- negatives against magic blast and shockwave
- negatives against wall hit/contact/damage

## 16. Risk Register

| Risk | Level | Mitigation |
| --- | --- | --- |
| Video may slow down or pose out | High | Front-load action into first 1.0s-1.5s and require continued motion after cut window. |
| Prompt-only video identity drift | High | Treat first route as motion/geometry probe; identity review required. |
| Guard clash may become hand-push | Medium | Emphasize shoulder-and-forearm pressure and guard compression. |
| Wall may disappear or become actual contact | Medium | Keep wall visible as background danger only; repeat no body-wall contact. |
| Action may become too wide or long approach | Medium | First frame must already be close range. |
| 5s clip may have only 1.0s-1.5s usable material | Medium | Plan for edit extraction, not full-clip usability. |
| Dual-character combat may still fail visually | High | Require human/ChatGPT visual review after download. |
| Video remote failure | Medium | If video also fails remotely, route should move to manual/external or single-character insert. |
| Static tail | Medium | Specify rain occlusion, guard separation, footwork, and counter-initiation after main contact. |

## 17. Source Update Candidate Notes

Do not update Source from this report. Candidate future evidence:

- After repeated `text2image` final-generation failures, video route may be preferable if prior video can produce downloadable media.
- For video prompts, front-load useful action into the first 1.0s-1.5s.
- If generated duration is longer than needed, design for edit extraction rather than expecting the whole clip to be usable.
- Avoid static pose-out tails by specifying continued motion after the cut window.
- Do not assume still keyframe generation is safer than video when still routes repeatedly fail remotely.

## 18. What Not To Do

- Do not run Dreamina in K242V.
- Do not submit/query/download.
- Do not retry/resubmit failed text2image tasks.
- Do not create prompt/package/manifest files in K242V.
- Do not stage media.
- Do not modify `sources/`.
- Do not mark final.
- Do not lock.

## 19. Safety Confirmation

- No Dreamina command was run.
- No submit/query/download/retry/resubmit/batch happened.
- No media was created.
- No prompt/package/manifest/shot record was modified.
- `sources/` remained clean and untouched.
- Runtime code and `configs/providers.json` were not modified.
- No auth/session/token/key/env file was opened, copied, printed, staged, or committed.
- Only this K242V text report is intended for staging.

## 20. Final Verdict

`SHOT04_R02_NEAR_WALL_GUARD_CLASH_VIDEO_ROUTE_PLANNING_READY_K243V_TEXT2VIDEO_PACKAGE`
