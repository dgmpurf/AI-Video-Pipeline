# Action Reference Video Library Plan

## Purpose

Plan a lightweight action reference video library for future SHOT-04 R02 and combat-action review. This plan does not create, download, copy, edit, or upload media. It does not authorize Dreamina. It is evidence-only and should be transformed by ChatGPT Pro Extended or the human before becoming official Source.

Core rule:

```text
Reference video is action grammar, not active generation input by default.
```

## What To Search

- Short real or staged fight clips showing shoulder pressure into a guard.
- Wuxia or martial-arts blocking examples with crossed guard compression.
- Wet-floor skid, rain, slick stone, or slippery footwork examples.
- Short edit windows where the useful action happens inside 0.0s-1.5s.
- Clips with clear force transfer: attacker drive, defender compression, skid/recovery, counter-readiness.
- Examples where the tail keeps motion alive instead of ending in a static pose.

## What Not To Search

- Gore, severe injury, real harm, or unsafe impact footage.
- Clips whose primary value is wall damage, body-wall collision, or destructive breakage.
- Long choreography reels where the desired action cannot be isolated.
- Highly stylized VFX blasts, shockwaves, or magic impacts.
- Content requiring login, paid access, scraping, or rights-unclear reuse.
- Any reference intended to be copied as final art or used as active generation input without a separate rights/safety decision.

## Naming Convention

Use paired media and annotation files:

```text
REF_001.mp4
REF_001.md
REF_002.mp4
REF_002.md
```

Suggested folder when separately authorized:

```text
productions/chi_yan_tian_qiong/reference_library/action_grammar/
```

No media should be created, copied, downloaded, or staged under this Part 4 task.

## Lightweight Annotation Template

```markdown
# REF_001 Action Grammar Note

- reference_id: REF_001
- source_url_or_origin: unknown
- rights_status: unknown / public_reference_only / licensed / owned
- safe_for_upload_as_evidence: unknown
- active_generation_input_allowed: false
- shot_relevance: SHOT-04 R02 near-wall guard-clash
- action_type: shoulder/forearm pressure into crossed guard
- environment_features: wet floor / rain / corridor / wall proximity
- useful_window: 0.00s-1.50s
- what_to_learn: timing, pressure, skid, guard compression
- what_not_to_copy: identity, costume, exact choreography, copyrighted framing
- notes:
```

## Timeline Breakdown Template

Use the same markers as the K242V/K244 front-loaded edit-window plan:

| Marker | Annotation |
| --- | --- |
| 0.00s | Starting pose/action state; already close or long approach? |
| 0.10s | First pressure/contact cue. |
| 0.35s | Main guard compression, shoulder/forearm drive, or force transfer. |
| 0.65s | Skid, rain/floor feedback, body reaction, hit-stop, or pressure lock. |
| 1.00s | Recovery/counter-readiness begins. |
| 1.35s | Best cut window candidate. |
| 1.50s | End of likely useful edit window; note whether motion stays alive. |

## Review Scoring Sheet

Score each field from 1 to 5.

| Field | Score 1 | Score 3 | Score 5 |
| --- | --- | --- | --- |
| action clarity | unreadable / vague push | readable but imperfect | clear force chain and action result |
| pressure | weak / decorative | moderate pressure | strong shoulder/forearm drive and guard compression |
| wet-floor feedback | absent | some skid/spray | clear skid, spray, or slick-floor reaction |
| edit-window usefulness | useful beat after 1.5s or not isolated | partial 0.0s-1.5s value | strong useful beat inside 0.0s-1.5s |
| similarity to SHOT-04 R02 | generic / off-route | partial match | near-wall guard-clash match without wall collision |

Optional reviewer notes:

```markdown
- best_frame_or_time:
- main action lesson:
- failure risk if copied:
- prompt influence:
- review influence:
```

## How Reference Videos Should Influence Prompts

- Use references to define action grammar: pressure, timing, skid, guard compression, and counter-readiness.
- Convert visual observations into prompt verbs and timing clauses, not copied image details.
- Use the reference to justify first-frame closeness and short edit-window targets.
- Do not add reference video as an active input by default.
- Do not copy identity, costumes, camera compositions, logos, watermarks, or distinctive copyrighted choreography.
- Keep SHOT-04 R02 route constraints intact: no body-wall contact, no wall hit, no wall damage, no static pose-out.

## How Reference Videos Should Influence Visual Review

- Compare generated media against action clarity, pressure, wet-floor feedback, edit-window usefulness, and similarity to SHOT-04 R02.
- Ask whether the output shows a readable force chain, not whether it imitates the reference.
- Record whether the useful action appears by 1.35s-1.50s.
- Flag static tail, long approach, hand-push, missing skid, identity drift, duplicate bodies, and wall-contact leakage.
- Use the scoring sheet to separate "technically generated" from "visually useful."

## Copyright / Safety / No Final-Asset-Use Warning

- Reference videos are research and action-grammar evidence only.
- Do not treat reference videos as final production assets.
- Do not upload, redistribute, or use a reference as active generation input unless rights and safety are separately reviewed.
- Avoid violent injury, gore, unsafe real harm, or identifiable private-person footage.
- Keep source URLs and rights status in the annotation note.

## Relation To CTRL Assets / Action Grammar

- Action reference videos behave like CTRL/action grammar assets, not identity or final-frame assets.
- They may inform timing, force direction, and review rubric.
- They should not override character identity refs, location continuity, Source governance, or human final/lock approval.
- A future CTRL asset may be derived only after separate authorization and rights/safety review.

## Starter Reference Pair Template

```text
REF_001.mp4
REF_001.md
```

`REF_001.md` should contain:

```markdown
# REF_001 Action Grammar Note

- reference_id: REF_001
- active_generation_input_allowed: false
- action clarity score:
- pressure score:
- wet-floor feedback score:
- edit-window usefulness score:
- similarity to SHOT-04 R02 score:

## Timeline

| Marker | Note |
| --- | --- |
| 0.00s |  |
| 0.10s |  |
| 0.35s |  |
| 0.65s |  |
| 1.00s |  |
| 1.35s |  |
| 1.50s |  |
```
