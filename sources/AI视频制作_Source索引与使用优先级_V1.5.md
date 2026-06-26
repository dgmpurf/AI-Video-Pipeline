# AI视频制作_Source索引与使用优先级 V1.5

> 项目：AI视频制作  
> 类型：Project Source 总索引 / 调用优先级 / 使用说明  
> 版本：V1.5  
> 生成日期：2026-06-26  
> 用途：在 V1.4 索引基础上，追加 V1.11 连续战斗动作密度与环境破坏因果规则，并明确 Codex 本地 `sources/` 只读使用规则。  
> 说明：本文件不是新增 prompt 规则库，而是当前 Source 体系的导航文件。它不替代 V1.1–V1.11、Seedance V0.3、Dreamina CLI 工作流、DreaminaBatcher schema、dreamina_cli_help / latest help，也不替代当前本地 `dreamina <command> -h`。

---

## 0. V1.5 更新结论

V1.5 在 V1.4 基础上新增一类内容层规则：

```text
AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
```

新增原因：

```text
SHOT-03-V003 实测确认：
1. 仅简化空间并不能保证战斗成功。
2. 动作 prompt 如果缺少早接触、contact beat 数量、演员因果、环境破坏因果和尾段不停手，容易生成腿部空走、低冲击、错误裂口和 idle tail。
3. Codex package review 只能验证文件结构、引用、参数和安全边界；动作类 prompt 还必须通过 ChatGPT 内容审核。
4. 本地 speed-up 只适合内容结构已成立但节奏略慢的片段，不能修复 contact 缺失、破坏因果错误或尾段停手。
```

本版同时明确：

```text
Codex 可读取本地 sources/ 作为参考；
除非人类明确单独授权，Codex 不得新增、修改、删除、重命名、移动或 stage sources/ 内任何文件。
正式 ChatGPT Project Source 更新文件由 ChatGPT 生成，用户手动上传。
```

---

## 1. 当前 active source 应包括

```text
AI视频制作_实测规则库_V1.1.md
AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md
AI视频制作_实测规则库_V1.3_外部案例观察与关键帧规则增补稿.md
AI视频制作_实测规则库_V1.4_外部知识库与商业视觉模板增补稿.md
AI视频制作_实测规则库_V1.5_剧本美术与分镜设计增补稿.md
AI视频制作_实测规则库_V1.6_分镜模板与风格词库增补稿.md
AI视频制作_实测规则库_V1.7_中国传统故事与神话改编增补稿.md
AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md
AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md
AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md
AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md
AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
dreamina_cli_help.md
dreamina_cli_help_latest.md
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
```

如果本地 `sources/` 中暂时缺少其中某个文件，以 ChatGPT Project Source 或用户提供的最新文件为准；如果执行层命令事实冲突，以当前本地 `dreamina <command> -h` 为准。

---

## 2. 总优先级规则

## 2.1 执行层优先级

Dreamina CLI 的真实执行能力，以当前本地命令输出为最高事实源：

```text
当前本地 dreamina <command> -h
> dreamina_cli_help_latest.md
> dreamina_cli_help.md
> Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
> Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
> Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
> DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
> 其他通用工作流 Source
```

V1.11 是内容 / prompt 规则，不是 CLI 合约。  
V1.11 不得覆盖 duration、ratio、model_version、image count、submit/query/download 等命令事实。

## 2.2 内容创作与 prompt 规则优先级

对战斗 / 动作 / 武打 / 环境交互 prompt，建议调用：

```text
Source Index / task router
> V1.11 连续战斗动作密度与环境破坏因果规则
> V1.2 动作 / 打击感 / hit-stop / fight physics
> V1.9 空间调度 / 角色站位 / 脚落地
> V1.10 / V1.10.1 场景锚点 / 视角 / CTRL-CAM / 短硬 prompt
> V1.8 多模态参考职责 / IP 安全
> Seedance V0.3 三层描述 / Composition Matrix
> 旧项目规则和一般美术分镜规则
> 外部未验证教程
```

对非战斗类镜头，可跳过 V1.11，按场景、角色、风格、镜头目标选择对应规则。

---

## 3. V1.11 的调用条件

必须在以下任务前读取 V1.11：

- SHOT-03 V004 或后续 combat package。
- 任何快速徒手 / 拳脚 / 冷兵器连续攻防 prompt。
- 任何涉及建筑、道具、栏杆、木门、瓦片、柱子破坏的打斗 prompt。
- 任何结尾可能变成 pose / readable endpoint 的动作 prompt。
- 任何想用本地 speed-up 修节奏的片段判断。
- 任何以腿部、脚步、滑步、扫踢、失衡为重点的动作镜头。

不应只依赖 V1.11 的场景：

- 非战斗纯环境镜头。
- image2image 角色资产。
- Dreamina 命令语法。
- IP / 参考图安全。
- 多模态 reference pack duty。
- final edit lock / final_master 政策。

---

## 4. 新增流程门禁：动作 prompt 内容审核

对 combat/action prompt，进入 live submit 前必须满足：

```text
codex_package_review=passed
chatgpt_prompt_content_audit=passed
human_submit_authorization=true
```

其中：

- Codex package review：检查 JSON/CSV、manifest、reference path、settings、`final_master=false`、`locked=false`、no media staged 等技术结构。
- ChatGPT prompt content audit：检查动作密度、contact beat、演员因果、环境破坏因果、尾段不停手、脸部和身份风险。
- Human submit authorization：明确授权 canary / preflight / exactly one submit。

Codex package review passed 不等于 prompt 内容可提交。

---

## 5. V1.11 的核心检查清单

每个 combat prompt 至少应能回答：

```text
0.15-0.30 秒内谁和谁发生第一次接触？
5 秒内有几个清晰 contact beats？
每个 contact beat 的攻击路径、接触点、防守反应、脚步结果和反弹是什么？
最后 0.8 秒是否仍在攻防？
如果建筑损坏，谁撞到了哪里，裂口/碎片从哪里出现，何时出现？
是否用了明确角色名，而不是“一个角色/另一个角色”？
是否有过长腿部空走或 setup？
是否有 readable endpoint / clear ending / pose-out 风险？
```

不能回答，则不应进入 live submit。

---

## 6. 与既有 Source 的关系

### 6.1 与 V1.2 的关系

V1.11 补充 V1.2 的动作、变身、运镜、打击感规则，进一步细化“连续 combat 的接触节奏和因果链”。

### 6.2 与 V1.8 的关系

V1.8 解决多模态参考职责和 IP 安全；V1.11 解决动作本体结构。  
参考图职责正确并不代表动作 prompt 成功。

### 6.3 与 V1.9 的关系

V1.9 处理空间调度、远近站位、落地位置；V1.11 强调在空间清楚的基础上还必须保持 contact density。

### 6.4 与 V1.10 / V1.10.1 的关系

V1.10 / V1.10.1 处理场景锚点、视角、短硬 prompt、CTRL-CAM；V1.11 强调场景和镜头清楚之后，战斗动作仍需可数 contact schedule。

### 6.5 与 Dreamina CLI 文件的关系

V1.11 不提供 CLI 命令事实，不判断实际可执行参数。  
提交、查询、下载、duration、ratio、resolution、model_version、poll、reference 数量等仍以执行层 source 和当前本地 help 为准。

---

## 7. Codex 本地 sources/ 只读规则

对 Codex 任务：

```text
G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/
```

是只读本地参考库。

Codex 可以：

- 读取 sources/ 理解项目规则。
- 用 sources/ 校验 prompt / package / workflow。
- 在 report 中记录 source update recommendation。

Codex 不可以，除非用户单独明确授权：

- 在 sources/ 新增文件。
- 修改 sources/ 文件。
- 删除 sources/ 文件。
- 重命名 / 移动 sources/ 文件。
- stage sources/ 文件。
- 把 draft 当作 live Project Source。

Source 更新草稿应写在任务指定位置，例如：

```text
reports/source_update_drafts/
```

正式 ChatGPT Project Source 文件应由 ChatGPT 生成，用户手动上传到 Project Source。

---

## 8. 何时更新 Source

建议更新 Source 的依据：

- 多次真实项目生成失败 / 成功产生稳定规律。
- 人审和 prompt 审核均确认同一类问题反复出现。
- 平台能力 / CLI help / model contract 改变。
- 某条规则已经能指导下一版生成并显著降低失败风险。

不建议更新 Source 的情况：

- 单次偶然失败，尚未形成规律。
- 只来自外部教程，未在项目中验证。
- 与当前官方 CLI help 冲突。
- 只是某个 shot 的一次性美术偏好。

V1.11 属于 B 级项目实测规则：已由 SHOT-02 / SHOT-03 多轮实测支持，但尚未跨项目验证为 A 级通用规则。

---

## 9. 对 SHOT-03 V004 的直接要求

后续 SHOT-03 V004 package 之前必须执行：

1. 读取 V1.11。
2. 生成 actual manual prompt。
3. 由 ChatGPT 审核 prompt 内容。
4. Codex 再做 package review。
5. 人类明确授权 submit。
6. 才能 Dreamina canary / preflight / exactly one submit。

V004 prompt 不能复用 V003 的时间结构。  
V004 必须包含 contact-beat schedule、无 idle tail、演员因果、环境破坏因果或明确移除破坏。

---

## 10. Final Verdict

```text
SOURCE_INDEX_V1_5_READY_WITH_V1_11_COMBAT_DENSITY_RULES
```
