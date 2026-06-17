# IMAGE REVIEW TEMPLATE

## Review Header
- review_id: {{review_id}}
- logical_id: {{logical_id}}
- candidate_id: {{candidate_id}}
- reviewer: {{reviewer}}
- decision: approve | reject | needs_rerun | hold
- created_at: {{created_at}}

## Image Checklist
- Composition: pass/fail
- Face quality: pass/fail
- Noise / compression: pass/fail
- Prompt alignment: pass/fail
- Notes:
  - {{reviewer_notes}}

## Decision
- target_status_after_decision: {{target_status_after_decision}}
- issue_tags: {{issue_tags}}