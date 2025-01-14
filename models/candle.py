import logging
import datetime

from typing import Optional
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from base import Base
from base import session_scope

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
    def get_candles(cls, limit: int):
        with session_scope() as session:
            candles = session.query(cls).order_by(desc(cls.time)).limit(limit).all()
        return candles



class UsdJpy1H(BaseCandle, Base):
    __tablename__ = 'USD_JPY_1H'
