from datetime import datetime, timezone, timedelta
from dateutil import tz
import pytest

from models.core import dt


def test_is_naive():
    naive_dt = datetime.now()
    non_naive_dt = datetime.now().replace(tzinfo=tz.tzlocal())
    assert dt.is_naive(naive_dt) == True
    assert dt.is_naive(non_naive_dt) == False


def test_utc_now():
    output = dt.utc_now()
    assert output.tzinfo == timezone.utc

def test_local_datetime():
    now = (2001, 1, 2, 23, 59, 59)
    assert dt.local_datetime(*now).tzinfo == tz.tzlocal()

def test_utc_to_local():
    # utcのdatetimeを生成
    utc_dt = datetime.now(tz.tzutc())

    # naiveなdatetimeを生成
    naive_dt = datetime.now()


    assert utc_dt - dt.utc_to_local(utc_dt) == timedelta(0)

    with pytest.raises(dt.NaiveError):
        dt.utc_to_local(naive_dt)

