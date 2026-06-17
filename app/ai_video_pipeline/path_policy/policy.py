from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from shutil import copy2


class PathPolicyError(ValueError):
    pass


@dataclass(frozen=True)
class PathPolicy:
    workspace_root: Path

    def __post_init__(self) -> None:
        object.__setattr__(self, "workspace_root", Path(self.workspace_root).resolve())

    def _in_workspace(self, candidate: Path) -> bool:
        resolved = Path(candidate).resolve()
        try:
            resolved.relative_to(self.workspace_root)
            return True
        except ValueError:
            return False

    def ensure(self, candidate: Path) -> Path:
        resolved = Path(candidate).resolve()
        if not self._in_workspace(resolved):
            raise PathPolicyError(f"Path denied by workspace policy: {resolved}")
        return resolved

    def ensure_mkdir(self, path: Path) -> Path:
        target = self.ensure(path)
        return target

    def ensure_write(self, path: Path) -> Path:
        target = self.ensure(path)
        return target

    def ensure_copy(self, src: Path, dst: Path) -> tuple[Path, Path]:
        return self.ensure(src), self.ensure(dst)

    def ensure_rename(self, src: Path, dst: Path) -> tuple[Path, Path]:
        return self.ensure(src), self.ensure(dst)

    def mkdir(self, path: Path, exist_ok: bool = True) -> None:
        target = self.ensure_mkdir(path)
        target.mkdir(parents=True, exist_ok=exist_ok)

    def write_text(self, path: Path, content: str, encoding: str = "utf-8") -> Path:
        target = self.ensure_write(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding=encoding)
        return target

    def copy(self, src: Path, dst: Path) -> Path:
        self.ensure_copy(src, dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        return Path(copy2(src, dst))

    def rename(self, src: Path, dst: Path) -> Path:
        self.ensure_rename(src, dst)
        return Path(src).rename(dst)
