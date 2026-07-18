from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass, is_dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Protocol, Sequence


class CommandResultLike(Protocol):
    argv: list[str]
    returncode: int
    stdout: str
    stderr: str


Runner = Callable[[Sequence[str]], CommandResultLike]
AtomicWriter = Callable[[Path, Mapping[str, Any]], Path]

_URL_RE = re.compile(r"https?://[^\s\"'<>]+", flags=re.IGNORECASE)
_AUTH_RE = re.compile(
    r"(?im)(authorization\s*[:=]\s*)(?:bearer\s+)?[^\s,;]+"
)
_COOKIE_RE = re.compile(r"(?im)(cookie\s*[:=]\s*)[^\r\n]+")
_SECRET_FIELD_RE = re.compile(
    r"(?i)([\"']?(?:access[_-]?token|refresh[_-]?token|api[_-]?key|token|secret|session|cookie)[\"']?\s*[:=]\s*[\"']?)([^\"',\s}\]]+)"
)
_PROMPT_FIELD_RE = re.compile(
    r"(?i)([\"']?(?:prompt|negative_prompt)[\"']?\s*[:=]\s*[\"'])(.*?)([\"'](?=\s*[,}\r\n]|$))"
)
_SENSITIVE_ARG_FLAGS = {
    "--access_token",
    "--api_key",
    "--authorization",
    "--cookie",
    "--negative_prompt",
    "--prompt",
    "--refresh_token",
    "--secret",
    "--session",
    "--token",
}
_PROMPT_ARG_FLAGS = {"--negative_prompt", "--prompt"}


class DuplicateSubmitForbidden(RuntimeError):
    def __init__(self, experiment_id: str, submit_id: str) -> None:
        super().__init__(
            f"duplicate submit forbidden for {experiment_id}: existing submit_id={submit_id}"
        )
        self.experiment_id = experiment_id
        self.submit_id = submit_id
        self.stage = "pre_subprocess_guard"


@dataclass(frozen=True)
class SanitizedCommandResult:
    argv: list[str]
    returncode: int
    stdout: str
    stderr: str


@dataclass
class DurableCommandExecution:
    operation_id: str
    experiment_id: str
    command_type: str
    operation_kind: str
    result: CommandResultLike
    envelope_path: Path
    evidence_dir: Path
    parsed_evidence: dict[str, Any] | None = None
    parsed_evidence_path: Path | None = None
    known_submit_id: str = ""
    secret_values: tuple[str, ...] = ()
    atomic_writer: AtomicWriter | None = None

    def persist_postprocessing_failure(
        self,
        error: BaseException,
        *,
        stage: str = "postprocessing",
    ) -> Path:
        parsed = self.parsed_evidence or {}
        submit_id = str(parsed.get("submit_id") or self.known_submit_id or "")
        if submit_id:
            remote_state = "created_or_possible_created"
        elif self.operation_kind == "submit" and self.result.returncode == 0:
            remote_state = "created_or_possible_created"
        else:
            remote_state = "not_proven_created"
        payload = {
            "schema_version": "1.0",
            "operation_id": self.operation_id,
            "experiment_id": self.experiment_id,
            "command_type": self.command_type,
            "operation_kind": self.operation_kind,
            "remote_task_creation_state": remote_state,
            "local_postprocessing_status": "failed",
            "failure_stage": stage,
            "exception_class": type(error).__name__,
            "exception_message": sanitize_text(
                str(error), secret_values=self.secret_values
            ),
            "subprocess_envelope_path": str(self.envelope_path),
            "parsed_task_evidence_path": (
                str(self.parsed_evidence_path) if self.parsed_evidence_path else None
            ),
            "submit_id": submit_id or None,
            "logid": parsed.get("logid"),
            "gen_status": parsed.get("gen_status"),
            "queue_status": parsed.get("queue_status"),
            "credit_count": parsed.get("credit_count"),
            "submit_attempt_count": 1 if self.operation_kind == "submit" else 0,
            "created_task_count": 1 if submit_id else 0,
            "query_count": 1 if self.operation_kind == "query" else 0,
            "download_count": 1 if self.operation_kind == "download" else 0,
            "retry_count": 0,
            "resubmit_count": 0,
            "failure_recorded_at": utc_now(),
        }
        target = self.evidence_dir / f"{safe_name(self.operation_id)}.postprocessing_failure.json"
        writer = self.atomic_writer or atomic_write_json
        return writer(target, payload)

    @contextmanager
    def postprocessing_guard(self, *, stage: str = "postprocessing") -> Iterator[None]:
        try:
            yield
        except BaseException as error:
            self.persist_postprocessing_failure(error, stage=stage)
            raise


@dataclass(frozen=True)
class CreditContinuityResult:
    passed: bool
    classification: str
    current_balance_numeric: int | None
    threshold_passed: bool
    drift_amount: int | None
    drift_direction: str
    scope_or_budget_enlarged: bool
    stop_condition: str | None


@dataclass(frozen=True)
class PostSubmitCreditResult:
    passed: bool
    classification: str
    immediate_pre_submit_balance: int | None
    immediate_post_submit_balance: int | None
    observed_credit_delta: int | None
    provider_credit_count_numeric: int | None
    stop_condition: str | None


def _credit_integer(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value) if value.is_integer() else None
    if isinstance(value, str) and re.fullmatch(r"[+-]?\d+", value.strip()):
        return int(value.strip())
    return None


def validate_pre_submit_credit_continuity(
    *,
    prior_observed_balance: Any,
    current_observed_balance: Any,
    required_dynamic_threshold: Any,
    intervening_authorized_CAL001_submit_count: Any,
) -> CreditContinuityResult:
    current = _credit_integer(current_observed_balance)
    threshold = _credit_integer(required_dynamic_threshold)
    prior = _credit_integer(prior_observed_balance)
    submit_count = _credit_integer(intervening_authorized_CAL001_submit_count)

    if current is None:
        return CreditContinuityResult(
            False,
            "current_balance_nonnumeric",
            None,
            False,
            None,
            "unknown",
            False,
            "Current pre-submit balance is absent or nonnumeric.",
        )
    if threshold is None:
        return CreditContinuityResult(
            False,
            "dynamic_threshold_nonnumeric",
            current,
            False,
            None,
            "unknown",
            False,
            "Required dynamic credit threshold is absent or nonnumeric.",
        )
    if prior is None:
        return CreditContinuityResult(
            False,
            "prior_balance_nonnumeric",
            current,
            current >= threshold,
            None,
            "unknown",
            False,
            "Prior credit observation is absent or nonnumeric.",
        )
    if submit_count is None or submit_count < 0:
        return CreditContinuityResult(
            False,
            "intervening_submit_count_invalid",
            current,
            current >= threshold,
            current - prior,
            "unknown",
            False,
            "Intervening authorized CAL-001 submit count is invalid.",
        )

    drift = current - prior
    direction = "positive" if drift > 0 else "negative" if drift < 0 else "none"
    threshold_passed = current >= threshold
    if not threshold_passed:
        return CreditContinuityResult(
            False,
            "below_dynamic_credit_threshold",
            current,
            False,
            drift,
            direction,
            False,
            f"Current balance {current} is below required threshold {threshold}.",
        )

    if submit_count == 0:
        if drift > 0:
            classification = "positive_nonspend_credit_drift"
            stop_condition = None
            passed = True
        elif drift == 0:
            classification = "no_pre_submit_credit_drift"
            stop_condition = None
            passed = True
        else:
            classification = "unexplained_negative_credit_drift"
            stop_condition = (
                "Current balance decreased without an intervening authorized "
                "CAL-001 submit."
            )
            passed = False
    else:
        expected_drift = -70 * submit_count
        if drift == expected_drift:
            classification = "authorized_submit_credit_drift"
            stop_condition = None
            passed = True
        else:
            classification = "authorized_submit_credit_drift_unreconciled"
            stop_condition = (
                f"Observed drift {drift} does not equal the expected "
                f"{-70 * submit_count} credits for {submit_count} authorized submit(s)."
            )
            passed = False

    return CreditContinuityResult(
        passed,
        classification,
        current,
        True,
        drift,
        direction,
        False,
        stop_condition,
    )


def validate_post_submit_credit_reconciliation(
    *,
    immediate_pre_submit_balance: Any,
    immediate_post_submit_balance: Any,
    provider_credit_count: Any,
) -> PostSubmitCreditResult:
    pre_balance = _credit_integer(immediate_pre_submit_balance)
    post_balance = _credit_integer(immediate_post_submit_balance)
    provider_count = _credit_integer(provider_credit_count)
    delta = (
        pre_balance - post_balance
        if pre_balance is not None and post_balance is not None
        else None
    )

    if pre_balance is None or post_balance is None:
        return PostSubmitCreditResult(
            False,
            "post_submit_balance_nonnumeric",
            pre_balance,
            post_balance,
            delta,
            provider_count,
            "Immediate pre/post-submit balances are absent or nonnumeric.",
        )
    if provider_credit_count is None:
        return PostSubmitCreditResult(
            False,
            "provider_credit_count_absent",
            pre_balance,
            post_balance,
            delta,
            None,
            "Provider credit_count is absent.",
        )
    if provider_count is None:
        return PostSubmitCreditResult(
            False,
            "provider_credit_count_nonnumeric",
            pre_balance,
            post_balance,
            delta,
            None,
            "Provider credit_count is nonnumeric or ambiguous.",
        )
    if provider_count != 70:
        return PostSubmitCreditResult(
            False,
            "provider_credit_count_not_70",
            pre_balance,
            post_balance,
            delta,
            provider_count,
            f"Provider credit_count is {provider_count}, not 70.",
        )
    if delta != 70:
        return PostSubmitCreditResult(
            False,
            "post_submit_credit_delta_not_70",
            pre_balance,
            post_balance,
            delta,
            provider_count,
            f"Observed immediate post-submit credit delta is {delta}, not 70.",
        )
    return PostSubmitCreditResult(
        True,
        "exact_70_credit_reconciliation",
        pre_balance,
        post_balance,
        delta,
        provider_count,
        None,
    )


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", str(value)).strip("._")
    return cleaned or "operation"


def sanitize_text(value: str, *, secret_values: Sequence[str] = ()) -> str:
    sanitized = str(value or "")
    for secret in sorted(
        {str(item) for item in secret_values if str(item)}, key=len, reverse=True
    ):
        sanitized = sanitized.replace(secret, "<redacted_secret>")
    sanitized = _PROMPT_FIELD_RE.sub(r"\1<redacted_prompt>\3", sanitized)
    sanitized = _AUTH_RE.sub(r"\1<redacted>", sanitized)
    sanitized = _COOKIE_RE.sub(r"\1<redacted>", sanitized)
    sanitized = _SECRET_FIELD_RE.sub(r"\1<redacted>", sanitized)
    sanitized = _URL_RE.sub("<redacted_url>", sanitized)
    return sanitized


def sanitize_command_structure(
    argv: Sequence[str], *, secret_values: Sequence[str] = ()
) -> list[str]:
    sanitized: list[str] = []
    redact_next: str | None = None
    for raw in argv:
        item = str(raw)
        if redact_next is not None:
            if redact_next in _PROMPT_ARG_FLAGS:
                sanitized.append(
                    f"<redacted_prompt sha256={sha256_text(item)} chars={len(item)}>"
                )
            else:
                sanitized.append("<redacted>")
            redact_next = None
            continue
        sanitized.append(sanitize_text(item, secret_values=secret_values))
        if item.lower() in _SENSITIVE_ARG_FLAGS:
            redact_next = item.lower()
    return sanitized


def atomic_write_json(
    path: Path,
    payload: Mapping[str, Any],
    *,
    replace_func: Callable[[str, str], Any] = os.replace,
) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.", suffix=".tmp", dir=str(target.parent)
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(dict(payload), handle, ensure_ascii=True, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        replace_func(str(temporary), str(target))
        _fsync_parent(target.parent)
    finally:
        if temporary.exists():
            temporary.unlink()
    return target


def _fsync_parent(parent: Path) -> None:
    directory_flag = getattr(os, "O_DIRECTORY", None)
    if directory_flag is None:
        return
    descriptor: int | None = None
    try:
        descriptor = os.open(str(parent), os.O_RDONLY | directory_flag)
        os.fsync(descriptor)
    except OSError:
        return
    finally:
        if descriptor is not None:
            os.close(descriptor)


def infer_operation_kind(argv: Sequence[str]) -> str:
    values = [str(item) for item in argv]
    if len(values) > 1 and values[1] == "query_result":
        return "download" if "--download_dir" in values else "query"
    return "submit"


def execute_with_durable_evidence(
    *,
    runner: Runner,
    argv: Sequence[str],
    evidence_dir: Path,
    operation_id: str,
    experiment_id: str,
    command_type: str,
    operation_kind: str | None = None,
    existing_submit_record: Path | None = None,
    known_submit_id: str = "",
    secret_values: Sequence[str] = (),
    clock: Callable[[], str] = utc_now,
    atomic_writer: AtomicWriter = atomic_write_json,
) -> DurableCommandExecution:
    kind = operation_kind or infer_operation_kind(argv)
    if kind == "submit" and existing_submit_record is not None:
        assert_no_existing_submit(existing_submit_record, experiment_id)

    evidence_root = Path(evidence_dir)
    started_at = clock()
    try:
        raw_result = runner(list(argv))
    except BaseException as error:
        failure_payload = {
            "schema_version": "1.0",
            "operation_id": operation_id,
            "experiment_id": experiment_id,
            "command_type": command_type,
            "operation_kind": kind,
            "subprocess_returned": False,
            "remote_task_creation_state": "not_proven_created",
            "local_postprocessing_status": "not_started",
            "failure_stage": "runner_failed_before_command_result",
            "exception_class": type(error).__name__,
            "exception_message": sanitize_text(str(error), secret_values=secret_values),
            "started_at": started_at,
            "failed_at": clock(),
            "command_structure_without_prompt_or_secrets": sanitize_command_structure(
                argv, secret_values=secret_values
            ),
        }
        atomic_writer(
            evidence_root / f"{safe_name(operation_id)}.invocation_failure.json",
            failure_payload,
        )
        raise

    completed_at = clock()
    sanitized_stdout = sanitize_text(
        str(raw_result.stdout or ""), secret_values=secret_values
    )
    sanitized_stderr = sanitize_text(
        str(raw_result.stderr or ""), secret_values=secret_values
    )
    sanitized_argv = sanitize_command_structure(argv, secret_values=secret_values)
    sanitized_result = _replace_command_result(
        raw_result,
        argv=sanitized_argv,
        stdout=sanitized_stdout,
        stderr=sanitized_stderr,
    )
    envelope_payload = {
        "schema_version": "1.0",
        "operation_id": operation_id,
        "experiment_id": experiment_id,
        "command_type": command_type,
        "operation_kind": kind,
        "started_at": started_at,
        "completed_at": completed_at,
        "subprocess_exit_code": int(raw_result.returncode),
        "sanitized_stdout": sanitized_stdout,
        "sanitized_stderr": sanitized_stderr,
        "stdout_sha256": sha256_text(sanitized_stdout),
        "stderr_sha256": sha256_text(sanitized_stderr),
        "hash_scope": "sanitized_utf8",
        "command_structure_without_prompt_or_secrets": sanitized_argv,
        "evidence_persisted_at": clock(),
    }
    envelope_path = atomic_writer(
        evidence_root / f"{safe_name(operation_id)}.subprocess_envelope.json",
        envelope_payload,
    )

    execution = DurableCommandExecution(
        operation_id=operation_id,
        experiment_id=experiment_id,
        command_type=command_type,
        operation_kind=kind,
        result=sanitized_result,
        envelope_path=envelope_path,
        evidence_dir=evidence_root,
        known_submit_id=known_submit_id,
        secret_values=tuple(str(item) for item in secret_values if str(item)),
        atomic_writer=atomic_writer,
    )
    if kind != "submit":
        return execution

    try:
        parsed = parse_task_creation_evidence(
            sanitized_stdout + "\n" + sanitized_stderr
        )
        parsed.update(
            {
                "schema_version": "1.0",
                "operation_id": operation_id,
                "experiment_id": experiment_id,
                "command_type": command_type,
                "subprocess_exit_code": int(raw_result.returncode),
                "remote_task_creation_state": (
                    "created"
                    if parsed.get("submit_id")
                    else "possible_created"
                    if int(raw_result.returncode) == 0
                    else "not_confirmed"
                ),
                "submit_attempt_count": 1,
                "created_task_count": 1 if parsed.get("submit_id") else 0,
                "query_count": 0,
                "download_count": 0,
                "retry_count": 0,
                "resubmit_count": 0,
                "parsed_at": clock(),
                "subprocess_envelope_path": str(envelope_path),
            }
        )
        parsed_path = atomic_writer(
            evidence_root / f"{safe_name(operation_id)}.parsed_task_creation.json",
            parsed,
        )
        execution.parsed_evidence = parsed
        execution.parsed_evidence_path = parsed_path
        return execution
    except BaseException as error:
        execution.persist_postprocessing_failure(
            error, stage="task_creation_parse_or_persistence"
        )
        raise


def _replace_command_result(
    result: CommandResultLike,
    *,
    argv: list[str],
    stdout: str,
    stderr: str,
) -> CommandResultLike:
    if is_dataclass(result):
        try:
            return replace(result, argv=argv, stdout=stdout, stderr=stderr)
        except TypeError:
            pass
    return SanitizedCommandResult(
        argv=argv,
        returncode=int(result.returncode),
        stdout=stdout,
        stderr=stderr,
    )


def parse_task_creation_evidence(text: str) -> dict[str, Any]:
    payloads = _json_candidates(text)
    submit_id = _first_value(payloads, {"submit_id"}) or _regex_value(
        text, "submit_id"
    )
    logid = _first_value(payloads, {"logid"}) or _regex_value(text, "logid")
    gen_status = _first_value(payloads, {"gen_status"}) or _regex_value(
        text, "gen_status"
    )
    queue_status = _first_value(payloads, {"queue_status"}) or _regex_value(
        text, "queue_status"
    )
    credit_value = _first_value(payloads, {"credit_count"}) or _regex_value(
        text, "credit_count"
    )
    return {
        "submit_id": str(submit_id) if submit_id not in (None, "") else None,
        "logid": str(logid) if logid not in (None, "") else None,
        "gen_status": (
            str(gen_status) if gen_status not in (None, "") else None
        ),
        "queue_status": (
            str(queue_status) if queue_status not in (None, "") else None
        ),
        "credit_count": _coerce_int(credit_value),
    }


def _json_candidates(text: str) -> list[Any]:
    candidates: list[Any] = []
    try:
        candidates.append(json.loads(text))
    except json.JSONDecodeError:
        pass
    for line in text.splitlines():
        value = line.strip()
        if not value:
            continue
        try:
            candidates.append(json.loads(value))
        except json.JSONDecodeError:
            continue
    return candidates


def _first_value(payloads: Sequence[Any], keys: set[str]) -> Any:
    for payload in payloads:
        found = _find_value(payload, keys)
        if found not in (None, ""):
            return found
    return None


def _find_value(payload: Any, keys: set[str]) -> Any:
    if isinstance(payload, dict):
        for key, value in payload.items():
            if str(key).lower() in keys and value is not None:
                return value
            nested = _find_value(value, keys)
            if nested not in (None, ""):
                return nested
    elif isinstance(payload, list):
        for item in payload:
            nested = _find_value(item, keys)
            if nested not in (None, ""):
                return nested
    return None


def _regex_value(text: str, field: str) -> str | None:
    match = re.search(
        rf"{re.escape(field)}[\"':= ]+([A-Za-z0-9._:-]+)",
        text,
        flags=re.IGNORECASE,
    )
    return match.group(1) if match else None


def _coerce_int(value: Any) -> int | None:
    if value in (None, "") or isinstance(value, bool):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def load_existing_submit_evidence(record_path: Path) -> dict[str, Any]:
    path = Path(record_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"existing submit record must be a JSON object: {path}")
    submit = payload.get("submit_evidence")
    if not isinstance(submit, dict):
        submit = payload
    credit = payload.get("credit_evidence")
    if not isinstance(credit, dict):
        credit = {}
    download = payload.get("download")
    if not isinstance(download, dict):
        download = {}

    experiment_id = str(
        payload.get("experiment_id") or submit.get("experiment_id") or ""
    )
    submit_id = str(submit.get("submit_id") or payload.get("submit_id") or "")
    logid = str(submit.get("logid") or payload.get("logid") or "")
    last_known_state = str(
        submit.get("gen_status")
        or payload.get("gen_status")
        or payload.get("terminal_state")
        or "unknown"
    )
    query_count = _coerce_int(payload.get("query_count"))
    if query_count is None:
        history = payload.get("query_history")
        query_count = len(history) if isinstance(history, list) else 0
    download_count = _coerce_int(download.get("download_count"))
    if download_count is None:
        download_count = _coerce_int(payload.get("download_count")) or 0
    recorded_cost = _coerce_int(submit.get("submit_response_credit_count"))
    if recorded_cost is None:
        recorded_cost = _coerce_int(submit.get("credit_count"))
    if recorded_cost is None:
        recorded_cost = _coerce_int(credit.get("observed_credit_delta"))

    created = bool(submit_id)
    query_eligible = (
        created
        and last_known_state.lower() in {"created", "pending", "querying", "submitted"}
        and download_count == 0
    )
    return {
        "record_path": str(path),
        "experiment_id": experiment_id,
        "existing_submit_created": created,
        "submit_id_available": bool(submit_id),
        "submit_id": submit_id or None,
        "logid_available": bool(logid),
        "logid": logid or None,
        "last_known_remote_state": last_known_state,
        "recorded_cost": recorded_cost,
        "query_count_already_used": query_count,
        "download_count_already_used": download_count,
        "duplicate_submit_forbidden": created,
        "query_recovery_eligible": query_eligible,
        "requires_separate_human_authorization": True,
        "retry_allowed": False,
        "resubmit_allowed": False,
    }


def assert_no_existing_submit(record_path: Path, experiment_id: str) -> None:
    recovery = load_existing_submit_evidence(record_path)
    recorded_experiment = str(recovery.get("experiment_id") or "")
    if recorded_experiment and recorded_experiment != experiment_id:
        raise ValueError(
            f"existing submit record experiment mismatch: {recorded_experiment} != {experiment_id}"
        )
    if recovery["duplicate_submit_forbidden"]:
        raise DuplicateSubmitForbidden(
            experiment_id, str(recovery["submit_id"] or "")
        )
