# PHASE K187 - SHOT-04 Route A Single Submit Result

## 1. Purpose

Record the human-authorized K187 L3 one-submit-only execution for the SHOT-04 Route A package:

`SHOT-04-V001 / routeA_railing_lattice_impact_rebound`

This phase performed exactly one Dreamina `multimodal2video` submit with `--poll 0`. It did not query or download.

## 2. Authorization Level and Boundaries

Authorization level: `L3 one-submit only`

Human authorization allowed:

- corrected Dreamina preflight
- exactly one `multimodal2video` submit using the K185/K186-reviewed package
- `--poll 0`
- K187 submit result report

Forbidden in K187:

- query_result
- download
- retry
- resubmit
- batch
- media staging
- final decision
- lock decision
- `sources/` modification

## 3. Preflight Summary

### Git / Source Preflight

- Branch state before submit: `main...origin/main`
- `sources/` status: clean
- Untracked noise: `.vs/` only
- `sources/` was not modified or staged.

### Dreamina Canary

Dreamina executable:

`C:/Users/msjpurf/bin/dreamina.exe`

Version result:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

User credit result:

```json
{
  "total_credit": 1830,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

### Command Contract Preflight

Command checked:

`C:/Users/msjpurf/bin/dreamina.exe multimodal2video -h`

Contract result:

- command exists: true
- supports `--image`: true
- supports repeated image refs: true
- input limit includes image<=9: true
- K187 image refs count: 3
- supports `model_version=seedance2.0_vip`: true
- supports `duration=5` in 4-15s range: true
- supports `ratio=16:9`: true
- supports `video_resolution=720p` for seedance2.0_vip: true
- supports `--poll 0`: true

## 4. Package Used

Prompt file:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt`

Package JSON:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_v001_routeA_railing_lattice_impact_rebound_multimodal2video_package_no_submit.json`

Manifest CSV:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-V001_routeA_no_submit.csv`

K186 package review:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K186_SHOT04_ROUTE_A_PACKAGE_REVIEW_READY_FOR_HUMAN_SUBMIT_DECISION.md`

Package review status before K187:

`pass_ready_for_human_K187_submit_authorization_decision`

## 5. Reference Images Submitted

1. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
2. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
3. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

## 6. Actual Submit Command Shape

The prompt was read from the approved prompt file with UTF-8 encoding.

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt"
C:\Users\msjpurf\bin\dreamina.exe multimodal2video `
  --image "productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg" `
  --image "productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg" `
  --image "productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 5 `
  --ratio 16:9 `
  --video_resolution 720p `
  --poll 0
```

## 7. Submit Result

Submit attempted: yes

Submit count: exactly one

Submit response summary:

```json
{
  "submit_id": "39f10fdc-50c8-4d03-ae59-c1189447300b",
  "logid": "20260628134823169254047008236EE77",
  "gen_status": "querying",
  "credit_count": 70
}
```

Recorded fields:

| field | value |
|---|---|
| submit_id | `39f10fdc-50c8-4d03-ae59-c1189447300b` |
| logid | `20260628134823169254047008236EE77` |
| gen_status | `querying` |
| credit_count | `70` |
| fail_reason | none returned |

## 8. Explicit Non-Actions

- No `query_result` was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
- No media was created.
- No media was staged.
- No final decision was made.
- No lock decision was made.
- No package/prompt/manifest/shot-record files were modified in K187.
- `sources/` was not modified.

## 9. Next Required Phase

Recommended next phase:

K188 query-only authorization for existing submit id:

`39f10fdc-50c8-4d03-ae59-c1189447300b`

K188 should be separately authorized by the human. It should query this exact submit id only. Download should require explicit authorization if not bundled into the K188 scope.

## 10. Safety Confirmation

- corrected Dreamina preflight completed
- exactly one submit executed
- `--poll 0` used
- no query
- no download
- no retry
- no resubmit
- no batch
- no media staged
- `final_master=false`
- `locked=false`

## 11. Final Verdict

SHOT04_ROUTE_A_K187_SUBMITTED_NO_QUERY_NO_DOWNLOAD_PENDING_K188_AUTHORIZATION
