# CAL-003 R1 Blind Package Windows Durability Repair

## Decision

- Actual decision: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_BLIND_PACKAGE_WINDOWS_DURABILITY_REPAIR_AND_AUDIT_COMPLETE`
- Next phase: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_BLIND_PACKAGE_REPAIR_AUDIT_COMPLETE_REEXECUTION_AUTHORIZATION_HUMAN_DECISION`
- Starting checkpoint: `900bc32e3b90fbfbc1b182c332c8181a77c3c987`
- Branch: `main`
- Starting `origin/main`: `900bc32e3b90fbfbc1b182c332c8181a77c3c987`

The repair validates a persistence implementation only.

It does not recreate the prior random mapping or salt.

The failed one-time authorization remains exhausted.

A completely fresh blind-package execution authorization is required.

## Authorization

- Canonical authorization bytes: `4788`
- Canonical authorization SHA-256: `f2096d7c1ed298aa2a2f31374ca09cc5ff729ed2a7a67b8c070436db4b391015`
- Derived Base64 characters: `6384`
- UTF-8 round trip: `PASS`
- Authorization activated/consumed/reusable: `true / true / false`
- Activation event: first creation of the exact repair temporary root

## Prior Failure Boundary

The five prior R1 blind-package failure records remain historical failure
evidence and were not rewritten. Durable repository evidence establishes an
`OSError`, persisted phase `startup`, one permutation attempt, one salt
generation attempt, zero review-visible media, no surviving sealed ZIP, and no
public mapping or salt.

The accepted bounded repair target separately records the high-confidence
Windows reproduction: `os.fsync()` on a read-only `rb` file descriptor raised
`OSError` with safe numeric errno `9`. The deleted transient script is not
treated as durable repository evidence.

The historical `failure_phase=startup` value was insufficient because it did
not identify the risky persistence operation. The new implementation records
the phase and operation before each write, flush, integrity check, rename, and
cleanup operation.

## Persistent Implementation

Exactly four implementation files were created:

1. `tools/cal003_blind_package/__init__.py`
2. `tools/cal003_blind_package/durability.py`
3. `tools/cal003_blind_package/failure_state.py`
4. `tools/cal003_blind_package/runner.py`

No committed `run_blind_package.py` existed at the starting checkpoint.

Implementation version:
`CAL003_BLIND_PACKAGE_WINDOWS_DURABILITY_V0_1`.

## Windows Durability Design

- Writable durability handle mode: `r+b`
- File durability order: `open -> flush -> os.fsync -> close`
- Read-only durability call sites: `0`
- Windows directory-fsync call sites: `0`
- Partial flow: writable flush, exact ZIP validation, then publication
- Publication: same-volume `os.replace(partial, final)`
- Final flow: writable flush followed by complete ZIP revalidation
- Copy-delete fallback: absent
- Internal retry: absent

Partial and final validation enforce a regular non-symlink file, reparse-point
rejection where standard-library metadata exposes it, ZIP integrity, exact
members, no duplicates, no absolute or traversal names, exact member SHA-256
values, and a caller-supplied commitment check.

## Failure State And Sanitization

Phases:

`STARTUP`, `SEALED_ZIP_WRITE`, `SEALED_PACKAGE_FILE_FLUSH`,
`SEALED_ZIP_INTEGRITY`, `ATOMIC_RENAME`,
`FINAL_PACKAGE_FILE_FLUSH`, `FINAL_ZIP_INTEGRITY`, `CLEANUP`, `COMPLETE`.

Operation codes:

`WRITE_PARTIAL_ZIP`, `FLUSH_PARTIAL_ZIP`, `VERIFY_PARTIAL_ZIP`,
`ATOMIC_REPLACE`, `FLUSH_FINAL_ZIP`, `VERIFY_FINAL_ZIP`,
`CLEANUP_TASK_CREATED_PATHS`.

Sanitized failure evidence contains only exception class, safe numeric errno,
safe numeric winerror where supported, failure phase, and operation code. It
does not persist raw exception text, arguments, traceback, path values, mapping,
salt, or source-to-alias data.

## Tests

Exactly four standard-library test files were created:

1. `tests/cal003_blind_package/test_windows_fsync_regression.py`
2. `tests/cal003_blind_package/test_atomic_zip_persistence.py`
3. `tests/cal003_blind_package/test_failure_state_sanitization.py`
4. `tests/cal003_blind_package/test_runner_nondisclosure.py`

Mirror validation:

- Compile: `PASS`
- Unit tests: `40`
- Failures/errors/skips/warnings: `0 / 0 / 0 / 0`
- Preliminary static inspection: `12/12 PASS`

Repository validation:

- Compile: `PASS`
- Unit tests: `40`
- Failures/errors/skips/warnings: `0 / 0 / 0 / 0`

Regression results:

- Legacy Windows read-only-fsync reproduction: `PASS`, errno `9`
- Repaired writable helper: `PASS`
- Partial ZIP durability: `PASS`
- Final ZIP durability: `PASS`
- Atomic replacement: `PASS`
- Exact member and member-hash verification: `PASS`
- Commitment verification: `PASS`
- Cleanup confinement: `PASS`
- Failure-phase recording: `PASS`
- Error sanitization: `PASS`
- Nondisclosure: `PASS`

Raw test stdout and stderr were not persisted. Only command identity, return
code, byte length, SHA-256, counts, and pass/failure summaries appear in the
repair record.

## Independent Audit

- Static checks: `96`
- Passes/failures/skips/warnings: `96 / 0 / 0 / 0`
- Category distribution: `12 / 24 / 20 / 16 / 12 / 12`
- Overall result: `PASS`

The categories cover repository and input bindings, Windows file durability,
atomic ZIP persistence, failure-state sanitization, nondisclosure and synthetic
fixtures, and output-path/protected-state controls.

## Evidence And Scope

- Exact write set: `12` new file paths
- Implementation files: `4`
- Test files: `4`
- Repair record: `1`
- Static audit: `1`
- Evidence manifest: `1`
- Governance report: `1`
- Output coverage: `11/11`
- Committed-input coverage: `6/6`
- Total unique bound paths: `17`
- Sensitive-data scan: `PASS`
- Protected-state validation: `PASS`
- Temporary cleanup: `PASS`

All five prior R1 blind-package failure records, all R1 download/query/submit
evidence, all canonical media and technical records, CAL-002 artifacts,
Prompts, packages, references, prior reports, production artifacts, and Source
files remain unchanged.

## No-Live Boundary

- Dreamina, Provider, version, user-credit, and Help calls: `0`
- Credit operations: `0`
- Random permutation and random salt generation: `0 / 0`
- Real mapping creation and canonical media reads: `0 / 0`
- ffmpeg, ffprobe, remux, and padding operations: `0`
- Production sealed ZIP and blinded media creation: `0 / 0`
- Semantic review, review freeze, unblinding, and Gate derivation: `0`
- Repeatability conclusion known: `false`

## Production Boundary

- Production reentry authorized: `false`
- Production approved: `false`
- Fixed task completion: `false`
- Final master: `false`
- Locked: `false`
- C02 reopened: `false`
- C03 authorized: `false`
- Original R02 blocked: `true`
- R02 authorized: `false`

## Git Finalization

At report serialization, commit and push are pending exact-scope validation.
The terminal receipt records their actual outcome. The only authorized commit
message is:

`fix(cal003): harden blind package Windows durability`

No automatic blind-package reexecution is authorized.
