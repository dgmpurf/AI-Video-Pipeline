# PHASE K153 - SHOT-03 SPLIT-02 Pose/Keyframe Reference Plan

## Purpose

Plan the SPLIT-02 pose/keyframe reference strategy after the K152 start/end frame selection.

This phase records the human-confirmed K152 frame-pair decision and defines what a future intermediate pose/keyframe reference should show. It does not create the pose/keyframe, a final prompt, a package, media, frames, contact sheets, manifests, or shot records.

## Files Inspected

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K151_SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K149_SHOT03_BASELINE_CANDIDATE_STATE_RECORD.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K148_SHOT03_V004_CUT_CANDIDATE_SELECTION_RECORDED.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K146_SHOT03_V004_CUT_CANDIDATES_CREATED.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md

## Source Governance Confirmation

- sources/ was read as reference only.
- No sources/ files were modified.
- No sources/ files were staged.
- Official Source updates require ChatGPT generation/review and human manual action.
- source_write_allowed=false
- source_stage_allowed=false
- source_commit_allowed=false

## K152 Selection Record

Human-confirmed K152 decision:

> 纭 K152锛歱rimary start = CUT_B_START_03锛宐ackup start = CUT_B_START_04锛沺rimary return = CUT_C_RETURN_01锛宐ackup return = CUT_C_RETURN_04/05锛汻ETURN_02/03 rejected锛涜繘鍏?K153 pose/keyframe reference plan銆?

Recorded selection:

- primary start = CUT_B_START_03
- backup start = CUT_B_START_04
- primary return = CUT_C_RETURN_01
- backup return = CUT_C_RETURN_04 / CUT_C_RETURN_05
- rejected return = CUT_C_RETURN_02 / CUT_C_RETURN_03

## Frame Candidate Inventory

| Candidate ID | Path | Exists | Role | Reason Selected Or Rejected |
| --- | --- | --- | --- | --- |
| CUT_B_START_03 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg | true | primary_start | Human-confirmed best start anchor from CUT_B for entering SPLIT-02; should preserve the current corridor-combat momentum before the terrain insert. |
| CUT_B_START_04 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_04_t2p00.jpg | true | backup_start | Human-confirmed backup start anchor if CUT_B_START_03 proves too early or less compatible with the future pose/keyframe. |
| CUT_C_RETURN_01 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg | true | primary_return | Human-confirmed best return anchor into CUT_C; should receive the exit from the SPLIT-02 terrain insert with minimal visual jump. |
| CUT_C_RETURN_04 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_04_t0p60.jpg | true | backup_return | Human-confirmed backup return if the primary return is too abrupt or if the future insert exits closer to mid-CUT_C motion. |
| CUT_C_RETURN_05 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_05_t0p80.jpg | true | backup_return | Human-confirmed backup return if the selected intermediate pose/keyframe needs a later CUT_C receiving position. |
| CUT_C_RETURN_02 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_02_t0p20.jpg | true | rejected_return | Human-confirmed rejected return candidate; keep only as audit evidence, not as preferred SPLIT-02 return planning material. |
| CUT_C_RETURN_03 | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_03_t0p40.jpg | true | rejected_return | Human-confirmed rejected return candidate; keep only as audit evidence, not as preferred SPLIT-02 return planning material. |

## Continuity Assessment

CUT_B_START_03 can feed into a column-edge compression insert if the future insert keeps the V004 corridor direction, mid-shot framing, and ongoing contact pressure. It should not be treated as a final pose; it is a continuity anchor for the incoming momentum.

CUT_C_RETURN_01 can receive the return from SPLIT-02 if the future insert exits with both fighters still close, engaged, and aligned to the corridor. It should receive a combat-driven exit, not a reset or new standoff.

CUT_B_START_04, CUT_C_RETURN_04, and CUT_C_RETURN_05 should remain available as backup anchors. They are useful if the future intermediate pose/keyframe needs a slightly later entry or later return point.

Existing K151 frames are enough as continuity anchors, but they are not enough by themselves to define the terrain beat. An intermediate pose/keyframe is recommended because the intended physical job is specific: column-edge guard compression + brief occlusion. Without an intermediate reference, a future video generation may fall back into ordinary corridor combat, walking around a pillar, or soft body drift.

## Recommended Intermediate Pose/Keyframe

Tentative reference ID:

SPLIT02_POSE_KF_01_column_edge_guard_compression

The future intermediate pose/keyframe should show:

- same exterior corridor / rainy temple / wet stone / railing / wooden column
- V004-like camera and corridor composition
- Fenshou close to the column edge, driving pressure into Shuangji's guard
- Shuangji's guard compressed toward the column edge
- column partially occluding the body line
- both bodies still engaged, not separated
- forearms and shoulders visibly compressed, not soft pushing
- one terrain job only: the column functions as obstacle/occluder
- no stepping on column base
- no jump
- no hangtime
- no parkour display
- no wall-run
- no breakage
- no pose-out
- no random stone
- no roof/stairs/eaves

## Pose/Keyframe Design Constraints

- Camera/framing should stay V004-like: exterior corridor, mid-shot readability, rainy temple environment, wet stone, railing, wooden column.
- The column must be an obstacle/occluder, not a force trigger or magical power source.
- The terrain job is one beat only: guard compression into column-edge occlusion.
- Character identities should remain readable, but no face close-up is needed.
- Both fighters must remain physically engaged.
- No architecture damage, cracks, debris, wood splinters, railing breakage, door breakage, lattice breakage, or wall breakage.
- No foot-on-column-base, foot-on-random-stone, jump, hangtime, parkour, roof, stairs, eaves route, or wall-run.
- The return path must allow CUT_C_RETURN_01 as the primary return anchor.
- The pose/keyframe must not become a poster-like pose, static standoff, or slow showcase.

## Future Reference-Pack Strategy

| Reference Item | Source | Future Purpose | Required In K154/K155? | Notes |
| --- | --- | --- | --- | --- |
| Fenshou identity ref | Existing approved Fenshou identity/reference image | Preserve Fenshou identity during future SPLIT-02 planning or generation | Required later, not in K153 | Identity only; do not use blurred video frames as primary identity reference. |
| Shuangji identity ref | Existing approved Shuangji identity/reference image | Preserve Shuangji identity and prevent drift | Required later, not in K153 | Highest importance for identity stability if future multimodal/video package is used. |
| Corridor/scene ref | V004 corridor material and K151/K144 frame candidates | Preserve exterior corridor, column, railing, wet stone, rain, and V004 style | Required later, not in K153 | Scene/world reference only. |
| Primary start frame | CUT_B_START_03_t1p80.jpg | Entry continuity from preferred CUT_B SPLIT-01 baseline | Required for planning; possible package reference later | Start anchor, not identity reference. |
| Intermediate pose/keyframe | SPLIT02_POSE_KF_01_column_edge_guard_compression, to be designed later | Define the exact column-edge compression beat | Recommended K154 planning item | Do not create media in K153. |
| Primary return frame | CUT_C_RETURN_01_t0p00.jpg | Return continuity into possible CUT_C SPLIT-03 candidate | Required for planning; possible package reference later | Return anchor, not identity reference. |
| Backup start frame | CUT_B_START_04_t2p00.jpg | Alternative entry continuity if start 03 is too early | Optional later | Keep available. |
| Backup return frames | CUT_C_RETURN_04_t0p60.jpg and CUT_C_RETURN_05_t0p80.jpg | Alternative receiving points if CUT_C_RETURN_01 is too abrupt | Optional later | Keep available; do not use rejected return 02/03. |

## Future Generation Route Discussion

No route is selected in K153. Later options:

- frames2video after start/intermediate/end references exist: useful if the project can provide strong visual anchors across the exact terrain beat, but risk remains if identities or body mechanics drift.
- multimodal2video with identity + scene + selected frame references: useful for identity protection and scene preservation, but the action may still need a clear intermediate pose/keyframe to avoid soft or generic corridor fighting.
- image2image to create the intermediate pose keyframe before video generation: useful if K154 determines the column-edge compression must be visually locked before any video attempt.
- local-only edit continuity if terrain insert is abandoned: safest if the human prefers to avoid more SPLIT-02 risk and simply bridge CUT_B to CUT_C.

No live generation happens in K153 because the pose/keyframe reference has not been human-approved and no package has been prepared.

## Recommended Next Phase

Recommend K154:

Create a text-only SPLIT02_POSE_KF_01 keyframe prompt draft and reference-duty map.

K154 should remain:

- no Dreamina
- no package
- no media
- no final prompt/package until human approves

## Alternative K154

If the human wants to avoid more SPLIT-02 risk, K154 can instead plan CUT_B -> CUT_C direct edit continuity.

## What Not To Do

- no prompt-only V007
- no full 5s terrain force-chain attempt
- no foot-on-column-base
- no architecture breakage
- no Dreamina submit
- no final/lock
- no Source modification by Codex

## Source Update Recommendation

Do not update official Source in K153.

V1.12 should likely be generated later by ChatGPT after the SPLIT-02 strategy is either tested or abandoned. K153 is planning evidence only, not official Source.

## Safety

- Dreamina was not run.
- No submit/query/download happened.
- No retry/resubmit happened.
- No new media was created.
- No frames/contact sheets/cuts were created.
- No V007 prompt/package was created.
- No final SPLIT-02 prompt/package was created.
- No SHOT-04 prompt/package was created.
- No package JSON/manifest/shot record was created.
- No shot record was modified.
- sources/ was not modified or staged.
- Runtime code was not modified.
- configs/providers.json was not modified.
- Media artifacts were not staged.
- final_master=false
- locked=false
- SHOT-02 / V013 / V018 / V004 / V005 / V006 lock states were not touched.

## Final Verdict

SHOT03_SPLIT02_POSE_KEYFRAME_REFERENCE_PLAN_READY_HUMAN_K154_DECISION_REQUIRED
