# PHASE K143 - SHOT-03 V004 Edit/Cut Artifact Plan

Text-only V004-based edit/cut artifact plan for SHOT-03 SPLIT-01 and possible SPLIT-03 use.

No Dreamina command was run. No submit, query_result, download, retry, resubmit, media generation, frame extraction, contact sheet generation, cut MP4 creation, V007 prompt, SPLIT-02 prompt, SHOT-04 prompt, package JSON, manifest CSV, or shot record JSON was created in this phase.

## 1. Purpose

Plan the next local review step for SHOT-03 V004 as the clean corridor combat baseline.

K142 selected the conservative next route: use V004 as the existing positive media candidate and determine whether it can supply SPLIT-01, and possibly SPLIT-03, before creating any new terrain insert package.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K142_SHOT03_EXISTING_MEDIA_SPLIT_CUT_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K141_SHOT03_SPLIT_SHOT_MICRO_SEQUENCE_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K140_SHOT03_ROUTE_DECISION_RECORD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K139_SHOT03_V004_V005_V006_COMPARATIVE_STRATEGY_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K121_SHOT03_V004_HUMAN_REVIEW_AND_V005_TERRAIN_AFFORDANCE_DIRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`

Media metadata inspected only:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V004_20260626_150150/SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage.mp4`

## 3. Source Governance Confirmation

- `sources/` was read only.
- No file under `sources/` was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Official Source updates require ChatGPT generation/review and human manual action.
- `source_read_allowed=true`
- `source_recommendation_allowed=true`
- `source_draft_allowed=true`
- `source_write_allowed=false`
- `source_stage_allowed=false`
- `source_commit_allowed=false`
- `source_push_allowed=false`

## 4. V004 Role

V004 remains the best available SHOT-03 clean corridor baseline/fallback.

Current role:

- best clean corridor baseline/fallback
- candidate SPLIT-01 source
- possible SPLIT-03 return-to-close-combat source
- usable as terrain/world reference
- not a complete terrain-affordance solution
- not final
- not locked

Why V004 is the right next review target:

- It is the only positive candidate among V004/V005/V006.
- It already solved several earlier problems: corridor readability, identity stability, rhythm, and lack of wrong structural damage.
- It can keep SHOT-03 moving while SPLIT-02 terrain affordance remains deferred until a stronger reference strategy exists.

## 5. V004 Media Inventory

| Field | Value |
|---|---|
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-03-V004_20260626_150150/SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage.mp4` |
| exists | true |
| size_bytes | `8039122` |
| sha256 | `9031f6482718a4c460e568b79dcb0b8fdf7eaf5e13308cbc74f132deb0414cc0` |
| sha256_matches_expected | true |
| duration_seconds | `5.016666666666667` |
| resolution | `1280x720` |
| fps | `24.119601328903656` |
| frame_count | `121` |
| current_human_review_status | `positive_clean_corridor_combat_needs_terrain_affordance_escalation` |
| final_master | false |
| locked | false |

No media was created in K143.

## 6. Proposed K144 Review Artifact Plan

K144 should create local visual review artifacts from the existing V004 MP4 only.

Recommended K144 artifacts:

- review frames directory:
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k144_v004_cut_review_frames/`
- contact sheet:
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/SHOT-03-V004_K144_cut_review_contact_sheet.jpg`
- text review map:
  - K144 should record frame timestamps and candidate windows, but should not modify shot records unless separately authorized.

Recommended frame timestamps:

| frame_index | timestamp | note |
|---:|---:|---|
| 01 | 0.00s | opening state |
| 02 | 0.30s | early contact / setup check |
| 03 | 0.60s | early exchange density |
| 04 | 0.90s | SPLIT-01 candidate region |
| 05 | 1.20s | SPLIT-01 candidate region |
| 06 | 1.50s | SPLIT-01 candidate region |
| 07 | 1.80s | SPLIT-01 / transition check |
| 08 | 2.10s | CUT_A end / CUT_B middle check |
| 09 | 2.40s | CUT_B / SPLIT-03 start check |
| 10 | 2.70s | CUT_B end / continuation check |
| 11 | 3.00s | CUT_C middle |
| 12 | 3.30s | CUT_C end check |
| 13 | 3.60s | later return-to-combat check |
| 14 | 3.90s | CUT_D middle |
| 15 | 4.20s | CUT_D end check |
| 16 | 4.50s | tail activity check |
| 17 | 4.80s | no idle tail check |
| 18 | 5.00s | final valid frame / cut-through-action check |

Timestamp adjustment rule:

- V004 duration is approximately `5.016666666666667s`, so `5.00s` is within the clip.
- K144 should use nearest valid frame if exact timestamp seeking lands between frames.
- K144 should use Python/cv2 or existing local tooling only if authorized.

Contact sheet plan:

- Use all 18 frames above.
- Suggested layout: 6 columns x 3 rows.
- Label each cell with frame index and timestamp.
- Do not overwrite older V004 contact sheets unless K144 explicitly reports that the K144-specific target path is new or safe.

## 7. Candidate Cut Windows To Inspect In K144

These are planning windows only. K143 does not create cuts.

| Candidate | Window | Possible use | Why inspect | Main risk |
|---|---|---|---|---|
| V004_CUT_A | 0.30s-2.20s | possible SPLIT-01 | avoids very first opening, should catch early combat density and corridor baseline | may miss opening context or end before best exchange |
| V004_CUT_B | 0.60s-2.80s | possible SPLIT-01 | likely stronger if the fight settles after the opening; good 2.2s baseline candidate | may start too late for continuity after SHOT-02 |
| V004_CUT_C | 1.20s-3.40s | possible SPLIT-03 or continuation | useful if mid-clip has best return-to-close-combat rhythm | may be too detached from sequence opening |
| V004_CUT_D | 2.00s-4.20s | possible later return-to-combat / fallback bridge | tests whether later material can bridge after future SPLIT-02 | may include weaker tail or ordinary movement |
| V004_CUT_E | 3.00s-5.00s | tail activity diagnostic only | checks whether V004 tail keeps action alive or idles | not recommended unless tail has strong contact/re-entry |

K144 should visually verify the windows before any cut MP4 is created. If the human wants actual cut candidates, that should be K145.

## 8. Human Review Criteria For V004 Cuts

Human review should score each candidate window against:

- contact density
- first clear contact timing
- visible body result for contacts
- no idle tail
- stable Fenshou / Shuangji identity
- readable corridor / column / railing / wet stone space
- no unintended structural breakage
- no chaotic choreography
- usable rhythm for SHOT-03 baseline
- whether the cut feels too ordinary
- whether it can bridge into a later SPLIT-02 terrain insert
- whether it can return from a future SPLIT-02 insert as SPLIT-03
- whether the end frame is useful for continuing into SHOT-04 planning

Suggested human labels:

- `preferred_split01_candidate`
- `usable_split01_backup`
- `possible_split03_candidate`
- `too_ordinary_but_safe`
- `reject_for_idle_tail`
- `reject_for_identity_or_space_instability`

## 9. Recommended K144

Recommended next phase:

**K144 V004 local review frames + contact sheet + candidate cut-window map.**

K144 should:

1. Confirm `sources/` clean.
2. Confirm V004 MP4 exists and matches sha256.
3. Generate K144-specific review frames at the 18 timestamps listed above.
4. Generate a K144-specific contact sheet.
5. Create a text report mapping the proposed windows to the contact-sheet frames.
6. Do not create cut MP4 files unless the user explicitly adds that authorization to K144.
7. Do not run Dreamina.

Cut MP4 creation should be separated as K145 after human review of the K144 contact sheet, unless the human explicitly authorizes both review artifacts and cut creation in one phase.

## 10. Deferred Items

Deferred until after V004 cut review:

- SPLIT-02 terrain insert prompt planning
- SPLIT-02 reference frame / pose / action reference selection
- SHOT-04 architectural interaction planning
- any V1.12 Source update proposal
- final/lock decision
- actual cut MP4 creation unless separately authorized
- any Dreamina submit/query/download

## 11. What Not To Do

- Do not create prompt-only V007.
- Do not run immediate Dreamina submit.
- Do not create SPLIT-02 prompt/package.
- Do not create SHOT-04 prompt/package.
- Do not mark final.
- Do not lock.
- Do not modify official Source from Codex.
- Do not treat V004 as a terrain-affordance solution; it is a clean corridor baseline/fallback.

## 12. Safety

- No Dreamina command was run.
- No submit, query_result, download, retry, resubmit, or batch operation happened.
- No media was created, edited, copied, moved, deleted, or staged.
- No frames were extracted.
- No contact sheets were created.
- No cuts were created.
- No prompt/package/manifest/shot record was created or modified.
- `sources/` was read only and not staged.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `final_master=false`.
- `locked=false`.
- SHOT-02 / V013 / V018 / V004 / V005 / V006 lock states were not touched.

## 13. Final Verdict

SHOT03_V004_EDIT_CUT_ARTIFACT_PLAN_READY_HUMAN_K144_AUTHORIZATION_REQUIRED
