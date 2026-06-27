# PHASE K154 - SHOT-03 SPLIT-02 Pose Keyframe Prompt Draft and Reference Map

## 1. Purpose

Create a text-only draft prompt and reference-duty map for the future intermediate still keyframe:

`SPLIT02_POSE_KF_01_column_edge_guard_compression`

This report is planning evidence only. It does not create a standalone prompt file, package JSON, manifest, shot record, media file, or Dreamina task.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K153_SHOT03_SPLIT02_POSE_KEYFRAME_REFERENCE_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K151_SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K149_SHOT03_BASELINE_CANDIDATE_STATE_RECORD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K148_SHOT03_V004_CUT_CANDIDATE_SELECTION_RECORDED.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K146_SHOT03_V004_CUT_CANDIDATES_CREATED.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

## 3. Source Governance Confirmation

- `sources/` was read only.
- No official Source file was created, edited, moved, deleted, staged, committed, or pushed.
- This K154 report is evidence and draft planning only, not official Source.
- Any future official Source update still requires ChatGPT generation/review and human manual application.

## 4. Corrected K152 Selection Note

Recorded corrected wording:

`纭 K152锛歱rimary start = CUT_B_START_03锛宐ackup start = CUT_B_START_04锛沺rimary return = CUT_C_RETURN_01锛宐ackup return = CUT_C_RETURN_04/05锛汻ETURN_02/03 rejected锛涜繘鍏?K153 pose/keyframe reference plan銆?`

K153 is preserved as-is and was not edited in this phase.

## 5. Current Continuity Anchors

- Current SHOT-03 baseline candidate: V004 CUT_B style corridor combat.
- SPLIT-02 micro-goal: column-edge guard compression plus brief occlusion.
- Physical job: two fighters stay in the exterior temple corridor. Fenshou pressures Shuangji's guard line toward a wooden column edge. Forearms and shoulders compress briefly as the column partially occludes the body line. Both remain engaged and ready to exit back into close combat.
- This is not a foot-on-column attack, not a wall-run, not a parkour insert, and not structural breakage.

## 6. Frame Candidate Inventory for Selected Anchors

| candidate_id | path | exists | role | future usage note |
|---|---|---:|---|---|
| CUT_B_START_03 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | yes | primary SPLIT-02 start anchor | Continuity/composition reference only. Do not use as identity source. |
| CUT_B_START_04 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_04_t2p00.jpg` | yes | backup SPLIT-02 start anchor | Backup timing if START_03 feels too early. Do not use as identity source. |
| CUT_C_RETURN_01 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | yes | primary return anchor | Return-continuity target after the inserted terrain beat. |
| CUT_C_RETURN_04 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_04_t0p60.jpg` | yes | backup return anchor | Backup return if RETURN_01 is too abrupt. |
| CUT_C_RETURN_05 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_05_t0p80.jpg` | yes | backup return anchor | Later backup return, likely more settled. |

## 7. Reference-Duty Map

| label | source path / type | future duty | must preserve | must not copy/change | required now/later | risk notes |
|---|---|---|---|---|---|---|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` / upload-safe identity image | Fenshou identity-only reference | black-red heavy costume language, male-coded body mass, armor silhouette, hair/face consistency | Must not dictate exact pose, corridor geometry, or camera angle | Later, if a keyframe package is authorized | Video frames are too soft for identity protection; use this as the clean identity anchor. |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` / upload-safe identity image | Shuangji highest-priority identity-only reference | female-coded face, blue-white/silver costume language, hair shape, slimmer silhouette | Must not become male-coded, swapped with Fenshou, duplicated, or copied as the whole scene | Later, if a keyframe package is authorized | Highest drift risk. This reference should override video-frame softness. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` / upload-safe scene/world image | Scene/world continuity only | rainy ancient temple mood, wet stone, wooden architecture, exterior corridor plausibility | Must not become courtyard shockwave scene, roof scene, stairs scene, or modern environment | Later, if a package needs scene support | Scene anchor helps avoid drifting away from the V004 corridor style, but should not override action composition. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` / video-derived frame | Primary continuity/composition start anchor | V004-like corridor combat spacing, engaged fighters, camera continuity | Must not be used as identity source; do not preserve blur/artifacts as character truth | Now for planning, later for keyframe reference if approved | Useful for timeline continuity, not for identity lock. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` / video-derived frame | Return continuity target | Close-combat exit direction and corridor energy after insert | Must not force a static end pose or identity details | Now for planning, later for edit/return matching | The pose keyframe should remain compatible with returning to this frame family. |
| `@SPLIT02_POSE_KF_01_DRAFT` | This K154 report only / draft text | Future intermediate pose keyframe concept | column-edge guard compression, partial occlusion, engaged forearm/shoulder pressure | Must not become a submitted prompt, package, final keyframe, locked ref, or production asset in K154 | Draft now; possible K155 ChatGPT/human audit next | Draft is intentionally non-final and must be audited before any package creation. |

## 8. Draft Keyframe Prompt

Status markers:

- `DRAFT_ONLY_NOT_FOR_SUBMIT`
- `NOT_FINAL`
- `REQUIRES_CHATGPT_AND_HUMAN_AUDIT`

```text
SPLIT02_POSE_KF_01_column_edge_guard_compression銆傜敾闈腑涓嶈鍑虹幇浠讳綍鏂囧瓧銆佺紪鍙锋垨鏍囪瘑銆?

这是一个单张静态关键帧，不是视频。保持 SHOT-03 V004 风格的雨中古寺外廊近身战斗，湿石板地面、木质廊柱、栏杆、屋檐雨线和冷灰蓝雨光保持一致。画面为中景或中远景，正面略斜的外廊构图，人物全身或大半身可读，不要切成拳头或脸部大特写。

画面核心是“廊柱边缘护架压缩”。木质廊柱位于画面中央附近或前景/中景边缘，柱子只形成短暂半身遮挡和空间压迫，不要变成跳跃道具。焚狩在左侧或左前方，黑红重甲与深色长发保持稳定，身体低重心前压，肩膀和右前臂向霜玑的中线施压。霜玑在右侧或右后方，蓝白/银色服装、女性脸部结构、长发和较轻身形保持稳定，双臂护架被压到廊柱边缘附近，前臂和肩线明显承受压力。

两人的前臂、肩膀、胸廓和脚步必须仍然处在真实接触受力中。焚狩的后脚踩在湿石板上发力，膝盖微屈，腰胯带肩向前压；霜玑的支撑脚短滑，身体侧旋卸力，护架被撞开一小段但没有失去战斗姿态。接触点要有明确身体结果：护架压缩、肩线偏移、躯干轻微扭转、脚下湿石板小水花和滑痕。

廊柱只遮住两人身体的一小部分，用来制造空间窄迫感和短暂视觉遮挡。不要让人物消失在柱子后面，不要让柱子完全挡住脸或关键动作。两人脸部以中景可读的 3/4 侧脸为主，焚狩和霜玑的脸部结构、发型和服装语言必须稳定一致。

画面要像即将插入 CUT_B_START_03 与 CUT_C_RETURN_01 之间的中间动作关键帧：仍然是连续近身交手，不是摆拍，不是回合制停顿，不是镜头结束姿势。两人保持紧张接触，并且能够自然衔接回后续外廊近身战斗。

限制：不要脚踩柱基，不要随机石块，不要跳跃，不要滞空，不要跑酷展示，不要上屋顶，不要楼梯，不要檐口动作，不要飞身踢，不要完整绕柱，不要大范围换边。不要栏杆断裂，不要门窗破裂，不要墙体破洞，不要木屑飞溅，不要结构裂缝，不要建筑自发损坏。不要第二次爆炸，不要巨大球形冲击波，不要圆形水幕，不要护盾罩。不要现代城市，不要第三人，不要重复角色，不要融合身体，不要多余肢体，不要武器，不要文字水印。
```

## 9. Draft Prompt Risk Audit

| risk | why it matters | mitigation in draft | remaining concern |
|---|---|---|---|
| Column becomes a jump/parkour prop | SPLIT-02 must be column-edge compression, not terrain acrobatics | Explicitly says no foot-on-column-base, no jump, no hangtime, no parkour, no roof/stairs/eaves | Needs ChatGPT/human audit to ensure wording does not over-invite terrain spectacle. |
| Static pose showcase | A still keyframe can become poster-like and freeze action energy | Says this must bridge CUT_B_START_03 to CUT_C_RETURN_01 and remain engaged contact | Still-frame generation may favor beauty-pose; package should later use action-result wording strongly. |
| Structural damage hallucination | V005/V006 experiments showed terrain ambitions can cause wrong damage | Explicitly forbids cracks, debris, splinters, railing/door/window breakage, self-damage | If future prompt says "compression" too dramatically, model may invent damage. |
| Identity drift, especially Shuangji | Video frames are soft and V011/V012 history showed identity instability | Reference-duty map makes Shuangji identity anchor highest priority and forbids male-coding | Future package must actually include identity refs and not rely on video frames alone. |
| Column occludes too much | Brief occlusion is desired, but not lost action | Draft says column only partially blocks a small body portion and must not hide faces/key motion | Needs human visual review if generated. |
| Overloaded single frame | Too many physical requirements can make anatomy messy | Draft limits to one micro-goal: forearm/shoulder guard compression at column edge | Future K155 can simplify wording if needed. |

## 10. Clause-Level Source Compliance Map

| source / planning rule | required behavior | draft prompt clause | status | improvement needed |
|---|---|---|---|---|
| Source governance V0.1 | Sources read-only; drafts are reports, not official Source | This report states source governance and no Source modification | present | None for K154. |
| K150/K153 micro-goal | Single terrain insert: column-edge guard compression plus brief occlusion | "画面核心是...廊柱边缘护架压缩" | present | K155 can decide if "terrain insert" should be even smaller. |
| K151 continuity anchors | Use CUT_B_START_03 as start, CUT_C_RETURN_01 as return | Prompt says it inserts between those frame families | present | Future package should include both as continuity refs, not identity refs. |
| V1.11 contact-result rule | Contact must show body result, not soft push | Prompt requires guard compression, shoulder shift, torso twist, foot skid | present | Later video prompt may need timing and repeated beats; still keyframe only needs one clear result. |
| V1.2 physical force chain | Foot/knee/hip/shoulder/forearm chain should be visible | Prompt names back foot, bent knee, waist/hip driving shoulder, forearm pressure | present | Could be shortened in final audited prompt if too verbose. |
| No slow pose / no static standoff | The still must imply active continuous combat | Prompt says not poster, not turn-based pause, not end pose | present | Visual output still requires review because a keyframe can always read posed. |
| No foot-on-column-base / no parkour | SPLIT-02 should not repeat rejected V005 terrain ambiguity | Hard negative block bans foot-on-column-base, jumping, hangtime, parkour, roof/stairs/eaves | present | This is intentionally conservative. |
| No structural breakage | Column/railing must not crack or break | Hard negative block bans cracks, debris, splinters, broken railing/doors/windows/walls | present | Future SHOT-04 can handle breakage separately. |
| Face/identity stability | Fenshou and Shuangji must remain readable and distinct | Prompt states Fenshou black-red and Shuangji blue-white/silver female-coded structure | present | Identity references must be included if the draft becomes a package. |
| Reference-duty separation | Identity refs must not be confused with scene/action refs | Reference-duty map separates identity, scene, start anchor, return anchor | present | Future package must preserve this exact separation. |

## 11. Future Route Discussion

Recommended sequence:

1. K155: human + ChatGPT audit of this draft prompt and reference-duty map.
2. K156: possible actual prompt file or package planning only, if human approves the K155 audit direction.
3. Later: image2image may create the intermediate still pose keyframe only after prompt/package approval.
4. Later still: frames2video or multimodal2video may test the SPLIT-02 insert only after the keyframe exists and its package is approved.

Alternative route:

- If human rejects the SPLIT-02 risk, plan a direct CUT_B to CUT_C edit continuity route and defer terrain insert exploration.

## 12. Recommended Next Phase

K155 should be a human + ChatGPT audit/refinement phase. It should remain text-only unless the human explicitly authorizes creation of a standalone prompt file or package.

## 13. What Not To Do

- Do not run Dreamina.
- Do not submit, query, download, retry, resubmit, or batch.
- Do not create media, frames, contact sheets, cut MP4s, or generated images.
- Do not create a standalone prompt txt/json in K154.
- Do not create a package, manifest, or shot record in K154.
- Do not modify `sources/`, runtime code, or `configs/providers.json`.
- Do not mark final master.
- Do not lock.

## 14. Source Update Recommendation

No official Source update is recommended in K154. Any V1.12 Source update should wait until the SPLIT-02 keyframe route is tested or abandoned, and must follow the Source governance rule: ChatGPT/human-controlled official Source only.

## 15. Safety

- Dreamina was not run.
- No submit/query/download happened.
- No media was generated.
- No prompt/package/manifest/shot-record file was created.
- `sources/` remained read-only and unstaged.
- `final_master=false`.
- `locked=false`.
- Human and ChatGPT audit required before any package or generation step.

## 16. Final Verdict

SHOT03_SPLIT02_POSE_KF_PROMPT_DRAFT_AND_REFERENCE_MAP_READY_HUMAN_CHATGPT_AUDIT_REQUIRED
