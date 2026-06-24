# PHASE K80 - SHOT-02-V017 Single Submit Result

## Human Authorization

The user explicitly authorized one Dreamina `multimodal2video` submit for `SHOT-02-V017_uploadsafe_fast_upperbody_refined_particles`.

Execution boundaries:

- Submit exactly once.
- Do not query.
- Do not download.
- Do not retry.
- Do not resubmit.
- Do not batch.
- Do not run `--poll`.
- Do not mark final master.
- Do not lock.
- Final video approval requires future human review after a separately authorized query/download.

## K79 Context

`reports/PHASE_K79_SHOT02_V017_PACKAGE_REVIEW.md` reviewed the package as ready for human submit approval.

Important package context:

- `SHOT-02-V013-CUT01-LOCKED` remains the locked baseline.
- `SHOT-02-V014-R02_uploadsafe` is the positive action-quality reference.
- `SHOT-02-V016_uploadsafe` is the positive-with-notes action reference.
- `SHOT-02-V015_uploadsafe` is the failure reference.
- `SHOT-02-V017` is an optional correction experiment for faster upper-body close combat and refined particle feedback.

## Canary Result

Result: pass.

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Dreamina version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- `user_credit`: succeeded
- Account credit at submit canary: `2392`
- VIP level: `maestro`

## Command-Contract Preflight

Result: pass.

Checked command:

```powershell
C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h
```

Confirmed:

- `task_type=multimodal2video`
- `model_version=seedance2.0_vip` is supported
- `duration=5` is within supported `4-15s`
- `ratio=16:9` is supported
- `video_resolution=720p` is supported for `seedance2.0_vip`
- `--image` is repeatable
- image input limit is `image<=9`
- exactly three active image references were used
- command contract valid: true

## Active References Used

1. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
2. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
3. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

Excluded:

- Original PNG locked references were not used as active references.
- V014-R02 MP4/contact sheet were not used as active visual references.
- V015 MP4/contact sheet were not used as active visual references.
- V016 MP4/contact sheet were not used as active visual references.
- V009/V010/V011/V012/V013 frames, cut frames, contact sheets, and downloaded video frames were not used as active visual references.

## Exact Submit Command

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 -LiteralPath 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V017_uploadsafe_fast_upperbody_refined_particles_prompt.txt'
& 'C:/Users/msjpurf/bin/dreamina.exe' multimodal2video `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg' `
  --image 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg' `
  --prompt $prompt `
  --duration 5 `
  --ratio '16:9' `
  --video_resolution '720p' `
  --model_version 'seedance2.0_vip'
```

No `--poll` was used.

## Submit Response Summary

Result: valid task accepted by Dreamina.

- `submit_id`: `8ffd960c-e1df-41dd-89a1-c18c9c1a12e7`
- `logid`: `20260624222858169254047008970B607`
- `credit_count`: `70`
- `gen_status`: `querying`
- `queue_status`: not returned

## Boundaries Confirmed

- Exactly one submit was run.
- No `query_result` was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch command was run.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- V013/V014-R02/V015/V016 shot records were not modified.
- `final_master=false`.
- `locked=false`.
- Human review remains required after future download.

## Next Required Step

Future step requires explicit user authorization:

```powershell
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 8ffd960c-e1df-41dd-89a1-c18c9c1a12e7
```

If a later query succeeds, download and human review must be handled in a separate authorized phase.

## Final Verdict

SHOT_02_V017_SUBMITTED_NO_QUERY_NO_DOWNLOAD
