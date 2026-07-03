# AI视频制作_模仿参考库总体设计_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE
> 类型：模仿参考库总体设计 / Source 候选 / Reference Retrieval System 设计稿
> 版本：V0.1
> 生成日期：2026-07-03
> 生成方：ChatGPT
> 状态：Draft；需用户人工确认后，才可作为 official Source 或本地执行规范使用。
> 适用范围：本地 AI 视频模仿参考库、动作 / 运镜 / FX / 剪辑 / 表演 / 构图 / 环境反馈 / 风格光影 / 声音节奏参考检索、Prompt Compiler、Reference Duty Planner、Review Recorder、Failure Ledger。
> 重要边界：本文件不授权 Dreamina submit / query / download，不授权 Codex 修改 official Source，不授权上传第三方影视 / 游戏 / 动漫 / 教程素材作为 active input。

---

## 0. 一句话结论

```text
AI 视频模仿参考库不是素材库，而是“可检索、可审计、可反馈学习的模仿语法库”。
```

它的核心目标不是保存视频本身，而是把 3000–4000 条、未来数万条参考片段转化为：

```text
可搜索的动作 / 运镜 / 特效 / 剪辑 / 表演 / 构图 / 环境 / 风格 / 声音语法
+ 可复制的 prompt words
+ 可审计的 reference duty
+ 可执行的 do_not_copy
+ 可复用的 review criteria
+ 可学习的 success / failure feedback
```

第一版建议：

```text
Local-first
SQLite + FTS5
segment-first
controlled bilingual tags
rights / safety fields first-class
active_input_allowed=false by default
PySide6 workbench later
Codex L1 local indexer after schema fixed
```

---

## 1. 生成依据

本 V0.1 综合以下六轮 Deep Research：

```text
1. AI Video Mimic Reference Library Tag System
2. Local Video Reference Library Automatic Annotation and Multimodal Retrieval Plan
3. Safety Boundaries for an AI Video Mimic Reference Library
4. AI Video Reference Library Feedback Ranking and Context-Aware Recommendation Research
5. AI 视频模仿参考库的 AE / PR / 后期特效分类体系研究
6. Local-First Workbench for an AI Video Mimic Reference Library
```

并对齐当前项目已有规则：

```text
AI视频制作_自动化治理与Source权限规则
AI视频制作_自动化宏流程与授权等级
AI视频制作_项目蓝图与产品化路线
AI视频制作_Prompt编译器与结果优先动作语法
AI视频制作_动作参考视频库与审片标准
AI视频制作_实测规则库_V1.8 多模态素材职责
AI视频制作_实测规则库_V1.11 连续战斗动作密度
AI视频制作_实测规则库_V1.12 失败台账与路线重置
Dreamina CLI 执行契约与 2026-07-01 help snapshot
```

本文件是综合设计，不是对 Deep Research 原文的直接搬运。外部研究、行业标准和工具建议仅作为 evidence / proposal，进入项目时必须经过项目化改写与人工确认。

---

## 2. 定位：这个库是什么，不是什么

### 2.1 是什么

```text
Mimic Reference Library
Reference Retrieval Engine
CTRL Reference Search
AI_VIDEO_PIPELINE 的参考检索与选择模块
```

它用于：

```text
1. 找动作参考：格挡、滑步、摔倒、打击、hit-stop、反击预备。
2. 找运镜参考：低机位推进、手持微晃、speed ramp push-stop、短环绕。
3. 找特效参考：闪白、震屏、粒子爆散、雨水反馈、glitch、mask transition。
4. 找剪辑节奏：卡点、freeze frame、smash cut、match cut、cut mid-exchange。
5. 找表演参考：迟疑、惊觉、冷笑、呼吸停顿、手部微动作。
6. 找构图 / 空间参考：靠墙压迫、走廊纵深、前景遮挡、近远分层。
7. 找环境反馈：雨水、水花、烟尘、布料、发丝、地面反光。
8. 找风格光影：低饱和冷雨光、noir、高反差、game cinematic、semi-realistic 3D。
9. 找声音节奏：impact sting、whoosh、bass drop、breath cue、beat sync。
```

它服务于：

```text
Prompt Compiler
Reference Duty Planner
Review Recorder
Failure / Success Ledger
Post Plan / Edit Timeline
未来 GUI / Production Cockpit
```

---

### 2.2 不是什么

它不是：

```text
最终素材库
版权素材库
商业可发布素材库
默认 active generation input 库
影视 / 游戏 / 动漫素材搬运库
模型训练数据集
Git media repository
无人审核自动推荐系统
```

特别强调：

```text
第三方影视、电视剧、游戏、动漫、广告、MV、教程、社交平台短视频
默认只作 offline grammar / prompt abstraction / review standard，
不得默认上传给生成平台作为 active input。
```

---

## 3. 核心对象模型

### 3.1 raw_clip

`raw_clip` 是原始导入视频文件。

例：

```text
RAW_000001.mp4
RAW_000002.mov
RAW_000003.mkv
```

职责：

```text
保留来源文件
记录技术元数据
记录来源与版权风险
作为 ref_segment 的父对象
```

不直接作为主要搜索单位。原因：10–24 秒原始片段通常包含多个动作、多个剪辑点或多个可学习元素，直接搜索 raw_clip 会导致搜索结果过粗。

---

### 3.2 ref_segment

`ref_segment` 是真正的检索单位。

例：

```text
REF_ACT_000321_crossed_guard_wet_skid
REF_CAM_000044_low_angle_push_stop
REF_FX_000212_white_flash_micro_shake
REF_EDIT_000077_speed_ramp_cut
```

一个 raw_clip 可以拆成多个 ref_segment：

```text
RAW_000128 24s 原片
  → REF_ACT_000401 0.8s–4.2s 学近身格挡
  → REF_CAM_000178 4.2s–8.0s 学低机位推进
  → REF_FX_000063 8.0s–10.5s 学闪白震屏
```

`ref_segment` 必须能回答：

```text
这一段主要学什么？
不要学什么？
适合 prompt 影响，还是 review 影响？
是否允许 active input？
在什么场景中用过？
成功还是失败？
```

---

### 3.3 reference package

最小可用包：

```text
REF_ACT_000321_crossed_guard_wet_skid.mp4
REF_ACT_000321_crossed_guard_wet_skid.md
```

推荐增强包：

```text
ref_segments/
  REF_ACT_000321_crossed_guard_wet_skid.mp4

notes/
  REF_ACT_000321_crossed_guard_wet_skid.md

thumbs/
  REF_ACT_000321.jpg

frames/
  REF_ACT_000321/
    frame_00_contact_start.jpg
    frame_01_guard_compression.jpg
    frame_02_skid_feedback.jpg
    frame_03_counter_ready.jpg
```

数据库只存路径与元数据，不把原视频塞进 DB。

---

## 4. 三层数据结构

### 4.1 Resource Metadata：资源元数据

描述“这个文件是什么”。

吸收 PBCore / Dublin Core / XMP / IPTC / EBUCore 中适合的基础字段：

```text
identifier
title
description
source
relation
creator
credit_line
copyright_notice
rights_status
format
duration
fps
resolution
aspect_ratio
file_location
digital_source_type
language
```

在本项目中对应：

```text
raw_clips
assets
source records
technical metadata
rights metadata
```

---

### 4.2 Mimic Grammar：模仿语法

描述“它能让模型 / 人类学习什么”。

包括：

```text
action
camera
composition
FX
editing
performance
environment feedback
style / lighting
sound rhythm
animation grammar
game timing
```

它是本库和普通素材库的主要差异。

例如：

```text
crossed_guard_compression
shoulder_forearm_pressure
wet_floor_skid
low_angle_push_stop
one_frame_white_flash
micro_camera_shake
cut_mid_exchange
cold_rain_backlight
breath_pause
```

---

### 4.3 Usage Memory：使用记忆

描述“它在真实项目里好不好用”。

包括：

```text
reference_duty
do_not_copy
prompt_words
review_criteria
post_plan
edit_timeline_note
active_input_allowed
offline_grammar_only
prompt_influence_allowed
review_standard_only
usage_attempts
success_count
failure_count
context_score
risk_score
```

这层让库从“能搜”升级为“会记住哪条在什么场景有效”。

---

## 5. 使用等级与安全边界

### 5.1 usage_class

每个 ref_segment 至少归入一种使用等级：

| usage_class | 含义 | 默认来源 |
|---|---|---|
| `offline_grammar_only` | 只能离线观察、拆语法、做人工理解 | 影视、动漫、游戏、广告、MV、教程、社交短视频 |
| `prompt_influence_allowed` | 可抽象成 prompt words / 动作词 / 运镜词 | 已去 IP 化、去身份、去具体剧情 |
| `review_standard_only` | 只作为审片标准，不参与生成输入 | 高风险但结构有参考价值 |
| `active_input_allowed` | 可上传给模型作为 active reference | 自录、授权、无 IP、无脸、无 logo、无水印、无 UI |
| `do_not_use` | 不使用 | 泄露、盗版、未授权敏感、隐私、未成年人、强风险素材 |

默认：

```text
active_input_allowed=false
offline_grammar_only=true
```

---

### 5.2 active_input_allowed 判定

只有全部通过，才可设为 true：

```text
rights_status = self_owned / licensed / client_approved
无可识别演员脸 / 名人脸 / 隐私人物
无 IP 角色 / 特定服装 / 特定场景强识别
无 logo / 品牌 / 水印 / UI / HUD / 字幕
无版权音乐 / 可识别声音
无 C2PA / Content Credentials “no AI use” 风险
用途职责单一
人工审核通过
```

否则：

```text
active_input_allowed=false
```

---

### 5.3 风险标签 risk_tags

第一版建议：

```text
rights_unknown
license_scope_unclear
public_reference_only
copyright_risk
ip_risk
actor_face
celebrity_face
minor_possible
voice_present
music_present
logo_present
watermark_present
subtitle_burnin
ui_overlay
hud_present
tutorial_overlay
brand_packaging
social_handle_overlay
c2pa_no_ai_flag
source_unknown
reupload_suspected
leak_risk
style_pollution
reference_attention_conflict
active_input_denied
do_not_use
```

搜索模式不同，风险处理不同：

```text
active input 搜索：高风险硬过滤
prompt-only 搜索：高风险降权并提示
review-only 搜索：除 do_not_use 外可显示
offline grammar 搜索：允许显示，但必须标风险
```

---

## 6. 标签体系总览

### 6.1 L1 大类

第一版 L1：

```text
BASIC          基础信息
SOURCE_RIGHTS  来源与版权
INTENT_SAFETY  用途与安全
CONTEXT        场景上下文
ACTION         动作
ANIM_MOTION    动画运动规律
GAME_TIMING    游戏战斗时序
CAMERA         运镜
COMPOSITION    构图与调度
FX             特效 / AE / PR
EDIT           剪辑与节奏
PERFORMANCE    表演与情绪
ENVIRONMENT    环境反馈
STYLE_LIGHT    风格与光影
SOUND_RHYTHM   声音节奏
RISK           风险
USAGE_FEEDBACK 使用结果与反馈
```

---

### 6.2 L2 中类

示例：

```text
ACTION:
guard_block, strike, kick, dodge, grapple, fall, jump, landing, weapon, body_contact, action_timing

CAMERA:
shot_scale, camera_angle, movement, support_style, lens_effect

FX:
impact_fx, light_fx, particle_fx, distortion_fx, transition_fx, graphic_overlay, post_method

EDIT:
cut_type, tempo, timing_pattern, narrative_function

COMPOSITION:
space_type, blocking, subject_relation, framing_rule, axis_continuity

PERFORMANCE:
emotion, facial_cue, body_cue, gaze, breath

ENVIRONMENT:
weather, surface_response, material_response, cloth_hair_response
```

---

### 6.3 L3 细标签

L3 只给高价值片段或高频查询片段深标。

示例：

```text
crossed_guard_compression
shoulder_forearm_pressure
wet_floor_skid
rear_foot_slide
counter_ready_twist
speed_ramp_push_stop
one_frame_white_flash
micro_camera_shake
shock_ripple
mask_transition
smear_frame
hitstop_contact
cut_mid_exchange
cold_rain_backlight
foreground_obstruction
near_wall_pressure
```

原则：

```text
标签字典可以提前细；
每条视频不必一次填满；
全库先 L1/L2 粗标；
rating 4–5 或高复用片段再 L3 深标。
```

---

## 7. 搜索体系

### 7.1 四种检索通道

```text
1. Exact facet filter
2. SQLite FTS5 full-text search
3. Semantic / vector search later
4. Feedback-weighted reranking
```

#### Exact facet filter

用于硬筛：

```text
ref_type
source_type
rights_status
active_input_allowed
usage_class
duration
risk_tags
fx_execution_mode
review_status
```

#### FTS5 full-text search

用于像搜索引擎一样查：

```text
query_text
prompt_words
reference_duty
do_not_copy
review_criteria
notes
tags aliases
OCR / ASR text
```

#### Semantic search

第二阶段再加：

```text
text → video
image → video
video → video
similar segment
```

#### Feedback-weighted reranking

使用上下文成功 / 失败记录调整排序。

---

### 7.2 搜索结果分桶

不建议只给一条长列表。建议分桶：

```text
Best Fit Now
Prompt-only References
Review-only References
Active-input-safe References
Offline Grammar References
Explore / 未验证候选
High-risk Observation Only
```

对 FX 类还可分：

```text
Model-first
Model-plus-post
Post-only
Edit-rhythm-only
Review-standard-only
Offline-grammar-only
```

---

### 7.3 搜索结果卡片字段

每个卡片显示：

```text
thumb / contact sheet
ref_id
title
ref_type
source_type
duration
useful_window
primary_learning
top_tags
usage_class
active_input_allowed
risk badges
quality_score
context_success_summary
latest_used_at
one-line reference_duty
copy buttons
```

复制按钮：

```text
copy prompt_words
copy reference_duty
copy do_not_copy
copy review_criteria
copy post_plan
copy edit_timeline_note
copy ref path
```

---

## 8. 排序与反馈权重

### 8.1 第一版排序公式

```text
final_score =
  0.30 * facet_match_score
+ 0.20 * fts_bm25_score
+ 0.15 * exact_tag_overlap
+ 0.15 * context_success_score
+ 0.08 * human_quality_score
+ 0.05 * novelty_bonus
+ 0.07 * diversity_bonus
- 0.20 * risk_penalty
- 0.15 * context_failure_penalty
- 0.10 * redundancy_penalty
```

解释：

```text
facet_match_score：标签 / 类型 / 安全边界匹配
fts_bm25_score：全文搜索命中
context_success_score：类似场景中成功过
human_quality_score：人工评分
novelty_bonus：新候选探索
diversity_bonus：避免十条都一样
risk_penalty：版权 / IP / 水印 / 脸 / UI 风险
context_failure_penalty：类似场景失败过
redundancy_penalty：同源 / 同动作重复过多
```

---

### 8.2 context_key

必须区分全局失败与局部失败。

推荐三层：

```text
strict_context_key
soft_context_key
coarse_context_key
```

示例：

```text
strict_context_key =
wuxia_action | rainy_corridor | near_wall_guard_clash |
ACT:shoulder_pressure+crossed_guard+wet_skid |
CAM:medium_close+slight_push |
FX:rain_spray |
text2video | seedance2

soft_context_key =
rainy_corridor | close_combat | guard_clash | wet_floor | video

coarse_context_key =
ACTION | close_combat | video
```

失败只应强烈影响 strict context，不应直接全局降权。

---

### 8.3 feedback events

每次使用参考后，至少记录：

```text
attempt_id
project_name
shot_id
context_key
model_name
task_type
selected_ref_ids
usage_mode
result_status
success_type
failure_type
visual_score
human_note
next_action
created_at
```

result_status：

```text
success
partial_success
failure
active_input_failed
prompt_only_success
review_only_useful
unsafe_blocked
not_tested
```

failure_type 可继承项目失败台账：

```text
visual_execution_failure
prompt_priority_failure
reference_attention_conflict
identity_drift
timing_tail_poseout_failure
video_action_quality_failure
style_pollution
action_too_weak
wrong_camera
active_input_rejected
```

---

## 9. 自动标注与人工确认

### 9.1 自动标注职责

第一版自动完成：

```text
ffprobe metadata
duration / fps / resolution / codec
sha256
thumbnail
contact sheet
keyframes
scene / shot boundary candidate
ASR transcript
OCR text
face_present
watermark_present
subtitle_present
ui_hud_present
pose / face summary
CLIP / OpenCLIP embedding
filename tag extraction
rule-based initial risk_tags
```

自动标注只给：

```text
candidate tags
confidence
source_method=auto
```

不得直接把自动标签当人工确认标签。

---

### 9.2 人工确认职责

必须人工确认：

```text
primary_ref_type
primary_learning
usage_class
active_input_allowed
rights_status
reference_duty
do_not_copy
prompt_ready
success / failure feedback
```

高风险字段必须人工：

```text
IP 风险
演员 / 名人脸
版权风险
active input 白名单
do_not_use
```

---

### 9.3 标注等级

```text
L0 raw_imported
自动导入，只知道文件和元数据。

L1 triaged
人工粗标：ref_type、source_type、primary_learning、usage_class、risk。

L2 tagged_ref
已有 L1/L2 标签、useful_window、质量评分，可搜索。

L3 prompt_ready
已有 prompt_words、reference_duty、do_not_copy、review_criteria。

L4 proven_context
已经在真实项目/场景中使用并有 success/failure 记录。

L5 active_safe
通过权利、安全、人工审核，可作为 active input 候选。
```

---

## 10. Reference Duty 输出规范

每个 prompt-ready ref_segment 必须可导出：

```text
reference_duty
do_not_copy
prompt_words
review_criteria
```

### 10.1 ACTION 模板

```text
REF_ACT_000321 只作为动作语法参考。
只参考：近身接触、身体发力路径、护架压缩、后脚滑退、雨水反馈和反击预备节奏。
不要复制：人物身份、演员脸、服装、场景、道具、镜头背景、台词、音乐、剧情或原镜头顺序。
```

### 10.2 CAMERA 模板

```text
REF_CAM_000044 只作为运镜参考。
只参考：低机位推进速度、镜头方向、停顿节奏和轻微手持惯性。
不要复制：参考视频中的人物、场景、光影、道具、品牌、剧情或美术风格。
```

### 10.3 FX 模板

```text
REF_FX_000212 只作为特效节奏参考。
只参考：命中瞬间闪白、2–3 帧微震、粒子散开的先后顺序和衰减节奏。
不要复制：原视频人物、场景、logo、UI、字幕、水印、品牌包装、IP 造型或具体画面构图。
```

### 10.4 EDIT 模板

```text
REF_EDIT_000077 只作为剪辑节奏参考。
只参考：切点位置、speed ramp 节奏、hit-stop 停顿长度和 cut mid-exchange 的收尾方式。
不要复制：原画面内容、原镜头顺序、原音乐、原字幕、原人物或原剧情。
```

---

## 11. AE / PR / 后期特效执行归属

### 11.1 fx_execution_mode

```text
generate_inside_model
generate_plus_post
post_only
editing_reference_only
review_standard_only
```

判断原则：

```text
场景原生效果 → 模型生成或模型+后期
精确文字 / logo / HUD / UI / 分屏 / screen replacement → post_only
精确 cut point / speed ramp / freeze frame → editing_reference_only 或 post_only
仅用于判断生成结果是否对 → review_standard_only
```

### 11.2 决策表

| 问题 | 是 | 决策 |
|---|---|---|
| 效果是场景内物理现象？ | 是 | generate_inside_model / generate_plus_post |
| 需要精确文字、版式、logo、HUD、UI？ | 是 | post_only |
| 本质是时间线重定时、卡点、cut point？ | 是 | editing_reference_only |
| 素材有水印、字幕、UI、品牌、IP？ | 是 | offline_grammar_only |
| 只用于判断效果是否达标？ | 是 | review_standard_only |

---

## 12. 本地文件夹结构

推荐：

```text
reference_library/
  raw_clips/
    RAW_000001.mp4
    RAW_000002.mp4

  ref_segments/
    REF_ACT_000001_guard_clash_skid.mp4
    REF_CAM_000001_low_angle_push_stop.mp4
    REF_FX_000001_hit_flash_shake.mp4

  derived/
    thumbs/
    contact_sheets/
    keyframes/
    waveforms/
    proxies/

  notes/
    REF_ACT_000001_guard_clash_skid.md

  db/
    refs.sqlite
    backups/

  manifests/
    refs_export.csv
    tags_export.csv

  logs/
    ingest.log
    feedback.log
```

不要把 raw_clips / ref_segments 放进普通 Git。

Git 只管理：

```text
schema.sql
tag_dictionary.csv
template.md
source candidate docs
small manifests
tool code
```

---

## 13. 数据库核心表

第一版最少：

```text
raw_clips
ref_segments
tags
tag_aliases
segment_tags
contexts
attempts
attempt_segment_refs
segment_context_stats
feedback_events
ref_segments_fts
```

### 13.1 raw_clips

```text
raw_id
source_type
source_name
source_url
local_path
sha256
duration_ms
width
height
fps
codec
has_audio
rights_status
imported_at
notes
```

### 13.2 ref_segments

```text
ref_id
raw_id
title
primary_ref_type
secondary_ref_types
local_path
thumb_path
contact_sheet_path
start_ms
end_ms
duration_ms
useful_window
summary
query_text
prompt_words_zh
prompt_words_en
reference_duty
do_not_copy
review_criteria
post_plan
edit_timeline_note
active_input_allowed
offline_grammar_only
prompt_influence_allowed
review_standard_only
do_not_use
review_status
quality_score
risk_score
notes
extra_json
```

### 13.3 tags

```text
tag_key
zh_label
en_label
category
level
parent_tag_key
aliases
exact_filter_default
fulltext_default
semantic_default
weight_stats_default
description
```

### 13.4 attempts

```text
attempt_id
project_name
shot_id
context_key
search_query
model_name
task_type
selected_ref_ids
usage_mode
result_status
success_type
failure_type
visual_score
human_note
created_at
```

---

## 14. GUI / Workbench 方向

### 14.1 第一版产品形态

推荐：

```text
PySide6 + SQLite + FTS5 + FFmpeg / ffprobe + PySceneDetect
```

理由：

```text
本地 Windows 友好
适合桌面文件操作
适合表格 / 树 / 快捷键 / 多窗格
不需要先做浏览器权限模型
不需要云端
```

### 14.2 页面模块

```text
Library Home
Ingest Queue
Clip Browser
Reference Search
Reference Detail
Batch Tagging
Attempt Recorder
Feedback / Stats
Admin / Tag Dictionary
Backup / Export
```

### 14.3 核心 UI 结构

```text
左：搜索栏 + facet filters
中：结果卡片 / 列表 / contact sheet
右：详情 + 视频预览 + 标签 + reference duty + copy buttons
下：attempt / feedback quick form
```

---

## 15. 与 AI_VIDEO_PIPELINE 的对接

### 15.1 Prompt Compiler

参考库输出：

```text
prompt_words
reference_duty
do_not_copy
review_criteria
post_plan
edit_timeline_note
risk_tags
```

Prompt Compiler 使用：

```text
P0：主视觉结果 / 动作因果 / 时间窗
P1：身份 / 场景 / 镜头 / reference duty
P2：compact negatives / do_not_copy
```

禁止：

```text
把 reference duty 放到 P0 前面
把参考视频当作要复制的源画面
把 active_input_allowed=false 的片段上传给生成平台
```

---

### 15.2 Review Recorder

参考库提供审片标准：

```text
动作因果是否清楚？
接触点是否读得懂？
受力反馈是否成立？
运镜速度是否接近？
特效出现点是否对？
尾段是否 static pose-out？
是否泄漏原参考的人物 / 场景 / IP / logo？
```

Review Recorder 把结果写回：

```text
feedback_events
segment_context_stats
attempts
failure ledger
success ledger
```

---

### 15.3 Failure Ledger

失败不只记录“这个参考不好”。

必须写：

```text
这个参考在什么 context 下失败？
失败是动作、运镜、特效、风格、身份还是安全？
是 active input 失败，还是 prompt-only 失败？
是否仍可作为 review standard？
是否只需降权，不需全局禁用？
```

---

## 16. Codex / Agent 边界

### 16.1 Codex 可做

```text
读取设计文档
读取标签字典
读取本地视频目录
生成 refs.sqlite
运行 ffprobe / ffmpeg / PySceneDetect
生成 thumbnails / contact sheets
导入 CSV / SQL
生成 refsearch CLI
生成本地 reports
```

### 16.2 Codex 不可做

```text
修改 official Source
把参考视频提交进 Git
把第三方参考视频上传给 Dreamina
运行 Dreamina submit / query / download
自动判定 active_input_allowed=true
自动 final / lock
自动公开导出参考视频
```

### 16.3 L1 Indexer 授权边界

首个 Codex 任务应为：

```text
L1 local artifacts only
no Dreamina
no submit
no query
no download
no media generation
no Source modification
no Git media stage
```

---

## 17. 最小可落地版本 MVP

### 17.1 MVP 必须有

```text
refs.sqlite
schema.sql
tag_dictionary.csv
import_refs.py
extract_thumbs.py
refsearch.py
feedback_log.py
reference_library/ folder structure
```

功能：

```text
扫描 raw_clips
写 raw_clips 表
抽 metadata / thumb / contact sheet
人工导入 / 修改标签
FTS5 搜索
按 usage_class / risk / ref_type 过滤
复制 reference duty / prompt words
记录 success / failure
导出 CSV
```

### 17.2 MVP 不做

```text
不做完整 GUI
不做云同步
不做多用户权限
不做自动上传生成平台
不做复杂向量数据库
不做自动法律判断
不做自动深标 4000 条
不做模型训练
不做最终剪辑系统
```

---

## 18. 未来扩展路线

### Phase 1：本地索引

```text
SQLite + FTS5
raw_clips / ref_segments
手动标签 + 自动 metadata
refsearch CLI
```

### Phase 2：自动标注增强

```text
ASR / OCR
PySceneDetect
OpenCLIP embedding
MediaPipe risk flags
similar segment search
```

### Phase 3：Workbench

```text
PySide6 GUI
Clip Browser
Search Panel
Batch Tagging
Reference Duty Export
Attempt Recorder
```

### Phase 4：语义 / 向量搜索

```text
SQLite Vec1 or FAISS
Qdrant local optional
hybrid lexical + vector
MMR diversity reranking
```

### Phase 5：Production Cockpit

```text
和 AI_VIDEO_PIPELINE GUI 合并
Asset Planner
Prompt Compiler
Reference Duty Planner
Review Panel
Failure Ledger
Authorization Gate
```

---

## 19. 推荐后续文档

本总纲之后，建议继续生成：

```text
02_AI视频制作_模仿参考库标签字典_V0.1.csv
03_AI视频制作_模仿参考库数据库Schema_V0.1.sql
04_AI视频制作_模仿参考库ReferenceDuty与安全规则_V0.1.md
05_AI视频制作_模仿参考库GUI与人工标注流程_V0.1.md
06_Codex_L1_REF_LIBRARY_INDEXER_SPEC_V0.1.md
```

---

## 20. Final Verdict

```text
MIMIC_REFERENCE_LIBRARY_SYSTEM_DESIGN_V0_1_READY
```

当前结论：

```text
六轮 Deep Research 已足够。
停止继续泛化调研。
进入 Source 候选 / schema / tag dictionary / Codex L1 local indexer 落地阶段。
```
