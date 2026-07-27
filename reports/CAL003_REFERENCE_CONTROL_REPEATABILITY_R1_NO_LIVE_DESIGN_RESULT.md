# CAL003 Reference Control Repeatability R1 No-Live Design Result

## 1. Actual Decision

`CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_NO_LIVE_DESIGN_AND_STATIC_AUDIT_COMPLETE`

## 2. Starting Checkpoint

`main` at `b16c6522c3f09a3b3f81ff816b2090d4cefe5efb`, with `origin/main` aligned before activation.

## 3. Authorization Profile And Lifecycle

Authorization bytes=`5866`; SHA-256=`3c63594bbfb9325958ea846796fe37efdb462e6ded3fa74f4ac118ef47797601`; Base64 characters=`7824`. The authorization remains unactivated through all in-memory checks and is consumed at the first authorized repository write.

## 4. CAL-002 Evidence Bindings

The final review record, review report, review evidence manifest, governance report, C02 review contract, common Prompt source, PUSH reference, and IMPACT reference are bound byte-for-byte and to HEAD.

## 5. CAL-002 Bounded Versus Generalized Boundary

Preserved decision: `ROUTE_A_BOUNDED_REFERENCE_SPECIFIC_MOTION_DIFFERENTIATION_CAPABILITY_ESTABLISHED_IN_C02_BUT_NOT_GENERALIZED_TO_PRODUCTION`. CAL-002 established bounded evidence in one controlled pair, not generalized reliability.

## 6. CAL-003 Independent-Experiment Classification

CAL-003 is a new independent experiment. It is not C02/C03, a retry, resubmit, redownload, review reopening, Route A reopening, R02 reopening, production recovery, or production re-entry.

## 7. Scientific Question And Hypothesis

The design tests whether family-specific motion differentiation repeats across three stochastic replicates per family under byte-identical text and identical non-reference Provider fields.

## 8. Six-Task Replicate Structure

PUSH-01, PUSH-02, PUSH-03, IMPACT-01, IMPACT-02, and IMPACT-03 form three ordinal matched pairs.

## 9. Exact Common Prompt Binding

Path=`experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DESIGN/prompts/common.txt`; bytes=`2010`; SHA-256=`bbaadf89c81a60336742a17925bc6d3cf54009e1f99818c2300b90920af6b93d`; the existing terminal LF is preserved byte-for-byte.

## 10. Reference Bindings

PUSH=`experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CLEAN_FULL_DURATION_MULTI_BEAT_REFERENCE_V0_2/media/ACTION_REF_PUSH_02.mp4` / `6006b7abc88a53978a9a7993a0b7852179ddbbbcd960d13f07ebc68218872ed6`. IMPACT=`experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CLEAN_FULL_DURATION_MULTI_BEAT_REFERENCE_V0_2/media/ACTION_REF_IMPACT_02.mp4` / `a0a2662dc598f4980d3f1f22cff2c2915a0f422d797f0e09eb53e8e78110623c`.

## 11. Provider-Payload Equality Design

All three packages within each family have byte-identical Provider payloads. All six share identical non-reference Provider fields.

## 12. Four-Pointer Cross-Family Isolation

The only permitted cross-family Provider-payload differences are reference_id, reference_path, reference_sha256, and reference_upload_binding. Non-allowlisted differences=`0`.

## 13. Within-Family Future-Argv Equality

PUSH future argv equality=`3/3`; IMPACT future argv equality=`3/3`. Replicate, task, submission-position, and blind metadata are excluded.

## 14. Fixed Future Submission Order

`PUSH-01, IMPACT-01, IMPACT-02, PUSH-02, PUSH-03, IMPACT-03`.

## 15. No-Parallelism Rule

Parallelism=`0`; maximum in-flight submit process=`1`; a failure stops later submissions.

## 16. Inactive Budget Values

Maximum unit decrement=`160`; proposed total ceiling=`960`; budget_active=`false`.

## 17. Future Runtime-Credit And Help Requirements

Fresh user_credit and runtime Help verification are mandatory before any separately authorized live phase. Neither is called here.

## 18. Blind Mapping Commitment Protocol

Mapping status=`NOT_MATERIALIZED`. A future one-time secure permutation, salt, commitment, freeze, and reveal sequence requires fresh authority.

## 19. Complete-MP4 Review Requirement

All six future outputs must be reviewed from first frame through final frame. Contact sheets are assistance only.

## 20. Twelve Dimensions And Two Signatures

Each blind output is scored on all 12 committed motion dimensions against both PUSH and IMPACT signatures before unblinding.

## 21. Sample Gate

A sample requires technical validity, complete review, own score >= 8, margin >= 3, zero material sentinels, no role conflict, and no action-family failure.

## 22. Family Repeatability Gate

Each family requires at least 2/3 sample passes, median own score >= 8, median margin >= 3, and no more than one reference-ignored sample.

## 23. Ordinal-Pair Gate

At least 2/3 ordinal pairs must be observably differentiated after valid complete-MP4 review and post-unblinding Gate derivation.

## 24. Positive-Result Interpretation Boundary

Maximum positive interpretation=`CAL003_R1_INITIAL_WITHIN_PAIR_REPEATABILITY_EVIDENCE_ESTABLISHED_REQUIRES_NEXT_EXPERIMENT_HUMAN_DECISION`. It does not prove generalized Provider reliability, production readiness, or a universal motion-only contract.

## 25. Static Audit

Static audit=`360/360 PASS`; failures=`0`; skips=`0`; warnings=`0`.

## 26. Exact Sixteen-File Write Set

The write set contains exactly 16 new paths: one human decision, one design spec, one copied Prompt, six packages, two manifests, one submission order, one blind-review protocol, one review contract, one static audit, and this report.

## 27. Evidence Coverage

Non-self output coverage=`15/15`; committed-input coverage=`8/8`; total unique bound paths=`23`.

## 28. Source Media Prompt Package And Reference Immutability

Existing Sources, media, Prompts, packages, references, prior experiments, and prior reports remain unchanged. The CAL-003 Prompt is an exact copy.

## 29. Dreamina And Provider Call Counts

Dreamina=`0`; Provider=`0`; version/user_credit/Help=`0/0/0`; submit/query/download/retry/resubmit/batch=`0/0/0/0/0/0`.

## 30. Production Final And Lock Boundaries

live_authority=false; production_approved=false; fixed_task_completion=false; final_master=false; locked=false; C03_authorized=false; original_R02_blocked=true.

## 31. Commit And Push Outcome

At report serialization, Git finalization is pending the already authorized exact-scope validation. Required commit message is `design(cal003): prepare reference repeatability R1`; one push to `origin/main` is permitted. The immutable terminal receipt records the actual outcome; no post-commit report mutation is allowed.

## 32. Exact Next Phase

`CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_LIVE_AUTHORIZATION_HUMAN_DECISION`

**No live generation authority was created.**

**The credit limits are inactive design ceilings only.**

**CAL-003 R1 remains unexecuted until a fresh exact human live authorization is issued.**
