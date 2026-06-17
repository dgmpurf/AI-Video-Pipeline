from __future__ import annotations

from pathlib import Path
from typing import List

from ..path_policy import PathPolicy, PathPolicyError


def _is_hidden_path(path: Path) -> bool:
    return any(part != "." and part.startswith(".") for part in path.parts)


def discover_manifests(production_dir: Path, path_policy: PathPolicy) -> List[Path]:
    production = path_policy.ensure(Path(production_dir))
    manifests_dir = production / "manifests"

    if not manifests_dir.is_dir():
        return []

    policy = path_policy
    try:
        policy.ensure(manifests_dir)
    except PathPolicyError:
        raise

    discovered: list[Path] = []
    for path in manifests_dir.rglob("*.csv"):
        if path.is_dir() or path.suffix.lower() != ".csv":
            continue
        if _is_hidden_path(path) or path.name.startswith("."):
            continue
        discovered.append(policy.ensure(path))

    return sorted(discovered)


def discover_manifest_files(production_dir: Path, workspace_root: Path) -> List[Path]:
    return discover_manifests(production_dir, PathPolicy(workspace_root))
