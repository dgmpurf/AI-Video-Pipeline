from __future__ import annotations

from pathlib import Path


def compute_sha256(path: Path, block_size: int = 1024 * 1024) -> str:
    hash_obj = __import__("hashlib").sha256()
    with Path(path).open("rb") as handle:
        while True:
            chunk = handle.read(block_size)
            if not chunk:
                break
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


def verify_sha256(path: Path, expected_sha256: str) -> bool:
    return compute_sha256(path) == expected_sha256
