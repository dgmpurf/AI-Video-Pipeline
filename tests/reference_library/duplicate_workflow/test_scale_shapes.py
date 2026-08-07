import pytest

from app.ai_video_pipeline.reference_library.duplicate_workflow.errors import MappingError
from app.ai_video_pipeline.reference_library.duplicate_workflow.mapper import plan_scale_shape


@pytest.mark.parametrize("record_count", [30, 5000, 100000])
def test_scale_shape_uses_bounded_explicit_edges_only(record_count):
    first = plan_scale_shape(record_count, [("B", "A"), ("A", "B"), ("C", "D")])
    second = plan_scale_shape(record_count, [("D", "C"), ("B", "A")])
    assert first == second
    assert first["candidate_edge_count"] == 2
    assert first["all_pairs_enumerated"] is False
    assert sum(item["end"] - item["start"] for item in first["partitions"]) == record_count


def test_scale_shape_rejects_self_edges():
    with pytest.raises(MappingError):
        plan_scale_shape(30, [("A", "A")])
