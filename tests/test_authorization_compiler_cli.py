from __future__ import annotations

import base64
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "authorization_compiler.py"
VISUAL_RECORD = (
    ROOT
    / "experiments"
    / "CAL-001"
    / "authorizations"
    / "CAL001_P3D_W01_F06_recovery_visual_review_record_and_technical_completion_authorization.json"
)
CHECKPOINT = "a838723b8824a1003b6abab220257d0e20fa31ad"


def _run(*args: str, input_bytes: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=ROOT,
        input=input_bytes,
        capture_output=True,
        check=False,
    )


def test_compile_file_and_stdin_exact_are_deterministic(tmp_path: Path) -> None:
    raw = b"APPROVE_CLI_EXACT_INPUT."
    source = tmp_path / "authorization.txt"
    source.write_bytes(raw)

    first = _run("compile", "--text-file", str(source))
    second = _run("compile", "--stdin-exact", input_bytes=raw)
    third = _run("compile", "--text-file", str(source))

    assert first.returncode == 0
    assert second.returncode == 0
    assert third.returncode == 0
    assert first.stderr == b""
    assert first.stdout == second.stdout == third.stdout
    payload = json.loads(first.stdout.decode("utf-8", errors="strict"))
    assert payload["command"] == "compile"
    assert payload["byte_length"] == len(raw)
    assert payload["sha256"] == hashlib.sha256(raw).hexdigest()
    assert payload["base64"] == base64.b64encode(raw).decode("ascii")
    assert payload["serialization_profile_valid"] is True
    assert payload["authorization_evidence_verified"] is False
    assert payload["authorization_verified"] is False
    assert payload["eligible_for_authority_activation"] is False
    assert payload["execution_authority_active"] is False


def test_compile_rejects_trailing_lf_without_repair() -> None:
    result = _run("compile", "--stdin-exact", input_bytes=b"APPROVE_CLI.\n")

    assert result.returncode == 1
    payload = json.loads(result.stdout.decode("utf-8", errors="strict"))
    assert payload["lf_present"] is True
    assert payload["trailing_newline"] is True
    assert payload["authorization_verified"] is False
    assert payload["provider_command_invocation_count"] == 0


def test_verify_mode_checks_expected_values(tmp_path: Path) -> None:
    raw = b"APPROVE_VERIFY_MODE."
    source = tmp_path / "authorization.txt"
    source.write_bytes(raw)
    encoded = base64.b64encode(raw).decode("ascii")

    result = _run(
        "verify",
        "--text-file",
        str(source),
        "--expected-byte-length",
        str(len(raw)),
        "--expected-sha256",
        hashlib.sha256(raw).hexdigest(),
        "--expected-base64",
        encoded,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout.decode("utf-8", errors="strict"))
    assert payload["command"] == "verify"
    assert payload["expected_values_match"] is True
    assert payload["authorization_evidence_verified"] is True
    assert payload["authorization_verified"] is True
    assert payload["eligible_for_authority_activation"] is False
    assert payload["execution_authority_active"] is False


def test_verify_record_mode_reproduces_committed_visual_fixture(
    tmp_path: Path,
) -> None:
    record = json.loads(VISUAL_RECORD.read_bytes().decode("utf-8", errors="strict"))
    raw = record["canonical_authorization_text"].encode("utf-8")
    source = tmp_path / "authorization.txt"
    source.write_bytes(raw)

    result = _run(
        "verify-record",
        "--text-file",
        str(source),
        "--record",
        str(VISUAL_RECORD),
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout.decode("utf-8", errors="strict"))
    assert payload["command"] == "verify-record"
    assert payload["expected_base64_matches"] is True
    assert payload["record_canonical_text_matches"] is True
    assert payload["record_representations_consistent"] is True
    assert payload["authorization_evidence_verified"] is True
    assert payload["authorization_verified"] is True


def test_verify_checkpoint_uses_only_explicit_values() -> None:
    result = _run(
        "verify-checkpoint",
        "--required-checkpoint",
        CHECKPOINT,
        "--local-head",
        CHECKPOINT,
        "--origin-main",
        CHECKPOINT,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout.decode("utf-8", errors="strict"))
    assert payload["checkpoint_binding_verified"] is True
    assert payload["eligible_for_authority_activation"] is False
    assert payload["execution_authority_active"] is False
    assert payload["provider_command_allowed"] is False


def test_exact_input_modes_are_mutually_exclusive(tmp_path: Path) -> None:
    source = tmp_path / "authorization.txt"
    source.write_bytes(b"APPROVE_EXACT.")

    result = _run(
        "compile",
        "--text-file",
        str(source),
        "--stdin-exact",
        input_bytes=b"APPROVE_EXACT.",
    )

    assert result.returncode == 2
    assert result.stdout == b""


def test_atomic_output_requires_explicit_overwrite(tmp_path: Path) -> None:
    raw = b"APPROVE_ATOMIC_OUTPUT."
    source = tmp_path / "authorization.txt"
    output = tmp_path / "compiled.json"
    source.write_bytes(raw)

    first = _run(
        "compile",
        "--text-file",
        str(source),
        "--output",
        str(output),
    )
    before = output.read_bytes()
    blocked = _run(
        "compile",
        "--text-file",
        str(source),
        "--output",
        str(output),
    )
    after_block = output.read_bytes()
    overwritten = _run(
        "compile",
        "--text-file",
        str(source),
        "--output",
        str(output),
        "--overwrite",
    )

    assert first.returncode == 0
    assert first.stdout == b""
    assert blocked.returncode == 2
    assert after_block == before
    assert overwritten.returncode == 0
    assert output.read_bytes() == before
    payload = json.loads(before.decode("utf-8", errors="strict"))
    assert payload["serialization_profile_valid"] is True
    assert payload["authorization_verified"] is False


def test_verify_record_rejects_conflicting_aliases(tmp_path: Path) -> None:
    raw = b"APPROVE_CLI_CONFLICT."
    source = tmp_path / "authorization.txt"
    record_path = tmp_path / "conflicting-record.json"
    source.write_bytes(raw)
    record_path.write_text(
        json.dumps(
            {
                "byte_length": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "base64": base64.b64encode(raw).decode("ascii"),
                "authorization_base64": base64.b64encode(
                    b"APPROVE_CLI_DIFFERENT."
                ).decode("ascii"),
            }
        ),
        encoding="utf-8",
    )

    result = _run(
        "verify-record",
        "--text-file",
        str(source),
        "--record",
        str(record_path),
    )

    assert result.returncode == 1
    assert result.stderr == b""
    payload = json.loads(result.stdout.decode("utf-8", errors="strict"))
    assert payload["record_representations_consistent"] is False
    assert payload["record_representation_conflicts"] == ["base64"]
    assert payload["authorization_evidence_verified"] is False
    assert payload["authorization_verified"] is False
    assert payload["eligible_for_authority_activation"] is False
