# PHASE K214 - SHOT-04 R02 Submit Failure Triage / Upload-Path Remediation Planning

## Purpose

K214 triages the K213 SHOT-04 R02 Dreamina submit failure and proposes a safe upload-path remediation plan. This is a report-only phase. It does not retry, resubmit, query, download, generate media, create upload-safe derivatives, or modify package files.

## K213 Carry-Forward

- K213 report: `reports/PHASE_K213_SHOT04_R02_L3_DREAMINA_SUBMIT_RESULT.md`
- submit_id: `5612bb09-e22b-4b32-881d-0742c1f57f2b`
- gen_status: `fail`
- fail_reason: `upload resource "productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png": upload image: upload phase, no file upload, please check log for more details`
- failed reference path from CLI response: `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- exactly one submit was run in K213.
- no retry, resubmit, query, or download happened in K213.

Important interpretation: the returned `submit_id` is not a successful queued task because `gen_status=fail`.

## Failed Reference Path Details

Architecture reference inspected:

- label: `WALL_PANEL_ARCHITECTURE_REF`
- relative path used in K213: `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- absolute path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403\a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- exists: yes
- file size: `4196828` bytes
- extension: `.png`
- detected image format: PNG
- dimensions: `2560x1440`
- sha256: `0a319ac0b8ebd060869d6dec0bebfe260a017df85b18c9500f1c1b5a5ecc1f5d`
- relative path length: `148`
- absolute path length: `187`
- relative path depth: `6`
- directory class: `runs/live` generated-result directory

Risk notes:

- The file exists locally and has a nonzero size, so the K213 failure was not caused by a missing local path.
- The failed architecture ref has the longest path, deepest directory, largest landscape dimensions, and largest file size among the four submitted references.
- The path is not over Windows classic `MAX_PATH`, but it is materially more complex than the shorter locked reference paths.

## Other Reference Path Comparison

| Label | Relative Path | Exists | Size Bytes | Format | Dimensions | SHA256 | Relative Length | Absolute Length | Directory Class |
| --- | --- | --- | ---: | --- | --- | --- | ---: | ---: | --- |
| `FENSHOU_IDENTITY_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | yes | `1959523` | PNG | `1440x2560` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | `98` | `137` | `locked_refs` |
| `SHUANGJI_IDENTITY_ANCHOR_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | yes | `3874061` | PNG | `1440x2560` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | `114` | `153` | `locked_refs` |
| `SHUANGJI_FULL_BODY_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | yes | `1752299` | PNG | `1440x2560` | `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a` | `99` | `138` | `locked_refs` |

Comparison notes:

- Two smaller locked refs uploaded successfully according to Dreamina logs: `FENSHOU_IDENTITY_REF` and `SHUANGJI_FULL_BODY_REF`.
- The larger `SHUANGJI_IDENTITY_ANCHOR_REF` also failed upload according to logs, even though the K213 CLI response surfaced the architecture ref as the fail_reason.
- This suggests the issue is not only the `runs/live` path. File size, host upload timeout, and/or PNG upload behavior are likely contributing factors.

## CLI / Log Inspection Summary

Logs inspected:

- `C:\Users\msjpurf\.dreamina_cli\logs\dreamina.log.2026-06-28_23`
- `C:\Users\msjpurf\.dreamina_cli\logs\dreamina.log`

Only non-secret upload-related lines were inspected. No auth/session/token/key/env contents were opened or printed.

Relevant log findings:

- K213 started a `multimodal2video` submit with four image paths.
- `FENSHOU_IDENTITY_REF` upload completed successfully.
- `SHUANGJI_FULL_BODY_REF` upload completed successfully.
- Architecture ref upload failed with `context deadline exceeded` after three attempts against a ByteDance VOD upload host.
- `SHUANGJI_IDENTITY_ANCHOR_REF` upload also failed with `upload phase, no file upload`.
- Resource upload summary: `path_count=4 stored_count=2`.

Representative non-secret log excerpts:

```text
Direct Upload success ... submit_id=5612bb09-e22b-4b32-881d-0742c1f57f2b
[ResourceUpload] upload completed ... path=productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
[ResourceUpload] upload completed ... path=productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png
Fail to upload image ... domain tos-d-x-hl.bytedancevod.com ... All attempts fail:
#1 ... context deadline exceeded
#2 ... context deadline exceeded
#3 ... context deadline exceeded
[ResourceUpload] upload file failed ... path=productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png ... upload phase, no file upload
[ResourceUpload] upload file failed ... path=productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png ... upload phase, no file upload
[ResourceUpload] finished resource_type=image path_count=4 stored_count=2
```

## Likely Cause Assessment

| Possible Cause | Assessment |
| --- | --- |
| Relative path upload issue | Possible but not primary. Two relative locked-ref paths uploaded successfully, while one relative `runs/live` path and one relative `locked_refs` path failed. |
| Long or nested path issue | Possible contributor for the architecture ref. Its absolute path length is `187` and it lives under a deep `runs/live/...` directory, but the Shuangji identity anchor failed from a shorter locked path too. |
| Image metadata / PNG upload issue | Plausible. Both failed files are larger PNGs: architecture `4196828` bytes and Shuangji identity anchor `3874061` bytes. The two smaller PNGs succeeded. |
| File lock / permission issue | Less likely. Files were readable locally, dimensions and hashes were computed, and logs indicate HTTP upload timeouts rather than local open failures. |
| Dreamina CLI upload bug | Plausible. Failure occurred in the upload phase with `no file upload`, `contentType` blank, and upload host context deadlines. |
| CLI cannot upload from `runs/live` reliably | Possible for the architecture ref, but insufficient alone because one locked ref also failed. |
| Reference should be copied to package-local upload-safe path | Strong recommendation. It would simplify path handling and make K215 package state more reproducible. |
| Architecture ref may need lightweight compression/re-encoding | Strong recommendation. It addresses size/PNG/upload timeout risk without changing the locked originals. |
| Network/upload host transient issue | Plausible. Logs show ByteDance VOD upload hosts timing out. K213 boundaries correctly prohibited retrying. |

Overall assessment:

The strongest evidence points to an upload-phase timeout / upload HOST failure, likely aggravated by larger PNG files and possibly by the architecture reference's deep `runs/live` path. Since two of four resources uploaded successfully, reference count alone is not the primary cause.

## Remediation Options

| Option | Description | Expected Benefit | Risk | Creates Media/Copy Artifacts | Requires Human Authorization | Changes Reference Strategy | Preserves final_master=false / locked=false |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | Use absolute paths in submit command only | Reduces relative-path ambiguity | Does not address large PNG upload timeout; failed locked ref suggests path is not sole issue | no | yes | no | yes |
| B | Create package-local upload-safe copies under a shorter path | Shorter, uniform paths; keeps package reproducible | Copies media; must avoid treating copies as locked/final | yes, copies | yes | no | yes |
| C | Create lightly re-encoded/compressed upload-safe derivative for architecture ref only | Reduces largest file and deep path risk | Does not address Shuangji identity anchor failure | yes, derivative | yes | no, if duty remains architecture ref | yes |
| D | Create package-local upload-safe copies or derivatives for all four refs | Most consistent path/size remediation; handles both failed files and keeps submit command simple | Creates multiple media artifacts; requires careful metadata and no media staging | yes, copies/derivatives | yes | no | yes |
| E | Re-run submit with same assets but absolute paths | Fastest minimal change | Risky: may repeat upload timeout; violates no-retry unless separately authorized | no | yes | no | yes |
| F | Reduce to 3 refs only if upload failure appears reference-count-related | Lowers upload burden | Changes reference strategy and weakens identity/architecture duties; evidence does not point primarily to reference count | no or yes depending implementation | yes | yes | yes |

## Recommended K215

Recommended next phase:

K215 = SHOT-04 R02 Upload-Safe Reference Packaging, No Submit.

Suggested K215 scope:

- Create package-local upload-safe copies or lightly re-encoded derivatives under:
  `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/`
- Preserve all locked originals.
- Do not modify locked refs.
- Do not stage media files unless a later task explicitly authorizes media staging; if media artifacts are generated, keep them uncommitted or follow explicit project media policy.
- Record each upload-safe reference path, sha256, dimensions, format, and source lineage.
- Prefer upload-safe derivatives for at least the two larger failed files:
  - `WALL_PANEL_ARCHITECTURE_REF`
  - `SHUANGJI_IDENTITY_ANCHOR_REF`
- Consider package-local upload-safe copies or derivatives for all four refs for command consistency.
- Update package JSON/manifest to point to upload-safe package-local refs only if explicitly authorized in K215.
- Keep `submit_allowed=false`, `query_allowed=false`, `download_allowed=false`, `final_master=false`, and `locked=false`.
- Then run K216 submit-readiness re-review before any new submit authorization.

Rationale:

Absolute paths alone are not the safest next step because the logs show a second failure from a shorter `locked_refs` path. Upload-safe package-local references and possible lightweight re-encoding address both path complexity and large PNG upload timeout risk while respecting no-retry boundaries.

## Boundary Confirmation

- No Dreamina submit was run in K214.
- No query or download was run.
- No retry or resubmit was run.
- No batch action was run.
- No media was generated.
- No upload-safe derivative files were created.
- No media was staged.
- No package, prompt, manifest, shot record, or locked reference was modified.
- No final or locked state was set.
- `final_master=false`.
- `locked=false`.

## Source Governance Confirmation

- `sources/` was checked and remained clean.
- No Source file was modified, staged, committed, or pushed.
- No runtime code or `configs/providers.json` was modified.
- No auth/session/token/key/env file was opened, copied, printed, staged, or committed.

## Final Verdict

SHOT04_R02_SUBMIT_FAILURE_TRIAGE_READY_K215_UPLOAD_SAFE_REFERENCE_PACKAGING_NO_SUBMIT
