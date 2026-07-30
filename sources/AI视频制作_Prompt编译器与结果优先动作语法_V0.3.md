# AI视频制作_Prompt编译器与结果优先动作语法_V0.3

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Prompt Compiler Source replacement candidate for V0.2  
> 版本：V0.3  
> 生成日期：2026-07-24  
> 状态：**受限候选，待人类审阅并手动应用**  
> 来源：V0.2 规则 + CAL-002 Batch01–Batch04 + Batch04 完整 MP4 mixed verdict  
> 核心限制：V0.3 不把 Batch04 Candidate bundle 提升为统一默认层；它新增的是 action-family routing 和视觉审核 gate。

---

## 0. 核心原则

Prompt Compiler 的目标不是“把所有规则写进去”，而是：

```text
先选择动作族
→ 明确初始状态
→ 编译可见动作因果
→ 规定接触与结果窗口
→ 限制结束状态持续时间
→ 生成可审片的验收条件
```

高风险动作 Prompt 必须满足：

```text
P0：主视觉结果 / 初始状态 / 动作因果 / 接触与结果 / 时间窗
P1：角色身份 / 场景 / 镜头 / Reference duty / 风格
P2：精简负面约束 / removed constraints / 防止旧失败路线
```

不能把 P0 埋在：

- asset ID；
- phase metadata；
- reference duty 长说明；
- 风格词；
- 审计表；
- negative list；
- Source 引用。

---

## 1. 先路由动作族，再写 Prompt

所有高风险动作任务必须先设置：

```yaml
action_family:
action_goal:
initial_state_contract:
contact_contract:
body_result_contract:
foot_result_contract:
ending_contract:
review_window:
```

最小 action family：

```text
push_reaction
brief_impact_recoil
pressure_guard_clash
continuous_combat
knockback_flyout
transition_or_other
```

禁止：

```text
把一个已在 push_reaction 中显示正面信号的 bundle
直接复制到 brief_impact_recoil
```

若动作族未确定：

```text
compiler_status = BLOCKED_ACTION_FAMILY_UNRESOLVED
```

---

## 2. P0 首句规则

高风险动作 Prompt 第一段必须直接说明：

1. 画面要看到的核心动作结果；
2. 初始状态；
3. 谁先发力；
4. 接触发生在哪里；
5. receiver 的主要可见后果。

例：push reaction

```text
A 5-second cinematic push-reaction shot: the attacker and receiver begin visibly separated at close range; the attacker initiates a compact two-hand push, contact becomes readable around the early action window, and only after contact the receiver's torso shifts backward and one rear foot makes a single recovery placement.
```

例：brief impact

```text
A 5-second brief-impact shot: both fighters begin visibly separated; the attacker makes one compact forearm impact, the receiver shows immediate upper-body recoil and exactly one rear-foot step, and the attacker retracts promptly instead of maintaining a push.
```

禁止首句：

- “保持电影感”；
- “参考图如下”；
- “This is not final”；
- “角色A和角色B在场景中”；
- 负面约束；
- package / phase ID。

---

## 3. Initial State Contract

初始状态必须显式选择，不能依赖模型推断。

```yaml
start_mode:
  separated
  already_close_no_contact
  existing_pressure
  continuation_after_contact
```

### 3.1 separated

适用：

- push reaction onset；
- brief impact；
- strike；
- shove；
- collision onset。

必须审核：

```text
first_frame_separation_audit = required
```

### 3.2 already_close_no_contact

适用：

- 近身 guard clash；
- 需要快速接触但仍要看到 contact onset。

关键区别：

```text
already close
≠
already touching
```

### 3.3 existing_pressure

只适用：

- 镜头目标就是 pressure continuation；
- 不需要证明 contact onset。

必须在 Prompt 和 review 中声明：

```text
contact_onset_not_evaluated = true
```

### 3.4 continuation_after_contact

只适用：

- reaction insert；
- release / retract；
- aftermath。

不得将其误评为 impact-onset 成功。

---

## 4. 动作因果链字段

动作 Prompt 至少包含：

| 字段 | 说明 |
|---|---|
| action_family | 动作族 |
| attacker | 谁发力 |
| defender / receiver | 谁承受 |
| initiation | 攻击者怎样启动 |
| force line | 力从哪里到哪里 |
| contact point | 接触点 |
| contact onset | 接触何时可见 |
| body reaction | receiver 身体如何变化 |
| foot result | 是否需要、需要几个、发生何时 |
| attacker release / retract | 是否需要结束接触 |
| environment feedback | 地面、雨水、衣服、护甲反馈 |
| timing window | 动作和可剪窗口 |
| ending state | 最终状态 |
| ending duration | 最终状态允许保持多久 |
| removed constraints | 明确移除旧失败项 |
| visual audits | 下载后如何判断 |

---

## 5. Action-family 编译模板

### 5.1 Push Reaction Compiler

目标链：

```text
separated start
→ visible initiation
→ readable contact
→ post-contact torso displacement
→ exactly one rear-foot recovery placement
→ stabilization
→ pressure release or clear cut
```

推荐字段：

```yaml
start_mode: separated
contact_type: two_hand_push_or_defined_push
receiver_body_result: torso_and_shoulders_shift_backward
foot_result_count: 1
foot_result_type: rear_foot_recovery_placement
stabilization_target: early_window
release_required: true
```

强制审查：

- 首帧是否分离；
- receiver 是否只在接触后反应；
- 是否恰好一次脚步结果；
- 是否变成 hit、drag、slide 或 multi-step；
- 稳定后是否仍持续按住；
- static tail 是否超限。

禁止把“stabilize”写成无限保持。应写：

```text
After stabilization, reduce pressure or cut away; do not hold the same contact pose for multiple seconds.
```

### 5.2 Brief Impact / Recoil Compiler

目标链：

```text
separated start
→ compact initiation
→ brief contact
→ immediate upper-body recoil
→ exactly one rear-foot step
→ prompt attacker retract
→ short stabilization
```

推荐字段：

```yaml
start_mode: separated
contact_duration: brief
receiver_body_result: immediate_upper_body_recoil
foot_result_count: 1
foot_result_type: rear_foot_step
attacker_retract_required: true
prolonged_push_forbidden: true
```

强制审查：

- 首帧不得接触；
- contact onset 必须可见；
- impact 不得退化为持续 push；
- recoil 必须可读；
- foot step 必须发生在接触后；
- retract 不能替代 receiver reaction；
- stabilization 后 static tail 不得过长。

### 5.3 Pressure / Guard Clash Compiler

目标链示例：

```text
already close without completed contact
→ compact entry
→ guard compression
→ body pressure
→ skid / rebound
→ counter-readiness
→ cut mid-exchange
```

可使用：

```text
first frame already close
```

但必须同时写：

```text
not already frozen in the completed contact result
```

如果 action goal 是 existing pressure continuation，则不得把缺少 contact onset 误判为失败；review contract 必须一致。

### 5.4 Continuous Combat Compiler

继承 V1.11：

- 早接触；
- contact-beat schedule；
- 明确 actor causality；
- no idle tail；
- cut mid-exchange；
- 环境破坏必须有唯一因果。

不得使用 push/impact 的“稳定站定”作为默认结尾。

### 5.5 Knockback / Flyout Compiler

必须单独定义：

- launch cause；
- airborne onset；
- feet leaving ground；
- travel direction；
- landing / offscreen endpoint；
- camera relation；
- 不允许 ground slide 伪装 airborne flyout。

此动作族不由 Batch04 结论直接验证。

---

## 6. Timing Plan

时间表必须服务动作族，而不是使用统一模板。

### 6.1 Push Reaction 参考窗口

```text
0.00–0.20s  separated start and initiation
0.20–0.60s  readable contact
0.50–1.00s  torso displacement
0.80–1.30s  exactly one recovery placement
1.20–1.60s  stabilization
afterwards  pressure release, re-entry, or cut; no multi-second hold
```

### 6.2 Brief Impact 参考窗口

```text
0.00–0.20s  separated start and compact initiation
0.20–0.55s  brief impact
0.30–0.80s  immediate upper-body recoil
0.50–1.10s  exactly one rear-foot step
0.50–1.00s  attacker retract
1.00–1.50s  short stabilization or cut
```

注意：

- 时间文字不是物理引擎；
- 时间窗口不能替代首帧审核；
- 任何动作结果仍需完整 MP4 审片。

---

## 7. Ending Contract

每个 Prompt 必须同时定义：

```yaml
ending_state:
ending_entry_time:
ending_hold_max:
post_result_motion:
cut_strategy:
```

### 7.1 禁止模糊 ending

高风险词：

```text
stabilize
settle
hold
clear ending
readable endpoint
```

若无持续时间，它们容易产生多秒 static tail。

### 7.2 推荐写法

Push：

```text
The receiver regains balance by the early window; the attacker then reduces pressure and the shot cuts or continues with small recovery motion. Do not hold the same contact pose for the remaining seconds.
```

Impact：

```text
The attacker retracts immediately after the brief impact; the receiver completes one recovery step and remains alive with breathing and guard motion. No prolonged push and no long idle tail.
```

Continuous combat：

```text
Continue fighting through the cut; no pose-out.
```

---

## 8. 强制 Visual Audit Gate

每个高风险动作 Prompt 必须生成以下审核字段。

### 8.1 通用审核

```yaml
first_frame_state:
action_onset_visible:
contact_onset_visible:
post_contact_reaction_visible:
foot_result_required:
foot_result_count:
prolonged_contact:
static_tail_duration:
ending_contract_satisfied:
action_family_match:
```

### 8.2 first_frame_separation_audit

当 `start_mode=separated`：

```text
第一帧是否清楚分离？
```

失败即：

```text
INVALID_INITIAL_STATE_FOR_ONSET_EVALUATION
```

### 8.3 action_onset_visibility_audit

```text
是否能看到 attacker 在接触前启动？
```

### 8.4 contact_onset_readability_audit

```text
能否区分 contact 前后？
```

### 8.5 post_contact_reaction_audit

```text
receiver 的反应是否发生在 contact 后？
```

### 8.6 exactly_one_foot_result_audit

只在目标要求时使用：

```text
是否恰好一个？
是否在 contact 后？
是否变成 slide / multi-step / no-step？
```

### 8.7 prolonged_contact_audit

```text
接触是否超过动作族的目标窗口？
```

### 8.8 static_tail_duration_audit

```text
核心结果完成后，静态尾段持续多久？
```

### 8.9 action_family_routing_audit

```text
最终视频是否仍属于预定 action family？
```

例如：

- impact 变 push；
- push 变 hit；
- flyout 变 ground slide；
- recovery 变 idle pose。

---

## 9. 结果优先不等于负面堆砌

负面项只服务 P0。

推荐：

```text
No first-frame contact, no prolonged push, no multi-step retreat, no static pose-out.
```

不推荐：

- 重复几十个同义 negative；
- 先写大段禁止项再写动作；
- 用 negative 替代明确动作链；
- 把旧失败对象反复召回。

---

## 10. Reference Duty

如果使用参考图 / 视频，必须记录：

```yaml
reference_label:
duty:
forbidden_duty:
priority:
risk:
mitigation:
```

典型职责：

- identity ref：身份，不负责站位；
- architecture ref：场景结构，不负责动作；
- layout ref：几何，不负责美术；
- action video：动作节奏，不复制人物和场景；
- CTRL-CAM：镜头速度和惯性，不复制剧情。

Action-family route 不得由 Reference 自动推定。

---

## 11. Prompt Review 默认策略

用户默认审查媒体，不默认审查 Prompt。

Prompt 只在以下情况展示：

1. 连续失败；
2. action family 变化；
3. initial-state contract 变化；
4. package review 发现缺陷；
5. production route 重大变化；
6. 用户主动要求；
7. provisional calibration 规则准备进入生产。

---

## 12. Compiler 输出结构

每次编译输出：

```text
1. Action-family classification
2. Initial-state contract
3. P0 dominant result sentence
4. Actor / force / contact / reaction chain
5. Foot-result contract
6. Timing plan
7. Ending-state and duration contract
8. Composition / camera
9. Identity / environment / Reference support
10. Removed constraints
11. Compact negatives
12. Visual audit checklist
13. Risk labels
14. Human review surface
15. Production / calibration use boundary
```

---

## 13. 编译阻塞条件

出现以下任一项，不应进入 live submit：

```text
action family unresolved
initial state unresolved
contact onset not auditable
required body result missing
required foot result count missing
ending duration unspecified
static-tail audit absent
reference duties conflicting
component-level claim exceeds evidence
production Prompt imports provisional rule without human acceptance
```

状态示例：

```text
BLOCKED_ACTION_FAMILY_UNRESOLVED
BLOCKED_INITIAL_STATE_CONTRACT_MISSING
BLOCKED_ENDING_DURATION_MISSING
BLOCKED_PROVISIONAL_RULE_NOT_ACCEPTED
```

---

## 14. Batch04 解释边界

Batch04 支持：

- A01 push reaction 中存在 action-specific positive signal；
- first-frame separation、post-contact reaction、foot-result 和 static-tail audit 有必要；
- push 与 impact 应分开路由。

Batch04 不支持：

- 完整 Candidate bundle 成为 universal default；
- 任一组件独立因果证明；
- 生产 Prompt 自动更新；
- Candidate 视频 production-ready。

固定字段：

```yaml
treatment_bundle_screening: true
component_level_causal_attribution_permitted: false
bundle_supported_as_general_default: false
production_prompt_auto_update: false
```

---

## 15. Source 与应用边界

本文件是 V0.2 的替换候选。

只有人类手动应用后：

```text
active_prompt_compiler = V0.3
```

在此之前：

```text
active_prompt_compiler = 当前已应用版本
```

Codex / automation 不得：

- 直接修改 `sources/`；
- 因本候选存在就宣称已生效；
- 自动改 production Prompt；
- 自动创建 live package。

---

## 16. Final verdict

```text
PROMPT_COMPILER_V0_3_RESTRICTED_ACTION_FAMILY_CANDIDATE_READY_FOR_HUMAN_REVIEW
```
