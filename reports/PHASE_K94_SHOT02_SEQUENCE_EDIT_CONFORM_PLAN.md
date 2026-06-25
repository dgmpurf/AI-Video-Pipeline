# PHASE K94 - SHOT-02 Sequence Edit Conform Plan

## Purpose

This phase creates a SHOT-02 sequence-level edit/conform plan after the K93 combat-stage closeout.

This is planning only. It is not final master creation.

No Dreamina command was run. No submit/query/download happened. No AI generation happened. No media files were created, edited, moved, deleted, or staged.

## Current Locked Candidate

- Candidate id: `SHOT-02-V018-speed-1p18x`
- Role: main current combat segment
- Path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/speed_diagnostics/SHOT-02-V018/SHOT-02-V018_speed_1p18x.mp4`
- SHA256: `f48ed132f0d8ff9a7c853698e4102900ebedcc86dbfb2f1ad680de96fb044a08`
- Duration seconds: `4.270315091210613`
- Frame count: `103`
- Resolution: `1280x720`
- FPS: `24.12`
- `locked=true` only for `lock_scope=shot02_current_edit_candidate`
- `final_master=false`
- `whole_film_final_master=false`

## Backup Candidate

- Candidate id: `SHOT-02-V018-speed-1p12x`
- Role: conservative backup if `1.18x` feels too fast
- Path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/speed_diagnostics/SHOT-02-V018/SHOT-02-V018_speed_1p12x.mp4`
- SHA256: `d05e106d5731b1b7fc68fb679819f723965edda4dcbd9afb05def3388b92486b`
- Duration seconds: `4.519071310116086`
- Frame count: `109`

Use this only if `1.18x` feels too fast in full sequence context, after sound design or neighboring-shot pacing is considered.

## Historical Preservation

V013 CUT01 remains the historical locked passed segment.

- Candidate id: `SHOT-02-V013-CUT01-LOCKED`
- Path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V013/SHOT-02-V013_CUT01_0p00_to_2p20_best_close_combat_candidate.mp4`
- SHA256: `dae11211fa19818a947d865d789b16a35126da91de71b7ae5eb026b315548c23`
- Duration seconds: approximately `2.208333`
- Role: historical locked passed segment
- Preserved: true
- Not replaced by V018: true

V013 was not deleted, overwritten, moved, modified, or replaced. V013 is not displaced by V018 unless the human explicitly approves a future replacement.

## Supporting References

| Source | Role | Use policy |
| --- | --- | --- |
| `SHOT-02-V014-R02` | Strong positive energy/realism reference | Reference only, or later optional insert decision. Not an automatic insert. |
| `SHOT-02-V016` | Possible lower-body / line-steal insert reference | Later edit-conform decision only. Not an automatic insert. |
| `SHOT-02-V017` | Camera/framing reference but slow/soft action caution | Do not use as main action target. |
| `SHOT-02-V015` | Rejected caution reference | Avoid as a positive target. |

## Proposed Sequence Routes

### Route A - Primary Simple

Use `SHOT-02-V018-speed-1p18x` as the whole current combat beat without extra inserts.

Recommendation: recommended.

Reason: this is the cleanest route. It uses the locked current edit candidate, avoids overcomplication, and keeps the sequence from getting disturbed before full pacing is known.

### Route B - Conservative Pacing

Use `SHOT-02-V018-speed-1p12x` if `1.18x` feels too fast in the full sequence or sound design context.

Recommendation: backup.

Reason: it keeps the same V018 content while adding a little readability if neighboring shots are slower.

### Route C - Insert Experiment Later

Optionally test V016 lower-body / line-steal or V014-R02 energy insert in a future conform phase only.

Recommendation: not recommended immediately.

Reason: V014-R02/V016 inserts may improve variety, but they can also disrupt identity, pacing, or continuity. Do not disturb the locked current candidate before sequence-level pacing is known.

## Future Cut / Conform Notes

- Do not cut through hard contact beats.
- Potential trims are only at the very start or very end.
- Start: use V018 1.18x from `0.00s` unless later assembly needs a pre-roll trim.
- Beginning micro-trim zone: `0.00-0.15s` only if the first pose feels static.
- End: use near full `4.27s` unless the final beat feels too long.
- Ending micro-trim zone: last `0.10-0.30s` only if motion dies or the transition requires it.
- Do not create media in this phase.

Sound design notes for later:

- Add short cloth snap, armor jolt, foot skid, and water splash on contact beats.
- Keep hit-stop sound tight, not slow-motion-heavy.
- Do not cover weak contact with loud sound if visual contact is unclear.

Transition notes for later:

- Enter from the previous shot on motion or camera energy, not static pose.
- Exit on displacement, recovery, or re-entry direction.
- Use V018 1.12x if nearby shots are slower and 1.18x feels too abrupt.

## Risk Notes

- `1.18x` may become too fast depending on neighboring shots.
- `1.12x` may be safer if the full sequence needs more readability.
- V014-R02/V016 inserts may improve variety but can also disrupt identity/pacing continuity.
- Further generation may waste credits unless a specific missing beat is identified.

Avoid:

- V015-style repeated soft forearm/palm checks.
- Long binds.
- Push-hands rhythm.
- Overly dominant particles.
- Slow-motion-only impact.
- Auto-inserting V014-R02/V016 before conform review.

## Finalization Policy

- Current lock applies only to `shot02_current_edit_candidate`.
- Do not create final master without human approval.
- Do not replace V013 without human approval.
- Do not mark V018 as whole-film final master.
- Do not set `final_master=true`.

## Safety Confirmation

- No Dreamina command was run.
- `dreamina version` was not run.
- `dreamina user_credit` was not run.
- No submit/query/download happened.
- No AI media was generated.
- No media files were created, edited, moved, deleted, or staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- Project Source files were not modified.
- V013 media was preserved.

## Recommended Next Steps

A. Stop SHOT-02 combat generation and move to another shot.

B. Later do real local edit/conform with explicit media-edit authorization.

C. Later prepare Source update after more shot cycles accumulate.

## Output Files

- Sequence conform plan JSON: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/plans/SHOT-02_sequence_edit_conform_plan_after_combat_closeout.json`
- Report: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K94_SHOT02_SEQUENCE_EDIT_CONFORM_PLAN.md`

## Final Verdict

SHOT_02_SEQUENCE_EDIT_CONFORM_PLAN_READY_AFTER_COMBAT_CLOSEOUT
