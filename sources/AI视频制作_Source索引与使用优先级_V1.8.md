# AI视频制作_Source索引与使用优先级_V1.8

版本：V1.8 Draft  
来源：K244S Source synthesis  
状态：Source 索引草案，需人类手动确认后进入 `sources/`

## 0. 本版更新目的

V1.8 在既有 Source 索引基础上增加 K244S 之后的新规则入口：

- 失败台账与路线重置规则
- Prompt Compiler V0.2
- 自动化宏流程 V0.2
- 动作参考视频库与审片标准
- SHOT-04 R02 的双人近身战斗失败经验

## 1. 推荐 Source 优先级

### P0：硬治理与执行边界

1. `AI视频制作_自动化治理与Source权限规则_V0.1.md`
2. `AI视频制作_自动化宏流程与授权等级_V0.2.md`
3. `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
4. `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
5. `Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
6. `dreamina_cli_help_latest.md`

### P1：Prompt 与动作规则

1. `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
2. `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
3. `AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
4. `AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
5. `AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
6. `AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`

### P2：多模态、IP 安全、参考体系

1. `AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
2. `AI视频制作_动作参考视频库与审片标准_V0.1.md`
3. `DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`

### P3：剧本、美术、传统故事、风格扩展

保留既有 V1.3–V1.7 等规则库，按具体任务需要读取。

## 2. K244S Evidence Pack 的地位

K244S 文件不是官方 Source。  
它们是 Source 合成的证据输入。

可作为证据读取：

- failure ledger
- success ledger
- prompt outcome dataset
- prompt archive
- review excerpts
- root cause taxonomy
- macro-run lessons
- source update candidates
- action reference plan

但 Codex 不得直接把 K244S 文件复制到 `sources/`。

## 3. 新增工作流建议

### 3.1 失败/成功周期升级

每完成一个重要 shot 阶段，或出现连续失败，应生成：

```text
failure ledger
success ledger
prompt outcome dataset
source update candidates
```

### 3.2 用户默认审查对象

默认：

```text
用户审图片/视频
ChatGPT/Codex 内部审 prompt/package/manifest
```

prompt 给用户看的触发条件：

- 连续失败
- 核心方向变化
- package review 阻塞
- 用户主动要求

### 3.3 一键式流程定义

一键式 = gated macro-run，不是无限自动化。

必须保留：

- Source preflight
- package review
- human authorization
- submit/query/download 分离
- review artifact
- human visual review
- final/lock 人类确认

## 4. SHOT-04 R02 当前主线状态

截至 K244S：

```text
SHOT-04 R02 当前路线：near-wall guard-clash text2video
K243V：no-submit text2video package ready
K244：package review pass with high-risk notes
K245：尚未 submit，等待人类 one-submit-only 授权
final_master=false
locked=false
```

## 5. 冲突处理

如果本索引与较旧索引冲突：

- Source 治理以 P0 硬治理文件为准。
- Dreamina 参数以当前 live help / official help 校正版为准。
- SHOT-04 R02 的失败路线处理以 V1.12 和 Prompt Compiler V0.2 为准。
- Codex 不得自行解释为可修改 Source。

## 6. 推荐使用方式

对 Codex：

```text
先读 Source 索引
再读 P0 治理/宏流程
再读 Prompt Compiler
再读对应动作规则
最后读 task-specific reports/evidence
```

对 ChatGPT：

```text
Pro Extended 用 K244S evidence pack 合成 Source
Think 用于常规 K-phase 判断
Pro 用于视觉审核和重大路线选择
```
