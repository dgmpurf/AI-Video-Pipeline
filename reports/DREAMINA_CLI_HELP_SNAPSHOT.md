# Dreamina CLI Help Snapshot

Executable: `C:/Users/msjpurf/bin/dreamina.exe`

## root help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina [flags]

即梦 official AIGC CLI tool for login, account, and generation workflows

About:
  dreamina is the 即梦 official AIGC CLI tool.

Quick start:
  1. Run "dreamina login" to complete OAuth device login.
  2. For headless login, run "dreamina login --headless", then "dreamina login checklogin --device_code=<device_code>".
  3. Run a generator command such as "dreamina text2image --prompt=\"a cat portrait\"".
  4. Use "dreamina query_result --submit_id=<id>" for async tasks, or "dreamina list_task" to review saved tasks.
  5. Use "dreamina user_credit" to check the current account credit balance.

Tips:
  Run "dreamina <subcommand> -h" to view detailed help for any subcommand.
  Login now uses OAuth Device Flow and prints verification_uri, user_code, and device_code in the terminal.
  All generation operations consume credits.
  Seedance 2.0 family is a flagship video generation model family and is a strong choice when output quality matters most.

Built-in Commands:
  help                 Help about any command
  list_task            List saved tasks with status and result summary
  login                Log in locally with OAuth Device Flow before using task and account commands
  logout               Clear the local OAuth login state
  query_result         Query the current result of an async generation task
  relogin              Clear the local OAuth login state and force a fresh OAuth login
  session              Manage sessions (create/list/search/rename/delete)
  user_credit          Show the current user's remaining credit balance
  version              Print build version and commit information


Generator Commands:
  frames2video         Submit a Dreamina first-last-frames video task
  image2image          Submit a Dreamina image-to-image task
  image2video          Animate one image into video; use multiframe2video for multi-image stories
  image_upscale        Submit a Dreamina image upscale task
  multiframe2video     Create a coherent video story from multiple images
  multimodal2video     Dreamina flagship video mode (全能参考 / formerly ref2video) with all-around references and Seedance 2.0
  text2image           Submit a Dreamina text-to-image task
  text2video           Submit a Dreamina text-to-video task


Examples:
  dreamina login
  dreamina login --headless
  dreamina login checklogin --device_code=<device_code> --poll=30
  dreamina logout
  dreamina relogin
  dreamina user_credit
  dreamina list_task --gen_status=success
  dreamina query_result --submit_id=550e8400-e29b-41d4-a716-446655440000
  dreamina text2image --prompt="a cat portrait" --ratio=1:1 --resolution_type=2k

```

### stderr
```text

```

## text2image help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina text2image [flags]

Submit a Dreamina text-to-image task. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- model_version: 3.0, 3.1, 4.0, 4.1, 4.5, 4.6, 4.7, 5.0
- ratio: 21:9, 16:9, 3:2, 4:3, 1:1, 3:4, 2:3, 9:16
- 3.0/3.1 -> resolution_type 1k or 2k
- 4.0/4.1/4.5/4.6/4.7/5.0 -> resolution_type 2k or 4k

Notes:
- omit --model_version to use the default model
- omit --resolution_type to use the model default


Flags:
      --prompt string            generation prompt
      --session int              session id (default 0 "默认对话") 
      --ratio string             supported values: 21:9, 16:9, 3:2, 4:3, 1:1, 3:4, 2:3, 9:16
      --resolution_type string   supported values by model: 3.0/3.1 -> 1k or 2k; 4.0/4.1/4.5/4.6/4.7/5.0 -> 2k or 4k; omit to use the model default
      --model_version string     supported values: 3.0, 3.1, 4.0, 4.1, 4.5, 4.6, 4.7, 5.0
      --poll int                 submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                     help for text2image

Global Flags:
      --version   print build version information

Examples:
  dreamina text2image --prompt="a cat portrait" --ratio=1:1 --resolution_type=2k

```

### stderr
```text

```

## image2image help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina image2image [flags]

Upload 1 to 10 local images, then submit a Dreamina image-to-image task. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- model_version: 4.0, 4.1, 4.5, 4.6, 4.7, 5.0
- ratio: 21:9, 16:9, 3:2, 4:3, 1:1, 3:4, 2:3, 9:16
- resolution_type: 2k, 4k

Notes:
- 1k is not supported for image2image
- omit --model_version to use the default model
- omit --resolution_type to use the model default
- 一次最多上传十张图片，否则可能导致生图失败


Flags:
      --images strings           local input image paths
      --prompt string            edit prompt
      --session int              session id (default 0 "默认对话") 
      --ratio string             supported values: 21:9, 16:9, 3:2, 4:3, 1:1, 3:4, 2:3, 9:16
      --resolution_type string   supported values: 2k, 4k; omit to use the model default
      --model_version string     supported values: 4.0, 4.1, 4.5, 4.6, 4.7, 5.0
      --poll int                 submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                     help for image2image

Global Flags:
      --version   print build version information

Examples:
  dreamina image2image --images ./input.png --prompt="turn into watercolor"

```

### stderr
```text

```

## image2video help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina image2video [flags]

Upload one local image, then submit a Dreamina image-to-video task. For multi-image storytelling, use multiframe2video; for full-reference mixed-media generation, use multimodal2video. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- basic usage: --image + --prompt
- advanced controls: set any of --duration, --video_resolution, or --model_version
- advanced model_version values: 3.0, 3.0fast, 3.0pro, 3.0_fast, 3.0_pro, 3.5pro, 3.5_pro, seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip
- seedance2.0_vip -> video_resolution 720p or 1080p
- all other models -> video_resolution 720p
- ratio is inferred from the input image and is not set on this command

Notes:
- omit advanced controls to use the default image-to-video path
- duration, model_version, and video_resolution must be provided in a supported combination
- 部分高内容安全风险模型在首次使用前，可能需要先在 Dreamina Web 端完成授权确认。若返回 AigcComplianceConfirmationRequired，请先完成授权后重试。


Flags:
      --image string              local first-frame image path
      --prompt string             generation prompt
      --duration int              advanced controls only; supported duration ranges by model: 3.0/3.0fast/3.0pro -> 3-10, 3.5pro -> 4-12, seedance2.0 family -> 4-15 (default 5)
      --video_resolution string   advanced controls only; supported values by model: seedance2.0_vip -> 720p or 1080p; all other models -> 720p
      --model_version string      advanced controls only; supported values: 3.0, 3.0fast, 3.0pro, 3.0_fast, 3.0_pro, 3.5pro, 3.5_pro, seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip
      --session int               session id (default 0 "默认对话") 
      --poll int                  submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                      help for image2video

Global Flags:
      --version   print build version information

Examples:
  dreamina image2video --image=./first.png --prompt="camera push in"

```

### stderr
```text

```

## frames2video help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina frames2video [flags]

Upload two local images as first and last frames, then submit a Dreamina video generation task. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- model_version: 3.0, 3.5pro, seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip
- seedance2.0_vip -> video_resolution 720p or 1080p; duration 4-15s
- 3.0 -> video_resolution 720p; duration 3-10s
- 3.5pro -> video_resolution 720p; duration 4-12s
- all other seedance2.0 models -> video_resolution 720p; duration 4-15s

Notes:
- ratio is inferred from the first frame image size
- default model_version: seedance2.0fast
- omit --video_resolution to use the model default
- 部分高内容安全风险模型在首次使用前，可能需要先在 Dreamina Web 端完成授权确认。若返回 AigcComplianceConfirmationRequired，请先完成授权后重试。


Flags:
      --first string              local first-frame image path
      --last string               local last-frame image path
      --prompt string             generation prompt
      --session int               session id (default 0 "默认对话") 
      --duration int              video duration in seconds; supported ranges: 3.0 -> 3-10, 3.5pro -> 4-12, seedance2.0 family -> 4-15 (default 5)
      --video_resolution string   supported values by model: seedance2.0_vip -> 720p or 1080p; all other models -> 720p
      --model_version string      supported values: 3.0, 3.5pro, seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip; default: seedance2.0fast
      --poll int                  submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                      help for frames2video

Global Flags:
      --version   print build version information

Examples:
  dreamina frames2video --first=./start.png --last=./end.png --prompt="season changes"

```

### stderr
```text

```

## multimodal2video help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina multimodal2video [flags]

Upload local images, videos, and audio, then submit Dreamina's flagship multimodal video generation mode. This corresponds to the "全能参考" (All-around reference) feature on the web interface (formerly known as ref2video). This is the strongest video generation mode currently exposed in the CLI, supports all-around references, and supports the Seedance 2.0 family (flag values: seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip). The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- inputs: any mix of --image, --video, --audio
- at least one --image or --video is required
- audio inputs must be 2-15 seconds
- model_version: seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip
- ratio: 1:1, 3:4, 16:9, 4:3, 9:16, 21:9
- seedance2.0_vip -> video_resolution 720p or 1080p
- all other models -> video_resolution 720p
- duration: 4-15s

Notes:
- local files are uploaded automatically before submit
- input limits: image<=9, video<=3, audio<=3
- 部分高内容安全风险模型在首次使用前，可能需要先在 Dreamina Web 端完成授权确认。若返回 AigcComplianceConfirmationRequired，请先完成授权后重试。


Flags:
      --image stringArray         repeat for each local input image path
      --video stringArray         repeat for each local input video path
      --audio stringArray         repeat for each local input audio path
      --prompt string             optional multimodal edit prompt
      --duration int              video duration in seconds; supported range: 4-15 (default 5)
      --ratio string              supported values: 1:1, 3:4, 16:9, 4:3, 9:16, 21:9
      --video_resolution string   supported values by model: seedance2.0_vip -> 720p or 1080p; all other models -> 720p
      --model_version string      supported values: seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip
      --session int               session id (default 0 "默认对话") 
      --poll int                  submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                      help for multimodal2video

Global Flags:
      --version   print build version information

Examples:
  dreamina multimodal2video --image ./input.png --prompt="turn this into a cinematic shot"
  dreamina multimodal2video --image ./input.png --audio ./music.mp3 --model_version=seedance2.0fast --duration=5
  dreamina multimodal2video --image ./input.png --video ./ref.mp4 --audio ./music.mp3 --model_version=seedance2.0fast --duration=5

```

### stderr
```text

```

## query_result help
- Ran: `true`
- Return code: `0`

### stdout
```text
Usage:
  dreamina query_result [flags]

Query one async task by submit_id.


Flags:
      --download_dir string   download result media into the target directory
  -h, --help                  help for query_result
      --submit_id string      task submit_id

Global Flags:
      --version   print build version information

Examples:
  dreamina query_result --submit_id=3f6eb41f425d23a3

```

### stderr
```text

```
