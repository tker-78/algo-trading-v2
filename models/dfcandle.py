from datetime import datetime

from .candle import factory_base_candle
import settings

class DataframeCandle(object):
    def __init__(self):
        self.duration = settings.tradeDuration
        self.candle_cls = factory_base_candle(settings.tradeCurrency, settings.tradeDuration)
        self.candles = []

    def set_candles_between(self, start: datetime, end: datetime):
        candles = self.candle_cls.get_candles_between(start, end)
        self.candles = candles

    def set_candles_by_limit(self, limit: int = 100):
        candles = self.candle_cls.get_candles_by_limit(limit)
        self.candles = candles