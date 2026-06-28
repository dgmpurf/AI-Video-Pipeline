# AI视频制作_Prompt编译器与结果优先动作语法_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Source 候选 / Prompt Compiler / Result-first Action Grammar  
> 版本：V0.1  
> 生成方：ChatGPT  
> 建议应用方式：由人类用户手动上传 / 复制到 ChatGPT Project Source 或本地 `sources/`。Codex / automation 不得直接写入 `sources/`。  
> 核心目的：在 Source 规则、Codex package review 与 Dreamina submit 之间，增加一层“Prompt Compiler / Prompt Director”规则，确保 prompt 不只是规则齐全，而是把模型注意力优先导向可见视觉结果。

---

## 0. 一句话结论

```text
Source compliance 不是 rule inclusion，而是 visible-result prioritization。
高风险动作 / 建筑互动 prompt 必须先写“结果优先动作主句”，再写参考职责、时间表和负面约束。
```

以前的失败不是流程坏了，而是 prompt 编译层不够强：

```text
Source 读到了；
package 合规了；
clause-level compliance 也通过了；
但模型第一优先级没有被推向“必须看到的动作结果”。
```

---

## 1. 生成依据与证据等级

本规则来自《赤焰对天穹》SHOT-03 / SHOT-04 多轮真实生成、下载、人审、ChatGPT 复盘、Codex 报告与 prompt/package 审计。

主要证据链：

```text
K190：SHOT-04 Route A 视觉失败。prompt 通过 package/source compliance，但核心动作失败，生成结果读成 sustained pushing / wrestling tendency。
K191：提出 R02 result-first 策略，将动作改写为 wooden wall-panel slam / back-first rebound。
K191P：审计当前 prompt pipeline，确认缺少 Prompt Compiler / Prompt Director 层。
K192：确认不应盲目直接 prompt-only 重包；应先补 wall-panel / side-wall 视觉目标参考，再考虑 contact keyframe。
```

证据等级：

```text
B 级项目实测规则。
```

理由：

```text
已经有本项目真实失败链路支持，但仍需在 SHOT-04 R02 / 后续动作镜头中继续复测。
```

---

## 2. 适用范围

适用于：

```text
近身格斗
建筑 / 地形互动
撞墙 / 撞栏杆 / 撞门框
木格 / 木墙板 / 侧廊墙接触
短爆发身体冲撞
武器或身体导致环境局部反馈
双人动作 blocking
需要身份、动作、场景、接触因果同时成立的复杂 prompt
```

尤其适用于：

```text
“动作描述已写得很详细，但模型仍然生成软推、摆 pose、站桩、推搡、wrestling hold”的情况。
```

不替代：

```text
Source governance
Dreamina CLI 执行契约
DreaminaBatcher manifest schema
已有动作密度 / contact beat / damage causality 规则
Composition Matrix
```

它补充的是：

```text
prompt 编译顺序、模型注意力优先级、结果主句语法、视觉结果验收表。
```

---

## 3. Prompt Compiler / Prompt Director 定义

### 3.1 Prompt Compiler

Prompt Compiler 是 package 之前的提示词编译层。

它负责把：

```text
创作意图
+ Source 规则
+ K-phase failure evidence
+ reference-duty map
+ 人类 / ChatGPT 审核意见
```

转成：

```text
模型真正容易执行的、结果优先、优先级排序清楚的 prompt grammar。
```

Prompt Compiler 不只是把规则塞进 prompt。  
它必须决定：

```text
1. 哪个视觉结果最重要？
2. 这个视觉结果是否出现在 prompt 最前面？
3. 哪些参考图会抢模型注意力？
4. 哪些负面约束会稀释动作？
5. 这件事能不能靠 prompt-only 完成？
6. 是否需要关键帧、墙面参考、pose sketch、frames2video 或 multiframe？
```

### 3.2 Prompt Director

Prompt Director 是人类 / ChatGPT 的判断角色。

它负责在冲突中做选择：

```text
身份 vs 动作
场景一致 vs 接触点清晰
建筑反馈 vs 不破坏
脸部可读 vs 身体遮挡
时间表完整 vs 主结果强度
```

Prompt Director 的核心判断：

```text
本镜头最想让观众看到什么？
```

如果答不出来，不应进入 L2 package。

---

## 4. 当前 pipeline 的健康部分

当前半自动流程应保留：

```text
1. Source read-only governance
2. human-only official Source update
3. macro-run 授权等级
4. submit / query / download / retry / final / lock 分离
5. package JSON / manifest CSV / prompt txt 可审计
6. ref sha256 校验
7. Dreamina command-contract preflight
8. K-phase report / commit / push traceability
9. media 默认不 stage
10. human + ChatGPT visual review gate
```

结论：

```text
工程治理是健康的。
不要为了 prompt 失败去削弱 submit/query/download/final/source 边界。
```

---

## 5. 当前 pipeline 的弱点

当前弱点不是“不读 Source”，而是：

```text
Source rule included ≠ visual result prioritized
```

常见失败：

```text
1. clause-level Source compliance 通过，但主视觉动作不够强。
2. prompt 前半段被 reference duties / scene / camera / constraints 占满。
3. 主动作结果出现太晚。
4. 使用 soft verbs：compress / pressure / move toward / use environment。
5. 负面约束过多，稀释正向动作。
6. 时间表变成审计 checklist，而不是模型驱动语法。
7. package review 证明文件正确，但不能证明视觉结果会成功。
```

---

## 6. Result-first prompt 核心规则

高风险动作 prompt 必须先写：

```text
dominant visual result sentence
```

它应该回答：

```text
观众第一眼必须看到什么动作结果？
谁打谁？
用什么身体部位？
打到什么接触点？
对方身体如何位移？
环境产生什么后果？
动作如何继续？
```

推荐语法：

```text
Actor body-part -> target contact-point -> immediate visible consequence -> continuation.
```

示例：

```text
Fenshou lands one explosive shoulder-check into Shuangji's crossed guard and slams her back-first into a wooden wall panel.
```

然后再写：

```text
Her shoulder and upper back hit the panel hard.
The panel makes a shallow inward dent / local flex only at the exact contact point.
A burst of rainwater and two tiny wood splinters move outward in the same force direction.
The wall panel remains standing.
Shuangji immediately rebounds off the panel and counters.
```

---

## 7. 推荐 Prompt 层级 V0.1

高风险动作 / 建筑互动 prompt 推荐顺序：

```text
A. Dominant visual result sentence
B. Actor / target / impact object
C. Physical consequence
D. Rebound / continuation
E. Scene and camera
F. Reference duties
G. Timing schedule
H. Identity protection
I. Compact negative constraints
```

### 7.1 A：Dominant visual result sentence

必须在最前面 1–2 句内出现。

标准：

```text
读完开头，审稿人能立刻说出“这个镜头必须发生什么”。
```

### 7.2 B：Actor / target / impact object

必须清楚：

```text
Fenshou 是动作发起者；
Shuangji 是承受者但不是被动摆拍；
impact object 是 wooden wall panel / side-wall / lattice wall；
不是抽象的“environment”。
```

### 7.3 C：Physical consequence

必须写身体结果：

```text
torso turns
upper back hits
rear foot skids
guard compresses
water bursts
local dent/flex appears
```

### 7.4 D：Rebound / continuation

必须防止静态推搡：

```text
Shuangji immediately rebounds and counters.
Fenshou recoils and re-enters.
No sustained pushing.
No wrestling hold.
```

### 7.5 E：Scene and camera

场景和镜头要服务主动作，不要盖过它：

```text
medium-wide rainy corridor combat shot
slight front three-quarter angle
both feet and contact point readable
```

### 7.6 F：Reference duties

参考职责要短、清楚、排好优先级。  
不要让 reference-duty prose 占据 prompt 开头过多位置。

### 7.7 G：Timing schedule

时间表必须支持主结果，而不是替代主结果。

### 7.8 H：Identity protection

身份保护要紧凑：

```text
Fenshou remains black-red male fighter.
Shuangji remains female-coded blue-white/silver fighter.
```

### 7.9 I：Compact negative constraints

负面约束应压缩，不要堆墙。

---

## 8. Strong verbs / Soft verbs 规则

### 8.1 优先使用强结果动词

推荐：

```text
slam
crash
drive into
shoulder-check
hit
snap back
rebound
counter
skid
jam
deflect
```

### 8.2 避免 soft process verbs 作为主动作

风险词：

```text
compress toward
pressure
guide toward
move into
use the environment
interact with
crowd
approach
shows tension
```

这些词可以作为辅助，但不能做主动作结果句。

### 8.3 例子

弱：

```text
Fenshou compresses Shuangji's guard toward the railing.
```

强：

```text
Fenshou's shoulder-check slams Shuangji back-first into the wooden wall panel, then she rebounds into a counter.
```

---

## 9. Prompt Priority Audit

每个高风险 prompt 在 L2 package 前必须做 Prompt Priority Audit。

| priority_rank | prompt_segment | word_position_or_section | intended_model_attention | result_strength_score_0_to_2 | risk_of_misread | rewrite_needed | notes |
|---|---|---|---|---:|---|---|---|
| P0 | Dominant visual result sentence | first 50–80 words | Required visible action | 0/1/2 | soft push / pose / missing result | yes/no |  |
| P0 | Physical hit path | opening action block | Cause of impact | 0/1/2 | no force chain | yes/no |  |
| P0 | Environmental consequence | opening or immediate follow-up | Contact feedback | 0/1/2 | random damage / no damage | yes/no |  |
| P0 | Rebound / continuation | opening or timing block | No static hold | 0/1/2 | wrestling tendency | yes/no |  |
| P1 | Reference duties | compact reference section | Identity / scene protection | 0/1/2 | ref attention conflict | yes/no |  |
| P1 | Timing schedule | after result block | Contact density | 0/1/2 | checklist without result | yes/no |  |
| P2 | Negative constraints | end block | Risk suppression | 0/1/2 | dilution / overconstraint | yes/no |  |

评分：

```text
0 = 缺失或很弱
1 = 存在但可能被误读
2 = 强、靠前、可视觉验收
```

硬规则：

```text
P0 任一项为 0，不应进入 L2 package。
P0 主结果句如果出现在 reference/scene/camera 长段之后，应标记 rewrite_needed=true。
```

---

## 10. Visual Result Compliance

Visual Result Compliance 与 Source compliance 分开。  
它检查 prompt 是否定义了可视觉验收的结果。

| intended_visual_result | prompt_phrase | expected_screen_evidence | risk_if_model_ignores | needs_keyframe_or_reference | pass_condition_for_review |
|---|---|---|---|---|---|
| Shuangji is slammed back-first into wooden wall panel |  | upper back/shoulder hits wall surface | soft push / no target | true/false | visible body-wall contact |
| panel dents/flexes locally |  | shallow dent/local flex at contact point | random damage / no feedback | true/false | feedback appears after contact only |
| rainwater/two splinters burst outward |  | small particles follow force direction | decorative debris | true/false | debris direction matches hit |
| Shuangji rebounds and counters |  | body leaves wall and counter begins | pinned/wrestling hold | true/false | rebound within same shot |
| final frame cuts mid-exchange |  | both still moving | pose-out | false | no idle tail |

---

## 11. Negative Constraint Compression Audit

### 11.1 审计目标

防止 prompt 变成负面限制墙。

### 11.2 方法

记录：

```text
positive_action_word_count
negative_constraint_word_count
negative_to_positive_ratio
duplicated_negatives
convertible_negatives
high_priority_negatives_kept
```

建议：

```text
高风险负面约束保留 8–12 条。
重复项合并。
能转成正向表达的转正向表达。
```

例：

弱：

```text
No flying. No jumping. No roof route. No wall run.
```

更稳：

```text
Both fighters remain grounded on the wet corridor floor with short, forceful footwork.
```

再在尾部保留：

```text
No roof route, no wall run.
```

---

## 12. Reference Duty Attention Audit

### 12.1 为什么需要

参考职责是必要的，但如果放在 prompt 最前面过长，会抢走动作结果的注意力。

### 12.2 表格

| ref | duty | priority | should_appear_before_result | risk | mitigation |
|---|---|---|---|---|---|
| Fenshou identity | identity only | P1 | no | identity over action | compact |
| Shuangji identity | identity only, highest identity priority | P1 | no | gender drift / identity drift | compact but explicit |
| Rainy temple scene | world only | P2 | no | scene dilutes action | brief |
| Wall-panel target | architecture target only | P0/P1 | maybe after result | target missing | may need dedicated ref |
| Contact keyframe | action/blocking only | P0 | maybe yes | can pollute identity | duty must be strict |

原则：

```text
主动作结果优先于长 reference prose。
如果 wall-panel target 是核心视觉结果，必须有 P0/P1 级别视觉锚点。
```

---

## 13. Prompt-only Risk Label

当目标物 / 接触姿态没有视觉参考时，必须标记：

```yaml
prompt_only_high_risk: true
missing_visual_target_ref: true
requires_human_acceptance_of_risk: true
```

适用情况：

```text
只靠文字写 wall-panel slam；
现有 scene ref 没有清楚 wall-panel target；
需要精确 body-wall contact；
需要双人身份 + blocking + 建筑反馈同时成立。
```

---

## 14. Prompt Outcome Dataset

每次生成后在 report 中记录：

```yaml
prompt_id:
prompt_sha256:
task_type:
refs_count:
dominant_result_sentence:
first_dominant_action_position:
positive_action_word_count:
negative_constraint_word_count:
negative_to_positive_ratio:
source_rules_used:
visual_status:
identity_status:
action_status:
architecture_causality_status:
blocking_status:
failure_cause_hypothesis:
wording_likely_caused_misread:
next_rewrite_principle:
```

用途：

```text
让失败不只变成主观评价，而变成可检索、可归纳、可升级 Source 的数据。
```

---

## 15. Pre-L2 Checklist for High-risk Action Prompts

在未来高风险动作 prompt 进入 L2 package 前，必须检查：

```text
1. 是否命名了唯一 required visible result？
2. 结果是否在前 1–2 句出现？
3. 是否使用 actor body-part -> contact target -> visible consequence -> continuation？
4. 主动作是否早于长 reference / scene / camera block？
5. 是否把 soft verbs 换成 result verbs？
6. 是否完成 Prompt Priority Audit？
7. 是否完成 Visual Result Compliance？
8. 是否完成 Negative Constraint Compression Audit？
9. 是否完成 Reference Duty Attention Audit？
10. 如果缺 visual target ref，是否标记 prompt_only_high_risk？
11. 是否明确 final_master=false / locked=false？
12. 是否决定 prompt-only 是否足够，还是需要 reference/keyframe/frames？
```

---

## 16. K192 后续路线规则

K192 已确认：

```text
route_decision = B_FIRST_WALL_PANEL_REFERENCE_THEN_C_CONTACT_KEYFRAME
```

后续原则：

```text
1. 先补 wall-panel / side-wall / wooden lattice wall 视觉目标参考。
2. 再考虑 contact keyframe / wall-impact keyframe。
3. 不应直接盲目重新做 prompt-only R02 package。
4. 若没有 wall-panel target ref，直接 prompt-only 必须标记 high-risk。
```

---

## 17. Codex 角色更新

Codex 继续负责：

```text
读取 Source
创建报告
生成 package / manifest / prompt 文件
校验 sha256
执行 Dreamina 命令
抽帧 / sheet / 本地校验
commit / push text reports
```

Codex 新增应负责：

```text
Prompt Priority Audit
Visual Result Compliance
Negative Constraint Compression Audit
Reference Duty Attention Audit
Prompt Outcome Dataset 记录
prompt-only risk label
```

Codex 不负责：

```text
official Source 更新
最终视觉通过
final/lock
无授权 retry/resubmit
高风险创意 prompt 独立改写
```

---

## 18. Future Source 更新建议

本文件可作为 Project Source 候选。

建议文件名：

```text
AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md
```

未来可能再拆分：

```text
AI视频制作_视觉结果合规表与Prompt优先级审计_V0.1.md
AI视频制作_引用职责注意力与负面约束压缩规则_V0.1.md
```

官方 Source 更新流程：

```text
ChatGPT 生成 / 审阅
→ 人类检查
→ 人类手动上传 Project Source
→ 如需本地同步，人类手动复制到 local sources/
→ Codex 后续只读
```

---

## 19. Final Invariants

```yaml
source_write_allowed: false
source_stage_allowed: false
source_commit_allowed: false

source_compliance_is_not_enough: true
visible_result_prioritization_required: true
prompt_priority_audit_required_for_high_risk_action: true
visual_result_compliance_required_for_high_risk_action: true
negative_constraint_compression_required: true
reference_duty_attention_audit_required: true
prompt_only_high_risk_label_required_when_target_ref_missing: true

final_master_requires_human_authorization: true
locked_requires_human_authorization: true
retry_resubmit_requires_human_authorization: true
```

---

## 20. Final Verdict

```text
PROMPT_COMPILER_AND_RESULT_FIRST_ACTION_GRAMMAR_V0_1_READY_FOR_HUMAN_SOURCE_REVIEW
```
