from datetime import datetime
from typing import Optional

import logging
import math

logger = logging.getLogger(__name__)


class Ticker(object):
    def __init__(self, time: datetime, bid: float, ask: float ):
        self.time = time
        self.bid = bid
        self.ask = ask

    @property
    def mid_price(self):
        return (self.bid + self.ask) / 2

    @property
    def values(self):
        return {
            'time': self.time,
            'bid': self.bid,
            'ask': self.ask
        }

    def truncate_date_time(self, duration) -> Optional[datetime]:
        ticker_time = self.time
        if duration == "5m":
            new_minute = math.floor(ticker_time.minute / 5) * 5
            ticker_time = datetime(self.time.year,
                                   self.time.month,
                                   self.time.day,
                                   self.time.hour,
                                   new_minute)
            time_format = '%Y-%m-%d %H:%M'
        if duration == "30m":
            new_minute = math.floor(ticker_time.minute / 30) * 30
            ticker_time = datetime(self.time.year,
                                   self.time.month,
                                   self.time.day,
                                   self.time.hour,
                                   new_minute)
            time_format = '%Y-%m-%d %H:%M'
        elif duration == "1h":
            time_format = '%Y-%m-%d %H'
        elif duration == "4h":
            new_hour = math.floor(ticker_time.hour / 4) * 4
            ticker_time = datetime(self.time.year,
                                   self.time.month,
                                   self.time.day,
                                   new_hour)
            time_format = '%Y-%m-%d %H'
        elif duration == "24h":
            time_format = '%Y-%m-%d'
        else:
            logger.warning(f'Unknown time duration: {duration}')
            return

        str_date = datetime.strftime(ticker_time, time_format)
        return datetime.strptime(str_date, time_format)



