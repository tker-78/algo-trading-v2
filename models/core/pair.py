
from dataclasses import dataclass

@dataclass(frozen=True)
class Pair(object):
    base_symbol: str
    quote_symbol: str

    def __str__(self):
        return f'{self.base_symbol}/{self.quote_symbol}'

@dataclass(frozen=True)
class PairInfo(object):
    base_precision: int
    quote_precision: int
