import pytest
import logging
from datetime import datetime
from api.gmo.apiclient import Ticker

def test_mid_price():
    time = datetime(2000, 1, 1)
    bid = 100.0
    ask = 120.0
    ticker = Ticker(time, bid, ask)
    assert ticker.mid_price == 110.0

def test_truncate_date_time_5m():
    ticker_time = datetime(2000, 1, 1, 12, 14, 45)
    ticker = Ticker(ticker_time, 100, 101)
    ticker.time = ticker.truncate_date_time("5m")
    assert ticker.time.hour == 12
    assert ticker.time.minute == 10

def test_truncate_date_time_30m():
    ticker_time = datetime(2000, 1, 1, 12, 33, 45)
    ticker = Ticker(ticker_time, 100, 101)
    ticker.time = ticker.truncate_date_time("30m")
    assert ticker.time.hour == 12
    assert ticker.time.minute == 30

def test_truncate_date_time_1h():
    ticker_time = datetime(2000, 1, 1, 12, 30, 45)
    ticker = Ticker(ticker_time, 100, 101)
    ticker.time = ticker.truncate_date_time("1h")
    assert ticker.time.hour == 12
    assert ticker.time.minute == 0

def test_truncate_date_time_4h():
    ticker_time = datetime(2000, 1, 1, 11, 30, 45)
    ticker = Ticker(ticker_time, 100, 101)
    ticker.time = ticker.truncate_date_time("4h")
    assert ticker.time.hour == 8
    assert ticker.time.minute == 0

def test_truncate_date_time_24h():
    ticker_time = datetime(2000, 1, 1, 11, 30, 45)
    ticker = Ticker(ticker_time, 100, 101)
    ticker.time = ticker.truncate_date_time("24h")
    assert ticker.time.day == 1
    assert ticker.time.hour == 0
    assert ticker.time.minute == 0

def test_truncate_date_time_unknown():
    ticker_time = datetime(2000, 1, 1, 11, 30, 45)
    ticker = Ticker(ticker_time, 100, 101)
    assert ticker.truncate_date_time("1000H") is None

def test_truncate_date_time_unknown_log(caplog):
    ticker_time = datetime(2000, 1, 1, 11, 30, 45)
    ticker = Ticker(ticker_time, 100, 101)
    with caplog.at_level(logging.WARNING):
        ticker.truncate_date_time("1000H")
        assert "Unknown time duration: 1000H" in caplog.text


