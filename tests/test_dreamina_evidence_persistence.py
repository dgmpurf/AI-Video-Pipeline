from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pytest

from app.ai_video_pipeline.execution.dreamina_evidence import (
    DuplicateSubmitForbidden,
    assert_no_existing_submit,
    atomic_write_json,
    execute_with_durable_evidence,
    load_existing_submit_evidence,
)


ROOT = Path(__file__).resolve().parents[1]
F01_RECORD = (
    ROOT
    / "experiments"
    / "CAL-001"
    / "execution_records"
    / "P3B_R2"
    / "CAL001-F01-P2-R1_technical_record.json"
)


@dataclass(frozen=True)
class FakeResult:
    argv: list[str]
    returncode: int
    stdout: str
    stderr: str


def _submit_result(argv: list[str]) -> FakeResult:
    return FakeResult(
        list(argv),
        0,
        json.dumps(
            {
                "submit_id": "SUB-001",
                "logid": "LOG-001",
                "gen_status": "querying",
                "credit_count": 70,
            }
        ),
        "",
    )


def _execute(tmp_path: Path, *, runner=_submit_result, argv: list[str] | None = None):
    return execute_with_durable_evidence(
        runner=runner,
        argv=argv or ["dreamina", "text2video", "--prompt", "private prompt"],
        evidence_dir=tmp_path / "evidence",
        operation_id="submit-001",
        experiment_id="EXP-001",
        command_type="text2video",
        operation_kind="submit",
    )


def test_01_success_persists_envelope_before_parsed_task_evidence(tmp_path: Path) -> None:
    execution = _execute(tmp_path)

    envelope = json.loads(execution.envelope_path.read_text(encoding="utf-8"))
    parsed = json.loads(execution.parsed_evidence_path.read_text(encoding="utf-8"))

    assert envelope["subprocess_exit_code"] == 0
    assert envelope["sanitized_stdout"]
    assert envelope["sanitized_stderr"] == ""
    assert len(envelope["stdout_sha256"]) == 64
    assert len(envelope["stderr_sha256"]) == 64
    assert "private prompt" not in json.dumps(envelope)
    assert parsed["submit_id"] == "SUB-001"
    assert parsed["logid"] == "LOG-001"
    assert parsed["gen_status"] == "querying"
    assert parsed["credit_count"] == 70
    assert parsed["submit_attempt_count"] == 1
    assert parsed["created_task_count"] == 1


def test_02_postprocessing_failure_preserves_created_task_evidence(tmp_path: Path) -> None:
    execution = _execute(tmp_path)

    with pytest.raises(RuntimeError, match="downstream record failed"):
        with execution.postprocessing_guard(stage="record_write"):
            raise RuntimeError("downstream record failed")

    envelope = json.loads(execution.envelope_path.read_text(encoding="utf-8"))
    failure_path = tmp_path / "evidence" / "submit-001.postprocessing_failure.json"
    failure = json.loads(failure_path.read_text(encoding="utf-8"))

    assert envelope["subprocess_exit_code"] == 0
    assert failure["remote_task_creation_state"] == "created_or_possible_created"
    assert failure["local_postprocessing_status"] == "failed"
    assert failure["submit_id"] == "SUB-001"
    assert failure["logid"] == "LOG-001"
    assert failure["credit_count"] == 70
    assert failure["submit_attempt_count"] == 1
    assert failure["created_task_count"] == 1


def test_03_atomic_write_interruption_leaves_no_valid_partial_record(tmp_path: Path) -> None:
    target = tmp_path / "record.json"

    def fail_replace(source: str, destination: str) -> None:
        raise OSError(f"replace interrupted: {source} -> {destination}")

    with pytest.raises(OSError, match="replace interrupted"):
        atomic_write_json(target, {"new": True}, replace_func=fail_replace)

    assert not target.exists()
    assert list(tmp_path.glob("*.tmp")) == []


def test_04_atomic_write_interruption_preserves_existing_valid_record(tmp_path: Path) -> None:
    target = tmp_path / "record.json"
    target.write_text('{"old": true}\n', encoding="utf-8")

    def fail_replace(source: str, destination: str) -> None:
        raise OSError("replace interrupted")

    with pytest.raises(OSError, match="replace interrupted"):
        atomic_write_json(target, {"new": True}, replace_func=fail_replace)

    assert json.loads(target.read_text(encoding="utf-8")) == {"old": True}
    assert list(tmp_path.glob("*.tmp")) == []


def test_05_sanitization_removes_secrets_but_preserves_operational_fields(
    tmp_path: Path,
) -> None:
    def runner(argv: list[str]) -> FakeResult:
        stdout = (
            '{"submit_id":"SUB-SECRET","logid":"LOG-SECRET",'
            '"gen_status":"querying","credit_count":70,'
            '"prompt":"full private prompt","access_token":"TOKEN-123",'
            '"token":"PLAIN-TOKEN-456",'
            '"download_url":"https://example.test/file?signature=secret"}'
        )
        stderr = "Authorization: Bearer BEARER-123\nCookie: SID=COOKIE-123"
        return FakeResult(list(argv), 0, stdout, stderr)

    execution = _execute(
        tmp_path,
        runner=runner,
        argv=[
            "dreamina",
            "text2video",
            "--prompt",
            "full private prompt",
            "--token",
            "TOKEN-123",
        ],
    )
    persisted = execution.envelope_path.read_text(encoding="utf-8")

    for secret in [
        "full private prompt",
        "TOKEN-123",
        "PLAIN-TOKEN-456",
        "BEARER-123",
        "COOKIE-123",
        "signature=secret",
    ]:
        assert secret not in persisted
    for operational in ["SUB-SECRET", "LOG-SECRET", "querying", "credit_count"]:
        assert operational in persisted
    parsed = json.loads(execution.parsed_evidence_path.read_text(encoding="utf-8"))
    assert parsed["submit_id"] == "SUB-SECRET"
    assert parsed["logid"] == "LOG-SECRET"
    assert parsed["credit_count"] == 70


def test_06_preexisting_created_submit_blocks_runner_invocation(tmp_path: Path) -> None:
    record = tmp_path / "existing.json"
    record.write_text(
        json.dumps(
            {
                "experiment_id": "EXP-001",
                "submit_evidence": {
                    "submit_id": "SUB-EXISTING",
                    "logid": "LOG-EXISTING",
                    "gen_status": "querying",
                },
                "query_count": 0,
                "download": {"download_count": 0},
            }
        ),
        encoding="utf-8",
    )
    calls: list[list[str]] = []

    def runner(argv: list[str]) -> FakeResult:
        calls.append(list(argv))
        return _submit_result(argv)

    with pytest.raises(DuplicateSubmitForbidden) as error:
        execute_with_durable_evidence(
            runner=runner,
            argv=["dreamina", "text2video", "--prompt", "private"],
            evidence_dir=tmp_path / "evidence",
            operation_id="submit-001",
            experiment_id="EXP-001",
            command_type="text2video",
            operation_kind="submit",
            existing_submit_record=record,
        )

    assert error.value.stage == "pre_subprocess_guard"
    assert calls == []
    assert not (tmp_path / "evidence").exists()


def test_07_recovery_read_path_uses_committed_f01_without_dreamina(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def forbidden(*args, **kwargs):
        raise AssertionError("Dreamina or subprocess must not run")

    monkeypatch.setattr(subprocess, "run", forbidden)
    before = hashlib.sha256(F01_RECORD.read_bytes()).hexdigest()
    recovery = load_existing_submit_evidence(F01_RECORD)
    after = hashlib.sha256(F01_RECORD.read_bytes()).hexdigest()

    assert before == after
    assert recovery["experiment_id"] == "CAL001-F01-P2-R1"
    assert recovery["existing_submit_created"] is True
    assert recovery["submit_id"] == "4e4588dd-a0e1-4539-8390-692cb9bf80f8"
    assert recovery["logid"] == "20260718154849169254047008489C358"
    assert recovery["last_known_remote_state"] == "querying"
    assert recovery["recorded_cost"] == 70
    assert recovery["query_count_already_used"] == 0
    assert recovery["download_count_already_used"] == 0
    assert recovery["query_recovery_eligible"] is True
    assert recovery["requires_separate_human_authorization"] is True
    assert recovery["retry_allowed"] is False
    assert recovery["resubmit_allowed"] is False


def test_08_existing_f01_explicitly_forbids_duplicate_submit() -> None:
    with pytest.raises(DuplicateSubmitForbidden) as error:
        assert_no_existing_submit(F01_RECORD, "CAL001-F01-P2-R1")
    assert error.value.submit_id == "4e4588dd-a0e1-4539-8390-692cb9bf80f8"


def test_09_runner_failure_before_command_result_is_distinct(tmp_path: Path) -> None:
    def runner(argv: list[str]) -> FakeResult:
        raise FileNotFoundError("fake executable missing")

    with pytest.raises(FileNotFoundError, match="fake executable missing"):
        _execute(tmp_path, runner=runner)

    failure_path = tmp_path / "evidence" / "submit-001.invocation_failure.json"
    failure = json.loads(failure_path.read_text(encoding="utf-8"))
    assert failure["subprocess_returned"] is False
    assert failure["remote_task_creation_state"] == "not_proven_created"
    assert failure["local_postprocessing_status"] == "not_started"
    assert not (tmp_path / "evidence" / "submit-001.subprocess_envelope.json").exists()


def test_10_dataset_mutation_failure_cannot_erase_envelope(tmp_path: Path) -> None:
    execution = _execute(tmp_path)
    envelope_before = execution.envelope_path.read_bytes()

    with pytest.raises(OSError, match="dataset mutation failed"):
        with execution.postprocessing_guard(stage="dataset_mutation"):
            raise OSError("dataset mutation failed")

    assert execution.envelope_path.read_bytes() == envelope_before
    failure = json.loads(
        (tmp_path / "evidence" / "submit-001.postprocessing_failure.json").read_text(
            encoding="utf-8"
        )
    )
    assert failure["failure_stage"] == "dataset_mutation"
    assert failure["submit_id"] == "SUB-001"
    assert failure["local_postprocessing_status"] == "failed"


@pytest.mark.parametrize(
    ("operation_kind", "expected_query_count", "expected_download_count"),
    [("query", 1, 0), ("download", 0, 1)],
)
def test_11_returned_recovery_operations_count_before_postprocessing(
    tmp_path: Path,
    operation_kind: str,
    expected_query_count: int,
    expected_download_count: int,
) -> None:
    execution = execute_with_durable_evidence(
        runner=lambda argv: FakeResult(list(argv), 0, '{"gen_status":"querying"}', ""),
        argv=["dreamina", "query_result", "--submit_id", "SUB-EXISTING"],
        evidence_dir=tmp_path / "evidence",
        operation_id=f"{operation_kind}-001",
        experiment_id="EXP-001",
        command_type="query_result",
        operation_kind=operation_kind,
        known_submit_id="SUB-EXISTING",
    )

    with pytest.raises(RuntimeError, match="later processing failed"):
        with execution.postprocessing_guard(stage=f"{operation_kind}_postprocessing"):
            raise RuntimeError("later processing failed")

    failure = json.loads(
        (
            tmp_path
            / "evidence"
            / f"{operation_kind}-001.postprocessing_failure.json"
        ).read_text(encoding="utf-8")
    )
    assert failure["remote_task_creation_state"] == "created_or_possible_created"
    assert failure["query_count"] == expected_query_count
    assert failure["download_count"] == expected_download_count


def test_12_caller_supplied_secret_is_redacted_from_failure_record(
    tmp_path: Path,
) -> None:
    execution = execute_with_durable_evidence(
        runner=_submit_result,
        argv=["dreamina", "text2video", "--prompt", "private prompt"],
        evidence_dir=tmp_path / "evidence",
        operation_id="submit-001",
        experiment_id="EXP-001",
        command_type="text2video",
        operation_kind="submit",
        secret_values=["UNLABELED-SECRET-VALUE"],
    )

    with pytest.raises(RuntimeError, match="UNLABELED-SECRET-VALUE"):
        with execution.postprocessing_guard(stage="later_validation"):
            raise RuntimeError("validation exposed UNLABELED-SECRET-VALUE")

    failure_text = (
        tmp_path / "evidence" / "submit-001.postprocessing_failure.json"
    ).read_text(encoding="utf-8")
    assert "UNLABELED-SECRET-VALUE" not in failure_text
    assert "<redacted_secret>" in failure_text
