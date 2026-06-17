from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..assets.registry import AssetRegistry
from ..core.models import ShotRecord, ShotStatus
from ..path_policy import PathPolicy


class ShotRegistryError(ValueError):
    pass


@dataclass
class ShotRegistry:
    path: Path
    path_policy: PathPolicy
    asset_registry: AssetRegistry | None = None

    def __post_init__(self) -> None:
        self.path = self.path_policy.ensure(Path(self.path))

    def _load_payload(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"shots": []}
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        if isinstance(raw, dict):
            return {
                "shots": raw.get("shots", []),
            }
        if isinstance(raw, list):
            return {"shots": raw}
        raise ShotRegistryError("Invalid shot registry format")

    def load(self) -> list[ShotRecord]:
        payload = self._load_payload()
        records = [ShotRecord.from_dict(item) for item in payload.get("shots", [])]
        return self._sort_shots(records)

    def save(self, shots: list[ShotRecord]) -> None:
        sorted_shots = self._sort_shots(shots)
        self.path_policy.ensure(self.path.parent)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps({"shots": [item.asdict() for item in sorted_shots]}, ensure_ascii=True, indent=2),
            encoding="utf-8",
        )

    def add_shot(self, shot: ShotRecord) -> ShotRecord:
        shot.validate()
        shots = self.load()
        shot.validate()
        if any(existing.shot_id == shot.shot_id for existing in shots):
            raise ShotRegistryError(f"Shot already exists: {shot.shot_id}")
        self._validate_required_assets(shot)
        shots.append(shot)
        self._validate_continuity_links(shots)
        self.save(shots)
        return shot

    def update_shot(self, shot_id: str, **updates: object) -> ShotRecord:
        shots = self.load()
        target = self.get_by_shot_id(shot_id)
        if target is None:
            raise ShotRegistryError(f"Shot not found: {shot_id}")
        idx = shots.index(target)
        payload = target.asdict()
        payload.update(updates)
        payload.pop("status", None)
        status = updates.get("status", target.status)
        if isinstance(status, ShotStatus):
            payload["status"] = status.value
        else:
            payload["status"] = str(status)
        payload.setdefault("review_status", payload.get("review_status", target.review_status))
        payload["required_asset_ids"] = list(payload.get("required_asset_ids") or [])
        updated = ShotRecord.from_dict(payload)
        shots[idx] = updated
        self._validate_required_assets(updated)
        self._validate_continuity_links(shots)
        self.save(shots)
        return updated

    def get_by_shot_id(self, shot_id: str) -> ShotRecord | None:
        for shot in self.load():
            if shot.shot_id == shot_id:
                return shot
        return None

    def list_by_scene(self, scene_id: str) -> list[ShotRecord]:
        return self._sort_shots([shot for shot in self.load() if shot.scene_id == scene_id])

    def list_by_status(self, status: ShotStatus | str) -> list[ShotRecord]:
        wanted = ShotStatus(status)
        return self._sort_shots([shot for shot in self.load() if shot.status == wanted])

    def validate_required_assets(self, shots: list[ShotRecord] | None = None) -> None:
        items = self.load() if shots is None else shots
        for shot in items:
            self._validate_required_assets(shot)

    def validate_continuity(self) -> None:
        self._validate_continuity_links(self.load())

    def _validate_continuity_links(self, shots: list[ShotRecord]) -> None:
        by_id = {shot.shot_id: shot for shot in shots}
        for shot in shots:
            if shot.previous_shot_id:
                previous_shot = by_id.get(shot.previous_shot_id)
                if previous_shot is None:
                    raise ShotRegistryError(f"Missing previous shot '{shot.previous_shot_id}' for {shot.shot_id}")
                if previous_shot.next_shot_id and previous_shot.next_shot_id != shot.shot_id:
                    raise ShotRegistryError(
                        f"Inconsistent continuity: {previous_shot.shot_id} -> {previous_shot.next_shot_id}"
                    )
            if shot.next_shot_id:
                next_shot = by_id.get(shot.next_shot_id)
                if next_shot is not None and next_shot.previous_shot_id and next_shot.previous_shot_id != shot.shot_id:
                    raise ShotRegistryError(
                        f"Inconsistent continuity: {next_shot.shot_id} <- {next_shot.previous_shot_id}"
                    )

    def _validate_required_assets(self, shot: ShotRecord) -> None:
        if not self.asset_registry or not shot.required_asset_ids:
            return
        for entry in shot.required_asset_ids:
            logical_id, candidate_id = self._parse_asset_reference(entry)
            matches = self.asset_registry.get_by_logical_id(logical_id, candidate_id)
            if not matches:
                raise ShotRegistryError(f"Missing required asset: {entry}")

    @staticmethod
    def _parse_asset_reference(entry: str) -> tuple[str, str | None]:
        if ":" in entry:
            logical_id, candidate_id = entry.split(":", 1)
            return logical_id.strip(), candidate_id.strip() or None
        return entry.strip(), None

    @staticmethod
    def _sort_shots(shots: list[ShotRecord]) -> list[ShotRecord]:
        return sorted(shots, key=lambda item: (item.scene_id, item.shot_index, item.shot_id))
