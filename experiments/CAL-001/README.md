# CAL-001 Project-Wide Prompt Calibration

## Purpose

CAL-001 compares four prompt architectures across seven stable benchmark families using three independent replicates per architecture. This tree is a fixed no-run definition and contains no generated media.

## Fixed versus adaptive experiments

CAL-001A contains exactly 84 fixed experiments known before execution. No row depends on another result, and no winner-based replacement, prompt rewrite, retry, resubmit, task addition, or manifest expansion is allowed. Adaptive work belongs only to separately authorized CAL-001B.

## CAL-001A versus CAL-001B

CAL-001A has a recorded conditional pre-authorization but execution_authority_active=false. CAL-001B is excluded and requires separate English authorization.

## Directory structure

- fixtures: validated existing project media registry; no media is copied here.
- prompts: 28 unique provider-prompt definitions shared by replicates.
- packages: 84 no-submit experiment packages.
- manifests: fixed 84-row CSV.
- schemas and datasets: technical record, scoring, failure-label, result, and visual-review templates.
- reviews: human and independent P2 checklists.
- budget and matrices: fixed arithmetic and full experiment map.

## No-run state

Dreamina was not run. All packages and manifest rows set no_submit=true; submit, query, download, retry, resubmit, and batch authority are false; final_master=false; locked=false. Future output directories are named but not created.

## Activation sequence

1. Complete CAL-001-P2 independent review.
2. Obtain explicit human acceptance of the fixed manifest and inventory hashes.
3. Run CAL-001-P3 activation-precondition audit.
4. Verify live Dreamina command facts, login, credits, and task cost in the authorized execution environment.
5. Activate CAL-001A only if every precondition passes.

## Result-record flow

Future execution writes technical facts to the experiment results dataset and leaves non-applicable visual scores null. Successful downloaded videos follow the planned metadata, 0/1/2/3/4-second frames, final readable frame, and 3x2 contact-sheet workflow. No cut is created by default.

## Human review boundary

P1-R2 assigns no visual scores or outcomes. Human manifest acceptance is false, and future generated videos require human visual review before any production use.

## Final and lock boundary

No manifest acceptance, execution result, score, or visual success automatically sets final or lock. final_master=true and locked=true require explicit human approval outside this phase.
