# PHASE K109 - SHOT-03 V003 Upload-Safe Simplified Corridor Package Ready

## Purpose

Create the SHOT-03 V003 upload-safe simplified exterior-column-corridor no-submit package. This is a text-only package phase. No Dreamina command was run and no media operations were performed.

## V002 Problem Being Fixed

SHOT-03 V002 fixed part of the V001 exterior-start problem, but it overloaded the model with too many spatial beats in one 5-second generation:

- exterior veranda
- columns
- wet stairs
- eaves / roof edge
- roof / tiles
- local breakage

Human review found V002 visually chaotic, with messy choreography, early rooftop drift into SHOT-04 / SHOT-05 territory, and poor face stability, especially for Shuangji in motion or closer views.

## V003 Route

V003 simplifies the shot to one stable environment zone:

- exterior veranda / column corridor / railing combat only
- one stable wet stone floor plane
- columns and railing as tactical obstacles
- wet stairs only as background or edge context
- eaves / roofline only as background context
- no roof duel
- no full stair route

## Package Files

- Manual prompt: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V003_uploadsafe_simplified_exterior_column_corridor_prompt.txt
- Prompt JSON: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V003_uploadsafe.json
- Manifest CSV: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V003_uploadsafe.csv
- Shot record JSON: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V003_uploadsafe.json

## Active References

Exactly three upload-safe JPG references are active:

1. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg
2. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg
3. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg

Original PNG locked refs are not active visual references. SHOT-03 V001/V002 media, contact sheets, and review frames are not active visual references. Prior MP4 files, contact sheets, and review frames are not active visual references.

## Prompt Design Summary

- Beat 01, 0.00s-1.20s: exterior veranda / column corridor start.
- Beat 02, 1.20s-3.60s: single-zone column / railing combat exchange.
- Beat 03, 3.60s-5.00s: controlled local architecture reaction and readable endpoint.

The prompt removes roof duel, full stair route, temple destruction, weapons, giant forms, and over-expanded environmental escalation from this version.

## Face Stability Design

- Medium or medium-wide camera.
- Avoid extreme close-ups.
- Keep faces readable but not too large in frame.
- Preserve Shuangji female identity, silver-blue high ponytail, and blue-silver / white-blue costume language.
- Preserve Fenshou black-red armored male identity.
- No Shuangji gender drift.
- No costume merge, duplicate bodies, extra fighters, or face/body swapping.

## Settings

- task_type: multimodal2video
- model_version: seedance2.0_vip
- duration: 5
- ratio: 16:9
- video_resolution: 720p
- submit_allowed: false
- query_allowed: false
- download_allowed: false
- final_master: false
- locked: false
- human_review_required: true

## Validation

- Prompt file exists: pass.
- Prompt JSON parses: pass.
- Shot record JSON parses: pass.
- Manifest CSV reads: pass.
- All active references exist locally: pass.
- No media staged: pass.
- Upload-safe JPGs not staged: pass.
- .vs/ not staged: pass.

## Next Step

K110 should be SHOT-03 V003 package review. Do not submit unless the human explicitly authorizes a later live submit phase.

## Safety Confirmation

- No Dreamina command was run.
- No submit/query/download happened.
- No AI media was generated.
- No media files were created, edited, moved, deleted, or staged.
- Runtime code was not modified.
- configs/providers.json was not modified.
- Project Source files were not modified.
- SHOT-02 / V013 / V018 lock states were not altered.

Final verdict: SHOT03_V003_UPLOADSAFE_SIMPLIFIED_CORRIDOR_PACKAGE_READY_NO_SUBMIT
