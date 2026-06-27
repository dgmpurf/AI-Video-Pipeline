# PHASE K157 - SHOT-03 SPLIT-02 Pose Keyframe Prompt Audit Ready for Package Planning

## 1. Purpose

Audit the K156 standalone draft prompt and reference-duty map for:

`SPLIT02_POSE_KF_01_column_edge_guard_compression`

This phase records the ChatGPT audit direction and human route status. It does not create a package, manifest, shot record, media artifact, or Dreamina task.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K156_SHOT03_SPLIT02_POSE_KF_STANDALONE_PROMPT_DRAFT_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt`
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
- K157 creates one audit report only.

## 4. Prompt File Validation

| field | value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` |
| exists | yes |
| size_bytes | 1933 |
| sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| expected_sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| sha256_matches_expected | true |
| encoding | UTF-8 readable; ASCII-safe first line verified |
| status from K156 | `DRAFT_ONLY_NOT_FOR_SUBMIT`; `NOT_FINAL`; `REQUIRES_HUMAN_CHATGPT_APPROVAL_BEFORE_PACKAGE_OR_DREAMINA` |

The K156 prompt body is clean enough for the next planning step. It remains draft-only and not submit-ready.

## 5. Reference Validation

| logical label | path | exists | intended duty | K157 audit note |
|---|---|---:|---|---|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | yes | Fenshou identity-only | Keep as identity anchor only. Do not use it to define pose, camera, or corridor geometry. |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | yes | Shuangji highest-priority identity-only | Required if future package planning proceeds. Do not let video-derived frames override Shuangji identity. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | yes | scene/world only | Use for rainy temple world continuity only, not identity or action mechanics. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | yes | start continuity/composition anchor | Use as incoming V004 corridor-combat pressure reference only. Not identity reference. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | yes | return continuity/composition anchor | Use as return target after the insert. Not identity reference. |

## 6. K157 ChatGPT Audit Summary

1. K156 fixed the major K154/K155 mojibake issue in the standalone prompt body by using an ASCII-safe first line.
2. K156 reduced foot/skid/force-chain emphasis and avoided reintroducing V005/V006 terrain-trigger failure patterns.
3. The prompt correctly keeps the micro-goal narrow: column-edge guard compression plus brief occlusion.
4. The column is correctly described as obstacle/partial occluder only.
5. The prompt correctly avoids foot-on-column-base, random stone stepping, jump/hangtime/parkour, roof/stairs/eaves route, wall-run, architecture breakage, shockwave, water shield, and smoke explosion.
6. Remaining risk: the generated keyframe may be too subtle or ordinary, but that is acceptable for a low-risk SPLIT-02 insert.
7. Remaining risk: close overlapping arms may still produce anatomy or body-fusion issues, so future package review must preserve readable body separation.

## 7. Audit Decision

- `prompt_audit_status=approved_for_package_planning_not_for_submit`
- `final_master=false`
- `locked=false`
- `submit_allowed=false`
- `package_creation_allowed=false_in_K157`
- `next_phase=K158_package_planning_only`

The K156 standalone draft prompt is approved for K158 package planning only. It is not final, not locked, and not submit-ready.

## 8. Remaining Risks

| risk | note for K158 |
|---|---|
| Action may become poster pose | Package planning should keep the keyframe as a middle contact beat between CUT_B_START_03 and CUT_C_RETURN_01. |
| Close contact may create body fusion | Future package review must require readable body separation and avoid over-overlapping limbs. |
| Column may over-occlude bodies | Column should hide only a small part of arms/torso, not faces or the full contact relationship. |
| Generated result may be too ordinary | Acceptable if it safely bridges the edit; reject only if it fails the column-edge compression purpose. |
| Identity drift remains possible without proper identity refs | K158 must preserve identity refs as identity-only and include Shuangji identity as high priority if package planning proceeds. |
| Package must not become full 5s terrain force-chain | K158 should stay keyframe/package planning only, not a video choreography package. |

## 9. K158 Recommendation

Recommend K158:

Create a package-planning report only for `SPLIT02_POSE_KF_01`.

K158 should decide task_type candidate and package structure, but still no Dreamina unless separately authorized.

K158 may prepare a package plan, not submit. K158 should likely consider image2image keyframe generation using identity refs plus scene/world ref plus start/return anchors, but only as planning.

## 10. What Not To Do

- no Dreamina
- no submit/query/download
- no final/lock
- no prompt-only V007
- no full 5s terrain force-chain
- no Source modification by Codex

## 11. Source Update Recommendation

Do not update official Source in K157.

V1.12 should wait until SPLIT-02 is tested or abandoned. K157 is evidence for later Source discussion, not official Source.

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

SHOT03_SPLIT02_POSE_KF_PROMPT_AUDITED_APPROVED_FOR_PACKAGE_PLANNING_NOT_SUBMIT_READY_FOR_K158
