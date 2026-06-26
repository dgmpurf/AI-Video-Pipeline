# AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿_DRAFT

> 状态：DRAFT，仅供人工审阅。  
> 输出位置：`reports/source_update_drafts/`。  
> 重要说明：本文件不是正式 `sources/` 修改，不应直接视为已进入 Project Source。  
> 生成依据：SHOT-02 combat closeout / SHOT-02 V018 speed diagnostics / SHOT-03 V001-V003 human review and prompt audit.  
> 证据等级：B 级项目实测规则。已由《赤焰对天穹》多轮 SHOT-02 / SHOT-03 实测强支持，但尚未跨项目验证为 A 级通用规则。

---

## 1. Purpose

本草案沉淀 SHOT-02 与 SHOT-03 战斗生成实测经验，重点补充：

- 连续战斗动作密度。
- 接触 beat 时间表。
- 环境破坏因果链。
- 末尾 idle tail / pose-out 防止。
- 动作 prompt 提交前内容审计门槛。

它补充 V1.2 的打击感 / 受力反馈规则、V1.8 的多模态素材职责、V1.9 的空间调度、V1.10/V1.10.1 的场景锚点与运镜规则，不替代现有 Source。

---

## 2. Evidence Base

### 2.1 SHOT-02 V018

- V018 是当前 SHOT-02 强候选，并通过 `1.18x` 本地 speed diagnostic 锁定为当前 edit candidate。
- Speed-up 有效的前提是原始内容已经基本可用：角色关系、接触链、打击方向和画面结构成立。
- 结论：speed-up 可以修节奏，不可修内容结构。

### 2.2 SHOT-03 V001

- V001 mixed positive：早期 combat 和建筑参与有可取之处。
- 主要问题是 continuity：起点像深厅 / corridor，结尾 abrupt eaves / roof endpoint。
- 结论：空间路线需要清楚，但不能为了路线把 5 秒镜头塞满过多地点。

### 2.3 SHOT-03 V002

- V002 rejected：试图在一个 5 秒片段内覆盖 exterior veranda、columns、wet stairs、eaves、roof/tiles。
- 结果 choreography chaotic，route jumpy，rooftop / tile position too early，face stability weak。
- 结论：一镜头不能过载空间路线；一个 5 秒 combat shot 应优先一个主空间区。

### 2.4 SHOT-03 V003

- V003 failed for action density, weak impact, wrong environmental damage causality, and idle tail。
- Prompt 简化了空间，但过度转向 setup / leg movement，没有强制早接触、contact beat 数量、因果破坏和末尾持续交锋。
- 结论：空间简化不是战斗成功。战斗 prompt 必须有可审计的 contact-beat schedule。

---

## 3. Rule: 5-Second Combat Action Density

5 秒 combat source clip 必须有足够动作密度。

硬规则：

- First contact should happen within `0.15s-0.30s`.
- No pure setup / leg movement longer than `0.35s`.
- A 5-second combat clip should contain at least `5-6` clear contact beats.
- Each contact beat must include:
  - attack path
  - contact point
  - defender reaction
  - rebound
  - immediate continuation
- Last `0.8s` must continue fighting and should cut mid-exchange.
- Avoid ending with pose, stare, standing still, readable endpoint, or clear endpoint language.

风险写法：

```text
0.00s-1.20s: establish the space / move along the corridor
3.60s-5.00s: readable ending / clear endpoint
```

更稳写法：

```text
0.00s-0.30s: Fenshou's forearm collides with Shuangji's guard.
0.30s-1.20s: two more short contact beats, each with visible reaction and rebound.
3.50s-5.00s: continue fighting through the cut; no pose-out, no idle tail.
```

---

## 4. Rule: Contact-Beat Schedule Required

Action prompts must include a beat table or explicit timing schedule.

Baseline for a 5-second combat clip:

| Time | Required combat function |
| --- | --- |
| `0.00s-0.30s` | first contact |
| `0.30s-1.20s` | at least two additional contacts |
| `1.20s-3.50s` | continued attack-defend chain |
| `3.50s-5.00s` | no idle tail; at least two contact/re-entry actions |

Each row should name:

- who attacks
- who defends
- body part / weapon / contact point
- reaction direction
- footwork result
- rebound or next entry

如果 prompt 不能回答这些问题，不应进入 live submit。

---

## 5. Rule: Actor-Specific Causality

Avoid generic language such as:

```text
one character attacks, another character defends
one fighter moves forward, the other moves sideways
```

Use explicit subject causality:

```text
Fenshou attacks / Shuangji defends.
Shuangji counters / Fenshou recoils.
Fenshou's right forearm drives diagonally toward Shuangji's centerline.
Shuangji's left forearm catches the wrist and redirects it outward.
```

Every combat beat should name:

- attack path
- contact point
- reaction direction
- footwork
- rebound / continuation

This protects attack-defense causality and reduces soft push-hands or generic body drifting.

---

## 6. Rule: Environmental Damage Causality

Any architecture or prop damage must be causally bound.

Required:

- exact body part or object hits exact environment element
- damage appears only after contact
- crack / splinter point matches impact point
- debris direction follows force direction
- attacker and defender both show reaction or rebound

Forbidden:

- character hits opponent while unrelated wood / stone cracks behind them
- cracks appear before impact
- crack appears at wrong height or wrong location
- background damage with no visible contact event
- decorative breakage that is not part of the combat chain

If the damage cannot be described as a clear cause-effect chain, remove the damage entirely.

---

## 7. Rule: Local Environment Interaction

One 5-second shot should prioritize one main spatial zone.

Avoid packing:

```text
exterior corridor -> stairs -> eaves -> roof
```

into a single 5-second combat generation.

Better:

```text
one exterior corridor / column / railing zone
with tactical column use, railing pressure, wet-floor footwork, and one causally bound local reaction.
```

Important caution from V003:

- If simplifying space, do not also simplify action.
- Architecture should be tactical obstacle or causal reaction, not decoration.
- Local breakage must serve a contact beat.

---

## 8. Rule: Tail Behavior

Replace ending language that invites standing still.

Avoid:

- readable endpoint
- clear ending
- settle into stance
- hold position
- face each other
- return to calm pose

Use:

- continue fighting through the cut
- cut mid-exchange
- immediate re-entry
- no pose-out
- no idle tail
- final frame still contains attack / defense / recovery motion

For combat clips, a clean ending is often worse than a usable edit handle.

---

## 9. Rule: Leg / Footwork Shots

Footwork must serve combat.

Valid footwork functions:

- kick
- sweep
- step trap
- slip recovery
- pivot under pressure
- forced sidestep
- traction loss after impact
- rebound step into next contact

Do not spend more than `0.35s` on legs moving without contact or tactical effect.

If showing feet, bind footwork to:

- an attack
- a defense
- a contact beat
- a forced reaction
- wet-floor feedback

Risk:

```text
one foot moves forward and the other moves back
```

without combat consequence reads as weak setup, not fighting.

---

## 10. Rule: Face Stability vs Action Density

Medium / medium-wide framing can reduce face collapse, but it does not guarantee action density.

Use both:

- framing to protect face / identity
- beat count to protect combat density

Avoid extreme face close-ups in fast combat unless the shot is about expression rather than action.

Medium framing should not become an excuse for:

- setup-heavy blocking
- distant low-impact movement
- idle endings
- unclear contact points

---

## 11. Rule: Speed-Up Applicability

Local speed-up is valid only when:

- content is correct
- action chain is complete
- contact beats exist
- identities and spatial relationships are usable
- only rhythm is slightly slow

Speed-up is not valid when:

- contact beats are missing
- damage causality is wrong
- characters stop fighting
- wrong object cracks
- prompt timing structure is broken
- the shot has an idle tail

SHOT-02 V018 supports speed-up as a finishing edit tool. SHOT-03 V003 shows speed-up cannot repair structural combat prompt failure.

---

## 12. Process Rule: ChatGPT Content Audit Gate

Before any live submit for action / combat prompts, require:

1. Codex package review passed.
2. ChatGPT prompt content audit passed.
3. Human submit authorization.

The prompt content audit must check:

- first contact timing
- contact beat count
- final `0.8s` action
- actor-specific causality
- environmental damage causality
- face / identity risk
- idle-tail / pose risk
- overlong negative constraints vs concrete positive action

Codex package review alone is not enough for action prompts. A package may be syntactically valid but content-weak.

---

## 13. V004 Direction Summary

SHOT-03 V004 should:

- not reuse V003 timing structure
- use a contact-beat schedule
- continue fighting through final frame
- bind or remove environmental damage
- use fewer but stronger negative constraints
- keep medium framing while protecting action density
- receive actual manual prompt audit before submit

High-level V004 principle:

```text
空间只保留一个主区域，但动作必须更密、更硬、更连续。
```

---

## 14. Status / Evidence Level

- Evidence level: B-level project-tested rule.
- Scope: AI video combat prompts for Dreamina / Seedance-like workflows.
- Evidence: repeated SHOT-02 / SHOT-03 generation, download, human review, local edit diagnostics, and prompt audit.
- Limitation: not yet cross-project universal.
- Upgrade to A-level requires repeated success in SHOT-03 V004+ and at least one additional combat sequence or project.

---

## 15. One-Line Summary

```text
连续战斗镜头不能只靠“激烈、真实、电影感”驱动；必须用早接触、contact-beat 数量、演员因果、环境破坏因果和无 idle tail 规则把动作密度写成可审计结构。
```
