# Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版

> 项目：AI 视频制作 / Dreamina CLI 执行层 Source  
> 版本：V1.1  
> 更新依据：`dreamina_cli_help.md` 完整 `dreamina -h` 与子命令 `-h` 输出  
> 生成时间：2026-06-07 08:42:00  
> 建议：替换或覆盖 `Dreamina_CLI工作流与执行规范_V1.0.md` 作为 active Source。

---

# 0. V1.1 必改点

```text
1. image2image 的参数是 --images，可重复，支持 1-10 张；
2. image2video 只支持单张 --image，并且不传 --ratio；
3. multimodal2video 是“全能参考 / All-around reference”，支持 image<=9、video<=3、audio<=3；
4. frames2video 是首尾帧视频，使用 --first / --last；
5. multiframe2video 是多帧故事生成，使用 --images 和 transition-prompt；
6. 所有 generator 命令都可带 --session；
7. 多数 generator 命令可带 --poll；
8. output_dir 仍然只用于 query_result --download_dir，不属于 submit 参数。
```

---

# 1. CLI 事实来源优先级

执行层规则优先级：

```text
dreamina_cli_help.md / 本地 dreamina <command> -h
> Dreamina_CLI工作流与执行规范
> DreaminaBatcher_manifest_schema
> 通用 AI 视频工作流
```

如果本文件与最新本地 CLI help 冲突，以本地 CLI help 为准。

---

# 2. 全局执行模型

Dreamina CLI 是异步任务系统。

```text
submit -> 返回 submit_id
query_result -> 查询状态
query_result --download_dir -> 下载结果
下载后 -> 按 output_name 本地重命名
```

提交阶段不要传：

```text
output_dir
output_name
external_id
```

这些只属于本地记录、下载和重命名。

---

# 3. 生成命令与用途

## 3.1 text2image

```text
纯文本生成图片。
```

参数：

```text
--prompt
--model_version
--ratio
--resolution_type
--session
--poll
```

模型：

```text
3.0 3.1 4.0 4.1 4.5 4.6 4.7 5.0
```

分辨率：

```text
3.0/3.1 -> 1k / 2k
4.0+ -> 2k / 4k
```

---

## 3.2 image2image

```text
上传 1-10 张本地图片，提交图生图任务。
```

参数：

```text
--images <path>  可重复，1-10 张
--prompt
--model_version
--ratio
--resolution_type
--session
--poll
```

重要：

```text
参数名是 --images，不是 --image；
1k 不支持 image2image；
resolution_type 只支持 2k / 4k；
一次最多 10 张图片。
```

项目用途：

```text
SHOT-xx-KF 关键帧图；
角色 / 场景 / 武器 / 终极形态参考下的构图重建。
```

---

## 3.3 text2video

```text
纯文字生成视频。
```

参数：

```text
--prompt
--duration
--ratio
--video_resolution
--model_version
--session
--poll
```

模型：

```text
seedance2.0
seedance2.0fast
seedance2.0_vip
seedance2.0fast_vip
```

时长：

```text
4-15 秒
```

---

## 3.4 image2video

```text
单张图片动画化为视频。
```

参数：

```text
--image <path>
--prompt
--duration
--video_resolution
--model_version
--session
--poll
```

重要：

```text
只支持 1 张 --image；
ratio 从输入图推断；
不要给 image2video 传 --ratio；
多图故事用 multiframe2video；
全能参考用 multimodal2video。
```

---

## 3.5 frames2video

```text
首尾帧视频。
```

参数：

```text
--first <path>
--last <path>
--prompt
--duration
--video_resolution
--model_version
--session
--poll
```

用途：

```text
变身前后；
场地切换前后；
门打开前后；
动作起点和终点都必须稳定的镜头。
```

注意：

```text
ratio 从 first frame 推断。
```

---

## 3.6 multiframe2video

```text
多图连续故事生成。
```

参数：

```text
--images <path>  2-20 张
--prompt         仅 2 图 shorthand
--duration       仅 2 图 shorthand
--transition-prompt
--transition-duration
--session
--poll
```

规则：

```text
N 张图片需要 N-1 个 transition-prompt；
ratio 从第一张图片推断；
不支持 model_version 和 video_resolution 覆盖；
每段时长 0.5-8 秒；
总时长 >= 2 秒。
```

---

## 3.7 multimodal2video

```text
全能参考 / All-around reference / ref2video。
```

参数：

```text
--image <path>   可重复，最多 9
--video <path>   可重复，最多 3
--audio <path>   可重复，最多 3
--prompt
--duration
--ratio
--video_resolution
--model_version
--session
--poll
```

要求：

```text
至少有一个 --image 或 --video；
audio 必须 2-15 秒；
duration 4-15 秒。
```

项目用途：

```text
多图参考的视频镜头；
角色 + 场景 + 关键帧 + 武器/终极形态共同参考的视频生成。
```

---

# 4. task_type 判定规则

```text
无参考图的图片任务 -> text2image
有参考图的图片任务 -> image2image
图片放大 -> image_upscale

无参考素材的视频 -> text2video
单张图片视频 -> image2video
首尾帧视频 -> frames2video
多帧故事视频 -> multiframe2video
多图 / 视频 / 音频全能参考 -> multimodal2video
```

当前动作短片推荐：

```text
A-CH / A-PROP / A-SC 原子资产 -> text2image
SHOT-KF，带角色/场景/武器参考 -> image2image
普通单图动画镜头 -> image2video
多参考图视频镜头 -> multimodal2video
变身/场地切换且有明确首尾图 -> frames2video 可测试
多张连续分镜故事过渡 -> multiframe2video 可测试
```

---

# 5. manifest 到 CLI 参数映射

## 5.1 image2image

manifest：

```text
image = A-CH-A-01|A-CH-B-01|A-SC-01
```

CLI：

```text
--images path1
--images path2
--images path3
```

注意：

```text
不是 --image。
```

## 5.2 image2video

manifest：

```text
image = SHOT-01-KF
```

CLI：

```text
--image path1
```

注意：

```text
不传 --ratio。
```

## 5.3 frames2video

推荐 manifest：

```text
first = START_ID
last = END_ID
```

CLI：

```text
--first START_PATH
--last END_PATH
```

如果没有 first/last 字段，可约定：

```text
task_type=frames2video
image=START_ID|END_ID
```

由执行器转换为 first/last。

## 5.4 multiframe2video

manifest：

```text
image = FRAME1|FRAME2|FRAME3
transition_prompt = prompt1|prompt2
transition_duration = duration1|duration2
```

CLI：

```text
--images path1
--images path2
--images path3
--transition-prompt prompt1
--transition-prompt prompt2
```

## 5.5 multimodal2video

manifest：

```text
image = IMG1|IMG2|IMG3
video = VID1
audio = AUD1
```

CLI：

```text
--image IMG_PATH1
--image IMG_PATH2
--image IMG_PATH3
--video VID_PATH1
--audio AUD_PATH1
```

---

# 6. @ 与引用规则

## 6.1 逻辑 ID

```text
A-CH-A-01
SHOT-10-KF
A-SC-03
```

用途：

```text
文档、manifest、DAG、文件命名、依赖关系。
```

不要默认把逻辑 ID 当平台真实 token。

## 6.2 平台 @token

形如：

```text
@图片1
@图片2
```

只有确认平台原生支持且执行器已完成映射时才使用。

## 6.3 CLI 执行层

可靠方式：

```text
--image / --images / --video / --audio + 真实文件路径
```

prompt 中优先写：

```text
参考图1作为角色参考；
参考图2作为场景参考；
参考视频1作为运镜参考。
```

---

# 7. session 规则

所有 generator 命令支持：

```text
--session <id>
```

建议：

```text
每个正式项目创建独立 session；
manifest 可新增 session_id 字段；
没有 session_id 时默认 session 0。
```

---

# 8. 必须更新的旧规则

如果旧 Source 中写过：

```text
image2image -> --image
```

必须改成：

```text
image2image -> --images，可重复，1-10 张
```

如果旧 Source 中写过：

```text
image2video 可传 ratio
```

必须改成：

```text
image2video 不传 ratio，ratio 从输入图推断
```

如果旧 Source 中没有：

```text
frames2video
multiframe2video
```

应加入。

---

# 9. 一句话总结

```text
以 dreamina_cli_help.md 为 CLI 参数最高事实来源：image2image 使用重复 --images；image2video 只接收单张 --image 且不传 ratio；多图/视频/音频参考使用 multimodal2video；首尾帧使用 frames2video；多帧故事使用 multiframe2video。
```
