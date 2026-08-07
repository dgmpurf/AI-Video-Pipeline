import sqlite3

from app.ai_video_pipeline.reference_library.duplicate_workflow.identity import logical_content_hash
from app.ai_video_pipeline.reference_library.duplicate_workflow.registry import LOGICAL_REGISTRY
from app.ai_video_pipeline.reference_library.duplicate_workflow.schema import create_schema, insert_rows


def _database(path, mapped, reverse):
    connection = sqlite3.connect(path)
    create_schema(connection)
    rows = {
        entry.table: tuple(reversed(mapped.rows[entry.table])) if reverse else mapped.rows[entry.table]
        for entry in LOGICAL_REGISTRY
    }
    insert_rows(connection, rows)
    connection.commit()
    return connection


def test_logical_hash_is_insertion_order_independent(tmp_path, mapped_model):
    first = _database(tmp_path / "first.sqlite3", mapped_model, False)
    second = _database(tmp_path / "second.sqlite3", mapped_model, True)
    try:
        assert logical_content_hash(first) == logical_content_hash(second)
    finally:
        first.close()
        second.close()


def test_logical_hash_excludes_its_own_column(tmp_path, mapped_model):
    connection = _database(tmp_path / "self.sqlite3", mapped_model, False)
    try:
        before = logical_content_hash(connection)
        connection.execute("UPDATE read_model_meta SET logical_content_hash=?", ("f" * 64,))
        connection.commit()
        assert logical_content_hash(connection) == before
    finally:
        connection.close()
