# CAL-001 Authorization Serialization Compiler Independent No-Live Audit Result

## 1. Audit Decision

- phase_id: `CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_INDEPENDENT_NO_LIVE_AUDIT`
- decision: `safe_block`
- audit_result: `blocking implementation defects reproduced independently`
- audited_parent: `a838723b8824a1003b6abab220257d0e20fa31ad`
- audited_current: `c96c76278abcdb85ed8149b748cc5a3fe9692f2f`
- implementation_code_modified: `false`
- tests_modified: `false`
- Dreamina_called: `false`
- provider_called: `false`
- F07_called: `false`
- F07_authorized: `false`

The implementation receipt was not used as proof. The audit read the committed implementation, the parent-to-current diff, the applicable Source mirror, the historical records, and the blocked R1 report. Independent in-memory probes and an isolated parent worktree supplied the audit evidence.

## 2. Repository And Source Preflight

- repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- branch: `main`
- starting local HEAD: `c96c76278abcdb85ed8149b748cc5a3fe9692f2f`
- starting origin/main: `c96c76278abcdb85ed8149b748cc5a3fe9692f2f`
- staged files: none
- unrelated tracked changes outside the known Source mirror: none

The exact known human-managed Source-mirror changes were present:

```text
 D sources/AI视频制作_Source索引与使用优先级_V1.11.md
?? sources/AI视频制作_Source索引与使用优先级_V1.12.md
?? sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md
```

- unexpected Source changes: `false`
- Source paths touched by this audit: `false`
- Source paths staged by this audit: `false`
- human Source-mirror reconciliation required before F07: `true`

## 3. Audited Commit Scope

The parent-to-current diff contains exactly the six declared files:

- `app/ai_video_pipeline/governance/__init__.py`
- `app/ai_video_pipeline/governance/authorization_serialization.py`
- `tools/authorization_compiler.py`
- `tests/test_authorization_serialization.py`
- `tests/test_authorization_compiler_cli.py`
- `reports/PHASE_CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_NO_LIVE_IMPLEMENTATION_RESULT.md`

No implementation report assertion was accepted without independent code or runtime evidence.

## 4. Blocking Finding 1: Contradictory Records Are Accepted

Severity: `blocking`

The verifier silently chooses the first recognized representation instead of rejecting contradictory representations. `_record_containers()` prioritizes nested containers, and `_first_value()` returns immediately on the first recognized name. Byte length, SHA-256, Base64, canonical text, and record facts all use this selection mechanism.

Relevant implementation locations:

- `authorization_serialization.py:288` byte-length selection
- `authorization_serialization.py:298` SHA-256 selection
- `authorization_serialization.py:315` Base64 alias selection
- `authorization_serialization.py:361` canonical-text alias selection
- `authorization_serialization.py:535` container ordering
- `authorization_serialization.py:547` first-value selection

Independent probes supplied correct canonical bytes and a favorable first value plus a contradictory second value. Every contradictory record returned:

```text
authorization_verified=true
eligible_for_authority_activation=true
validation_errors=[]
```

| Conflict | Observed result |
| --- | --- |
| `base64` correct plus conflicting `authorization_base64` | accepted |
| `locally_derived_base64` correct plus conflicting `locally_generated_base64` | accepted |
| correct nested byte length plus conflicting top-level byte length | accepted |
| correct nested SHA-256 plus conflicting top-level SHA-256 | accepted |
| correct `canonical_authorization_text` plus conflicting `exact_authorization_text` | accepted |

This violates the Source rule that derived evidence conflicts must safe-block and that the verifier must never select one favorable copy to trust.

Required repair behavior:

1. Enumerate every recognized representation from every recognized container.
2. Validate type and format for every occurrence.
3. Require all duplicate representations of the same fact to agree.
4. Reject any conflicting canonical-text field, derived evidence alias, nested fact, or top-level fact with an explicit deterministic conflict error.
5. Add adversarial regression tests for every conflict above and for conflicts in nested verification facts.

No repair was made during this audit.

## 5. Blocking Finding 2: Compile-Only Can Report Activation Readiness

Severity: `blocking`

A valid byte-profile compilation sets both:

```text
authorization_verified=true
eligible_for_authority_activation=true
```

at `authorization_serialization.py:263-265`, before any expected authorization record or checkpoint has been verified.

`evaluate_activation_eligibility()` accepts either `AuthorizationSerializationResult` or `AuthorizationVerificationResult`. Its checkpoint argument is optional. At `authorization_serialization.py:498-516`, a compile-only result with no checkpoint produces:

```json
{
  "checkpoint_binding_required": false,
  "checkpoint_binding_verified": null,
  "decision": "ready",
  "eligible_for_authority_activation": true,
  "execution_authority_active": false,
  "provider_command_allowed": false
}
```

The current implementation does not activate authority itself, but the field names and `decision=ready` allow a future caller to mistake byte-profile validity for complete human authorization evidence and checkpoint eligibility. The audit requirement that compile-only cannot be misinterpreted as full authorization is therefore not met.

Required repair behavior:

1. Keep serialization profile validity separate from authorization evidence verification.
2. A compile result must not call itself `authorization_verified` or activation-eligible.
3. Activation eligibility must require a verified authorization record and the explicitly required checkpoint/scope gates.
4. `evaluate_activation_eligibility()` should reject compile-only input or return a non-activation state such as `serialization_ready_for_evidence_verification`.
5. Add tests proving compile-only cannot return `ready` or activation eligibility.

No repair was made during this audit.

## 6. Passing Core Semantic Checks

Independent probes verified:

- canonical calculations use the original bytes;
- file input uses `Path.read_bytes()`;
- stdin uses `sys.stdin.buffer.read()`;
- invalid UTF-8 fails deterministically;
- canonical input is not stripped or Unicode-normalized;
- BOM, CR, LF, trailing space, and Markdown fences are rejected;
- SHA-256 and Base64 derive from original bytes;
- locally generated Base64 round-trips byte-for-byte;
- malformed Base64 is rejected;
- correct hash with incorrect Base64 is rejected;
- incorrect hash with correct Base64 is rejected;
- incorrect length with correct hash is rejected;
- a selected canonical-text value differing from supplied bytes is rejected;
- same-length and underscore-to-letter mutations are rejected;
- checkpoint local, origin, malformed, and changed-value cases safe-block;
- failure never activates authority, allows a provider command, or consumes a counter;
- all result types retain provider invocation count `0` and operation count `0`;
- stable JSON is byte-identical across repeated calls;
- pure results contain no timestamp, environment state, or machine path;
- implementation imports contain no Dreamina or provider module;
- the pure verifier performs no implicit Git lookup.

Lowercasing occurs only for hexadecimal digest/checkpoint comparison, not canonical authorization input. `os.replace()` is used only for explicit output-file publication.

## 7. Historical Fixture Independence

A separate standard-library probe read canonical text directly from each committed record, encoded it as UTF-8, calculated SHA-256 and Base64, decoded the committed Base64 exactly once, and compared the bytes. It did not call the new compiler/verifier.

| Fixture | Bytes | SHA-256 | Record evidence | Round trip |
| --- | ---: | --- | --- | --- |
| F06 recovery query R2 | 432 | `0f4306d42084ab96044eea5a89d338e0cf1e41c31e39d8df85b25a15626fe883` | match | match |
| F06 recovery download | 607 | `e56a37cc5e7f17aaa691ec4e5862fa9253e1a0273221523f9b2a2c172601ff4a` | match | match |
| F06 review-artifact authorization | 583 | `472da91ce12a778f6505844fb52e80a86dd2c1e11cafd469c344cfe08d4df1a1` | match | match |
| F06 visual-review authorization | 1036 | `e50c231685d549167eeb71ce229e3f61e17ad392da1fc1468aa41d9ccdcb2632` | match | match |

The independent R1 reconstruction produced:

- canonical bytes: `416`
- canonical SHA-256: `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3`
- supplied Base64 decoded bytes: `416`
- decoded SHA-256: `f5eb16120e865791f0444a8f0e45cf85aedf141d8f1334c7795196bfb5704b11`
- decoded bytes equal canonical bytes: `false`
- rejection required and observed in the verifier: `true`

## 8. CLI Audit

Independent subprocess probes used only the local Python CLI and temporary system-directory files. No probe called Git, Dreamina, or a provider.

| CLI behavior | Result |
| --- | --- |
| compile from raw file | pass, exit 0 |
| compile from binary stdin | pass, exit 0 |
| file/stdin serialization facts equal | pass |
| repeated JSON bytes stable | pass |
| piped trailing LF | rejected, exit 1 |
| binary invalid UTF-8 | rejected, exit 1 |
| verify expected values | pass, exit 0 |
| verify committed-style record | pass, exit 0 |
| verify explicit checkpoint values | pass, exit 0 |
| mutually exclusive input modes | enforced, exit 2 |
| initial optional output publication | pass |
| default existing-output protection | pass, exit 2, original unchanged |
| explicit overwrite | pass, exit 0 |
| malformed record error JSON | parseable stderr, exit 2 |
| unexpected canonical-text leakage | absent |
| temporary `.tmp` residue | none |

Static inspection confirms same-directory `mkstemp`, flush plus `fsync`, no-overwrite publication using `os.link`, and explicit-overwrite publication using `os.replace`.

## 9. Test And Parent-Baseline Audit

Current checkpoint commands and results:

```text
python -m pytest -o addopts= -q tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
32 passed, 0 failed

python -m pytest -o addopts= -q --tb=no
500 passed, 10 failed
```

An isolated detached worktree at parent `a838723b8824a1003b6abab220257d0e20fa31ad` was created under a short Windows path. The complete parent suite produced `413 passed, 65 failed`; 55 additional failures were caused by the isolated checkout not containing local untracked/ignored workspace artifacts and were not used for commit-regression classification.

The exact ten node IDs failing in the current workspace were then run at the parent checkpoint. All ten failed there:

| Current failure | Parent classification |
| --- | --- |
| `test_phase_c.py::test_16_templates_are_ascii_safe` | pre_existing_at_parent |
| `test_phase_c.py::test_17_templates_do_not_contain_false_true_mixed_token` | pre_existing_at_parent |
| `test_phase_f6_3.py::test_16_f6_3_review_record_appends_lock_with_paths` | pre_existing_at_parent |
| `test_phase_f6_4.py::test_03_f6_4_review_record_exists` | pre_existing_at_parent |
| `test_phase_g2_3.py::test_03_review_records_and_template_show_approve` | pre_existing_at_parent |
| `test_phase_g4_3.py::test_05_review_record_and_template_show_approval` | pre_existing_at_parent |
| `test_phase_g4_4.py::test_03_all_locked_assets_have_review_records` | pre_existing_at_parent |
| `test_phase_h3.py::test_02_review_record_was_added_without_locking_failed_keyframe` | pre_existing_at_parent |
| `test_phase_j11.py::test_03_review_record_documents_user_lock_decision` | pre_existing_at_parent |
| `test_phase_j11.py::test_04_prompt_and_status_files_unblock_shot_02_kf_002` | pre_existing_at_parent |

Classification totals:

- failures introduced by current commit: `0`
- current failures pre-existing at parent: `10`
- current failures unknown: `0`

Both temporary worktrees were removed. `git worktree list --porcelain` shows only the main repository worktree.

## 10. Protected-State Confirmation

- CAL-001 execution-state SHA-256: `e42e92700d63e9f78a9ac9fb564f3d7410d94f4160dd6e047ab02eeaa02c205b`
- `execution_authority_active=false`
- `remaining_noncanary_tasks_authorized=false`
- stop condition: `F06_technically_completed_authority_closed_no_F07_authorization`
- `F07_authorized=false`
- CAL-001 state changed: `false`
- datasets modified: `false`
- manifest modified: `false`
- media modified: `false`
- authorization history modified: `false`
- Prompt/package files modified: `false`
- `final_master=false`
- `locked=false`

## 11. Audit Verdict And Required Repair Phase

The implementation has useful deterministic byte handling and correct historical compatibility, but it does not meet the READY rules because contradictory records are accepted and compile-only can report activation readiness.

Final verdict:

`CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_INDEPENDENT_AUDIT_SAFE_BLOCK_REPAIR_REQUIRED`

Recommended next phase:

`CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_CONTRADICTION_AND_ACTIVATION_BOUNDARY_REPAIR_NO_LIVE`

That phase should modify only the compiler/verifier and focused tests, then require a new independent no-live audit. F07 preflight or authorization remains blocked. Human reconciliation of the local `sources/` mirror is still required before any later F07 decision.
