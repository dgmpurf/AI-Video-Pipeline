import pytest

from app.ai_video_pipeline.reference_library.event_ledger.v2.base_bridge import validate_base_binding
from app.ai_video_pipeline.reference_library.event_ledger.v2.errors import BaseBridgeError


def test_bridge_preserves_v0_1_identity(base_snapshot):
    binding = validate_base_binding(base_snapshot.binding.to_dict())
    assert binding == base_snapshot.binding
    assert base_snapshot.base_catalog_identity["record_count"] == 3


def test_bridge_rejects_missing_identity_field(base_snapshot):
    value = base_snapshot.binding.to_dict()
    value.pop("base_v0_1_checkpoint_sha256")
    with pytest.raises(BaseBridgeError):
        validate_base_binding(value)
