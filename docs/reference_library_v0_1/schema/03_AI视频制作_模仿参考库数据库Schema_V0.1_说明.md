# AI视频制作_模仿参考库数据库Schema_V0.1_说明

## 0. 文件定位

本说明对应：

```text
03_AI视频制作_模仿参考库数据库Schema_V0.1.sql
03_AI视频制作_模仿参考库_empty_refs_with_tags_V0.1.sqlite
```

这是 **AI 视频模仿参考库** 的 SQLite 起步 schema，用于把已经完成的：

```text
01 总体设计
02 标签字典
```

落到可执行数据库结构。

它仍然是 **Draft / 执行规范候选**，不是 official Source。正式进入 Project Source 或本地 `sources/` 前，仍需人工确认。

## 1. 设计原则

```text
视频文件放本地文件夹，不塞进数据库。
SQLite 只存路径、元数据、标签、搜索文本、安全状态、使用反馈。
搜索单位以 ref_segment 为主，不只搜 raw_clip。
active_input_allowed 默认 false。
外部影视 / 游戏 / 动漫 / 教程素材默认 offline_grammar_only。
FTS5 负责第一版搜索引擎。
Context + feedback 负责后续推荐排序。
```

## 2. 核心对象

| 表 | 作用 |
|---|---|
| `raw_clips` | 原始视频文件记录，存路径、来源、技术元数据、权利状态 |
| `ref_segments` | 真正可搜索 / 可复用的参考片段 |
| `tags` | 双语受控标签字典，字段匹配 `02_AI视频制作_模仿参考库标签字典_V0.1.csv` |
| `tag_aliases` | 中英文别名与同义词 |
| `segment_tags` | 片段与标签的多对多关系 |
| `media_artifacts` | 缩略图、contact sheet、关键帧、代理视频等派生产物 |
| `transcripts` | ASR / 人工转写文本 |
| `detections` | OCR、pose、face、logo、watermark、UI 等检测结果 |
| `captions` | VLM caption 或人工描述 |
| `embeddings` | 预留 CLIP/OpenCLIP/FAISS/Qdrant/sqlite-vec 等向量检索引用 |
| `scene_contexts` | 场景 / 剧本 / shot goal 上下文 |
| `retrieval_attempts` | 搜索尝试记录 |
| `generation_attempts` | 实际生成 / 审片尝试记录 |
| `attempt_refs` | 一次尝试中用了哪些参考、承担什么职责 |
| `feedback_events` | success / partial_success / failure 等反馈事件 |
| `ref_context_stats` | 每个参考在不同 context 下的成功失败统计 |
| `ref_segments_fts` | FTS5 全文搜索索引 |
```

## 3. 已验证内容

本次生成时已用 Python `sqlite3` 执行完整 SQL，并导入标签字典：

```text
tags: 450
tag_aliases: 172
```

并执行了一个 FTS5 smoke test：插入测试片段、搜索 `wet`、确认可命中，然后删除测试数据。

## 4. 初始化方式

在本地可用：

```bash
sqlite3 refs.sqlite < 03_AI视频制作_模仿参考库数据库Schema_V0.1.sql
```

如果要直接使用已导入标签的空库，可复制：

```text
03_AI视频制作_模仿参考库_empty_refs_with_tags_V0.1.sqlite
```

## 5. 标签导入策略

Schema 中 `tags` 表与 CSV 字段基本一一对应：

```text
tag_id
tag_key
zh_name
en_name
category
parent_tag_key
level
aliases_zh
aliases_en
use_for_exact_filter
use_for_fulltext
use_for_semantic
use_for_weighting
default_usage_class
default_active_input_allowed
default_reference_role
risk_level
description_zh
description_en
examples
do_not_use_for
source_basis
status
```

`tag_aliases` 是从 `aliases_zh` / `aliases_en` 拆出来的规范化别名表，方便后续搜索框做同义词展开。

## 6. FTS5 搜索字段

`ref_segments_fts` 搜索以下字段：

```text
标题
摘要
query_text
tag_text
alias_text
risk_text
prompt_words_zh / prompt_words_en
reference_duty
do_not_copy
review_criteria
post_plan
edit_timeline_note
notes
```

建议第一版搜索时使用：

```text
精确标签筛选 + FTS5 MATCH + 风险过滤 + context_score 排序
```

## 7. 与 GUI / Workbench 的关系

GUI 第一版可以直接使用这些视图：

| 视图 | 用途 |
|---|---|
| `v_ref_search_cards` | 搜索结果卡片 |
| `v_active_input_candidates` | active input 候选，只显示低风险片段 |
| `v_prompt_ready_refs` | prompt-ready / deep-tagged 片段 |
| `v_offline_grammar_refs` | 仅离线语法参考片段 |
| `v_ref_context_score_summary` | 反馈权重与上下文成功率展示 |

## 8. 与 Codex L1 的关系

这份 schema 适合后续给 Codex 写 L1 本地索引工具：

```text
扫描 reference_library/raw_clips
ffprobe 读取元数据
ffmpeg 生成缩略图 / contact sheet
PySceneDetect 生成候选 ref_segment
导入 SQLite
自动写 query_text / 初始 tag suggestions
建立 FTS5
不跑 Dreamina
不 submit / query / download
不修改 official Source
```

## 9. 后续待补

下一步建议生成：

```text
04_AI视频制作_模仿参考库ReferenceDuty与安全规则_V0.1.md
```

它会把 `reference_duty`、`do_not_copy`、`active_input_allowed`、`offline_grammar_only`、`review_standard_only`、`prompt_influence_allowed` 的规则正式整理成可复制模板。
