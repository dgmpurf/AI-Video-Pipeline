# PHASE K167 - SHOT-03 SPLIT02_POSE_KF_01 R02 Identity Repair Prompt Draft

## Purpose

Create R02 identity repair standalone prompt draft and reference-duty map for `SPLIT02_POSE_KF_01_R02_identity_repair`.

This is a text-only prompt drafting phase. It does not create a package, manifest, shot record, media, or Dreamina task.

## Files Inspected

| File | Status | Size Bytes |
|---|---:|---:|
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K166_SHOT03_SPLIT02_POSE_KF_IDENTITY_LOCK_REPAIR_PLAN.md` | exists | 11502 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md` | exists | 4581 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K164_SHOT03_SPLIT02_POSE_KF_DOWNLOAD_READY.md` | exists | 5998 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K163_SHOT03_SPLIT02_POSE_KF_QUERY_STATUS.md` | exists | 5245 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K162R_SHOT03_SPLIT02_POSE_KF_SUBMIT_RESULT.md` | exists | 7789 |
| `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K160_SHOT03_SPLIT02_POSE_KF_PACKAGE_REVIEW.md` | exists | 11275 |
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

## K166 Carry-Forward

- R01 failed Shuangji identity.
- Human review line preserved: "女性人物没锁定".
- R01 composition is partially useful.
- R01 is not final.
- R01 is not locked.
- R01 is only a composition/action reference.
- R01 must not be used as a primary identity reference.
- Primary repair route is 3-ref identity-priority.

## Reference Validation

| Label | Path | Exists | SHA256 | Duty | Include In R02 Primary Plan | Notes |
|---|---|---:|---|---|---:|---|
| `@SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | true | `fbc0e674e19d74c9ba4b8488e2c4da79f0a415e1c6811d0613803150bd9bad1d` | highest-priority identity-only | true | Must dominate Shuangji face, silhouette, body frame, hair, and costume language. |
| `@FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | true | `70c01dec0bc3aa0eadd9f554c731be4991320b742cb2f9a2f1195a0d4f08bed3` | identity-only | true | Preserves left-side black-red male fighter identity and pressure role. |
| `@K164_FAILED_IMAGE_COMPOSITION_ONLY` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/83628bbc-88bc-4c04-9e7c-11697c84fd95_image_1.png` | true | `d328bc4fb0e8f630925d9d9508ecb1394b55de023313900ec50ba2e4e4fa9284` | corridor / column / close-contact composition only, explicitly not identity | true | Supplies useful composition but must not supply Shuangji face, jaw, neck, shoulders, or masculine / androgynous cues. |
| `@V004_CORRIDOR_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | true | `f2117d0ac806179dd2ac5f009d3483184b500ba2489512894059379c73bc531b` | optional scene/world only | false | Excluded from primary R02 to reduce reference overload; safer fallback than video-derived body anchors if environment drifts. |
| `@SPLIT02_START_ANCHOR_CUT_B_START_03` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg` | true | `9d4dd30aa7f0ed707db1b1219f34db7d51e8998f3d4893acbf33214f6b81e1bb` | review/context only | false | Excluded from primary R02 because it can reintroduce video-derived identity ambiguity. |
| `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg` | true | `14b2451e2cc45cc18510817f772fbf2f86c8c02c8f717902fd8807a459bfde37` | review/context only | false | Excluded from primary R02 because return continuity is less important than identity repair in this phase. |

## R02 Reference-Duty Map

- `@SHUANGJI_IDENTITY_REF`: highest-priority identity-only.
- `@FENSHOU_IDENTITY_REF`: identity-only.
- `@K164_FAILED_IMAGE_COMPOSITION_ONLY`: corridor / column / close-contact composition only, explicitly not identity.
- `@V004_CORRIDOR_SCENE_REF`: optional fallback scene/world only, excluded from primary R02.
- `@SPLIT02_START_ANCHOR_CUT_B_START_03`: review/context only, excluded from primary R02.
- `@SPLIT02_RETURN_ANCHOR_CUT_C_RETURN_01`: review/context only, excluded from primary R02.

## Prompt File Created

| Field | Value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SPLIT02_POSE_KF_01_R02_identity_repair_DRAFT_prompt.txt` |
| exists | true |
| size_bytes | 2940 |
| sha256 | `47739cb33850d2d692ee13479dde8c13822acab34bc6ff94f55c4ecec06de853` |
| encoding | UTF-8 |
| status | `DRAFT_ONLY_NOT_FOR_SUBMIT` |
| final status | `NOT_FINAL` |
| package status | `NOT_PACKAGE` |
| audit requirement | `REQUIRES_HUMAN_CHATGPT_AUDIT_BEFORE_PACKAGE` |

## Full Prompt Body

```text
SPLIT02_POSE_KF_01_R02_identity_repair. No visible text, numbers, labels, captions, logo, watermark, or UI marks in the image.

This is a single static keyframe, not a video.

Repair goal: preserve the corridor, wooden column, rain, and close-contact composition from the failed R01 image, but replace the right-side fighter identity with the approved Shuangji identity. The failed R01 image is composition reference only. Do not copy the failed R01 face, jaw, neck, shoulder shape, body language, or masculine / androgynous identity cues.

Shuangji must be the right-side blue-white and silver adult female fighter. Preserve a clearly feminine facial structure, softer jawline, slimmer neck, narrower shoulders, lighter body frame, elegant female wuxia / xianxia presence, long pale-blue or silver-blue hair, and blue-white / silver costume language. Do not masculinize Shuangji. Do not turn Shuangji into a male warrior. Do not make Shuangji androgynous. Do not broaden her neck or shoulders. Do not harden her jawline. Do not copy the failed R01 right-side face.

Fenshou remains the left-side black-red armored male fighter. Preserve his black-red armor, darker hair, stronger male body mass, and pressure role. Do not swap the two characters. Do not duplicate either character.

The scene remains the same rainy exterior ancient temple corridor: wet stone floor, wooden corridor columns, railing line, cold blue-gray rain light, and medium-wide readable action framing. The wooden column sits between or near the two fighters and works only as a narrow obstacle and partial occluder. It is not a stepping point, not a force trigger, not a parkour prop, and not a breakable object.

The action remains one narrow beat: Fenshou presses into Shuangji's raised guard from the left side, and Shuangji resists beside the column while staying visibly female and identity-stable. Shuangji's forearms and shoulders are compressed toward the column edge, but her face and body silhouette must remain readable and feminine. The column may partially hide a small part of overlapping arms or torsos, but it must not hide Shuangji's face or erase her identity.

Both fighters remain physically engaged and close together. Neither fighter is separated, posing, resetting, or looking away. The image should feel like one middle keyframe of close corridor combat: incoming pressure, one compressed column-edge beat, then ready to return to close combat.

Both fighters' feet stay on the flat wet stone floor. No one steps on the column base. No one steps on a random stone. No jump, no hangtime, no parkour, no wall-run, no roof, no stairs, no eaves route.

No railing, door, lattice, wall, or column breakage. No cracks, debris, wood splinters, broken boards, shockwave, water shield, smoke explosion, or architecture destruction.

No extra characters, no duplicated fighters, no body fusion, no extra limbs, no random weapons, no text, no watermark.
```

## Risk Audit

| Risk | Mitigation In Prompt | Remaining Concern |
|---|---|---|
| Shuangji still masculinized | Explicitly requires adult female Shuangji, feminine facial structure, softer jawline, slimmer neck, narrower shoulders, lighter body frame, elegant female wuxia / xianxia presence | Model may still infer masculine structure from close guard compression or armor overlap |
| R01 failed identity leaking into repair | States failed R01 is composition reference only and forbids copying failed R01 face, jaw, neck, shoulder shape, body language, or masculine / androgynous identity cues | K164 image remains a generation reference in primary plan, so leakage is still possible |
| 3 refs may lose corridor detail | K164 image carries corridor / column / pressure composition; prompt restates rainy exterior ancient temple corridor | Scene/world detail may weaken without V004 scene ref |
| Close-contact body fusion | Prompt says no body fusion, no extra limbs, and keeps both fighters physically engaged but distinct | Overlapping arms beside column remain inherently high risk |
| Column over-occlusion | Prompt permits only small partial occlusion of arms/torsos and forbids hiding Shuangji's face or erasing identity | Column may still obscure face if composition dominates |
| Action becomes static pushing | Prompt frames one compressed corridor-combat middle keyframe with incoming pressure and return readiness | Still-image keyframe may naturally read as static pressure rather than dynamic compression |
| Architecture damage hallucination | Explicitly forbids breakage, cracks, debris, splinters, broken boards, shockwave, shield, smoke explosion, or destruction | Wet corridor and pressure pose may still invite minor debris unless constrained in package review |
| Identities swapped or duplicated | Prompt fixes Shuangji on right, Fenshou on left, forbids swapping and duplication | If visual refs conflict, side assignment can still drift |

## Clause-Level Compliance

- R01 failed image is composition-only, not identity.
- Shuangji identity is highest priority.
- Fenshou identity is preserved.
- The original 5-ref package is not repeated unchanged.
- No video generation is planned in K167.
- No package is created in K167.
- No Dreamina command is run.
- No final or locked state is set.

## Recommended Next Phase

Recommend K168: human + ChatGPT audit of R02 repair prompt and reference-duty map.

K168 should decide whether to:

- approve R02 prompt for no-submit package planning
- revise prompt again
- use 3-ref primary package
- use 4-ref fallback with V004 scene/world
- stop SPLIT-02 repair and plan direct `CUT_B -> CUT_C` continuity

K168 must not submit.

## What Not To Do

- Do not run Dreamina.
- Do not submit.
- Do not package.
- Do not use R01 as identity ref.
- Do not proceed to video generation.
- Do not mark final.
- Do not lock.
- Do not update Source in K167.

## Source Update Recommendation

Do not update official Source in K167.

Future Source note candidate: R01 demonstrated that successful composition does not imply identity pass; failed outputs must be demoted to composition-only and repair prompts must explicitly forbid copying failed identity cues.

## Safety

- No Dreamina command was run.
- No submit/query/download occurred.
- No retry/resubmit occurred.
- No media was created.
- No media was staged.
- No package JSON was created.
- No manifest CSV was created.
- No shot record JSON was modified.
- `sources/` was untouched.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `final_master=false`.
- `locked=false`.

## Final Verdict

`SHOT03_SPLIT02_POSE_KF_R02_IDENTITY_REPAIR_PROMPT_DRAFT_READY_HUMAN_K168_AUDIT_REQUIRED`
