# Gold Adjudication Template

用于 gold set 最终裁决。只有这个裁决结果可以进入 final label / tag_rules / alias_rules / risk_rules。

## ref

- ref_id:
- file_path:
- adjudication_date:

## accepted controlled tags

```yaml
accepted_controlled_tags:
  - tag:
    reason:
```

## rejected tags

```yaml
rejected_tags:
  - tag:
    reason:
```

## accepted impression aliases

```yaml
accepted_impression_aliases:
  - user_phrase:
    normalized_alias:
    mapped_controlled_tag:
    reason:
```

## final usage_class

- final_usage_class:
- reason:

## final risk_tags

```yaml
final_risk_tags:
  - tag:
    reason:
    severity:
```

## final reference_duty

```text

```

## final do_not_copy

```text

```

## prompt_ready yes/no

- prompt_ready: yes / no
- reason:

## active_input_allowed yes/no

- active_input_allowed: yes / no
- reason:

## adjudicator

- name:
- role:

## reason

```text

```
