# Phase D.1 Template Placement and Prompt Layer Audit

## 1) Template placement inventory

### App package scope
- app/ai_video_pipeline/shots/SHOT_REGISTRY_TEMPLATE.json : missing (not present in app package)
- app/ai_video_pipeline/prompts/PROMPT_RECORD_TEMPLATE.json : missing (not present in app package)

### Production scope (productions/<production_id>/...)
- productions/chi_yan_tian_qiong/shots/SHOT_REGISTRY_TEMPLATE.json : present
- productions/chi_yan_tian_qiong/shots/shot_registry.template.json : present
- productions/chi_yan_tian_qiong/prompts/PROMPT_RECORD_TEMPLATE.json : present
- productions/chi_yan_tian_qiong/prompts/prompt_record.template.json : present

## 2) App-level template usage review

- App-level template files are not present in the workspace.
- No app code path references those app-level template names.
- Because app-level templates are absent, they are not active duplicates and not imported by runtime code.

## 3) Production-level canonicality

- The production template files under `productions/chi_yan_tian_qiong/...` are present and are the canonical user-facing templates for this production.
- No app-level templates are being used as runtime defaults for D.1 scope.

## 4) Prompt layer boundary audit

- PromptFactory does not call any provider.
- PromptFactory does not call Dreamina.
- PromptFactory does not read old project paths.
- PromptFactory only assembles prompt text from structured data.
- Reference role order is validated by `ReferenceRole` and `validate_reference_roles`.
- `contains_vague_action_language` is test-covered and deterministic.

## 5) Safety scan for old path tokens

Forbidden old-path tokens checked:
- G:\\AICODING\\AI\u89c6\u9891\u5de5\u4f5c\u6d41
- G:/AICODING/AI\u89c6\u9891\u5de5\u4f5c\u6d41
- G:\\AICODING\\dreamina_upload_staging
- G:/AICODING/dreamina_upload_staging
- DreaminaBatcher_v2_clean
- V8_validation
- APITEST
- CLI_md

Result:
- No match of the above tokens was found in production template files, app code, or runtime tests.
- Existing historical scan/report entries continue to document policy and scan definitions.

## 6) Report quality checks

- This report does not contain malformed encoding placeholders.
- This report does not contain mixed false-token artifacts.
- Report headings and table headings remain ASCII.

## 7) Policy recommendation

Production-specific templates live under productions/<production_id>/...
Reusable package default templates, if needed, must live under app/ai_video_pipeline/templates/
Code modules such as shots/ and prompts/ should not silently contain production templates unless clearly documented.

## 8) Final status

- PHASE D.1 template placement: accepted for hardening review.
- PHASE D live-run remains disabled.
- Final verdict: `PHASE_D_ACCEPTED`
