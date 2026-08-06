from __future__ import annotations

import os
from pathlib import Path

from .errors import LedgerLockedError


class ExclusiveLedgerLock:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._descriptor: int | None = None
        self._owned = False

    @property
    def owned(self) -> bool:
        return self._owned

    def acquire(self) -> "ExclusiveLedgerLock":
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        flags |= getattr(os, "O_BINARY", 0)
        try:
            descriptor = os.open(self.path, flags, 0o600)
        except FileExistsError as error:
            raise LedgerLockedError(
                f"ledger lock already exists: {self.path}"
            ) from error
        self._descriptor = descriptor
        self._owned = True
        return self

    def release(self) -> None:
        if not self._owned:
            return
        descriptor = self._descriptor
        self._descriptor = None
        if descriptor is not None:
            os.close(descriptor)
        try:
            self.path.unlink()
        finally:
            self._owned = False

    def __enter__(self) -> "ExclusiveLedgerLock":
        return self.acquire()

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.release()
