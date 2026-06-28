# PHASE K183 - SHOT-04 Route A Composition Matrix and Prompt Blueprint

## 1. Purpose

Develop SHOT-04 Route A into a Composition Matrix and prompt blueprint without generating media.

Route A is the human-selected SHOT-04 architecture / terrain interaction direction: railing / wooden lattice impact and rebound. This report turns that route into planning material for later human + ChatGPT review, not into a live Dreamina package.

## 2. Authorization Level

| field | value |
|---|---|
| authorization_level | `L0/L2 planning-only macro-run` |
| run_dreamina | false |
| submit | false |
| query | false |
| download | false |
| retry | false |
| resubmit | false |
| create_media | false |
| create_frames | false |
| create_contact_sheets | false |
| create_cut_mp4 | false |
| create_package_json | false |
| create_manifest_csv | false |
| create_or_modify_prompt_txt | false |
| create_or_modify_shot_record_json | false |
| final_master | false |
| locked | false |

No Dreamina, no submit/query/download, no media generation, no package/manifest/prompt txt, and no final/lock decision are authorized in K183.

## 3. Files Inspected

Source files, read-only:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化宏流程与授权等级_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

Project reports:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K182_SHOT04_ARCHITECTURE_TERRAIN_INTERACTION_CONCEPT_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K181_SHOT03_K180_CONTINUOUS_RECUT_REVIEW_SELECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K176_SHOT03_SPLIT02_ROUTE_DECISION_AFTER_R01_R02.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K175_SHOT03_SPLIT02_POSE_KF_R02_VISUAL_REVIEW_FAILED_BLOCKING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md`

## 4. Source Governance Confirmation

The Source files were read only.

- No `sources/` file was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Codex / automation may create Source update recommendations inside reports only.
- Official Source update requires ChatGPT generation/review and human manual action.
- K183 is a planning report and prompt blueprint, not official Source.

## 5. SHOT-03 Carry-Forward

| field | value |
|---|---|
| SHOT03_current_preferred_edit_candidate | `K180 Candidate B` |
| candidate_B_path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/shot03_v004_continuous_recut/K179_180/SHOT-03_K180_V004_CONTINUOUS_0p60_3p10_tighter_preview.mp4` |
| SHOT03_final_master | false |
| SHOT03_locked | false |
| SPLIT02_image2image_repair_loop | `paused` |
| R01_approved_keyframe | false |
| R02_approved_keyframe | false |
| SHOT04_goal | `architecture_terrain_interaction` |

K180 Candidate B remains the current preferred SHOT-03 edit candidate. It is not final and not locked. SHOT-04 now owns the architecture / terrain interaction goal.

## 6. SHOT-04 Route A Premise

Route A uses one main interaction: railing / wooden lattice impact and rebound.

One main space zone: exterior corridor / side corridor railing-lattice zone.

Core action:

1. Fenshou pressures Shuangji into the railing or wooden lattice through direct body / guard contact.
2. The railing or lattice reacts only at the exact shoulder-back / guard contact point.
3. A small crack, flex, water burst, or splinter response occurs only after contact.
4. Shuangji rebounds from that contact and immediately counters.
5. The final frame cuts mid-exchange, while both fighters are still in attack / defense / rebound motion.

## 7. Composition Matrix

Canvas ratio recommendation: `16:9`.

Camera position: exterior side corridor, slight front three-quarter angle down the railing line. Camera is at human chest height or slightly low, not overhead, not extreme close-up, and not a flat side-scroller profile.

Shot size: medium-wide combat framing. Both full upper bodies and foot contact points remain readable. Faces remain visible enough for identity, but the shot prioritizes body pressure, railing contact, and rebound.

### Screen-Percent Matrix

| element | type | bbox_percent | layer | anchor_points | orientation | motion_path |
|---|---|---|---|---|---|---|
| Fenshou | character | `[18, 24, 48, 94]` | midground left-center | rear boot `[22, 92]`, lead shoulder `[42, 45]`, right forearm `[43, 50]` | black-red male fighter, left-to-right pressure line, torso angled toward Shuangji | drives from left-center toward right-center, shoulder and forearm compress Shuangji's guard into railing |
| Shuangji | character | `[46, 22, 72, 94]` | midground right-center | shoulder-back contact `[66, 47]`, left guard `[49, 50]`, rear foot skid `[68, 91]` | blue-white/silver female fighter, guarded side angle, face 3/4 visible | receives pressure into railing, compresses, rebounds leftward/forward into counter |
| railing / wooden lattice | architecture | `[66, 38, 96, 78]` | midground right to background | contact point `[68, 48]`, railing top line `[66, 43]`, lattice bars `[74, 46]` | diagonal corridor line receding to background | stays fixed except localized flex/crack/splinter at Shuangji shoulder-back / guard contact point |
| corridor floor | environment | `[0, 72, 100, 100]` | foreground to midground | foot skid zone `[58, 90]`, water splash zone `[63, 88]` | wet stone corridor floor | water splashes and skid streaks follow foot pressure; no floor collapse |
| corridor posts / side wall | architecture | `[68, 8, 100, 82]` | midground to background | stable verticals `[75, 12]`, `[88, 18]` | rainy temple corridor structure | stable world anchor; no unrelated column breakage |
| temple background / rain | environment | `[0, 0, 100, 74]` | background | roofline `[50, 15]`, rain veil `[50, 40]` | cool gray-blue rainy temple atmosphere | rain responds locally near impact; background remains stable |

### Foreground / Midground / Background

- Foreground: wet stone floor, small rain splashes, no dominant foreground object hiding faces.
- Midground: Fenshou, Shuangji, railing/lattice contact point. This is the primary action layer.
- Background: corridor depth, temple architecture, rain curtain, stable roof / wall / posts.

### Locked Elements

- Only two fighters: Fenshou and Shuangji.
- Fenshou remains black-red male fighter identity.
- Shuangji remains female-coded blue-white / silver identity.
- Exterior corridor / side corridor railing-lattice zone remains the only active space zone.
- Railing / lattice damage is localized to one contact point.
- Rainy temple atmosphere and wet stone floor remain consistent.

### Forbidden Elements

- Third person, duplicate character, body fusion, extra limbs.
- Fenshou / Shuangji identity swap.
- Shuangji masculinization.
- Random background breakage.
- Crack before contact.
- Entire building collapse.
- Unrelated column breakage.
- Full wall-run, roof route, large jump, floating.
- Static pushing / wrestling pose.
- Portrait / beauty-pose framing.
- Long face occlusion behind railing, lattice, rain, dust, or splinters.

## 8. Natural Language Translation of Composition Matrix

Frame the shot in a rainy exterior side corridor of the ancient temple. Keep a medium-wide combat view at a slight front three-quarter angle along the railing line, so both fighters, their feet on the wet stone, and the railing/lattice contact point are readable.

Fenshou stays on the left-center midground as the black-red male fighter. His rear boot drives against the wet stone floor while his lead shoulder and forearm press diagonally toward Shuangji. Shuangji stays on the right-center midground as the blue-white / silver female fighter. Her guard catches Fenshou's pressure, her shoulder-back and forearm are forced into the nearby wooden railing or lattice, and her rear foot skids briefly on the wet stone.

The railing/lattice is a fixed corridor structure on the right side of the frame. It must not break by itself. It only flexes or cracks at the exact moment Shuangji's shoulder-back or guard makes contact. Two or three small splinters, rain droplets, and a short water burst move outward in the same force direction. Shuangji rebounds from that railing contact and immediately counters, while Fenshou recoils and re-enters guard. The clip ends while the exchange is still active.

## 9. Reference-Duty Plan

Likely reference classes for a later package:

| reference class | duty | must not do |
|---|---|---|
| Fenshou identity ref | Identity only: black-red male fighter face, hair, armor, silhouette, costume language. | Not blocking, not scene layout, not action timing. |
| Shuangji identity ref | Identity only: female-coded blue-white / silver face, hair, silhouette, costume language. Highest identity protection priority. | Not blocking, not scene layout, not action timing. |
| scene / corridor ref | World and architecture only: rainy temple corridor, railing/lattice, wet stone floor, depth, lighting. | Not character identity, not exact action pose. |
| optional action / blocking reference | Body pressure / shoulder-check / guard compression only. | Not identity, not costume, not scene. |
| optional railing / lattice contact point ref | Architecture contact detail only: where body/guard hits railing, localized flex/crack/splinter direction. | Not identity, not broad destruction, not unrelated structure damage. |

R01/R02 restrictions:

- Do not use R01 or R02 as approved keyframes.
- Do not use failed R01 Shuangji identity as an identity reference.
- R01/R02 may be mentioned as failure evidence only.
- R01/R02 must not become generation references unless explicitly approved later by the human.

## 10. Prompt Blueprint

This is a blueprint only, not a prompt txt file.

### Reference Duties

- Fenshou identity reference: identity only.
- Shuangji identity reference: identity only, highest priority for female-coded blue-white / silver identity.
- Corridor / scene reference: world, architecture, rain, wet stone, railing/lattice only.
- Optional action/blocking reference: shoulder-check pressure and guard compression only.
- Optional railing/lattice reference: localized contact feedback only.

### First-Frame State

From the first frame, both fighters are already in close corridor combat. Fenshou is left-center, pressing forward. Shuangji is right-center, guarding near the railing/lattice. The railing/lattice already exists at frame start as a stable architecture element, but it is not cracked yet.

### Time Schedule 0.00s-5.00s

| time | blueprint action |
|---|---|
| `0.00s-0.30s` | First contact. Fenshou's shoulder / forearm pressure hits Shuangji's guard. Shuangji's torso and rear foot react immediately. |
| `0.30s-1.10s` | Second beat. Shuangji redirects part of the pressure; Fenshou re-enters with short shoulder pressure. No slow display. |
| `1.10s-2.10s` | Third beat. Fenshou compresses Shuangji's guard toward the railing. Railing still does not crack until shoulder-back / guard contact happens. |
| `2.10s-3.20s` | Architecture beat. Shuangji shoulder-back / guard contacts the railing/lattice. Only the contact point flexes/cracks; rain droplets and tiny splinters move along the force direction. |
| `3.20s-4.30s` | Rebound beat. Shuangji rebounds off the railing and counters into Fenshou's guard / shoulder line. Fenshou recoils but stays engaged. |
| `4.30s-5.00s` | Re-entry beat. Both fighters continue attack / defense / rebound motion. End mid-exchange, no pose-out, no idle tail. |

### Contact-Beat Schedule

1. Fenshou shoulder / forearm collides with Shuangji guard.
2. Shuangji redirects, Fenshou re-enters.
3. Fenshou compresses guard toward railing.
4. Shuangji shoulder-back / guard impacts railing/lattice; localized architecture feedback appears after contact.
5. Shuangji rebounds and counters.
6. Fenshou recoils, re-guards, and re-enters as the clip cuts.

### Architecture Damage Causality

- The railing/lattice crack/flex/splinter appears only after Shuangji shoulder-back or guard contact.
- No crack before contact.
- No random background breakage.
- No unrelated column breakage.
- No overdestruction.
- No entire building collapse.
- Water, rain droplets, and splinters follow the physical force direction.

### Identity Protection

- Fenshou remains one black-red male fighter.
- Shuangji remains one female-coded blue-white / silver fighter.
- No role swap.
- No duplicate fighters.
- No body fusion.
- No extra limbs.
- Faces should remain readable in 3/4 side angle when possible.
- Do not hide Shuangji's face for too long behind railing, lattice, rain, smoke, splinters, arms, or hair.

### Camera / Framing

- Medium-wide corridor combat shot.
- Slight front three-quarter angle along the railing line.
- Camera may use small handheld pressure or short tracking movement.
- No extreme close-up.
- No overhead.
- No flat horizontal game-like side view.
- Do not drift into beauty portrait framing.

### Ending Rule

The final frame must cut mid-exchange. Both fighters should still be moving through guard, rebound, or counter pressure. Do not settle into a clean pose, stare-down, poster frame, or idle tail.

### Negative Constraints

No Dreamina execution in K183. For a later prompt, avoid: full wall-run, roof route, floating, big jump, random architecture destruction, crack before contact, entire building collapse, unrelated column breakage, static pushing pose, wrestling hold, beauty pose, role swap, duplicate characters, extra limbs, body fusion, Shuangji masculinization, long face occlusion, text, watermark.

## 11. Timing / Contact-Beat Schedule Requirements

- First contact by `0.15s-0.30s`.
- At least five contact / reaction / re-entry beats across a 4-5 second later generation.
- Prefer six beats if the later prompt remains 5 seconds.
- No idle tail.
- No pose-out.
- Final frame remains in attack / defense / rebound motion.

## 12. Architecture Causality Rules

- Lattice / railing crack, flex, water burst, or splinter appears only after Shuangji shoulder-back or guard contact.
- No random background breakage.
- No crack before contact.
- No overdestruction.
- No entire building collapse.
- No unrelated column breakage.
- Water, rain, and splinters follow the force direction from left-center pressure toward the right-side railing/lattice.
- If the causality cannot be made clear in the later package, reduce structural damage to flex + water burst only.

## 13. Identity and Blocking Risk Controls

- Identity and blocking are separate constraints.
- Identity references protect face, hair, costume, silhouette, and color language only.
- Blocking references protect body pressure, contact point, foot placement, and force direction only.
- Avoid static pushing / wrestling pose.
- Avoid portrait / beauty pose.
- Avoid Fenshou / Shuangji identity swap.
- Avoid extra limbs or body fusion.
- Avoid Shuangji masculinization.
- Avoid hiding faces too long behind railing, lattice, rain, arms, splinters, dust, smoke, or hair.
- Keep Shuangji female-coded blue-white / silver identity.
- Keep Fenshou black-red male fighter identity.
- Keep foot placement readable: Fenshou drives from left-center; Shuangji skids / rebounds near right-center railing.

## 14. Clause-Level Source Compliance Draft

| source_rule | required_behavior | prompt_blueprint_clause | status | risk_if_missing |
|---|---|---|---|---|
| V1.11 early contact | First clear contact within `0.15s-0.30s`. | Time schedule starts with Fenshou shoulder / forearm hitting Shuangji guard at `0.00s-0.30s`. | present | Model may spend opening on setup or corridor display. |
| V1.11 contact-beat schedule | 5-second combat should include 5-6 contact beats with contact point, reaction, rebound, re-entry. | Contact-beat schedule lists six beats from initial guard collision through final re-entry. | present | Fight may become soft movement or sparse blocking. |
| V1.11 damage causality | Architecture feedback must be caused by specific body/object contact and appear after contact. | Architecture beat specifies Shuangji shoulder-back / guard contacts railing before localized crack/flex/splinter. | present | Random breakage, decorative damage, or cracks before impact. |
| V1.11 no idle tail / cut mid-exchange | Final `0.8s` continues attack/defense and cuts in motion. | Ending rule and `4.30s-5.00s` schedule require active re-entry and no pose-out. | present | Clip may end as poster pose or stare-down. |
| V1.2 fight physics / force reaction | Impact must show body consequence: shoulder, forearm, torso, foot skid, rebound. | Matrix and timing specify guard compression, torso reaction, foot skid, rebound, counter. | present | Contact may look weightless or like static pushing. |
| V1.9 blocking / foot placement / scene zone | Use clear foot placement, frame zones, and avoid ambiguous character position. | Screen-percent matrix defines Fenshou left-center, Shuangji right-center, railing contact point, wet floor skid zone. | present | Characters may drift, swap sides, or lose readable blocking. |
| V1.8 reference duties | Each reference must have one duty and must not mix identity, scene, action, and blocking. | Reference-duty plan separates identity refs, scene ref, action/blocking ref, and contact-point ref. | present | Identity drift or reference pollution may recur. |
| Seedance V0.3 Composition Matrix | Use bbox/layer/orientation as planning tool, then translate to natural language. | K183 includes screen-percent matrix and separate natural language translation. | present | Prompt may rely on raw bbox text that models do not follow naturally. |
| Macro governance no final/lock/source write | Planning cannot imply final, lock, Source modification, or live execution. | Authorization, Source governance, safety, and What Not To Do sections keep all false. | present | Planning report could be mistaken for package approval or Source update. |

## 15. Recommended K184

K184 should be human / ChatGPT review of this K183 blueprint.

No Dreamina yet.

K184 may decide whether to:

1. revise the blueprint;
2. create an L2 no-submit package;
3. add manual pose/keyframe control;
4. switch to backup route B, doorway / side-hall threshold compression.

## 16. What Not To Do

- Do not run Dreamina.
- Do not submit/query/download.
- Do not create package JSON.
- Do not create manifest CSV.
- Do not create prompt txt.
- Do not use R01/R02 as approved keyframes.
- Do not mark final.
- Do not lock.
- Do not update official Source.
- Do not treat this blueprint as a live package.

## 17. Safety

- No Dreamina command was run.
- No submit/query/download was run.
- No retry/resubmit was run.
- No media was created.
- No media was staged.
- No package JSON was created.
- No manifest CSV was created.
- No prompt txt was created or modified.
- No shot record JSON was created or modified.
- No runtime code was modified.
- `configs/providers.json` was not modified.
- `sources/` was untouched.
- `final_master=false`
- `locked=false`

## 18. Final Verdict

SHOT04_ROUTE_A_COMPOSITION_MATRIX_PROMPT_BLUEPRINT_READY_HUMAN_CHATGPT_K184_REVIEW
