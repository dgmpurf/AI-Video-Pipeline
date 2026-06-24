# PHASE K71 - SHOT-02-V015 Download Result

Date: 2026-06-24
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass downloaded the existing SHOT-02-V015 submit result exactly once, validated the local MP4, and created review frames plus a contact sheet.

- Exactly one `query_result --download_dir` command was run.
- No retry happened.
- No resubmit happened.
- No new generation command was run.
- No media was staged.
- Runtime code, configs/providers.json, and Project Source files were not modified.
- V013 shot record was not modified.
- V014-R02 shot record was not modified.
- V015 final_master=false.
- V015 locked=false.

## Human Authorization

The human approved continuing the normal separated flow after K70 query success. This is K71 download-only for V015.

## K69 / K70 Context

| Field | Value |
|---|---|
| submit_id | bf1f4ca2-0cce-492d-a128-dba16bffc72c |
| logid | 20260624164032172018000001705ABF7 |
| K69 submit status | querying |
| K69 credit_count | 70 |
| K70 gen_status | success |
| K70 queue_status | Finish |
| K70 result availability | video_result_available_not_downloaded |
| K70 expected metadata | mp4, 1280x720, 24 fps, duration=5.042s |

## Canary Result

`dreamina version` succeeded.

| Field | Value |
|---|---|
| version | 46b5b0e-dirty |
| commit | 46b5b0e |
| build_time | 2026-06-03T19:39:25Z |

`dreamina user_credit` succeeded.

| Field | Value |
|---|---|
| user_id | 1611200923726843 |
| vip_level | maestro |
| total_credit_before_download | 2462 |

No logger Access denied error occurred.

No login/auth failure occurred.

## Download Command Used

```powershell
& 'C:\Users\msjpurf\bin\dreamina.exe' query_result --submit_id=bf1f4ca2-0cce-492d-a128-dba16bffc72c --download_dir 'G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V015_20260624_164032/'
```

The generic downloaded file was renamed within the same run directory to the standardized output name.

## Download Result

Local MP4:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V015_20260624_164032/SHOT-02-V015_uploadsafe_fast_hand_exchange_micro_fx.mp4

| Field | Value |
|---|---|
| exists | true |
| sha256 | C9039A7C0E1CA5DC52564DA8689C90348169FDD1A8540799E7D2287EDDC036F9 |
| file_size_bytes | 9501011 |
| duration_seconds | 5.016667 |
| container_duration_seconds | 5.085011 |
| resolution | 1280x720 |
| fps / avg_frame_rate | 24.119601 |
| r_frame_rate | 60 |
| frame_count | 121 |
| video_codec | h264 |

The tiny difference from K70 duration metadata is within normal container/probe variance and is not treated as a validation failure.

## Contact Sheet / Review Frames

Review directory:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V015/

Contact sheet:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V015/SHOT-02-V015_contact_sheet.jpg

Contact sheet sha256:

512895D2CED53A43E2B9FAD6DEFED735A36BDBFDBA73D41ED742A69682DBD82D

Review frames:

| Frame | Timestamp | SHA256 |
|---|---:|---|
| frame_00.jpg | 0.00s | 317DDE6D9E639E28E2D2812C38EEE12D46386F33F3E0260617F3BB0A596FDAA4 |
| frame_01.jpg | 1.00s | 6CCA4949955AA0A995956003622BFA693CEDB091C312F610322BE579F56053C2 |
| frame_02.jpg | 2.00s | E8362C2CBDAF0CCFF1A8330C970FDE1BF177951C812848602C51327F01F39CD1 |
| frame_03.jpg | 3.00s | D6E04F8A1CE60D5600B2D37ECB45375F2D2E78942BA55983F6772662B9B26130 |
| frame_04.jpg | 4.00s | 9E77F1A323AD930855CFECAAD3460D01644EF95A3C923CAC41A2A894018DB9F3 |
| frame_05.jpg | 5.00s | C864E87079C1DE634D16C20367524611BAA1A4C1E41A3DCEA3FA13CC2DBC68A2 |

## Boundaries Confirmed

- Exactly one `query_result --download_dir` command was run.
- No retry happened.
- No resubmit happened.
- No media was staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- V013 lock state was unchanged.
- V014-R02 shot record was unchanged.
- V015 final_master=false.
- V015 locked=false.

## Next Required Step

Human visual review of the MP4 and contact sheet is required.

Optional Codex visual review should happen only if the human asks.

No final/lock decision should be made without explicit human approval.

Final verdict:
SHOT_02_V015_DOWNLOADED_PENDING_HUMAN_REVIEW
