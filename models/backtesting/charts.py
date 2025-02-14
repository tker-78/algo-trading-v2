
import abc
import logging

logger = logging.getLogger(__name__)


class LineChart(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_title(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_traces(self, figure: ..., row: int) :
        raise NotImplementedError()


class LineCharts(object):
    """
    デフォルトでは2つのタイプのチャートを表示する
    1. candle chart(buy, sellのシグナル表示を含む
    2. balance chart(口座残高の推移)
    """
    def __init__(self, exchange: ...):
        self.exchange = exchange
        ...

    def add_balance(self, symbol: str):
        ...

    def add_portfolio_value(self, symbol: str, precision: int = 2):
        ...

    def add_pair(self, pair: ..., include_buys: bool = True, include_sells: bool = True):
        ...

    def add_pair_indicator(self, name: str, pair: ..., get_data_point: ...):
        ...

    def show(self, show_legend: bool = True):
        ...
