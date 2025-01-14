import pytest
import datetime
from sqlalchemy import text
from candle import UsdJpy1H, BaseCandle
from base import engine, session_scope, Base

@pytest.fixture(scope='module')
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_create_candle(setup_database):
    time = datetime.datetime(2020, 1, 1, 0, 0)
    assert UsdJpy1H.create(time, 100.0, 110, 90, 105) is True

def test_get_candle(setup_database):
    time = datetime.datetime(2020, 1, 1, 0, 0)
    candle = UsdJpy1H.get(time)
    assert candle is not None
    assert candle.time == time
    assert candle.open == 100.0
    assert candle.high == 110.0
    assert candle.low == 90.0
    assert candle.close == 105

def test_delete_candle(setup_database):
    time = datetime.datetime(2020, 1, 1, 0, 0)
    UsdJpy1H.delete(time)
    candle = UsdJpy1H.get(time)
    assert candle is None

def test_update_candle(setup_database):
    time = datetime.datetime(2020, 1, 1, 0, 0)
    candle = UsdJpy1H.create(time, 100, 100, 100, 100)
    candle = UsdJpy1H.get(time)
    candle.high = 200
    candle.low = 0
    candle.open = 100
    candle.close = 50
    candle.update()
    assert candle.high == 200
    assert candle.low == 0
    assert candle.open == 100
    assert candle.close == 50

