# dreamina_cli_help_latest.md｜2026-07-01 本地帮助快照

> Project: AI video production / Dreamina CLI execution layer Source
> Type: local CLI help snapshot, not a rules explanation
> 应用方式：建议由用户手动替换当前 `dreamina_cli_help_latest.md`；手动应用后作为 active help snapshot Source。
> Source evidence: `reports/diagnostics/DREAMINA_CLI_HELP_SNAPSHOT_AFTER_UPDATE_20260701.md`

## Authority

This file is a help snapshot, not a rules explanation.

The highest fact source remains the current runtime output of:

```text
dreamina <command> -h
```

If this snapshot conflicts with runtime help, runtime help wins.

## Captured Version

Binary version output:

```json
{
  "version": "2a20fff-dirty",
  "commit": "2a20fff",
  "build_time": "2026-06-26T06:36:39Z"
}
```

Installer metadata:

```text
version: v1.4.10
release_date: 2026-06-26
```

Installer release note summary:

- `text2image` and `image2image` support `generate_num` for 1-10 images.
- `seedance2.0_vip` adds `4k` video resolution support.
- image upscale query failure was fixed.
- some `image2video` generation failures were fixed.
- video model naming changed from old 3.x names to Seedance 1.x names where applicable.

## Environment Distinction

PowerShell-visible CLI:

```text
C:/Users/msjpurf/bin/dreamina.exe
```

Status:

- version: `2a20fff-dirty`
- commit: `2a20fff`
- build_time: `2026-06-26T06:36:39Z`
- `user_credit` succeeded in the evidence report
- preferred live execution path until Linux CLI login is confirmed

Linux-installed CLI:

```text
/home/ke/.local/bin/dreamina
```

Status:

- installed by official update command
- same binary version output
- login pending user action at capture time
- do not use for live submit until `checklogin` and `user_credit` succeed in that environment

## Snapshot Coverage

Full sanitized help output is stored in:

```text
reports/diagnostics/DREAMINA_CLI_HELP_SNAPSHOT_AFTER_UPDATE_20260701.md
```

Captured help commands:

- `dreamina version`
- `dreamina -h`
- `dreamina login -h`
- `dreamina login checklogin -h`
- `dreamina user_credit -h`
- `dreamina query_result -h`
- `dreamina list_task -h`
- `dreamina session -h`
- `dreamina session create -h`
- `dreamina session list -h`
- `dreamina session search -h`
- `dreamina session rename -h`
- `dreamina session delete -h`
- `dreamina text2image -h`
- `dreamina image2image -h`
- `dreamina text2video -h`
- `dreamina image2video -h`
- `dreamina frames2video -h`
- `dreamina multiframe2video -h`
- `dreamina multimodal2video -h`
- `dreamina image_upscale -h`

## Key Command Facts From 2026-07-01 Snapshot

### text2image

- `model_version`: `3.0`, `3.1`, `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`
- `ratio`: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`
- `generate_num`: `1-10`
- `3.0/3.1`: `resolution_type 1k or 2k`
- `4.0/4.1/4.5/4.6/4.7/5.0`: `resolution_type 2k or 4k`

### image2image

- input flag: `--images`
- supports 1-10 local input images
- `model_version`: `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`
- `ratio`: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`
- `generate_num`: `1-10`
- `resolution_type`: `2k`, `4k`

### text2video

- `model_version`: `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `ratio`: `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`; `duration 4-15s`
- all other listed models: `video_resolution 720p`; `duration 4-15s`

### image2video

- single local image input via `--image`
- ratio is inferred from input image; do not pass `--ratio`
- advanced model names include `seedance1.0fast`, `seedance1.0`, `seedance1.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`
- all other listed models: `video_resolution 720p`

### frames2video

- first/last image input via `--first` and `--last`
- ratio inferred from first frame
- `model_version`: `seedance1.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`; `duration 4-15s`
- `seedance1.5pro`: `video_resolution 720p`; `duration 4-12s`

### multiframe2video

- input: `--images`
- supports 2-20 images
- for exactly 2 images, supports shorthand `--prompt` and optional `--duration`
- for 3+ images, repeat `--transition-prompt`
- `transition-duration` can repeat once per segment
- ratio inferred from first image
- no `model_version` or `video_resolution` override

### multimodal2video

- inputs: repeated `--image`, repeated `--video`, repeated `--audio`
- at least one `--image` or `--video` is required
- input limits: image <= 9, video <= 3, audio <= 3
- audio inputs must be 2-15 seconds
- `model_version`: `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `ratio`: `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`
- all other listed models: `video_resolution 720p`
- `duration`: `4-15s`

### query_result

- `--submit_id` queries one async task.
- `--download_dir` downloads result media into the target directory.
- Query without `--download_dir` is query-only.

### image_upscale

- `resolution_type`: `2k`, `4k`, `8k`
- `4k` and `8k` require VIP.

## Safety Note

All generation commands consume credits. Submit, query, download, retry, resubmit, final, and lock must remain separately authorized unless the human explicitly grants a macro authorization.
