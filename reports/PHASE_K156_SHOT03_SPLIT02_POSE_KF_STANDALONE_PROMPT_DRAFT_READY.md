# PHASE K156 - SHOT-03 SPLIT-02 Pose Keyframe Standalone Prompt Draft Ready

## 1. Purpose

Create a standalone draft prompt txt and reference-duty map for:

`SPLIT02_POSE_KF_01_column_edge_guard_compression`

This is a draft prompt file only. It is not final, not a Dreamina package, and not approved for submit.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K155_SHOT03_SPLIT02_POSE_KF_DRAFT_AUDIT_AND_REFINED_PROMPT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K154_SHOT03_SPLIT02_POSE_KF_PROMPT_DRAFT_AND_REFERENCE_MAP.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K153_SHOT03_SPLIT02_POSE_KEYFRAME_REFERENCE_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K151_SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

## 3. Source Governance Confirmation

- `sources/` was read-only reference material.
- No `sources/` file was created, edited, renamed, moved, deleted, staged, committed, or pushed.
- Official Source updates require ChatGPT generation/review and human manual action.
- K156 creates one prompt draft file and one report only.

## 4. K155 Basis

- K155 verdict: `DRAFT_REVISED_READY_FOR_HUMAN_REVIEW_NOT_FOR_PACKAGE`
- K155 identified K154 mojibake and reduced foot/skid/force-chain risk.
- K156 creates a clean standalone draft prompt only.
- K156 does not create a final prompt, package JSON, manifest CSV, shot record JSON, media, or Dreamina task.

## 5. Prompt File Created

| field | value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` |
| exists | yes |
| size_bytes | 1933 |
| sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| encoding | UTF-8 |
| status | `DRAFT_ONLY_NOT_FOR_SUBMIT`; `NOT_FINAL`; `REQUIRES_HUMAN_CHATGPT_APPROVAL_BEFORE_PACKAGE_OR_DREAMINA` |

## 6. Reference-Duty Map

| logical label | source path | exists | duty | must preserve | must not copy/change | risk notes |
|---|---|---:|---|---|---|---|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | yes | Identity-only for Fenshou | black-red armored male fighter identity, face/hair/costume language | Must not dictate corridor pose, exact camera, or action mechanics | Use as identity anchor only if a future package is approved. |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | yes | Highest-priority identity-only for Shuangji | blue-white/silver female fighter identity, face/hair/body/costume language | Must not be overridden by blurred video frames; must not become male-coded | Highest identity-drift risk, so keep this as identity anchor only. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | yes | Scene/world only | rainy temple world, wet stone, wooden architectural language, cold rain mood | Must not dictate character identity or exact body contact pose | Scene ref helps world continuity but V004 video-derived anchors remain needed for corridor composition. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | yes | Start continuity/composition anchor only | incoming corridor-combat pressure, V004-like spacing, action direction | Must not be identity reference or artifact source | Video-derived frame is a continuity anchor only. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | yes | Return continuity/composition anchor only | exit path back into close corridor combat | Must not force static end pose; must not be identity reference | Future keyframe should be compatible with this return family. |
| `@SPLIT02_POSE_KF_01_DRAFT_PROMPT` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` | yes | Draft-only still keyframe prompt | narrow micro-goal: column-edge guard compression + brief occlusion | Not final, not package, not submit-ready, not locked | Requires K157 human + ChatGPT audit before any package planning. |

## 7. Clean Prompt Body

```text
SPLIT02_POSE_KF_01_column_edge_guard_compression. No visible text, numbers, labels, captions, logo, watermark, or UI marks in the image.

This is a single static keyframe, not a video.

Use the same rainy exterior temple corridor style as SHOT-03 V004: wet stone floor, wooden corridor columns, railing line, cold blue-gray rain light, and medium-wide action framing. The camera should feel V004-like, with readable bodies and no face close-up.

The wooden column sits near the center-left or center of the action area. The column works only as a narrow obstacle and partial occluder. It is not a stepping point, not a force trigger, not a parkour prop, and not a breakable object.

Fenshou remains the black-red armored male fighter. Shuangji remains the blue-white and silver female fighter. They are still in close combat beside the wooden column.

Fenshou presses into Shuangji's raised guard from the left side. Shuangji's forearms and shoulders are compressed toward the column edge. The column partially hides a small part of their overlapping arms or torsos, creating a tight corridor squeeze.

Both fighters remain physically engaged and close together. Neither fighter is separated, posing, resetting, or looking away. The image should feel like one middle keyframe between CUT_B_START_03 and CUT_C_RETURN_01: incoming corridor-combat pressure, one compressed column-edge beat, then ready to return to close corridor combat.

Both fighters' feet stay on the flat wet stone floor. No one steps on the column base. No one steps on a random stone. No jump, no hangtime, no parkour, no wall-run, no roof, no stairs, no eaves route.

No railing, door, lattice, wall, or column breakage. No cracks, debris, wood splinters, broken boards, shockwave, water shield, smoke explosion, or architecture destruction.

No extra characters, no duplicated fighters, no body fusion, no extra limbs, no random weapons, no text, no watermark.
```

## 8. Risk Check

| risk | mitigation in prompt | remaining concern |
|---|---|---|
| Column becomes stepping object | Prompt says column is not a stepping point and no one steps on column base. | Future package refs must not visually imply foot-on-base. |
| Column becomes parkour prop | Prompt says not parkour prop, no jump, hangtime, wall-run, roof, stairs, or eaves route. | If future K157/K158 adds terrain spectacle, this risk can return. |
| Action becomes poster pose | Prompt says both fighters remain physically engaged and this is a middle keyframe between CUT_B_START_03 and CUT_C_RETURN_01. | Static keyframes can still become posed; human review remains required. |
| Architecture damage appears | Prompt explicitly bans railing/door/lattice/wall/column breakage, cracks, debris, splinters, broken boards, shockwave, shield, smoke explosion, and architecture destruction. | Avoid verbs like smash/crush/break in future package language. |
| Identities drift | Prompt states Fenshou and Shuangji identity roles; reference-duty map requires identity refs. | Future package must include identity refs and not rely on video frames. |
| Scene drifts away from V004 | Prompt anchors rainy exterior temple corridor and V004-like camera. | Future visual refs must preserve corridor, not revert to open courtyard. |
| Body fusion / extra limbs | Prompt bans body fusion, extra limbs, duplicated fighters, and extra characters. | Close overlapping arms are still anatomy-risky; future package may need one clear contact plane. |
| Prompt too narrow / too ordinary | Prompt intentionally narrows to one micro-goal: column-edge guard compression plus brief occlusion. | This may be subtle; K157 should decide if the micro-goal is worth a keyframe attempt. |

## 9. Clause-Level Compliance Map

| requirement | prompt/report clause | status | note |
|---|---|---|---|
| One physical job only | "one compressed column-edge beat" and column-edge guard compression | present | No full 5s force-chain attempt. |
| Static keyframe, not video | "This is a single static keyframe, not a video." | present | No timecode choreography. |
| Column as obstacle/occluder | "works only as a narrow obstacle and partial occluder" | present | Not a force trigger or prop. |
| No foot-on-column-base/random stone | "No one steps on the column base. No one steps on a random stone." | present | Keeps K155 risk reduction. |
| No jump/parkour/roof/stairs/eaves | Hard negative sentence lists all forbidden routes. | present | Prevents V005/V006 terrain drift. |
| No architecture breakage | Hard negative sentence bans breakage/cracks/debris/splinters. | present | No SHOT-04 damage escalation here. |
| V004 corridor continuity | "same rainy exterior temple corridor style as SHOT-03 V004" | present | Links to baseline corridor candidate. |
| Reference-duty separation | Section 6 separates identity refs, scene ref, start anchor, return anchor, draft prompt. | present | Video-derived frames are continuity/composition only. |
| No final/lock | Prompt status and safety say not final and not locked. | present | Human + ChatGPT approval required before package. |
| No Dreamina/no package in K156 | Purpose, K155 basis, and safety sections state no Dreamina and no package. | present | K156 is text-only draft prompt + report. |

## 10. Recommended Next Phase

Recommend K157:

Human + ChatGPT audit of the standalone draft prompt file and reference-duty map.

K157 should decide whether to:

- approve the prompt file for package planning
- revise the prompt again
- abandon SPLIT-02 and plan CUT_B -> CUT_C direct edit continuity

K157 remains no Dreamina unless explicitly authorized.

## 11. What Not To Do

- no prompt-only V007
- no full 5s terrain force-chain attempt
- no Dreamina submit
- no final/lock
- no Source modification by Codex

## 12. Safety

- no Dreamina
- no submit/query/download
- no retry/resubmit
- no media created
- no frames/contact sheets/cuts created
- no package JSON/manifest/shot record created
- no shot record modified
- `sources/` not modified/staged
- runtime/config not modified
- media artifacts not staged
- `final_master=false`
- `locked=false`

## 13. Final Verdict

SHOT03_SPLIT02_POSE_KF_STANDALONE_DRAFT_PROMPT_READY_HUMAN_CHATGPT_K157_AUDIT_REQUIRED
