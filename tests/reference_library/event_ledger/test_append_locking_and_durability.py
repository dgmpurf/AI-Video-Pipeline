from __future__ import annotations

import multiprocessing
import os
import threading
import time
from pathlib import Path

import pytest

from app.ai_video_pipeline.reference_library.event_ledger import append_event
from app.ai_video_pipeline.reference_library.event_ledger.errors import (
    DuplicateEventError,
    LedgerLockedError,
    LedgerValidationError,
)
from app.ai_video_pipeline.reference_library.event_ledger.ledger import (
    _append_durable,
    _write_complete,
)
from app.ai_video_pipeline.reference_library.event_ledger.locking import (
    ExclusiveLedgerLock,
)
from app.ai_video_pipeline.reference_library.event_ledger.manifest import (
    EVENTS_FILENAME,
    LOCK_FILENAME,
)


def _hold_lock_in_process(lock_path: str, ready, release) -> None:
    with ExclusiveLedgerLock(lock_path):
        ready.set()
        release.wait(10)


class _ShortWriteHandle:
    def __init__(self) -> None:
        self.data = bytearray()

    def write(self, data) -> int:
        selected = bytes(data[:3])
        self.data.extend(selected)
        return len(selected)


def test_complete_write_loop_handles_short_writes() -> None:
    handle = _ShortWriteHandle()
    _write_complete(handle, b"0123456789")
    assert bytes(handle.data) == b"0123456789"


def test_stale_preexisting_lock_hard_stops_without_write(
    initialized_ledger, base_adapter, make_event
) -> None:
    lock_path = initialized_ledger / LOCK_FILENAME
    lock_path.write_bytes(b"stale evidence")
    with pytest.raises(LedgerLockedError):
        append_event(initialized_ledger, base_adapter, make_event())
    assert lock_path.read_bytes() == b"stale evidence"
    assert not (initialized_ledger / EVENTS_FILENAME).exists()


def test_lock_is_held_through_post_write_tail_verification(
    initialized_ledger, base_adapter, make_event, monkeypatch
) -> None:
    import app.ai_video_pipeline.reference_library.event_ledger.ledger as ledger_module

    original = ledger_module._post_write_validate
    observed: list[bool] = []

    def checking(*args, **kwargs):
        observed.append((initialized_ledger / LOCK_FILENAME).exists())
        return original(*args, **kwargs)

    monkeypatch.setattr(ledger_module, "_post_write_validate", checking)
    append_event(initialized_ledger, base_adapter, make_event())
    assert observed == [True]
    assert not (initialized_ledger / LOCK_FILENAME).exists()


def test_append_flushes_then_fsyncs_a_writable_descriptor(tmp_path: Path, monkeypatch) -> None:
    path = tmp_path / "events.jsonl"
    calls: list[str] = []
    import app.ai_video_pipeline.reference_library.event_ledger.ledger as ledger_module

    original_write = ledger_module._write_complete
    real_fsync = os.fsync

    def tracking_write(handle, data):
        calls.append("write")
        return original_write(handle, data)

    def tracking_fsync(descriptor):
        os.write(descriptor, b"")
        calls.append("fsync")
        return real_fsync(descriptor)

    monkeypatch.setattr(ledger_module, "_write_complete", tracking_write)
    monkeypatch.setattr(ledger_module.os, "fsync", tracking_fsync)
    _append_durable(path, b"line\n")
    assert calls == ["write", "fsync"]
    assert path.read_bytes() == b"line\n"


def test_simulated_write_interruption_leaves_evidence_and_no_repair(
    initialized_ledger, base_adapter, make_event, monkeypatch
) -> None:
    import app.ai_video_pipeline.reference_library.event_ledger.ledger as ledger_module

    def interrupted(handle, data):
        handle.write(data[:11])
        raise OSError("simulated write interruption")

    monkeypatch.setattr(ledger_module, "_write_complete", interrupted)
    with pytest.raises(OSError, match="write interruption"):
        append_event(initialized_ledger, base_adapter, make_event())
    path = initialized_ledger / EVENTS_FILENAME
    assert 0 < path.stat().st_size < 100
    assert not (initialized_ledger / LOCK_FILENAME).exists()
    monkeypatch.undo()
    with pytest.raises(LedgerValidationError):
        append_event(initialized_ledger, base_adapter, make_event())


def test_simulated_fsync_interruption_does_not_reappend_or_repair(
    initialized_ledger, base_adapter, make_event, monkeypatch
) -> None:
    import app.ai_video_pipeline.reference_library.event_ledger.ledger as ledger_module

    draft = make_event()

    def interrupted(_descriptor):
        raise OSError("simulated fsync interruption")

    monkeypatch.setattr(ledger_module.os, "fsync", interrupted)
    with pytest.raises(OSError, match="fsync interruption"):
        append_event(initialized_ledger, base_adapter, draft)
    path = initialized_ledger / EVENTS_FILENAME
    assert path.read_bytes().endswith(b"\n")
    assert not (initialized_ledger / LOCK_FILENAME).exists()
    monkeypatch.undo()
    before = path.read_bytes()
    with pytest.raises(DuplicateEventError):
        append_event(initialized_ledger, base_adapter, draft)
    assert path.read_bytes() == before


def test_postwrite_verification_failure_preserves_entry_without_repair(
    initialized_ledger, base_adapter, make_event, monkeypatch
) -> None:
    import app.ai_video_pipeline.reference_library.event_ledger.ledger as ledger_module

    def fail(*_args, **_kwargs):
        assert (initialized_ledger / LOCK_FILENAME).exists()
        raise RuntimeError("simulated postwrite verification failure")

    monkeypatch.setattr(ledger_module, "_post_write_validate", fail)
    with pytest.raises(RuntimeError, match="postwrite"):
        append_event(initialized_ledger, base_adapter, make_event())
    assert (initialized_ledger / EVENTS_FILENAME).read_bytes().endswith(b"\n")
    assert not (initialized_ledger / LOCK_FILENAME).exists()


def test_thread_contention_allows_exactly_one_lock_owner(tmp_path: Path) -> None:
    lock_path = tmp_path / LOCK_FILENAME
    barrier = threading.Barrier(2)
    outcomes: list[str] = []

    def contender() -> None:
        barrier.wait()
        try:
            with ExclusiveLedgerLock(lock_path):
                outcomes.append("won")
                time.sleep(0.1)
        except LedgerLockedError:
            outcomes.append("blocked")

    threads = [threading.Thread(target=contender) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=5)
    assert sorted(outcomes) == ["blocked", "won"]
    assert not lock_path.exists()


def test_spawned_process_contention_observes_existing_lock(tmp_path: Path) -> None:
    context = multiprocessing.get_context("spawn")
    ready = context.Event()
    release = context.Event()
    lock_path = tmp_path / LOCK_FILENAME
    process = context.Process(
        target=_hold_lock_in_process,
        args=(str(lock_path), ready, release),
    )
    process.start()
    assert ready.wait(10)
    try:
        with pytest.raises(LedgerLockedError):
            ExclusiveLedgerLock(lock_path).acquire()
    finally:
        release.set()
        process.join(timeout=10)
    assert process.exitcode == 0
    assert not lock_path.exists()
