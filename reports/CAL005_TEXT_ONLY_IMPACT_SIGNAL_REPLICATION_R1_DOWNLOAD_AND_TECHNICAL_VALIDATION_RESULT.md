# CAL005 R1 Media Download and Technical Validation Result

- Decision: `CAL005_R1_PARTIAL_DOWNLOAD_FAILURE_HUMAN_DECISION`
- Starting checkpoint: `45eb075e7f41c2f633f6bcc34a4dcf5ea3c256b7`
- Authorization activation UTC: `2026-07-29T12:18:47.789006Z`
- Download completion UTC: `2026-07-29T12:21:44.553666Z`
- Downloads attempted: `6`
- Successful downloads: `2`
- Technically valid files: `2`
- Query without download directory: `0`
- Submit/retry/resubmit/user-credit operations: `0/0/0/0`
- Semantic review, visual scoring, and scientific derivation: `false`

## Per-task technical results

| Pos | Task | Condition | Rep | Download | Bytes | Duration | Dimensions | Codecs | Decode | Technical |
| ---: | --- | --- | ---: | --- | ---: | ---: | --- | --- | --- | --- |
| 1 | N0R-01 | N0R | 1 | FAIL | 0 | n/a | 0x0 | n/a | NOT_RUN | FAIL |
| 2 | I0R-01 | I0R | 1 | FAIL | 0 | n/a | 0x0 | n/a | NOT_RUN | FAIL |
| 3 | I0R-02 | I0R | 2 | FAIL | 0 | n/a | 0x0 | n/a | NOT_RUN | FAIL |
| 4 | N0R-02 | N0R | 2 | FAIL | 0 | n/a | 0x0 | n/a | NOT_RUN | FAIL |
| 5 | N0R-03 | N0R | 3 | PASS | 4737910 | 5.061950s | 1280x720 | h264/aac | PASS | PASS |
| 6 | I0R-03 | I0R | 3 | PASS | 3429867 | 5.061950s | 1280x720 | h264/aac | PASS | PASS |

## Boundaries

- Media remains outside the Git repository.
- No media was staged or committed.
- No signed URL or raw Provider response was persisted.
- No video was watched and no review frame, thumbnail, or contact sheet was created.
- `production_approved=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

Next phase: `CAL005_R1_PARTIAL_DOWNLOAD_ROUTE_RESET_HUMAN_DECISION`
