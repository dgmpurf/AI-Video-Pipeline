# AI视频制作_Source索引与使用优先级 V1.3

> 项目：AI视频制作  
> 类型：Project Source 总索引 / 调用优先级 / 使用说明  
> 生成日期：2026-06-18  
> 用途：在 V1.2 索引基础上，追加 Dreamina CLI 执行契约 V1.2。  
> 说明：本文件不是新增 prompt 规则库，而是当前 Source 体系的导航文件。它不替代 V1.1–V1.10.1、Seedance V0.3、Dreamina CLI V1.1、DreaminaBatcher schema V1.1、dreamina_cli_help.md，也不替代当前本地 `dreamina <command> -h`。

---

## 0. V1.3 更新结论

V1.3 在 V1.2 索引基础上新增执行层补丁：

```text
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
```

新增原因：

```text
PHASE_K2B 审计确认：
当前本地 Dreamina CLI image2video + seedance2.0_vip 支持 duration=4–15s。
SHOT-02-V002 使用 duration=2 不符合当前 CLI image2video 执行契约。
网页端可能支持 1–2 秒视频，但不能直接等同于 CLI 能力。
submit_id / querying 不能单独证明任务参数合法。
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
Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
dreamina_cli_help.md
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
```

---

## 2. 总优先级规则

### 2.1 内容创作与 Prompt 规则优先级

```text
本项目实测规则 V1.1 / V1.2 / V1.9 / V1.10 / V1.10.1
> 本项目 Source 增补 V1.3–V1.8
> Seedance V0.3 综合工作流手册
> 外部教程 / 外部案例 / GitHub prompt 案例
> 纯理论 / 未验证经验
```

### 2.2 Dreamina CLI / Batcher 执行层优先级

```text
当前本地 dreamina <command> -h
> dreamina_cli_help.md
> Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
> Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
> DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
> 其他通用工作流 Source
```

如果命令参数冲突，以当前本地 CLI help 为准。

---

## 3. 新增任务类型：Dreamina CLI live submit / execution contract

当用户要执行真实 Dreamina 任务，尤其是：

```text
text2video
image2video
frames2video
multiframe2video
multimodal2video
image2image
text2image
```

必须优先读取：

```text
Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
dreamina_cli_help.md
Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
```

必须执行 command-contract preflight：

```text
1. dreamina executable path
2. dreamina version
3. selected command help
4. task_type
5. model_version
6. duration
7. video_resolution
8. ratio rule
9. input count
10. input paths
11. command_contract_valid
```

没有通过预检，不允许 live submit。

---

## 4. Web 与 CLI 差异规则

如果用户说：

```text
网页端可以 1 秒
网页端可以 2 秒
网页端有某个控制项
网页端任务可见 / 不可见
```

不得直接转换为 CLI 参数。

必须判断：

```text
这是 Web 能力，还是 CLI 能力？
当前本地 CLI help 是否支持？
如果不支持，是否改为 manual_web_run？
是否改为 CLI 合法最短时长 + 剪辑裁短？
```

---

## 5. SHOT-02-V002 后续执行规则

当前结论：

```text
SHOT-02-V002 duration=2 CLI image2video 包：
command-contract-invalid
不得继续用当前 CLI image2video 提交
```

推荐：

```text
SHOT-02-V002-CLI4
task_type=image2video
model_version=seedance2.0_vip
duration=4
video_resolution=720p
ratio omitted
exactly one --image
final edit target = 1–2s
```

如果坚持 1–2 秒：

```text
走 manual_web_run，并明确登记为网页端手动运行，不伪装为 CLI run。
```

---

## 6. live submit 报告最低字段

任何 live submit 报告必须包含：

```text
command_contract_preflight
dreamina_executable_path
dreamina_version
exact submit command
submit response status
submit_id
logid
credit_count
fail_reason if any
exact query command
query_result status
download happened
output path if downloaded
validation result if downloaded
```

新增硬规则：

```text
submit_id alone is not enough.
querying alone is not enough.
```

---

## 7. 当前 Source 锁版建议

当前版本：

```text
Source Index V1.3
规则库 V1.1–V1.10.1
Dreamina CLI 执行契约 V1.2
工作流手册 Seedance V0.3
执行层 Dreamina CLI V1.1
Batcher schema V1.1
CLI help 2026-06-07 / 本地 help 实时优先
```

建议状态：

```text
可以继续真实项目测试。
后续若 Dreamina CLI 更新，必须重新跑 K2B 类审计。
```

---

## 8. 一句话总结

```text
V1.3 索引的核心更新是：把 Dreamina CLI 执行契约 V1.2 纳入 active source。后续所有 live submit 都必须先过当前 CLI help 的命令契约预检；网页端能力不能直接等同于 CLI 能力。
```
