# PHASE K60 - SHOT-02-V014 Upload Failure Diagnostic And R02 Package

Date: 2026-06-24
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass performs local diagnostics on the SHOT-02-V014 reference images, creates upload-safe JPG reference copies, and prepares the SHOT-02-V014-R02 upload-safe package.

- Dreamina was not run.
- No dreamina version or user_credit command was run.
- No multimodal2video command was run.
- No submit/query/download/retry/resubmit/batch happened.
- Runtime code and configs/providers.json were not modified.
- Project Source files were not modified.
- Original locked_refs were not modified, moved, deleted, or overwritten.
- V013 shot record was not modified.
- V013 CUT01 remains the locked current SHOT-02 passed segment.
- Generated upload-safe JPGs were not staged.
- V014-R02 final_master=false and locked=false.

## Why K60 Is Being Done

The original SHOT-02-V014 package passed review, but three live submit attempts failed in the Dreamina upload/auth transport layer:

- K57 failed before valid task creation with authsdk refresh / protocol transport request failure.
- K58 returned a submit_id but `gen_status=fail` during the first reference image upload to imagex.bytedanceapi.com.
- K59 returned a submit_id but `gen_status=fail` during the scene reference upload: upload phase, no file upload.

A fourth direct submit with the same original PNG references is not recommended without upload-safe mitigation.

## K57/K58/K59 Failure Pattern

| Phase | Result | Submit ID | Failure |
|---|---|---|---|
| K57 | failed before valid task creation | none | authsdk refresh failed / protocol transport request failure |
| K58 | gen_status=fail | 489a4946-6365-42f2-a942-bddb725ddc8d | Fenshou reference upload timeout to imagex.bytedanceapi.com |
| K59 | gen_status=fail | 436fc5ef-24ed-4166-bb85-2df60c5437a5 | scene reference upload phase reported no file upload |

No successful queued generation exists from K57, K58, or K59.

## Original Reference Inspection

| Ref | Path | Size Bytes | Format | Dimensions | Color Mode | Alpha | ICC/Profile | SHA256 |
|---|---|---:|---|---|---|---|---|---|
| Fenshou identity | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png | 1959523 | PNG | 1440x2560 | RGB / Format24bppRgb | false | no ICC profile detected | 83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F |
| Shuangji identity | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png | 3874061 | PNG | 1440x2560 | RGB / Format24bppRgb | false | no ICC profile detected | 15339627A18D20C00FFBF1321696C175C451F00CFF621E3E20D1162EC5890E11 |
| Scene/world | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png | 4147285 | PNG | 2560x1440 | RGB / Format24bppRgb | false | no ICC profile detected | 831C8743C019D37334B64A5843C7E595B909F75090DE15BA55FF4730891AF452 |

## Upload-Safe Copies

Output directory:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/

Re-encode settings:

- RGB JPEG
- quality 92
- no crop
- aspect ratio preserved
- dimensions preserved because original long edge was already 2560
- alpha stripped / not present
- unnecessary metadata stripped as practical by drawing into a fresh 24-bit RGB bitmap

| Ref | Upload-Safe Path | Size Bytes | Format | Dimensions | Color Mode | Alpha | ICC/Profile | SHA256 |
|---|---|---:|---|---|---|---|---|---|
| Fenshou identity | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg | 385741 | JPEG | 1440x2560 | RGB / Format24bppRgb | false | no ICC profile detected | 70C01DEC0BC3AA0EADD9F554C731BE4991320B742CB2F9A2F1195A0D4F08BED3 |
| Shuangji identity | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg | 711550 | JPEG | 1440x2560 | RGB / Format24bppRgb | false | no ICC profile detected | FBC0E674E19D74C9BA4B8488E2C4DA79F0A415E1C6811D0613803150BD9BAD1D |
| Scene/world | G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg | 828881 | JPEG | 2560x1440 | RGB / Format24bppRgb | false | no ICC profile detected | F2117D0AC806179DD2AC5F009D3483184B500BA2489512894059379C73BC531B |

## V014-R02 Package Paths

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V014-R02_uploadsafe_multimodal_legwork_hand_foot_combo_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V014-R02_uploadsafe.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V014-R02_uploadsafe.csv`
- Shot record: `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V014-R02_uploadsafe.json`
- Report: `reports/PHASE_K60_SHOT02_V014_UPLOAD_FAILURE_DIAGNOSTIC_AND_R02_PACKAGE.md`

## V014-R02 Package Policy

- shot_id: SHOT-02-V014-R02
- variant_id: uploadsafe
- source_package: SHOT-02-V014
- task_type: multimodal2video
- provider: dreamina_cli
- model_version: seedance2.0_vip
- duration: 4
- video_resolution: 720p
- ratio: 16:9
- submit_allowed=false
- query_allowed=false
- download_allowed=false
- final_master=false
- locked=false
- human_review_required=true
- baseline_locked_version=SHOT-02-V013-CUT01-LOCKED
- replacement_policy: cannot replace locked V013 CUT01 unless human explicitly approves future replacement

## Reference Strategy

V014-R02 uses exactly the 3 upload-safe JPG copies.

The manifest does not include the original PNG refs.

The package does not use V009/V010/V011/V012/V013 frame/media/contact sheet/video paths as visual references.

Reference duties remain unchanged:

1. Fenshou upload-safe JPG = Fenshou identity only.
2. Shuangji upload-safe JPG = highest-priority Shuangji female identity protection only.
3. Scene upload-safe JPG = rainy temple scene/world only.

## Validation Checklist

- V014-R02 prompt JSON parses.
- V014-R02 shot record JSON parses.
- V014-R02 manifest CSV reads.
- The 3 upload-safe JPG files exist locally.
- All 3 upload-safe JPGs are RGB and have no alpha channel.
- V014-R02 prompt JSON and manifest contain no V009/V010/V011/V012/V013 frame/media paths.
- Original locked_refs were not modified.
- submit_allowed=false.
- final_master=false.
- locked=false.
- Manual prompt includes upload-safe @ reference-duty map.
- Negative constraints still include male-coded Shuangji, role swap, duplicate characters, extra limbs, weapons, flying, big jump, big flying kick, acrobatic spin kick, new shockwave, second explosion, text, watermark, slow motion, held-contact choreography, and final pose-out.

## Safety Confirmation

- V013 lock state was not changed.
- Original locked_refs were not modified.
- No Dreamina command was run.
- No submit/query/download happened.
- Generated JPGs were not staged.
- V014-R02 final_master=false.
- V014-R02 locked=false.

## Next Recommended Step

Run K61 package review for the V014-R02 upload-safe package.

Only after K61 passes and the human explicitly approves should any single submit be attempted.

Final verdict:
SHOT_02_V014_R02_UPLOADSAFE_PACKAGE_READY_NO_SUBMIT
