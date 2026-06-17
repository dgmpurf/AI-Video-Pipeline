# Shot Design Template

## Shot record fields
- `shot_id`: logical shot identifier
- `sequence_id`: sequence group identifier
- `scene_id`: scene identifier
- `shot_index`: position in shot order
- `title`: short human title
- `shot_type`: establishing, action, movement, dialogue, insert, transition
- `duration_seconds`: shot duration estimate
- `story_beat`: narrative meaning of the shot
- `visual_goal`: required visual outcome
- `action_goal`: action intent (optional only for establishing shots)
- `camera_goal`: camera intent
- `required_asset_ids`: ordered list of asset logical ids

## Continuity rules
- If `previous_shot_id` is set, that shot must exist.
- If `next_shot_id` is set, that shot must exist.
- Previous/next references must be symmetric.
- Shot continuity should follow `shot_index` sequence.

## Review fields
- `status`: draft, planned, approved, locked, rejected, archived
- `review_status`: pending_review, approved, rejected, needs_rerun