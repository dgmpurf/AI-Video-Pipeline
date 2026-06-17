# Prompt Factory Usage Notes

Use `PromptFactory` to build deterministic prompts from structured data.

## Inputs
- `shot_record`: required `ShotRecord` fields
- `reference_roles`: list of reference role objects
- `style_rules`: optional style plan
- `negative_rules`: optional ordered negative prompt list

## Outputs
- `build_reference_role_block(reference_roles)` returns deterministic role text ordered by `order`.
- `build_keyframe_prompt(...)` returns a structured keyframe prompt string.
- `build_video_prompt(...)` returns a structured video prompt string.
- `build_negative_prompt(...)` merges ordered negative rules into a single string.

## Determinism
- Sorting by numeric `order` guarantees stable output for the same input payload.
- Rule strings preserve input order.

## Guidance
- Avoid vague action verbs in final action shots.
- Favor explicit motion terms such as contact point, force chain, and body weight transfer.