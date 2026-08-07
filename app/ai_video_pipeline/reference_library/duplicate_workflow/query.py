from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Mapping

from .errors import QueryError
from .models import VerificationResult
from .promotion import resolve_current
from .verify import open_read_only, require_valid_generation


QUERY_CONTRACT_VERSION = "RL_P3_QUERY_V0_1"


def _rows(connection: sqlite3.Connection, sql: str, values: tuple[Any, ...]) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(sql, values).fetchall()]


def _json(value: str) -> Any:
    try:
        return json.loads(value)
    except json.JSONDecodeError as error:
        raise QueryError("stored bounded JSON is invalid") from error


class DuplicateWorkflowReadModel:
    """Pinned read-only access to one verified immutable RL-P3 generation."""

    def __init__(
        self,
        generation_path: Path,
        verification: VerificationResult,
        connection: sqlite3.Connection,
    ) -> None:
        self.generation_path = generation_path
        self.verification = verification
        self.connection = connection

    @classmethod
    def open_generation(
        cls,
        generation_path: str | Path,
        *,
        pointer: Mapping[str, Any] | str | Path | None = None,
        expected_upstream: Mapping[str, Any] | None = None,
    ) -> "DuplicateWorkflowReadModel":
        path = Path(generation_path).resolve(strict=True)
        verification = require_valid_generation(
            path, pointer=pointer, expected_upstream=expected_upstream
        )
        return cls(path, verification, open_read_only(path))

    @classmethod
    def open_current(
        cls,
        state_root: str | Path,
        *,
        expected_upstream: Mapping[str, Any] | None = None,
    ) -> "DuplicateWorkflowReadModel":
        generation, pointer = resolve_current(state_root)
        return cls.open_generation(
            generation, pointer=pointer, expected_upstream=expected_upstream
        )

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "DuplicateWorkflowReadModel":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _envelope(self) -> dict[str, Any]:
        meta = self.verification.metadata
        return {
            "generation_filename": self.generation_path.name,
            "materialization_generation_id": meta["materialization_generation_id"],
            "read_model_schema_version": meta["read_model_schema_version"],
            "logical_hash_registry_version": meta["logical_hash_registry_version"],
            "logical_content_hash": self.verification.logical_content_hash,
            "v0_2_ledger_id": meta["v0_2_ledger_id"],
            "v0_2_checkpoint_id": meta["v0_2_checkpoint_id"],
            "v0_2_through_position": meta["v0_2_through_position"],
            "v0_2_projection_hash": meta["v0_2_projection_hash"],
        }

    def pair_state(self, pair_id: str) -> dict[str, Any]:
        if not isinstance(pair_id, str) or not pair_id:
            raise QueryError("pair_id must be a nonempty string")
        history = _rows(
            self.connection,
            "SELECT * FROM pair_relation_history WHERE pair_id=? "
            "ORDER BY ledger_position,event_id COLLATE BINARY",
            (pair_id,),
        )
        decisions = [
            row for row in history
            if row["record_kind"] == "DECISION" and row["active"] == 1
        ]
        return {
            "query_contract_version": QUERY_CONTRACT_VERSION,
            "query_kind": "PAIR_STATE_FROM_PAIR_HISTORY_ONLY",
            "generation": self._envelope(),
            "pair_id": pair_id,
            "history": history,
            "current_decision": decisions[-1] if decisions else None,
            "cluster_inference_used": False,
        }

    def cluster_state(self, cluster_snapshot_id: str) -> dict[str, Any]:
        snapshots = _rows(
            self.connection,
            "SELECT * FROM cluster_snapshot WHERE cluster_snapshot_id=?",
            (cluster_snapshot_id,),
        )
        if len(snapshots) > 1:
            raise QueryError("cluster snapshot identity is ambiguous")
        members = _rows(
            self.connection,
            "SELECT * FROM cluster_member WHERE cluster_snapshot_id=? "
            "ORDER BY member_ordinal,member_id COLLATE BINARY",
            (cluster_snapshot_id,),
        )
        history = _rows(
            self.connection,
            "SELECT * FROM cluster_confirmation_history WHERE cluster_snapshot_id=? "
            "ORDER BY ledger_position,event_id COLLATE BINARY",
            (cluster_snapshot_id,),
        )
        current = [row for row in history if row["active"] == 1]
        return {
            "query_contract_version": QUERY_CONTRACT_VERSION,
            "query_kind": "CLUSTER_STATE",
            "generation": self._envelope(),
            "snapshot": snapshots[0] if snapshots else None,
            "members": members,
            "confirmation_history": history,
            "current_confirmation": current[-1] if current else None,
            "pair_authority_created": False,
        }

    def representative_state(
        self, cluster_snapshot_id: str, representative_role: str
    ) -> dict[str, Any]:
        arguments = (cluster_snapshot_id, representative_role)
        proposals = _rows(
            self.connection,
            "SELECT * FROM representative_proposal_history "
            "WHERE cluster_snapshot_id=? AND representative_role=? "
            "ORDER BY ledger_position,event_id COLLATE BINARY",
            arguments,
        )
        decisions = _rows(
            self.connection,
            "SELECT * FROM representative_decision_history "
            "WHERE cluster_snapshot_id=? AND representative_role=? "
            "ORDER BY ledger_position,event_id COLLATE BINARY",
            arguments,
        )
        current_proposals = [row for row in proposals if row["current"] == 1 and row["active"] == 1]
        current_decisions = [row for row in decisions if row["current"] == 1 and row["active"] == 1]
        return {
            "query_contract_version": QUERY_CONTRACT_VERSION,
            "query_kind": "REPRESENTATIVE_STATE",
            "generation": self._envelope(),
            "cluster_snapshot_id": cluster_snapshot_id,
            "representative_role": representative_role,
            "proposal_history": proposals,
            "decision_history": decisions,
            "current_proposal": current_proposals[-1] if current_proposals else None,
            "current_decision": current_decisions[-1] if current_decisions else None,
        }

    def execution_eligibility(
        self, cluster_snapshot_id: str, representative_role: str
    ) -> dict[str, Any]:
        state = self.representative_state(cluster_snapshot_id, representative_role)
        proposal = state["current_proposal"]
        decision = state["current_decision"]
        reasons: list[str] = []
        if proposal is None:
            reasons.append("representative_proposal_not_current_active_unsuperseded_unretracted")
        if decision is None or decision.get("decision") != "ACCEPT":
            reasons.append("human_decision_not_current_active_unrevoked_accept")
        if reasons:
            return {**state, "eligible": False, "reasons": reasons}
        proposal_payload = _json(proposal["payload_json"])
        decision_payload = _json(decision["payload_json"])
        exact_fields = (
            "cluster_snapshot_id",
            "representative_role",
            "member_ids",
            "candidate_ids",
            "proposed_member_id",
            "policy_id",
            "policy_version",
        )
        if decision["representative_proposal_event_id"] != proposal["event_id"]:
            reasons.append("decision_proposal_event_mismatch")
        if decision["representative_proposal_body_hash"] != proposal["event_body_hash"]:
            reasons.append("decision_proposal_body_hash_mismatch")
        if any(proposal_payload.get(field) != decision_payload.get(field) for field in exact_fields):
            reasons.append("proposal_decision_exact_binding_mismatch")
        if proposal["pinned_checkpoint_id"] != decision["pinned_checkpoint_id"]:
            reasons.append("checkpoint_pin_mismatch")
        if proposal["pinned_projection_hash"] != decision["pinned_projection_hash"]:
            reasons.append("projection_pin_mismatch")
        member = self.connection.execute(
            "SELECT * FROM member_context_snapshot WHERE member_id=?",
            (proposal["proposed_member_id"],),
        ).fetchone()
        if member is None:
            reasons.append("proposed_member_context_absent")
        else:
            context = dict(member)
            if context["generation_input_allowed"] != "TRUE":
                reasons.append("rights_generation_input_not_allowed")
            if context["publication_allowed"] != "TRUE":
                reasons.append("rights_publication_not_allowed")
            if context["availability"] not in {"AVAILABLE", "PRESENT"}:
                reasons.append("member_not_available")
            if context["lifecycle"] not in {"ACTIVE", "CURRENT"}:
                reasons.append("member_lifecycle_not_active")
            rights_refs = _json(proposal["rights_snapshot_refs_json"])
            lifecycle_refs = _json(proposal["lifecycle_snapshot_refs_json"])
            member_id = proposal["proposed_member_id"]
            artifact_context = _json(context["artifact_context_json"])
            if rights_refs.get(member_id) != artifact_context.get("rights_snapshot_ref"):
                reasons.append("rights_snapshot_ref_stale")
            if lifecycle_refs.get(member_id) != artifact_context.get("lifecycle_snapshot_ref"):
                reasons.append("lifecycle_snapshot_ref_stale")
        return {**state, "eligible": not reasons, "reasons": reasons}
