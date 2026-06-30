# AI视频制作_动作参考视频库与审片标准_V0.1

版本：V0.1 Draft  
来源：K244S SHOT-04 R02 evidence pack  
状态：Source 草案，需人类手动确认后进入 `sources/`

## 0. 核心规则

```text
动作参考视频 = 动作语法库
不是素材库
不是默认 active generation input
不是最终版权资产
```

动作参考用于：

- 理解动作结构
- 提取时间轴
- 改写 prompt 动词
- 建立审片标准
- 训练人类/模型区分“技术成功”和“动作可用”

## 1. 适合搜索的参考

优先找：

- 两人近身格挡
- 肩膀 / 前臂 / 身体线压进防守方护架
- crossed guard compression
- 防守方湿地滑步
- 雨水 / 水花 / 地面反光反馈
- 靠墙但不撞墙的空间压迫
- 1.0–1.5s 内完成接触、受力、滑步、反击预备
- 尾段保持运动，不 static pose-out

不优先找：

- 撞墙破墙
- gore / 严重伤害
- 魔法爆炸 / 冲击波
- 长距离起跑
- 只帅但动作关系不清的镜头
- 无法截取短窗口的长打斗合集

## 2. 文件命名

推荐：

```text
REF_001_guard_clash_skid_rain.mp4
REF_001_guard_clash_skid_rain.md
```

最小可用包：

```text
REF_001.mp4
REF_001.md
```

不要把参考视频提交进 Git，除非另有授权。

## 3. 标注模板

```markdown
# REF_001 Action Grammar Note

- reference_id: REF_001
- source_url_or_origin:
- rights_status: unknown / public_reference_only / licensed / owned
- active_generation_input_allowed: false
- shot_relevance: SHOT-04 R02 near-wall guard-clash
- action_type:
- environment_features:
- useful_window:
- what_to_learn:
- what_not_to_copy:

## Timeline

| Marker | Note |
|---|---|
| 0.00s | 是否已经近身？是否有长距离起跑？ |
| 0.10s | 第一次压力/接触 cue |
| 0.35s | 主护架压缩 / 肩前臂压力 / 力传递 |
| 0.65s | 滑步 / 雨水 / 地面反馈 / hit-stop |
| 1.00s | 恢复 / 反击预备开始 |
| 1.35s | 最佳剪辑点候选 |
| 1.50s | 有用窗口结束，尾段是否仍在动 |

## Scoring

- action clarity: 1-5
- pressure: 1-5
- wet-floor feedback: 1-5
- edit-window usefulness: 1-5
- similarity to SHOT-04 R02: 1-5

## Prompt influence

## Review influence
```

## 4. 审片表

生成视频后，用下面标准审查：

| 项目 | 失败 | 一般 | 通过 |
|---|---|---|---|
| 第一帧是否已近身 | 远距离起手 | 半近身 | 已经近身 |
| 是否看懂两人在打斗 | 看不懂 | 勉强 | 清楚 |
| 是否有交叉护架 | 无 | 模糊 | 清晰 |
| 是否有压力线 | 无 | 手推 | 肩/前臂/身体线 |
| 是否有湿地滑步 | 无 | 不明显 | 清楚 |
| 是否有雨水反馈 | 无 | 有一点 | 与动作相关 |
| 是否靠墙但不撞墙 | 撞墙/贴墙 | 过近风险 | 近墙无接触 |
| 是否 static pose-out | 是 | 有点 | 否 |
| 是否可剪 1.0–1.5s | 不行 | 勉强 | 可以 |

## 5. 参考如何影响 prompt

把参考转成动作语言，而不是复制镜头。

例如：

```text
already close from first frame
shoulder-and-forearm pressure
crossed guard compression
rear foot skid
rain spray from wet floor
counter-ready twist
cut mid-exchange
```

## 6. 参考如何影响视觉审查

不要问“像不像参考”。  
要问：

- 动作因果是否一样清楚？
- 接触/压力点是否读得懂？
- 受力反馈是否成立？
- 湿地/雨水是否参与动作？
- 是否能剪出同样短的有效窗口？

## 7. 版权和安全

- 参考视频仅作内部动作语法研究。
- 不作为最终素材。
- 不公开传播。
- 不上传生成平台作为 active input，除非权利和安全另行确认。
- 不使用真实伤害、血腥、隐私人物或明显侵权素材作为 active input。

## 8. CTRL 资产关系

动作参考视频可归入 CTRL / action grammar evidence。  
它不等于角色 identity ref，不等于 final shot，不等于可直接喂给模型的媒体输入。

## 9. SHOT-04 R02 当前参考方向

当前优先参考：

```text
near-wall guard clash
shoulder/forearm pressure
crossed guard compression
wet-floor skid
rain spray
counter-readiness
no wall hit
no wall damage
no body-wall contact
```
