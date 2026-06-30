# AI视频制作_Prompt编译器与结果优先动作语法_V0.2

版本：V0.2 Draft  
来源：K244S SHOT-04 R02 evidence pack  
状态：Source 草案，需人类手动确认后进入 `sources/`

## 0. 核心原则

Prompt Compiler 的目标不是“把所有规则写进去”，而是让模型优先执行可见结果。

高风险动作 prompt 必须满足：

```text
P0：主视觉结果 / 动作因果 / 接触或压力关系 / 时间窗
P1：角色身份 / 场景 / 镜头 / 风格
P2：负面约束 / 禁止项 / 不要回到旧失败路线
```

不能把 P0 埋在 reference duty、风格、审计表、负面词或资产编号之后。

## 1. P0 首句规则

高风险动作 prompt 的第一句必须说明“看得见的动作结果”。

例：

```text
A 5-second cinematic semi-realistic 3D wuxia action video in a rainy ancient temple side corridor: from the first frame, Fenshou, a black-red armored male warrior, is already close in center-left, driving forward with compact shoulder-and-forearm pressure into Shuangji's crossed guard.
```

禁止首句是：

- asset ID
- phase ID
- package metadata
- reference duty
- “This is not final”
- 大段环境/风格铺陈
- 负面约束列表

## 2. 动作因果链字段

动作 prompt 至少包含：

| 字段 | 说明 |
|---|---|
| attacker | 谁发力 |
| defender | 谁承受 |
| force line | 力从哪里到哪里 |
| contact / pressure point | 接触点或压力点 |
| body reaction | 承受方身体如何变化 |
| environment feedback | 地面、雨水、衣服、护甲如何反馈 |
| timing window | 哪一段最可剪 |
| ending state | 是否继续运动，是否反击预备 |
| removed constraints | 旧失败路线明确移除什么 |

## 3. 视频 prompt 的前置动作规则

当生成 4–5s 视频但只需要 1.0–1.5s 可用动作时，必须明确：

```text
first frame already close
no long approach
main pressure/contact by 0.35s
skid/reaction by 0.65s
counter-readiness by 1.35s
cut-worthy moment by 1.50s
keep motion alive after main contact
no static pose-out
```

推荐时间表：

| 时间 | 动作 |
|---|---|
| 0.00–0.10s | 已经近身，无长距离起跑 |
| 0.10–0.35s | 肩/前臂压力进入交叉护架 |
| 0.35–0.65s | 防守方滑步，雨水/地面/护架反馈出现 |
| 0.65–1.00s | 短暂压力锁 / hit-stop |
| 1.00–1.35s | 防守方扭身反击预备 |
| 1.35–1.50s | 可剪辑窗口 |
| 1.50s 后 | 继续运动，不进入静态摆拍 |

## 4. 结果优先，不等于负面堆砌

负面词必须服务 P0，不得主导 prompt。

推荐写法：

```text
No body-wall contact, no wall hit, no wall damage, no static pose-out, no magic blast.
```

不推荐：

- 重复几十个相近负面词
- 把模型注意力拉回失败目标
- 在正向目标不清晰时大量写 negative constraints

## 5. Reference Duty 规则

如果使用参考图，必须写清：

```text
reference_label
duty
forbidden_duty
priority
risk
mitigation
```

参考图不得默认承担全部任务。

例如：

- architecture ref 只管场景/墙面材质，不管动作姿态。
- identity ref 只管身份，不管构图。
- layout ref 只管几何，不管最终美术。

## 6. Prompt Review 默认策略

用户默认审查图片/视频，不审 prompt。

prompt 只在这些情况给用户看：

1. 连续失败。
2. 核心动作方向改变。
3. package review 发现阻塞缺陷。
4. 用户主动要求看 prompt。
5. 需要由用户判断创意方向是否偏离。

## 7. Visual Result Compliance

每个高风险 prompt 应同时生成视觉验收条件，供下载后审片：

```text
是否一开始已近身？
是否看得出交叉护架？
是否有肩/前臂压力？
是否有湿地滑步？
是否有雨水/衣服/护甲反馈？
是否变成推手？
是否静态 pose-out？
是否泄漏旧失败目标？
哪一段能剪出 1.0–1.5s？
```

## 8. SHOT-04 R02 的 prompt 教训

- audit-oriented prompt 可能 clause-level 合规但视觉失败。
- result-first prompt 也不能保证远端成功，但更利于判断失败原因。
- text2image 不是双人近身战斗的默认安全路径。
- text2video prompt 必须 motion-first，不能按静帧逻辑写。
- 旧失败约束必须明确 removed，不允许悄悄回流。

## 9. 推荐 Prompt Compiler 输出结构

每次编译输出：

```text
1. P0 dominant result sentence
2. Action chain
3. Timing plan
4. Composition / camera
5. Identity/environment support
6. Removed constraints
7. Compact negatives
8. Visual result compliance checklist
9. Risk labels
10. Human review surface
```
