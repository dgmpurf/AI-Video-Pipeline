# AI视频制作_Source索引与使用优先级_V1.11

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：Project Source index / replacement for V1.10  
> 版本：V1.11  
> 生成日期：2026-07-18  
> 状态：待人类审阅并手动应用  
> 应用方式：建议由用户手动替换 V1.10；Codex / automation 不得直接修改、stage、commit 或 push official `sources/`。

---

## 0. V1.11 更新结论

V1.11 在 V1.10 基础上增加三项内容：

1. 新增项目专属模式选择覆盖层：
   `AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md`
2. 将 Surface、Model、Effort、Execution Environment 从旧的 Think / Pro 标签中拆开。
3. 更新当前生产与校准状态：
   - K270M / K270O / K270Q 已证明 B3 safe/simplified 路线可 submit、query success 并下载；
   - 该结果被人工判定更接近地面滑行，不是目标中的 airborne fly-out；
   - K270S 暂停，未来等待动作参考后进入 K271A；
   - CAL-001A 已记录为 conditional pre-authorization，但执行权限仍未激活。

V1.11 不替代任何单项治理、CLI、Prompt、动作、Reference、Manifest 或 Script Source。

---

## 1. 推荐 Source 优先级

### P0：硬治理与执行边界

必须优先读取：

1. `AI视频制作_自动化治理与Source权限规则_V0.1.md`
2. `AI视频制作_自动化宏流程与授权等级_V0.2.md`
3. `dreamina_cli_help_latest.md`
4. `Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md`
5. `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
6. `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
7. `Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md`
8. `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`

P0 控制：

- Source authority；
- Codex / automation 权限；
- Dreamina canary 与 command-contract；
- submit / query / download / retry / resubmit / batch / final / lock；
- live execution 环境；
- 媒体 staging 与 Git 边界。

### P0.25：模式、模型、Effort 与执行环境

新增并读取：

- `AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md`

P0.25 只负责：

- Chat / Work / Codex / Sites 的任务路由；
- 当前可用模型选择；
- Effort / Speed；
- Local / Worktree / Cloud；
- Plan / Goal / Scheduled；
- 正式授权文本默认使用英文。

P0.25 不得覆盖 P0。

### P0.5：项目蓝图

读取：

- `AI视频制作_项目蓝图与产品化路线_V0.1.md`

### P1：Prompt、动作与失败规则

对 Prompt、镜头、动作和结果审查，按任务选择：

- `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`
- `AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `AI视频制作_动作参考视频库与审片标准_V0.1.md`
- `Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`
- 其他相关实测规则库 V1.1–V1.8。

### P2：多模态、Reference 与 Manifest

按任务选择：

- `AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md`
- 当前 reference library / rights / duty / manifest 规则；
- 当前任务 package、manifest、asset registry 和 shot record。

### P3：剧本、美术、风格与传统故事

按任务选择：

- `AI视频制作_实测规则库_V1.5_剧本美术与分镜设计增补稿.md`
- `AI视频制作_实测规则库_V1.6_分镜模板与风格词库增补稿.md`
- `AI视频制作_实测规则库_V1.7_中国传统故事与神话改编增补稿.md`
- 其他相关 script / art / style Sources。

---

## 2. 按任务的最小阅读顺序

### 2.1 创意、剧本、Prompt 路线

```text
P0 governance
→ P0.25 mode routing
→ P0.5 blueprint
→ relevant P1 / P2 / P3
→ current shot reports
```

### 2.2 Dreamina live 执行

```text
P0 governance
→ P0.25 environment selection
→ current dreamina_cli_help_latest
→ current runtime dreamina <command> -h
→ task workflow / schema
→ prompt/package/manifest/ref hashes
→ exact human authorization
```

### 2.3 视觉审查

```text
P0 final/lock boundary
→ P0.25 Chat visual-review route
→ action/reference review Source
→ downloaded media / frames / contact sheet
→ human comments
→ current shot reports
```

### 2.4 CAL-001 Prompt Calibration

```text
P0 governance and macro rules
→ P0.25 mode routing
→ Prompt Compiler
→ failure ledger / route reset
→ action/reference review
→ fixed manifest and dataset schema
→ independent review
→ human manifest acceptance
→ activation audit
```

---

## 3. 冲突规则

1. 人类当前明确授权最优先；范围更窄的授权覆盖更宽的 Source 默认。
2. P0 治理与安全覆盖 P0.25 模式路由。
3. 当前运行时 `dreamina <command> -h` 覆盖旧 CLI 文档中的命令事实。
4. 当前账号 UI 实际可用的 Surface、Model、Effort 和 Environment 覆盖过期模式名称。
5. task-specific report 只能证明其记录的任务，不自动扩展到其他任务族。
6. submit success 不等于 query/download/visual/final/lock。
7. visual success 不等于 final/lock。

---

## 4. Source 更新治理

Codex 可以：

- 读取 Source；
- 在 `reports/` 下创建 Source update recommendation 或候选草稿；
- 创建执行证据、manifest、dataset 和报告；
- 建议人类手动应用。

Codex 不得：

- 创建、修改、删除、重命名或移动 `sources/` 下的文件；
- stage、commit 或 push official Source；
- 上传或替换 ChatGPT Project Source；
- 未经人类手动应用就宣称候选 Source active。

外部校准包只能作为 adaptation input，不能原样复制为 official Source。

---

## 5. 当前 Dreamina CLI 状态

PowerShell live path：

```text
C:/Users/msjpurf/bin/dreamina.exe
```

Linux installed path：

```text
/home/ke/.local/bin/dreamina
```

当前规则：

- PowerShell CLI 是 live execution 默认路径；
- Linux CLI 仅在该环境的 login/checklogin 与 `user_credit` 成功后才可执行 live task；
- 每个 live phase 仍必须运行对应 canary 和 command help；
- CLI、模型、价格和登录态不得仅根据历史报告推断。

---

## 6. 当前 SHOT-04 R02a 状态

截至 K270R：

- 原始 B3 submit 在 K270G 失败，未创建 task；
- B3 safe/simplified 在 K270M submit 成功；
- K270O query 返回 success；
- K270Q 下载 1 个本地视频；
- 人工判断该视频主要表现为地面滑行，不符合目标中的空中击飞；
- K270R 只记录 review-artifact 授权；
- K270S 暂停，不生成帧 / contact sheet；
- 未来等待动作模仿参考后进入：
  `K271A_ACTION_REFERENCE_INTAKE_FOR_AIRBORNE_FLYOUT`。

当前边界：

```yaml
K270Q_media_status: diagnostic_ground_slide_evidence
K270S_execution: paused
new_airborne_generation: not_authorized
final_master: false
locked: false
```

---

## 7. 当前 CAL-001 状态

CAL-001A 已记录：

```yaml
authorization_language: English
authorization_type: conditional_pre_authorization
execution_authority_active: false
fixed_manifest_target_count: 84
fixed_manifest_exists: false
fixed_manifest_human_reviewed: false
credit_budget_max: 5880
credit_floor: 560
retry_count_max: 0
resubmit_count_max: 0
batch_expansion: false
final_master: false
locked: false
```

推荐准备顺序：

1. 应用 GPT-5.6 模式选择 Source 候选；
2. `CAL-001-P1_PROJECT_WIDE_PROMPT_CALIBRATION_NO_RUN_MANIFEST_AND_SCHEMA_CREATION`；
3. CAL-001-P2 独立 package / budget / permission / stop-condition 审查；
4. 人类 manifest 接受；
5. CAL-001-P3 activation-precondition audit；
6. 仅在全部条件通过后激活 CAL-001A；
7. CAL-001B 必须使用独立英文授权。

---

## 8. 维护规则

- 模式、模型、Work / Codex / Sites 变化：优先更新 P0.25 覆盖层。
- Dreamina 命令、模型、成本和登录态变化：更新对应 CLI / workflow Source。
- Prompt 规则变化：只有在跨测试族稳定证据形成后才进入 P1 Source。
- 单次生成结果、临时项目状态和未复现经验优先留在 reports，不直接升级为通用规则。
- Source Index 只负责阅读顺序、冲突和当前入口，不替代单项 Source。
