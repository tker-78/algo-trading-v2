
from models.core import pair


def test_str():
    assert str(pair.Pair("USD", "JPY")) == "USD/JPY"

def test_eq():
    assert pair.Pair("USD", "JPY") == pair.Pair("USD", "JPY")
    assert pair.Pair("USD", "JPY") != pair.Pair("GBP", "JPY")
