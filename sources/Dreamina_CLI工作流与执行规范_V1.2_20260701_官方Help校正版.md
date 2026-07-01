# Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版

> 类型：Dreamina CLI workflow and execution specification
> 应用方式：建议由用户手动替换 V1.1。
> 状态：待用户手动应用；手动上传 / 同步后作为 official Source 使用。

## 1. Highest Fact Source

Current runtime help remains the highest command fact source:

```text
dreamina <command> -h
```

If this document conflicts with runtime help, runtime help wins.

## 2. Global Workflow Rules

- Generation commands consume credits.
- Submit, query, download, retry, resubmit, final, and lock are separate gates.
- `query_result --download_dir` is download; `query_result` without `--download_dir` is query-only.
- `output_dir` and `output_name` belong to local bookkeeping/download planning, not submit flags unless the specific runtime help says otherwise.
- Do not infer support across commands. Check each command help.

## 3. Command Selection

| Need | Command |
|---|---|
| prompt-only image | `text2image` |
| image-guided image edit | `image2image` |
| prompt-only video | `text2video` |
| one image to video | `image2video` |
| first/last frame video | `frames2video` |
| multiple image story | `multiframe2video` |
| all-around refs across image/video/audio | `multimodal2video` |
| upscale one image | `image_upscale` |

## 4. text2image

Supported facts from 2026-07-01 help:

- `--prompt`
- `--ratio`
- `--resolution_type`
- `--model_version`
- `--generate_num`
- `--poll`
- `model_version`: `3.0`, `3.1`, `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`
- `ratio`: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`
- `generate_num`: `1-10`
- `3.0/3.1`: `resolution_type 1k or 2k`
- `4.0+`: `resolution_type 2k or 4k`

## 5. image2image

Supported facts:

- input flag is `--images`
- supports 1-10 input images
- supports `--generate_num 1-10`
- `model_version`: `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`
- `ratio`: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`
- `resolution_type`: `2k`, `4k`

## 6. text2video

Supported facts:

- `model_version`: `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `ratio`: `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9`
- `duration`: `4-15`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`
- all other listed models: `video_resolution 720p`

## 7. image2video

Supported facts:

- exactly one `--image`
- do not pass `--ratio`; ratio is inferred from input image
- advanced model names include `seedance1.0fast`, `seedance1.0`, `seedance1.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `seedance1.0fast/seedance1.0`: duration `3-10`
- `seedance1.5pro`: duration `4-12`
- `seedance2.0 family/seedance2.0mini`: duration `4-15`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`
- all other listed models: `video_resolution 720p`

## 8. frames2video

Supported facts:

- uses `--first` and `--last`
- ratio inferred from first frame
- `model_version`: `seedance1.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `seedance1.5pro`: duration `4-12`, `720p`
- `seedance2.0 family/seedance2.0mini`: duration `4-15`
- `seedance2.0_vip`: `720p`, `1080p`, or `4k`

## 9. multiframe2video

Supported facts:

- uses `--images`
- 2-20 images
- exactly 2 images can use shorthand `--prompt` and `--duration`
- 3+ images should repeat `--transition-prompt`
- repeat `--transition-duration` once per transition segment when needed
- ratio inferred from first image
- does not support `model_version` or `video_resolution` override

## 10. multimodal2video

Supported facts:

- uses repeated `--image`, `--video`, and `--audio`
- at least one image or video is required
- image <= 9
- video <= 3
- audio <= 3
- audio inputs must be 2-15 seconds
- `model_version`: `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`
- `ratio`: `1:1`, `3:4`, `16:9`, `4:3`, `9:16`, `21:9`
- `duration`: `4-15`
- `seedance2.0_vip`: `video_resolution 720p, 1080p, or 4k`
- all other listed models: `video_resolution 720p`

## 11. image_upscale

Supported facts:

- one `--image`
- `resolution_type`: `2k`, `4k`, `8k`
- `4k` and `8k` require VIP

## 12. Async Boundary

Submit success requires structured submit evidence. For async generation, do not treat process exit alone as success.

After submit returns `submit_id` and `gen_status=querying`, a later query phase must be separately authorized.

Download requires explicit authorization and `--download_dir`.

## 13. Safety Boundary

This workflow specification does not authorize live operations. It only describes command facts for future authorized phases.
