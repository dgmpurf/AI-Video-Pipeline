# PHASE K155 - SHOT-03 SPLIT-02 Pose Keyframe Draft Audit and Refined Prompt

## 1. Purpose

Audit and refine the K154 `SPLIT02_POSE_KF_01_column_edge_guard_compression` draft prompt and reference-duty map.

This phase is text-only. The revised prompt remains embedded inside this report only and is not a standalone prompt file, package, manifest, shot record, or production asset.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K154_SHOT03_SPLIT02_POSE_KF_PROMPT_DRAFT_AND_REFERENCE_MAP.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K153_SHOT03_SPLIT02_POSE_KEYFRAME_REFERENCE_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K151_SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K149_SHOT03_BASELINE_CANDIDATE_STATE_RECORD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K148_SHOT03_V004_CUT_CANDIDATE_SELECTION_RECORDED.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

## 3. Source Governance Confirmation

- `sources/` was read-only reference material.
- No `sources/` file was created, edited, renamed, moved, deleted, staged, committed, or pushed.
- Official Source updates require ChatGPT generation/review and human manual application.
- K155 creates evidence and draft planning under `reports/` only.

## 4. K154 Audit Summary

| item | result | note |
|---|---|---|
| Text-only boundary | passed | K154 created only a report. |
| No Dreamina/package/media | passed | No submit/query/download, no media, no package files. |
| Reference-duty map | useful | Identity refs, scene ref, start anchor, return anchor, and draft role were separated clearly. |
| Mojibake issue | present | Corrected K152 wording and the K154 draft prompt first line contain encoding corruption. |
| Production readiness | not ready | K154 draft cannot be used as a production prompt without human/ChatGPT audit and clean text correction. |
| Action risk | needs reduction | Foot/skid/force-chain language is directionally valid but too prominent for this micro-goal. |
| Revision requirement | required | K155 should reduce foot emphasis and keep the column as obstacle/occluder only. |

K154 is directionally useful but not production-ready. It correctly identifies the micro-goal, yet the draft should be narrowed before any K156 standalone prompt or package planning.

## 5. Corrected K152 Wording

Recorded corrected line:

`纭 K152锛歱rimary start = CUT_B_START_03锛宐ackup start = CUT_B_START_04锛沺rimary return = CUT_C_RETURN_01锛宐ackup return = CUT_C_RETURN_04/05锛汻ETURN_02/03 rejected锛涜繘鍏?K153 pose/keyframe reference plan銆?`

K153 and K154 themselves were not modified in K155.

## 6. Anchor Frame Inventory

| candidate_id | path | exists | role | future usage note |
|---|---|---:|---|---|
| CUT_B_START_03 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | yes | primary start anchor | Use as entry continuity/composition only; not identity reference. |
| CUT_B_START_04 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_04_t2p00.jpg` | yes | backup start anchor | Keep available if START_03 feels early or too visually distant. |
| CUT_C_RETURN_01 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | yes | primary return anchor | Use as return continuity target after the column-edge compression keyframe. |
| CUT_C_RETURN_04 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_04_t0p60.jpg` | yes | backup return anchor | Backup if RETURN_01 is too abrupt. |
| CUT_C_RETURN_05 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_05_t0p80.jpg` | yes | backup return anchor | Later backup return, likely more settled. |

## 7. Audit of K154 Draft Prompt Risks

| issue | why it matters | K155 decision |
|---|---|---|
| Mojibake in first line | A corrupted first line is unsafe for a production prompt and may break instruction clarity. | Keep K155 report-only; K156 must clean/confirm the first line before any standalone prompt file. |
| Too much foot/skid/force-chain language | Prior V005/V006 failures showed that strong foot/terrain language can become footwork display, soft stepping, or terrain-prop behavior. | Reduce foot detail to "feet stay on flat wet stone floor"; keep body compression in arms/torso/guard. |
| Possible column-as-prop risk | Column could become a stepping point, force trigger, or parkour object. | Define the column only as narrow obstacle and partial occluder. |
| Possible pose showcase risk | Still keyframes can become poster poses instead of implied action. | Keep "middle keyframe between CUT_B_START_03 and CUT_C_RETURN_01" and "physically engaged." |
| Possible structural damage hallucination | Terrain pressure can induce cracks, debris, splinters, or broken architecture. | Hard-ban breakage, cracks, debris, splinters, water shield, smoke explosion, and architecture destruction. |
| Possible identity drift | Video-derived frames are not sufficient identity protection. | Keep identity refs identity-only and state video frames are continuity/composition only. |
| Possible overcomplexity | Too many force-chain clauses can confuse a single static image request. | Narrow to one visible physical job: guard compressed toward the column edge. |

## 8. Refined Draft Keyframe Prompt

Status markers:

- `DRAFT_ONLY_NOT_FOR_SUBMIT`
- `NOT_FINAL`
- `REQUIRES_HUMAN_CHATGPT_APPROVAL_BEFORE_PROMPT_FILE_OR_PACKAGE`

Important note: the first line below is preserved in the K155 draft structure requested for this audit, but it still requires clean human/ChatGPT confirmation before any production prompt file is created.

```text
SPLIT02_POSE_KF_01_column_edge_guard_compression銆傜敾闈腑涓嶈鍑虹幇浠讳綍鏂囧瓧銆佺紪鍙锋垨鏍囪瘑銆?

This is a single static keyframe, not a video.
Use the same rainy exterior temple corridor style as SHOT-03 V004: wet stone floor, wooden corridor columns, railing line, cold blue-gray rain light, medium-wide action framing.
The wooden column sits near the center-left or center of the action area and works only as a narrow obstacle and partial occluder.

Fenshou remains the black-red armored male fighter. Shuangji remains the blue-white/silver female fighter.
They are still in close combat beside the wooden column.
Fenshou presses into Shuangji's raised guard from the left side.
Shuangji's forearms and shoulders are compressed toward the column edge.
The column partially hides a small part of their overlapping arms or torsos, creating a tight corridor squeeze.
Both fighters remain physically engaged and close together; neither fighter is separated, posing, or resetting.

The image should feel like one middle keyframe between CUT_B_START_03 and CUT_C_RETURN_01:
incoming pressure from CUT_B, one compressed column-edge beat, then ready to return to close corridor combat.
Keep the camera V004-like, medium-wide, readable bodies, no face close-up, no poster pose.

Both fighters' feet stay on the flat wet stone floor.
No one steps on the column base, no one steps on a random stone, no one jumps, no hangtime, no parkour, no wall-run, no roof, no stairs, no eaves route.
No railing, door, lattice, wall, or column breakage.
No cracks, debris, wood splinters, broken boards, shockwave, water shield, smoke explosion, or architecture destruction.
No extra characters, no duplicated fighters, no body fusion, no extra limbs, no random weapons, no text, no watermark.
```

## 9. Refined Reference-Duty Map

| label | source path / type | future duty | must preserve | must not copy/change | required now/later | risk notes |
|---|---|---|---|---|---|---|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` / upload-safe identity image | Fenshou identity-only | black-red armor, male-coded fighter role, face/hair/costume language | Do not dictate pose, exact corridor placement, or camera | Later if K156 authorizes prompt/package planning | Identity refs protect character continuity; they are not scene or action refs. |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` / upload-safe identity image | Shuangji highest-priority identity-only | female-coded face/body, blue-white/silver costume, hair language | Do not let video-frame blur override identity; do not male-code or duplicate | Later if K156 authorizes prompt/package planning | Highest-priority identity anchor. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` / upload-safe scene/world image | Scene/world only | rainy temple atmosphere, wet stone, wooden architecture, corridor compatibility | Do not use as character identity or exact action pose | Later if K156 authorizes package planning | Helps prevent scene drift but must not overpower V004 corridor anchors. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` / video-derived frame | Primary continuity/composition start anchor | incoming pressure direction, V004-like spacing, corridor combat flow | Not identity reference; do not preserve blur/artifacts as character truth | Now for planning; later if package approved | Should only feed the pose's entry relationship. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` / video-derived frame | Primary return continuity target | exit relationship back into close corridor combat | Not identity reference; do not force static end pose | Now for planning; later if package approved | Pose must remain compatible with returning into this frame family. |
| `@SPLIT02_POSE_KF_01_REFINED_DRAFT` | This K155 report only / refined draft text | Future keyframe concept only | one compressed column-edge beat, narrow obstacle/occluder, no stepping/breakage | Do not treat as final prompt, official Source, package, locked ref, or submitted asset | Now only as report evidence | Requires human/ChatGPT approval before K156 creates any standalone file. |

## 10. Revised Risk Audit

| risk | mitigation in refined draft | remaining concern |
|---|---|---|
| Foot/base stepping | Feet stay on flat wet stone; explicit no column base and no random stone. | A future visual package must avoid reference images that imply stepping. |
| Column turning into parkour prop | Column is only a narrow obstacle and partial occluder; no parkour, wall-run, roof, stairs, or eaves. | If K156 adds too much terrain language, this risk can return. |
| Action becoming poster pose | Prompt calls it a middle keyframe between CUT_B and CUT_C with both fighters engaged. | Static keyframe generation can still beautify; human review remains required. |
| Structural damage | Explicit no railing, door, lattice, wall, or column breakage; no cracks/debris/splinters. | "Compression" must remain body/guard compression, not architecture compression. |
| Identity drift | Identity refs remain identity-only; video-derived frames are not identity sources. | Future package must actually include the identity refs if Dreamina is later used. |
| Scene drift | V004 corridor style and scene/world ref are specified. | Scene ref path is courtyard/world style, so V004 video anchors still matter for corridor composition. |
| Over-occlusion by column | Column hides only a small part of overlapping arms or torsos. | Generated keyframe may still hide faces; review must check readable bodies. |
| Body fusion | Hard negative: no body fusion, no extra limbs, no duplicated fighters. | Close overlapping arms increase anatomy risk; K156 may need even clearer separation language. |

## 11. Clause-Level Compliance Map

| source / planning rule | required behavior | refined prompt clause | status | remaining improvement |
|---|---|---|---|---|
| One physical job only | Keep SPLIT-02 narrow | "one compressed column-edge beat" | present | K156 should resist adding extra terrain actions. |
| Column as obstacle/occluder | Column must not become force trigger or prop | "works only as a narrow obstacle and partial occluder" | present | Future package should repeat this in reference-duty notes. |
| No foot-on-column-base | Avoid V005/V006 foot/terrain failure mode | "No one steps on the column base" | present | Keep foot language minimal. |
| No jump/parkour/roof/stairs/eaves | Avoid acrobatic drift | "no jumps, no hangtime, no parkour, no wall-run, no roof, no stairs, no eaves route" | present | None for K155. |
| No architecture breakage | Avoid hallucinated structural damage | "No railing, door, lattice, wall, or column breakage" | present | K156 should avoid words like smash/crush into column. |
| V004-like corridor composition | Preserve baseline candidate continuity | "same rainy exterior temple corridor style as SHOT-03 V004" | present | Future package should include V004-derived anchors. |
| Identity/reference duty separation | Identity refs identity-only; video frames continuity-only | Refined reference-duty map separates duties | present | Future package should not use V004 frames as identity anchors. |
| Static keyframe, not video | K155 is keyframe prompt draft only | "This is a single static keyframe, not a video" | present | Do not add timecode choreography in K156 prompt file unless task changes. |
| Not final / not locked | No final approval in K155 | status markers and safety section | present | Human review needed before any package or generation. |
| No Dreamina / no package in K155 | Text-only audit only | purpose, safety, and what-not-to-do sections | present | None for K155. |

## 12. K155 Audit Verdict

`DRAFT_REVISED_READY_FOR_HUMAN_REVIEW_NOT_FOR_PACKAGE`

The refined draft reduces the main risk introduced by K154: overemphasis on foot/skid/force-chain language. It keeps the micro-goal narrow, treats the column as an obstacle/occluder only, and keeps the draft report-only. It is still not a production prompt because K156 must cleanly confirm the first-line text and decide whether to create any standalone prompt file.

## 13. Recommended Next Phase

Recommend K156:

Human decision whether to convert the refined draft into a standalone prompt file and package-planning phase.

K156 should still be no Dreamina unless explicitly authorized.

Possible K156 outputs:

- actual prompt txt draft under `prompts/manual` only if human authorizes
- reference-duty package plan only
- no submit

## 14. Alternative Next Phase

If the human rejects SPLIT-02 risk:

- plan direct CUT_B -> CUT_C edit continuity
- defer terrain insert
- avoid keyframe/image2image route for this split

## 15. What Not To Do

- no prompt-only V007
- no full 5s terrain force-chain attempt
- no foot-on-column-base
- no architecture breakage
- no Dreamina submit
- no final/lock
- no Source modification by Codex

## 16. Source Update Recommendation

Do not update official Source in K155.

V1.12 should wait until SPLIT-02 is either tested or abandoned. K155 is evidence for later Source discussion, not official Source.

## 17. Safety

- no Dreamina
- no submit/query/download
- no retry/resubmit
- no new media created
- no frames/contact sheets/cuts created
- no standalone prompt file created
- no package JSON/manifest/shot record created
- no shot record modified
- `sources/` not modified/staged
- runtime/config not modified
- media artifacts not staged
- `final_master=false`
- `locked=false`
- SHOT-02 / V013 / V018 / V004 / V005 / V006 lock states not touched

## 18. Final Verdict

SHOT03_SPLIT02_POSE_KF_DRAFT_AUDITED_AND_REFINED_READY_HUMAN_K156_DECISION_REQUIRED
