
from models.core import enums

def test_str():
    assert str(enums.OrderOperation(100)) == "buy"
    assert str(enums.OrderOperation(101)) == "sell"