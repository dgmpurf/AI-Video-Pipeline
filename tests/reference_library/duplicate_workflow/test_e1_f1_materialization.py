from app.ai_video_pipeline.reference_library.duplicate_workflow.builder import build_generation
from app.ai_video_pipeline.reference_library.duplicate_workflow.models import RuntimeStateProtectionPolicy
from app.ai_video_pipeline.reference_library.duplicate_workflow.query import DuplicateWorkflowReadModel
from app.ai_video_pipeline.reference_library.event_ledger.v2.schema import derive_pair_id


def _build(tmp_path, mapped):
    policy = RuntimeStateProtectionPolicy(
        tmp_path / "repo", tmp_path / "source", (tmp_path / "media",)
    )
    return build_generation(tmp_path / "state", mapped, protection_policy=policy)


def test_e1_pair_query_never_infers_from_cluster(tmp_path, mapped_model):
    build = _build(tmp_path, mapped_model)
    missing_pair = derive_pair_id("FULL_FILE_SHA256", ["MEMBER-A", "MEMBER-C"])
    with DuplicateWorkflowReadModel.open_generation(build.generation_path) as model:
        result = model.pair_state(missing_pair)
    assert result["history"] == []
    assert result["current_decision"] is None
    assert result["cluster_inference_used"] is False


def test_f1_query_recomputes_current_exact_eligibility(tmp_path, mapped_model, scenario_bundle):
    build = _build(tmp_path, mapped_model)
    snapshot = scenario_bundle[1]
    with DuplicateWorkflowReadModel.open_generation(build.generation_path) as model:
        result = model.execution_eligibility(snapshot, "GENERATION_INPUT")
    assert result["eligible"] is True
    assert result["reasons"] == []
