# CAL005 R1 Failed-Four Download Recovery Result

- Decision: `CAL005_R1_DOWNLOAD_RECOVERY_PARTIAL_FAILURE_HUMAN_DECISION`
- Starting checkpoint: `0a024cf19d5e28c14701dc4847ec8c4629eec988`
- Authorization activation UTC: `2026-07-29T12:58:37.072923Z`
- Recovery completion UTC: `2026-07-29T13:00:54.660235Z`
- Replacement invocations: `4`
- Replacement successes: `0`
- Replacement failures: `4`
- Dreamina invocations for positions 5 and 6: `0`
- Query without download, submit, retry, resubmit, and user-credit: `0`
- Semantic review, scoring, scientific derivation, and randomness: `0`

## Replacement results

| Pos | Task | Exit | Result | Failure class | Sanitized message | Bytes | Duration | Technical |
| ---: | --- | ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | N0R-01 | 1 | FAIL | DOWNLOAD_TRANSPORT_BODY_READ_TIMEOUT | download video 1: write file: context deadline exceeded (Client.Timeout or context cancellation while reading body) | 0 | n/a | FAIL |
| 2 | I0R-01 | 1 | FAIL | DOWNLOAD_TRANSPORT_BODY_READ_TIMEOUT | download video 1: write file: context deadline exceeded (Client.Timeout or context cancellation while reading body) | 0 | n/a | FAIL |
| 3 | I0R-02 | 1 | FAIL | DOWNLOAD_TRANSPORT_BODY_READ_TIMEOUT | download video 1: write file: context deadline exceeded (Client.Timeout or context cancellation while reading body) | 0 | n/a | FAIL |
| 4 | N0R-02 | 1 | FAIL | DOWNLOAD_TRANSPORT_BODY_READ_TIMEOUT | download video 1: write file: context deadline exceeded (Client.Timeout or context cancellation while reading body) | 0 | n/a | FAIL |

## Existing successful media revalidation

| Pos | Task | Bytes | Identity unchanged | Decode | Technical | Dreamina calls |
| ---: | --- | ---: | --- | --- | --- | ---: |
| 5 | N0R-03 | 4737910 | true | PASS | PASS | 0 |
| 6 | I0R-03 | 3429867 | true | PASS | PASS | 0 |

## Local learning and synchronization record

- Persist successful help-command evidence before launching the next independent preflight check.
- Resolve and identity-verify ffmpeg and ffprobe before a combined preflight script depends on them.
- Do not use cross-volume directory rename on Windows; use same-volume temporary paths or exclusive copy with byte and SHA-256 verification.
- Retain a structurally redacted failure message for failed CLI or Provider commands, not only byte counts.
- Keep the first four prior failures root-cause unresolved unless new sanitized evidence supports a narrower classification.

- These entries are local Source-update candidates only.
- `sources/*` was not modified.
- Exact recovery root cause established: all four replacement downloads failed while reading the response body with `context deadline exceeded (Client.Timeout or context cancellation while reading body)`.

- Local deterministic corrections used: `3/3`.

## Boundaries

- Media remains outside Git and no media is staged or committed.
- No raw stdout, stderr, Provider response, signed URL, token, cookie, account, or session value is persisted.
- No semantic review or scientific result was performed.
- `production_approved=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

Next phase: `CAL005_R1_PERSISTENT_PARTIAL_DOWNLOAD_ROUTE_RESET_HUMAN_DECISION`
