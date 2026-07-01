# DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版

> 类型：DreaminaBatcher manifest schema candidate
> Intended action: replacement candidate for V1.1
> Status: not official Source until human-applied

## 1. Purpose

This candidate updates the manifest schema to match the 2026-07-01 Dreamina CLI help snapshot.

Runtime `dreamina <command> -h` remains the highest command fact source.

## 2. Base Manifest Columns

Recommended common columns:

```csv
project_name,shot_id,asset_id,task_type,model_version,ratio,prompt_path,prompt,duration,video_resolution,resolution_type,generate_num,output_dir,output_name,external_id,image,video,audio,first,last,transition_prompt,transition_duration,session_id,poll,status,fail_reason,local_output_path,version,notes
```

`generate_num` is newly important for image commands that support it.

## 3. Task Type Mapping

| task_type | CLI command | Input fields |
|---|---|---|
| `text2image` | `dreamina text2image` | prompt/prompt_path |
| `image2image` | `dreamina image2image` | image field mapped to repeated `--images` |
| `text2video` | `dreamina text2video` | prompt/prompt_path |
| `image2video` | `dreamina image2video` | one image |
| `frames2video` | `dreamina frames2video` | first + last, or image START\|END if adapter supports it |
| `multiframe2video` | `dreamina multiframe2video` | multiple images, transition prompt/duration |
| `multimodal2video` | `dreamina multimodal2video` | repeated image/video/audio |
| `image_upscale` | `dreamina image_upscale` | one image |

## 4. Field Rules

### generate_num

- allowed for `text2image`: `1-10`
- allowed for `image2image`: `1-10`
- omitted or empty for video and upscale commands

### video_resolution

- allowed for `text2video`, `image2video`, `frames2video`, `multimodal2video`
- `seedance2.0_vip` supports `720p`, `1080p`, or `4k` where help shows it
- all other listed video models generally use `720p` unless runtime help changes
- empty for image commands and multiframe2video

### resolution_type

- used by image commands and image_upscale
- `text2image`: depends on model
- `image2image`: `2k` or `4k`
- `image_upscale`: `2k`, `4k`, `8k`
- empty for video commands

### ratio

- explicit for `text2image`, `image2image`, `text2video`, and `multimodal2video`
- empty for `image2video`, `frames2video`, and `multiframe2video` because ratio is inferred from image input

### output_dir and download

`output_dir` is not a submit flag.

Download is a later action through:

```text
dreamina query_result --submit_id <id> --download_dir <dir>
```

Do not convert `output_dir` into `--download_dir` during submit.

## 5. Model Version Allow Lists From 2026-07-01 Help

### text2image

`3.0`, `3.1`, `4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`

### image2image

`4.0`, `4.1`, `4.5`, `4.6`, `4.7`, `5.0`

### text2video

`seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`

### image2video

`seedance1.0fast`, `seedance1.0`, `seedance1.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`

### frames2video

`seedance1.5pro`, `seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`

### multimodal2video

`seedance2.0`, `seedance2.0fast`, `seedance2.0_vip`, `seedance2.0fast_vip`, `seedance2.0mini`

## 6. No-Submit Package Safety Flags

No-submit package manifests should preserve or pair with package JSON fields:

- `no_submit=true`
- `submit_authorized=false`
- `query_authorized=false`
- `download_authorized=false`
- `retry_authorized=false`
- `resubmit_authorized=false`
- `batch_authorized=false`
- `final_master=false`
- `locked=false`

## 7. Validation Checklist

Before any future live phase:

1. `sources/` clean.
2. Package JSON parses.
3. Manifest CSV parses.
4. Prompt path exists.
5. Local refs exist if required.
6. Model/duration/ratio/resolution fields match current runtime help.
7. `output_dir` is not treated as submit download.
8. Live phase has explicit human authorization.
