# PHASE K75 - SHOT-02-V016 Upload-Safe Single Submit Result

## Human Authorization

The human explicitly approved a single SHOT-02-V016 upload-safe submit:

> 批准 V016 upload-safe 单次 submit。允许 Codex 先跑 Dreamina canary 和 multimodal2video command-contract preflight；通过后只 submit 一次。不要 query，不要 download，不要 retry，不要 resubmit。

## Package Review Context

- Package review: `reports/PHASE_K74_SHOT02_V016_PACKAGE_REVIEW.md`
- Package review verdict: `SHOT_02_V016_PACKAGE_REVIEW_READY_FOR_HUMAN_SUBMIT_APPROVAL`
- V016 package state before submit: package-ready, not final, not locked.
- This pass is the first explicit human-authorized V016 submit attempt.
- V013 CUT01 remains the locked current SHOT-02 passed segment.
- V014-R02 remains the stronger positive enhancement candidate.
- V015 remains a rejected failure reference.
- V016 is an optional correction experiment and cannot replace locked V013 CUT01 without future explicit human approval.

## Canary Result

- Command: `C:\Users\msjpurf\bin\dreamina.exe version`
- Result: passed
- Version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- Command: `C:\Users\msjpurf\bin\dreamina.exe user_credit`
- Result: passed
- User credit summary: user_id `1611200923726843`, vip_level `maestro`, total_credit `2462`
- Logger Access denied: no
- Login/auth failure: no

## Command-Contract Preflight Result

- Command checked: `C:\Users\msjpurf\bin\dreamina.exe multimodal2video -h`
- Task type: `multimodal2video`
- Image inputs: repeatable `--image`
- Minimum input rule: at least one `--image` or `--video` required
- Image limit: `image<=9`
- Selected image count: `3`
- Model version: `seedance2.0_vip`
- Duration: `5`, supported by duration range `4-15s`
- Ratio: `16:9`, supported
- Video resolution: `720p`, supported for `seedance2.0_vip`
- Audio/video reference required: no
- All three upload-safe JPG reference paths exist: yes
- Active references are upload-safe JPG paths: yes
- Original PNG locked refs used as active visual references: no
- `command_contract_valid`: true

## Exact Upload-Safe References Used

1. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
2. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
3. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

## Reference Exclusions Confirmed

- Original PNG locked refs were not used as active visual references.
- No SHOT-02-V009, V010, V011, V012, or V013 frames/media were used as active visual references.
- No V014-R02 MP4/contact sheet was used as an active visual reference.
- No V015 MP4/contact sheet was used as an active visual reference.
- Only the three upload-safe JPG references listed above were passed to Dreamina.

## Submit Command Summary

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V016_uploadsafe_hand_foot_line_steal_prompt.txt'
& 'C:\Users\msjpurf\bin\dreamina.exe' multimodal2video `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg' `
  --prompt $prompt `
  --duration 5 `
  --ratio '16:9' `
  --video_resolution '720p' `
  --model_version 'seedance2.0_vip'
```

No `--poll` flag was passed.

## Submit Response Summary

- Submit attempted: yes
- Submit attempts in this phase: exactly one
- Submit result: accepted for async generation
- `submit_id`: `d51a3b18-7320-4d2a-9890-f0e0e74e2297`
- `logid`: `202606242128201692540470089189AD9`
- `credit_count`: `70`
- `gen_status`: `querying`
- `queue_status`: not returned by submit response
- Failure error: none returned

Important: `submit_id` plus `querying` is not final success. Query/download still requires separate future human authorization.

## Boundaries Confirmed

- Exactly one V016 submit attempt was run in this phase.
- No `query_result` command was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch command was run.
- No media was created or staged.
- Upload-safe JPG files were not staged.
- `.vs/` was not staged.
- V013 lock state was not modified.
- V014-R02 shot record was not modified.
- V015 shot record was not modified.
- V016 `final_master=false`.
- V016 `locked=false`.

## Next Required Step

Future step, only if explicitly approved by the human:

- K76 query/download-if-success for submit_id `d51a3b18-7320-4d2a-9890-f0e0e74e2297`

Do not query, download, retry, resubmit, or treat the task as final without separate authorization.

## Final Verdict

SHOT_02_V016_SUBMITTED_NO_QUERY_NO_DOWNLOAD
