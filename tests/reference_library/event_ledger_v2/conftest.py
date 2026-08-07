from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from app.ai_video_pipeline.reference_library.event_ledger.enums import (
    CHECKPOINT_SCHEMA_VERSION as V1_CHECKPOINT,
    EVENT_SCHEMA_VERSION as V1_EVENT,
    LEDGER_SCHEMA_VERSION as V1_LEDGER,
    PROJECTION_SCHEMA_VERSION as V1_PROJECTION,
)
from app.ai_video_pipeline.reference_library.event_ledger.v2.base_bridge import bridge_v0_1_base
from app.ai_video_pipeline.reference_library.event_ledger.v2.canonical import canonical_sha256
from app.ai_video_pipeline.reference_library.event_ledger.v2.checkpoint import build_checkpoint_payload
from app.ai_video_pipeline.reference_library.event_ledger.v2.enums import (
    EVENT_SCHEMA_VERSION,
    AggregateType,
    AuthorityClass,
    EventType,
)
from app.ai_video_pipeline.reference_library.event_ledger.v2.ledger import (
    ZERO_HASH,
    build_entry,
)
from app.ai_video_pipeline.reference_library.event_ledger.v2.manifest import build_manifest
from app.ai_video_pipeline.reference_library.event_ledger.v2.models import LedgerEntry
from app.ai_video_pipeline.reference_library.event_ledger.v2.projection import replay_entries
from app.ai_video_pipeline.reference_library.event_ledger.v2.registry import event_contract
from app.ai_video_pipeline.reference_library.event_ledger.v2.schema import (
    derive_cluster_snapshot_id,
    derive_pair_id,
    derive_representative_proposal_id,
    finalize_event,
)


MEMBERS = ("MEMBER-A", "MEMBER-B", "MEMBER-C")


@pytest.fixture
def base_snapshot():
    catalog = {
        "rl_p0_commit": "d009129f54936a1967bcd471759ee5c8ec9145fb",
        "package_filename": "reference-library.zip",
        "package_bytes": 1234,
        "package_sha256": "1" * 64,
        "record_schema_version": "REFERENCE_LIBRARY_RECORD_V0_1",
        "record_count": 3,
    }
    manifest = {
        "ledger_id": "RL-LEDGER-V1-TEST",
        "ledger_schema_version": V1_LEDGER,
        "event_schema_version": V1_EVENT,
        "projection_schema_version": V1_PROJECTION,
    }
    projection = {
        "projection_schema_version": V1_PROJECTION,
        "ledger_id": manifest["ledger_id"],
        "through_position": 0,
        "through_entry_hash": "0" * 64,
        "records": {},
    }
    projection_hash = canonical_sha256(projection)
    checkpoint = {
        "checkpoint_schema_version": V1_CHECKPOINT,
        "checkpoint_id": "RL-CHK-V1-TEST",
        "prefix_position": 0,
        "prefix_entry_hash": "0" * 64,
        "projection_hash": projection_hash,
        "base_catalog_identity": catalog,
    }
    contexts = {}
    for member in MEMBERS:
        rights = f"RIGHTS-{member}"
        lifecycle = f"LIFECYCLE-{member}"
        contexts[member] = {
            "member_id": member,
            "pilot_clip_id": f"PILOT-{member}",
            "record_id": f"RECORD-{member}",
            "lifecycle": "ACTIVE",
            "availability": "AVAILABLE",
            "rights_provenance": "VERIFIED",
            "generation_input_allowed": True,
            "publication_allowed": "TRUE",
            "rights_snapshot_ref": rights,
            "lifecycle_snapshot_ref": lifecycle,
            "artifact_context": {
                "rights_snapshot_ref": rights,
                "lifecycle_snapshot_ref": lifecycle,
            },
        }
    return bridge_v0_1_base(
        manifest,
        checkpoint,
        projection,
        checkpoint_event_id="RL-EVT-V1-CHECKPOINT",
        member_context=contexts,
    )


@dataclass
class EventScenario:
    base: object
    manifest: dict
    entries: list[LedgerEntry] = field(default_factory=list)
    checkpoints: list[dict] = field(default_factory=list)

    @classmethod
    def create(cls, base):
        return cls(
            base,
            build_manifest(
                base,
                created_by="RL-P3-TEST",
                created_at="2026-08-07T00:00:00Z",
            ),
        )

    def projection(self):
        return replay_entries(
            self.manifest,
            self.base,
            tuple(self.entries),
            accepted_checkpoints=tuple(self.checkpoints),
        )

    def checkpoint(self):
        checkpoint = build_checkpoint_payload(self.projection(), tuple(self.entries))
        self.checkpoints.append(checkpoint)
        return checkpoint

    def add(
        self,
        event_type: str,
        aggregate_id: str,
        target_member_ids: list[str],
        payload: dict,
        *,
        supersedes: list[str] | None = None,
        retracts: list[str] | None = None,
        pinned: bool = False,
    ):
        contract = event_contract(event_type)
        checkpoint = self.checkpoint() if pinned else None
        draft = {
            "event_schema_version": EVENT_SCHEMA_VERSION,
            "event_type": event_type,
            "aggregate_type": contract.aggregate_types[0],
            "aggregate_id": aggregate_id,
            "target_member_ids": sorted(target_member_ids),
            "actor": {
                "actor_id": "TEST-ACTOR",
                "actor_type": "HUMAN" if contract.authority_class == AuthorityClass.HUMAN_DECISION.value else "CODEX",
                "model_name": None,
                "model_version": None,
            },
            "authority_class": contract.authority_class,
            "occurred_at": "2026-08-07T00:00:00Z",
            "recorded_at": "2026-08-07T00:00:00Z",
            "source_trace_ids": ["TRACE-001"],
            "base_v0_1_checkpoint_id": self.base.binding.base_v0_1_checkpoint_id,
            "base_v0_1_projection_hash": self.base.binding.base_v0_1_projection_hash,
            "precondition_v0_2_checkpoint_id": checkpoint["checkpoint_id"] if checkpoint else None,
            "precondition_v0_2_projection_hash": checkpoint["projection_hash"] if checkpoint else None,
            "supersedes_event_ids": sorted(supersedes or []),
            "retracts_event_ids": sorted(retracts or []),
            "payload": payload,
        }
        event = finalize_event(draft)
        entry = LedgerEntry(
            build_entry(
                self.manifest,
                event,
                position=len(self.entries) + 1,
                previous_entry_hash=self.entries[-1].entry_hash if self.entries else ZERO_HASH,
            )
        )
        replay_entries(
            self.manifest,
            self.base,
            (*self.entries, entry),
            accepted_checkpoints=tuple(self.checkpoints),
        )
        self.entries.append(entry)
        return entry

    def evidence(self, left="MEMBER-A", right="MEMBER-B"):
        pair = sorted([left, right])
        return self.add(
            EventType.DUPLICATE_EVIDENCE_ADDED.value,
            derive_pair_id("FULL_FILE_SHA256", pair),
            pair,
            {
                "evidence_id": f"EVIDENCE-{left}-{right}",
                "evidence_domain": "FULL_FILE_SHA256",
                "evidence_kind": "SHA256_EQUALITY",
                "member_ids": pair,
                "observation_state": "OBSERVED",
                "technical_exact_equality": True,
                "measurement_trace_ids": [f"MEASURE-{left}-{right}"],
                "evidence_value": {"equal": True},
                "limitations": [],
            },
        )

    def pair_accept(self, left="MEMBER-A", right="MEMBER-B"):
        evidence = self.evidence(left, right)
        pair = sorted([left, right])
        pair_id = derive_pair_id("FULL_FILE_SHA256", pair)
        proposal = self.add(
            EventType.PAIR_RELATION_PROPOSAL_ADDED.value,
            pair_id,
            pair,
            {
                "pair_relation_proposal_id": f"PAIR-PROPOSAL-{left}-{right}",
                "pair_id": pair_id,
                "evidence_domain": "FULL_FILE_SHA256",
                "member_ids": pair,
                "proposed_relation": "DUPLICATE",
                "evidence_event_ids": [evidence.event.event_id],
                "policy_id": "PAIR-POLICY",
                "policy_version": "1",
                "limitations": [],
            },
        )
        decision = self.add(
            EventType.PAIR_RELATION_DECISION_RECORDED.value,
            pair_id,
            pair,
            {
                "pair_decision_id": f"PAIR-DECISION-{left}-{right}",
                "pair_id": pair_id,
                "evidence_domain": "FULL_FILE_SHA256",
                "member_ids": pair,
                "proposal_event_ids": [proposal.event.event_id],
                "decision": "ACCEPT",
                "reason": "synthetic acceptance",
                "authorization_trace_ids": ["AUTH-PAIR"],
            },
        )
        return decision

    def cluster(self, members=MEMBERS):
        checkpoint = build_checkpoint_payload(self.projection(), tuple(self.entries))
        snapshot = derive_cluster_snapshot_id(
            "FULL_FILE_SHA256",
            members,
            checkpoint["checkpoint_id"],
            checkpoint["projection_hash"],
        )
        payload = {
            "cluster_proposal_id": "CLUSTER-PROPOSAL-001",
            "cluster_snapshot_id": snapshot,
            "cluster_kind": "FULL_FILE_SHA256",
            "member_ids": sorted(members),
            "supporting_pair_decision_event_ids": [],
            "policy_id": "CLUSTER-POLICY",
            "policy_version": "1",
            "limitations": [],
        }
        entry = self.add(
            EventType.CLUSTER_PROPOSAL_ADDED.value,
            snapshot,
            list(members),
            payload,
            pinned=True,
        )
        return snapshot, entry

    def representative(self, snapshot, proposed="MEMBER-A"):
        checkpoint = build_checkpoint_payload(self.projection(), tuple(self.entries))
        candidates = list(MEMBERS)
        ranking = {"method": "SYNTHETIC_EXPLICIT_ORDER"}
        proposal_id = derive_representative_proposal_id(
            cluster_snapshot_id=snapshot,
            representative_role="GENERATION_INPUT",
            member_ids=MEMBERS,
            candidate_ids=candidates,
            policy_id="REP-POLICY",
            policy_version="1",
            ranking_facts=ranking,
            pinned_checkpoint_id=checkpoint["checkpoint_id"],
            pinned_projection_hash=checkpoint["projection_hash"],
        )
        refs_rights = {member: f"RIGHTS-{member}" for member in candidates}
        refs_lifecycle = {member: f"LIFECYCLE-{member}" for member in candidates}
        payload = {
            "representative_proposal_id": proposal_id,
            "cluster_snapshot_id": snapshot,
            "representative_role": "GENERATION_INPUT",
            "member_ids": list(MEMBERS),
            "candidate_ids": candidates,
            "proposed_member_id": proposed,
            "policy_id": "REP-POLICY",
            "policy_version": "1",
            "ranking_facts": ranking,
            "rights_snapshot_refs": refs_rights,
            "lifecycle_snapshot_refs": refs_lifecycle,
            "limitations": [],
        }
        entry = self.add(
            EventType.REPRESENTATIVE_PROPOSAL_ADDED.value,
            f"{snapshot}::GENERATION_INPUT",
            list(MEMBERS),
            payload,
            pinned=True,
        )
        return entry, checkpoint


@pytest.fixture
def scenario(base_snapshot):
    return EventScenario.create(base_snapshot)
