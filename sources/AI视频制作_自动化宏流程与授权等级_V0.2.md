# AI视频制作_自动化宏流程与授权等级_V0.2

版本：V0.2 Draft  
来源：K244S SHOT-04 R02 evidence pack  
状态：Source 草案，需人类手动确认后进入 `sources/`

## 0. 一键式定义

“一键式”不是无限自动执行。  
本项目的一键式应定义为：

```text
带授权边界、带内部 gate、可中断、可审计、可复盘、可回滚的 macro-run。
```

## 1. 全局硬规则

- Codex 不修改官方 `sources/`。
- submit/query/download/retry/resubmit 必须分开授权，除非明确 macro 授权合并。
- package review pass 不等于 submit 授权。
- submit success 不等于 query/download 授权。
- query success 不等于 download 授权。
- download success 不等于 visual success。
- visual success 不等于 final/lock。
- final/lock 必须人类明确批准。

## 2. Macro-run 组件

### A. Input / Story Compiler

接收用户输入：小说、剧本、一句话、世界观、动作想法。  
输出结构化生产意图：

- 对白
- 动作
- 表情
- 语气
- 声音
- 时空坐标
- 人物站位
- 情绪转折
- 镜头目的
- 物理因果
- 风险点

### B. Script / Shot Compiler

把剧本拆成镜头和动作 beat。

必须输出：

- shot_id
- beat goal
- action chain
- timing window
- review criteria
- what not to do

### C. Asset Planner A/L/C/HC/CTRL/SHOT

资产分层：

| 层级 | 用途 |
|---|---|
| A | 基础角色/场景/道具资产 |
| L | 轻依赖资产 |
| C | 复合锚帧/关键帧 |
| HC | 高阶复合资产 |
| CTRL | layout、动作参考、姿态、镜头控制 |
| SHOT | 最终镜头生成资产 |

### D. Prompt Compiler

生成 prompt，并做：

- Prompt Priority Audit
- Visual Result Compliance
- Negative Constraint Compression
- Reference Duty Attention Audit
- Timing/front-loaded action audit

### E. Package Builder

生成：

- prompt txt
- package JSON
- manifest CSV
- report

默认 no-submit。

### F. Independent Package Review

检查：

- JSON/CSV parse
- command contract
- hashes
- refs
- prompt priority
- flags false
- final_master=false
- locked=false

### G. Human Authorization Gate

人类授权类型：

```text
submit
query
download
retry
resubmit
media creation
Source update
final
lock
```

每种必须单独记录。

### H. Dreamina Execution Layer

live 阶段必须先运行对应 task help：

- text2image -h
- image2image -h
- text2video -h
- multimodal2video -h

然后只执行授权动作。

### I. Query / Download Layer

- query-only 不带 `--download_dir`。
- download-only 只下载已有 success submit_id。
- fail 无结果时禁止 download。
- query loop 需要 macro 授权。

### J. Review Artifact Builder

媒体存在时可自动构建：

- metadata
- frames
- contact sheet
- sha256
- duration / frame count

Review artifacts 是证据，不是审批。

### K. Human Visual Review Recorder

默认用户只审图片/视频。

记录：

- human review quote
- visual status fields
- usable_as_final
- locked
- failure categories
- recommended next route

### L. Failure / Success Ledger Writer

每个 shot 定期写：

- failure ledger
- success / partial success ledger
- prompt outcome dataset
- review excerpts

### M. Source Update Recommender

Codex 只能写 report 下的 Source candidates。  
ChatGPT Pro Extended / 人类负责生成官方 Source 草案。  
人类手动应用。

## 3. Macro-run 授权等级建议

### L0：纯规划/报告

允许读文件、写报告，不允许 live。

### L1：本地 artifacts

允许抽帧、contact sheet、metadata，不运行 Dreamina。

### L2：no-submit package

允许创建 prompt/package/manifest/report，不 live。

### L3：单项 live

可选一种：

- one-submit-only
- one-query-only
- download-only

禁止自动连带动作。

### L4：bounded macro-run

可在一次人类授权下执行：

```text
package validate
preflight
one submit
bounded query
success download
review artifacts
report
```

必须有：

- submit_count_max
- query_count_max
- download_count_max
- retry_count_max=0 unless explicit
- final/lock=false
- stop conditions

### L5：production macro-run

未来可配置是否人工审查。  
默认仍然：final/lock 必须人类确认。

## 4. 强制 Stop Gates

Macro-run 必须在以下情况停止：

1. `sources/` 脏。
2. package defect。
3. command contract 不匹配。
4. 需要 submit 授权。
5. submit-only 完成。
6. query-only 完成。
7. success 但 download 未授权。
8. media 存在但未 visual review。
9. remote failure 重复。
10. 路线重大变化。
11. final/lock。
12. Source update。

## 5. 失败触发路线重置

当出现：

```text
两个结构不同路线 valid-submit 后 remote final-generation failed
```

Macro-run 必须停止自动 retry，进入 route reset。

## 6. 用户默认审查对象

用户默认审查：

- 图片
- 视频
- review artifacts

用户不默认审查：

- prompt
- package JSON
- manifest CSV

prompt 只在连续失败、重大方向变化、package defect 或用户要求时给用户看。

## 7. SHOT-04 R02 应用规则

当前状态：

- K244 text2video package review pass with high-risk notes。
- K245 仍需人类授权。
- K245 只允许 one-submit-only。
- K246 query、K247 download、K248 visual review 必须分阶段或明确 macro 授权。

## 8. Source 更新周期

每隔一段失败/成功链路，应自动生成：

- failure ledger
- success ledger
- prompt outcome dataset
- Source update candidates

但 official Source 仍由 ChatGPT + 人类手动治理。
