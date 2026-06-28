# PHASE K215 - SHOT-04 R02 Upload-Safe Reference Packaging, No Submit

## Purpose

K215 creates package-local upload-safe reference files for SHOT-04 R02 and updates no-submit package metadata to point to those local upload-safe refs. This is remediation packaging only. It does not submit, query, download, retry, resubmit, batch, generate new scene/action media, stage media, mark final, or lock.

## K214 Carry-Forward

- K214 report: `reports/PHASE_K214_SHOT04_R02_SUBMIT_FAILURE_TRIAGE_UPLOAD_PATH_REMEDIATION_PLANNING.md`
- K213 submit_id: `5612bb09-e22b-4b32-881d-0742c1f57f2b`
- K213 gen_status: `fail`
- K213 failure class: upload-phase timeout / upload-host failure.
- K214 log finding: `path_count=4 stored_count=2`.
- Refs uploaded successfully in K213: `FENSHOU_IDENTITY_REF`, `SHUANGJI_FULL_BODY_REF`.
- Refs that failed in K213: `WALL_PANEL_ARCHITECTURE_REF`, `SHUANGJI_IDENTITY_ANCHOR_REF`.
- K214 recommendation: create upload-safe package-local refs, preserve originals, keep no-submit boundaries, then run K216 submit-readiness re-review.

## Files Modified

- `productions/chi_yan_tian_qiong/prompts/shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit.csv`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/README.md`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/reference_duty_map.md`

## Files Created

Text report:

- `reports/PHASE_K215_SHOT04_R02_UPLOAD_SAFE_REFERENCE_PACKAGING_NO_SUBMIT.md`

Local media artifacts, not staged and not committed:

- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_wall_panel_arch_ref_upload_safe.jpg`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_fenshou_identity_upload_safe.jpg`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_identity_anchor_upload_safe.jpg`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_full_body_upload_safe.jpg`

## Upload-Safe Refs Created

Method for all four refs:

- local re-encode to JPG
- JPEG quality: `90`
- long edge resized to `1920`
- no crop
- no content redesign
- original source files preserved unchanged

| Original Reference ID | Original Path | Original SHA256 | Upload-Safe Local Path | Upload-Safe SHA256 | Format | Dimensions | Size Bytes | Method |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| `WALL_PANEL_ARCHITECTURE_REF` | `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png` | `0a319ac0b8ebd060869d6dec0bebfe260a017df85b18c9500f1c1b5a5ecc1f5d` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_wall_panel_arch_ref_upload_safe.jpg` | `1fb81bb7dadf476b82dd675b7942ff22acf0f520433a838826b06a3307c836cc` | JPG | `1920x1080` | `413694` | re-encode/compress |
| `FENSHOU_IDENTITY_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_fenshou_identity_upload_safe.jpg` | `5858915575eb0fef7dea1448aa149ee3543ec0af3581acbeab07d9bd0bb06743` | JPG | `1080x1920` | `264243` | re-encode/compress |
| `SHUANGJI_IDENTITY_ANCHOR_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_identity_anchor_upload_safe.jpg` | `036760c0d8fd48a5d010328396c29d95392ec380a38039dd0a2ad4963aaf52b9` | JPG | `1080x1920` | `386471` | re-encode/compress |
| `SHUANGJI_FULL_BODY_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_full_body_upload_safe.jpg` | `db80fd001611f19762593cacbb8ba225a09a9d2db59a53ce355aa28cb8794086` | JPG | `1080x1920` | `248965` | re-encode/compress |

## JSON Update Summary

Package JSON was updated to:

- keep `package_id` unchanged.
- keep `task_type=multimodal2video`.
- keep `model_version=seedance2.0_vip`.
- keep `duration=5`.
- keep `ratio=16:9`.
- keep `video_resolution=720p`.
- keep the preferred 4-reference strategy.
- preserve `original_reference_map`.
- update active `reference_map` entries to package-local upload-safe paths.
- add original path / original sha256 lineage on each active reference entry.
- add upload-safe metadata: format, dimensions, size bytes, method.
- set `upload_safe_refs_created=true`.
- set `upload_safe_refs_committed=false`.
- set `upload_safe_refs_local_only=true`.
- set `upload_safe_ref_dir=productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/`.
- set `upload_safe_package_status=upload_safe_refs_packaged_no_submit`.
- set `package_status=upload_safe_refs_packaged_no_submit`.
- set recommended next phase to K216 submit-readiness re-review.
- keep no-submit/final/lock flags false.

## CSV Update Summary

Manifest CSV was updated to:

- keep exactly one row.
- keep task metadata unchanged.
- keep the same four reference IDs.
- update `reference_paths` to the package-local upload-safe paths.
- add `upload_safe_sha256s`.
- add `original_reference_paths`.
- set `status=upload_safe_refs_packaged_no_submit`.
- keep `submit_allowed=false`.
- keep `query_allowed=false`.
- keep `download_allowed=false`.
- keep `final_master=false`.
- keep `locked=false`.
- keep `human_review_required=true`.

## README / Reference Duty Map Update Summary

- README now records K215 upload-safe packaging status, local upload-safe paths, sha256 values, method, media staging rule, and recommended K216.
- Reference duty map now points active references to upload-safe paths while preserving original source paths and original sha256 values.
- Duties remain unchanged.
- Upload-safe refs are documented as local submit helpers only.
- Originals remain authoritative for lineage.
- Upload-safe refs are not final and not locked.

## Validation Results

K215 validation passed:

- JSON parse: ok.
- CSV read: ok.
- Upload-safe refs exist locally: yes.
- Upload-safe refs have nonzero size: yes.
- Upload-safe dimensions and format are readable: yes.
- Upload-safe sha256 values recorded: yes.
- Package JSON active reference paths point to upload-safe refs: yes.
- Manifest CSV reference paths point to upload-safe refs: yes.
- Original refs remain present and unchanged.
- Prompt sha256 unchanged: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`.
- `submit_allowed=false`.
- `query_allowed=false`.
- `download_allowed=false`.
- `final_master=false`.
- `locked=false`.
- `sources/` clean.

## Media Staging Confirmation

- Upload-safe media created locally: yes.
- Upload-safe media staged: no.
- Upload-safe media committed: no.
- Media directory remains local-only: `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/`.

## No-Submit Boundary Confirmation

- No Dreamina submit was run.
- No retry or resubmit was run.
- No query or download was run.
- No batch action was run.
- No contact sheet or review frames were created.
- No new scene/action media was generated.
- No media was staged.
- No source update happened.
- No final or locked state was set.

## Known Limitations

K215 does not prove that Dreamina upload will succeed. It only prepares shorter, smaller, package-local upload-safe refs to reduce upload failure risk. K216 must re-review the upload-safe package before any new human L3 submit authorization.

## Recommended K216

K216 = SHOT-04 R02 Upload-Safe Package Submit-Readiness Review, No Submit.

## Final Verdict

SHOT04_R02_UPLOAD_SAFE_REFERENCE_PACKAGING_NO_SUBMIT_READY_K216_SUBMIT_READINESS_REVIEW
