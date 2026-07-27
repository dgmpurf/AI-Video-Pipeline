# CAL003 R1 Blind Technical Diagnostic Result

- Decision: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_BLIND_TECHNICAL_DIAGNOSTIC_COMPLETE`
- Diagnostic classification: `TRANSIENT_V0_2_ORCHESTRATION_OR_PARSE_DEFECT_HIGH_CONFIDENCE`
- Next phase: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_BLIND_TECHNICAL_DIAGNOSTIC_COMPLETE_REPAIR_OR_V0_3_AUTHORIZATION_HUMAN_DECISION`
- Starting checkpoint: `bafb50cf84e2d53186b02ef066fb690aab7ed051`

## Authorization And Prior Attempt

- New authorization: verified, activated, consumed, and non-reusable.
- Prior authorization remains exhausted and historical only.
- Prior mirror compile: PASS.
- Prior tests: 3 files / 73 methods / 71 passed / 2 failed / 0 errors / 0 skips / 0 warnings.
- Prior media reproductions, repository outputs, commits, and pushes: 0.
- The two prior failures were the same inclusive duration-boundary binary-float defect.

## Decimal Correction

- Duration values remain their original ffprobe decimal text.
- Expected duration: `5.085011`.
- Inclusive tolerance: `0.000001`.
- Acceptance rule: `abs(observed - expected) <= tolerance` using `Decimal`.
- Binary-float subtraction and `math.isclose` are not used for the duration gate.
- Exact, positive-boundary, and negative-boundary tests pass.
- Positive and negative beyond-boundary tests fail as required.
- Nonfinite, malformed, empty, overlong, integer, float, and null inputs fail safely.

## Bound Inputs

- Committed-input coverage: `10/10`.
- Runtime-media coverage: `6/6`.
- Existing V0.2 failure evidence and repair implementation remain unchanged.

## Validation

- Persistent module: `tools/cal003_blind_package/technical_validation.py`.
- Check catalog: 23 codes in exact order.
- Test files: 3.
- Mirror compile: PASS.
- Mirror tests: 106 methods / 0 failures / 0 errors / 0 skips / 0 warnings.
- Repository compile: PASS.
- Repository tests: 106 methods / 0 failures / 0 errors / 0 skips / 0 warnings.

## Deterministic Media Results

### C01

- Canonical path: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_01.mp4`
- Canonical bytes/SHA-256: `2299169` / `888bb1a27951cbe211b8a0506a5decb20c4f9aa2e9ba255a7832c1735836380c`
- Remux bytes: `2298618`
- Padding bytes: `1895686`
- Padded bytes/SHA-256: `4194304` / `25003635fd8aa8290e038d4820dd773f4f695882aea24179a7e6d3b13937ec91`
- Duration text/difference: `5.085011` / `0.000000`
- Probe: h264=True, yuv420p=True, size=1280x720, frames=121, rotation=0, forbidden metadata=0
- Evaluated checks: `21/21`
- First failed check: `none`
- Video framemd5 records/equivalent: `121` / `true`
- Audio framemd5 records/equivalent: `219` / `true`
- Technical result: `PASS`

### C02

- Canonical path: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_01.mp4`
- Canonical bytes/SHA-256: `2365925` / `86505a14f9afbb48db44b429e5b60b36094cb896acf34a23f19a4299785d591f`
- Remux bytes: `2365374`
- Padding bytes: `1828930`
- Padded bytes/SHA-256: `4194304` / `708b38e0f6019620621db02a45dc58b987afe4a092b5a5ce8531d25536a0c259`
- Duration text/difference: `5.085011` / `0.000000`
- Probe: h264=True, yuv420p=True, size=1280x720, frames=121, rotation=0, forbidden metadata=0
- Evaluated checks: `21/21`
- First failed check: `none`
- Video framemd5 records/equivalent: `121` / `true`
- Audio framemd5 records/equivalent: `219` / `true`
- Technical result: `PASS`

### C03

- Canonical path: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_02.mp4`
- Canonical bytes/SHA-256: `3147949` / `5bff5f8fe963d2db826b2195194a648ebe8823fb53078ee82d43f2adf9ff5ca9`
- Remux bytes: `3147398`
- Padding bytes: `1046906`
- Padded bytes/SHA-256: `4194304` / `b5c8ad4bf6426af47d738646c2fa17dc64d33c52647caa8dc9f610e38f1dc7e9`
- Duration text/difference: `5.085011` / `0.000000`
- Probe: h264=True, yuv420p=True, size=1280x720, frames=121, rotation=0, forbidden metadata=0
- Evaluated checks: `21/21`
- First failed check: `none`
- Video framemd5 records/equivalent: `121` / `true`
- Audio framemd5 records/equivalent: `219` / `true`
- Technical result: `PASS`

### C04

- Canonical path: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_02.mp4`
- Canonical bytes/SHA-256: `2852365` / `9db1d8dff40c5b69641be0e49f1ff107231bce88f618b218089a38214e85af21`
- Remux bytes: `2851814`
- Padding bytes: `1342490`
- Padded bytes/SHA-256: `4194304` / `11ae7266fcdaea4c111ff7de7815402de4ff5f93965e85ba3b2c7dae2d2c77ad`
- Duration text/difference: `5.085011` / `0.000000`
- Probe: h264=True, yuv420p=True, size=1280x720, frames=121, rotation=0, forbidden metadata=0
- Evaluated checks: `21/21`
- First failed check: `none`
- Video framemd5 records/equivalent: `121` / `true`
- Audio framemd5 records/equivalent: `219` / `true`
- Technical result: `PASS`

### C05

- Canonical path: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_03.mp4`
- Canonical bytes/SHA-256: `2417274` / `196945461a5a7c748e75911e962dde8523f99762bc64e0ffa2bb506d4f52f921`
- Remux bytes: `2416723`
- Padding bytes: `1777581`
- Padded bytes/SHA-256: `4194304` / `87b399536ffe25e888e1c843c6cbc54ceea5b5efc4d9fa23cb9e8f9ef3e1dab3`
- Duration text/difference: `5.085011` / `0.000000`
- Probe: h264=True, yuv420p=True, size=1280x720, frames=121, rotation=0, forbidden metadata=0
- Evaluated checks: `21/21`
- First failed check: `none`
- Video framemd5 records/equivalent: `121` / `true`
- Audio framemd5 records/equivalent: `219` / `true`
- Technical result: `PASS`

### C06

- Canonical path: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_03.mp4`
- Canonical bytes/SHA-256: `2419698` / `36bfa241c6262daccce1c87df53e8e589ef63a46fdfeef385a560ee55ea74cd9`
- Remux bytes: `2419147`
- Padding bytes: `1775157`
- Padded bytes/SHA-256: `4194304` / `c34d0c36c68099a9e74dfb5fc41d2745ac16e36f4deb4f0cd4dd1caaafac92e6`
- Duration text/difference: `5.085011` / `0.000000`
- Probe: h264=True, yuv420p=True, size=1280x720, frames=121, rotation=0, forbidden metadata=0
- Evaluated checks: `21/21`
- First failed check: `none`
- Video framemd5 records/equivalent: `121` / `true`
- Audio framemd5 records/equivalent: `219` / `true`
- Technical result: `PASS`

## Classification And Governance

- Technical PASS/FAIL: `6/0`.
- Local safety failures: `0`.
- Pairwise diagnostic comparisons: `15`.
- Diagnostic-to-canonical comparisons: `36`.
- Hash uniqueness: PASS.
- Canonical-hash difference: PASS.
- All six deterministic technical reproductions passed the explicit contract using exact decimal duration arithmetic.
- The historical V0.2 failure remains valid; the new evidence supports a high-confidence transient V0.2 orchestration or parsing defect.
- This result does not authorize automatic V0.3 execution.

## Scope And Cleanup

- Created repository paths: exactly 10.
- Evidence output coverage: `9/9`.
- Static audit: `72/72 PASS`.
- Temporary mirror, helper, remux, padded media, and framemd5 artifacts: removed.
- Sensitive-data scan: PASS.
- Protected-state validation: PASS.
- Dreamina, Provider, credit, permutation, salt, mapping, commitment, sealed ZIP, and review-visible media operations: 0.
- Semantic review, review freeze, unblinding, Gate derivation, and repeatability conclusion: false.
- production_reentry_authorized=false.
- production_approved=false.
- fixed_task_completion=false.
- final_master=false.
- locked=false.

## Git Finalization

- Commit target: `diagnose(cal003): harden blind technical validation`.
- Push target: `origin/main`.
- At report serialization these actions are pending governed finalization; the terminal receipt records their actual result.
