# PHASE K166 - SHOT-03 SPLIT02_POSE_KF_01 Identity-Lock Repair Plan

## Purpose

Plan identity-lock repair after K165 failed Shuangji identity for `SPLIT02_POSE_KF_01_column_edge_guard_compression`.

This phase is text-only planning. It does not create media, prompt files, package JSON, manifest CSV, shot records, or Dreamina tasks.

## Files Inspected

| File | Status | Size Bytes |
|---|---:|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md` | exists | 4581 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K164_SHOT03_SPLIT02_POSE_KF_DOWNLOAD_READY.md` | exists | 5998 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K163_SHOT03_SPLIT02_POSE_KF_QUERY_STATUS.md` | exists | 5245 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K162R_SHOT03_SPLIT02_POSE_KF_SUBMIT_RESULT.md` | exists | 7789 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K160_SHOT03_SPLIT02_POSE_KF_PACKAGE_REVIEW.md` | exists | 11275 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K158_SHOT03_SPLIT02_POSE_KF_PACKAGE_PLANNING.md` | exists | 12040 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K156_SHOT03_SPLIT02_POSE_KF_STANDALONE_PROMPT_DRAFT_READY.md` | exists | 11723 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_column_edge_guard_compression_DRAFT_prompt.txt` | exists | 1933 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md` | exists | 10075 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md` | exists | 9151 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md` | exists | 14850 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md` | exists | 10469 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md` | exists | 27677 |

## Source Governance Confirmation

- `sources/` was read-only.
- `git status --short -- sources/` returned clean.
- No `sources/` file was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Official Source update requires ChatGPT generation/review and human manual action.

## K165 Carry-Forward

Exact human review line:

> 女性人物没锁定

K165 decision carried forward:

- `visual_status=failed_identity_lock`
- `composition_status=partially_useful`
- `action_status=partially_useful_but_static`
- `shuangji_identity_status=failed`
- `usable_as_final=false`
- `usable_as_locked_keyframe=false`
- `usable_as_primary_identity_ref=false`
- `usable_as_composition_reference=true`
- `final_master=false`
- `locked=false`

The K164 output may be used only as composition/action evidence. It must not become an identity reference.

## Failed Image Validation

| Field | Value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/83628bbc-88bc-4c04-9e7c-11697c84fd95_image_1.png` |
| exists | true |
| size_bytes | 4285884 |
| sha256 | `d328bc4fb0e8f630925d9d9508ecb1394b55de023313900ec50ba2e4e4fa9284` |
| sha256_matches_K165 | true |
| format | PNG |
| width | 2560 |
| height | 1440 |
| intended future duty | composition/action only |
| identity reference allowed | false |

## Reference Existence Checked

| Reference | Path | Exists | Future Duty |
|---|---|---:|---|
| Fenshou identity | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | true | identity only |
| Shuangji identity | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | true | highest-priority identity only |
| V004 scene/world | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | true | optional scene/world only |
| CUT_B start anchor | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | true | review/context only for first repair |
| CUT_C return anchor | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | true | review/context only for first repair |

## Failure Diagnosis

Likely causes:

- The original 5-ref package may have overloaded identity, scene, start continuity, return continuity, and composition duties.
- Video-derived anchors and two-character close contact likely weakened Shuangji identity priority.
- The prompt identity wording was not strong enough for female-coded Shuangji face, jawline, neck, shoulder silhouette, and body frame.
- Close arm contact, armor compression, and shoulder-forward pose may push Shuangji toward male-coded or androgynous body language.
- Scene/composition succeeded, but identity priority failed.
- The K164 image proves the column-edge compression idea has usable composition value, but it also proves composition success alone is not enough for an approved keyframe.

## Repair Strategy Comparison

| Option | Ref Pack | Expected Value | Risk | Identity-Lock Strength | Composition Preservation Strength | Recommendation |
|---|---|---|---|---|---|---|
| A. 3-ref identity-priority repair | Shuangji identity, Fenshou identity, K164 failed image composition-only | Reduces reference overload and gives Shuangji identity the clearest priority while preserving the failed image's useful corridor/column composition | May lose some exact V004 corridor world continuity | high | medium-high | primary recommended route |
| B. 4-ref repair with one added scene or start anchor | Shuangji identity, Fenshou identity, K164 composition-only, plus either V004 scene/world or CUT_B_START_03 | Adds a safety rail for environment or entry continuity if 3-ref route drifts | Additional reference can again compete with identity priority | medium-high | high | fallback only |
| C. Repeat original 5-ref package unchanged | Original K159/K160 five refs | Would preserve the tested setup | Already failed Shuangji identity; likely repeats the same identity drift | low | high | avoid |
| D. Shuangji-only identity repair precursor | Shuangji identity-focused crop/upper-body/face planning before full two-character keyframe | Could strengthen female-coded identity before returning to contact composition | Adds another phase and may not solve two-character contact | very high for Shuangji alone | low for full keyframe | alternative if two-character repair keeps masculinizing Shuangji |
| E. Abandon SPLIT-02 and direct CUT_B -> CUT_C edit continuity | No new generated keyframe; use existing V004 cut continuity | Avoids further identity drift cost | Loses the desired column-edge compression insert | not applicable | not applicable | fallback strategic exit |

## Recommended Primary Repair Route

Prefer the 3-ref identity-priority repair route:

- `@SHUANGJI_IDENTITY_REF`: highest-priority identity anchor.
- `@FENSHOU_IDENTITY_REF`: identity anchor.
- `@K164_FAILED_IMAGE_COMPOSITION_ONLY`: composition/action reference only.

Exclude from generation refs for the first repair:

- `@V004_CORRIDOR_SCENE_REF`
- `@SPLIT02_START_ANCHOR_CUT_B_START_03`
- `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01`

Keep excluded refs only as review/context references. This route directly addresses the failure mode: composition worked, identity failed. The repair should give Shuangji identity fewer competing visual signals.

## Fallback Repair Route

If the 3-ref route is judged too likely to lose corridor environment, use 4 refs:

- Shuangji identity.
- Fenshou identity.
- K164 failed image composition-only.
- V004 scene/world ref.

The V004 scene/world ref is safer than CUT_B_START_03 for fallback because it carries environment/material language without bringing a second video-derived body/face signal that could again interfere with Shuangji identity. CUT_B_START_03 should remain continuity review context rather than a generation ref unless environment continuity fails badly.

## Revised Prompt Direction

Do not create the final prompt file in K166. Future K167 prompt revision should require:

- Right-side fighter must be Shuangji, an adult female blue-white/silver fighter.
- Preserve feminine facial structure, softer jawline, slimmer neck/shoulder silhouette, lighter body frame.
- Do not masculinize Shuangji.
- Do not turn Shuangji into a male warrior.
- Do not duplicate or swap identities.
- Keep Fenshou as black-red male fighter on the left.
- K164 image supplies only corridor, column, and pressure composition.
- K164 image must not be copied for Shuangji face/body identity.
- Keep the column as obstacle/partial occluder only.
- No column-base stepping.
- No jump, parkour, roof, stairs, or eaves.
- No architecture breakage.

## Reference-Duty Map For Future K167/K168

| Label | Duty |
|---|---|
| `@SHUANGJI_IDENTITY_REF` | highest-priority identity only |
| `@FENSHOU_IDENTITY_REF` | identity only |
| `@K164_FAILED_IMAGE_COMPOSITION_ONLY` | corridor/column/action composition only, not identity |
| optional `@V004_CORRIDOR_SCENE_REF` | scene/world only, maybe excluded from first repair |
| optional `@SPLIT02_START_ANCHOR_CUT_B_START_03` | continuity review only |
| optional `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | continuity review only |

## Recommended Next Phase

Recommend K167: create a revised standalone repair prompt draft and reference-duty map for `SPLIT02_POSE_KF_01_R02_identity_repair`.

K167 should be text-only:

- no package JSON
- no manifest CSV
- no submit
- no Dreamina
- no media

## Alternative Next Phases

- `K167_ALT`: direct `CUT_B -> CUT_C` edit continuity planning if the human wants to stop SPLIT-02 repair.
- `K167_ALT`: Shuangji-only identity/crop repair planning if full two-character repair seems too risky.

## What Not To Do

- Do not use K164 image as approved keyframe.
- Do not use K164 image as primary identity reference.
- Do not proceed to video generation.
- Do not repeat the original 5-ref package unchanged.
- Do not mark final.
- Do not lock.
- Do not update Source in K166.
- Do not run Dreamina.

## Source Update Recommendation

Do not update official Source in K166.

Candidate future Source note: 5-ref image2image may preserve composition but fail female identity lock; identity repair should prioritize character identity refs, reduce reference overload, and demote failed outputs to composition-only evidence.

## Safety

- No Dreamina command was run.
- No submit/query/download occurred.
- No retry/resubmit occurred.
- No media was created.
- No media was staged.
- No package JSON was modified.
- No manifest CSV was modified.
- No prompt txt was modified.
- No shot record JSON was created or modified.
- `sources/` was untouched.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `final_master=false`.
- `locked=false`.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_IDENTITY_LOCK_REPAIR_PLAN_READY_HUMAN_K167_DECISION_REQUIRED`
