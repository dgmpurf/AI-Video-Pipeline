# PHASE K15: SHOT-02-V009 Body Footwork Reaction Image2Video Package Report

Date: 2026-06-20

## Scope

- Prepare SHOT-02-V009 image2video package only.
- Do not submit Dreamina, query, download, generate AI media, lock, mark final master, or auto-continue.
- Do not modify Source files, runtime code, or configs/providers.json.

## Context

- Current preferred SHOT-02 impact sequence:
  - V007C preimpact pressure charge.
  - V006 CUT03 shockwave reveal.
  - V008B aftershock rain recovery.
- Current preferred full impact beat: FULL_B.
- Next missing material is body / footwork reaction and transition into the next combat beat.
- V009 purpose: create a short grounded physical recovery source after the full impact beat, not another shockwave clip.

## Input Reference

- Source video: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-full-impact-beat/SHOT-02_FULL_TEST_B_C1_plus_V008B.mp4
- Selected input image: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_3p20s.png
- Selected frame time: 3.20s.
- Selected frame resolution: 1280x720.
- Selected frame file size: 730539 bytes.
- Selected frame sha256: e5aa966d0e7f99f1b09f694f6ea32792a9d07fb0bd1f17cacda50489ecb11d91.
- Backup input image: productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_2p75s.png
- Backup frame sha256: 9c1754b0576baaad6b38b38a6bfb974c59c29294531e8698208be0f0ef67123a.
- Derived ref policy: local media only; do not stage or commit unless explicitly approved later.

## Start Frame Selection

- Review reference: reports/PHASE_K14_SHOT02_V009_START_FRAME_REVIEW.md
- Preferred candidate: 3.20s.
- Backup candidate: 2.75s.
- Selection reason: 3.20s best balances post-shockwave timing, readable fighters, readable temple environment, and body/footwork reaction potential. 2.75s remains useful if a more active starting frame is needed.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 0.8-1.5s
- video_resolution: 720p
- ratio: omitted for image2video
- image input count: exactly one --image
- command_contract_valid: true

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V009_body_footwork_reaction_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V009.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V009.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V009.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-V009_image2video_readiness_review.md

## Prompt Strategy

- Chinese prompt.
- Controlled physical action.
- Focus on stance recovery, footwork, body reaction, clothing/hair settling, rain/mist returning to normal, and transition into the next combat beat.
- Do not create a new shockwave, second explosion, water wall, circular water curtain, shield dome, or new full attack.
- Preserve rainy ancient temple frontal axis and readable two-character spatial relationship.

## Command Preview Only

Do not run this command until explicit live-submit approval is given and command-contract preflight passes:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V009_body_footwork_reaction_prompt.txt"
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/derived_refs/SHOT-02-V009_start_frame_candidates/SHOT-02-V009_start_candidate_3p20s.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --poll 0
```

## Codex Download Stage (SHOT-02-V009, Existing Submit)

- `submit_id`: `1b359b01-a7c8-4d77-a9db-6c82251e36f4`
- `logid`: `20260621001332169254047008993B0B1`
- Download command attempted once with:
  - `dreamina query_result --submit_id 1b359b01-a7c8-4d77-a9db-6c82251e36f4 --download_dir <run_dir>`
- Result: **failed locally** (Codex local environment permission issue before media download).
- Non-sensitive error summary: Dreamina log initialization denied access to `C:\\Users\\msjpurf\\.dreamina_cli\\logs\\dreamina.log.2026-06-21_13`.
- No clip output, contact sheet, or review frames generated in this step.
- Interpretation: this was a local Codex logger block, not a remote generation failure.

## Manual Download Ingest

- Human manual download succeeded.
- Standardized output path: `productions/chi_yan_tian_qiong/runs/live/SHOT-02-V009_manual_download/SHOT-02-V009_body_footwork_reaction_motion.mp4`
- Original manual download file: `productions/chi_yan_tian_qiong/runs/live/SHOT-02-V009_manual_download/1b359b01-a7c8-4d77-a9db-6c82251e36f4_video_1.mp4`
- File size: `6880052` bytes
- SHA256: `44e724c924f57346428e0753fe784255a40ed47694ca00bced4520519795d195`
- Duration: `4.016667s`
- Resolution: `1280x720`
- FPS: `24.149377593360995`
- Frame count: `97`
- Contact sheet: `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_contact_sheet.jpg`
- Review frames:
  - `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_0p00s.jpg`
  - `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_0p50s.jpg`
  - `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg`
  - `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p50s.jpg`
  - `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_2p00s.jpg`
  - `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_last_4p00s.jpg`
- Human review status: pending.

## Risk Notes

- The model may restart shockwave language from the source frame context; prompt forbids new shockwave, second explosion, and water wall.
- The model may generate a new attack; prompt requires recovery and next-beat setup only.
- The model may over-settle into static posing; final edit should use the best 0.8-1.5s segment with visible physical weight shift.
- The selected frame is derived local media and should remain untracked unless later explicitly approved.

## Validation Result

- JSON parse: passed for prompt JSON and shot video record.
- CSV read: passed for image2video manifest.
- Selected input image path exists: true.
- Selected input image sha256 matches: true.
- duration=4 recorded: true.
- ratio omitted: true.
- image_input_count=1: true.
- command_contract_valid=true: true.
- final_edit_target=0.8-1.5s: true.

## Decision

SHOT_02_V009_MANUAL_DOWNLOAD_INGESTED_REVIEW_PENDING
