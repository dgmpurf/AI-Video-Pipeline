# AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿

> 项目：AI视频制作  
> 类型：实测规则库增补稿 / combat prompt density and causal damage supplement  
> 版本：V1.11  
> 生成日期：2026-06-26  
> 适用范围：AI 视频动作 / 武打 / 连续近战 / 环境交互破坏类 prompt  
> 证据等级：B 级项目实测规则  
> 使用定位：补充 V1.2 动作与打击感规则、V1.8 多模态素材职责、V1.9 空间调度、V1.10 / V1.10.1 场景锚点与视角规则；不替代 Dreamina CLI 执行契约。  
> 重要说明：本文件可上传到 ChatGPT Project Source；Codex 本地 `sources/` 目录仍按只读参考处理，除非人工另行授权修改。

---

## 0. 一句话结论

连续战斗镜头不能只靠“激烈、真实、电影感”驱动；必须用**早接触、contact-beat 数量、演员因果、环境破坏因果、无 idle tail** 把动作密度写成可审计结构。

```text
空间只保留一个主区域，但动作必须更密、更硬、更连续。
```

---

## 1. 生成依据与证据等级

本规则来自《赤焰对天穹》SHOT-02 / SHOT-03 多轮真实生成、下载、人审、剪辑诊断和 prompt 审核。

### 1.1 SHOT-02 V018：速度补救有效的边界

- V018 原始内容基本成立：角色关系、接触链、打击方向、镜头关系可用。
- 通过本地 `1.18x` speed diagnostic 后成为当前 SHOT-02 edit candidate。
- 经验：**speed-up 可以修节奏，但不能修动作结构。**
- 适用边界：只有当原片动作链完整、contact beats 存在、身份和空间关系成立时，速度诊断才值得优先尝试。

### 1.2 SHOT-03 V001：空间连续性不能靠压缩路线解决

- V001 有早期 combat 和建筑参与价值。
- 失败点：深厅 / corridor 起点缺少进入因果；eaves / roof endpoint 过于突兀。
- 经验：空间路线要清楚，但不能为了展示完整路线，把 5 秒镜头塞满过多地点。

### 1.3 SHOT-03 V002：一镜头过载空间路线会导致混乱

- V002 试图覆盖 exterior veranda、columns、wet stairs、eaves、roof / tiles。
- 结果：choreography chaotic、route jumpy、rooftop / tile position too early、face stability weak。
- 经验：一个 5 秒 combat shot 应优先一个主空间区，最多只做一次清晰位移，不应一镜头完成“外廊 → 台阶 → 檐口 → 屋顶”。

### 1.4 SHOT-03 V003：空间简化不等于动作成功

- V003 将空间简化到 exterior corridor / column / railing zone。
- 失败点：动作密度不足、打击弱、环境破坏因果错误、最后约 1 秒停手。
- prompt 审核显示：开头过度 setup / leg movement；没有强制早接触；没有 contact-beat 数量；使用泛称“one character / another character”；允许建筑破坏但没有因果绑定；结尾“clear endpoint / readable ending”诱导站定。
- 经验：空间简化后，更需要 contact-beat schedule 来保证战斗密度。

### 1.5 证据等级

- 当前等级：B 级项目实测规则。
- 适用：Dreamina / Seedance-like workflow 的动作视频 prompt，尤其是近身打斗、环境交互、建筑破坏、脚步/身法镜头。
- 限制：尚未跨项目验证为 A 级通用规则。
- 升级条件：SHOT-03 V004+ 以及至少一条额外 combat sequence 复现成功。

---

## 2. 规则：5 秒战斗镜头必须有动作密度

5 秒 combat source clip 不能用“先建立空间、再慢慢进入战斗、最后清楚收束”的普通镜头逻辑。它必须在时间表里直接写入动作密度。

### 2.1 硬性建议

- 第一处明确接触应发生在 `0.15s-0.30s` 内。
- 纯 setup / 纯腿部移动 / 纯站位不得超过 `0.35s`。
- 5 秒战斗片段应至少包含 `5-6` 个清晰 contact beats。
- 每个 contact beat 必须包括：
  - attack path
  - contact point
  - defender reaction
  - rebound
  - immediate continuation
- 最后 `0.8s` 必须继续攻防，并建议 cut mid-exchange。
- 避免以 pose、对视、站定、readable endpoint、clear endpoint 收尾。

### 2.2 高风险写法

```text
0.00s-1.20s: establish the space / move along the corridor
3.60s-5.00s: readable ending / clear endpoint
```

这种写法容易让模型生成腿部前后移动、空间展示、最后站定。

### 2.3 更稳写法

```text
0.00s-0.30s: Fenshou's forearm collides with Shuangji's guard.
0.30s-1.20s: two more short contact beats, each with visible reaction and rebound.
3.50s-5.00s: continue fighting through the cut; no pose-out, no idle tail.
```

---

## 3. 规则：Action prompt 必须有 contact-beat schedule

所有 fast combat / hand-to-hand / weapon clash / environment fight prompt，都应包含可审计的 timing schedule。

### 3.1 5 秒 baseline 表

| Time | Required combat function |
|---|---|
| `0.00s-0.30s` | first contact |
| `0.30s-1.20s` | at least two additional contacts |
| `1.20s-3.50s` | continued attack-defend chain |
| `3.50s-5.00s` | no idle tail; at least two contact / re-entry actions |

### 3.2 每一行必须能回答

- 谁攻击？
- 谁防守？
- 使用哪个身体部位 / 武器 / 道具？
- 接触点在哪里？
- 受力方向是什么？
- 脚步结果是什么？
- 反弹 / 换线 / 追击如何继续？

如果 prompt 不能回答这些问题，不应进入 live submit。

---

## 4. 规则：演员因果必须明确，不要泛称“一个角色”

### 4.1 避免

```text
one character attacks, another character defends
one fighter moves forward, the other moves sideways
一方前压，另一方侧移
```

这类写法会削弱攻防因果，让模型生成“好像在动，但打击关系不清”的动作。

### 4.2 使用明确主体

```text
Fenshou attacks / Shuangji defends.
Shuangji counters / Fenshou recoils.
Fenshou's right forearm drives diagonally toward Shuangji's centerline.
Shuangji's left forearm catches the wrist and redirects it outward.
```

### 4.3 每个 beat 应具备

```text
角色名
→ 攻击路径
→ 接触点
→ 防守 / 受击反应
→ 脚步结果
→ 反弹 / 续招
```

---

## 5. 规则：环境破坏必须有唯一因果链

建筑、栏杆、瓦片、木门、木格窗、檐口、灯笼、经幡等环境反馈，必须被具体动作触发。

### 5.1 必须满足

- 明确身体部位或物体撞到明确环境元素。
- 损坏只在接触之后出现。
- 裂纹 / 木屑 / 碎片位置与接触点一致。
- 碎片方向服从受力方向。
- 攻击者 / 防守者 / 建筑三者至少有一个清晰反作用反馈。

### 5.2 禁止

- 角色打中对手时，后方木头或石头无因开裂。
- 裂口提前出现。
- 裂口出现在错误高度 / 错误位置。
- 背景自动损坏但没有接触事件。
- 只把破坏当装饰特效，而不是战斗因果链。

### 5.3 稳妥写法

```text
Fenshou shoulder-checks Shuangji's guard and forces her half-step sideways into the wooden railing. The railing cracks only at Shuangji's shoulder-back contact point; two small splinters and rain droplets fly outward in the same force direction. Shuangji rebounds from the railing and immediately counters.
```

### 5.4 如果写不清因果

如果不能把破坏写成清楚因果链，就移除破坏，只保留雨水飞溅、衣摆、发丝、脚步水花等非结构破坏反馈。

---

## 6. 规则：一个 5 秒镜头优先一个主空间

### 6.1 避免空间过载

高风险路线：

```text
exterior corridor -> stairs -> eaves -> roof
```

在 5 秒内完成这类四级路线，很容易导致 jumpy route、面部崩坏、屋顶过早、动作编排混乱。

### 6.2 更稳空间策略

```text
one exterior corridor / column / railing zone
with tactical column use, railing pressure, wet-floor footwork, and one causally bound local reaction.
```

### 6.3 关键提醒

- 如果简化空间，不要同时简化动作。
- 建筑必须成为战术障碍或因果反馈，不只是背景。
- 本地破坏必须服务于 contact beat。
- 湿石阶、屋檐、屋顶线可以作为背景/方向提示，但不应同时成为主动作区。

---

## 7. 规则：尾段必须“切在动作中”

### 7.1 禁用结尾语言

避免：

- readable endpoint
- clear ending
- settle into stance
- hold position
- face each other
- return to calm pose
- 清晰收束
- 稳定站定
- 对视停顿

### 7.2 推荐结尾语言

使用：

- continue fighting through the cut
- cut mid-exchange
- immediate re-entry
- no pose-out
- no idle tail
- final frame still contains attack / defense / recovery motion
- 最后一帧仍在攻防 / 追击 / 反弹 / 恢复中

### 7.3 原则

对战斗片段而言，一个“干净结束”通常不如一个“可剪辑的动作尾巴”。  
除非镜头本身是胜负收束或情绪对峙，否则不要让 combat clip 在最后 0.8 秒站住。

---

## 8. 规则：腿部 / 脚步镜头必须服务战斗

### 8.1 有效脚步功能

脚步必须绑定战斗功能，例如：

- kick
- sweep
- step trap
- slip recovery
- pivot under pressure
- forced sidestep
- traction loss after impact
- rebound step into next contact
- 踩水滑退后立刻反击
- 被撞偏后用脚跟刹住重心

### 8.2 时间限制

不要花超过 `0.35s` 展示无战斗结果的腿部前后移动。

### 8.3 高风险画面

```text
one foot moves forward and the other moves back
```

如果没有 contact、tactical effect、recovery、re-entry，它只会读成弱 setup，而不是打斗。

---

## 9. 规则：中景保护脸，但不保证动作密度

中景 / 中远景可以降低脸崩风险，但不能自动提高动作密度。

### 9.1 必须同时使用

- framing protects face / identity
- beat count protects combat density

### 9.2 避免

- 中景下远远地低冲击移动。
- 中景下花太多时间走位。
- 中景下最后停手对视。
- 以“脸稳定”为理由取消密集接触。

### 9.3 适用

- 快速打斗中，避免极近脸部特写。
- 表情镜头和动作镜头分开设计。
- 若必须保脸，仍要用 contact-beat schedule 保动作。

---

## 10. 规则：速度补救的适用边界

### 10.1 适合做 speed-up 的情况

- 内容正确。
- 动作链完整。
- contact beats 已存在。
- 身份和空间关系可用。
- 只有 rhythm 稍慢。

SHOT-02 V018 支持这类用法：原内容成立，只需局部速度诊断解决节奏问题。

### 10.2 不适合 speed-up 的情况

- contact beats 缺失。
- 破坏因果错误。
- 角色停手。
- 错误物体开裂。
- prompt 时间结构错误。
- 有 idle tail。
- 纯腿部移动过长。

SHOT-03 V003 说明：速度不能修结构性 prompt 失败。

---

## 11. 流程规则：ChatGPT Prompt Content Audit Gate

Codex package review 只能证明文件、引用、JSON/CSV、权限和安全边界成立。  
动作类 prompt 还必须通过 ChatGPT 内容审核。

### 11.1 Combat prompt submit 前置条件

进入 live submit 前必须满足：

```text
codex_package_review=passed
chatgpt_prompt_content_audit=passed
human_submit_authorization=true
```

### 11.2 ChatGPT 内容审核必须检查

- 第一接触时间。
- contact beat 数量。
- 最后 `0.8s` 是否继续攻防。
- 是否有明确 Fenshou / Shuangji 主体因果。
- 环境破坏是否有因果链。
- 是否有脸部 / 身份风险。
- 是否有 idle-tail / pose-out 风险。
- 正向动作是否足够具体。
- 负面约束是否过长而挤压动作信息。
- 是否把“速度补救”错误用于结构失败片段。

### 11.3 通过标准

一个 combat prompt 至少要能回答：

```text
0.15-0.30 秒谁和谁发生第一次接触？
5 秒内有几个独立 contact beats？
每个 contact beat 打到哪里，谁怎么反应？
最后 0.8 秒是否还在打？
如果建筑损坏，谁撞到了哪里，裂口从哪里出现？
```

不能回答，则不应 submit。

---

## 12. V004 方向摘要

SHOT-03 V004 应遵守：

- 不复用 V003 timing structure。
- 使用 contact-beat schedule。
- 第一接触在 `0.15s-0.30s`。
- 5 秒至少 `5-6` 个 contact beats。
- 最后 `0.8s` 继续攻防并 cut mid-exchange。
- 建筑破坏必须绑定单一因果链，或者完全移除。
- 减少无效负面约束，强化正向动作。
- 中景保护脸，但用 beat count 保证动作密度。
- actual manual prompt 必须先通过 ChatGPT 内容审核再 submit。

### 12.1 V004 高层原则

```text
空间只保留一个主区域，但动作必须更密、更硬、更连续。
```

---

## 13. 推荐 Prompt 模板片段

### 13.1 不推荐

```text
0.00s-1.20s: establish exterior corridor. Characters move along the railing.
3.60s-5.00s: clear endpoint and readable ending.
One character uses the column while the other moves sideways.
Railing cracks from the impact.
```

### 13.2 推荐

```text
0.00s-0.25s:
Fenshou's right forearm crashes into Shuangji's left guard near the column. Shuangji's shoulder turns back; her right foot skids on wet stone. Both arms rebound.

0.25s-0.65s:
Shuangji steps back in and snaps a palm into Fenshou's shoulder armor. Fenshou's torso turns off-line; his rear boot splashes water and immediately drives forward again.

0.65s-1.10s:
Fenshou shoulder-checks Shuangji toward the railing. The railing does not crack yet. Shuangji braces, pivots, and counters with a short elbow-line guard.

1.10s-2.20s:
Two more fast contact beats, each with contact point, reaction, rebound, and immediate re-entry.

2.20s-3.60s:
Fenshou forces Shuangji half-step sideways into the wooden railing. Only at her shoulder-back contact point, a short crack appears. Two wood splinters and rain droplets fly outward. She rebounds and counters immediately.

3.60s-5.00s:
Continue two more attack-defense beats through the final frame. No pose-out, no idle tail. Cut mid-exchange.
```

---

## 14. 与既有 Source 的关系

- 补充 V1.2：更细化连续 combat 的 contact beat 和因果链。
- 补充 V1.8：多模态参考图职责不等于动作结构；动作仍需 timing schedule。
- 补充 V1.9：空间调度要与动作密度同时成立。
- 补充 V1.10 / V1.10.1：场景锚点和视角清楚不等于战斗有效；仍需 contact schedule。
- 不替代 Dreamina CLI help、Dreamina CLI 执行契约、manifest schema、Seedance 手册。

---

## 15. 最终执行提醒

任何后续 SHOT-03 V004 或新 combat/action prompt：

1. 先读取本规则。
2. 生成 actual manual prompt。
3. ChatGPT 审核 prompt 内容。
4. Codex package review 审技术结构。
5. 人类明确批准 submit。
6. 再进入 Dreamina canary / preflight / single submit。

不要让“文件正确”掩盖“动作不够密、不够因果、不够连续”。

---

## 16. Final Verdict

```text
SOURCE_V1_11_CONTINUOUS_COMBAT_DENSITY_AND_CAUSAL_DAMAGE_READY
```
