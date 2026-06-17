from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Iterable

from ..core.models import (
    AssetRecord,
    AssetRelationship,
    AssetRelationshipType,
    AssetStatus,
    ReviewStatus,
)
from ..path_policy import PathPolicy


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _normalize_key(logical_id: str, candidate_id: str) -> tuple[str, str]:
    return (str(logical_id), str(candidate_id))


class AssetRegistry:
    """Persistent helper for candidate/asset tracking."""

    def __init__(self, path: Path, policy: PathPolicy | None = None) -> None:
        self.path = policy.ensure(path) if policy is not None else Path(path)
        self.policy = policy

    def load(self) -> list[AssetRecord]:
        payload = self._load_payload()
        return payload["assets"]

    def save(self, records: list[AssetRecord], relationships: list[AssetRelationship] | None = None) -> None:
        payload = {"assets": [item.asdict() for item in records], "relationships": []}
        relationships = relationships or self._load_payload()["relationships"]
        payload["relationships"] = [item.asdict() for item in relationships]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.policy is not None:
            self.policy.ensure(self.path)
        self.path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")

    def add_asset(self, asset: AssetRecord) -> AssetRecord:
        if not asset.candidate_id:
            raise ValueError("candidate_id is required for AssetRecord")
        records, relationships = self._load_payload().values()
        records.append(asset)
        self.save(records, relationships)
        return asset

    def update_asset(self, logical_id: str, candidate_id: str, **updates: object) -> AssetRecord:
        records, relationships = self._load_payload().values()
        target = self._find_asset(records, logical_id, candidate_id)
        if target is None:
            raise KeyError(f"asset not found: {logical_id}/{candidate_id}")

        for key, value in updates.items():
            if key == "status":
                value = AssetStatus(value)
            elif key == "review_status":
                value = ReviewStatus(value)
            setattr(target, key, value)
        target.updated_at = _now()
        self.save(records, relationships)
        return target

    def get_by_logical_id(self, logical_id: str, candidate_id: str | None = None) -> list[AssetRecord]:
        records = self.load()
        if candidate_id is None:
            return [item for item in records if item.logical_id == logical_id]
        return [item for item in records if item.logical_id == logical_id and item.candidate_id == candidate_id]

    def list_by_status(self, status: AssetStatus | str) -> list[AssetRecord]:
        wanted = AssetStatus(status)
        return [item for item in self.load() if item.status == wanted]

    def list_by_review_status(self, review_status: ReviewStatus | str) -> list[AssetRecord]:
        wanted = ReviewStatus(review_status)
        return [item for item in self.load() if item.review_status == wanted]

    def list_by_asset_type(self, asset_type: str) -> list[AssetRecord]:
        return [item for item in self.load() if item.asset_type.value == asset_type]

    def reject_asset(self, logical_id: str, candidate_id: str, reason: str) -> AssetRecord:
        if not reason:
            raise ValueError("reject reason required")
        return self.update_asset(
            logical_id=logical_id,
            candidate_id=candidate_id,
            status=AssetStatus.rejected.value,
            review_status=ReviewStatus.rejected.value,
            review_note=reason,
        )

    def archive_asset(self, logical_id: str, candidate_id: str) -> AssetRecord:
        return self.update_asset(
            logical_id=logical_id,
            candidate_id=candidate_id,
            status=AssetStatus.archived.value,
            review_status=ReviewStatus.pending_review.value,
        )

    def mark_as_candidate(self, logical_id: str, candidate_id: str) -> AssetRecord:
        return self.update_asset(
            logical_id=logical_id,
            candidate_id=candidate_id,
            status=AssetStatus.candidate.value,
            review_status=ReviewStatus.pending_review.value,
        )

    def can_be_reference(self, logical_id: str, candidate_id: str | None = None) -> bool:
        entries = self.get_by_logical_id(logical_id, candidate_id)
        if not entries:
            return False
        return all(item.status not in {AssetStatus.rejected, AssetStatus.archived} for item in entries)

    def add_relationship(self, relationship: AssetRelationship) -> AssetRelationship:
        payload = self._load_payload()
        relationships = payload["relationships"]
        relationships.append(relationship)
        self.save(payload["assets"], relationships)
        return relationship

    def list_relationships(
        self,
        logical_id: str,
        candidate_id: str | None = None,
    ) -> list[AssetRelationship]:
        relationships = self._load_payload()["relationships"]
        result: list[AssetRelationship] = []
        for item in relationships:
            if item.logical_id == logical_id and (candidate_id is None or item.candidate_id == candidate_id):
                result.append(item)
                continue
            if item.related_logical_id == logical_id and (
                candidate_id is None or item.related_candidate_id == candidate_id
            ):
                result.append(item)
        return result

    def add_exact_duplicate(self, left: tuple[str, str], right: tuple[str, str]) -> AssetRelationship:
        left_asset = self._find_asset_payload(left[0], left[1])
        right_asset = self._find_asset_payload(right[0], right[1])
        if left_asset is None or right_asset is None:
            raise KeyError("both assets must exist before duplicate linkage")

        canonical_key = min(_normalize_key(left[0], left[1]), _normalize_key(right[0], right[1]))
        duplicate_key = max(_normalize_key(left[0], left[1]), _normalize_key(right[0], right[1]))
        relationship = AssetRelationship(
            logical_id=canonical_key[0],
            candidate_id=canonical_key[1],
            related_logical_id=duplicate_key[0],
            related_candidate_id=duplicate_key[1],
            relationship_type=AssetRelationshipType.exact_duplicate,
            is_canonical=True,
        )
        payload = self._load_payload()
        self._remove_existing_pair_relationships(payload["relationships"], left, right, AssetRelationshipType.exact_duplicate)
        payload["relationships"].append(relationship)
        self.save(payload["assets"], payload["relationships"])
        return relationship

    def mark_continuity_pair(
        self,
        left: tuple[str, str],
        right: tuple[str, str],
        note: str = "",
    ) -> AssetRelationship:
        relationship = AssetRelationship(
            logical_id=left[0],
            candidate_id=left[1],
            related_logical_id=right[0],
            related_candidate_id=right[1],
            relationship_type=AssetRelationshipType.continuity_pair,
            is_canonical=False,
            note=note,
        )
        return self.add_relationship(relationship)

    def mark_near_duplicate_variant(
        self,
        left: tuple[str, str],
        right: tuple[str, str],
        note: str = "",
    ) -> AssetRelationship:
        relationship = AssetRelationship(
            logical_id=left[0],
            candidate_id=left[1],
            related_logical_id=right[0],
            related_candidate_id=right[1],
            relationship_type=AssetRelationshipType.near_duplicate_variant,
            is_canonical=False,
            note=note,
        )
        return self.add_relationship(relationship)

    def get_canonical_for_exact_duplicate(self, logical_id: str, candidate_id: str) -> tuple[str, str] | None:
        for item in self.list_by_type(logical_id, candidate_id, AssetRelationshipType.exact_duplicate):
            if item.is_canonical:
                return item.logical_id, item.candidate_id
            return item.related_logical_id, item.related_candidate_id
        return None

    def list_by_type(
        self,
        logical_id: str,
        candidate_id: str,
        relationship_type: AssetRelationshipType,
    ) -> list[AssetRelationship]:
        return [
            item
            for item in self.list_relationships(logical_id, candidate_id)
            if item.relationship_type == relationship_type
        ]

    def _find_asset(self, records: list[AssetRecord], logical_id: str, candidate_id: str) -> AssetRecord | None:
        for item in records:
            if item.logical_id == logical_id and item.candidate_id == candidate_id:
                return item
        return None

    def _find_asset_payload(self, logical_id: str, candidate_id: str) -> AssetRecord | None:
        records = self._load_payload()["assets"]
        return self._find_asset(records, logical_id, candidate_id)

    def _remove_existing_pair_relationships(
        self,
        relationships: list[AssetRelationship],
        left: tuple[str, str],
        right: tuple[str, str],
        relationship_type: AssetRelationshipType,
    ) -> None:
        left_key = _normalize_key(left[0], left[1])
        right_key = _normalize_key(right[0], right[1])
        filtered: list[AssetRelationship] = []
        for item in relationships:
            if item.relationship_type != relationship_type:
                filtered.append(item)
                continue
            first = _normalize_key(item.logical_id, item.candidate_id)
            second = _normalize_key(item.related_logical_id, item.related_candidate_id)
            if {first, second} == {left_key, right_key}:
                continue
            filtered.append(item)
        relationships[:] = filtered

    def _load_payload(self) -> dict[str, list]:
        if not self.path.exists():
            return {"assets": [], "relationships": []}

        raw = json.loads(self.path.read_text(encoding="utf-8"))
        if isinstance(raw, list):
            records = [AssetRecord.from_dict(item) for item in raw]
            return {"assets": records, "relationships": []}

        records = [AssetRecord.from_dict(item) for item in raw.get("assets", [])]
        relationships = [AssetRelationship.from_dict(item) for item in raw.get("relationships", [])]
        return {"assets": records, "relationships": relationships}

    def _to_json_payload(self, records: list[AssetRecord], relationships: list[AssetRelationship]) -> dict[str, object]:
        return {
            "assets": [item.asdict() for item in records],
            "relationships": [item.asdict() for item in relationships],
        }
