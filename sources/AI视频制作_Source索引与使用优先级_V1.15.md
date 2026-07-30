# AI视频制作_Source索引与使用优先级_V1.15

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Source index / V1.14 replacement  
> 版本：V1.15  
> 生成日期：2026-07-30  
> Official Source authority：**human user only**  
> 激活判定：**本文件被用户手动加入或替换到 ChatGPT Project Source 后即为 active；不得依赖正文中的“候选/待应用”字样判断状态。**  
> Codex / automation：不得创建、修改、stage、commit、push 或宣称已应用 Official Source。

---

## 0. V1.15 更新结论

V1.15 在 V1.14 基础上完成四项更新：

1. Rolling Current State 升级为 `AI视频制作_当前项目状态与双轨切换_V0.3.md`：
   - 当前 repository HEAD / origin/main = `2dfd67e6b6318133c0b342ebc99edb2dd32921c3`；
   - CAL-003、CAL-004、CAL-005 R1 均已完成 human final decision 并关闭；
   - 当前阶段为 Source candidate pack 已生成、等待用户手动应用与验收；
   - 所有 Provider、submit、query、download、retry、resubmit、batch、unblind、production、final、lock authority 均为 false。
2. `AI视频制作_结构化验证器与盲审冻结治理规则` 升级为 V0.2：
   - 保留 path-aware / role-aware validator、synthetic positive/negative fixtures 和盲审冻结边界；
   - 增加 schema-first、producer-bound 容器与字段路径验证；
   - 区分 pre-activation failure 与 post-activation failure；
   - 强制多次受控 sealed open 的 attempt-separated / cumulative accounting；
   - 固化 Gate precedence、跨实验复现和 setup-bounded interpretation 三条稳定治理规则。
3. 新增 `AI视频制作_动作家族校准实验综合与生产边界_V0.1.md`：
   - 保存 CAL-003 至 CAL-005 的 setup-bounded 实验综合；
   - 将 PUSH-like 更可重复、ACTION_REF_PUSH_02 的正向证据、当前 IMPACT recipes 未复现等结论保持为 provisional experimental findings；
   - 明确禁止将其解释为 Provider-wide bias、IMPACT 不可能生成或 production approval。
4. 纠正旧 Current State 中的过期状态：
   - CAL-005 已完成 controlled unblinding、condition analysis 和 human final decision；
   - mapping 已在受控合同内揭盲；
   - sealed ZIP 历史累计打开 2 次，分别属于原执行与窄恢复授权；当前 unblind authority 仍为 false；
   - main production line 继续暂停。

V1.15 不产生任何 Dreamina、Provider、live、unblind、Source write、production、final 或 lock authority。

---

## 1. 推荐 Source 优先级

### P0：硬治理、授权、验证与执行边界

必须优先读取：

1. `AI视频制作_自动化治理与Source权限规则_V0.1.md`
2. `AI视频制作_自动化宏流程与授权等级_V0.2.md`
3. `AI视频制作_正式授权序列化与完整性校验规则_V0.1.md`
4. `AI视频制作_结构化验证器与盲审冻结治理规则_V0.2.md`
5. `dreamina_cli_help_latest.md`
6. `Dreamina_CLI执行契约_V1.5_下载传输恢复与证据保全补丁.md`
7. `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
8. `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
9. `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
10. `Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
11. `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`

P0 控制：

- human-only Official Source authority；
- canonical authorization、UTF-8 serialization 与 checkpoint binding；
- Goal lifecycle、fresh authority 与 consumed/non-reusable 状态；
- submit/query/download/retry/resubmit/batch/unblind/final/lock；
- sealed mapping、blind review、freeze、controlled unblinding 与 attempt accounting；
- Dreamina CLI、direct HTTP fallback 和敏感信息边界；
- path-aware / role-aware / schema-bound validator；
- Gate precedence、跨实验复现要求和 setup-bounded interpretation；
- Git、external artifact、overwrite 和 output allowlist。

### P0.25：模式、模型、Effort 与执行环境

读取：

- `AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md`

不得覆盖 P0。

### P0.4：Rolling Current State

读取：

- `AI视频制作_当前项目状态与双轨切换_V0.3.md`

定位：

```text
rolling_current_state
replaceable_state_capsule
not_stable_rule_source
```

精确 HEAD、commit、hash、authority、subscription 和 phase 若与更新的 repository evidence 或用户当前明确陈述冲突，以最新证据为准。

### P0.5：项目蓝图

- `AI视频制作_项目蓝图与产品化路线_V0.1.md`

### P1：Prompt、动作、失败与审片规则

按任务读取：

- `AI视频制作_Prompt编译器与结果优先动作语法_V0.3.md`
- `AI视频制作_动作家族校准实验综合与生产边界_V0.1.md`
- `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md`
- `AI视频制作_动作参考视频库与审片标准_V0.1.md`
- 其他相关实测规则与当前 experiment review contract。

`动作家族校准实验综合与生产边界_V0.1` 属于 provisional evidence，不得覆盖 Prompt Compiler 或产生 production authority。

### P2：多模态、Reference 与 Manifest

- `AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`
- 当前 reference library、rights、duty、manifest、asset registry 与 package evidence。

### P3：剧本、美术、风格与传统故事

按任务读取 V1.5–V1.7 及其他相关 Sources。

---

## 2. 按任务的最小阅读顺序

### 2.1 新 Chat / 当前项目恢复

```text
P0 governance
→ 本 Source Index V1.15
→ Rolling Current State V0.3
→ latest repository evidence
→ relevant stable/provisional task Source
→ current human instruction
```

Project memory 只能辅助理解，不得独立恢复 checkpoint、SHA、submit ID、Provider 状态、sealed open count 或 authority。

### 2.2 正式授权与 live 执行

```text
exact human-approved canonical text
→ serialization verifier
→ HEAD/origin binding
→ current runtime help and access verification
→ package/ref/media hashes
→ exact operation count and stop rules
→ activation boundary
```

任何过期订阅、旧 CLI 登录态或历史积分余额都不得被当作 live authority。

### 2.3 Blind review / freeze / unblind

```text
canonical media technical PASS
→ randomized blind package + commitment + sealed package
→ isolated complete-MP4 blind review
→ byte-identical freeze
→ fresh controlled-unblinding authorization
→ exactly bounded sealed access
→ condition analysis
→ human final decision
→ cross-experiment synthesis
```

Freeze、unblind、condition analysis、human final decision 是不同阶段，不得自动串联授权。

### 2.4 Source 更新

```text
repository evidence
→ Codex read-only Source Update Evidence Pack in reports/
→ ChatGPT Source synthesis
→ human review
→ human manual Project Source upload/replacement
→ post-application verification
```

Codex 不得写 `sources/`，也不得根据文件存在自行宣称 Project Source 已应用。

---

## 3. Gate、复现与解释优先级

以下规则作为 V1.15 的稳定治理入口：

1. 单个 favorable sample、median uplift 或 directional delta 不得覆盖失败的 pre-registered family/condition Gate。
2. Prompt、reference 或 route 在自身 Gate 通过且在 bounded comparable conditions 下完成跨实验复现前，不得提升为 stable production guidance。
3. Action-family calibration 结论必须保持 setup-bounded；除非另有证据，不得声称 Provider-wide、model-wide 或 universal causality。

实验性动作结论仍由 `动作家族校准实验综合与生产边界_V0.1` 管理。

---

## 4. 冲突解决

```text
current explicit human instruction
> P0 governance
> current runtime help/access facts
> latest repository evidence
> Rolling Current State
> stable task Source
> provisional experiment findings
> Project memory
```

任何低优先级内容都不得创造 live、unblind、Source write、production、final 或 lock authority。

---

## 5. V1.15 人工应用图

用户手动应用时：

1. 用 V1.15 替换 Source Index V1.14；
2. 用 Rolling Current State V0.3 替换 V0.2；
3. 用 Validator/Governance V0.2 替换 V0.1；
4. 新增 `动作家族校准实验综合与生产边界_V0.1`；
5. 保留 Prompt Compiler V0.3、Dreamina CLI V1.2–V1.5、正式授权、自动化治理及其他稳定 Sources；
6. 不因即梦订阅结束而删除 CLI 治理文件；它们仍控制未来重新订阅或恢复 access 后的执行；
7. 应用后通过 Project Source 文件清单核验，不通过正文中的“候选/待应用”字样判断 active 状态。

---

## 6. 当前证据锚点

```yaml
repository_head: 2dfd67e6b6318133c0b342ebc99edb2dd32921c3
origin_main: 2dfd67e6b6318133c0b342ebc99edb2dd32921c3
head_origin_aligned: true
synthesis_commit_message: synthesize(cal): prepare CAL003-CAL005 source evidence
synthesis_report: reports/CAL003_CAL004_CAL005_CROSS_EXPERIMENT_SYNTHESIS_AND_SOURCE_UPDATE_EVIDENCE_PACK.md
source_evidence_directory: reports/source_update_drafts/CAL003_CAL004_CAL005_SYNTHESIS_V0_1
```

本节属于 Rolling evidence anchor，不构成永久技术规律。
