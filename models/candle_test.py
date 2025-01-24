import pytest
from datetime import datetime
from sqlalchemy import text
from candle import UsdJpy1H, BaseCandle, generate_candle
from base import engine, session_scope, Base

@pytest.fixture(scope='module')
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_create_candle(setup_database):
    time = datetime(2020, 1, 1, 0, 0)
    assert UsdJpy1H.create(time, 100.0, 110, 90, 105) is True

def test_get_candle(setup_database):
    time = datetime(2020, 1, 1, 0, 0)
    candle = UsdJpy1H.get(time)
    assert candle is not None
    assert candle.time == time
    assert candle.open == 100.0
    assert candle.high == 110.0
    assert candle.low == 90.0
    assert candle.close == 105

def test_delete_candle(setup_database):
    time = datetime(2020, 1, 1, 0, 0)
    UsdJpy1H.delete(time)
    candle = UsdJpy1H.get(time)
    assert candle is None

def test_update_candle(setup_database):
    time = datetime(2020, 1, 1, 0, 0)
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

def test_get_candles_by_limit(setup_database):
    with session_scope() as session:
        session.query(UsdJpy1H).delete()

    candle = UsdJpy1H.create(datetime(2000, 1, 1, 0, 0), 100, 100, 100, 100)
    candle = UsdJpy1H.create(datetime(2001, 1, 1, 0, 0), 200, 100, 100, 100)
    candle = UsdJpy1H.create(datetime(2002, 1, 1, 0, 0), 300, 100, 100, 100)

    candles = UsdJpy1H.get_candles_by_limit(100)
    assert len(candles) == 3
    assert candles[-1].open == 100

def test_get_candles_between(setup_database):
    with session_scope() as session:
        session.query(UsdJpy1H).delete()


    candle = UsdJpy1H.create(datetime(2000, 1, 1, 0, 0), 100, 100, 100, 100)
    candle = UsdJpy1H.create(datetime(2001, 1, 1, 0, 0), 200, 100, 100, 100)
    candle = UsdJpy1H.create(datetime(2002, 1, 1, 0, 0), 300, 100, 100, 100)
    candle = UsdJpy1H.create(datetime(2003, 1, 1, 0, 0), 300, 100, 100, 100)
    candle = UsdJpy1H.create(datetime(2004, 1, 1, 0, 0), 300, 100, 100, 100)

    candles = UsdJpy1H.get_candles_between(datetime(2002, 1,1,0, 0),
                                           datetime(2003, 12, 31, 0, 0))
    assert len(candles) == 2
    assert candles[-1].open == 300


def test_values(setup_database):
    time = datetime(2000, 1, 1, 0, 0)
    UsdJpy1H.create(time, 100, 200, 300, 400)
    candle = UsdJpy1H.get(time)

    assert candle.values['time'] == '2000-01-01 00:00'


def test_factory_base_candle(setup_database):
    ...

def test_generate_candle(setup_database):
    ticker = ...
    currency = 'USD_JPY'
    duration = '1H'

    assert generate_candle(ticker, currency, duration) == True
