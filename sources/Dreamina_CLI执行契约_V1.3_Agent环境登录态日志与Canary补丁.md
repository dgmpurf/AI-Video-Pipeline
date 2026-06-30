# Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁

> 项目：AI 视频制作 / Dreamina CLI 执行层 Source  
> 类型：执行契约补丁 / Agent-Codex 环境登录态与日志排查规则 / Canary 规则  
> 建议合并位置：`Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md` 之后  
> 生成依据：SHOT-02-V009 Codex Dreamina CLI logger/auth 真实故障复盘、用户提供《即梦 CLI 体验指南》、2026-06-21 本地 `dreamina -h` 与子命令 `-h` handoff。  
> 证据等级：执行层 A/B 混合。CLI 参数事实以当前本地 help 为 A 级事实；Agent/Codex 登录态与日志规则来自本项目真实故障复盘，作为 B 级工程规则，后续可随 CLI 更新修订。  
> 注意：本文件不替代 `dreamina_cli_help_latest.md`，也不替代当前运行时 `dreamina <command> -h`。执行层最高事实来源仍然是当前本地 CLI help。

---

# 0. 本次补丁结论

本次补丁解决 V1.2 未覆盖的一类问题：

```text
同一台机器上，人类终端可以使用 Dreamina CLI，但 Agent/Codex 运行 Dreamina CLI 时可能失败。
失败原因可能不是 prompt、不是远端任务、不是账户权益，而是本地执行身份、日志目录、登录态上下文不一致。
```

本次 SHOT-02-V009 复盘确认：

```text
1. 远端任务已成功，人工 Git Bash 能 query/download。
2. Codex 曾在真正 query/download 前被本地 logger 初始化阻断：
   ~/.dreamina_cli/logs/dreamina.log.<hour> Access is denied。
3. ACL / owner 修复后，logger Access denied 消失。
4. 随后暴露第二层问题：CodexSandboxOnline 缺少有效 Dreamina 登录态，user_credit 失败。
5. 通过 Codex 执行上下文完成 OAuth headless login + checklogin 后，Codex user_credit 成功。
```

一句话：

```text
Dreamina CLI 在 Agent/Codex 环境下的可用性，必须用 canary 验证；不能因为人类终端可用，就默认 Codex 可用。
```

---

# 1. 执行层优先级补丁

执行命令、参数、字段映射时，优先级为：

```text
当前本地 dreamina <command> -h
> dreamina_cli_help_latest.md
> Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md
> Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md
> Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md
> DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md
> 其他通用视频工作流 Source
```

体验指南、release note、安装脚本提示用于排查和更新，不直接覆盖本地 `dreamina version` 与 `dreamina <command> -h`。

---

# 2. CLI 更新优先排查规则

根据用户提供《即梦 CLI 体验指南》，排查 Dreamina CLI 问题时优先执行：

```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

更新后必须重新打开终端或确认 PATH 生效，再记录：

```text
dreamina version
dreamina -h
dreamina <subcommand> -h
```

重要注意：

```text
安装脚本 release note 可能与本地 dreamina version 输出不一致。
如果安装脚本提示已更新，但 dreamina version 仍显示旧 commit/build_time，仍以本地 version/help 实测输出为执行事实。
```

本项目 2026-06-21 实测：

```text
安装脚本重新下载 dreamina.exe 后，本地 version 仍为：
46b5b0e-dirty / commit 46b5b0e / build_time 2026-06-03T19:39:25Z。
```

因此：

```text
不得只根据网页/指南版本号推断本地支持能力；
必须保存本地 version/help 快照。
```

---

# 3. Agent/Codex 执行身份规则

Dreamina CLI 本地状态存放在用户主目录：

```text
~/.dreamina_cli/tasks.db
~/.dreamina_cli/logs/
~/.dreamina_cli/version.json
~/.dreamina_cli/dreamina/SKILL.md
```

Agent/Codex 可能不是人类终端同一 Windows 身份。

本项目实测身份示例：

```text
人类终端：DESKTOP-0K9UPOV\msjpurf
Codex：desktop-0k9upov\codexsandboxonline
Codex 相关组：DESKTOP-0K9UPOV\CodexSandboxUsers
```

规则：

```text
1. 人类 Git Bash / PowerShell 可用，不等于 Codex 可用。
2. Codex 能运行 dreamina version，不等于 Codex 已登录。
3. Codex 必须通过 dreamina user_credit 才能视为账户态可用。
4. 如果 Codex 需要长期执行 Dreamina，推荐由 Codex 执行上下文完成 login --headless + checklogin。
5. 不要让 Codex 随意运行 logout / relogin；这可能破坏人类终端可用的登录态。
```

---

# 4. 必须执行的 Canary 规则

任何 Codex/Agent Dreamina live work 前，必须先跑 canary：

```text
dreamina version
dreamina user_credit
```

可选附加：

```text
whoami
whoami /groups
```

Canary 通过标准：

```text
1. dreamina version 成功；
2. 没有 initialize file logger / Access is denied；
3. dreamina user_credit 成功返回 user_id、vip_level、total_credit；
4. 没有“未检测到有效登录态”；
5. 没有 auth / login / permission failure。
```

Canary 状态枚举：

```text
CODEX_DREAMINA_CLI_CANARY_OK
CODEX_DREAMINA_CLI_LOGGER_ACCESS_DENIED
CODEX_DREAMINA_CLI_LOGIN_OR_AUTH_FAILED
CODEX_DREAMINA_CLI_LOGIN_PENDING_OR_FAILED
CODEX_DREAMINA_CLI_UNKNOWN_FAILURE
```

如果不是 `CODEX_DREAMINA_CLI_CANARY_OK`：

```text
不得 submit。
不得 query_result。
不得 download。
不得 batch。
不得把失败记为远端生成失败。
```

---

# 5. Logger Access Denied 分类规则

如果出现：

```text
initialize logs failed
initialize file logger failed
open ~/.dreamina_cli/logs/dreamina.log...
Access is denied
```

必须记录为：

```text
local_cli_logger_blocked
```

不是：

```text
remote_generation_failed
prompt_failed
model_failed
submit_failed_no_retry
```

排查项：

```text
1. whoami / whoami /groups
2. ~/.dreamina_cli owner
3. ~/.dreamina_cli/logs owner
4. dreamina.log* owner / ACL / inherited permissions
5. 是否有 Deny entries
6. 人类终端与 Codex 终端是否同一身份
7. 是否存在旧小时日志文件由不同身份创建
8. 是否存在管理员 PowerShell、人类终端、Codex 混用同一目录
```

推荐安全修复：

```text
1. 先停止 Dreamina CLI 相关进程。
2. 对 ~/.dreamina_cli 执行 takeown / icacls，统一 owner 与继承。
3. 只在必要时重建 logs 目录；不要删除 auth/session/token 状态。
4. 修复后先跑 canary，不直接跑真实任务。
```

---

# 6. 登录态 / Auth 失败分类规则

如果 logger 已经不报错，但 Codex 执行：

```text
dreamina user_credit
```

返回：

```text
未检测到有效登录态，请先执行 dreamina login
```

或 exit code 1 无有效账户信息，则记录为：

```text
local_cli_login_state_missing_for_agent
```

原因可能包括：

```text
1. Codex 与人类终端不是同一 Windows 身份；
2. 登录态文件存在但绑定用户上下文；
3. 文件 ACL 可读但 token/cookie/session 无法被 Codex 身份使用；
4. Codex 需要自己的 OAuth Device Flow 登录。
```

修复流程：

```text
dreamina login --headless
# 人类打开 verification_uri，输入 user_code 授权
dreamina login checklogin --device_code=<device_code> --poll=120
dreamina user_credit
```

禁止：

```text
不得先运行 logout / relogin，除非用户明确要求切换/清理登录态。
```

---

# 7. OAuth / Headless 登录工作流

体验指南与本地 help 均确认当前登录使用 OAuth Device Flow。

标准交互登录：

```text
dreamina login
```

Agent/Codex 推荐无阻塞登录：

```text
dreamina login --headless
dreamina login checklogin --device_code=<device_code> --poll=30
dreamina user_credit
```

记录规则：

```text
1. 可以向用户展示 verification_uri、user_code、device_code。
2. 不要打印、复制、保存 auth/session/token/key/env 文件内容。
3. 授权完成后必须用 user_credit 自检。
4. 只有 user_credit 成功，才允许 Codex 执行后续被明确授权的 submit/query/download。
```

---

# 8. 异步任务与下载规则补丁

Dreamina 生成任务通常是异步：

```text
submit -> submit_id
query_result -> gen_status / queue_status / result
query_result --download_dir -> 下载结果
```

规则：

```text
1. submit_id 只是追踪号，不是最终成功。
2. querying 只是生成中，不是最终成功。
3. success 仍需下载和本地校验后才能记录 success_downloaded。
4. query_result 不带 --download_dir 只查询，不下载。
5. query_result --download_dir 才是下载阶段，必须被明确授权。
6. output_dir / output_name 不属于 submit 参数。
```

V1.2 的硬规则继续有效：

```text
submit_id alone is not enough.
querying alone is not enough.
```

---

# 9. 显式授权边界

默认边界：

```text
no submit
no query_result
no download
no batch
no retry
no relogin/logout
```

只有用户明确授权具体步骤，Codex/Agent 才能执行：

```text
1. one submit
2. one query_result
3. query/download existing submit_id
4. local metadata update
5. local contact sheet
```

授权文本必须包含：

```text
task_id / submit_id
命令类型
是否允许 download
是否允许 commit
是否禁止 retry / resubmit
```

---

# 10. 状态字段补丁

新增/推荐状态：

```text
local_cli_logger_blocked
local_cli_login_state_missing_for_agent
manual_download_success
success_downloaded_manual
remote_final_status_unknown_due_to_local_cli_block
codex_canary_ok
codex_canary_failed_logger
codex_canary_failed_login
agent_login_restored
```

错误分类示例：

```text
Codex query/download 报 Access denied：
status=local_cli_logger_blocked
remote_final_status=unknown
do_not_resubmit=true
manual_query_possible=true

人类手动下载成功：
status=success_downloaded_manual
remote_generation_status=success_by_manual_download
preserve_codex_failure=local_cli_logger_blocked 或 local_cli_login_state_missing_for_agent
```

---

# 11. 反馈 / Bug Report 信息清单

排查前必须准备：

```text
1. 执行的完整命令；
2. 终端错误信息；
3. dreamina version 输出；
4. 相关 dreamina <command> -h 输出；
5. ~/.dreamina_cli/logs/ 中非敏感相关日志片段；
6. submit_id / logid / credit_count，如果有；
7. gen_status / queue_status；
8. download_dir / output path，如果涉及下载；
9. 人类终端和 Codex 终端是否结果不同；
10. whoami / whoami /groups，如果是 Agent 环境问题。
```

不要提供：

```text
auth/session/token/key/env 文件内容。
```

---

# 12. 推荐最小闭环

新环境或修复后，按以下顺序验证：

```text
1. 安装 / 更新 CLI；
2. dreamina version；
3. dreamina -h；
4. dreamina login 或 login --headless；
5. dreamina user_credit；
6. 低成本 text2image 测试（仅在用户明确授权时）；
7. query_result；
8. query_result --download_dir；
9. 再进入视频、多帧、全能参考、批量任务。
```

Agent/Codex 环境中，第 6 步之后才算“真实生成测试”，必须获得明确授权。

---

# 13. SHOT-02-V009 事故复盘写入规则

本项目 V009 复盘应作为后续案例基准：

```text
1. V009 valid submit 成功；
2. Codex query/download 首次失败于 local logger Access denied；
3. 人类 Git Bash 手动 download 成功；
4. logger ACL 修复后 Codex Access denied 消失；
5. Codex user_credit 失败，说明 Codex 缺少登录态；
6. Codex OAuth checklogin 成功后 user_credit 成功；
7. Codex Dreamina CLI 恢复，但仍需每次 live work 前 canary。
```

结论：

```text
这不是 prompt 失败；
不是远端生成失败；
不是 submit_id 失效；
是本地 Agent/Codex 执行环境问题。
```

---

# 14. 与 V1.2 的关系

V1.2 解决：

```text
命令契约、Web/CLI 差异、submit_id/querying 不足以证明成功。
```

V1.3 补充：

```text
Agent/Codex 本地执行身份、logger、登录态、canary、人工 fallback。
```

两者共同构成真实 Dreamina CLI 执行前置检查：

```text
1. command-contract preflight；
2. Agent/Codex canary；
3. explicit authorization boundary。
```

---

# 15. 一句话总结

```text
Dreamina CLI 在 Agent/Codex 环境中，不仅要确认命令参数合法，还要确认本地执行身份能写日志、能读/建立登录态、能通过 user_credit。每次真实 submit/query/download 前，先跑 version + user_credit canary；未通过就不得把本地失败误记为远端生成失败。
```
