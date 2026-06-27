# AI视频制作_自动化宏流程与授权等级_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 版本：V0.1  
> 状态：Project Source 候选  
> 生成方：ChatGPT  
> 应用方式：由人类用户手动上传 / 复制到 ChatGPT Project Source 或本地 `sources/`。Codex / automation 不得直接写入 `sources/`。  
> 核心目的：把原先大量碎片化的 Codex ↔ ChatGPT 循环整合为可授权、可审计、可中断、可复盘的 macro-run / 大阶段执行流程。

---

## 0. 本 Source 的定位

本 Source 只规范 **自动化宏流程与授权等级**。

它不替代：

- `AI视频制作_Source索引与使用优先级`
- `AI视频制作_自动化治理与Source权限规则`
- `Dreamina CLI Help / 执行契约`
- `DreaminaBatcher manifest schema`
- `AI视频制作_实测规则库`
- 项目具体 K-phase reports
- 具体镜头 prompt / package / manifest / shot record

本 Source 的作用是：

```text
把多个已经验证过的生产步骤合并成更大的授权执行单元，
同时保留 source governance、human gate、submit/query/download/final/lock 边界。
```

---

## 1. 背景：为什么需要 macro-run

在 SHOT-03 的制作中，项目形成了大量小 phase：

```text
prompt draft
prompt audit
package ready
package review
submit authorization
query authorization
download authorization
local validation
contact sheet / review frames
human review
ChatGPT visual review
route decision
source update recommendation
```

这些步骤本身是必要的，但不一定每一次都要人工在 ChatGPT 和 Codex 之间逐步确认。

后续应将多个小步骤整合为 **macro-run**：

```text
不是削减步骤，
而是把步骤折叠进一个带内部 gate 的大阶段执行。
```

---

## 2. 关键结论：K176 之后可以开始切换 macro-run

SHOT-03 SPLIT-02 的 R01/R02 已经证明：

```text
R01：5-ref image2image 保留了部分 corridor / column composition，但 Shuangji identity lock 失败。
R02：3-ref identity-priority 修回部分 Shuangji identity，但 two-character blocking / action relation 失败。
```

K176 已确认：

```yaml
route_decision: pause_SPLIT02_image2image_repair_loop
preferred_next_route: SHOT03_CUT_B_to_CUT_C_direct_edit_continuity
terrain_interaction_route: defer_to_SHOT04_architecture_interaction_design
manual_pose_keyframe_route: optional_future_only
continue_R03_image2image: false
final_master: false
locked: false
```

因此：

```text
从 K177 开始，可切换为 macro-run 工作方式。
K177 建议使用 L1/L2 local/report macro。
第一个完整 L4 one-submit + bounded query + download + review artifacts macro-run，建议放到 SHOT-04。
```

---

## 3. Macro-run 定义

Macro-run 是一次 Codex 任务中连续执行多个生产步骤。

典型 L4 macro-run 可包含：

```text
1. 读取 Source / reports / shot records
2. git/source preflight
3. prompt 编译或使用 ChatGPT-approved prompt
4. package JSON / manifest CSV / shot record / report 生成
5. package validation / package review
6. Dreamina corrected preflight
7. exactly one submit
8. bounded query
9. success 后 download once
10. local media validation
11. review frames / contact sheet
12. full report
13. staged-file safety check
14. text-only commit / push
15. final verdict
```

Macro-run 必须有明确授权等级、允许范围、禁止范围和内部 gate。

---

## 4. 授权等级

### L0：Planning Only

适用：

- 路线分析
- prompt 草案
- reference-duty map
- risk register
- source update recommendation
- macro-run plan
- report

允许：

```yaml
create_report: true
create_prompt_draft_inside_report: true
read_sources: true
```

禁止：

```yaml
create_prompt_file: false
create_package_json: false
create_manifest_csv: false
run_dreamina: false
submit: false
query: false
download: false
create_media: false
final_master: false
locked: false
```

---

### L1：Local Review Artifacts Only

适用：

- 已有视频 / 图片的本地分析
- 抽帧
- contact sheet
- metadata validation
- cut-window planning
- local-only report

允许：

```yaml
extract_frames: true
create_contact_sheet: true
create_cut_candidates_if_explicitly_authorized: conditional
validate_media: true
create_report: true
```

禁止：

```yaml
run_dreamina: false
submit: false
query: false
download: false
stage_media: false
final_master: false
locked: false
```

---

### L2：No-submit Package

适用：

- prompt txt
- package JSON
- manifest CSV
- package report
- package review

允许：

```yaml
create_prompt_txt: true
create_package_json: true
create_manifest_csv: true
create_shot_record_json: conditional
validate_refs: true
create_report: true
```

禁止：

```yaml
run_dreamina: false
submit: false
query: false
download: false
create_media: false
final_master: false
locked: false
```

所有 L2 package 必须包含：

```yaml
submit_allowed: false
query_allowed: false
download_allowed: false
retry_allowed: false
resubmit_allowed: false
final_master: false
locked: false
human_submit_authorization_required: true
package_review_required: true
```

---

### L3：One-submit Only

适用：

- 人类已经批准一次 submit
- 只允许提交，不允许 query/download

允许：

```yaml
dreamina_version: true
dreamina_user_credit: true
dreamina_command_help: true
submit_count_max: 1
```

禁止：

```yaml
query: false
download: false
retry: false
resubmit: false
batch: false
create_media_manually: false
final_master: false
locked: false
```

L3 输出必须包含：

```text
submit_id
logid
gen_status
credit_count
fail_reason
no_query_confirmation
no_download_confirmation
```

---

### L4：One-submit + Bounded Query + Download-on-success + Review Artifacts

适用：

- 希望 Codex 一次性完成 submit/query/download/review artifacts
- 人类已明确授权该 macro-run 的完整 L4 范围

允许：

```yaml
create_package: true
package_review: true
dreamina_version: true
dreamina_user_credit: true
dreamina_command_help: true
submit_count_max: 1
query_count_max: explicit_number
query_interval_seconds: explicit_number
download_on_success: true
download_count_max: 1
validate_media: true
create_review_frames: true
create_contact_sheet: true
create_report: true
text_only_commit_push: true
```

禁止：

```yaml
retry: false
resubmit: false
extra_submit: false
batch: false
source_write: false
source_stage: false
media_stage: false
final_master: false
locked: false
runtime_config_change: false
auth_token_env_stage: false
```

L4 不是自动 final。  
L4 结束后的素材状态只能是：

```text
candidate
pending_human_review
pending_chatgpt_review
not_final
not_locked
```

---

### L5：Retry / Resubmit

默认禁用。

只有人类明确授权时才允许。

L5 必须单独开 phase，不得作为 L4 自动后续。

---

## 5. 永久硬边界

### 5.1 Source 权限

Official Project Source files are controlled only by the human user.

Codex / automation 可以：

```yaml
source_read_allowed: true
source_recommendation_allowed: true
source_draft_allowed: true
write_reports: true
```

Codex / automation 不可以：

```yaml
source_write_allowed: false
source_stage_allowed: false
source_commit_allowed: false
source_push_allowed: false
create_sources_files: false
edit_sources_files: false
delete_sources_files: false
rename_sources_files: false
move_sources_files: false
treat_reports_as_official_source: false
```

Official Source 更新路径：

```text
1. K-phase reports / human review / ChatGPT review 形成 evidence
2. ChatGPT 生成或审阅 official Source markdown
3. 人类检查
4. 人类手动上传到 ChatGPT Project Source
5. 如需本地同步，人类手动复制 / 替换到 local sources/
6. Codex 后续只读
```

---

### 5.2 submit / query / download 权限

默认状态：

```yaml
submit_allowed: false
query_allowed: false
download_allowed: false
```

只有在人类授权等级包含相应动作时才允许。

规则：

```text
submit 授权 ≠ query 授权
query 授权 ≠ download 授权
download 授权 ≠ final/lock 授权
L4 可以合并 submit/query/download，但必须在授权文本中明确 query_count、download_on_success 和 retry/resubmit 禁止。
```

---

### 5.3 final / locked 权限

Codex 不得自动设置：

```yaml
final_master: true
locked: true
approved: true
usable_as_final: true
```

即使 macro-run 成功生成、查询、下载、抽帧、生成 contact sheet，也只能标记：

```yaml
human_review_required: true
chatgpt_visual_review_required: true
final_master: false
locked: false
```

---

### 5.4 retry / resubmit 权限

Codex 不得自动 retry / resubmit。

失败时只允许：

```text
record failure
summarize failure reason
recommend fix route
wait for human authorization
```

---

### 5.5 Media stage / commit 权限

Codex 不得 stage 或 commit：

```text
mp4
png
jpg
jpeg
webp
gif
downloaded media
review frames
contact sheets
cut candidates
auth/session/token/key/env files
```

除非人类明确另行授权，否则只允许 stage：

```text
reports
prompt txt
package JSON
manifest CSV
lightweight metadata JSON
```

---

## 6. Dreamina corrected preflight

Macro-run 中涉及 Dreamina 时，必须使用 corrected preflight：

```text
dreamina version
dreamina user_credit
dreamina <target_command> -h
```

不得把顶层命令当作登录检查：

```text
dreamina checklogin
```

说明：

```text
user_credit 成功可作为 Agent/Codex 环境下账户可用 canary。
dreamina login checklogin 只用于 headless login flow 的 device_code 轮询。
不要在普通生产 preflight 中随便 login/logout/relogin。
```

每次 live execution 必须记录：

```text
local dreamina version
target command help output / supported flags
model_version
ratio
duration / resolution / resolution_type
poll / no-poll behavior
```

不得只根据旧经验推断本地 CLI 能力。

---

## 7. L4 Macro-run 内部 Gate

所有 L4 macro-run 必须包含以下 gate：

### Gate 1：Git / Source Preflight

检查：

```text
branch status
git status --short
git status --short -- sources/
sources/ clean
.vs/ only untracked noise
```

若 sources/ dirty，立即停止。

---

### Gate 2：Input / Evidence Loader

读取：

```text
Source index
automation governance
Dreamina help / CLI contract
relevant K-phase reports
shot records
prompt / package / manifest
active refs
```

缺失非关键文件时记录 absent。  
缺失关键 prompt/package/ref 时阻塞。

---

### Gate 3：Prompt / Package Validation

检查：

```text
prompt exists
prompt UTF-8 readable
prompt sha256
package JSON parses
manifest CSV reads
manifest row_count expected
refs exist
reference-duty map present
submit_allowed=false before authorization
final_master=false
locked=false
```

---

### Gate 4：Clause-level Compliance

不能只写：

```text
files inspected: Source V1.x
```

必须写：

| 字段 | 含义 |
|---|---|
| source_rule | 哪条规则 |
| required_behavior | 需要落实什么 |
| prompt_clause | prompt 哪句话落实 |
| status | present / weak / missing |
| risk_if_missing | 缺失风险 |

如果没有对应 prompt clause：

```text
source_rule_not_operationalized
```

不得放行。

---

### Gate 5：Command-contract Preflight

执行：

```text
dreamina version
dreamina user_credit
dreamina <target_command> -h
```

检查：

```text
repeated image flags
prompt flag
model_version
ratio
duration / resolution
resolution_type
poll=0 / async behavior
download behavior
```

---

### Gate 6：Submit Gate

限制：

```yaml
submit_count_max: 1
retry_allowed: false
resubmit_allowed: false
```

记录：

```text
submit_id
logid
gen_status
credit_count
fail_reason
```

不得在 submit 后自动宣称成功。  
成功必须由 query 确认。

---

### Gate 7：Bounded Query Gate

限制：

```yaml
query_count_max: explicit_number
query_interval_seconds: explicit_number
poll_loop_allowed: false unless explicitly authorized
```

若 still querying：

```text
stop and report
```

若 failed：

```text
stop and report
no retry
no resubmit
```

若 success：

```text
download only if L4 scope authorized download_on_success=true
```

---

### Gate 8：Download Gate

限制：

```yaml
download_count_max: 1
download_only_existing_success_result: true
download_unrelated_result: false
```

记录：

```text
local_path
size_bytes
sha256
format
width / height
duration / fps / frame_count if video
```

不 stage media。

---

### Gate 9：Review Artifact Gate

允许：

```text
review frames
contact sheet
metadata report
```

禁止：

```text
automatic final
automatic locked
```

---

### Gate 10：Staged-file Safety Gate

只允许 stage 授权范围内 text files。  
必须列出 staged files。

不得 stage：

```text
media
sources/
.vs/
auth/session/token/key/env
runtime/config
unrelated files
```

---

## 8. Macro-run 输出格式

每个 macro-run 最终回复必须包含：

```text
1. phase executed yes/no
2. authorization level
3. preflight pass/block
4. source governance status
5. prompt/package/ref validation
6. command-contract result if applicable
7. submit result if applicable
8. query result if applicable
9. download result if applicable
10. media validation if applicable
11. review artifact paths if created
12. staged files
13. commit / push result
14. final verdict
15. recommended next phase
```

---

## 9. Human / ChatGPT / Codex 的分工

### ChatGPT

负责：

```text
creative direction
prompt design
macro-run instruction
visual review
source drafting
route decision support
failure pattern analysis
```

### Codex

负责：

```text
local execution
git/source preflight
package generation
CLI command execution
download
local validation
frame extraction
contact sheet
report writing
text-only commit/push
```

Codex 不负责：

```text
final visual approval
locking
Source official update
unbounded retry/resubmit
```

### Human

负责：

```text
authorization
visual judgment
final/lock decision
manual Source application
project-level route choice
```

---

## 10. 给 ChatGPT 的反馈包

每次 macro-run 后，用户应尽量把以下内容反馈给 ChatGPT：

```text
Codex final response
K-phase report md
downloaded image/video if visual review is needed
contact sheet
review frames if relevant
user human review comments
any unexpected CLI/code errors
```

ChatGPT 应基于：

```text
human review
Codex report
media / sheet / frames
Source rules
prior reports
```

做三方审核和下一步指令。

---

## 11. R01/R02 教训：identity vs blocking trade-off

SHOT-03 SPLIT-02 证明：

```text
5-ref image2image:
composition better
Shuangji identity failed

3-ref identity-priority image2image:
Shuangji identity partially repaired
two-character blocking/action relation failed
```

结论：

```text
ordinary image2image is not reliably solving:
dual-character identity
precise close-contact blocking
corridor/column composition
all at once
```

因此：

```text
do not continue R03 ordinary image2image immediately
do not use R01/R02 as approved keyframes
do not proceed to video generation from R01/R02
pause SPLIT-02 image2image repair loop
use CUT_B -> CUT_C direct edit continuity for SHOT-03
defer terrain / architecture interaction to SHOT-04
```

---

## 12. SHOT-03 当前路线

SHOT-03 当前优先：

```yaml
CUT_B: current preferred SPLIT-01 clean corridor combat candidate
CUT_A: backup SPLIT-01
CUT_C: possible SPLIT-03 / return-to-close-combat
final_master: false
locked: false
```

K177 应优先：

```text
plan SHOT-03 CUT_B -> CUT_C edit continuity
local/report-only first
no Dreamina
no new submit
no final/lock
```

SHOT-04 可作为后续 L4 macro-run 试点：

```text
architecture / terrain interaction
body impact / doorway / railing / lattice / wall panel
rain / dust / smoke concealment
object return / counterattack
```

---

## 13. 何时使用 Pro 模式

建议使用 Pro / 高推理模式的场景：

```text
Source 正式生成 / 更新
macro-run 指令生成
跨多个 K-phase 的路线裁决
多源规则合并
复杂镜头 prompt 设计
复杂失败复盘
视觉审核后的策略判断
```

普通 Thinking / medium 可用于：

```text
单一 K-phase report
本地 artifact 生成
简单 package review
metadata validation
```

---

## 14. 代码级自动化建议

不要一开始就写完全自动化 runner。  
建议先用 macro prompt 跑 2–3 次 L4，稳定后再固化为代码。

未来可设计：

```text
macro_runner.py
macro_job.json
phase_state.json
```

runner 必须强制：

```yaml
submit_count_max: 1
query_count_max: explicit_number
download_count_max: 1
retry_allowed: false
resubmit_allowed: false
source_write_allowed: false
media_stage_allowed: false
final_master_allowed: false
locked_allowed: false
```

代码级 runner 的输出也必须生成 K-phase report。

---

## 15. 推荐默认 L4 Codex Prompt 骨架

```text
PHASE: <Kxxx_MACRO_NAME>

Authorization level:
L4 = one submit + bounded query + download-on-success + local review artifacts

Human authorization:
<quote exact authorization>

Allowed:
- package creation/review
- corrected Dreamina preflight
- exactly one submit
- bounded query
- download once if success
- validation
- review frames/contact sheet
- report
- text-only commit/push

Forbidden:
- retry
- resubmit
- extra submit
- source modification
- final/lock
- media staging
- runtime/config modification
- auth/token/env staging

Internal gates:
1. Git/source preflight
2. Evidence loading
3. Prompt/package validation
4. Clause-level compliance
5. Command-contract preflight
6. Submit exactly once
7. Bounded query
8. Download on success only
9. Local validation/review artifacts
10. Staged-file safety

Final output:
- submit_id/logid
- query status
- media path if downloaded
- sha256/metadata
- review artifact paths
- staged files
- commit/push
- final verdict
```

---

## 16. Source 更新时机

本 Source 可立即作为 Project Source 候选上传。

但它不要求立刻停止当前 K-phase。  
推荐顺序：

```text
1. 上传本 Source
2. 从 K177 开始使用 L1/L2 macro
3. 在 SHOT-04 使用第一条 L4 macro-run
4. 根据实际执行结果，再生成 V0.2
```

---

## 17. Final Invariants

```yaml
source_read_allowed: true
source_recommendation_allowed: true
source_draft_allowed: true
source_write_allowed: false
source_stage_allowed: false
source_commit_allowed: false
source_push_allowed: false

submit_requires_authorization: true
query_requires_authorization: true
download_requires_authorization: true
retry_requires_authorization: true
resubmit_requires_authorization: true
final_master_requires_authorization: true
locked_requires_authorization: true

macro_run_allowed: true
macro_run_must_have_authorization_level: true
macro_run_must_have_internal_gates: true
macro_run_does_not_imply_final_or_locked: true

media_stage_default: false
sources_stage_default: false
auth_token_env_stage_default: false
```
