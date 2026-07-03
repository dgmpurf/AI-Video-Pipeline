# 06_Codex_L1_REF_LIBRARY_INDEXER_SPEC_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE / AI Video Mimic Reference Library
> 类型：Codex L1 本地索引器任务说明 / Local-only implementation spec
> 版本：V0.1 Draft
> 生成日期：2026-07-03
> 状态：执行规范候选，不是 official Source
> 适用范围：本地参考视频库扫描、元数据提取、缩略图 / contact sheet 生成、SQLite + FTS5 建库、标签字典导入、CLI 搜索。
> 重要边界：本任务只允许 L1 local artifacts；不运行 Dreamina；不 submit / query / download；不上传云端；不修改 official Source；不把参考视频提交进 Git。

---

## 0. 一句话结论

```text
Codex L1 REF Library Indexer = 本地参考视频库索引器。
它只负责扫描本地视频、抽取技术元数据、生成本地预览物、导入标签字典、建立 SQLite + FTS5 搜索索引和输出报告。
它不负责生成视频、不负责上传素材、不负责判断 final、不负责修改 Source。
```

---

## 1. 任务定位

本任务是前五份模仿参考库设计文档之后的第一个可执行工程任务。

输入：

```text
01_AI视频制作_模仿参考库总体设计_V0.1.md
02_AI视频制作_模仿参考库标签字典_V0.1.csv
03_AI视频制作_模仿参考库数据库Schema_V0.1.sql
04_AI视频制作_模仿参考库ReferenceDuty与安全规则_V0.1.md
05_AI视频制作_模仿参考库GUI与人工标注流程_V0.1.md
```

输出：

```text
reference_library/db/refs.sqlite
reference_library/derived/posters/
reference_library/derived/contact_sheets/
reference_library/derived/keyframes/
reference_library/manifests/refs_export.csv
reference_library/logs/import_report_*.md
tools/ref_library/ref_indexer.py
tools/ref_library/refsearch.py
```

本任务不是 GUI 任务。
本任务不是 Dreamina 任务。
本任务不是 Source 更新任务。
本任务是为后续 GUI / Workbench 提供本地索引基础。

---

## 2. 授权等级

授权等级：

```text
L1：本地 artifacts
```

允许：

```text
读取本地参考视频文件夹
读取标签字典 CSV
读取 SQLite schema SQL
创建 / 更新本地 refs.sqlite
生成 poster frame
生成 contact sheet
生成 keyframe image
生成 muted proxy，可选，默认关闭
生成 CSV / JSONL 导出
生成本地报告
运行 refsearch CLI 查询本地 DB
```

禁止：

```text
Dreamina submit
Dreamina query_result
Dreamina download
Dreamina batch
任何 AI 生成媒体
上传任何参考视频到云端
联网下载素材
自动修改 ChatGPT Project Source
创建 / 编辑 / 删除 / stage / commit / push sources/*
stage / commit / push 原始视频或 reference segments
自动把 active_input_allowed 改成 true
自动把任何素材标为 final / locked
自动删除原始视频
```

派生预览物说明：

```text
poster / contact sheet / keyframes 是本地 review artifacts，不是生成媒体，不是最终素材。
它们可以用于人工浏览和标注，但不能被误认为 active generation input。
```

---

## 3. 推荐文件夹结构

```text
reference_library/
  raw_clips/
    RAW_000001.mp4
    RAW_000002.mov

  ref_segments/
    # 可选。第一版可以只建 segment metadata，不一定实际切短视频。
    REF_ACT_000001_guard_clash_skid.mp4

  derived/
    posters/
      RAW_000001.jpg
    contact_sheets/
      RAW_000001_contact.jpg
    keyframes/
      RAW_000001/
        frame_0000.jpg
        frame_0001.jpg
    muted_proxies/
      # 默认不生成，需显式参数开启。

  db/
    refs.sqlite
    backups/

  manifests/
    refs_export.csv
    raw_clips_export.csv
    segments_export.csv

  logs/
    import_report_20260703_001.md
    errors_20260703_001.log

  config/
    ref_library_config.yaml
```

工具目录建议：

```text
tools/ref_library/
  ref_indexer.py
  refsearch.py
  schema_check.py
  media_probe.py
  media_artifacts.py
  tag_importer.py
  fts_tools.py
  README.md
```

---

## 4. 输入文件

### 4.1 必需输入

```text
--library-root <path>
--schema <path/to/03_AI视频制作_模仿参考库数据库Schema_V0.1.sql>
--tags-csv <path/to/02_AI视频制作_模仿参考库标签字典_V0.1.csv>
```

### 4.2 可选输入

```text
--raw-dir <path>             默认 reference_library/raw_clips
--db <path>                  默认 reference_library/db/refs.sqlite
--config <path>              默认 reference_library/config/ref_library_config.yaml
--source-type <type>         默认 unknown
--rights-status <status>     默认 unknown
--dry-run                    只扫描和报告，不写 DB
--no-artifacts               不生成 poster / contact sheet
--generate-contact-sheet     生成 contact sheet
--scene-detect               尝试 PySceneDetect 生成候选 segment
--muted-proxy                生成静音 proxy，默认 false
--limit N                    限制处理数量，用于测试
```

---

## 5. 默认安全值

所有新导入 raw_clip / ref_segment 默认：

```text
rights_status = unknown
usage_class = offline_grammar_only
active_input_allowed = 0
offline_grammar_only = 1
prompt_influence_allowed = 1
review_standard_only = 0
do_not_use = 0
human_review_required_for_active_input = 1
review_status = raw
status = imported
```

任何自动检测结果只能写为：

```text
auto_tag_suggestion
risk_suggestion
needs_human_review
```

不得自动写成：

```text
active_input_allowed = 1
prompt_ready = true
final = true
locked = true
```

---

## 6. 工具命令设计

### 6.1 初始化数据库

```bash
python tools/ref_library/ref_indexer.py init \
  --db reference_library/db/refs.sqlite \
  --schema 03_AI视频制作_模仿参考库数据库Schema_V0.1.sql \
  --tags-csv 02_AI视频制作_模仿参考库标签字典_V0.1.csv
```

行为：

```text
创建 refs.sqlite
执行 schema SQL
导入 tags
导入 tag_aliases
启用 PRAGMA foreign_keys=ON
启用 WAL，可选
运行 schema smoke test
输出 init report
```

不得：

```text
扫描视频
生成预览物
修改 Source
```

---

### 6.2 扫描与导入 raw clips

```bash
python tools/ref_library/ref_indexer.py import \
  --library-root reference_library \
  --raw-dir reference_library/raw_clips \
  --db reference_library/db/refs.sqlite \
  --generate-contact-sheet \
  --scene-detect
```

行为：

```text
递归扫描视频文件
计算 sha256 或快速 hash，可配置
调用 ffprobe 提取 metadata
生成 poster frame
生成 contact sheet，可选
运行 PySceneDetect，可选
写入 raw_clips
写入 media_artifacts
写入候选 ref_segments
写入 import report
```

默认支持扩展名：

```text
.mp4 .mov .mkv .avi .webm .m4v
```

---

### 6.3 搜索

```bash
python tools/ref_library/refsearch.py "wet floor skid guard clash" \
  --db reference_library/db/refs.sqlite \
  --mode offline_grammar \
  --top-k 20
```

支持参数：

```text
--mode offline_grammar | prompt_ready | active_input | review_standard | all
--ref-type ACT | CAM | FX | EDIT | PERF | COMP | STYLE | ENV | SOUND | MOCAP | MIXED
--source-type film,tv,gameplay,anime,self_shot,mocap,ae_pr
--risk-exclude actor_face,watermark,logo,ui_overlay
--active-only
--prompt-ready-only
--show why
--json
--csv
```

输出字段：

```text
rank
ref_id
title
primary_ref_type
source_type
duration
useful_window
risk_level
usage_class
active_input_allowed
prompt_words_en
reference_duty
do_not_copy
local_path
poster_path
why_matched
```

---

### 6.4 导出

```bash
python tools/ref_library/ref_indexer.py export \
  --db reference_library/db/refs.sqlite \
  --out reference_library/manifests/refs_export.csv
```

输出：

```text
raw_clips_export.csv
segments_export.csv
refs_export.csv
tags_export.csv
```

---

### 6.5 备份

```bash
python tools/ref_library/ref_indexer.py backup \
  --db reference_library/db/refs.sqlite \
  --out reference_library/db/backups/refs_20260703.sqlite
```

要求：

```text
使用 SQLite backup API 或 VACUUM INTO
不得直接复制正在写入中的 DB
生成 backup report
```

---

## 7. 处理流程

### Stage 0：Preflight

检查：

```text
Python version
ffmpeg availability
ffprobe availability
sqlite3 availability
PySceneDetect availability，可选
library_root exists
raw_dir exists
schema file exists
tags csv exists
db path writable
sources/ 不被修改
Git status 只读检查，可选
```

失败即停止：

```text
missing_schema
missing_tags_csv
library_root_missing
raw_dir_missing
ffprobe_missing
db_not_writable
invalid_task_boundary
```

---

### Stage 1：Schema 初始化

执行：

```text
create DB
apply schema
load tags CSV
load aliases
create indexes
create FTS5 table
smoke test
```

Smoke test：

```text
insert a temporary raw_clip
insert a temporary ref_segment
insert FTS row
search temporary keyword
delete temporary rows
confirm DB clean
```

---

### Stage 2：Raw clip 扫描

对每个视频：

```text
normalize path
assign raw_id
detect duplicate by sha256 or path
ffprobe metadata
write raw_clips row
write status=imported
```

raw_id 推荐：

```text
RAW_000001
RAW_000002
```

如果使用已有文件名：

```text
保留原文件名在 original_filename 字段
不要强行重命名原始文件
```

---

### Stage 3：Review artifacts

生成：

```text
poster frame
contact sheet
keyframes
optional scene detect report
```

默认策略：

```text
poster: duration 20% 或 thumbnail selected frame
contact sheet: 4x4 或 5x5
keyframes: scene boundaries + evenly spaced frames
```

文件命名：

```text
derived/posters/RAW_000001.jpg
derived/contact_sheets/RAW_000001_contact.jpg
derived/keyframes/RAW_000001/frame_0000.jpg
```

---

### Stage 4：Segment candidates

第一版可以只创建一个默认 segment：

```text
REF_RAW_000001_FULL
start_ms = 0
end_ms = raw duration
review_status = raw
```

如果启用 scene detect：

```text
REF_ACT_000001_SCENE_001
REF_ACT_000001_SCENE_002
```

注意：

```text
自动 segment 只是候选，不等于 prompt-ready。
```

---

### Stage 5：Auto suggestions

第一版低风险自动建议：

```text
source_type from folder name
ref_type from filename keyword
risk flags from filename / OCR / simple heuristics
duration bucket
has_audio
has_text_overlay
```

不得自动深标：

```text
crossed_guard_compression
actor_face
celebrity_face
specific IP identity
active_input_allowed=true
```

这些必须人工确认。

---

### Stage 6：FTS 同步

构建 query_text：

```text
title
filename tokens
source_type
primary_ref_type
tags
aliases
prompt_words
reference_duty
do_not_copy
notes
```

触发：

```text
insert/update ref_segments_fts
validate FTS count
run sample search
```

---

### Stage 7：Report

生成报告：

```text
processed file count
inserted raw_clips
inserted ref_segments
duplicate count
failed probe count
generated posters
generated contact sheets
scene detect candidates
tag import count
FTS smoke result
warnings
next human actions
```

报告路径：

```text
reference_library/logs/import_report_YYYYMMDD_HHMMSS.md
```

---

## 8. 数据库写入规则

必须使用事务：

```text
BEGIN
process batch
COMMIT
```

每 N 条提交一次，可配置：

```text
batch_size = 50
```

异常处理：

```text
单文件失败不应导致整个导入中断，除非 schema / DB / path policy 失败。
```

失败文件写入：

```text
logs/errors_*.log
import_errors table，可选
```

---

## 9. Path Policy

必须禁止：

```text
输出路径逃出 library_root
使用 .. 穿越路径
覆盖原始视频
写入 sources/
写入 productions/ 下非 reference_library 目录，除非用户明确指定
写入 Git staged media
```

建议 path check：

```text
resolved_output_path.is_relative_to(library_root)
```

Windows 注意：

```text
支持长路径
支持空格
支持中文路径
使用 pathlib
不要手写字符串拼接
```

---

## 10. Git 与 Source 边界

Codex 可做：

```text
读取 Source
读取报告
读取前五份设计稿
创建 tools/ref_library/*
创建 reference_library/db/*
创建 reference_library/derived/*
创建 reference_library/logs/*
创建 reference_library/manifests/*
```

Codex 不可做：

```text
create/edit/delete/rename/move/stage/commit/push sources/*
stage/commit/push raw_clips/*
stage/commit/push ref_segments/*.mp4
把 Deep Research 原文直接塞进 Source
把生成的草案标记为 official Source
```

推荐 `.gitignore`：

```gitignore
reference_library/raw_clips/
reference_library/ref_segments/
reference_library/derived/
reference_library/db/*.sqlite
reference_library/db/*.sqlite-wal
reference_library/db/*.sqlite-shm
reference_library/logs/
```

可考虑纳入 Git 的小文件：

```text
tools/ref_library/*.py
tools/ref_library/README.md
reference_library/config/ref_library_config.example.yaml
reference_library/manifests/sample_refs_export.csv
schema.sql
tags.csv
```

是否纳入仍需用户决定。

---

## 11. 安全边界

### 11.1 Active input

不得自动设置：

```text
active_input_allowed = 1
```

只有人工审核后可设置：

```text
rights_status in self_owned / licensed / client_owned
no actor_face
no celebrity_face
no logo
no watermark
no UI / HUD
no subtitles
no IP character
no suspicious provenance
human_active_input_approval = true
```

### 11.2 外部素材

默认：

```text
film / tv / anime / game / tutorial / ad / social_short
→ offline_grammar_only
→ active_input_allowed = 0
```

### 11.3 自动风险标记

自动工具只能写：

```text
risk_suggestion = true
risk_tags += detected_text_overlay
risk_tags += possible_watermark
needs_human_review = true
```

不能写：

```text
rights_status = licensed
celebrity_face = true
```

除非输入数据明确提供并人工确认。

---

## 12. Refsearch 输出模板

Markdown 输出示例：

```markdown
# Search Results

Query: wet floor skid guard clash
Mode: offline_grammar
Top K: 10

## 1. REF_ACT_000123_guard_clash_wet_skid

- score: 12.83
- source_type: film
- usage_class: offline_grammar_only
- active_input_allowed: false
- risk_tags: actor_face, copyright_risk
- duration: 4.8s
- useful_window: 0.30s-1.70s
- local_path: reference_library/ref_segments/REF_ACT_000123.mp4
- poster: reference_library/derived/posters/REF_ACT_000123.jpg

Reference Duty:
只参考动作节奏、护架压缩、后脚滑退和水花反馈。
不要复制人物身份、服装、场景、台词、背景或剧情。

Prompt Words:
already close from first frame; crossed guard compression; rear foot wet skid; rain spray.

Why matched:
FTS: wet, skid, guard
Tags: ACTION.guard_block, ENV.wet_floor
Context: rainy corridor close combat
```

JSON 输出示例：

```json
{
  "rank": 1,
  "ref_id": "REF_ACT_000123",
  "score": 12.83,
  "usage_class": "offline_grammar_only",
  "active_input_allowed": false,
  "reference_duty": "...",
  "prompt_words_en": "..."
}
```

---

## 13. 配置文件建议

```yaml
library:
  root: reference_library
  raw_dir: raw_clips
  db_path: db/refs.sqlite

artifacts:
  generate_posters: true
  generate_contact_sheets: true
  generate_keyframes: true
  generate_muted_proxy: false
  contact_sheet_columns: 5
  contact_sheet_rows: 5

import:
  default_source_type: unknown
  default_rights_status: unknown
  default_active_input_allowed: false
  default_offline_grammar_only: true
  hash_mode: sha256
  batch_size: 50

tools:
  ffmpeg_path: ffmpeg
  ffprobe_path: ffprobe
  use_pyscenedetect: true
  use_ocr: false
  use_asr: false
  use_embeddings: false

safety:
  forbid_source_write: true
  forbid_git_media_stage: true
  require_human_active_input_review: true
```

---

## 14. MVP 范围

MVP 必须完成：

```text
init DB
load tags
scan raw_clips
ffprobe metadata
poster generation
contact sheet generation
default full-length ref_segment
FTS5 search
CSV export
import report
refsearch CLI
```

MVP 可以暂不做：

```text
OCR
ASR
MediaPipe
OpenCLIP embeddings
Qdrant / FAISS / sqlite-vec
GUI
自动 scene split 实际切片
自动版权判断
自动 active-safe 判断
多用户权限
```

---

## 15. 测试要求

### Unit tests

```text
schema can initialize
tags CSV can import
path policy rejects ../ escape
ffprobe parser handles sample json
FTS search returns expected row
risk mode filtering works
export CSV parses
```

### Integration smoke test

使用 2–5 个小视频样本：

```text
import
generate poster
generate contact sheet
write raw_clips
write ref_segments
search known filename keyword
export CSV
backup DB
```

### Boundary tests

必须确认：

```text
sources/ 未被修改
raw video 未被删除
active_input_allowed 未自动置 true
Dreamina 未被调用
没有网络上传
```

---

## 16. Codex 执行 Prompt 模板

下面这段可直接给 Codex 使用。

```text
任务：实现 AI 视频模仿参考库 L1 本地索引器。

授权等级：L1 local artifacts only。

硬边界：
- 不运行 Dreamina。
- 不 submit / query / download / retry / resubmit。
- 不生成 AI 媒体。
- 不联网下载素材。
- 不上传任何视频到云端。
- 不创建、修改、删除、重命名、移动、stage、commit、push sources/*。
- 不把参考视频提交进 Git。
- 不自动设置 active_input_allowed=true。
- 不设置 final/locked。
- 只允许处理本地 reference_library 目录下的文件和本任务创建的 tools/ref_library 文件。

输入：
- 02_AI视频制作_模仿参考库标签字典_V0.1.csv
- 03_AI视频制作_模仿参考库数据库Schema_V0.1.sql
- reference_library/raw_clips/

目标交付：
1. tools/ref_library/ref_indexer.py
2. tools/ref_library/refsearch.py
3. tools/ref_library/README.md
4. reference_library/config/ref_library_config.example.yaml
5. reference_library/db/refs.sqlite
6. reference_library/manifests/refs_export.csv
7. reference_library/logs/import_report_*.md

功能要求：
- init: 初始化 SQLite，并导入标签字典。
- import: 扫描 raw_clips，调用 ffprobe，写 raw_clips 表。
- artifacts: 用 ffmpeg 生成 poster 和 contact sheet。
- segments: 为每个 raw clip 建立一个默认 full-length ref_segment。
- fts: 同步 ref_segments_fts。
- search: 提供 refsearch CLI，支持 FTS 查询、模式过滤、JSON 输出。
- export: 导出 CSV。
- backup: 备份 SQLite。

默认安全：
- rights_status=unknown
- active_input_allowed=0
- offline_grammar_only=1
- review_status=raw
- human_review_required_for_active_input=1

报告必须包含：
- git status 摘要
- files inspected
- files created
- files modified
- processed video count
- failed video count
- tag count imported
- DB smoke test result
- FTS smoke test result
- boundary verification:
  - dreamina_not_called=true
  - source_write_attempted=false
  - media_staged=false
  - active_input_auto_true_count=0

执行结束后只输出报告，不做 commit。
```

---

## 17. 完成标准

任务通过必须满足：

```text
SQLite 可打开
tags 表有数据
raw_clips 有导入记录
ref_segments 有默认记录
poster/contact sheet 可找到
refsearch 能搜出结果
CSV export 可打开
import report 存在
没有 Dreamina 命令调用
没有 Source 修改
没有 active_input 自动开启
```

---

## 18. 下一阶段

L1 indexer 完成后，下一阶段可以分三条路线：

### Route A：Workbench GUI

```text
基于 05_GUI 与人工标注流程文档，实现 PySide6 桌面工具。
```

### Route B：Auto Annotation L2

```text
接入 OCR / ASR / MediaPipe / OpenCLIP，生成 auto_tag_suggestions。
```

### Route C：Prompt Integration

```text
把 refsearch 结果接入 Prompt Compiler，生成 reference duty block 和 review criteria。
```

推荐顺序：

```text
L1 indexer
→ GUI 粗标
→ refsearch 实用化
→ 再加 OCR / ASR / embeddings
```

---

## 19. Final Verdict

```text
CODEX_L1_REF_LIBRARY_INDEXER_SPEC_V0_1_READY
```
