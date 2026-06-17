from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Sequence

from ..core.models import ProviderName, TaskSpec


@dataclass(frozen=True)
class ProviderConfig:
    name: str
    enabled: bool = False
    mode: str = "stub"
    executable: Optional[str] = None
    allow_live_run: bool = False
    extras: Dict[str, Any] = None

    @staticmethod
    def from_mapping(name: str, data: Dict[str, Any]) -> "ProviderConfig":
        return ProviderConfig(
            name=name,
            enabled=bool(data.get("enabled", False)),
            mode=data.get("mode", "stub"),
            executable=data.get("executable"),
            allow_live_run=bool(data.get("allow_live_run", False)),
            extras=dict(data),
        )


class ProviderAdapter(ABC):
    name: ProviderName

    @abstractmethod
    def build_submit_command(self, task: TaskSpec, references: Sequence[Path]) -> list[str]:
        ...


def load_provider_config(config_path: Path) -> Dict[str, ProviderConfig]:
    payload = json.loads(Path(config_path).read_text(encoding="utf-8"))
    providers = payload.get("providers", {})
    return {name: ProviderConfig.from_mapping(name, dict(cfg)) for name, cfg in providers.items()}
