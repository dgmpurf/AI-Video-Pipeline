# PHASE C Locked Asset Rules

## What can become `locked_after_human_review`
- Candidate assets with explicit reviewer approval.
- Only assets in `AssetStatus.candidate` that pass required review fields.
- The decision record must target `locked_after_human_review`.
- The lock is executed through `ReviewLocker.lock_asset` or `ReviewLocker.approve_candidate`.

## What cannot become `locked_after_human_review`
- Assets with `ReviewDecision` not equal to `approve`.
- Assets whose source path indicates mock output generation.
- Assets rejected by review (`AssetStatus.rejected`).
- Legacy/placeholder test artifacts unless explicitly reviewed.

## Why mock outputs cannot be locked
- Mock outputs are synthetic preview artifacts and do not represent production final output.
- They are created for pipeline validation only and may not satisfy human review completeness.
- Phase C enforces this by rejecting lock attempts where source path indicates a mock output.

## Why shot keyframes need human review
- Keyframes directly influence shot continuity and visual match for subsequent prompts.
- Automatic locking can propagate mistakes across sequence planning.
- Human approval ensures continuity and quality before final lock.

## Why A-level assets and SHOT-level outputs are separate
- `asset_type="audio|image|video|document"` and role-based identity are tracked independently.
- Shot-level outputs (`role=shot_video`) represent sequence outputs.
- Source-level assets (`role=source`) and keyframes remain independently selectable and trackable.
- This separation avoids implicit locking of every related artifact from a single decision.

## Duplicate vs variant vs continuity
- `exact_duplicate`: same file/sha group, one canonical record is selected.
- `near_duplicate_variant`: visually close variation, not rejected, kept as independent candidates.
- `continuity_pair`: intentionally similar assets across shots; do not deduplicate.
- `derived_from`/`alternate_candidate`/`replaces`/`rejected_due_to`: used for lineage and decision traceability, not automatic lock control.

## Required review fields before lock
- `review_id`
- `logical_id`
- `candidate_id`
- `decision` must be `approve`
- `reviewer` must be explicit and user-approved
- `target_status_after_decision`
- `created_at`
- `source_path`

## Policy checks
- `system` reviewer is not allowed to finalize locks for production candidates.
- Review decisions always append an immutable `review_records.jsonl` entry.
- Rejected/archived records are excluded from default references.