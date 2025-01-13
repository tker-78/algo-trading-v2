import pytest
from sqlalchemy import text
from base import engine, session_scope

def test_engine_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1