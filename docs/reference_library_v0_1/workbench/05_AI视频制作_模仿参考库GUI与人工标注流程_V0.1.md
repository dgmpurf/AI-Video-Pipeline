# AI视频制作_模仿参考库GUI与人工标注流程_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE
> 类型：模仿参考库工作台设计稿 / GUI 与人工标注流程规范 / Source 候选
> 版本：V0.1 Draft
> 生成日期：2026-07-03
> 生成方：ChatGPT
> 适用范围：本地 AI 视频模仿参考库；动作、运镜、AE/PR/后期特效、剪辑节奏、表演、构图、环境反馈、风格光影、声音节奏参考的检索、标注、预览、导出和反馈记录。
> 状态：Draft / Source 候选。进入 official Source 前需人类手动确认和上传。
> 重要边界：本文件不授权 Codex 运行 Dreamina，不授权 submit/query/download/retry/resubmit，不授权修改 official Source，不授权把参考视频上传为 active input。

---

## 0. 一句话结论

```text
模仿参考库第一版应做成本地搜索工作台：
PySide6 + SQLite + FTS5 + FFmpeg/PySceneDetect，
先解决“搜、看、标、选、导出、记录反馈”，
不要一开始做大型素材平台或云端多用户系统。
```

这不是普通素材管理器，也不是最终资产库。它是：

```text
Reference Search + Annotation + Reference Duty Export + Review Feedback Recorder
```

它服务于：

```text
Prompt Compiler
Reference Duty Planner
Review Recorder
Failure / Success Ledger
后期剪辑规划
未来 GUI production cockpit
```

---

## 1. 定位与非目标

### 1.1 定位

本地模仿参考库工作台用于管理：

```text
raw_clip：原始找到的视频文件，通常 10–24 秒。
ref_segment：从 raw_clip 中切出的可模仿窗口，通常 2–8 秒。
tagged_ref：已粗标 / 已深标的参考片段。
prompt_ready_ref：可直接导出 prompt words / reference duty / review criteria 的高价值片段。
```

核心工作不是“收藏视频”，而是回答：

```text
这个镜头需要什么参考？
哪条参考最适合？
这条参考只能学什么？
不能复制什么？
它过去在类似场景中成功还是失败？
它该影响 prompt、审片标准，还是后期计划？
```

### 1.2 非目标

第一版不做：

```text
云端素材平台
多人权限系统
在线协同
自动上传生成平台
自动选择并提交 Dreamina
复杂 NLE 时间线编辑器
全自动版权合规判断
全自动精细动作识别
完整向量数据库服务
```

### 1.3 默认安全边界

所有新导入视频默认：

```text
active_input_allowed = false
offline_grammar_only = true
prompt_influence_allowed = false until reviewed
review_standard_only = false until reviewed
human_review_required = true for active input
```

外部影视、电视剧、游戏、动漫、广告、教程、社交短视频默认不作为 active input，只作为：

```text
offline grammar
prompt influence after abstraction
review standard
post/edit grammar
```

---

## 2. 推荐产品形态

### 2.1 第一版推荐栈

```text
主界面：PySide6 桌面应用
数据库：SQLite + FTS5
媒体处理：ffprobe / ffmpeg
场景切分：PySceneDetect
缩略图 / contact sheet：ffmpeg
本地搜索：FTS5 + facets
后续语义搜索：OpenCLIP embeddings + sqlite-vec / FAISS
后台任务：Python worker，可选 FastAPI local worker
```

### 2.2 为什么第一版推荐 PySide6

| 方案 | 适合程度 | 说明 |
|---|---:|---|
| PySide6 | 高 | 最适合本地桌面、视频预览、表格、树状标签、快捷键、大量文件路径操作。 |
| Tauri + React | 中高 | 适合二期现代前端，但文件权限、WebView、前后端桥接会增加第一版复杂度。 |
| Electron | 中 | 成熟但重，需要处理 Chromium / Node / 安全边界。第一版不必。 |
| Streamlit | 中 | 适合快速内部 demo，不适合高频快捷键和长期桌面工作台。 |
| Gradio | 中 | 适合模型 demo / embedding inspector，不适合作主工作台。 |
| PySide + FastAPI local worker | 高 | 当后台任务变多时可用；主界面仍保持桌面化。 |
| Tkinter | 低中 | 够做小工具，不适合长期 GUI cockpit。 |

### 2.3 产品形态总览

```text
Reference Workbench
├── Library Home
├── Ingest Queue
├── Raw Clip Browser
├── Segment Editor
├── Reference Search
├── Reference Detail
├── Batch Tagging
├── Reference Duty Export
├── Attempt Recorder
├── Feedback / Stats Panel
├── Tag Dictionary Admin
├── Safety Review Queue
└── Backup / Export
```

---

## 3. 页面 / 模块清单

### 3.1 Library Home

用途：一眼看库的状态。

显示：

```text
总 raw_clips 数
总 ref_segments 数
待处理导入数
待粗标数
待深标数
prompt_ready 数
active_safe 候选数
offline_only 数
rejected 数
最近使用的参考
最近失败的参考
需要人工安全确认的参考
```

推荐卡片：

```text
Import backlog
Triage backlog
Prompt-ready refs
Active-input review queue
Recently successful refs
Recently failed refs
```

---

### 3.2 Ingest Queue

用途：导入新视频并生成初始 artifact。

每条 raw_clip 显示：

```text
文件名
路径
时长
分辨率
fps
codec
是否有音频
source_type 初猜
rights_status 默认 unknown
ingest_status
probe_status
thumb_status
contact_sheet_status
scene_detect_status
```

操作：

```text
Scan folder
Import selected
Run ffprobe
Generate poster
Generate contact sheet
Run scene detect
Mark source_type
Mark rejected
Open raw clip
```

第一版自动导入只做本地 artifact，不进入 Dreamina，不提交，不上传。

---

### 3.3 Raw Clip Browser

用途：查看原始视频和候选片段。

布局：

```text
左：raw_clip 列表 / 文件夹树
中：视频播放器
下：时间轴 + scene cut markers
右：metadata / candidate segments / risk flags
```

显示：

```text
video preview
poster frame
contact sheet
keyframes
scene detection markers
audio waveform optional
OCR / ASR indicators optional
risk badges
```

操作：

```text
Create segment from in/out
Accept scene-detected segment
Merge segments
Split segment
Reject raw clip
Open in file explorer
Copy local path
```

---

### 3.4 Segment Editor

用途：把 raw_clip 中真正有用的窗口变成 ref_segment。

必填字段：

```text
ref_id
raw_id
start_time
end_time
primary_ref_type
title
primary_learning
status
usage_class
```

推荐字段：

```text
useful_window
prompt_words_zh
prompt_words_en
reference_duty
do_not_copy
review_criteria
post_plan
edit_timeline_note
quality_score
risk_tags
```

支持：

```text
A/B loop playback
frame step
set start
set end
generate thumb
generate mini contact sheet
save segment
export segment file optional
```

---

### 3.5 Reference Search

用途：像搜索引擎一样查参考。

搜索模式：

```text
Keyword Search：FTS5
Facet Search：标签 / 来源 / 风险 / 状态
Prompt Duty Search：只搜 prompt_words / reference_duty / review_criteria
Similar Search：第一版用标签相似，二期用 embedding
Context Search：带 scene_signature / context_key 的推荐
```

左侧 facets：

```text
primary_ref_type
source_type
usage_class
active_input_allowed
rights_status
status
risk_tags
action_tags
camera_tags
fx_tags
edit_tags
performance_tags
environment_tags
style_tags
quality_score
duration range
```

结果分桶：

```text
Best fit now
Prompt-ready
Active-safe candidates
Offline grammar only
Review standard only
Post-only / edit-only
Explore / untested
Rejected hidden by default
```

---

### 3.6 Reference Detail

用途：查看一条 ref_segment 的完整信息。

显示区块：

```text
Preview
Core metadata
Tags
Risk and safety
Reference duty
Do not copy
Prompt words
Review criteria
Post plan
Edit timeline note
Usage history
Context stats
Related refs
```

操作：

```text
Copy prompt words
Copy reference duty
Copy do_not_copy
Copy review criteria
Copy post plan
Copy edit timeline note
Open raw clip
Open segment file
Mark used in attempt
Mark prompt_ready
Mark active-safe review required
Mark rejected
```

---

### 3.7 Batch Tagging

用途：快速处理大量素材，避免逐条深标。

支持：

```text
多选
批量添加标签
批量移除标签
批量设置 source_type
批量设置 usage_class
批量设置 status
批量设置 risk_tags
批量复制上一条标注
AI suggested tags review
keyboard-only tagging
```

推荐界面：

```text
左：待标注队列
中：大缩略图 / contact sheet / 短预览
右：标签面板 + suggested tags
下：快捷键提示 + save next
```

---

### 3.8 Safety Review Queue

用途：只处理可能成为 active input 的素材。

进入条件：

```text
active_input_candidate = true
或
user manually requests active review
或
source_type in self_shot / licensed / mocap / graybox
```

审核问题：

```text
是否自有 / 授权 / 客户明确批准？
是否无可识别人脸？
是否无 logo / watermark / UI / HUD / subtitle？
是否无音乐 / 语音权利风险？
是否无 IP 角色 / 特定服装 / 特定场景？
是否职责单一？
是否确实需要 active input，而不是 prompt words 足够？
```

输出：

```text
active_input_allowed = true / false
usage_class
risk_tags
reviewer
reviewed_at
safety_note
```

---

### 3.9 Reference Duty Export

用途：为 Prompt Compiler 生成安全可复制文本。

输出模板：

```text
[REF_ID] 只作为【动作/运镜/特效/剪辑/表演/构图/环境/风格/声音】参考。
只参考：【具体可学习点】。
不要复制：【人物、脸、服装、场景、IP、logo、UI、水印、台词、音乐、剧情、镜头背景】。
使用方式：【offline grammar / prompt influence / review standard / active input】。
```

支持导出：

```text
single ref duty
multi-ref duty pack
Prompt Compiler block
Review criteria block
Post plan block
Attempt record stub
```

---

### 3.10 Attempt Recorder

用途：记录“本次生成用了哪些参考，结果如何”。

字段：

```text
attempt_id
project_name
shot_id
context_key
task_type
model_name
model_version
prompt_id
selected_ref_ids
selected_roles
usage_modes
result_status
visual_score
success_type
failure_type
human_note
created_at
```

结果类型：

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

---

### 3.11 Feedback / Stats Panel

用途：查看参考片段在不同上下文中的表现。

显示：

```text
global used_count
global success_count
global failure_count
context success rate
strict_context stats
soft_context stats
coarse_context stats
model-specific stats
task-type stats
latest_used_at
failure modes
success scopes
```

支持：

```text
查看为什么排在前面
查看为什么被降权
人工 pin / unpin
人工 boost / suppress
reset context stats
export feedback ledger
```

---

### 3.12 Tag Dictionary Admin

用途：维护标签字典，不让标签越打越乱。

操作：

```text
新增 tag
修改 aliases
设置 parent_tag
设置 L1/L2/L3
设置是否用于 exact filter
设置是否用于 fulltext
设置是否用于 semantic
设置是否用于 weighting
合并重复标签
废弃标签
导入 / 导出 CSV
```

第一版建议：只允许维护者操作，不做复杂权限系统。

---

## 4. 核心用户流程

### 4.1 导入流程：raw_clip → ref_segment → tagged_ref → prompt_ready

```text
1. 用户把视频放入 import_inbox/
2. Workbench 扫描文件夹
3. ffprobe 读取技术信息
4. ffmpeg 生成 poster / contact sheet
5. PySceneDetect 生成候选 scene cuts
6. raw_clip 进入 Ingest Queue
7. 用户粗看，决定 keep / reject
8. 用户从 raw_clip 中切出 ref_segment
9. 用户给 ref_segment 粗标 L1/L2
10. 高价值 ref_segment 进入深标
11. 写 prompt_words / reference_duty / do_not_copy / review_criteria
12. 标为 prompt_ready
13. 后续搜索、选择、使用、反馈
```

### 4.2 搜索使用流程

```text
1. 用户写当前镜头需求：
   “雨夜走廊，近身护架压缩，湿地滑步，短暂 hit-stop。”

2. 在 Reference Search 搜：
   guard clash wet skid rain hit-stop

3. 过滤：
   primary_ref_type = ACTION
   usage_class = prompt_influence_allowed / offline_grammar_only
   risk = hide do_not_use

4. 查看结果卡片：
   thumb / tags / score / risk / reference duty

5. 选 1 条主参考，最多 1–2 条辅助参考。

6. 点击复制：
   prompt_words
   reference_duty
   do_not_copy
   review_criteria

7. 粘贴进 Prompt Compiler 或 package notes。

8. 生成后回到 Attempt Recorder 标记结果。
```

### 4.3 active input 使用流程

```text
1. 搜索时切换 mode = active_input
2. 系统硬过滤 active_input_allowed=false
3. 只显示 active-safe 片段
4. 用户检查 reference duty
5. 使用后 attempt 记录 selected_ref_ids
6. 如果结果污染身份 / 场景 / 风格，标记 active_input_failed
7. 系统降低该 context 下 active usage 权重
```

### 4.4 offline grammar 使用流程

```text
1. 搜索任意外部片段
2. 只看动作 / 运镜 / 特效 / 剪辑语法
3. 不上传视频
4. 只复制 prompt_words / review_criteria
5. 生成结果后记录 prompt_only_success / review_only_useful / failure
```

---

## 5. 人工标注分级流程

### 5.1 Level 0：自动导入

自动生成：

```text
raw_id
file_path
sha256
duration
fps
resolution
codec
audio_present
poster_path
contact_sheet_path
scene_detect_json
imported_at
```

无需人工填写。

### 5.2 Level 1：粗标

人工必填：

```text
keep / reject
primary_ref_type
source_type
usage_class
status
primary_learning
risk_level
```

推荐用时：每条 10–30 秒。

状态：

```text
raw
triaged
rejected
```

### 5.3 Level 2：片段标注

人工填写：

```text
ref_segment start/end
title
L1/L2 tags
useful_window
primary_learning
secondary_learning
quality_score
risk_tags
```

状态：

```text
tagged_ref
```

### 5.4 Level 3：prompt-ready 深标

只对高价值片段做。

填写：

```text
prompt_words_zh
prompt_words_en
reference_duty
do_not_copy
review_criteria
post_plan
edit_timeline_note
scoring
context hints
```

状态：

```text
prompt_ready
```

### 5.5 Level 4：active-safe 审核

只对自录 / 授权 / 灰盒 / 动捕等候选做。

填写：

```text
active_input_allowed
safety_review_status
reviewer
reviewed_at
safety_note
provider_input_risk
```

状态：

```text
active_safe
```

### 5.6 Level 5：使用反馈

每次使用后记录：

```text
attempt_id
usage_mode
result_status
success_type
failure_type
visual_score
human_note
would_reuse
```

系统更新：

```text
used_count
success_count
partial_success_count
failure_count
context_score
latest_used_at
```

---

## 6. 搜索界面设计

### 6.1 搜索栏

支持：

```text
中文关键词
英文关键词
混合关键词
标签 key
别名
短句
project context
```

示例：

```text
湿地滑步 护架压缩 雨水
crossed guard wet skid
low angle push stop
impact flash camera shake
fear to resolve breath pause
```

### 6.2 Facet 区域

必备 facet：

```text
primary_ref_type
source_type
usage_class
active_input_allowed
rights_status
status
risk_tags
duration
quality_score
success_count
failure_count
```

分类 facet：

```text
action_tags
camera_tags
fx_tags
edit_tags
composition_tags
performance_tags
environment_tags
style_tags
sound_tags
```

### 6.3 搜索模式

```text
All references
Prompt-ready only
Active input safe
Offline grammar
Review standard
Post-only
Recently successful
Recently failed
Untested explore
```

### 6.4 搜索结果排序

第一版：

```text
final_score =
  0.35 * exact_tag_match
+ 0.20 * fts_rank_score
+ 0.15 * quality_score
+ 0.15 * context_success_score
+ 0.10 * prompt_ready_bonus
+ 0.05 * diversity_bonus
- 0.20 * risk_penalty
- 0.15 * context_failure_penalty
```

active input 模式：

```text
active_input_allowed=false → hard filter
do_not_use=true → hard filter
watermark/logo/UI/actor_face → hard filter unless manually allowed
```

offline grammar 模式：

```text
high risk refs 可显示，但标红 / 降权 / 禁止 active export
```

---

## 7. 搜索结果卡片字段

### 7.1 Grid card

显示：

```text
thumbnail
ref_id
title
duration
primary_ref_type
top tags
usage badge
risk badges
quality score
context success summary
one-line learning
```

### 7.2 List row

字段：

```text
ref_id
title
source_type
primary_ref_type
duration
status
usage_class
active_input_allowed
quality_score
success/failure
primary_learning
tags
risk_tags
```

### 7.3 Detail drawer

显示：

```text
video preview
mini contact sheet
metadata
tags
reference_duty
do_not_copy
prompt_words
review_criteria
post_plan
edit_timeline_note
usage history
copy buttons
```

### 7.4 关键 badges

```text
PROMPT_READY
ACTIVE_SAFE
OFFLINE_ONLY
REVIEW_ONLY
POST_ONLY
EDIT_ONLY
DO_NOT_USE
IP_RISK
ACTOR_FACE
WATERMARK
UI_HUD
SUBTITLE
LOGO
STYLE_POLLUTION_RISK
REFERENCE_ATTENTION_CONFLICT
```

---

## 8. 批量标注与快捷键建议

### 8.1 核心快捷键

```text
Space：播放 / 暂停
J/K/L：后退 / 暂停 / 前进
I：设置 segment in
O：设置 segment out
S：保存 segment
N：下一条
B：上一条
1–9：快速打常用标签
A：标记 active candidate
P：标记 prompt_ready
G：标记 offline grammar
R：标记 review standard
X：reject
D：复制上一条标签
Ctrl+Enter：保存并下一条
Ctrl+C：复制当前 reference duty
Ctrl+Shift+C：复制全部 export block
```

### 8.2 批量操作

```text
批量添加标签
批量删除标签
批量设置 source_type
批量设置 usage_class
批量设置 status
批量设置 rights_status
批量设置 risk_tags
批量生成 thumbs
批量重建 FTS
批量导出 CSV
```

### 8.3 AI 预填与人工确认

AI / 脚本可预填：

```text
source_type guess
duration
resolution
scene cuts
thumbs
contact sheet
OCR text
ASR transcript
face_present
logo_present
watermark_present
motion intensity
suggested L1/L2 tags
suggested query_text
```

必须人工确认：

```text
active_input_allowed
rights_status
usage_class upgrade
reference_duty
do_not_copy
prompt_ready
deep L3 action tags
success / failure
final rating
```

---

## 9. Reference Duty 复制 / 导出流程

### 9.1 单条导出

```text
[REF_ACT_000123] 只作为动作节奏参考。
只参考：近身接触、护架压缩、后脚滑退、雨水反馈。
不要复制：人物身份、服装、场景、台词、剧情、镜头背景、logo、水印、字幕。
使用方式：prompt influence only；不作为 active input。
```

### 9.2 多条导出

```text
Reference Pack:

REF_ACT_000123：只参考动作节奏和身体受力。
REF_CAM_000044：只参考低机位推进速度和停顿。
REF_FX_000091：只参考 hit-stop 闪白和轻微震屏节奏。

不要让任何参考承担人物身份、场景、服装、剧情或 IP 风格。
```

### 9.3 Prompt Compiler Block

```text
REFERENCE DUTY:
- ACTION REF: [id] only for body mechanics and contact timing.
- CAMERA REF: [id] only for camera speed, direction, and stop timing.
- FX REF: [id] only for impact flash timing and shake decay.

DO NOT COPY:
identity, face, costume, original scene, logo, UI, subtitles, watermark, dialogue, music, plot, exact composition.
```

### 9.4 Review Criteria Block

```text
Review criteria derived from selected refs:
1. 是否第一帧已近身？
2. 是否有清楚接触 / 压力点？
3. 是否有受力反应？
4. 是否有环境反馈？
5. 是否出现参考污染？
6. 是否能剪出目标时间窗？
```

---

## 10. 成功失败反馈录入流程

### 10.1 使用后最小反馈

每次使用后最少填：

```text
attempt_id
selected_ref_ids
context_key
usage_mode
result_status
visual_score
human_note
```

### 10.2 result_status

```text
success
partial_success
failure
prompt_only_success
review_only_useful
active_input_failed
unsafe_blocked
not_tested
```

### 10.3 success_type

```text
action_success
camera_success
fx_success
edit_success
performance_success
composition_success
style_success
environment_success
review_standard_success
prompt_words_success
```

### 10.4 failure_type

```text
visual_execution_failure
prompt_priority_failure
reference_attention_conflict
identity_drift
style_pollution
camera_conflict
action_too_weak
timing_tail_poseout_failure
active_input_rejected
unsafe_reference_pollution
context_mismatch
```

### 10.5 反馈更新规则

```text
success:
  strict_context success +1
  soft_context success +0.5
  global success +0.2

partial_success:
  strict_context partial +1
  notes required

failure:
  strict_context failure +1
  soft_context failure +0.3
  global failure only if repeated across contexts

active_input_failed:
  active_input usage score down
  offline grammar score unchanged unless prompt污染

review_only_useful:
  review_standard score up
  active_input score unchanged
```

原则：

```text
不要一次失败就全局降权。
失败必须绑定 context、usage_mode、task_type、model。
```

---

## 11. 数据库字段建议

本 GUI 文档依赖前一份 Schema V0.1，重点字段如下。

### 11.1 raw_clips

```text
raw_id
local_path
sha256
source_type
rights_status
duration_sec
width
height
fps
has_audio
poster_path
contact_sheet_path
import_status
```

### 11.2 ref_segments

```text
ref_id
raw_id
start_time
end_time
duration
title
primary_ref_type
status
usage_class
active_input_allowed
offline_grammar_only
prompt_influence_allowed
review_standard_only
do_not_use
primary_learning
prompt_words_zh
prompt_words_en
reference_duty
do_not_copy
review_criteria
post_plan
edit_timeline_note
risk_tags
quality_score
query_text
```

### 11.3 tags / segment_tags

```text
tag_id
tag_key
zh_name
en_name
category
parent_tag_key
level
aliases
use_for_exact_filter
use_for_fulltext
use_for_semantic
use_for_weighting
```

### 11.4 generation_attempts

```text
attempt_id
project_name
shot_id
context_id
task_type
model_name
model_version
prompt_id
selected_ref_ids
result_status
visual_score
success_type
failure_type
human_note
created_at
```

### 11.5 feedback_events

```text
feedback_id
attempt_id
ref_id
context_id
usage_mode
outcome_class
success_scope
failure_scope
failure_mode
severity
human_confidence
would_reuse
note
created_at
```

---

## 12. GUI 与 SQLite / FTS5 / 向量搜索集成方式

### 12.1 第一版：SQLite + FTS5

```text
ref_segments = canonical data
ref_segments_fts = searchable text
views = search cards / prompt ready / active candidates
facets = normal indexed columns
```

搜索流程：

```text
user query
→ FTS5 MATCH
→ structured facet filter
→ ranking formula
→ result buckets
→ card display
```

### 12.2 二期：embedding / vector search

可选方案：

```text
sqlite-vec
FAISS
Qdrant local
```

二期流程：

```text
user query
→ FTS5 candidates
→ vector candidates
→ RRF / weighted fusion
→ context-aware rerank
→ diversity rerank
```

### 12.3 为什么不第一版就上向量 DB

```text
3k–4k 条规模不需要。
标签质量和 usage feedback 比 vector DB 更关键。
FTS5 + facets 已经足够第一版生产。
embedding 可以后加，不应阻塞 MVP。
```

---

## 13. 本地文件夹结构建议

```text
reference_library/
  import_inbox/
  raw_clips/
    RAW_000001.mp4
  ref_segments/
    REF_ACT_000001_guard_clash_skid.mp4
  proxies/
    muted/
    blurred/
  thumbs/
    REF_ACT_000001.jpg
  contact_sheets/
    RAW_000001_sheet.jpg
  frames/
    REF_ACT_000001/
      frame_00.jpg
      frame_01.jpg
  notes/
    REF_ACT_000001.md
  db/
    refs.sqlite
    backups/
  exports/
    refs_export.csv
    prompt_ready_refs.csv
    active_safe_refs.csv
  logs/
    ingest.log
    search.log
    feedback.log
```

规则：

```text
原始视频不进 Git。
ref_segments 视频默认不进 Git。
SQLite / CSV / SQL / 标签字典 / 文档可进入 text repo。
thumbs 是否进 Git 由你决定，默认不进。
重要备份另存本地 / 外置硬盘 / 私有同步盘。
```

---

## 14. 最小可落地版本

### 14.1 MVP 功能

```text
1. 扫描本地视频文件夹
2. ffprobe 导入 metadata
3. ffmpeg 生成 poster / contact sheet
4. SQLite 存 raw_clips / ref_segments
5. FTS5 搜索 ref_segments
6. 人工创建 segment
7. 人工粗标 L1/L2
8. 搜索结果卡片显示
9. 一键复制 prompt_words / reference_duty / do_not_copy / review_criteria
10. 记录 attempt 和 success/failure
11. 导出 CSV
12. 本地备份 DB
```

### 14.2 MVP 不做

```text
不做云同步
不做多人权限
不做自动 submit
不做 Dreamina 集成
不做完整视频播放器剪辑器
不做复杂 AI 自动 caption
不做全自动版权判断
不做 learned recommender
不做完整向量搜索
```

### 14.3 MVP 成功标准

```text
能导入 3000–4000 条视频
能按标签和关键词快速搜到参考
能预览缩略图 / contact sheet
能把高价值片段标成 prompt_ready
能导出 reference duty
能记录使用成败
能避免 active input 误用
```

---

## 15. 未来扩展路线

### 15.1 Phase 1：本地索引器

```text
CLI + SQLite
no GUI or minimal GUI
```

### 15.2 Phase 2：PySide6 Workbench

```text
视频预览
搜索卡片
批量标注
reference duty export
attempt recorder
```

### 15.3 Phase 3：自动标注增强

```text
OCR
ASR
face / logo / watermark flags
OpenCLIP embeddings
semantic search
```

### 15.4 Phase 4：推荐排序增强

```text
context-aware ranking
Bayesian success rate
diversity reranking
exploration / exploitation
```

### 15.5 Phase 5：Production Cockpit 集成

```text
Reference Search
→ Prompt Compiler
→ Package Builder
→ Review Recorder
→ Failure Ledger
```

### 15.6 Phase 6：Tauri / React 或 Web cockpit

当系统稳定后再考虑：

```text
更现代 UI
多面板
跨设备浏览
本地服务
多用户只读协作
```

---

## 16. 哪些功能第一版不要做

```text
不要做完整 NLE 时间线。
不要做自动剪辑成片。
不要做自动上传生成平台。
不要做自动选择参考并 live submit。
不要做全自动法律判断。
不要做复杂用户权限。
不要做云端同步。
不要做 vector DB 集群。
不要做完整 AI agent 闭环。
不要把参考视频放进 Git。
不要把第三方参考视频直接标为 active safe。
```

---

## 17. 3000–4000 条库的最佳实践

```text
1. 先导入全量 raw_clip metadata。
2. 先粗标，不要全量深标。
3. 每条初标 5–12 个标签即可。
4. 高价值片段再做 L3 深标。
5. 搜索单位必须是 ref_segment。
6. 每次生成最多选 1–3 条参考。
7. 外部素材默认 offline grammar only。
8. prompt_ready 是稀缺状态，不要滥用。
9. success/failure 必须记录 context。
10. 每月导出一次 CSV 备份。
```

---

## 18. 5万–10万条库的升级建议

当规模扩大后：

```text
1. 保留 SQLite 作为权威 metadata store。
2. FTS5 继续负责可解释全文搜索。
3. 增加 embedding index：sqlite-vec / FAISS / Qdrant local。
4. 增加 background workers。
5. 增加 preview cache 管理。
6. 增加 dedup / near-duplicate detection。
7. 增加 saved search 和 bulk review queue。
8. 增加 tag merge / alias management。
9. 增加 ranking evaluation set。
10. 仍然不把原始视频放进 Git。
```

不建议直接跳到：

```text
Elasticsearch cluster
cloud DAM
复杂 ML recommender
多人 SaaS
```

除非工作流已经明确需要。

---

## 19. 与 Prompt Compiler / Review Recorder / Failure Ledger 对接

### 19.1 Prompt Compiler 输入

Workbench 导出：

```text
selected_ref_ids
reference_duty_block
prompt_words_block
do_not_copy_block
review_criteria_block
post_plan_block
```

Prompt Compiler 负责：

```text
把 reference duty 放在 P1 / P2 合理位置
把 P0 可见结果放在首句
避免参考职责抢主视觉目标
避免负面词淹没正向动作
```

### 19.2 Review Recorder 输入

生成后回填：

```text
attempt_id
result_status
visual_score
success_type
failure_type
human_note
clip_time_window
usable_as_reference
```

### 19.3 Failure Ledger 输入

失败时写入：

```text
which refs were selected
which duty failed
which context failed
which risk occurred
next action
```

### 19.4 Reference Stats 更新

系统更新：

```text
global_score
context_score
task_type_score
model_score
active_input_score
prompt_only_score
review_standard_score
```

---

## 20. AI Agent 自动化边界

### 20.1 适合自动化

```text
扫描文件夹
读取 ffprobe metadata
生成 thumbnails
生成 contact sheets
PySceneDetect 候选切分
OCR / ASR / face_present / watermark_present 初筛
从文件名生成初始标签
重建 FTS
导出 CSV
生成备份
生成报告
```

### 20.2 必须人工确认

```text
active_input_allowed
rights_status 升级
prompt_ready
reference_duty
do_not_copy
success / failure
final quality score
高风险 IP / actor face / logo / UI 判断
是否加入 active-safe 白名单
```

### 20.3 禁止自动化越界

```text
不得自动上传参考视频到生成平台。
不得自动把第三方素材设为 active input。
不得自动修改 official Source。
不得自动 final / lock。
不得自动 live submit。
```

---

## 21. 推荐开发顺序

```text
1. 固定目录结构
2. 固定 SQLite schema
3. 写 import_refs.py
4. 写 thumb/contact sheet 生成器
5. 写 refsearch CLI
6. 写粗标 CSV / GUI 表格
7. 写 PySide6 最小工作台
8. 加 Reference Detail 和 Copy buttons
9. 加 Attempt Recorder
10. 加 feedback stats
11. 再加 OCR/ASR/OpenCLIP
12. 再考虑 Tauri/React 或更大 GUI
```

---

## 22. Final Verdict

```text
MIMIC_REFERENCE_LIBRARY_GUI_AND_ANNOTATION_WORKFLOW_V0_1_READY_AS_DRAFT
```

本文件建议作为：

```text
AI视频制作_模仿参考库总体设计_V0.1.md 的配套执行规范
02 标签字典
03 SQLite Schema
04 ReferenceDuty 与安全规则
之后的第五份落地文件
```

正式应用仍需人类确认。Codex / automation 只能读，不得自动把本文件写入 official Source。
