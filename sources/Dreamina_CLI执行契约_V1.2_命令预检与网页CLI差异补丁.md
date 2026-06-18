# Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁

> 项目：AI 视频制作 / Dreamina CLI 执行层 Source  
> 类型：执行契约补丁 / 命令预检规则 / Web 与 CLI 能力差异规则  
> 建议合并位置：`Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md` 与 `DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md` 之后  
> 生成依据：`PHASE_K2B_DREAMINA_CLI_EXECUTION_CONTRACT_AUDIT.md`，本地 Dreamina CLI help 审计  
> 审计日期：2026-06-18  
> 证据等级：执行层 A 级事实（基于当前本地 CLI help / version）；若本地 CLI 更新，必须重新审计。  
> 注意：本文件不替代 `dreamina_cli_help.md`。执行层最高事实来源仍然是当前本地 `dreamina <command> -h`。

---

## 0. 本次补丁结论

本次补丁解决一个执行层根问题：

```text
CLI 返回 submit_id 或 querying，并不等于任务参数一定符合当前 CLI 命令契约。
网页端支持的能力，也不能直接当作 CLI 能力。
```

本次审计确认：

```text
当前本地 CLI：
C:\Users\msjpurf\bin\dreamina.exe

dreamina version:
46b5b0e-dirty

当前 CLI image2video + seedance2.0_vip 支持：
duration = 4–15 秒
video_resolution = 720p 或 1080p
ratio 不传，由输入图片推断
input = exactly one --image
```

因此：

```text
SHOT-02-V002 使用 image2video + seedance2.0_vip + duration=2
在当前 CLI 下属于 command-contract-invalid。
```

---

## 1. 执行层优先级

执行命令、参数、字段映射时，优先级为：

```text
当前本地 dreamina <command> -h
> dreamina_cli_help.md
> 本文件 Dreamina_CLI执行契约_V1.2
> Dreamina_CLI工作流与执行规范_V1.1
> DreaminaBatcher_manifest_schema_V1.1
> 其他通用视频工作流 Source
```

如果本文件与当前本地 CLI help 冲突，以当前本地 CLI help 为准。

---

## 2. Web 能力 ≠ CLI 能力

必须明确区分：

```text
Dreamina Web 端能力
Dreamina CLI 能力
Dreamina API / Batcher 能力
```

禁止默认推导：

```text
网页端支持 1 秒视频
→ CLI image2video 也支持 1 秒

网页端可以选择某个视频时长
→ CLI 对同一个 model_version 也允许同样 duration

网页端能看到任务
→ CLI session / account / default dialog 一定一致
```

正确写法：

```text
如果某能力来自网页端，必须记录为 Web assumption / manual_web_run assumption。
如果要通过 CLI 执行，必须先用当前 dreamina <command> -h 做命令契约预检。
```

---

## 3. 当前本地 CLI 视频命令时长契约

### 3.1 image2video

```text
输入：
exactly one --image

ratio：
不传；由输入图片推断

支持模型与时长：
3.0 / 3.0fast / 3.0pro / 3.0_fast / 3.0_pro：3–10 秒
3.5pro / 3.5_pro：4–12 秒
seedance2.0 / seedance2.0fast / seedance2.0_vip / seedance2.0fast_vip：4–15 秒

分辨率：
seedance2.0_vip：720p 或 1080p
其他模型：720p
```

关键结论：

```text
当前 CLI 下，image2video 不支持 duration=1 或 duration=2。
```

---

### 3.2 text2video

```text
输入：
prompt only

支持模型：
seedance2.0 / seedance2.0fast / seedance2.0_vip / seedance2.0fast_vip

duration：
4–15 秒

ratio：
显式可传：1:1 / 3:4 / 16:9 / 4:3 / 9:16 / 21:9
```

关键结论：

```text
当前 CLI 下，text2video 不支持 duration=1 或 duration=2。
```

---

### 3.3 frames2video

```text
输入：
--first
--last

ratio：
不传；由 first frame 推断

支持模型与时长：
3.0：3–10 秒
3.5pro：4–12 秒
seedance2.0 family：4–15 秒
```

关键结论：

```text
当前 CLI 下，frames2video 不支持 duration=1 或 duration=2。
```

---

### 3.4 multimodal2video

```text
输入：
--image <= 9
--video <= 3
--audio <= 3
至少有一个 image 或 video

支持模型：
seedance2.0 / seedance2.0fast / seedance2.0_vip / seedance2.0fast_vip

duration：
4–15 秒

ratio：
显式可传
```

关键结论：

```text
当前 CLI 下，multimodal2video 不支持 duration=1 或 duration=2。
```

---

### 3.5 multiframe2video

```text
输入：
2–20 张图片

duration：
单段 0.5–8 秒
总时长 >= 2 秒

限制：
不支持 model_version 和 video_resolution override。
ratio 从第一张图推断。
```

注意：

```text
multiframe2video 的 0.5–2 秒 segment 不是 image2video 合同。
不能因为 multiframe2video 支持短 segment，就认为 image2video / seedance2.0_vip 支持 1–2 秒。
```

---

## 4. 提交前 Command-Contract Preflight

所有 live submit 前，必须通过命令契约预检。

最低记录字段：

```text
dreamina_executable_path
dreamina_version
task_type
command_help_checked_at
model_version
duration
video_resolution
ratio_rule
input_count
input_paths_exist
command_contract_valid
command_contract_notes
```

预检必须回答：

```text
1. 当前使用的是哪个 dreamina.exe？
2. dreamina version 是什么？
3. 当前 task_type 对应的 help 是否已经读取？
4. model_version 是否允许？
5. duration 是否在当前 CLI 支持范围内？
6. video_resolution 是否允许？
7. ratio 是否允许 / 是否必须省略？
8. 输入数量是否符合命令要求？
9. 所有本地路径是否存在？
10. 本次命令是否符合当前 CLI help？
```

如果 `command_contract_valid=false`：

```text
不得 submit。
不得记录为 submitted。
不得通过 query_result 修正这个状态。
```

---

## 5. submit_id / querying 不再作为唯一有效凭证

新增硬规则：

```text
submit_id alone is not enough.
querying alone is not enough.
```

必须同时记录：

```text
1. command_contract_valid=true
2. exact submit command
3. submit response status
4. submit_id
5. logid
6. credit_count
7. fail_reason / parameter error if any
8. query_result status
```

如果 submit response 已经暴露出参数错误或 gen_status=fail，即使后续 query_result 返回 querying，也不得把任务视为有效生成任务。

---

## 6. 状态字段规范

推荐新增/统一以下状态：

```text
package_ready_no_submit
command_contract_invalid
submit_blocked_by_preflight
submitted_querying
still_querying
success_downloaded
submitted_failed_no_retry
manual_web_run_required
manual_web_run_recorded
```

### 6.1 command_contract_invalid

适用：

```text
包已经生成，但参数不符合当前 CLI help。
```

必须记录：

```text
invalid_reason
do_not_submit_via_cli=true
manual_web_possible=true/false
recommended_fix
```

示例：

```text
status=command_contract_invalid
invalid_reason=duration=2 is not supported by current CLI image2video seedance2.0_vip; supported range is 4-15s
do_not_submit_via_cli=true
manual_web_possible=true
```

---

## 7. 短动作镜头的执行策略

如果创作目标是 1–2 秒动作高光，有三种路线：

### 路线 A：CLI 合法最短时长 + 后期剪辑

```text
用 CLI 支持的最短合法时长生成。
例如 image2video + seedance2.0_vip 当前最短 4 秒。
最终剪辑只取 1–2 秒高光段。
```

推荐用于：

```text
稳定生产
可追踪任务
自动化流程
Codex / Batcher pipeline
```

### 路线 B：manual_web_run

```text
如果 Dreamina Web 端已验证支持 1–2 秒，则使用网页端手动运行。
必须登记为 manual_web_run，不能伪装成 CLI run。
```

必须记录：

```text
web account
web session / project if available
manual upload refs
manual settings
web task id / screenshot / download path
human operator
```

### 路线 C：multiframe2video 短段测试

```text
如果有首尾帧或多帧关键姿态，可以用 multiframe2video 的短 segment。
但它不支持 model_version / video_resolution override。
它不是 image2video 的替代合同。
```

---

## 8. SHOT-02-V002 处理结论

本次审计后：

```text
SHOT-02-V002 duration=2 CLI package：
保留为 planning / prompt artifact
标记为 command-contract-invalid
不得通过当前 CLI image2video 提交
```

推荐新包：

```text
SHOT-02-V002-CLI4
task_type=image2video
model_version=seedance2.0_vip
duration=4
video_resolution=720p
ratio omitted
input exactly one --image
final_edit_target=1–2s
```

---

## 9. 给 Codex 的 live submit 最小要求

任何后续 live submit prompt 必须要求输出：

```text
1. command_contract_preflight result
2. exact dreamina executable path
3. dreamina version
4. exact submit command used
5. submit response raw summary
6. submit_id
7. logid
8. credit_count
9. exact query command used
10. query_result status
11. whether download happened
12. output path if downloaded
13. validation result if downloaded
14. final verdict
```

如果缺少 `command_contract_preflight` 或 `submit response status`，该执行报告不完整。

---

## 10. 一句话总结

```text
网页端支持的能力不能自动等同于 CLI 能力；CLI 提交前必须以当前 dreamina <command> -h 为准做命令契约预检。submit_id 和 querying 只是任务追踪信息，不是参数合法性的证明。
```
