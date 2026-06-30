# PHASE K250 - SHOT-04 R02 Near-Wall Guard-Clash Local Cut-Window Diagnostic

## 1. Purpose

Create a local edit-window diagnostic from the existing K247-downloaded SHOT-04 R02 near-wall guard-clash text2video result.

This phase creates exactly two local MP4 cut candidates from the existing video for later visual review. It does not run Dreamina, submit, query, download, retry, resubmit, batch, create a new generation, mark final, or lock.

## 2. Human Authorization

The human explicitly authorized K250 to create local cut-window diagnostic artifacts from this existing K247 video only:

```text
G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437/37d02a39-7ca3-4141-b5ce-3e578622843e_video_1.mp4
```

Allowed:

- local input video validation
- exactly two short local cut candidates
- lightweight metadata for those cuts
- one text report

Not authorized:

- Dreamina
- submit / query / download
- retry / resubmit / batch
- new generation
- final / lock
- media staging

## 3. ChatGPT Module Recommendation

- Current ChatGPT module for reviewing this Codex K250 result: ChatGPT Think
- Reason: K250 is local technical cut-window diagnostic and report validation only.
- Recommended next module for K251 visual review of cut candidates: ChatGPT Pro
- Pro Extended needed now: false
- Reason: Source synthesis or macro-pipeline redesign is not currently active.

## 4. Boundaries

- No Dreamina command was run.
- No submit was run.
- No query was run.
- No download was run.
- No retry or resubmit was run.
- No batch execution was run.
- No `sources/` files were modified.
- No prompt txt files were modified.
- No package JSON files were modified.
- No manifest CSV files were modified.
- No shot records were modified.
- No runtime/config/auth/session/token/key/env files were modified or printed.
- No MP4 files were staged.
- No extracted frames were staged.
- No contact sheets were staged.
- No artifact JSON was staged.
- `final_master=false`.
- `locked=false`.
- `visual_success_claimed=false`.
- No final approval is claimed.

## 5. Git / Source Preflight

Commands run:

```powershell
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
```

Result:

- branch status: `## main...origin/main`
- `sources/`: clean
- known allowed workspace noise present:
  - `.vs/`
  - `reports/context_recovery/`

K250 was not blocked by dirty sources.

## 6. K247 / K248 / K249 Lineage Verification

Read:

- `reports/PHASE_K247_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_DOWNLOAD_RESULT.md`
- `reports/PHASE_K248_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_REVIEW_ARTIFACTS_READY.md`
- `reports/PHASE_K249_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_VISUAL_REVIEW.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`

Verified:

- submit_id: `37d02a39-7ca3-4141-b5ce-3e578622843e`
- input video sha256: `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418`
- K249 visual_status: `partial_motion_probe_success_but_not_primary`
- K249 best_usable_time_window: `0.10s-0.65s`
- K249 secondary_possible_window: `4.25s-5.00s`
- K249 usable_as_SHOT04_R02_primary: `false`
- K249 usable_as_edit_candidate: `limited`
- K249 final_master: `false`
- K249 locked: `false`

## 7. Input Video Path, Size, SHA-256, Metadata

Input video:

```text
productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437/37d02a39-7ca3-4141-b5ce-3e578622843e_video_1.mp4
```

Validation:

- file exists: true
- file size bytes: `11431647`
- sha256: `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418`
- expected size matched: true
- expected sha256 matched: true
- width: `1280`
- height: `720`
- fps: `24.119601328903656`
- frame_count: `121`
- duration_seconds: `5.016666666666667`

K250 was not blocked by media hash mismatch.

## 8. K249 Visual Review Basis

K249 concluded:

- visual_status: `partial_motion_probe_success_but_not_primary`
- usable_as_SHOT04_R02_primary: `false`
- usable_as_edit_candidate: `limited`
- best usable window: `0.10s-0.65s`
- secondary possible window: `4.25s-5.00s`

K250 only tests those local windows as diagnostic cut candidates. It does not make a new visual success decision.

## 9. Cut Candidate Table

| Cut | Source window | Intended role | Risk | Output |
|---|---|---|---|---|
| CUT_A | `0.10s-0.65s` | `limited_near_wall_pressure_micro_insert_candidate` | `too_short_or_not_complete_action_beat` | `SHOT-04-R02-K250_CUT_A_0p10_0p65_near_wall_pressure_insert.mp4` |
| CUT_B | `4.25s-5.00s` | `secondary_tail_motion_diagnostic_candidate` | `late_window_may_not_match_front_loaded_edit_goal` | `SHOT-04-R02-K250_CUT_B_4p25_5p00_tail_motion_diagnostic.mp4` |

No other cut candidates were created.

## 10. Cutting Tool / Method

- ffmpeg availability: unavailable in PATH
- cutting method used: `python_cv2_frame_accurate_video_only_reencode`
- audio_preserved: `false`
- reencode_or_stream_copy: `python_cv2_frame_accurate_video_only_reencode`
- no music added
- no effects added
- no stabilization added
- no speed change
- no crop
- no color correction
- no overlays
- original video was not renamed or overwritten
- output directory was absent before K250 creation, so no existing K250 outputs were overwritten

## 11. CUT_A Output

Path:

```text
productions/chi_yan_tian_qiong/edits/shot04_r02_near_wall_guard_clash_cut_candidates/K250/SHOT-04-R02-K250_CUT_A_0p10_0p65_near_wall_pressure_insert.mp4
```

Validation:

- exists: true
- file size bytes: `843385`
- sha256: `583f5a667097b381bb97ff12a4abba106df6f80ab934fcb81d56697c65df50bf`
- duration_seconds: `0.6218905472636815`
- width: `1280`
- height: `720`
- fps: `24.12`
- frame_count: `15`
- source_start_frame: `2`
- source_end_frame: `16`
- source_frames_written: `15`
- audio_preserved: `false`
- diagnostic_artifact_only: true

## 12. CUT_B Output

Path:

```text
productions/chi_yan_tian_qiong/edits/shot04_r02_near_wall_guard_clash_cut_candidates/K250/SHOT-04-R02-K250_CUT_B_4p25_5p00_tail_motion_diagnostic.mp4
```

Validation:

- exists: true
- file size bytes: `687657`
- sha256: `072cc3028dc74fecf6e96f6368031bbed001560940af39feba2dece365487369`
- duration_seconds: `0.7462686567164178`
- width: `1280`
- height: `720`
- fps: `24.12`
- frame_count: `18`
- source_start_frame: `103`
- source_end_frame: `120`
- source_frames_written: `18`
- audio_preserved: `false`
- diagnostic_artifact_only: true

## 13. Local Metadata Index

Created local metadata index:

```text
productions/chi_yan_tian_qiong/edits/shot04_r02_near_wall_guard_clash_cut_candidates/K250/K250_cut_candidates_index.json
```

Validation:

- file size bytes: `2847`
- sha256: `d10c000e50510ff1534e6edc4af26ab4e58baaf2b06ee00c74a1b58bc6871696`
- staged: false

## 14. Stage / Review Status

- `media_not_staged=true`
- `cut_candidates_not_staged=true`
- `artifact_index_not_staged=true`
- `visual_success_claimed=false`
- `usable_as_SHOT04_R02_primary=false`
- `final_master=false`
- `locked=false`

## 15. Recommended Next Phase

Recommended next phase:

`K251 human + ChatGPT Pro visual review of CUT_A and CUT_B`

K251 should decide whether either cut candidate has limited edit value. K250 does not claim either cut is primary, final, locked, or visually successful.

## 16. Final Verdict

`K250_LOCAL_CUT_WINDOW_DIAGNOSTIC_READY_K251_VISUAL_REVIEW`
