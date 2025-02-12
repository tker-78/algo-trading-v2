import logging
from datetime import datetime

from typing import Optional
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError

from .base import Base
from .base import session_scope

logger = logging.getLogger(__name__)


class BaseCandle(object):
    time = Column(DateTime, primary_key=True, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)

    @classmethod
    def create(cls, time, open, high, low, close) -> bool:
        candle = cls(time=time, open=open, high=high, low=low, close=close)
        try:
            with session_scope() as session:
                session.add(candle)
                return True
        except IntegrityError:
            return False

    def update(self):
        with session_scope() as session:
            session.add(self)

    @classmethod
    def get(cls, time: datetime) -> Optional['BaseCandle']:
        """
        一つのcandleをデータベースから取得
        """
        with session_scope() as session:
            candle = session.query(cls).filter(cls.time == time).first()
        if candle is None:
            return None
        return candle

    @classmethod
    def delete(cls, time: datetime):
        with session_scope() as session:
            candle = session.query(cls).filter(cls.time == time).first()
            if candle:
                session.delete(candle)

    @classmethod
    def get_candles_by_limit(cls, limit: int):
        with session_scope() as session:
            candles = session.query(cls).order_by(desc(cls.time)).limit(limit).all()
        return candles

    @classmethod
    def get_candles_between(cls, start: datetime, end: datetime):
        with session_scope() as session:
            candles = session.query(cls).filter(cls.time.between(start, end)).all()
        return candles

    @property
    def values(self):
        return {
            'time': datetime.strftime(self.time, '%Y-%m-%d %H:%M'),
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close
        }

class UsdJpy1H(BaseCandle, Base):
    __tablename__ = 'USD_JPY_1H'

class UsdJpy4H(BaseCandle, Base):
    __tablename__ = 'USD_JPY_4H'

class UsdJpy24H(BaseCandle, Base):
    __tablename__ = 'USD_JPY_24H'


def factory_base_candle(currency, duration):
    if currency == 'USD_JPY' and duration == '1h':
        return UsdJpy1H
    elif currency == 'USD_JPY' and duration == '4H':
        return UsdJpy4H
    elif currency == 'USD_JPY' and duration == '24H':
        return UsdJpy24H
    else:
        return None


def generate_candle(ticker: ..., currency: str, duration: str) -> bool:
    """
    candleを作成したらTrueを返す
    **todo**
    factory_base_candleを使って、動的にローソク足データを作成する
    Ticker実装後に実装する
    """
    cls = factory_base_candle(currency, duration)

    # durationに基づいてtickerのtimeを切り上げする
    ticker_time = ticker.truncate_date_time(duration)

    # 対象のレコードを取り出す
    candle = cls.get(ticker_time)

    # tickerのask, bidの中間をpriceとして取り出す
    price = ticker.mid_price

    if candle is None:
        cls.create(ticker_time, price, price, price, price)
        return True

    if candle.high < price:
        candle.high = price
    elif candle.low > price:
        candle.low = price
    candle.close = price

    candle.update()
    return False




