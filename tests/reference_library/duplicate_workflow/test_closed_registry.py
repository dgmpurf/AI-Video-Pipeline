import sqlite3

import pytest

from app.ai_video_pipeline.reference_library.duplicate_workflow.errors import SchemaError
from app.ai_video_pipeline.reference_library.duplicate_workflow.identity import validate_registry_schema
from app.ai_video_pipeline.reference_library.duplicate_workflow.registry import (
    LOGICAL_REGISTRY,
    LOGICAL_TABLE_NAMES,
)
from app.ai_video_pipeline.reference_library.duplicate_workflow.schema import create_schema


def test_closed_registry_has_exact_fifteen_tables_and_no_fts():
    assert len(LOGICAL_REGISTRY) == 15
    assert len(LOGICAL_TABLE_NAMES) == 15
    assert all("fts" not in table.lower() for table in LOGICAL_TABLE_NAMES)


def test_extra_or_missing_physical_table_is_rejected(tmp_path):
    path = tmp_path / "registry.sqlite3"
    with sqlite3.connect(path) as connection:
        create_schema(connection)
        validate_registry_schema(connection)
        connection.execute("CREATE TABLE unexpected(value TEXT)")
        with pytest.raises(SchemaError):
            validate_registry_schema(connection)
