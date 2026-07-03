# AI视频制作_模仿参考库ReferenceDuty与安全规则_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE
> 类型：模仿参考库规则草案 / Source 候选 / 执行规范候选
> 版本：V0.1 Draft
> 生成日期：2026-07-03
> 生成方：ChatGPT
> 适用范围：AI 视频模仿参考库、动作/运镜/FX/剪辑/表演/构图/风格/声音参考片段、SQLite + FTS5 本地检索、Prompt Compiler、Reference Duty Planner、Review Recorder、Failure Ledger。
> 重要说明：本文件不是法律意见，不替代律师审查；本文件也不是 official Source。进入 Project Source 或本地 `sources/` 前，需由用户人工确认并手动应用。Codex / automation 不得直接修改 official Source。

---

## 0. 一句话结论

```text
模仿参考库里的外部视频默认不是素材，不是最终资产，也不是默认 active input。
每条参考必须先写清：只学什么，不学什么，能不能上传模型，失败/成功后如何记录。
```

本文件的核心目标是把参考片段从“看起来像某个视频”转成：

```text
可检索的模仿语法
+ 可复制的 Reference Duty
+ 可执行的 do_not_copy
+ 可审计的 active_input 安全边界
+ 可反馈更新的使用结果
```

---

## 1. 本文件定位

本文件承接六轮 Deep Research：

```text
1. AI Video Mimic Reference Library Tag System
2. Local Video Reference Library Automatic Annotation and Multimodal Retrieval Plan
3. Safety Boundaries for an AI Video Mimic Reference Library
4. AI Video Reference Library Feedback Ranking and Context-Aware Recommendation Research
5. AI 视频模仿参考库的 AE / PR / 后期特效分类体系研究
6. Local-First Workbench for an AI Video Mimic Reference Library
```

本文件不重复标签字典和 SQLite schema 的完整内容，只规定：

```text
usage_class 怎么判定
active_input_allowed 什么时候可以 true
reference_duty 怎么写
do_not_copy 怎么写
risk_tags 怎么用
搜索结果如何按安全模式过滤
Prompt Compiler 怎么吸收参考
Review Recorder 怎么记录成败
```

---

## 2. 核心术语

### 2.1 raw_clip

```text
raw_clip = 原始找到或导入的视频文件。
```

例：

```text
一段 18 秒影视动作片段
一段 AE 教程中的 impact flash 示例
一段游戏过场中的 boss skill cast
一段自录动捕滑步
```

raw_clip 不是最终检索单位，只是来源文件。

---

### 2.2 ref_segment

```text
ref_segment = 从 raw_clip 中切出的、真正有模仿价值的短窗口。
```

例如：

```text
RAW_000321.mp4
→ REF_ACT_000321_01_crossed_guard_skid_4s.mp4
→ REF_CAM_000321_02_low_angle_push_stop_5s.mp4
→ REF_FX_000321_03_white_flash_shake_2s.mp4
```

后续搜索、标注、反馈、reference duty 都应优先绑定到 ref_segment，而不是只绑定到 raw_clip。

---

### 2.3 Reference Duty

```text
Reference Duty = 明确说明这条参考只负责什么。
```

它回答：

```text
这条参考是学动作、运镜、特效、剪辑、表演、构图、环境反馈、风格，还是声音节奏？
模型 / 人类 / 后期到底应该从它身上学什么？
哪些内容不能复制？
```

---

### 2.4 do_not_copy

```text
do_not_copy = 禁止复制项。
```

它回答：

```text
不要复制人物身份、脸、服装、场景、剧情、UI、logo、水印、字幕、音乐、台词、IP 符号、镜头背景。
```

---

### 2.5 usage_class

每条 ref_segment 至少有一个主 usage_class：

```text
offline_grammar_only
prompt_influence_allowed
review_standard_only
active_input_allowed
do_not_use
```

可以多状态并存，但 active_input_allowed 必须独立审查。

---

## 3. Usage Class 五级定义

| usage_class | 中文 | 含义 | 默认对象 |
|---|---|---|---|
| `offline_grammar_only` | 仅离线语法 | 只能本地观察、拆动作/运镜/特效/剪辑结构，不上传模型 | 外部影视、动漫、游戏、教程、广告、社交短视频 |
| `prompt_influence_allowed` | 可转 prompt 语言 | 可把参考抽象成 prompt words / 动作词 / 运镜词 / FX 词 | 去 IP 化后的通用动作、镜头、效果语言 |
| `review_standard_only` | 仅审片标准 | 不用于生成，只用于判断生成结果是否达标 | 版权高风险但动作/特效结构有价值的片段 |
| `active_input_allowed` | 可主动输入 | 可上传给 AI 视频模型作为参考输入 | 自录、授权、灰盒、无 IP/脸/品牌/水印/字幕的干净参考 |
| `do_not_use` | 禁用 | 不建议进入任何流程，或仅保留隔离记录 | 泄露、盗录、隐私、未成年人、明显禁用来源、强风险素材 |

默认导入规则：

```text
所有新导入视频：
active_input_allowed = false
offline_grammar_only = true
prompt_influence_allowed = false until reviewed
review_standard_only = false until reviewed
do_not_use = false unless risk detected
human_review_required = true for active input
```

---

## 4. 来源类型默认安全边界

| source_type | 默认 usage_class | prompt influence | review standard | active input | 备注 |
|---|---|---:|---:|---:|---|
| `self_shot` 自录 | prompt / review / active 候选 | 是 | 是 | 可候选 | 仍需检查人脸、logo、隐私、音乐 |
| `inhouse_mocap` 内部动捕 | prompt / review / active 候选 | 是 | 是 | 可候选 | 最推荐动作 active input 来源 |
| `graybox_blender_unreal` 灰盒 | prompt / review / active 候选 | 是 | 是 | 可候选 | 最推荐运镜 / 空间参考来源 |
| `licensed_stock` 授权素材 | 视 license | 是 | 是 | 需人工确认 | 必须确认授权覆盖 AI reference use |
| `licensed_mocap` 授权动捕 | 视 license | 是 | 是 | 需人工确认 | 检查下游用途和 performer rights |
| `film` 电影 | offline grammar | 可抽象 | 是 | 默认否 | 不能复制演员、服装、场景、镜头 |
| `tv` 电视剧 | offline grammar | 可抽象 | 是 | 默认否 | 同上 |
| `anime` 动漫 | offline grammar | 可抽象 | 是 | 默认否 | 注意 IP 角色、风格污染 |
| `animation` 动画 | offline grammar | 可抽象 | 是 | 默认否 | 可学运动规律，不学角色设计 |
| `game_cinematic` 游戏过场 | offline grammar | 可抽象 | 是 | 默认否 | 注意角色/IP/UI/HUD/技能名 |
| `gameplay` 游戏实机 | offline grammar | 可抽象 | 是 | 默认否 | 注意 HUD、logo、UI、角色 IP |
| `ae_pr_tutorial` AE/PR 教程 | offline grammar / post plan | 可抽象 | 是 | 默认否 | 带 UI、水印、教程 overlay 时不可 active |
| `advertisement` 广告 | offline grammar | 谨慎 | 是 | 默认否 | 品牌、logo、版式、代言人风险高 |
| `mv` MV | offline grammar | 谨慎 | 是 | 默认否 | 音乐、艺人、镜头和造型风险 |
| `social_short` 社交短视频 | offline grammar | 谨慎 | 是 | 默认否 | 来源链与授权通常不清 |
| `unknown` 未知来源 | offline grammar / hold | 否 | 否 | 否 | 需人工确认来源 |

---

## 5. Active Input Allowed 判断表

只有全部 gate 通过，`active_input_allowed` 才能改为 true。

| Gate | 必须满足 | 不满足时 |
|---|---|---|
| Rights Gate | 自有 / 授权 / 委托 / 明确允许模型参考输入 | 保持 `active_input_allowed=false` |
| Provider Terms Gate | 不违反当前模型平台输入条款 | 保持本地离线 |
| Likeness Gate | 无可识别人脸/声音，或已取得明确授权 | 禁 active input |
| Brand/IP Gate | 无 logo、品牌包装、IP 角色、游戏 HUD、UI、水印 | 去除/模糊/禁 active |
| Provenance Gate | 来源明确，无泄露、盗录、未知转载链 | hold 或 do_not_use |
| Audio Gate | 无版权音乐、可识别说话人、原片台词 | 默认去音频或禁 active |
| Text/UI Gate | 无烧录字幕、平台水印、教程 UI、社媒 handle | 去除/裁切/禁 active |
| C2PA / AI Preference Gate | 无 no-AI / no-train / no-reference-use 信号 | 禁 active |
| Human Review Gate | 人工明确标记 active-safe | 未审不得 active |

硬规则：

```text
active_input_allowed=true 不得由机器自动最终决定。
自动工具只能提出 active-safe_candidate。
最终必须 human_review_active_input_passed=true。
```

---

## 6. Risk Grade 分级

| risk_grade | 含义 | 处理 |
|---|---|---|
| R0 Controlled | 自有 / 授权 / 灰盒 / 内部动捕，低风险 | 可进入 active 候选 |
| R1 Licensed Bounded | 有授权但范围需核对 | active 前需人工确认 license |
| R2 Tutorial / Demo | 教程或软件 demo，含 UI/字幕/水印可能高 | 默认 offline / post plan |
| R3 Third-party Expressive | 影视、动漫、游戏、广告、MV 等固定表达内容 | 默认 offline grammar only |
| R4 Restricted / Forbidden | 泄露、盗录、隐私、未成年人、禁用来源、no AI use | do_not_use |

默认映射：

```text
film / tv / anime / game / mv / ad → R3
tutorial / social short / unknown source → R2/R3/R4 depending risk
self_shot / inhouse_mocap / graybox → R0
licensed_stock / licensed_mocap → R1
```

---

## 7. Risk Tags 词表

### 7.1 权利与来源风险

```text
rights_unknown
license_scope_unclear
public_reference_only
contract_restricted
client_approval_required
source_unknown
scraped_social
reupload_suspected
leak_risk
takedown_history
c2pa_no_ai_flag
credentials_invalid
```

### 7.2 人脸 / 声音 / 身份风险

```text
face_present
actor_face
celebrity_face
minor_possible
voice_present
speaker_identifiable
voiceprint_risk
publicity_risk
biometric_processing_risk
```

### 7.3 品牌 / IP / UI 风险

```text
logo_present
trademark_visible
brand_packaging
ui_overlay
hud_present
game_hud
character_ip
franchise_symbol
signature_scene_motif
recognizable_costume
recognizable_weapon_design
```

### 7.4 包装与平台污染

```text
watermark_present
subtitle_burnin
channel_bug
social_handle_overlay
tutorial_cursor_overlay
app_ui_overlay
screen_recording_ui
platform_overlay
```

### 7.5 音频风险

```text
music_present
lyrics_present
dialogue_present
copyrighted_music_risk
voice_likeness_risk
```

### 7.6 生成污染风险

```text
style_pollution
reference_attention_conflict
identity_leak_risk
scene_copy_risk
camera_background_copy_risk
exact_layout_required
exact_text_required
exact_logo_required
exact_cut_timing_required
```

### 7.7 工作流状态风险

```text
human_review_required
active_input_denied
prompt_only_ok
review_only_ok
offline_only
do_not_use
```

---

## 8. Reference Duty 通用结构

每条 prompt-ready ref_segment 必须能生成以下结构：

```text
Reference Duty:
[REF_ID] 只作为【参考类型】参考。
只参考：
- ...
- ...
- ...

不要复制：
- ...
- ...
- ...

允许进入：
- offline grammar / prompt influence / review standard / active input candidate

禁止进入：
- ...
```

最小字段：

```text
reference_label
primary_reference_role
allowed_learning
forbidden_learning
usage_class
risk_tags
active_input_allowed
do_not_copy
```

---

## 9. Reference Duty 模板库

### 9.1 ACTION ONLY

```text
@REF_ID 只作为动作语法参考。
只参考：身体发力路径、接触时机、受力反应、脚步位移、重心转移、反弹续招、动作节奏。
不要复制：人物身份、演员脸、发型、服装、武器设计、场景背景、剧情、原镜头构图、台词、音乐、logo、字幕或水印。
```

适用：

```text
近身格挡
护架压缩
湿地滑步
摔倒
挥刀
闪避
动捕
武术训练
```

---

### 9.2 CAMERA ONLY

```text
@REF_ID 只作为运镜参考。
只参考：镜头高度、移动方向、推进/拉远速度、停顿节奏、手持惯性、环绕角度、加速/减速曲线。
不要复制：人物、服装、场景、光影、道具、剧情、品牌、字幕、UI 或镜头背景内容。
```

适用：

```text
低机位推进
手持微晃
speed ramp push stop
短环绕
穿门廊
跟拍
whip pan
```

---

### 9.3 FX ONLY

```text
@REF_ID 只作为特效语法参考。
只参考：特效起点、扩散方向、持续时间、透明度/亮度变化、粒子密度、震屏起止、闪白帧数、hit-stop 节奏。
不要复制：原视频人物、场景、logo、UI、字幕、品牌包装、角色设计、具体图形版式或原素材帧。
```

适用：

```text
impact flash
white flash
camera shake
shock ripple
particle burst
afterimage
glow trail
mask transition
glitch
```

---

### 9.4 EDITING RHYTHM ONLY

```text
@REF_ID 只作为剪辑节奏参考。
只参考：切点位置、速度变化、hit-stop 时长、慢动作进入点、freeze frame 时机、beat sync 关系。
不要复制：原片镜头顺序、人物、场景、音乐、台词、字幕、logo 或剧情事件。
```

适用：

```text
speed ramp
time remap
smash cut
match cut
jump cut
beat sync
freeze frame
```

---

### 9.5 PERFORMANCE ONLY

```text
@REF_ID 只作为表演/情绪参考。
只参考：眼神变化、呼吸节奏、肩膀紧张、手部动作、身体停顿、情绪递进。
不要复制：演员脸、明星气质、具体表演身份、服装、台词、场景或原剧情。
```

适用：

```text
fear_to_resolve
cold_smile
breath_pause
eye_shift
hand_clench
shock_reaction
hesitation
```

---

### 9.6 COMPOSITION / BLOCKING ONLY

```text
@REF_ID 只作为构图与空间调度参考。
只参考：前景/中景/背景层级、人物远近关系、左右分置、遮挡关系、场地落点、视线轴线。
不要复制：场景美术、建筑设计、人物身份、服装、IP 造型、原镜头背景或剧情。
```

适用：

```text
near_wall_pressure
two_character_close
foreground_obstruction
left_right_standoff
near_far_contrast
doorway_frame
center_axis
```

---

### 9.7 STYLE / LIGHTING ONLY

```text
@REF_ID 只作为风格与光影观察参考。
只参考：主色调、对比度、光源方向、轮廓光、材质质感、雨雾/烟尘氛围。
不要复制：具体角色、场景设计、IP 美术、logo、品牌视觉、构图或原剧情。
```

注意：

```text
第三方影视 / 动漫 / 游戏风格参考通常只能 offline grammar / prompt influence。
不可要求“照着某 IP 风格生成”。
```

---

### 9.8 ENVIRONMENT FEEDBACK ONLY

```text
@REF_ID 只作为环境反馈参考。
只参考：雨水、水花、尘土、烟雾、碎屑、衣摆、发丝、地面反光与动作之间的因果关系。
不要复制：人物、场景、道具、剧情、镜头背景、logo、字幕或原素材帧。
```

适用：

```text
rain_splash
wet_floor_reflection
dust_burst
cloth_flutter
hair_whip
debris_after_impact
```

---

### 9.9 SOUND RHYTHM ONLY

```text
@REF_ID 只作为声音节奏/剪辑卡点参考。
只参考：强弱拍、冲击点、静音点、呼吸停顿、whoosh 节奏、低频进入时间。
不要复制：音乐旋律、歌词、原声、人声、台词、音色、配乐编曲或可识别声音素材。
```

默认：

```text
外部片段音频不作为 active input。
若只是研究画面动作，优先生成 muted proxy。
```

---

## 10. do_not_copy 模板

### 10.1 中文标准版

```text
不要复制：
人物身份、演员脸、明星脸、发型、服装造型、角色设计、武器/道具专有设计、原场景空间、背景布局、建筑设计、品牌标识、logo、游戏 HUD、UI、字幕、水印、社媒账号、台词、旁白、音乐、歌词、剧情事件、原镜头顺序、可识别 IP 视觉符号、原片具体构图。
```

### 10.2 英文标准版

```text
Do not copy:
identity, face, celebrity likeness, hairstyle, wardrobe, character design, proprietary weapon or prop design, original set, background layout, architecture, logos, trademarks, game HUD, UI, subtitles, watermarks, social handles, dialogue, voiceover, music, lyrics, plot beats, original shot order, recognizable IP symbols, or the source shot composition.
```

### 10.3 动作参考短版

```text
只学动作因果，不复制人物、场景、服装、武器设计、剧情、镜头背景。
```

### 10.4 运镜参考短版

```text
只学镜头速度、方向、停顿和惯性，不复制画面内容。
```

### 10.5 FX 参考短版

```text
只学特效时序、扩散路径和层级，不复制原视频图形、logo、UI、字幕或角色。
```

---

## 11. 搜索模式下的安全过滤

### 11.1 Grammar Search

用途：

```text
找动作 / 运镜 / FX / 表演 / 风格语法。
```

过滤策略：

```text
允许显示 R2/R3，但标红。
隐藏 do_not_use。
默认不显示 active unsafe 的上传按钮。
```

排序：

```text
semantic_fit + tag_match + context_success - risk_penalty_light
```

---

### 11.2 Prompt Influence Search

用途：

```text
找可转 prompt words 的参考。
```

过滤策略：

```text
允许 offline_grammar_only，但必须显示 do_not_copy。
剔除 do_not_use。
IP / face / logo / watermark 风险只允许抽象化。
```

排序：

```text
prompt_word_value + tag_match + review_score - style_pollution_penalty
```

---

### 11.3 Active Input Search

用途：

```text
找可以上传给模型的参考视频。
```

硬过滤：

```text
active_input_allowed = true
human_review_active_input_passed = true
do_not_use = false
face_present = false unless consent documented
logo_present = false
watermark_present = false
ui_overlay = false
subtitle_burnin = false
rights_status in self_owned / licensed_active_ok / client_approved
```

排序：

```text
context_success + quality_score + tag_match - minor_risk_penalty
```

---

### 11.4 Review Standard Search

用途：

```text
找审片标准，不作为输入。
```

过滤策略：

```text
允许 R2/R3，只要不是 do_not_use。
突出 review_criteria 和 failure/success 标注。
```

---

### 11.5 Post Plan Search

用途：

```text
找 AE / PR / DaVinci / 剪映后期方案参考。
```

过滤策略：

```text
优先 fx_execution_mode in post_only / generate_plus_post / editing_reference_only。
包含 logo / UI / 字幕的外部教程仍可作为离线 post grammar，但不作为素材。
```

---

## 12. Prompt Compiler 对接规则

### 12.1 搜索结果进入 Prompt Compiler 的方式

搜索结果不得直接变成：

```text
“照着 REF_XXX 做”
“完全参考这个视频”
“生成类似这个片段”
```

必须变成：

```text
Reference Duty Block
Prompt Words
Do Not Copy Block
Visual Review Criteria
Post Plan / Edit Timeline
```

### 12.2 Prompt Compiler 输入结构

```yaml
references:
  - ref_id: REF_ACT_000123
    role: action_reference_only
    active_input_allowed: false
    usage_class: prompt_influence_allowed
    prompt_words:
      - already close from the first frame
      - shoulder-and-forearm pressure
      - crossed guard compression
      - rear foot skid on wet floor
    reference_duty: >
      Only study body force path, guard compression, skid timing, rain feedback.
    do_not_copy: >
      Do not copy identity, faces, costumes, scene, dialogue, music, logo, or shot composition.
```

### 12.3 P0 / P1 / P2 映射

```text
P0：把参考转成可见动作结果 / 时间窗 / 因果链。
P1：放 reference duty，说明每条参考职责。
P2：放 compact do_not_copy 和 negative constraints。
```

禁止：

```text
把大段 reference duty 放在首句，挤掉 P0 主视觉结果。
```

---

## 13. Review Recorder 对接规则

生成后不问：

```text
像不像参考？
```

而问：

```text
动作因果是否和参考一样清楚？
运镜速度/停顿是否达到参考的功能？
特效时序是否达到参考的功能？
环境反馈是否支持受力？
是否出现了 do_not_copy 里的泄漏？
这条参考在本 context 下是 success / partial_success / failure？
```

推荐字段：

```text
attempt_id
ref_id
context_key
usage_mode
result
success_scope
failure_scope
failure_mode
human_note
score_action
score_camera
score_fx
score_edit
score_safety
would_reuse_same_context
would_reuse_other_context
```

---

## 14. Feedback 更新规则

### 14.1 成功

```text
success_count +1
context_score 上升
global_score 小幅上升
```

只有当 active input 使用成功，才更新 active input 成功统计。

### 14.2 部分成功

```text
partial_success_count +1
记录成功 scope 和失败 scope
只提升对应 role，不提升全部能力
```

例：

```text
动作参考有效，但复制了原场景光影 → action_success + style_pollution_failure
```

### 14.3 失败

```text
failure_count +1
只在 strict_context / soft_context 下局部降权
不做全局封杀，除非跨多个 context 重复失败
```

### 14.4 安全失败

```text
active_input_failed
provider_reject
identity_leak
style_pollution
brand_leak
ui_leak
```

安全失败要影响 active input 排名，但不一定影响 offline grammar 价值。

---

## 15. Human Review Gate 表单

### 15.1 Active Input 审核表

```markdown
# Active Input Review

ref_id:
source_type:
source_url_or_origin:
local_path:
duration:
rights_status:
license_notes:
contains_face: true/false
contains_voice: true/false
contains_logo: true/false
contains_ui_or_hud: true/false
contains_watermark: true/false
contains_subtitles: true/false
contains_music_or_dialogue: true/false
ip_or_brand_risk:
c2pa_or_ai_preference:
sanitized_proxy_path:
allowed_usage:
reviewer:
reviewed_at:

Decision:
[ ] active_input_allowed = true
[ ] prompt_influence_allowed only
[ ] review_standard_only
[ ] offline_grammar_only
[ ] do_not_use

Reason:
```

### 15.2 Reference Duty 审核表

```markdown
# Reference Duty Review

ref_id:
primary_role:
allowed_learning:
forbidden_learning:
risk_tags:
do_not_copy:
prompt_words:
review_criteria:
post_plan:
is_duty_clear: true/false
is_duty_too_broad: true/false
needs_rewrite: true/false
```

---

## 16. 数据库字段建议

本文件对应 schema 中的关键字段：

```text
source_type
rights_status
usage_class
active_input_allowed
offline_grammar_only
prompt_influence_allowed
review_standard_only
do_not_use
human_review_required
human_review_active_input_passed
risk_level
risk_tags
reference_role
reference_duty
do_not_copy
prompt_words_zh
prompt_words_en
review_criteria
post_plan
edit_timeline_note
model_generation_risk
provider_input_license_risk
publicity_risk
brand_risk
provenance_status
content_credentials_status
```

建议 GUI 中把这些字段分成四组：

```text
可用方式
风险提示
参考职责
复制导出
```

---

## 17. 文件与 Git 边界

### 17.1 参考视频文件

```text
不要提交到 Git。
不要放进 official Source。
不要放进 locked_refs。
不要当最终素材。
```

可放本地：

```text
reference_library/raw_clips/
reference_library/ref_segments/
reference_library/proxies/
reference_library/thumbs/
reference_library/contact_sheets/
```

### 17.2 可进 Git 的内容

```text
标签字典 CSV
SQLite schema SQL
空库模板
说明文档
导出 manifest
小尺寸缩略图索引（视情况）
```

### 17.3 不进 Git 的内容

```text
原始视频
第三方参考片段
active input 候选媒体
含版权风险的代理视频
含人脸/声音/水印的截图
```

---

## 18. 最小可落地策略

第一版只需要做到：

```text
1. 所有导入片段默认 offline_grammar_only。
2. active_input_allowed 必须人工确认。
3. 搜索结果每条都显示 usage_class 和 risk_tags。
4. 每条 prompt-ready 参考必须有 reference_duty 和 do_not_copy。
5. 一键复制 prompt words / reference duty / review criteria。
6. 使用后记录 success / partial_success / failure。
7. 安全失败和视觉失败分开统计。
```

第一版不要做：

```text
自动法律判断
自动 active input 放行
自动上传模型
自动把外部片段作为 final asset
自动从影视片段生成 active input 包
```

---

## 19. 与既有项目规则关系

本文件继承：

```text
外部案例只作为观察样本，不直接成为项目资产。
多模态素材必须先写职责，不允许“都参考一下”。
动作参考视频是动作语法库，不是最终素材。
Official Source 只能由用户手动应用。
```

本文件新增：

```text
usage_class 五级安全边界
active_input_allowed gate
Reference Duty 模板库
do_not_copy 模板库
风险标签词表
搜索模式安全过滤
Prompt Compiler / Review Recorder 对接规则
```

---

## 20. Final Verdict

```text
REFERENCE_DUTY_AND_SAFETY_RULES_V0_1_READY_AS_DRAFT
```
