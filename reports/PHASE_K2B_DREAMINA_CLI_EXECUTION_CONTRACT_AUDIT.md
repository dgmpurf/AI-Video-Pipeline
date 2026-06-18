# PHASE K2B: Dreamina CLI Execution Contract Audit

Date: 2026-06-18

## Scope

- Audit the actual local Dreamina CLI execution contract before further generation.
- Problem under audit: SHOT-02-V002 used `image2video + seedance2.0_vip + duration=2`, but the local CLI may not support that combination.
- This report compares current CLI facts against project assumptions that may have come from Dreamina Web behavior.
- No Dreamina submit, query_result, list_task, download, media generation, prompt edit, Source edit, runtime code edit, configs/providers.json edit, or SHOT metadata edit was performed for this audit.

## Executable And Version

- Executable path: `C:\Users\msjpurf\bin\dreamina.exe`
- PowerShell command source: `C:\Users\msjpurf\bin\dreamina.exe`
- File version shown by PowerShell: `0.0.0.0`

`dreamina version` output:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

## Allowed Audit Commands Run

- `dreamina version`
- `dreamina image2video -h`
- `dreamina text2video -h`
- `dreamina frames2video -h`
- `dreamina multiframe2video -h`
- `dreamina multimodal2video -h`
- `dreamina image2image -h`
- `dreamina text2image -h`

No submit/query/download/list_task command was run as part of this audit.

## Actual CLI Help Summary

### image2video

- Input: exactly one local `--image`.
- Ratio: inferred from the input image; not set on this command.
- Advanced `model_version` values:
  - `3.0`, `3.0fast`, `3.0pro`, `3.0_fast`, `3.0_pro`
  - `3.5pro`, `3.5_pro`
  - `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`
- Duration ranges:
  - `3.0/3.0fast/3.0pro`: 3-10 seconds
  - `3.5pro`: 4-12 seconds
  - `seedance2.0 family`: 4-15 seconds
- Resolution:
  - `seedance2.0_vip`: `720p` or `1080p`
  - all other models: `720p`
- Default duration: 5 seconds.

### text2video

- Input: text prompt only.
- Supported models:
  - `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`
- Ratio values: `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9`.
- Duration range: 4-15 seconds for all supported models.
- Resolution:
  - `seedance2.0_vip`: `720p` or `1080p`
  - all other models: `720p`
- Default model: `seedance2.0fast`.
- Default duration: 5 seconds.

### frames2video

- Input: exactly two local images: `--first` and `--last`.
- Ratio: inferred from the first frame image size.
- Supported models:
  - `3.0`, `3.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`
- Duration ranges:
  - `3.0`: 3-10 seconds
  - `3.5pro`: 4-12 seconds
  - `seedance2.0 family`: 4-15 seconds
- Resolution:
  - `seedance2.0_vip`: `720p` or `1080p`
  - all other models: `720p`
- Default model: `seedance2.0fast`.
- Default duration: 5 seconds.

### multiframe2video

- Input: 2-20 local images via `--images`.
- For exactly 2 images: use shorthand `--prompt` and optional `--duration`.
- For 3+ images: repeat `--transition-prompt` once per transition and optionally repeat `--transition-duration`.
- Ratio: inferred from the first image.
- Model and video_resolution overrides: not supported by this command.
- Segment duration: each duration segment is limited to 0.5-8 seconds.
- Total duration must be at least 2 seconds.
- Default duration per segment: 3 seconds.

### multimodal2video

- Input: any mix of `--image`, `--video`, and `--audio`.
- Requirement: at least one `--image` or `--video`.
- Input limits: image <= 9, video <= 3, audio <= 3.
- Audio inputs must be 2-15 seconds.
- Supported models:
  - `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`
- Ratio values: `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9`.
- Duration range: 4-15 seconds.
- Resolution:
  - `seedance2.0_vip`: `720p` or `1080p`
  - all other models: `720p`
- Described by CLI help as the all-around reference mode corresponding to Dreamina Web's 全能参考.

### image2image

- Input: 1-10 local images.
- Supported models: `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`.
- Ratio values: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`.
- Resolution types: `2k`, `4k`.
- Note: `1k` is not supported for image2image.

### text2image

- Input: text prompt only.
- Supported models: `3.0`, `3.1`, `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`.
- Ratio values: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`.
- Resolution types:
  - `3.0/3.1`: `1k` or `2k`
  - `4.0/4.1/4.5/4.6/4.7/5.0`: `2k` or `4k`

## Current CLI-Supported Execution Matrix

| task_type | model_version | allowed duration | allowed resolution | ratio rule | input count / input rule |
| --- | --- | --- | --- | --- | --- |
| image2video | `3.0`, `3.0fast`, `3.0pro`, `3.0_fast`, `3.0_pro` | 3-10s | `720p` | inferred from input image; no ratio flag | exactly one `--image` |
| image2video | `3.5pro`, `3.5_pro` | 4-12s | `720p` | inferred from input image; no ratio flag | exactly one `--image` |
| image2video | `seedance2.0`, `seedance2.0fast`, `seedance2.0fast_vip` | 4-15s | `720p` | inferred from input image; no ratio flag | exactly one `--image` |
| image2video | `seedance2.0_vip` | 4-15s | `720p` or `1080p` | inferred from input image; no ratio flag | exactly one `--image` |
| text2video | `seedance2.0`, `seedance2.0fast`, `seedance2.0fast_vip` | 4-15s | `720p` | explicit ratio allowed | prompt only |
| text2video | `seedance2.0_vip` | 4-15s | `720p` or `1080p` | explicit ratio allowed | prompt only |
| frames2video | `3.0` | 3-10s | `720p` | inferred from first frame; no ratio flag | exactly two images: `--first`, `--last` |
| frames2video | `3.5pro` | 4-12s | `720p` | inferred from first frame; no ratio flag | exactly two images: `--first`, `--last` |
| frames2video | `seedance2.0`, `seedance2.0fast`, `seedance2.0fast_vip` | 4-15s | `720p` | inferred from first frame; no ratio flag | exactly two images: `--first`, `--last` |
| frames2video | `seedance2.0_vip` | 4-15s | `720p` or `1080p` | inferred from first frame; no ratio flag | exactly two images: `--first`, `--last` |
| multiframe2video | model override not supported | segment 0.5-8s; total >= 2s | override not supported | inferred from first image; no ratio flag | 2-20 images; N images require N-1 transition segments |
| multimodal2video | `seedance2.0`, `seedance2.0fast`, `seedance2.0fast_vip` | 4-15s | `720p` | explicit ratio allowed | image <= 9, video <= 3, audio <= 3; at least one image or video |
| multimodal2video | `seedance2.0_vip` | 4-15s | `720p` or `1080p` | explicit ratio allowed | image <= 9, video <= 3, audio <= 3; at least one image or video |
| image2image | `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0` | not a video duration command | `2k` or `4k` | explicit ratio allowed | 1-10 images |
| text2image | `3.0`, `3.1` | not a video duration command | `1k` or `2k` | explicit ratio allowed | prompt only |
| text2image | `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0` | not a video duration command | `2k` or `4k` | explicit ratio allowed | prompt only |

## Duration 1s / 2s Support In This CLI

| command | duration=1 | duration=2 | Notes |
| --- | --- | --- | --- |
| image2video | not supported | not supported | Lowest image2video duration is 3s for 3.0 family, 4s for 3.5pro and seedance2.0 family. |
| text2video | not supported | not supported | Supported range is 4-15s. |
| frames2video | not supported | not supported | Lowest frames2video duration is 3s for 3.0, 4s for 3.5pro and seedance2.0 family. |
| multiframe2video | conditionally supported as a segment if total duration >= 2s | supported for exactly 2 images or as segment if total duration >= 2s | This is not the same contract as image2video and does not support model/resolution overrides. |
| multimodal2video | not supported | not supported | Supported range is 4-15s. |

## Comparison Against Project Assumptions

| Assumption / Prior Practice | Actual Local CLI Fact | Result |
| --- | --- | --- |
| Dreamina video duration may start at 1s and is integer-based | This may be true for Dreamina Web or another interface, but current local CLI help does not support 1s for image2video/text2video/frames2video/multimodal2video. | Web behavior must not be treated as CLI contract. |
| SHOT-02-V002 package used `image2video + seedance2.0_vip + duration=2` | Current CLI says `image2video + seedance2.0_vip` supports 4-15s. | Command-contract-invalid for current CLI image2video. |
| Previous project sources may say Seedance 2.0 image2video supports 4-15s | Current CLI help confirms seedance2.0 family image2video supports 4-15s. | Confirmed for this local CLI build. |
| `ratio` should be omitted for image2video | Current CLI help says ratio is inferred from input image and is not set on image2video. | Confirmed. |
| `submit_id` means the task contract was valid | Previous SHOT-02-V002 submit produced a submit_id while the submit response also reported invalid duration. | Not sufficient. Submit response status/fail_reason must be audited. |
| Querying status alone is enough to treat a task as valid | Existing query_result can return `querying` even after submit reported invalid param. | Not sufficient. The submit response and command contract must be recorded together. |

## SHOT-02-V002 Diagnosis

The SHOT-02-V002 CLI command used:

```powershell
dreamina image2video `
  --image "productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 2 `
  --video_resolution 720p `
  --poll 0
```

Diagnosis:

- `task_type=image2video`: supported.
- exactly one `--image`: supported.
- `model_version=seedance2.0_vip`: supported.
- `video_resolution=720p`: supported.
- ratio omitted: correct.
- `duration=2`: not supported for current CLI image2video with `seedance2.0_vip`; supported range is 4-15s.

Therefore, SHOT-02-V002 was not valid under the current local CLI image2video command contract. The package should be treated as `command-contract-invalid` for CLI execution, while preserving it as a planning/prompt artifact until explicitly revised.

## Recommendation

- Do not reuse the existing SHOT-02-V002 CLI command as-is.
- If continuing through local CLI image2video with `seedance2.0_vip`, use the CLI-supported shortest duration: 4 seconds.
- If the creative requirement is truly a 1-2 second highlight clip, use a `manual_web_run` workflow or another explicitly validated interface that supports 1-2 second video generation.
- Do not change the SHOT-02-V002 package in this audit step; update it only after explicit approval.
- Before any new live submit, run a command-contract preflight against the exact local CLI help/version currently in use.

## New Execution Contract

Every live Dreamina submit must pass a preflight command-contract check before execution:

1. Confirm the exact `dreamina` executable path.
2. Confirm `dreamina version`.
3. Confirm the selected command's help contract for:
   - task_type
   - model_version
   - duration range
   - video_resolution
   - ratio rule
   - input count and input type
4. Confirm the exact prepared command matches the supported contract.
5. Record the submit response status, not only the submit_id.
6. Treat `submit_id` alone as insufficient evidence of a valid task.
7. Treat `querying` alone as insufficient evidence of a valid task.
8. If the submit response includes `gen_status=fail` or a parameter error, record it as a failed/invalid submit even if query_result later says `querying`.
9. Do not download unless query_result returns success and the submit response did not reveal a command-contract failure.
10. Do not mark any result as usable, locked, or final master without explicit human review.

## Decision

- Actual local CLI contract audited.
- SHOT-02-V002 `duration=2` is invalid for current CLI `image2video + seedance2.0_vip`.
- Recommended path: revise to CLI-supported 4s minimum or use a manual web workflow for 1-2s highlight clips.
- No SHOT-02-V002 package or metadata was changed by this audit.

DREAMINA_CLI_EXECUTION_CONTRACT_AUDIT_READY
