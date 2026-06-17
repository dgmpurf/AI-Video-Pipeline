from __future__ import annotations

import re
import shutil
import uuid
from pathlib import Path

from ..assets.media_integrity import compute_sha256
from ..path_policy import PathPolicy


def _normalize_ref_filename(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", value)
    if not safe or set(safe) == {"_"}:
        safe = f"ref_{uuid.uuid4().hex[:8]}"
    return safe


def stage_media_file(source_path: Path, staging_root: Path, policy: PathPolicy) -> tuple[Path, str]:
    src = policy.ensure(source_path)
    policy.ensure(staging_root)
    digest = compute_sha256(src)
    safe_name = f"{_normalize_ref_filename(src.stem)}_{digest[:12]}{src.suffix.lower()}"
    staged = Path(staging_root) / safe_name
    if staged.exists():
        if compute_sha256(staged) == digest:
            return staged, digest
    policy.ensure_write(staged)
    staged.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, staged)
    return staged, digest
