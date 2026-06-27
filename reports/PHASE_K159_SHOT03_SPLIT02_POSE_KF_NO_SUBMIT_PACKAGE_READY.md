# PHASE K159 - SHOT-03 SPLIT-02 Pose Keyframe No-Submit Package Ready

## 1. Purpose

Create no-submit image2image package files for `SPLIT02_POSE_KF_01_column_edge_guard_compression`.

This phase creates one package JSON, one manifest CSV, and this K159 report. It does not run Dreamina, does not submit, does not query/download, does not generate media, and does not create or modify any shot record.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K158_SHOT03_SPLIT02_POSE_KF_PACKAGE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K157_SHOT03_SPLIT02_POSE_KF_PROMPT_AUDIT_READY_FOR_PACKAGE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K156_SHOT03_SPLIT02_POSE_KF_STANDALONE_PROMPT_DRAFT_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

## 3. Source Governance Confirmation

- `sources/` was read-only reference material.
- No `sources/` file was created, edited, renamed, moved, deleted, staged, committed, or pushed.
- Official Source updates require ChatGPT generation/review and human manual action.
- K159 creates package metadata only and does not update official Source.

## 4. Prompt Validation

| field | value |
|---|---|
| prompt_path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` |
| exists | yes |
| size_bytes | 1933 |
| sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| expected_sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| sha256_matches_expected | true |
| status | draft_only_not_for_submit / not_final / not_submit_ready |

## 5. Reference Validation

| label | path | exists | duty | include_in_primary_package | K159 notes |
|---|---|---:|---|---:|---|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | yes | Fenshou identity only | true | Identity anchor only; does not define pose/camera. |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | yes | Shuangji highest-priority identity only | true | Must override video-frame softness for identity protection. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | yes | scene/world only | true | Scene/world material and rainy temple mood only. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | yes | start continuity/composition only | true | Incoming corridor-combat pressure anchor; not identity reference. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | yes | return continuity/composition only | true | Primary package includes it; fallback removes it if K160 sees overload risk. |

## 6. Package Files Created

| file | path | exists | size_bytes | sha256 |
|---|---|---:|---:|---|
| package_json | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_split02_pose_kf_01_image2image_package_no_submit.json` | yes | 5179 | `6e7da5ca561b51280b2a2eaeebf034758348346f1c1125ce61f08ce1a23ba78c` |
| manifest_csv | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_SPLIT02_POSE_KF_01_no_submit.csv` | yes | 1488 | `d32ad8f0ef5827b584c27910acfbd9436d0e714867032539070f5cdf1ae75375` |
| report | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K159_SHOT03_SPLIT02_POSE_KF_NO_SUBMIT_PACKAGE_READY.md` | yes | 9065 before self-reference cleanup | self-hash not recorded in body to avoid unstable self-reference |

## 7. Package Summary

- `task_type=image2image`
- `model_version=4.7`
- `ratio=16:9`
- `resolution_type=2k`
- `refs_count=5`
- `submit_allowed=false`
- `final_master=false`
- `locked=false`
- `package_status=package_ready_no_submit_pending_K160_review`
- `human_submit_authorization_required=true`
- `k160_package_review_required=true`

## 8. Fallback Package Strategy

If K160 judges the five-reference package overloaded, remove `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` from the image refs and keep it as review/planning reference only.

Do not create the fallback package unless the human later authorizes that change.

## 9. Clause-Level Package Compliance

| requirement | K159 result | status |
|---|---|---|
| image2image uses still-image package, not video | Package declares `task_type=image2image`; no video duration or video_resolution fields. | pass |
| image2image refs count within supported range | Primary package uses 5 refs; local Source/help allows repeated `--images` and image2image multiple refs. | pass |
| identity refs separated from continuity anchors | Package reference duties separate identity-only refs from start/return anchors. | pass |
| video-derived frames are continuity/composition only | CUT_B_START_03 and CUT_C_RETURN_01 are marked continuity/composition only. | pass |
| scene ref is scene/world only | Temple scene ref is marked scene/world only. | pass |
| no Dreamina submit | No Dreamina command was run. | pass |
| no final/lock | `final_master=false`, `locked=false`. | pass |
| no Source modification | `sources/` remained read-only and unstaged. | pass |

## 10. Risk Register

| risk | K160 review note |
|---|---|
| 5 refs may overload model | Check if return anchor should be dropped before any submit authorization. |
| Body fusion due to close contact | Review prompt/reference duties for readable body separation. |
| Column over-occlusion | Ensure column only hides a small part of overlapping arms/torso, not faces or full bodies. |
| Identity drift | Confirm identity refs are highest-priority for character identity, especially Shuangji. |
| Courtyard/corridor drift | Confirm V004 anchors preserve corridor composition while scene ref provides world/material support only. |
| Accidental architecture damage | Confirm prompt and package forbid breakage, cracks, splinters, broken boards, and structural damage. |
| Column-base stepping | Confirm no prompt/ref language encourages foot-on-column-base or random stone stepping. |
| Keyframe may be too ordinary | Accept subtle result only if it improves edit continuity and shows column-edge compression clearly enough. |

## 11. Recommended Next Phase

Recommend K160 independent package review, no submit.

K160 should check:

- package files exist
- package JSON valid
- manifest CSV valid
- prompt sha256
- ref path existence
- Source-governance boundaries
- no-submit status
- whether five-reference primary package is acceptable or fallback four-reference route is preferred

## 12. What Not To Do

- no Dreamina
- no submit/query/download
- no final/lock
- no prompt-only V007
- no full 5s terrain force-chain
- no Source modification by Codex

## 13. Source Update Recommendation

Do not update official Source in K159.

V1.12 should wait until SPLIT-02 is tested or abandoned. K159 is evidence for later Source discussion, not official Source.

## 14. Safety

- no Dreamina
- no submit/query/download
- no retry/resubmit
- no media created
- no frames/contact sheets/cuts created
- package JSON created no-submit
- manifest CSV created no-submit
- no shot record created/modified
- `sources/` not modified/staged
- runtime/config not modified
- media artifacts not staged
- `final_master=false`
- `locked=false`

## 15. Final Verdict

SHOT03_SPLIT02_POSE_KF_NO_SUBMIT_IMAGE2IMAGE_PACKAGE_READY_PENDING_K160_REVIEW
