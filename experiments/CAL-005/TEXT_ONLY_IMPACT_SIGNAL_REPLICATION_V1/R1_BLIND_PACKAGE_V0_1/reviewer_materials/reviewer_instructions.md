# CAL-005 R1 Blind Complete-MP4 Review Instructions

Use only the exact nine files supplied for Batch A.
Read `reviewer_manifest.json` first and validate the complete input inventory.
Review each of B01.mp4 through B06.mp4 from the first frame through the final frame.
Score PUSH and IMPACT independently for all twelve dimensions in `review_contract.json`.
Provide visible evidence for every dimension and a gapless timeline from 0.00 seconds through the complete observed ending.
Evaluate all required observations and all four material-copy sentinels.
Do not request, identify, or infer a hidden mapping, condition, Prompt stratum, canonical source, or experiment-level result.
Create one deterministic JSON review record per alias and freeze all six records before any mapping reveal.

Return exactly one ZIP named `CAL005_R1_BLIND_REVIEW_BATCH_A_V0_1.zip`.
Its exact member order must be:

1. B01_review.json
2. B02_review.json
3. B03_review.json
4. B04_review.json
5. B05_review.json
6. B06_review.json
7. batch_review_summary.json
8. SHA256SUMS

`SHA256SUMS` must list exactly the first seven members in that order and must not list itself.
Do not include MP4 files, reviewer input documents, mapping data, condition or Prompt identities, submit IDs, or result URLs in the returned ZIP.
