# Seedance 2.0 AI 视频制作综合使用手册 V0.3｜三层描述增强版

> 项目：AI 视频制作  
> 适用范围：即梦 / Seedance 2.0 多模态视频生成、分镜制作、AI 短片生产、后期剪辑与迭代复盘。  
> 版本：V0.3  
> 更新依据：V0.2 手册、用户融合版资料、《修月人》项目真实制作反馈，以及新增「三层描述 / Composition Matrix 构图矩阵」方法。  
> 说明：本文件是通用工作流 Source。具体项目里，如果本文件与项目实测规则冲突，以项目实测规则为准。

---

# 0. 核心结论

Seedance 2.0 不应被当作“一句话生成完整视频”的工具，而应被当作一个“多模态导演工具”。

正确工作流不是：

```text
一句 prompt -> 直接成片
```

而是：

```text
故事 -> 风格板 -> 角色/场景/道具板 -> 分镜 -> 镜头清单 -> 构图矩阵 -> 关键帧 -> 多模态参考 -> Seedance 片段生成 -> 剪辑合成 -> 反馈复盘 -> 更新规则库
```

核心原则：

```text
1. 先当导演，再当 prompt 工程师。
2. 先设计镜头，再生成视频。
3. 图片负责锁定画面变量，视频 prompt 负责运动、镜头和时间变化。
4. 每个短镜头只承担一个主要叙事功能。
5. 一个镜头优先只有一个主体动作、一个主要运镜、一个情绪目标。
6. 复杂动作、复杂运镜、复杂转场优先用参考视频或拆镜头，而不是纯文字硬写。
7. 生成结果最终靠剪辑完成，不要强迫模型一次解决全部问题。
8. 复杂构图先用「三层描述」结构化，再翻译成自然语言 prompt。
```

---

# 1. 模式选择

## 1.1 文生视频

适合：

```text
探索概念
不追求角色连续性
测试世界观氛围
生成意象镜头
```

不适合：

```text
需要同一角色连续出镜
需要道具严格一致
需要人物站位和视线严格控制
```

## 1.2 图生视频 / 首帧视频

适合：

```text
首帧构图已经确定
只需要让静态图轻微动起来
需要保持构图、主体、光影稳定
```

常用场景：

```text
空镜头
道具特写
人物轻微动作
慢推近 / 慢拉远
环境雾气、风、光线轻微变化
```

## 1.3 首尾帧视频

适合：

```text
动作起点和终点都必须稳定
人物从卧姿到坐姿
门打开前后
手从未触碰到触碰道具
抽象转场前后画面必须准确
```

注意：

```text
首帧和尾帧差距不要过大；
差距过大会导致中间跳变、溶解、主体错位。
```

## 1.4 全能参考 / Reference-to-video

适合：

```text
需要保持人物身份
需要保持道具形状
需要参考场景结构
需要动作或运镜参考
```

参考图数量建议：

```text
1–3 张最稳；
超过 3 张时必须明确每张职责；
不要为了“更稳”无脑上传很多图。
```

---

# 2. Reference Pack 职责规则

每个参考素材必须有明确职责。

不要写：

```text
参考这些图片。
```

要写：

```text
@图片1 作为主体角色参考，保持脸型、服装和身形。
@图片2 作为场景结构参考，不让其中人物出镜。
@图片3 只参考色调和材质，不复制具体构图。
@视频1 参考运镜节奏，不复制人物和场景。
@音频1 作为背景音乐节奏参考。
```

## 2.1 出镜规则

```text
出镜 = 参考素材中的主体实际进入最终画面。
```

示例：

```text
@图片1 中的郑洵作为主体出镜。
@图片2 只作为月下空地背景参考，不让其中人物出镜。
@图片3 只参考色调和画风，不复制其中角色或场景。
```

---

# 3. 资产生产体系

## 3.1 资产层级

```text
A     原子资产 / 完全独立资产
L     轻依赖资产
C     复合资产 / 锚帧
HC    上位复合资产
CTRL  控制资源
SHOT  镜头资源
```

## 3.2 资产生产顺序

```text
Phase 1：A 原子资产
Phase 2：L 轻依赖资产
Phase 3：C / HC 复合与锚帧
Phase 4：CTRL 控制资源
Phase 5：SHOT 镜头关键帧和视频
```

## 3.3 白底规则

```text
A-CH 独立人物资产：纯白背景
A-PROP 独立物品资产：纯白背景
A-SC 独立环境资产：不使用纯白背景，保留完整空场环境
A-STYLE 风格资产：不强制纯白背景
L / C / HC：根据用途进入真实场景
```

## 3.4 细节主体独立建模

除非只是意象图，否则重要细节主体尽量独立生成：

```text
角色
物品
工具
动物 / 工役
群体角色
可复用动作
特殊手部
特殊道具
```

## 3.5 角色基础资产建议

普通重要角色：

```text
主参考
三视图 + 正面头像四联图
典型动作图
必要表情图
```

神秘角色：

```text
限制视角视觉基准
背影
侧背
半遮面
手部
衣袖
不做完整正脸三视图
```

---

# 4. Prompt 写法总规则

## 4.1 图片 Prompt

图片 prompt 用来锁定：

```text
构图
人物身份
服装
场景
道具
光影
风格
比例
```

模板：

```text
资源ID_中文名。画面中不要出现任何文字、编号或标识。
【主体 / 场景 / 道具】，
【景别】，【机位】，【构图】，
【主体特征】，
【环境元素】，
【光源和色彩】，
【材质细节】，
【情绪】，
【比例】。
```

## 4.2 视频 Prompt

视频 prompt 用来锁定：

```text
起始状态
终止状态
时间线
主体动作
环境动作
运镜
视线
站位
光源稳定
禁止变化
```

模板：

```text
@首帧 作为起始画面。保持首帧中的【主体、服装、场景、构图、光影、风格】不变。

机位：
站位：
视线：
运动路径：
锁定元素：
光线：

0-2秒：……
2-5秒：……

镜头：
限制：
```

## 4.3 Prompt 应该更像镜头调度表

在视频阶段，不能只写“人物进入场景”“白衣人坐起”。  
必须写清：

```text
摄影机在哪里
谁在前景
谁在中景
谁在背景
人物从哪里进
停在哪里
看向哪里
哪些主体从第一帧就已经存在
哪些主体不能突然出现
```

## 4.4 复杂构图先写 Composition Matrix

如果一个镜头涉及多人、多道具、固定结构物、前景遮挡、远处目标、空间路径或复杂视线关系，不要直接写长 prompt。先写 Composition Matrix，再将其翻译成自然语言。

```text
Composition Matrix 负责：位置、大小、层级、朝向、视线、运动路径、锁定元素。
Prompt Translation 负责：把矩阵翻译成模型可理解的自然语言镜头调度。
```

---

# 5. 镜头调度六要素

每个视频镜头必须检查六项：

```text
1. Camera position：摄影机位置
2. Framing：前景 / 中景 / 背景
3. Blocking：人物站位
4. Eyeline：视线方向
5. Movement path：运动路径
6. Locked elements：锁定元素
```

示例：

```text
摄影机：在郑洵和王晦身后偏左，侧后方中景。
前景：郑洵、王晦从同一条草径进入。
中景：黑石与卧着的白衣修月人。
视线：两人的头部、胸口、脚尖都朝向黑石与白衣人。
运动路径：从画面左下方进入，停在空地边缘。
锁定元素：黑石和白衣人从第一帧开始已存在，不得突然出现。
```

---

# 6. Composition Matrix：三层描述与构图矩阵

## 6.1 为什么增加这一层

Composition Matrix 是我们在现有工作流中新加入的“构图中间层”。它不直接替代 prompt，也不直接要求 Seedance 理解数学坐标；它的作用是先把导演脑中的画面布局结构化，再翻译成模型更容易理解的自然语言。

原有流程是：

```text
故事 -> storyboard -> shot list -> keyframe prompt -> video prompt
```

V0.3 起，复杂镜头建议改为：

```text
故事 -> storyboard -> shot list -> Composition Matrix -> keyframe prompt -> video prompt
```

它主要解决：

```text
人物位置漂移
道具位置变化
主体大小忽大忽小
前景 / 中景 / 背景混乱
人物朝向不对
视线方向不对
运动路径不清
固定结构物漂浮或复制
镜头切换后空间关系断裂
```

适合使用 Composition Matrix 的镜头：

```text
多人站位
人物看向某个目标
前景人物 + 中景目标 + 背景结构
球场 / 舞台 / 擂台 / 房间 / 道路
产品广告构图
赛博屏幕空间
科幻舱室布局
一镜到底路径规划
首尾帧衔接
道具与人物手部关系
```

不必使用的镜头：

```text
纯风格图
抽象意象图
单个道具特写
单人头像
简单空镜
```

## 6.2 三层描述定义

“三层描述”不是把坐标直接塞给模型，而是分三步：

```text
Layer 1：Composition Matrix / 构图矩阵
Layer 2：Orientation & Pose / 方向、姿态、视线描述
Layer 3：Prompt Translation / 自然语言镜头调度翻译
```

### Layer 1：构图矩阵

用内部坐标描述：

```text
主体在画面哪里
占画面多大
属于前景 / 中景 / 背景
是否完整可见
是否被遮挡
与其他主体的相对位置
```

### Layer 2：方向姿态

描述：

```text
身体朝向
脸部朝向
视线目标
动作起点
动作终点
手部和道具关系
运动路径
```

### Layer 3：Prompt 翻译

把前两层翻译成 Seedance 更容易理解的自然语言：

```text
主角位于画面左下前景，占画面高度约三分之一，三分之二侧背面向远端右侧球门，肩膀、胸口、鼻尖和目光都朝向球门。
```

不要直接写：

```text
主角 bbox: [5,45,35,100]
```

坐标是内部规划语言，最终进入模型的必须是自然语言镜头调度。

## 6.3 坐标系统

Composition Matrix 使用屏幕坐标系，不使用数学笛卡尔坐标系。

```text
左上角 = (0, 0)
右上角 = (100, 0)
左下角 = (0, 100)
右下角 = (100, 100)
画面中心 = (50, 50)
```

规则：

```text
x 越大，越靠右。
y 越大，越靠下。
所有坐标都是画面百分比，不是像素。
```

这套坐标只用于我们内部构图规划。模型 prompt 里要翻译成：

```text
画面左上方
画面右下角
画面中央偏下
画面上方背景
画面左下前景
占画面宽度约三分之一
占画面高度约二分之一
```

## 6.4 bbox 基础格式

矩形区域用：

```text
bbox: [x1, y1, x2, y2]
```

含义：

```text
x1 = 左边界
 y1 = 上边界
x2 = 右边界
y2 = 下边界
```

示例：

```yaml
角色A:
  bbox: [35, 20, 65, 90]
```

翻译为：

```text
角色A位于画面中央，占据画面高度约七成，从画面上方约20%的位置延伸到下方约90%的位置。
```

左下角前景人物：

```yaml
角色A:
  bbox: [5, 45, 35, 100]
```

翻译为：

```text
角色A位于画面左下角前景，占据画面左侧约三分之一，从画面中部延伸到画面底部。
```

右上背景屏幕：

```yaml
屏幕B:
  bbox: [55, 8, 95, 35]
```

翻译为：

```text
屏幕B位于画面右上方背景，占画面宽度约四成。
```

## 6.5 anchor：关键锚点

bbox 只能说明主体大概范围。人物、道具和固定结构物还需要锚点。

人物建议锚点：

```yaml
anchor:
  head: [50, 24]
  chest: [50, 43]
  feet: [50, 92]
  right_hand: [58, 55]
  left_hand: [42, 55]
```

用途：

```text
确定头部位置
确定脚落点
确定手和道具关系
确定视线起点
确定运动路径
```

道具建议锚点：

```yaml
anchor:
  center: [64, 60]
  handle: [60, 52]
  bottom: [64, 68]
```

固定结构物建议锚点：

```yaml
anchor:
  base_left: [42, 88]
  base_right: [58, 88]
  top_center: [50, 35]
```

## 6.6 layer：前景 / 中景 / 背景

二维坐标不能表达纵深，所以必须加 layer。

```yaml
layer: foreground / midground / background
```

建议：

```text
前景 foreground：贴近镜头的人物、遮挡物、手部、道具。
中景 midground：主要行动区域、人物互动、关键目标。
背景 background：建筑、屏幕、远山、观众席、天空等。
```

翻译原则：

```text
前景人物位于画面左下角。
中景目标位于画面中央。
背景建筑位于画面上方。
```

## 6.7 orientation：方向、角度、视线

建议字段：

```yaml
orientation:
  body_facing: away_from_camera / camera / screen_left / screen_right / target:B
  head_facing: target:B
  gaze_target: B
  yaw: front / back / profile / three_quarter_front / three_quarter_back
  pitch: level / looking_down / looking_up
```

翻译时不要写生硬角度，优先写自然语言：

```text
背对镜头
三分之二侧背
侧身面向画面右侧
头部转向远处屏幕
目光集中在画面右上方广告屏
肩膀、胸口、鼻尖和目光都朝向目标
```

## 6.8 motion_path：运动路径

用来描述主体从哪里到哪里。

```yaml
motion_path:
  start: [30, 85]
  end: [50, 60]
  direction: toward_background_center
  speed: slow
```

翻译：

```text
主角从画面左下方缓慢进入，沿小路向画面上方中央移动，最后停在中景目标前方几步。
```

常用运动路径：

```text
从画面左下进入 → 停在画面中央
从画面右侧进入 → 走向中景目标
从画面中央偏下 → 向画面深处前行
从背景门口 → 走到前景桌边
从前景手部 → 推近到中景道具
```

## 6.9 locked_elements：锁定元素

每个矩阵都要写哪些不能变。

```yaml
locked_elements:
  - character_identity
  - costume
  - prop_shape
  - screen_position
  - light_direction
  - background_structure
  - motion_direction
```

翻译：

```text
保持人物身份、服装、灯笼形状、远处屏幕位置、光源方向和背景结构不变，不要新增人物，不要改变运动方向。
```

## 6.10 Composition Matrix 最小模板

```yaml
shot_id:
canvas:
  ratio: 9:16
  coordinate_system: screen_percent
  origin: top_left
  safe_area: [5, 5, 95, 95]

camera:
  shot_size:
  angle:
  position:
  movement:
  lens_feel:

layout:
  - id: A
    name:
    type: character / prop / structure / environment
    bbox: [x1, y1, x2, y2]
    layer: foreground / midground / background
    anchor:
      head:
      chest:
      feet:
      hand:
      prop:
    orientation:
      body_facing:
      head_facing:
      gaze_target:
    motion_path:
      start:
      end:
      direction:
    locked_elements:
      -
```

## 6.11 Translation 模板：矩阵转自然语言

把矩阵翻译成 prompt 时，按这个顺序：

```text
画幅与机位
主体位置和大小
前景 / 中景 / 背景分层
身体朝向与视线
道具关系
运动路径
锁定元素
禁止变化
```

模板：

```text
画面为【比例】，摄影机【机位】，【景别】。
【主体A】位于画面【区域】，占画面【比例】，属于【前景/中景/背景】。
【主体A】身体朝向【方向】，头部和目光看向【目标】。
【道具B】位于【主体A】的【部位】附近，保持【形状/材质/光线】不变。
【结构物C】位于画面【区域】背景，从第一帧开始已经存在，完整可见。
运动路径为：【主体A】从【起点】移动到【终点】。
保持【锁定元素】不变，不要【禁止变化】。
```

## 6.12 图片 Prompt 中怎么使用

Composition Matrix 在图片阶段用于锁定：

```text
主体位置
主体大小
画面比例
前中后景
道具位置
构图中心
留白区域
```

图片 prompt 不写坐标，只写翻译结果：

```text
9:16竖屏，中远景，主角位于画面中央偏下，占画面高度约三分之二，背对镜头，脚部接近画面底部；远处门位于画面上方中央背景，占画面宽度约三分之一；左侧保留大量暗色留白。
```

## 6.13 视频 Prompt 中怎么使用

Composition Matrix 在视频阶段用于锁定：

```text
起始位置
运动路径
终止位置
哪些主体不变
哪些主体不能突然出现
人物看向哪里
镜头从哪里到哪里
```

视频 prompt 示例：

```text
保持首帧构图不变。主角从画面中部偏下缓慢向画面上方中央移动，终点仍在小路中央。远处建筑始终位于画面上方中央背景，不移动，不变形。镜头平视后方跟拍，不绕到人物正面。
```

## 6.14 示例一：背后跟拍人物

### Composition Matrix

```yaml
shot_id: BACK-TRACK-01
canvas:
  ratio: 9:16
  coordinate_system: screen_percent
  origin: top_left
camera:
  shot_size: medium_wide
  angle: eye_level
  position: behind_subject
  movement: slow_follow
layout:
  - id: A
    name: 主角
    type: character
    bbox: [36, 18, 64, 94]
    layer: midground
    anchor:
      head: [50, 22]
      chest: [50, 42]
      feet: [50, 94]
      right_hand: [58, 55]
    orientation:
      body_facing: away_from_camera
      head_facing: forward
      gaze_target: road_depth
    motion_path:
      start: [50, 82]
      end: [50, 68]
      direction: toward_background_center
    locked_elements:
      - costume
      - silhouette
      - right_hand_prop
  - id: B
    name: 手提灯
    type: prop
    bbox: [58, 48, 70, 68]
    layer: midground
    attached_to: A.right_hand
    orientation:
      hanging: vertical
    locked_elements:
      - shape
      - warm_light
  - id: C
    name: 小路
    type: environment
    bbox: [25, 45, 75, 100]
    layer: background_to_foreground
    perspective: converges_to_top_center
    locked_elements:
      - path_direction
      - fog_density
```

### Prompt Translation

```text
画面为9:16竖屏，中远景，摄影机位于主角身后平视跟拍。主角位于画面中央偏下，占据画面高度约四分之三，背对镜头，身体朝向画面深处的小路。右手提着旧手提灯，手提灯位于人物右侧腰部附近，保持竖直悬挂并轻微摇晃。小路从画面下方中央延伸到画面上方中央，透视方向稳定。主角从画面中部偏下缓慢向画面深处前行。保持人物服装、背影轮廓、手提灯形状和小路方向不变，不要绕到人物正面，不要新增人物。
```

## 6.15 示例二：赛博屏幕构图

### Composition Matrix

```yaml
shot_id: CYBER-SCREEN-01
canvas:
  ratio: 9:16
camera:
  shot_size: medium_wide
  angle: low_eye_level
  position: behind_left_of_subject
  movement: slow_push_in
layout:
  - id: A
    name: 女侦探
    type: character
    bbox: [5, 30, 38, 98]
    layer: foreground
    orientation:
      body_facing: three_quarter_back
      gaze_target: B
    locked_elements:
      - black_coat
      - red_mechanical_eye
      - wet_hair
  - id: B
    name: 全息广告屏
    type: structure
    bbox: [48, 8, 95, 45]
    layer: background
    orientation:
      surface: facing_camera
    locked_elements:
      - screen_position
      - neon_blue_pink_light
  - id: C
    name: 街道反光
    type: environment
    bbox: [0, 55, 100, 100]
    layer: foreground_to_midground
    locked_elements:
      - wet_ground
      - neon_reflection
```

### Prompt Translation

```text
9:16竖屏，赛博朋克雨夜街巷，中远景，低平视机位缓慢推近。女侦探位于画面左下前景，占画面高度约三分之二，三分之二侧背面向远处广告屏，黑色长风衣、湿发、红色机械义眼保持不变。全息广告屏位于画面右上背景，占画面宽度约一半，屏幕正对镜头，发出蓝粉霓虹光。湿漉漉的街道路面占据画面下半部分，反射广告屏霓虹。女侦探的头部和视线都看向右上方广告屏。不要让女侦探正面对镜头，不要移动广告屏位置，不要新增人物。
```

## 6.16 示例三：场地结构物构图

### Composition Matrix

```yaml
shot_id: FIELD-STRUCTURE-01
canvas:
  ratio: 16:9
camera:
  shot_size: wide
  angle: eye_level
  position: audience_side
  movement: locked_or_slow_push
layout:
  - id: A
    name: 前景观众
    type: character
    bbox: [3, 45, 28, 100]
    layer: foreground
    orientation:
      body_facing: three_quarter_back
      gaze_target: B
    locked_elements:
      - foreground_position
      - not_on_field
  - id: B
    name: 唯一球门
    type: structure
    bbox: [66, 22, 95, 58]
    layer: midground_background
    anchor:
      left_post: [66, 58]
      right_post: [95, 58]
      crossbar_center: [80, 22]
    locked_elements:
      - single_goal
      - fixed_to_endline
      - full_visibility
  - id: C
    name: 禁区线
    type: field_marking
    bbox: [50, 58, 100, 85]
    layer: midground
    locked_elements:
      - field_geometry
```

### Prompt Translation

```text
16:9横屏，全景，摄影机位于看台一侧。前景观众位于画面左下角，只占画面高度约三分之一，三分之二侧背面向球场，不在草坪上，不遮挡球门。画面中只有一个完整球门，固定在画面右侧远端底线尽头，左门柱、右门柱、横梁和球网全部完整可见。球门前方清楚可见禁区线和小禁区线，球门后方是广告牌和观众席。不要第二个球门，不要让球门漂浮在草坪中段，不要让观众站进草坪。
```

## 6.17 多边形区域：暂不作为默认规则

如果主体区域不是矩形，可以用 polygon：

```yaml
area:
  type: polygon
  points:
    - [50, 0]
    - [100, 100]
    - [0, 50]
```

但 V0.3 阶段不建议默认使用 polygon。原因：

```text
1. 复杂度高；
2. 翻译成自然语言较难；
3. 大多数镜头用 bbox + layer + orientation 已足够；
4. AI 模型不会按精确多边形执行。
```

只有在复杂遮挡、异形屏幕、舞台区块或特殊构图时再使用。

## 6.18 使用边界

Composition Matrix 是构图规划工具，不是像素级控制器。

它追求：

```text
位置关系更清楚
主体大小更稳定
方向和视线更明确
前中后景更有层次
固定结构物更不容易漂移
```

它不保证：

```text
像素级精确位置
100% 不漂移
多主体复杂调度完全成功
复杂几何百分百还原
```

如果一个镜头加了矩阵仍不稳定，优先处理：

```text
缩短时长
减少主体
简化运镜
改用首尾帧
上传参考视频
拆镜头
```

---

# 7. 运镜规则

## 6.1 一个镜头只用一种主要运镜

稳定运镜：

```text
固定镜头
缓慢推近
缓慢拉远
平视跟拍
轻微横移
低角度缓慢推近
```

高风险运镜：

```text
快速摇镜
复杂环绕
一镜到底
主观快速转向
大幅度仰俯切换
同时推、摇、跟、转
```

## 6.2 关键帧视角必须和视频运镜一致

```text
正面关键帧不能要求背后跟拍。
背后跟拍必须先生成背影 / 侧背关键帧。
```

## 6.3 复杂运镜优先参考视频

如果需要复杂动作或镜头语言，应上传参考视频并写明：

```text
@视频1 只参考运镜节奏，不复制人物和场景。
```

---

# 8. 光线规则

## 7.1 光线要写成“光源逻辑”，不要只写“电影感”

更稳的写法：

```text
柔和弥散的夜间环境光
冷白边缘轮廓光
室内暖烛光
窗外冷月反射光
弱逆光勾边
```

高风险写法：

```text
月光照在脸上
一道月光射向人物
光柱照向主体
强烈神圣光芒
```

## 7.2 避免手电筒 / 丁达尔误生成

如果不想出现光柱，明确写：

```text
没有可见光束
没有丁达尔效应
没有手电筒式聚光
没有舞台灯打脸
只保留柔和弥散环境光和淡淡轮廓光
```

---

# 9. 时间线规则

## 8.1 5 秒镜头

```text
0-2秒：建立或起始动作
2-5秒：发现、停顿或反应
```

适合：

```text
插入镜头
轻动作
人物反应
道具特写
环境变化
```

## 8.2 10 秒镜头

```text
0-5秒：进入 / 建立
5-10秒：发现 / 变化 / 收束
```

注意：

```text
10 秒镜头可以省次数，但更难控制。
角色复杂、动作复杂、站位复杂时，宁愿拆成两个 5 秒。
```

## 8.3 15 秒镜头

仅适合：

```text
多段故事线
广告展示
MV
很稳定的环境镜头
```

复杂剧情不要直接 15 秒硬跑。

---

# 10. Negative Prompt 使用规则

负面提示有用，但不要无脑长串复制。

默认：

```text
先用正向 prompt 生成。
```

如果跑偏，再加 2–4 个最关键负面限制：

```text
不要新增人物
不要改变黑石形状
不要强光束
不要脸部漂移
不要多余手指
不要随机文字
```

对于视频阶段，负面提示重点保护：

```text
人物身份
手部
道具形状
场景结构
光线逻辑
镜头稳定
```

---

# 11. 常见失败与修正

| 问题 | 常见原因 | 修正 |
|---|---|---|
| 人物变脸 | 参考不足、动作复杂、时间过长 | 缩短时长，强化角色参考，减少动作 |
| 双人脸融合 | 双人正面过近、站位不清 | 改背后/侧后方，拉开距离，明确左右站位 |
| 主体突然出现 | 起始状态没锁 | 写“从第一帧开始已经存在” |
| 人物不看目标 | 没写 eyeline | 写头部、胸口、脚尖都朝向目标 |
| 物体变形 | 运镜激进或描述抽象 | 使用道具参考，放慢运镜，写形状不变 |
| 光像手电 | 写了光束/照脸 | 改为柔和弥散环境光，无可见光束 |
| 月相乱变 | 写“裂痕”或“破裂” | 改为边缘暗色小缺口，固定不动 |
| 场景像平行路过 | 缺 blocking | 写入口、终点、面向关系 |
| 参考图被忽略 | 未写 @ 职责 | 每张参考图都写“作为……参考” |
| 审核/版权受限 | 图片元数据/体积/相似度误判 | 先 WPS 轻微压缩，再转 JPG/裁切/换图 |

---

# 12. 文件与素材管理

## 11.1 命名令牌

图片 prompt 第一行建议加入：

```text
资源ID。画面中不要出现任何文字、编号或标识。
```

或：

```text
SHOT-08_月影节点初见关键帧。画面中不要出现任何文字、编号或标识。
```

这样下载文件名里有 ID，便于批量改名。

## 11.2 多版本不要急删

生成时可以保留：

```text
v01
v02
v03
```

但后续要建立：

```text
00_locked_refs
```

只把每个资源最终采用的主版本复制进去。

## 11.3 图片异常处理

如果参考图上传或生成时报错：

```text
1. 先用 WPS 轻微压缩画质；
2. 再尝试上传；
3. 仍不行再 PNG 转 JPG / 改尺寸 / 裁切；
4. 最后才换图。
```

---

# 13. 反馈迭代格式

以后每次反馈最好按这个格式：

```text
项目：
镜头编号：
使用素材：
图片 prompt：
视频 prompt：
生成时长：
生成结果：
问题：
满意部分：
不满意部分：
我猜原因：
截图/视频描述：
下一步想改什么：
```

我会整理成：

```text
稳定规则：以后继续用
风险规则：遇到要小心
禁止规则：以后尽量不用
```

---

# 14. 生成前检查清单

每次生成前检查：

```text
这个镜头的功能是什么？
这个镜头的时长是多少？
关键帧视角和视频运镜一致吗？
主体是谁？
谁出镜？
谁不出镜？
摄影机在哪里？
前景 / 中景 / 背景分别是什么？
人物从哪里来？
人物停在哪里？
人物看向哪里？
哪张图是角色参考？
哪张图是背景参考？
哪张图是风格参考？
有没有写清楚 @素材用途？
有没有只保留一个主要动作？
有没有只保留一个主要运镜？
有没有锁定光源？
有没有锁定不能变化的主体？
是否需要 Composition Matrix？
主体 bbox 是否清楚？
前景 / 中景 / 背景 layer 是否清楚？
人物 orientation 和 gaze_target 是否清楚？
motion_path 是否清楚？
坐标是否已经翻译成自然语言，而不是直接塞给模型？
这个镜头如何接上一个？
这个镜头如何接下一个？
```

答不上来，就先不要生成。

---

# 15. 一句话总结

```text
用资产锁定变量，用镜头调度控制关系，用短片段验证动作，用剪辑完成叙事，用复盘更新规则。
```
