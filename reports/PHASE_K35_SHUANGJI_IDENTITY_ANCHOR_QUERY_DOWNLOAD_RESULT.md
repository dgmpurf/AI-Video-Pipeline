# PHASE K35 Shuangji Identity Anchor Query/Download Result

Date: 2026-06-22

## Scope

- Query existing `A-CH-B-IDENTITY-002` submit_id only.
- Do not submit, resubmit, retry, batch, image2image, logout, or relogin.
- Download is allowed only through the single `query_result --download_dir` command in this pass.
- Do not mark final master or locked.
- Do not add this asset to `locked_refs`.

## Canary Result

Canary passed before query.

- Dreamina executable: `C:\Users\msjpurf\bin\dreamina.exe`
- `dreamina version`: `46b5b0e-dirty`
- commit: `46b5b0e`
- build_time: `2026-06-03T19:39:25Z`
- `dreamina user_credit`: succeeded
- total_credit before query: `2620`
- user_id: `1611200923726843`
- vip_level: `maestro`

## Exact Query Command

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id cfbfaa22-2a4e-40bc-b14e-987de51c3912 --download_dir "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-CH-B-IDENTITY-002_20260622_160419"
```

## Query Result Summary

- submit_id: `cfbfaa22-2a4e-40bc-b14e-987de51c3912`
- gen_status: `success`
- queue_status: `Finish`
- queue_idx: `0`
- queue_length: `0`
- priority: `1`
- credit_count: `1`

## Downloaded Candidate Images

Downloaded and canonicalized candidate path:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-CH-B-IDENTITY-002_20260622_160419/A-CH-B-IDENTITY-002-R01_candidate_01.png`

## Validation Metadata

| Candidate | Exists | File size | SHA-256 | Dimensions | Format |
|---|---|---:|---|---:|---|
| `candidate_01` | true | 3874061 bytes | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | 1440x2560 | PNG |

## Review Assets

Contact sheet:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/image_reviews/A-CH-B-IDENTITY-002/A-CH-B-IDENTITY-002_contact_sheet.jpg`

Review index:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/image_reviews/A-CH-B-IDENTITY-002/A-CH-B-IDENTITY-002_review_index.md`

## Planning Record Update

`productions/chi_yan_tian_qiong/assets/A-CH-B-IDENTITY-002_planning_record.json` was updated:

- status: `success_downloaded_pending_human_review`
- review_status: `pending`
- final_master: `false`
- locked: `false`
- human_review_required: `true`
- usable_as_identity_reference: `pending_human_review`

## Boundary Confirmation

- Exactly one `query_result --download_dir` command was run.
- No submit was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
- No image2image command was run in this pass.
- Media files were not staged.
- `final_master=false`
- `locked=false`
- Human review is required before any candidate can be locked or used as a production identity reference.

Final verdict: `SHUANGJI_IDENTITY_ANCHOR_SUCCESS_DOWNLOADED_REVIEW_READY`
