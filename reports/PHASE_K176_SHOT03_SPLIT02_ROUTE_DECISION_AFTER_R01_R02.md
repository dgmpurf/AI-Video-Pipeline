# PHASE K176 - SHOT-03 SPLIT-02 Route Decision After R01/R02

## Purpose

Decide the SHOT-03 SPLIT-02 route after two image2image attempts failed to solve the combined requirements of dual-character identity, precise close-contact blocking, and corridor/column composition.

This phase is decision/report only. It does not run Dreamina, submit, query, download, retry, resubmit, create media, create package files, or modify shot records.

## Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K175_SHOT03_SPLIT02_POSE_KF_R02_VISUAL_REVIEW_FAILED_BLOCKING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K174_SHOT03_SPLIT02_POSE_KF_R02_DOWNLOAD_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K173_SHOT03_SPLIT02_POSE_KF_R02_QUERY_STATUS.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K172_SHOT03_SPLIT02_POSE_KF_R02_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K170_SHOT03_SPLIT02_POSE_KF_R02_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K169_SHOT03_SPLIT02_POSE_KF_R02_NO_SUBMIT_PACKAGE_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K168_SHOT03_SPLIT02_POSE_KF_R02_PROMPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K167_SHOT03_SPLIT02_POSE_KF_R02_IDENTITY_REPAIR_PROMPT_DRAFT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K166_SHOT03_SPLIT02_POSE_KF_IDENTITY_LOCK_REPAIR_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K164_SHOT03_SPLIT02_POSE_KF_DOWNLOAD_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K151_SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K149_SHOT03_BASELINE_CANDIDATE_STATE_RECORD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K148_SHOT03_V004_CUT_CANDIDATE_SELECTION_RECORDED.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K146_SHOT03_V004_CUT_CANDIDATES_CREATED.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K141_SHOT03_SPLIT_SHOT_MICRO_SEQUENCE_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K140_SHOT03_ROUTE_DECISION_RECORD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

## Source Governance Confirmation

- `sources/` was read-only.
- No `sources/` file was modified.
- No `sources/` file was staged.
- No `sources/` file was committed.
- No `sources/` file was pushed.
- Official Source updates require ChatGPT generation/review and human manual action.

## Baseline SHOT-03 State

Current V004-derived baseline from K148/K149:

- CUT_B: current preferred SPLIT-01 clean corridor combat candidate
- CUT_A: backup SPLIT-01 candidate
- CUT_C: possible SPLIT-03 / return-to-close-combat candidate
- final_master=false
- locked=false

Important media state:

| cut | path | role | final_master | locked |
|---|---|---|---:|---:|
| CUT_A | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/shot03_v004_cut_candidates/K146/SHOT-03-V004_CUT_A_0p30_2p20_backup_SPLIT01.mp4` | backup SPLIT-01 | false | false |
| CUT_B | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/shot03_v004_cut_candidates/K146/SHOT-03-V004_CUT_B_0p60_2p80_preferred_SPLIT01.mp4` | preferred SPLIT-01 | false | false |
| CUT_C | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/shot03_v004_cut_candidates/K146/SHOT-03-V004_CUT_C_1p20_3p40_possible_SPLIT03.mp4` | possible SPLIT-03 | false | false |

## R01 Summary

- route: 5-ref image2image
- output image: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_20260627_202259/83628bbc-88bc-4c04-9e7c-11697c84fd95_image_1.png`
- composition / rainy corridor / column-edge setup: partially useful
- Shuangji identity lock: failed
- human review: `濂虫€т汉鐗╂病閿佸畾`
- usable_as_final=false
- locked=false
- usable only as composition/action evidence

R01 demonstrated that the 5-ref route could preserve some corridor/composition value, but it did not protect Shuangji's identity.

## R02 Summary

- route: 3-ref identity-priority image2image
- output image: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SPLIT02_POSE_KF_01_R02_20260627_234035/b7756ff1-2530-4f49-ac86-e69fd35f4786_image_1.png`
- Shuangji identity: partially repaired
- two-character blocking/action relation: failed
- action: too static
- human review: `涓や汉鐨勪綅缃笉瀵广€傚彟澶栵紝鎴戞兂鐭ラ亾鎴戜滑鍦ㄥ仛浠€涔?`
- usable_as_final=false
- locked=false

R02 demonstrated that reducing references and prioritizing identity improved Shuangji somewhat, but the image lost the core blocking/action relationship. Fenshou and Shuangji became separated by the column instead of compressed together by it, and Shuangji read too much like a static display pose.

## Comparative Diagnosis

- The 5-ref route preserved more composition value but failed female identity lock.
- The 3-ref route improved identity but lost correct two-character blocking and action pressure.
- Ordinary image2image is not reliably solving all three requirements together:
  - dual-character identity
  - precise close-contact blocking
  - corridor/column composition
- Continuing R03 ordinary image2image has low expected efficiency because the observed failure mode is oscillation: identity repair weakens blocking, while composition repair risks identity drift.
- The current project priority should be to keep SHOT-03 moving rather than spend more cycles trying to force a difficult insert keyframe through ordinary image2image.

## Route Comparison

| option | route | expected value | risk | production cost | recommendation |
|---|---|---|---|---|---|
| A | Continue R03 ordinary image2image repair | Might eventually produce a better image | High loop cost; identity/blocking trade-off already observed; may keep oscillating between identity repair and action/blocking failure | High | Avoid for now |
| B | Pause SPLIT-02 image2image repair loop and use CUT_B -> CUT_C direct edit continuity | Keeps SHOT-03 moving; uses existing V004-derived clean corridor combat candidates; avoids more image2image identity/action churn | SPLIT-02 terrain affordance insert is weakened or removed | Low to moderate | Preferred route |
| C | Move terrain / column / architecture interaction to SHOT-04 | Allows a new shot designed around architecture interaction from the start; avoids forcing precise terrain insert into an already difficult two-character continuity segment | SHOT-03 becomes less terrain-rich | Moderate | Pair with route B |
| D | Require manual pose sketch / manually controlled keyframe before any further SPLIT-02 generation | Could fix exact blocking if a controlled human/manual reference exists | More setup cost; not immediate production progress | Moderate to high | Keep as future option only |
| E | 4-ref fallback package adding V004 scene/world | May preserve corridor better | Does not directly solve blocking; may reintroduce identity pollution | Moderate | Not preferred now |

## K176 Decision

| field | value |
|---|---|
| route_decision | `pause_SPLIT02_image2image_repair_loop` |
| preferred_next_route | `SHOT03_CUT_B_to_CUT_C_direct_edit_continuity` |
| terrain_interaction_route | `defer_to_SHOT04_architecture_interaction_design` |
| manual_pose_keyframe_route | `optional_future_only` |
| continue_R03_image2image | false |
| final_master | false |
| locked | false |

## Recommended Next Phase

Recommend K177: plan SHOT-03 CUT_B -> CUT_C edit continuity and transition.

K177 should be local/report-only at first:

- no Dreamina
- no media generation
- no new submit
- no final/lock
- may inspect existing CUT_B/CUT_C metadata
- may plan whether a local edit bridge or review artifact is needed

## Alternative Next Phase

K177_ALT: SHOT-04 architecture / terrain interaction concept plan.

This should also be planning-only at first:

- no Dreamina
- no package until route is confirmed
- no final/lock

## What Not To Do

- Do not continue R03 ordinary image2image immediately.
- Do not use R01 or R02 as approved keyframes.
- Do not proceed to video generation from R01 or R02.
- Do not mark final.
- Do not lock.
- Do not update official Source in K176.
- Do not run Dreamina.

## Source Update Recommendation

Do not update official Source in K176.

Future Source V1.12 candidate:

- R01/R02 demonstrated an identity-vs-blocking trade-off in ordinary image2image.
- For precise two-character contact blocking, plain image2image may be inefficient without manual pose/keyframe control.
- Macro-run workflows should still preserve human final review and source-governance boundaries.

## Safety

- No Dreamina command was run.
- No submit/query/download was run.
- No retry/resubmit was run.
- No media was created.
- No media was staged.
- No package JSON was created or modified.
- No manifest CSV was created or modified.
- No prompt TXT was created or modified.
- No shot record JSON was created or modified.
- `sources/` was untouched.
- `final_master=false`
- `locked=false`

## Final Verdict

SHOT03_SPLIT02_ROUTE_DECISION_PAUSE_IMAGE2IMAGE_REPAIR_USE_CUT_B_CUT_C_CONTINUITY_DEFER_TERRAIN_TO_SHOT04_READY_K177
