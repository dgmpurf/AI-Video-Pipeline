# AI 视频模仿参考库 Calibration V0.1

本目录用于 AI 视频模仿参考库的小样本校准流程。

用途：

- 建立 user / ChatGPT / Codex 三方标注口径。
- 用 100-200 条 gold set 校准 controlled tags、impression aliases、risk rules。
- 为后续批量粗标、抽查、人工裁决提供模板。

边界：

- 本目录不存放媒体文件。
- 本目录不存放真实视频。
- 本目录不授权 Dreamina。
- 本目录不授权 submit / query / download / retry / resubmit。
- 本目录不授权视频扫描、缩略图、contact sheet、keyframe、数据库初始化。
- 本目录中的 Codex 输出只能作为候选建议，不能作为 final label。

推荐使用顺序：

1. `user_impression_note_template.md`
2. `chatgpt_structured_review_template.md`
3. `codex_auto_suggestion_schema.json`
4. `gold_adjudication_template.md`
5. `AI视频制作_模仿参考库Calibration流程_V0.1.md`
6. `audit_sampling_policy_V0.1.md`
