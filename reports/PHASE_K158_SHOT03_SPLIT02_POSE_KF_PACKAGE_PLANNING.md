# PHASE K158 - SHOT-03 SPLIT-02 Pose Keyframe Package Planning

## 1. Purpose

Plan the future package structure for `SPLIT02_POSE_KF_01_column_edge_guard_compression` without creating package files or submitting anything.

This phase decides a future task-type candidate and reference-pack structure only. It does not create package JSON, manifest CSV, shot record JSON, media, frames, contact sheets, or Dreamina tasks.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K157_SHOT03_SPLIT02_POSE_KF_PROMPT_AUDIT_READY_FOR_PACKAGE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K156_SHOT03_SPLIT02_POSE_KF_STANDALONE_PROMPT_DRAFT_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K155_SHOT03_SPLIT02_POSE_KF_DRAFT_AUDIT_AND_REFINED_PROMPT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K153_SHOT03_SPLIT02_POSE_KEYFRAME_REFERENCE_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K151_SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md`
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
- K158 creates one package-planning report only.

## 4. K157 Carry-Forward Status

- `prompt_audit_status=approved_for_package_planning_not_for_submit`
- `final_master=false`
- `locked=false`
- `submit_allowed=false`
- Package was not created in K157.
- K158 remains package planning only, not package creation.

## 5. Prompt Validation

| field | value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` |
| exists | yes |
| sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| expected_sha256 | `6b4bb07222a78603dc6bcb587b8e7ecda71605e226b542aff8badb0ec1e73cf8` |
| sha256_matches_expected | true |
| status | `DRAFT_ONLY_NOT_FOR_SUBMIT`; `NOT_FINAL`; `REQUIRES_HUMAN_CHATGPT_APPROVAL_BEFORE_PACKAGE_OR_DREAMINA` |

## 6. Reference Inventory

| label | path | exists | duty | include_in_primary_plan | risk note |
|---|---|---:|---|---:|---|
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | yes | Fenshou identity only | true | Must not define pose/camera; protects black-red male fighter identity. |
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | yes | Shuangji highest-priority identity only | true | Must not be overridden by video-derived frames; prevents gender/identity drift. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | yes | Scene/world only | true | Useful for rainy temple material language, but may bias toward courtyard unless V004 anchors keep corridor composition. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | yes | Start continuity/composition anchor only | true | Video-derived frame is not identity source; use for incoming pressure and corridor placement. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | yes | Return continuity/composition anchor only | true | Useful for edit continuity, but may overload a 5-ref image2image package. |

## 7. Task Type Comparison

| route | expected value | risk | suitable now? | reason |
|---|---|---|---:|---|
| image2image | Best fit for one still keyframe using multiple image refs; local Source/help says image2image uses repeatable `--images`, supports model 4.0-5.0, ratio 16:9, and resolution_type 2k/4k. | Too many refs can overload identity/scene/pose duties; still may produce ordinary or fused body result. | yes | SPLIT02_POSE_KF_01 is a static keyframe, not video. |
| text2image | Can create a still image with no refs. | Weak identity and corridor continuity; likely reintroduces drift. | no | We already have identity refs and V004 continuity anchors; ignoring them is lower quality. |
| frames2video | Can bridge first/last frames into a video. | Wrong phase: we do not yet have the intermediate pose keyframe; frames2video is video generation. | no | K158 is for planning a still keyframe first. |
| multimodal2video | Strong for all-around reference video generation. | Wrong task level now; risks turning the micro-goal into another 5s terrain force-chain. | no | Use only after a keyframe exists and a separate video package is approved. |
| direct edit continuity | Avoids generation risk entirely. | Does not add the intended terrain affordance insert. | fallback only | Use if human rejects SPLIT-02 keyframe risk. |

## 8. Recommended Package Planning Route

Primary route:

- task_type candidate: `image2image`
- output target: one still keyframe, `SPLIT02_POSE_KF_01_column_edge_guard_compression`
- primary ref pack: 5 refs if human accepts the complexity:
  - `@FENSHOU_IDENTITY_REF`
  - `@SHUANGJI_IDENTITY_REF`
  - `@V004_CORRIDOR_SCENE_REF`
  - `@SPLIT02_START_ANCHOR_CUT_B_START_03`
  - `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01`

Fallback route:

- task_type candidate: `image2image`
- fallback ref pack: 4 refs without the return anchor:
  - `@FENSHOU_IDENTITY_REF`
  - `@SHUANGJI_IDENTITY_REF`
  - `@V004_CORRIDOR_SCENE_REF`
  - `@SPLIT02_START_ANCHOR_CUT_B_START_03`
- Keep `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` as planning/review reference only if five refs seem overloaded.

## 9. Proposed Future Package Fields

No actual JSON, CSV, or shot record is created in K158. Proposed fields for a possible K159 no-submit package:

| field | proposed value / note |
|---|---|
| project_name | `chi_yan_tian_qiong` |
| shot_id | `SHOT-03-SPLIT02-POSE-KF-01` or project-approved keyframe id |
| asset_id / keyframe_id | `SPLIT02_POSE_KF_01_column_edge_guard_compression` |
| task_type | `image2image` |
| model_version | `4.7` unless K159 command-help preflight or human direction selects a better current default |
| ratio | `16:9` |
| resolution_type | recommend `2k` for first diagnostic keyframe; consider `4k` only after route is visually validated or if human wants higher detail despite higher cost/risk |
| prompt_path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` |
| images / ref paths | primary 5-ref pack, fallback 4-ref pack as listed above |
| output_dir | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_<timestamp>/` if later submitted |
| output_name | `SPLIT02_POSE_KF_01_column_edge_guard_compression.png` |
| submit_allowed | `false` |
| final_master | `false` |
| locked | `false` |

## 10. Clause-Level Package Compliance

| requirement | K158 planning stance | status |
|---|---|---|
| Identity refs separated from continuity anchors | Fenshou/Shuangji refs are identity-only; CUT_B/CUT_C frames are continuity/composition only. | planned |
| Scene ref is scene/world only | Temple scene ref should not define identity or action mechanics. | planned |
| Video-derived anchors are not identity refs | CUT_B_START_03 and CUT_C_RETURN_01 are not identity sources. | planned |
| image2image is still-image task | Recommended route creates one still keyframe before any video route. | planned |
| No Dreamina submit | K158 does not run Dreamina and recommends K159 no-submit package only. | enforced |
| No package created yet | K158 creates report only. | enforced |
| No final/lock | `final_master=false`, `locked=false`. | enforced |

## 11. Risk Register for Future Package

| risk | mitigation for K159 |
|---|---|
| Too many refs may overload identity/pose/corridor duties | Primary 5-ref route should be reviewed; fallback 4-ref route can omit return anchor from generation refs. |
| Generated keyframe may become ordinary | Treat subtle but readable column-edge compression as acceptable if edit continuity improves. |
| Body fusion / overlapping arms | Package should require readable separation between two bodies and avoid hiding all contact under the column. |
| Column over-occlusion | Column should hide only a small part of overlapping arms/torso, not faces or the whole action. |
| Identity drift | Include identity refs and explicitly mark Shuangji as highest-priority identity anchor. |
| Scene drift to courtyard instead of corridor | Use V004 start/return anchors for corridor composition; scene ref is world/material support only. |
| Unwanted architecture damage | Prompt and package notes must forbid cracks, splinters, broken boards, railing/door/lattice/wall/column breakage. |
| Column base stepping | Keep "no foot-on-column-base" and avoid images or wording that suggest stepping on the column. |
| Accidental action-poster pose | Keep middle-keyframe language: incoming pressure, one compressed beat, ready to return to close combat. |

## 12. Recommended Next Phase

Recommend K159:

Create no-submit image2image package files for `SPLIT02_POSE_KF_01` if human approves K158.

K159 may create:

- prompt package JSON
- manifest CSV row
- planning/package report

K159 must not submit. K159 must keep `submit_allowed=false` and no Dreamina.

## 13. Alternative Next Phase

If human rejects package planning:

- plan direct CUT_B -> CUT_C edit continuity
- defer SPLIT-02 keyframe
- do not create image2image package files

## 14. What Not To Do

- no Dreamina
- no submit/query/download
- no final/lock
- no prompt-only V007
- no full 5s terrain force-chain
- no Source modification by Codex

## 15. Source Update Recommendation

Do not update official Source in K158.

V1.12 should wait until SPLIT-02 is tested or abandoned. K158 is evidence for later Source discussion, not official Source.

## 16. Safety

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

## 17. Final Verdict

SHOT03_SPLIT02_POSE_KF_PACKAGE_PLANNING_READY_HUMAN_K159_DECISION_REQUIRED
