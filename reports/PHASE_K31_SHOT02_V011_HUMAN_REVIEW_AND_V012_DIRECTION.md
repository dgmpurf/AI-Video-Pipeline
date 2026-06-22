# PHASE K31 SHOT-02 V011 Human Review And V012 Direction

Date: 2026-06-22

## Scope

- Review human feedback for `SHOT-02-V011`.
- Verify the actual submitted V011 references from recorded submit evidence.
- Record V011 rejection and prepare V012 correction direction only.
- Do not run Dreamina, submit, query, download, retry, resubmit, batch, logout, or relogin.
- Do not prepare a V012 live package in this phase.

## V011 Technical Status

`SHOT-02-V011` was submitted, queried, downloaded, validated, and prepared for human review.

Technical result from `reports/PHASE_K30_SHOT02_V011_QUERY_DOWNLOAD_RESULT.md`:

- gen_status: `success`
- queue_status: `Finish`
- downloaded mp4: `productions/chi_yan_tian_qiong/runs/live/SHOT-02-V011_20260622_145250/SHOT-02-V011_multimodal_identity_locked_followup_attack.mp4`
- file_size_bytes: `6399405`
- sha256: `cf4f872531daa3524198f80d228bcaa5d082460c08f28a12743a772adf6c1ced`
- duration_seconds: `4.016667`
- resolution: `1280x720`
- fps: `24.149377593360995`
- frame_count: `97`
- contact sheet: `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V011/SHOT-02-V011_contact_sheet.jpg`

## Human Review Result

Status: `rejected_for_final_identity_and_rhythm_failed`

Human review conclusion:

- V011 does not pass final review.
- Shuangji still appears male-coded / male cultivator-like, despite the V011 identity reference package.
- Fight rhythm is still too slow.
- The action feels like staged performance sparring rather than fast collision-based close combat.
- Desired feel is faster staccato `da-da-da` close-range exchange with sharper contact and stronger collision feel.

Guardrails:

- `final_master=false`
- `locked=false`
- `usable_for_final=false`
- `usable_video_candidate=false`
- `official_video_candidate=false`
- `usable_as_identity_reference=false`
- `usable_as_visual_reference_for_next_generation=false`
- `usable_as_loose_action_composition_reference=false`

Do not use V011 as final footage or as visual reference for the next generation.

## Actual Submit Reference Verification

Evidence inspected:

- `reports/PHASE_K29_SHOT02_V011_SINGLE_SUBMIT_RESULT.md`
- `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V011.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V011.csv`
- `reports/PHASE_K28_SHOT02_V011_MULTIMODAL_PACKAGE_READY.md`

The recorded V011 submit command did include 5 image references.

Actual submitted references:

1. `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
2. `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
3. `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg`
4. `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V010/frame_06.jpg`
5. `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png`

Verification answers:

- Fenshou locked subject ref included: yes
- Shuangji locked subject ref included: yes
- V009 1.00s continuity frame included: yes
- V010 frame_06 included: yes
- A-SC-TEMPLE-COURTYARD-004 scene anchor included: yes
- task_type actually submitted: `multimodal2video`
- package/submit mismatch: no

Classification:

V011 failed despite correct submitted references. This is a model reference-following / identity preservation failure, not a missing package-reference failure.

## Shuangji Reference Search

Asset registry inspected:

`productions/chi_yan_tian_qiong/assets/asset_registry.json`

Current Shuangji reference found:

- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- logical_id: `A-CH-B-SUBJECT-001`
- status: `locked_after_human_review`
- review_status: `approved`
- role: `character`
- tags: `character`, `shuangji`, `subject`, `full_body`, `locked_ref`, `production_asset`, `production_candidate`
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`

No stronger Shuangji face / upper-body / portrait reference was found in the current asset registry.

Recommendation:

If identity stability remains the priority, create or select a clearer Shuangji identity/action keyframe before another video attempt, especially a face/upper-body/action pose reference that preserves female identity under motion.

## V012 Correction Direction

Do not use V010 or V011 frames as image references for V012. They risk reinforcing:

- wrong Shuangji identity
- male-coded Shuangji drift
- slow staged sparring rhythm
- pose-to-pose or arm-lock motion

Recommended reference strategy:

- Use locked Fenshou identity reference.
- Use locked Shuangji identity reference.
- Use a clean locked scene anchor.
- Avoid contaminated V010/V011 frames.
- If possible, first create or select a clearer Shuangji face/upper-body/action keyframe and use it as a higher-priority identity/action reference.

## V012 Rhythm Direction

Change action language away from:

- slow forearm pressure
- press / hold
- static arm-lock
- long hit-stop
- performance sparring
- pose-to-pose demonstration

Prefer:

- rapid three-beat close combat
- contact-recoil-contact rhythm
- fast staccato `da-da-da` timing
- short palm
- wrist slap
- forearm deflection
- immediate recoil after contact
- shoulder/elbow/wrist adjustments
- visible shoe skid and wet-floor splash
- no slow motion
- no frozen pullback
- true speed

Timing recommendation:

- Ask for 3 quick contact beats in the first `0.8-1.2s`.
- Final edit target: `0.6s-1.2s`.
- Do not structure the whole clip as a slow 4s hold.

Optional later local edit strategy:

If generated motion has useful contact beats but is slightly slow, test a `1.25x-1.5x` speed-up cut. Do not rely on speed-up to fix missing contact or wrong identity.

## V012 Prompt Direction Notes

Avoid:

- slow forearm pushing
- static arm-lock
- pose-to-pose sparring
- long hit-stop
- performance demonstration feel
- V010/V011 contaminated identity frames
- male-coded Shuangji drift

Prefer:

- rapid three-beat close combat
- contact-recoil-contact rhythm
- short palm, wrist slap, forearm deflection
- visible shoe skid and splash
- no slow motion
- no frozen pullback
- true speed
- final edit target `0.6s-1.2s`

## Next Step

Do not submit anything from this report.

Recommended next project step:

Prepare V012 only after deciding whether to create/select a stronger Shuangji identity/action reference first. If no stronger reference is available, prioritize that identity keyframe work before another video attempt.

Final verdict: `SHOT_02_V011_REJECTED_V012_DIRECTION_READY`
