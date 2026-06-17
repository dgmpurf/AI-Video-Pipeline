# Dreamina CLI 帮助信息

> 生成时间：2026-06-07 16:35:30
## dreamina -h

`	ext
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
`\n\n## dreamina help -h

`	ext
Usage:
  dreamina help [command] [flags]

Help provides help for any command in the application.
Simply type dreamina help [path to command] for full details.


Flags:
  -h, --help   help for help

Global Flags:
      --version   print build version information
`\n\n## dreamina list_task -h

`	ext
Usage:
  dreamina list_task [flags]

List tasks saved for the current logged-in user.


Flags:
      --gen_status string      filter by gen_status
      --gen_task_type string   filter by gen_task_type
  -h, --help                   help for list_task
      --limit int              max number of tasks to return (default 20)
      --offset int             offset for pagination
      --submit_id string       filter by submit_id

Global Flags:
      --version   print build version information

Examples:
  dreamina list_task
  dreamina list_task --gen_status=success
`\n\n## dreamina login -h

`	ext
Usage:
  dreamina login [flags]

Reuse the current local OAuth login state when it is still valid; otherwise start OAuth Device Flow.
By default the CLI prints verification_uri, user_code, and device_code, then waits for authorization to complete.
With --headless, the CLI prints the authorization material and exits without polling checklogin.
The legacy browser callback and manual-import login flow are no longer used.


Flags:
      --headless   print OAuth authorization material and exit without polling checklogin
  -h, --help       help for login

Global Flags:
      --version   print build version information

Examples:
  dreamina login
  dreamina login --headless
  dreamina login checklogin --device_code=<device_code> --poll=30
`\n\n## dreamina logout -h

`	ext
Usage:
  dreamina logout [flags]

Remove the local OAuth login state without touching tasks or config.


Flags:
  -h, --help   help for logout

Global Flags:
      --version   print build version information

Examples:
  dreamina logout
`\n\n## dreamina query_result -h

`	ext
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
`\n\n## dreamina relogin -h

`	ext
Usage:
  dreamina relogin [flags]

Remove the local OAuth login state first, then force a fresh OAuth Device Flow login.
By default the CLI prints verification_uri, user_code, and device_code, then waits for authorization to complete.
With --headless, the CLI prints the authorization material and exits without polling checklogin.


Flags:
      --headless   print OAuth authorization material and exit without polling checklogin
  -h, --help       help for relogin

Global Flags:
      --version   print build version information

Examples:
  dreamina relogin
  dreamina relogin --headless
`\n\n## dreamina session -h

`	ext
Usage:
  dreamina session [flags]

Manage Dreamina sessions (create, list, search, rename, delete).

A session is a container for organizing your creation history.
All generator commands accept a --session=<id> flag to submit tasks into a specific session.

Available Commands:
  create    Create a new session (auto-named or custom)
  list      List your recent sessions (alias: ls)
  search    Find a session ID by its name (alias: find)
  rename    Change a session's name (alias: update)
  delete    Delete a session (alias: rm)

Notes:
- All session commands require login (run "dreamina login" first).
- Session 0 is the default session. It cannot be renamed or deleted.
- Deleting a session will safely move its history back to the default session.


Flags:
  -h, --help   help for session

Global Flags:
      --version   print build version information

Examples:
  # 1. Create a session
  dreamina session create
  dreamina session create "My Video Project"

  # 2. List sessions (default 30; user-specified -n is capped at 100)
  dreamina session list
  dreamina session ls -n 100

  # 3. Find a session by name
  dreamina session search "Video"

  # 4. Rename a session
  dreamina session rename 10086 "New Project Name"

  # 5. Delete a session
  dreamina session rm 10086
`\n\n## dreamina session create -h

`	ext
Usage:
  dreamina session create [name] [flags]

Create a new session.

Args:
- name (optional): session name. If omitted, the backend generates a default name like "新对话 01-04 10:30".

Notes:
- name must be 1-50 characters after trimming spaces.



Flags:
  -h, --help   help for create

Global Flags:
      --version   print build version information

Examples:
  dreamina session create
  dreamina session create "我的视频项目"
`\n\n## dreamina session list -h

`	ext
Usage:
  dreamina session list [flags]

List recent sessions.

By default it requests and shows the latest 30 sessions from the backend, ordered by pinned first and then updated time descending.
If you pass -n/--max-count, the CLI requests that many sessions from the backend.
User-specified values are capped at 100.

Output:
- Table columns: ID, NAME, PINNED, UPDATED_AT
- UPDATED_AT is formatted as local time: YYYY-MM-DD HH:MM



Flags:
  -h, --help            help for list
  -n, --max-count int   maximum number of sessions to display (default 30)

Global Flags:
      --version   print build version information

Examples:
  dreamina session list
  dreamina session list -n 5
  dreamina session list -n 100
`\n\n## dreamina session search -h

`	ext
Usage:
  dreamina session search <name> [flags]

Search sessions by name.

The CLI requests the first 100 sessions from the backend and matches records whose name contains the input string. Matching is case-sensitive.



Flags:
  -h, --help   help for search

Global Flags:
      --version   print build version information

Examples:
  dreamina session search "视频"
  dreamina session search "我的年度总结"
`\n\n## dreamina session rename -h

`	ext
Usage:
  dreamina session rename <session_id> <new_name> [flags]

Rename a session.

This command only exposes renaming. Pin/unpin is intentionally not exposed in CLI.

Args:
- session_id: the target session ID
- new_name: the new session name (1-50 characters)

Notes:
- Session 0 is the default session and cannot be renamed.
- Negative session IDs are invalid.



Flags:
  -h, --help   help for rename

Global Flags:
      --version   print build version information

Examples:
  dreamina session rename 10086 "2024年度宣传片"
`\n\n## dreamina session delete -h

`	ext
Usage:
  dreamina session delete <session_id> [flags]

Delete a session.

Notes:
- Session 0 is the default session and cannot be deleted.
- Negative session IDs are invalid.
- This operation is safe. The backend performs a soft delete and will move related history records back to the default session.



Flags:
  -h, --help   help for delete

Global Flags:
      --version   print build version information

Examples:
  dreamina session delete 10085
  dreamina session rm 10085
`\n\n## dreamina user_credit -h

`	ext
Usage:
  dreamina user_credit [flags]

Query the current logged-in user's remaining Dreamina credits.


Flags:
  -h, --help   help for user_credit

Global Flags:
      --version   print build version information

Examples:
  dreamina user_credit
`\n\n## dreamina version -h

`	ext
Usage:
  dreamina version [flags]

Print build version and commit information


Flags:
  -h, --help   help for version

Global Flags:
      --version   print build version information

Examples:
  dreamina version
`\n\n## dreamina frames2video -h

`	ext
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
`\n\n## dreamina image2image -h

`	ext
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
`\n\n## dreamina image2video -h

`	ext
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
`\n\n## dreamina image_upscale -h

`	ext
Usage:
  dreamina image_upscale [flags]

Upload one local image, then submit a Dreamina image upscale task. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- resolution_type: 2k, 4k, 8k
- 2k is available to non-VIP users
- 4k and 8k require VIP


Flags:
      --image string             local input image path
      --session int              session id (default 0 "默认对话") 
      --resolution_type string   supported values: 2k, 4k, 8k; 4k and 8k require VIP
      --poll int                 submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                     help for image_upscale

Global Flags:
      --version   print build version information

Examples:
  dreamina image_upscale --image=./input.png --resolution_type=4k
`\n\n## dreamina multiframe2video -h

`	ext
Usage:
  dreamina multiframe2video [flags]

Upload multiple local images, then submit a Dreamina intelligent multi-frame video task for coherent visual storytelling. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- inputs: 2-20 images
- exactly 2 images: use shorthand --prompt and optional --duration
- 3+ images: repeat --transition-prompt once per transition segment to describe how one frame evolves into the next
- repeat --transition-duration once per transition segment, or omit it to default each segment to 3 seconds

Notes:
- designed for multi-image story generation, not full multimodal editing
- for N images, the transition count is N-1
- ratio is inferred from the first image
- model_version and video_resolution overrides are not supported by this command
- each duration segment is limited to [0.5, 8] seconds and total duration must be >= 2


Flags:
      --images strings                    local reference image paths
      --prompt string                     shorthand prompt for exactly 2 images
      --duration float                    shorthand transition duration in seconds for exactly 2 images; backend clamps each segment to [0.5, 8] and requires total duration >= 2 (default 3)
      --transition-prompt stringArray     repeat once per transition segment; for N images provide N-1 prompts
      --transition-duration stringArray   repeat once per transition segment in seconds; for N images provide N-1 durations, or omit to default each segment to 3
      --session int                       session id (default 0 "默认对话") 
      --poll int                          submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                              help for multiframe2video

Global Flags:
      --version   print build version information

Examples:
  dreamina multiframe2video --images ./a.png,./b.png --prompt="character turns around"
  dreamina multiframe2video --images ./a.png,./b.png,./c.png --transition-prompt="turn from A to B" --transition-prompt="turn from B to C"
`\n\n## dreamina multimodal2video -h

`	ext
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
`\n\n## dreamina text2image -h

`	ext
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
`\n\n## dreamina text2video -h

`	ext
Usage:
  dreamina text2video [flags]

Submit a Dreamina text-to-video task. The task is asynchronous, but --poll can wait briefly before falling back to query_result.

Supported combinations:
- model_version: seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip
- ratio: 1:1, 3:4, 16:9, 4:3, 9:16, 21:9
- seedance2.0_vip -> video_resolution 720p or 1080p; duration 4-15s
- all other models -> video_resolution 720p; duration 4-15s

Notes:
- default model_version: seedance2.0fast
- omit --video_resolution to use the model default
- omit --ratio to use the default ratio
- 部分高内容安全风险模型在首次使用前，可能需要先在 Dreamina Web 端完成授权确认。若返回 AigcComplianceConfirmationRequired，请先完成授权后重试。


Flags:
      --prompt string             generation prompt
      --session int               session id (default 0 "默认对话") 
      --duration int              video duration in seconds; supported range: 4-15 (default 5)
      --ratio string              supported values: 1:1, 3:4, 16:9, 4:3, 9:16, 21:9
      --video_resolution string   supported values by model: seedance2.0_vip -> 720p or 1080p; all other models -> 720p
      --model_version string      supported values: seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip; default: seedance2.0fast
      --poll int                  submit then poll query_result for up to N seconds at 1s intervals (0 disables polling)
  -h, --help                      help for text2video

Global Flags:
      --version   print build version information

Examples:
  dreamina text2video --prompt="a cat running" --duration=5
`\n\n## dreamina login checklogin -h

`	ext
Usage:
  dreamina login checklogin [flags]

Check the authorization result for a prior headless OAuth Device Flow login.
Pass the device_code printed by "dreamina login --headless" or "dreamina relogin --headless".
--poll=N waits for up to N seconds; --poll=0 checks only once.


Flags:
      --device_code string   device code printed by a prior headless OAuth login
  -h, --help                 help for checklogin
      --poll int             wait for up to N seconds before timing out; 0 checks once

Global Flags:
      --version   print build version information

Examples:
  dreamina login checklogin --device_code=<device_code>
  dreamina login checklogin --device_code=<device_code> --poll=30
`\n\n
