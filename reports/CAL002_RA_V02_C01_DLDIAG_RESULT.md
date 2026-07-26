# CAL002 Route A V0.2 C01 PUSH Diagnostic Download Result

## 1. Actual decision and next phase

Decision: `CAL002_ROUTE_A_V0_2_C01_PUSH_DIAGNOSTIC_DOWNLOAD_RECOVERY_FAILED`

Next phase: `CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_DOWNLOAD_FAILURE_RECOVERY_HUMAN_DECISION`

## 2. Starting checkpoint

`main`, local HEAD, and `origin/main` were aligned at `82688756f79aebf34673587d045948ee6ae930ad`.

## 3. Approval and lifecycle

Approval bytes/SHA-256: `4358` / `381cfe49512020c4c68f9679f2592db269460e16152fc3b8277763a52399c5d3`.
Authorization activated, consumed, reusable: `true / true / false`.

## 4. Query-recovery bindings

The governance report, evidence manifest, PUSH receipt, and continuity-only IMPACT receipt matched committed bytes and HEAD blobs.

## 5. Prior download failure

The previous attempt consumed one PUSH call, called no IMPACT task, retained no media, and lost its numeric child-process result.

## 6. Read-only triage classification

Prior classification: `LOCAL_EVIDENCE_HANDLER_RESULT_LOSS`, confidence `medium`.

## 7. Why PUSH-only recovery was selected

One diagnostic PUSH call was the narrowest gate capable of preserving the missing return-code and output-hash evidence.

## 8. Local toolchain

Python 3.10.11; ffprobe and ffmpeg `2023-03-27-git-f7abe92bd7-full_build-www.gyan.dev`.

## 9. Offline self-test

The hardened final suite passed `60 / 60 / 0`; it was invoked twice because the handler was tightened after the first clean pass. Dreamina calls and repository writes during self-test were zero.

## 10. Exact one-call boundary

Dreamina calls: `1`; PUSH: `1`; IMPACT: `0`; second PUSH: `0`.

## 11. Exact PUSH argv binding

Six elements, 177 bytes, SHA-256 `748ad9f869d79b4379dc98084b900156abcdcee9e8c758e8c4b1f086537cd757`, `shell=false`.

## 12. Nonthrowing subprocess design

The child was captured without `check=True`; launch exceptions, timeout, return code, stdout, and stderr were handled separately.

## 13. Durable pre-parse checkpoint

The external checkpoint was written, fsynced, atomically replaced, reread, and verified before output parsing.

## 14. Exact return code

Process launched: `true`; return code: `1`; timeout: `false`.

## 15. Launch-exception class

`null`.

## 16. Stdout and stderr bindings

stdout: `0` bytes / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

stderr: `116` bytes / `a21c749a55d94c76c89a802807f37dab868b1bacbbfb792450103574094b5631`.

Raw output was not persisted.

## 17. Filesystem snapshots

The pre-call root was empty. The post-call root contained exactly one new regular MP4 and no sidecar, archive, executable, symlink, reparse point, overwrite, or path escape.

## 18. Response parse and sanitization

Both streams decoded as UTF-8, but no complete, line, or embedded JSON document was found. No raw Provider object was retained.

## 19. Signed URL non-persistence

No signed URL was persisted, displayed, or opened.

## 20. Filesystem-delta result

`PASS`; one added file, zero changed files, and zero removed files.

## 21. Candidate binding

`5ff0ba35-5a2c-445a-8343-c95f31caaf4a_video_1.mp4`: `1669872` bytes, SHA-256 `f045a4cf65d962f6e19fbf171a2535633a038ed59c33a32a8e7b096fbbc315c3`.

## 22. Technical validation

ffprobe returned `0`; full decode returned `0`. The MP4 is H.264/yuv420p, 1280x720, 5.016667 seconds, 121 frames, rotation 0, with one video and one audio stream. A nonfatal decode diagnostic was observed but the bounded technical contract passed.

## 23. Canonical media binding

None. Failure-route rules prohibit moving media into the repository.

## 24. Failure classification and recovery recommendation

Primary: `DREAMINA_CLI_NONZERO_EXIT`. Optional factor: `DOWNLOAD_RESPONSE_PARSE_FAILURE`. The exact reason for exit code 1 after media creation remains unresolved.

Recommended gate: `HUMAN_DECISION_REQUIRED_BEFORE_ANY_FURTHER_PROVIDER_CALL`. Automatic retry is not authorized.

## 25. Exact repository write set

Exactly seven new diagnostic artifacts; zero repository media and zero technical-record artifacts.

## 26. Evidence coverage

The failure manifest binds six non-self artifacts: authorization, process checkpoint, PUSH receipt, failure analysis, execution record, and this report.

## 27. Temporary-root cleanup

Repository evidence was validated before cleanup. Download root, checkpoint root, and self-test root cleaned: `true / true / true`; temporary regular files remaining: `0`.

## 28. No IMPACT call

The IMPACT task was not called.

## 29. No retry or second PUSH

No retry, resubmit, query-only call, second PUSH, or alternate executable was used.

## 30. Source and protected state

No Source, prior media, package, Prompt, manifest, or protected state was modified.

## 31. Visual and capability boundary

Complete MP4 visual review was not performed. Visual success, reference leakage, motion-only behavior, and Route A capability remain unverified.

## 32. Next phase

`CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_DOWNLOAD_FAILURE_RECOVERY_HUMAN_DECISION`

`original_R02_blocked=true`

`R02_authorized=false`

`production_approved=false`

`fixed_task_completion=false`

`final_master=false`

`locked=false`
