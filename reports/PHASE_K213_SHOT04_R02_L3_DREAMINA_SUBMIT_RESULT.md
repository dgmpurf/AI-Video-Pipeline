# PHASE K213 - SHOT-04 R02 L3 Dreamina Submit Result

## Purpose

K213 executed the human-authorized L3 Dreamina submit-only step for SHOT-04 R02 using the K211/K212-reviewed no-submit package. This phase was submit-only: no query, no download, no retry, no resubmit, no batch, no media staging, no final, and no lock.

## Human L3 Authorization Summary

The human explicitly authorized SHOT-04 R02 to enter L3 Dreamina submit using:

- package_id: `SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit`
- task_type: `multimodal2video`
- model_version: `seedance2.0_vip`
- duration: `5`
- ratio: `16:9`
- video_resolution: `720p`
- prompt_sha256: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`
- 4-reference strategy
- exactly one submit
- no query
- no download
- no retry
- no resubmit

## Package Inspected

- `productions/chi_yan_tian_qiong/prompts/shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit.csv`
- `productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt`
- `reports/PHASE_K211_SHOT04_R02_PACKAGE_PROMPT_FIX_NO_SUBMIT.md`
- `reports/PHASE_K212_SHOT04_R02_PACKAGE_FILE_SUBMIT_READINESS_REVIEW_NO_SUBMIT.md`

## Package Validation Results

Pre-submit package validation passed:

- JSON parse: ok.
- CSV read: ok.
- CSV rows: `1`.
- package_id: `SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit`.
- task_type: `multimodal2video`.
- model_version: `seedance2.0_vip`.
- duration: `5`.
- ratio: `16:9`.
- video_resolution: `720p`.
- reference_count: `4`.
- all four reference paths exist locally.
- `submit_allowed=false`.
- `query_allowed=false`.
- `download_allowed=false`.
- `human_review_required=true`.
- `final_master=false`.
- `locked=false`.

## Prompt SHA256 Validation

- Expected prompt sha256: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`
- Prompt file sha256: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`
- JSON prompt sha256: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`
- CSV prompt sha256: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`
- Result: pass.

## Reference List And Existence Validation

| Label | Path | Exists |
| --- | --- | --- |
| `WALL_PANEL_ARCHITECTURE_REF` | `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png` | yes |
| `FENSHOU_IDENTITY_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | yes |
| `SHUANGJI_IDENTITY_ANCHOR_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | yes |
| `SHUANGJI_FULL_BODY_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | yes |

Additional local check after submit failure: the first architecture reference file still exists locally and has nonzero size (`4196828` bytes). The Dreamina failure occurred during CLI upload, not because the local path was missing.

## Dreamina Preflight Result

Dreamina executable:

- `C:\Users\msjpurf\bin\dreamina.exe`

Version:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

User credit:

```json
{
  "total_credit": 1759,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

Command-contract preflight:

- `dreamina multimodal2video -h` completed successfully.
- Supports repeated `--image`.
- Requires at least one image or video.
- Image limit: `image<=9`.
- Supports `seedance2.0_vip`.
- Supports duration `4-15`.
- Supports ratio `16:9`.
- Supports `720p` for `seedance2.0_vip`.
- `--poll 0` disables polling.

## Exact Submit Command Used

Shape used, with prompt body omitted from the report:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt"
& "C:\Users\msjpurf\bin\dreamina.exe" multimodal2video `
  --image "productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png" `
  --image "productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" `
  --image "productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png" `
  --image "productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 5 `
  --ratio "16:9" `
  --video_resolution 720p `
  --poll 0
```

Submit count: exactly `1`.

## Submit Result

Dreamina returned:

- submit_id: `5612bb09-e22b-4b32-881d-0742c1f57f2b`
- gen_status: `fail`
- logid: not returned
- credit_count: not returned
- queue/status fields: not returned
- fail_reason: `upload resource "productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png": upload image: upload phase, no file upload, please check log for more details`

Important interpretation:

- A `submit_id` was returned, but `gen_status=fail`.
- This is not a successful queued generation.
- No query was run.
- No download was run.
- No retry or resubmit was attempted.

## Boundary Confirmation

- Exactly one submit command was executed.
- No retry.
- No resubmit.
- No batch.
- No query.
- No download.
- No contact sheet.
- No review frames.
- No media staging.
- No package/prompt/manifest mutation.
- No shot record mutation.
- No final.
- No lock.
- `final_master=false`.
- `locked=false`.

## Source Governance Confirmation

- `sources/` was checked and remained clean.
- No Source file was modified, staged, committed, or pushed.
- No runtime code or `configs/providers.json` was modified.
- No auth/session/token/key/env file was opened, printed, staged, or committed.

## Git Staged Files

Expected staged file for K213:

- `reports/PHASE_K213_SHOT04_R02_L3_DREAMINA_SUBMIT_RESULT.md`

## Recommended K214

Because the submit returned `gen_status=fail`, K214 should not be a query/download phase yet.

Recommended next phase:

K214 = SHOT-04 R02 submit failure triage / upload-path remediation planning, no Dreamina retry unless separately authorized by the human.

The likely focus is the first architecture reference upload failure. Possible later fixes may include creating an upload-safe derivative reference or moving/copying the architecture reference to a shorter package-local path, but no such action is authorized in K213.

## Final Verdict

SHOT04_R02_L3_DREAMINA_SUBMIT_FAILED_NO_RETRY_NO_QUERY_NO_DOWNLOAD
