# DreaminaBatcher_manifest_schema_V1.1_官方Help校正版

> 项目：AI 视频制作 / DreaminaBatcher  
> 版本：V1.1  
> 更新依据：`dreamina_cli_help.md`  
> 生成时间：2026-06-07 08:42:00  
> 建议：替换 `DreaminaBatcher_manifest_schema_V1.0.md` 作为 active schema。

---

# 1. 标准字段

基础字段：

```csv
project_name,shot_id,task_type,model_version,ratio,prompt,duration,video_resolution,resolution_type,output_dir,output_name,external_id,image,video,audio
```

建议新增扩展字段：

```csv
session_id,first,last,transition_prompt,transition_duration,poll,status,fail_reason,local_output_path,version,notes
```

---

# 2. task_type 允许值

```text
text2image
image2image
image_upscale
text2video
image2video
frames2video
multiframe2video
multimodal2video
```

---

# 3. task_type 判定

```text
无参考图图片 -> text2image
有参考图图片 -> image2image
图片放大 -> image_upscale

无参考素材视频 -> text2video
单图视频 -> image2video
首尾帧视频 -> frames2video
多帧故事 -> multiframe2video
全能参考 / 多图 / 视频 / 音频参考 -> multimodal2video
```

---

# 4. 字段映射

## 4.1 text2image

```text
prompt -> --prompt
model_version -> --model_version
ratio -> --ratio
resolution_type -> --resolution_type
session_id -> --session
poll -> --poll
```

## 4.2 image2image

```text
image -> --images，可重复
prompt -> --prompt
model_version -> --model_version
ratio -> --ratio
resolution_type -> --resolution_type
session_id -> --session
poll -> --poll
```

重要：

```text
参数是 --images，不是 --image；
支持 1-10 张；
resolution_type 只支持 2k / 4k；
1k 不支持。
```

## 4.3 image_upscale

```text
image -> --image
resolution_type -> --resolution_type
session_id -> --session
poll -> --poll
```

## 4.4 text2video

```text
prompt -> --prompt
model_version -> --model_version
ratio -> --ratio
duration -> --duration
video_resolution -> --video_resolution
session_id -> --session
poll -> --poll
```

## 4.5 image2video

```text
image -> --image
prompt -> --prompt
model_version -> --model_version
duration -> --duration
video_resolution -> --video_resolution
session_id -> --session
poll -> --poll
```

重要：

```text
只允许 1 张 image；
不传 ratio；
ratio 由输入图推断。
```

## 4.6 frames2video

```text
first -> --first
last -> --last
prompt -> --prompt
model_version -> --model_version
duration -> --duration
video_resolution -> --video_resolution
session_id -> --session
poll -> --poll
```

如果没有 first/last 字段：

```text
task_type=frames2video 且 image=START|END
```

则执行器转换：

```text
第一项 -> --first
第二项 -> --last
```

## 4.7 multiframe2video

```text
image -> --images
prompt -> --prompt，仅 2 图 shorthand
duration -> --duration，仅 2 图 shorthand
transition_prompt -> --transition-prompt，可重复
transition_duration -> --transition-duration，可重复
session_id -> --session
poll -> --poll
```

限制：

```text
image 2-20 张；
N 张图需要 N-1 个 transition_prompt；
ratio 从第一张图推断；
不支持 model_version 和 video_resolution 覆盖。
```

## 4.8 multimodal2video

```text
image -> --image，可重复
video -> --video，可重复
audio -> --audio，可重复
prompt -> --prompt
model_version -> --model_version
ratio -> --ratio
duration -> --duration
video_resolution -> --video_resolution
session_id -> --session
poll -> --poll
```

限制：

```text
image <= 9
video <= 3
audio <= 3
至少有 image 或 video
audio 2-15 秒
duration 4-15 秒
resolution_type 为空
```

---

# 5. 校验规则

## 5.1 image2image

```text
1 <= image_count <= 10
resolution_type 为空或 2k/4k
禁止 duration/video_resolution
```

## 5.2 image2video

```text
image_count == 1
ratio 必须为空
video/audio 为空
resolution_type 为空
```

## 5.3 frames2video

```text
必须有 first 和 last
或 image_count == 2 并由执行器转换
ratio 必须为空
resolution_type 为空
```

## 5.4 multiframe2video

```text
2 <= image_count <= 20
若 image_count == 2，可用 prompt + duration shorthand
若 image_count >= 3，transition_prompt_count == image_count - 1
transition_duration_count == 0 或 image_count - 1
禁止 ratio/model_version/video_resolution 覆盖
```

## 5.5 multimodal2video

```text
image_count + video_count >= 1
image_count <= 9
video_count <= 3
audio_count <= 3
duration 4-15
resolution_type 为空
```

---

# 6. 当前项目建议

对于《赤焰对天穹》：

```text
A资产 -> text2image
SHOT-KF -> image2image，用 --images
普通单图动画镜头 -> image2video
多参考图视频镜头 -> multimodal2video
变身/场地切换若有首尾图 -> frames2video 可测试
多阶段连续分镜 -> multiframe2video 可测试
```

---

# 7. precheck 新增检查

```text
1. image2image 是否使用 --images；
2. image2video 是否只有一张 image 且不传 ratio；
3. frames2video 是否能解析 first/last；
4. multiframe2video transition 数量是否正确；
5. multimodal2video 是否至少有 image 或 video；
6. output_dir 是否只用于下载；
7. 所有逻辑 ID 是否能解析为真实文件路径。
```

---

# 8. 一句话总结

```text
V1.1 schema 的关键修正是：image2image 使用 --images；image2video 不传 ratio 且只吃单图；frames2video 用 --first/--last；multiframe2video 用 --images 与 transition prompt；multimodal2video 才是全能参考多模态视频。
```
