# PHASE K168 - SHOT-03 SPLIT02_POSE_KF_01 R02 Prompt Audit

## Purpose

Audit the `SPLIT02_POSE_KF_01_R02_identity_repair` standalone prompt draft and reference-duty map created in K167.

This phase decides whether the R02 identity repair prompt is ready for later no-submit package planning. It does not create package files, media, or any Dreamina task.

## Files Inspected

| File | Status | Size Bytes |
|---|---:|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K167_SHOT03_SPLIT02_POSE_KF_R02_IDENTITY_REPAIR_PROMPT_DRAFT.md` | exists | 13072 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_R02_identity_repair_DRAFT_prompt.txt` | exists | 2940 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K166_SHOT03_SPLIT02_POSE_KF_IDENTITY_LOCK_REPAIR_PLAN.md` | exists | 11502 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md` | exists | 4581 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K164_SHOT03_SPLIT02_POSE_KF_DOWNLOAD_READY.md` | exists | 5998 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K160_SHOT03_SPLIT02_POSE_KF_PACKAGE_REVIEW.md` | exists | 11275 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md` | exists | 10075 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md` | exists | 9151 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md` | exists | 14850 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md` | exists | 10469 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md` | exists | 27677 |

## Source Governance Confirmation

- `sources/` was read-only reference material.
- `git status --short -- sources/` returned clean.
- No file under `sources/` was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Official Source update requires ChatGPT generation/review and human manual action.
- Any Source update recommendation in this report is evidence only, not official Source.

## K167 Carry-Forward

- K167 created the R02 standalone repair prompt file.
- K167 prompt SHA256: `47739cb33850d2d692ee13479dde8c13822acab34bc6ff94f55c4ecec06de853`.
- The R02 primary route is a 3-ref identity-priority route.
- K167 did not run Dreamina.
- K167 did not create media, package JSON, manifest CSV, or shot record JSON.
- `final_master=false`.
- `locked=false`.

## Prompt File Validation

| Field | Value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_R02_identity_repair_DRAFT_prompt.txt` |
| exists | true |
| size_bytes | 2940 |
| sha256 | `47739cb33850d2d692ee13479dde8c13822acab34bc6ff94f55c4ecec06de853` |
| sha256_matches_expected | true |
| encoding | UTF-8 readable |
| status | `DRAFT_ONLY_NOT_FOR_SUBMIT` |
| final status | `NOT_FINAL` |
| package status | `NOT_PACKAGE` |
| audit requirement | `REQUIRES_HUMAN_CHATGPT_AUDIT_BEFORE_PACKAGE` |

Prompt validation result: pass.

## Reference Validation

| Label | Path | Exists | Duty | Include In R02 Primary Package | K168 Audit Note |
|---|---|---:|---|---:|---|
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | true | highest-priority identity-only | true | Correct primary anchor for repairing the K165 Shuangji identity failure. SHA256 `fbc0e674e19d74c9ba4b8488e2c4da79f0a415e1c6811d0613803150bd9bad1d`. |
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | true | identity-only | true | Correct identity anchor for keeping Fenshou as the left-side black-red male pressure role. SHA256 `70c01dec0bc3aa0eadd9f554c731be4991320b742cb2f9a2f1195a0d4f08bed3`. |
| `@K164_FAILED_IMAGE_COMPOSITION_ONLY` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/83628bbc-88bc-4c04-9e7c-11697c84fd95_image_1.png` | true | corridor / column / close-contact composition only, explicitly not identity | true | Correctly demoted from failed output to composition/action-only evidence. SHA256 `d328bc4fb0e8f630925d9d9508ecb1394b55de023313900ec50ba2e4e4fa9284`. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | true | optional scene/world only | false | Keep excluded from primary R02 to reduce reference overload; use only as fallback if the 3-ref route loses corridor environment. SHA256 `f2117d0ac806179dd2ac5f009d3483184b500ba2489512894059379c73bc531b`. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | true | review/context only | false | Exclude from primary R02 because it is video-derived and may reintroduce identity ambiguity. SHA256 `9d4dd30aa7f0ed707db1b1219f34db7d51e8998f3d4893acbf33214f6b81e1bb`. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | true | review/context only | false | Exclude from primary R02 because return continuity is less important than identity repair. SHA256 `14b2451e2cc45cc18510817f772fbf2f86c8c02c8f717902fd8807a459bfde37`. |

Reference validation result: pass.

## Reference-Duty Audit

- `@SHUANGJI_IDENTITY_REF` is highest-priority identity-only.
- `@FENSHOU_IDENTITY_REF` is identity-only.
- `@K164_FAILED_IMAGE_COMPOSITION_ONLY` is composition/action-only and explicitly not an identity reference.
- `@V004_CORRIDOR_SCENE_REF` is optional fallback scene/world only and excluded from the primary R02 route.
- `@SPLIT02_START_ANCHOR_CUT_B_START_03` and `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` are review/context-only and excluded from the primary R02 route.
- The failed R01/K164 output is not used as an approved keyframe and not used as an identity reference.

Reference-duty audit result: pass.

## Prompt Audit

### Positives

- Directly addresses the K165 failure: Shuangji identity failed while composition was partially useful.
- Explicitly prevents copying failed R01 male-coded cues: face, jaw, neck, shoulder shape, body language, and masculine / androgynous identity signals.
- Strengthens female-coded Shuangji face, neck, shoulder silhouette, body frame, hair, and costume language.
- Prevents character swap and duplicate characters.
- Keeps Fenshou as the left-side black-red male pressure role.
- Keeps the column as obstacle / partial occluder only.
- Keeps no jump, parkour, roof, stairs, eaves, or wall-run.
- Keeps no architecture breakage, debris, water shield, shockwave, or smoke explosion.
- States that the output is a single static keyframe, not a video.

### Concerns

- The prompt may overcorrect toward beauty/portrait identity if Shuangji identity language dominates the action language.
- Combat pressure may weaken if the model treats Shuangji identity repair as the main goal and de-emphasizes guard compression.
- The 3-ref route may lose corridor material detail without the V004 scene/world reference.
- Close-contact arms beside a column remain a body-fusion and extra-limb risk.
- Column partial occlusion may still hide Shuangji's face or reduce identity readability despite prompt constraints.

Prompt audit result: approved for no-submit package planning, not approved for submit.

## Risk Audit

| Risk | Mitigation In K167 Prompt / Reference Map | Remaining Concern |
|---|---|---|
| Shuangji still masculinized | Highest-priority Shuangji identity ref; explicit female-coded face, slimmer neck, narrower shoulders, lighter body frame; forbids masculine / androgynous identity cues | K164 composition-only image may still leak broad shoulder / male-coded pressure posture into the right-side figure |
| Shuangji over-beautified / too portrait-like | Keeps action as guard compression beside the column and preserves close physical engagement | Identity repair wording may pull the model toward a posed beauty image instead of combat pressure |
| Combat pressure weakened | Prompt says Fenshou presses into Shuangji's raised guard and Shuangji resists beside the column | Still-image generation may flatten the beat into static posing or soft contact |
| Corridor detail drift | K164 failed image carries corridor / column / close-contact layout; prompt restates rainy exterior ancient temple corridor | Without V004 scene/world ref, material language and exact corridor continuity may soften |
| R01 identity leakage | Failed R01/K164 image is composition-only and prompt forbids copying its failed face, jaw, neck, shoulder shape, body language, and masculine cues | Because the failed image remains a generation ref, leakage risk is reduced but not removed |
| Body fusion / extra limbs | Prompt forbids body fusion, extra limbs, duplicates, and keeps both fighters distinct | Close forearm compression and column overlap are inherently high risk |
| Column over-occlusion | Prompt permits only narrow partial occlusion and says the column must not hide Shuangji's face or erase identity | Model may still place the face behind the column if composition dominates |
| Identity swap / duplication | Prompt fixes Fenshou left and Shuangji right; forbids swap and duplication | Two-character composition remains vulnerable if refs conflict |
| Architecture damage hallucination | Prompt forbids railing/door/lattice/wall/column breakage, cracks, debris, splinters, shockwave, shields, smoke explosion, and destruction | Corridor pressure may still introduce small unintended debris unless checked in later package review |

## K168 Decision

| Field | Value |
|---|---|
| prompt_audit_status | `approved_for_no_submit_package_planning` |
| recommended_primary_package_route | `3_ref_identity_priority` |
| fallback_package_route | `4_ref_with_V004_scene_world_if_environment_drifts` |
| submit_allowed | false |
| package_creation_allowed | `false_in_K168` |
| final_master | false |
| locked | false |

K168 decision: `R02_PROMPT_AUDIT_PASS_READY_FOR_K169_NO_SUBMIT_PACKAGE_PLANNING`.

## Recommended Next Phase

Recommend K169: create no-submit R02 image2image package files using the 3-ref identity-priority route:

- `@SHUANGJI_IDENTITY_REF`
- `@FENSHOU_IDENTITY_REF`
- `@K164_FAILED_IMAGE_COMPOSITION_ONLY`

K169 may create package JSON, manifest CSV, and package report. K169 must not submit. K169 must not create media. K169 should preserve the fallback 4-ref strategy with `@V004_CORRIDOR_SCENE_REF` only if the human later requests it.

## Alternative Next Phase

If the human rejects the R02 repair risk:

- `K169_ALT`: plan direct `CUT_B -> CUT_C` edit continuity without another generated repair keyframe.
- `K169_ALT`: create 4-ref package planning with `@V004_CORRIDOR_SCENE_REF` included as scene/world fallback.
- No submit in either alternative.

## What Not To Do

- Do not run Dreamina.
- Do not submit/query/download.
- Do not create package files in K168.
- Do not create media.
- Do not mark final.
- Do not lock.
- Do not modify Source.
- Do not treat the K164 failed image as an identity reference.
- Do not repeat the original 5-ref package unchanged without explicit human direction.

## Source Update Recommendation

Do not update official Source in K168.

Candidate future Source note: after a failed generated keyframe, if composition is useful but identity fails, demote the failed output to composition-only, strengthen identity anchors, reduce reference overload, and explicitly forbid copying failed identity cues.

## Safety

- No Dreamina command was run.
- No submit/query/download occurred.
- No retry/resubmit occurred.
- No media was created.
- No media was staged.
- No package JSON was created.
- No manifest CSV was created.
- No prompt txt was created or modified in K168.
- No shot record JSON was created or modified.
- `sources/` was untouched.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `final_master=false`.
- `locked=false`.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_R02_PROMPT_AUDIT_PASS_READY_HUMAN_K169_PACKAGE_DECISION`
