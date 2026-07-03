# ChatGPT Structured Review Template

用于 ChatGPT / ChatGPT Pro 对参考片段做视觉拆解。输出是结构化候选，不是 final label。

## ref

- ref_id:
- file_path_or_frame_sheet:
- reviewer:
- review_date:

## visual_summary

```text

```

## primary_ref_type

```text

```

## controlled_tags

```yaml
controlled_tags:
  - tag:
    evidence:
    confidence:
```

## impression_tags_mapped

```yaml
impression_tags_mapped:
  - user_phrase:
    mapped_tag:
    mapping_confidence:
    note:
```

## reference_duty

```text

```

## do_not_copy

```text

```

## prompt_words

```yaml
prompt_words:
  positive:
    -
  avoid:
    -
```

## review_criteria

```yaml
review_criteria:
  action_clarity:
  timing_readability:
  motion_reference_value:
  camera_reference_value:
  environment_feedback_value:
  risk_notes:
```

## risk_tags

```yaml
risk_tags:
  - tag:
    reason:
    severity:
```

## usage_class recommendation

- usage_class_recommendation:
- reason:

## active_input recommendation

- active_input_recommendation: no / possible_after_human_review / blocked
- reason:

## uncertainty

```yaml
uncertainty:
  visual_uncertainty:
  tag_uncertainty:
  safety_uncertainty:
  needs_full_video_review:
  needs_user_adjudication:
```
