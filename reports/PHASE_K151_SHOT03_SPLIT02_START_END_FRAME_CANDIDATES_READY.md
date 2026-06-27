# PHASE K151 - SHOT-03 SPLIT-02 Start/End Frame Candidates Ready

## Purpose

Create local SPLIT-02 start/end frame candidates from existing CUT_B and CUT_C.

This phase creates local JPG review assets only. It does not create a final SPLIT-02 prompt, package, manifest, shot record, or new video media.

## Files Inspected

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K150_SHOT03_SPLIT02_MICRO_GOAL_REFERENCE_STRATEGY_PLAN.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K149_SHOT03_BASELINE_CANDIDATE_STATE_RECORD.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K148_SHOT03_V004_CUT_CANDIDATE_SELECTION_RECORDED.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K146_SHOT03_V004_CUT_CANDIDATES_CREATED.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K144_SHOT03_V004_REVIEW_ARTIFACTS_READY.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md

## Source Governance Confirmation

- sources/ was read as reference only.
- No sources/ files were modified.
- No sources/ files were staged.
- Official Source updates require ChatGPT generation/review and human manual action.
- source_write_allowed=false
- source_stage_allowed=false
- source_commit_allowed=false

## Input Validation

| Source Cut | Path | Exists | SHA256 | SHA256 Matches Expected | Duration | Resolution | FPS | Frame Count | Size Bytes |
| --- | --- | --- | --- | --- | ---: | --- | ---: | ---: | ---: |
| CUT_B | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/shot03_v004_cut_candidates/K146/SHOT-03-V004_CUT_B_0p60_2p80_preferred_SPLIT01.mp4 | true | c6954933010d3687441b795a523cfb65c01c75378fcdd68f30fdcd40d72ef911 | true | 2.2388059701492535 | 1280x720 | 24.12 | 54 | 1948726 |
| CUT_C | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/shot03_v004_cut_candidates/K146/SHOT-03-V004_CUT_C_1p20_3p40_possible_SPLIT03.mp4 | true | a4f6168cd77801daf8cf0ea6691e4dd65fe06b8df568d2b45869233fbcaa9598 | true | 2.197346600331675 | 1280x720 | 24.12 | 53 | 1957356 |

## Method

- method: Python/cv2 frame extraction and contact sheet generation
- ffmpeg_used=false
- Dreamina_used=false
- timestamp_basis=cut-local timestamps
- frame_selection=nearest valid frame by rounded local timestamp * source fps
- output_frame_format=JPG
- contact_sheet_layout=5 columns x 2 rows

## Artifacts Created

Output frame directory:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates

Contact sheet:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/SHOT-03-K151_SPLIT02_start_end_frame_candidates_contact_sheet.jpg

Artifact summary:

- frames_created=10
- contact_sheet_exists=true
- contact_sheet_resolution=2400x624
- contact_sheet_size_bytes=479114

## Candidate Frame Table

| Candidate ID | Source Cut | Requested Local Timestamp | Actual Frame Index | Actual Local Timestamp | File Path | Intended Role |
| --- | --- | ---: | ---: | ---: | --- | --- |
| CUT_B_START_01 | CUT_B | 1.40s | 34 | 1.4096185737976783s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_01_t1p40.jpg | SPLIT-02 start candidate from CUT_B |
| CUT_B_START_02 | CUT_B | 1.60s | 39 | 1.616915422885572s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_02_t1p60.jpg | SPLIT-02 start candidate from CUT_B |
| CUT_B_START_03 | CUT_B | 1.80s | 43 | 1.7827529021558872s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_03_t1p80.jpg | SPLIT-02 start candidate from CUT_B |
| CUT_B_START_04 | CUT_B | 2.00s | 48 | 1.990049751243781s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_04_t2p00.jpg | SPLIT-02 start candidate from CUT_B |
| CUT_B_START_05 | CUT_B | 2.20s | 53 | 2.197346600331675s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_B_START_05_t2p20.jpg | SPLIT-02 start candidate from CUT_B |
| CUT_C_RETURN_01 | CUT_C | 0.00s | 0 | 0.0s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_01_t0p00.jpg | SPLIT-02 end/return candidate from CUT_C |
| CUT_C_RETURN_02 | CUT_C | 0.20s | 5 | 0.20729684908789386s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_02_t0p20.jpg | SPLIT-02 end/return candidate from CUT_C |
| CUT_C_RETURN_03 | CUT_C | 0.40s | 10 | 0.41459369817578773s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_03_t0p40.jpg | SPLIT-02 end/return candidate from CUT_C |
| CUT_C_RETURN_04 | CUT_C | 0.60s | 14 | 0.5804311774461028s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_04_t0p60.jpg | SPLIT-02 end/return candidate from CUT_C |
| CUT_C_RETURN_05 | CUT_C | 0.80s | 19 | 0.7877280265339967s | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-03-V004/k151_split02_frame_candidates/CUT_C_RETURN_05_t0p80.jpg | SPLIT-02 end/return candidate from CUT_C |

## Candidate Pair Guidance

K152 human + ChatGPT visual review should evaluate:

- start candidate should show active contact or immediate pressure from CUT_B, not an idle pose.
- end candidate should allow return into CUT_C without visual jump.
- both should preserve corridor, column, railing, wet stone, and rain environment.
- no random stone or column-base stepping.
- no roof, stairs, eaves route, jump, or hangtime.
- no architecture breakage.
- identities should remain stable.
- the selected pair should support the K150 primary micro-goal: column-edge guard compression + brief occlusion.

## Recommended Next Phase

K152 should be human + ChatGPT visual review of the K151 contact sheet.

Possible K152 outcomes:

- select a start/end frame pair.
- decide keyframe/pose reference is needed.
- abandon SPLIT-02 and use CUT_B -> CUT_C edit continuity.
- proceed to prompt-planning only after human approval.

Do not perform K152 in K151.

## Safety

- Dreamina was not run.
- No submit/query/download happened.
- No retry/resubmit happened.
- No new video media was created.
- No cut MP4 was created.
- Only JPG frame candidates and one contact sheet were created.
- No V007 prompt/package was created.
- No final SPLIT-02 prompt/package was created.
- No SHOT-04 prompt/package was created.
- No package JSON/manifest/shot record was created.
- No shot record was modified.
- sources/ was not modified or staged.
- Runtime code was not modified.
- configs/providers.json was not modified.
- Media artifacts were created but not staged.
- final_master=false
- locked=false
- SHOT-02 / V013 / V018 / V004 / V005 / V006 lock states were not touched.

## Final Verdict

SHOT03_SPLIT02_START_END_FRAME_CANDIDATES_READY_PENDING_HUMAN_CHATGPT_REVIEW
