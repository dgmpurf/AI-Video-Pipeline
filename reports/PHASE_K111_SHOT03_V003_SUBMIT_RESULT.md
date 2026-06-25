# PHASE K111 - SHOT-03 V003 Single Submit Result

## Human Authorization

The human explicitly approved K111 for one SHOT-03 V003 upload-safe simplified exterior-column-corridor submit after Dreamina canary and multimodal2video command-contract preflight:

> K110 already manually committed and pushed successfully. K111 is approved: SHOT-03 V003 upload-safe simplified exterior-column-corridor single submit. Codex may run Dreamina canary and multimodal2video command-contract preflight first; if they pass, submit once only. Do not query, do not download, do not retry, do not resubmit. Keep final_master=false and locked=false.

## K110 Context

- Package review phase: PHASE_K110.
- Package review verdict: SHOT03_V003_PACKAGE_REVIEW_READY_FOR_HUMAN_SUBMIT_DECISION.
- K111 is the first human-authorized SHOT-03 V003 submit attempt.
- Submit id is not final success. Future query/download requires separate explicit human authorization.

## V003 Purpose

SHOT-03 V003 is intended to fix V002's choreography overload and face-stability risk by simplifying the shot to exterior veranda / column corridor / railing combat only. The prompt uses a medium or medium-wide camera intent, keeps one stable wet stone floor plane, and excludes roof duel, roof-tile combat, full wet-stair route, temple destruction, weapons, and extreme face close-ups.

## Canary Result

- Command: C:/Users/msjpurf/bin/dreamina.exe version
- Result: passed.
- Version: 46b5b0e-dirty.
- Commit: 46b5b0e.
- Build time: 2026-06-03T19:39:25Z.
- Command: C:/Users/msjpurf/bin/dreamina.exe user_credit
- Result: passed.
- Total credit at canary: 2112.
- VIP level: maestro.
- Logger Access denied: not observed.
- Login/auth failure: not observed.

## Command-Contract Preflight Result

- Command checked: C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h
- Result: passed.
- task_type available: multimodal2video.
- Repeatable --image supported: yes.
- At least one image/video required: yes.
- Image count limit: image<=9, therefore 3 images allowed.
- model_version seedance2.0_vip supported: yes.
- duration=5 supported: yes, supported range is 4-15 seconds.
- ratio=16:9 supported: yes.
- video_resolution=720p supported for seedance2.0_vip: yes.
- Audio/video reference required: no.
- command_contract_valid: true.

## Active Upload-Safe References Used

Exactly three upload-safe JPG references were used:

1. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg
2. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg
3. G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg

Original PNG locked refs were not used as active visual refs. SHOT-03 V001/V002 media or review assets were not used as active visual refs. Prior MP4 files, contact sheets, review frames, and generated media were not used as active visual refs.

## Submit Command Summary

Command summary:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V003_uploadsafe_simplified_exterior_column_corridor_prompt.txt'
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

No --poll flag was passed.

## Submit Response Summary

- Submit attempted: yes.
- Submit attempts count in this phase: 1.
- submit_id: dd7aba19-c468-418a-bcf4-2e9aa0712f94.
- logid: 2026062521030416925404700895796F1.
- credit_count: 70.
- gen_status: querying.
- queue_status: not returned.
- failure reason: none returned.

## Boundaries

- Exactly one submit attempt was run.
- No query_result was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No media was created or staged.
- Upload-safe JPGs were not staged.
- .vs/ was not staged.
- final_master=false.
- locked=false.
- SHOT-02 / V013 / V018 lock states were not changed.

## Next Required Step

Future PHASE_K112 may query/download this exact submit_id only with separate explicit human authorization:

- submit_id: dd7aba19-c468-418a-bcf4-2e9aa0712f94

Final verdict: SHOT03_V003_SUBMITTED_NO_QUERY_NO_DOWNLOAD
