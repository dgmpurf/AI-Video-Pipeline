# PHASE K44 SHOT-02 V012 Cut Speed Tests

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Purpose

SHOT-02-V012 is rejected for final use, but K42/K43 retained it as an optional local cut/speed-up diagnostic only.

This pass created local media edit tests from the existing downloaded V012 MP4. These tests are secondary diagnostics only. The primary path remains SHOT-02-V013 new generation with stronger choreography.

## Safety Boundaries

- Dreamina was not run.
- No submit, query_result, download, retry, resubmit, or batch action happened.
- No image2video, image2image, or multimodal2video command was run.
- No V013 package files were created.
- No source MP4 was moved, deleted, or overwritten.
- No media files were staged.
- final_master=false.
- locked=false.
- Human review is required before any final or lock decision.

## Source Video

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V012_20260622_233335/SHOT-02-V012_identity_locked_fast_staccato_combat.mp4

## Output Clips

CUT01 window: 0.50s-1.50s

1. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V012/SHOT-02-V012_CUT01_0p50_to_1p50_normal.mp4
2. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V012/SHOT-02-V012_CUT01_0p50_to_1p50_speed_1p25x.mp4
3. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V012/SHOT-02-V012_CUT01_0p50_to_1p50_speed_1p50x.mp4

CUT02 window: 0.75s-1.75s

4. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V012/SHOT-02-V012_CUT02_0p75_to_1p75_normal.mp4
5. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V012/SHOT-02-V012_CUT02_0p75_to_1p75_speed_1p25x.mp4
6. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V012/SHOT-02-V012_CUT02_0p75_to_1p75_speed_1p50x.mp4

## Validation Metadata

| Test | Exists | Duration | Resolution | FPS | Frame Count | File Size Bytes | SHA256 |
|---|---:|---:|---|---|---:|---:|---|
| CUT01 normal | true | 1.000s | 1280x720 | 24/1 | 24 | 1143712 | 3a5ae810b45b8edaf1dccf0ab520a83ceb357be9518c336fd1275d14f6a6c03b |
| CUT01 1.25x | true | 0.792s | 1280x720 | 24/1 | 19 | 976821 | 9a16a45824a9872f68bff059cfb8373b061353354a1ed823ec7aa69ee90e5e63 |
| CUT01 1.50x | true | 0.667s | 1280x720 | 24/1 | 16 | 889381 | 0c7bce1f3b09cc2edbe01933d755d8aa8373940b397a6df08fedba14fe6d4da6 |
| CUT02 normal | true | 1.000s | 1280x720 | 24/1 | 24 | 1079548 | aeb09ae09f2e4c4186aea90360836fe23ac606c347d82bc4f53915d8f17fd8e1 |
| CUT02 1.25x | true | 0.792s | 1280x720 | 24/1 | 19 | 918895 | 4c504507019edbc7bc8c6e13c4926b4e7c10ab1ad54044fe27142df4ece6c84e |
| CUT02 1.50x | true | 0.667s | 1280x720 | 24/1 | 16 | 842372 | b0b3b781b98c65840dea91534395eb4a74f4684d38805a0807f01babacab7a15 |

## Contact Sheet

Path:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V012/SHOT-02-V012_CUT_SPEED_TESTS_contact_sheet.jpg

Contact sheet metadata:

- exists=true
- file_size_bytes=161092
- sha256=26b72612c2275580198b46a753879c1a5243717e4d7dcf860b96c83576f92b77

Contact sheet grid order:

1. CUT01 1.5x
2. CUT02 1.5x
3. CUT01 1.25x
4. CUT02 1.25x
5. CUT01 normal
6. CUT02 normal

## Recommended Human Review Order

1. CUT01 1.5x
2. CUT02 1.5x
3. CUT01 1.25x
4. CUT02 1.25x
5. CUT01 normal
6. CUT02 normal

## Interpretation Reminder

V012 remains rejected for final use. These clips are useful only to test whether a tiny bridge/extract exists inside the generated material.

If the speed-up still lacks collision force or contact density, do not keep forcing V012. Continue to SHOT-02-V013 new generation with stronger action choreography.

Final verdict:
SHOT_02_V012_CUT_SPEED_TESTS_READY_FOR_HUMAN_REVIEW
