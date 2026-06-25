# PHASE K98 - SHOT-03 Route A/B Hybrid Package Design

## Purpose

This phase confirms SHOT-03 Route A/B hybrid and prepares the package design for a future SHOT-03 prompt/package phase.

This is not a live submit package. It does not create the final Dreamina prompt, manifest, shot record, or media outputs.

No Dreamina command was run. No submit/query/download happened. No AI media was generated. No media files were created, edited, moved, deleted, or staged.

## Human Route Confirmation

The human explicitly confirmed:

> 柱列廊道近身压迫 → 湿石阶高低差战斗 → 檐口/屋顶边缘收束

Selected route:

`Route A/B hybrid`

Operational meaning:

1. Column/corridor close-pressure combat.
2. Wet stone stair height-difference combat.
3. Eaves / roof-edge endpoint.

## Selected Route Explanation

SHOT-03 follows the closed SHOT-02 close-combat branch.

SHOT-02 current state remains:

- Current locked edit candidate: `SHOT-02-V018-speed-1p18x`
- Backup candidate: `SHOT-02-V018-speed-1p12x`
- Historical locked passed segment: `SHOT-02-V013-CUT01-LOCKED`
- `SHOT-02 final_master=false`
- `whole_film_final_master=false`

The Route A/B hybrid is the right next design because it preserves continuity from SHOT-02 floor-level close combat while making the next beat visibly about architecture.

The route expands the fight through the temple rather than jumping straight to destruction:

- It starts with pillar/corridor line pressure.
- It escalates into wet-stair height difference and traction problems.
- It ends at an eaves / roof-edge anchor, leaving SHOT-04 room for structural break and SHOT-05 room for full temple destruction.

## Beat-By-Beat Package Design

### Beat 01 - Column / Corridor Close Pressure

Environment anchor:

- Pillars.
- Corridor line.
- Rain-slick stone floor.

Action function:

- Expand close combat into architecture line control.
- Keep both characters close, but force tactical angle changes through pillar/corridor geometry.
- One fighter can use the column line to break angle or deny the other fighter's direct path.

Body mechanics:

- Short hard forearm, palm, shoulder, or guard contacts.
- Rebound after each contact.
- Shoulder turn, hip adjustment, and foot skid on wet stone.
- No long bind.

Camera function:

- Lateral track along the pillar/corridor line.
- Keep both fighters readable when a pillar partially occludes one body.
- Do not let occlusion become confusion.

Risk:

- The model may treat pillars as background decoration.
- A pillar may hide the actual contact point.

Future K99 prompt-design notes:

- Make the pillar/corridor an active obstacle.
- Name the contact point and the rebound.
- Describe foot contact on wet stone.
- Forbid soft push-hands rhythm.

### Beat 02 - Wet Stone Stair Height-Difference Combat

Environment anchor:

- Wet stone stairs.
- Step edges.
- Railing if available in the selected reference.

Action function:

- Introduce verticality and height difference.
- Change strike/guard angles through stair level.
- Force slip, recovery, pivot, and displacement.

Body mechanics:

- One fighter steps up or down under pressure.
- A foot nearly loses traction on the wet step.
- The recovery becomes counter-pressure rather than a fall.
- Defender reaction should show torso displacement, guard collapse, forced sidestep, or foot skid.

Camera function:

- Slight rising or diagonal follow is allowed only if the feet remain visibly anchored to steps.
- Keep the stair geometry readable.

Risk:

- Stairs may become visually unreadable.
- The model may convert stair movement into a floating leap.

Future K99 prompt-design notes:

- Write shoe/boot contact on wet step edges.
- Use height difference to change guard and strike angles.
- Forbid big jump, flying, or floaty rooftop movement.

### Beat 03 - Eaves / Roof-Edge Endpoint

Environment anchor:

- Eaves.
- Roof edge.
- Visible roof tiles.
- Wooden structure.

Action function:

- End with a spatial escalation cue toward SHOT-04.
- Show that the fight has reached a more dangerous architectural edge.
- Keep the temple intact enough that SHOT-04 can own structural break.

Body mechanics:

- Short recovery stance near roof edge or eaves.
- Footwork remains grounded.
- Tile/wood feedback can be small, but not full collapse.

Camera function:

- Hold enough roofline/eaves geometry for spatial continuity.
- Do not hide contact behind eaves.
- Do not convert the shot into a full rooftop duel yet.

Risk:

- The shot may jump too quickly into SHOT-04/05 territory.
- Roof movement may become floaty or overly mythic.

Future K99 prompt-design notes:

- Use roof edge as endpoint, not a full roof duel.
- Allow minor tile or wood feedback only.
- Forbid large structural collapse and full temple destruction.

## What SHOT-03 Must Not Do

SHOT-03 must not include:

- full temple destruction
- snow mountain transition
- weapon combat
- giant forms
- final master status
- large structural collapse
- over-dominant particles
- soft push-hands rhythm
- long held binds
- extra fighters or duplicate characters
- Shuangji gender drift
- costume merge between Fenshou and Shuangji

## Future K99 Package Requirements

K99 should create the actual SHOT-03 package only after this route-confirmation phase.

K99 should include:

- manual prompt text
- prompt JSON
- manifest CSV
- shot record JSON
- readiness review markdown
- package report

K99 should use:

- active route: `Route A/B hybrid`
- likely model family: `seedance2.0_vip`
- likely duration: `5s` for first SHOT-03 candidate
- likely ratio: `16:9`
- likely resolution: `720p`
- human review required
- `final_master=false`
- `locked=false`

K99 should likely use approved/upload-safe identity and scene anchors if available. Exact reference selection belongs to K99, not K98.

Known locked references for future consideration:

| Reference | Possible future duty |
| --- | --- |
| `A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | Fenshou identity |
| `A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | Shuangji full-body identity |
| `A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | highest-priority Shuangji identity anchor |
| `A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | rainy temple scene / world anchor |

If K99 needs multiple identity and scene references, `multimodal2video` should be reviewed as the likely task type. If a smaller CLI-legal task type can satisfy the route with fewer references, K99 should justify that choice after command-contract preflight. No live submit should happen without explicit human authorization.

## Route Risks And Mitigation

Risk: environment becomes background only.

Mitigation: explicitly name pillar, corridor, stair, eave, and roof-edge anchors as action surfaces or tactical obstacles.

Risk: model jumps to roof too early.

Mitigation: keep the roof edge as endpoint. Do not ask for a full rooftop duel in SHOT-03.

Risk: stairs become unreadable.

Mitigation: describe wet step edges, foot placement, traction, slip, and recovery.

Risk: roof movement becomes floaty.

Mitigation: forbid flying, big jump, and floaty wuxia movement. Keep foot contact visible.

Risk: rain hides contact.

Mitigation: make rain secondary to body mechanics and contact readability.

Risk: destruction escalates too early.

Mitigation: forbid full temple destruction, large collapse, and snow transition in SHOT-03.

## Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K97_SHOT03_TEMPLE_ENVIRONMENT_ESCALATION_PLANNING_PACKAGE.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/plans/SHOT-03_temple_environment_escalation_planning_package.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K96_MASTER_STORY_ARC_AND_SHOT03_SELECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/plans/master_story_arc_and_SHOT-03_selection.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K94_SHOT02_SEQUENCE_EDIT_CONFORM_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K93_SHOT02_COMBAT_STAGE_CLOSEOUT_AND_EDIT_CHECKLIST.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/assets/asset_registry.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/plans/`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.5_剧本美术与分镜设计增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.6_分镜模板与风格词库增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`

## Safety Confirmation

- No Dreamina command was run.
- `dreamina version` was not run.
- `dreamina user_credit` was not run.
- No submit/query/download happened.
- No retry/resubmit/batch happened.
- No AI media was generated.
- No media files were created, edited, moved, deleted, or staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- Project Source files were not modified.
- SHOT-02 / V013 / V018 lock states were not altered.

## Output Files

- Package design JSON: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/plans/SHOT-03_route_AB_hybrid_package_design.json`
- Report: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K98_SHOT03_ROUTE_AB_HYBRID_PACKAGE_DESIGN.md`

## Final Verdict

SHOT03_ROUTE_AB_HYBRID_PACKAGE_DESIGN_READY
