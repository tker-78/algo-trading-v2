import enum

class OrderOperation(enum.Enum):
    BUY = 100
    SELL = 101

    def __str__(self):
        return {
            OrderOperation.BUY: "buy",
            OrderOperation.SELL: "sell"
        }[self]

