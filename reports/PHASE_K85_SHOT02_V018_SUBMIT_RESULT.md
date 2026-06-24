# PHASE K85 - SHOT-02-V018 Upload-Safe Single Submit Result

## Human Authorization

The human explicitly approved one V018 upload-safe submit:

> 批准 V018 upload-safe 单次 submit。允许 Codex 先跑 Dreamina canary 和 multimodal2video command-contract preflight；通过后只 submit 一次。不要 query，不要 download，不要 retry，不要 resubmit。

This pass was limited to Dreamina canary, `multimodal2video -h` command-contract preflight, exactly one submit, and text metadata/report updates.

## Package Review Context

- Package review: `reports/PHASE_K84_SHOT02_V018_PACKAGE_REVIEW.md`
- K84 package verdict: `SHOT_02_V018_PACKAGE_REVIEW_READY_FOR_HUMAN_SUBMIT_APPROVAL`
- V018 package status before submit: `package_ready_no_submit`
- V018 role: optional hard-impact fast upper-body correction experiment
- This is the first explicit human-authorized V018 submit attempt.
- V018 is not final master and is not locked.
- Baseline lock remains: `SHOT-02-V013-CUT01-LOCKED`
- Replacement policy: V018 cannot replace locked V013 CUT01 unless the human explicitly approves a future replacement.

## Canary Result

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- `dreamina version`: passed
- Version: `46b5b0e-dirty`
- Commit: `46b5b0e`
- Build time: `2026-06-03T19:39:25Z`
- `dreamina user_credit`: passed
- User id: `1611200923726843`
- VIP level: `maestro`
- Total credit before submit: `2322`
- Logger Access denied: not observed
- Login/auth failure: not observed

## Command-Contract Preflight Result

- Command checked: `C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h`
- Task type: `multimodal2video`
- Image input: supported and repeatable via `--image`
- At least one image/video required: yes
- Image input limit: `image<=9`
- Selected image count: `3`
- Model version: `seedance2.0_vip`
- Duration: `5`, supported by the local help range `4-15s`
- Ratio: `16:9`, supported
- Video resolution: `720p`, supported for `seedance2.0_vip`
- Audio/video reference required: no
- Active references exist: yes
- Active references are upload-safe JPG paths, not original PNG locked refs: yes
- `command_contract_valid`: true

## Exact Upload-Safe References Used

1. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
2. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
3. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

Original PNG locked refs were not used as active visual references. No V009, V010, V011, V012, or V013 frames/media were used as active visual references. The V014-R02 MP4/contact sheet, V015 MP4/contact sheet, V016 MP4/contact sheet, and V017 MP4/contact sheet were not used as active visual references.

## Submit Command Summary

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V018_uploadsafe_hard_impact_fast_upperbody_prompt.txt'
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

- Submit attempted: yes
- Submit attempts in this phase: `1`
- Submit id: `9a29b16f-e1a5-4d48-bb60-6d8dcabcca77`
- Log id: `202606242353591692540470088626B09`
- Credit count: `70`
- Gen status: `querying`
- Queue status: not returned
- Submit response status: accepted / querying
- Submit id is not final success. Future query/download is required and needs separate explicit human approval.

## Boundaries Confirmed

- Exactly one V018 submit attempt in this phase: yes
- `query_result` run: no
- Download run: no
- Retry run: no
- Resubmit run: no
- Batch run: no
- Media created or staged: no
- Upload-safe JPGs staged: no
- `.vs/` staged: no
- V013 lock state unchanged
- V014-R02 shot record unchanged
- V015 shot record unchanged
- V016 shot record unchanged
- V017 shot record unchanged
- V018 `final_master=false`
- V018 `locked=false`
- Final video approval requires future human review after future download.

## Next Required Step

If the human approves, future K86 should query/download this exact submit id only:

`9a29b16f-e1a5-4d48-bb60-6d8dcabcca77`

Do not submit another V018 task unless the human explicitly authorizes a new submit attempt.

## Final Verdict

SHOT_02_V018_SUBMITTED_NO_QUERY_NO_DOWNLOAD
