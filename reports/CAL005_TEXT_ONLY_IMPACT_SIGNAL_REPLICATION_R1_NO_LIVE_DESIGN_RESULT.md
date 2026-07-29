# CAL-005 Text-Only IMPACT Signal Replication R1 No-Live Design

## Result

Decision: `CAL005_R1_NO_LIVE_DESIGN_COMPLETE_READY_FOR_REVIEW`

The package defines a six-task, two-condition replication of the partial CAL-004 text-only IMPACT signal. It creates design evidence only and creates no live authority.

## Scientific Question

Does the CAL-004 text-only IMPACT signal repeat when neutral and IMPACT-hard Prompts are compared under the same `text2video` route with no motion reference?

## Design

- Experiment/program/round: `CAL-005 / TEXT_ONLY_IMPACT_SIGNAL_REPLICATION_V1 / R1`
- Status: `NO_LIVE_DESIGN_ONLY`
- N0R: `ACTION_NEUTRAL_MINIMAL`, `text2video`, no motion reference, three replicates
- I0R: `IMPACT_CAUSAL_HARD`, `text2video`, no motion reference, three replicates
- Exact fixed order: `N0R-01, I0R-01, I0R-02, N0R-02, N0R-03, I0R-03`
- Randomness generated: `false`

Both Prompt files are byte-identical copies of their committed CAL-004 counterparts:

- `ACTION_NEUTRAL_MINIMAL`: 1978 bytes, SHA-256 `c15f93ee8ee55fccb827cbea8683c0538e13cefd138d0ae1a22761dce7c20ce0`
- `IMPACT_CAUSAL_HARD`: 2287 bytes, SHA-256 `c38e8bb135d6d9f29d510c2fb059b8f4a9ce7948626c19f43f98ad564b8422a5`

## Controls And Review

The CAL-004 actors, clothing, scene, camera, composition, lighting, style and technical planning values are preserved. All six tasks use `text2video`, one planned video, `seedance2.0_vip`, 5 seconds, 16:9 and 720p, with no image, video or audio reference.

Future review must be blind and use complete MP4s. It reuses the CAL-004 PUSH/IMPACT dual-signature framework, sample thresholds of IMPACT >= 8 and margin >= 3, and the three-sample condition Gate. The primary contrast is I0R versus N0R. No statistical-significance claim is authorized from three replicates.

## Historical Budget

- Last observed balance: `661`
- Last observed text2video unit cost: `70`
- Six-task planned decrement: `420`
- Arithmetic remainder: `241`
- Fresh balance asserted: `false`

## Authority Boundary

Fresh `user_credit`, current `text2video` help, login/canary verification, actual unit-cost confirmation and fresh human submit authorization are required before any future activation.

No Dreamina, Provider, credit, submit, query, download, retry, resubmit, media, randomness or Source operation was performed. `production_approved=false`, `fixed_task_completion=false`, `final_master=false`, and `locked=false`.

Next phase: `CAL005_R1_NO_LIVE_DESIGN_REVIEW_AND_SUBMIT_ACTIVATION_HUMAN_DECISION`.
