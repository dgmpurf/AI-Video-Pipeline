# chi_yan_tian_qiong production workflow

## Purpose
- Generate reviewed assets for one production with explicit lock controls.

## Files and folders
- `manifests/`: planned tasks and references.
- `assets/asset_registry.template.json`: canonical registry structure.
- `reviews/review_records.template.jsonl`: immutable review decision log.
- `reviews/IMAGE_REVIEW_TEMPLATE.md`: image review checklist.
- `reviews/VIDEO_REVIEW_TEMPLATE.md`: video review checklist.
- `reviews/RERUN_REASON_TEMPLATE.md`: rerun rationale form.
- `shots/SHOT_REGISTRY_TEMPLATE.json`: shot registry reference.
- `prompts/PROMPT_RECORD_TEMPLATE.json`: prompt record template.
- `locked_refs/` and `locked_videos/`: reserved review-locked outputs.

## Review policy
- `candidate` assets enter the registry as draft.
- Only reviewed candidates can become `locked_after_human_review`.
- `system` review decisions cannot finalize production locks.
- `rejected` and `archived` assets are excluded from reference candidates by default.

## Notes
- This production template set is ASCII-first.