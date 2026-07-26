# CAL002 Route A V0.2 C01 AST Query Recovery Result

## 1. Actual decision

Decision: `CAL002_ROUTE_A_V0_2_MATCHED_PAIR_C01_AST_QUERY_RECOVERY_TWO_TASKS_SUCCESS_DOWNLOAD_READY_FOR_HUMAN_AUTHORIZATION`.

## 2. Starting checkpoint

Branch `main`, HEAD/origin `6eddeb7130d9560fabe3197af0cedc383d7da26a`, parent `1efbf521635b61df26bab834ce987be47f0ce6b2`; no tracked, staged, or Source drift existed before activation.

## 3. Fresh approval and lifecycle

The exact 2869-byte approval, SHA-256 `e11bc420f1bfea80a67828efc4b4a309ee49054a5f3f64a9f72fe7ef4d445991`, remained inactive through preflight and self-test. It activated immediately before PUSH at `2026-07-26T12:24:16.206197Z` and is consumed and nonreusable.

## 4. Superseded prior recovery authorization

The prior 3554-byte recovery approval, SHA-256 `3b1c9a3300292aaf3c3c14be36ebc6ac388244f12eb34c65c71660651c7b5ff1`, was unactivated and unconsumed. It is superseded only for this route and remains nonreusable.

## 5. Prior blocked-query and false-positive evidence

The committed blocked report, evidence manifest, Help record, two not-called receipts, and execution record were rebound byte-for-byte.

## 6. No prior Provider task query

Prior PUSH query calls = 0; IMPACT query calls = 0; task state observed = false.

## 7. Failed 23/24 self-test facts

The prior 14418-byte parser had SHA-256 `7d3cb63afefc812fd159f980e23c4b70321c3224b096b762def2d526bd5b48a7`; 23 of 24 checks and all eight expected-failure fixtures passed; regex module imported = false.

## 8. Self-referential text-scanner defect

The only prior failure was its source-text detector matching its own import-example string, not an actual import.

## 9. AST-only correction design

Both temporary files were parsed with Python `ast`; only `ast.Import`, `ast.ImportFrom`, and dynamic-import `ast.Call` nodes were inspected. String constants and comment-like text were ignored.

## 10. Corrected self-test result

Exactly one offline invocation ran 28 fixtures: 20 expected-pass and 8 expected-failure. Passes = 28; failures = 0; overall = PASS.

## 11. No-regex and no-text-substring proof

Parser regex import = false; harness regex import = false; dynamic regex import = false; regex used = false; source-text substring and line inspection = false.

## 12. Prior Help evidence reuse

The committed successful Help record was reused. Raw Help output was neither reconstructed nor persisted.

## 13. Fresh metadata calls

Fresh Help = 0; version = 0; user_credit = 0.

## 14. Query count and order

Exactly two Dreamina calls ran: PUSH once then IMPACT once. Each used a four-element list argv with one `--submit_id`, zero `--download_dir`, and `shell=false`.

## 15. PUSH sanitized query result

Matching submit ID `5ff0ba35-5a2c-445a-8343-c95f31caaf4a`; Provider status `success`; queue `Finish`; result/video/image counts `1/1/0`; signed URL count 1; URL value not persisted or opened.

## 16. IMPACT sanitized query result

Matching submit ID `4c8b6184-7c0a-4b41-95f5-e215e35f195b`; Provider status `success`; queue `Finish`; result/video/image counts `1/1/0`; signed URL count 1; URL value not persisted or opened.

## 17. Provider and result counts

Both responses parsed as complete JSON without ambiguity. Successful tasks = 2; represented videos = 2; represented images = 0.

## 18. Terminal and download-ready values

Both tasks are terminal; Provider generation success = true; download_ready = true. Visual success remains unknown.

## 19. Decision-routing rationale

Both bound tasks satisfy the explicit success, terminal, video-count, and download-ready criteria. The route advances only to a separate human download-authorization decision.

## 20. No-download and no-URL-opening proof

Download calls = 0; URL opens = 0; video bytes obtained = false; signed URL values persisted = false.

## 21. No-loop and no-new-execution proof

Query loop, implicit requery, retry, resubmit, new submit, batch, and R02 execution are all false.

## 22. Protected-state boundary

Media and Sources are unchanged. All prior query, live, preparation, reference, review, lock, and report inputs remain unchanged.

## 23. Sensitive-data boundary

Raw stdout/stderr and raw Provider objects were not persisted. Only hashes, byte lengths, statuses, counts, submit IDs, and sanitization metadata were retained. Scan = PASS.

## 24. Exact write set

Exactly seven new QRYREC JSON/Markdown files were created. No existing file was modified.

## 25. Governance state

Download/retry/resubmit authority = false; Route A capability proven = false; production re-entry/approval = false; fixed-task completion = false; final_master = false; locked = false.

## 26. Next phase

`CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_DOWNLOAD_AUTHORIZATION_HUMAN_DECISION`. Commit hash and push result are externalized to the terminal receipt.
