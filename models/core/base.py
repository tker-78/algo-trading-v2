import logging
import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import DeclarativeBase
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class Base(DeclarativeBase): pass


engine = create_engine(f'postgresql+psycopg2://takuyakinoshita:'
                       f'@localhost:5432/algo2_backtest', pool_pre_ping=True)

Session = scoped_session(sessionmaker(bind=engine))
lock = threading.Lock()

@contextmanager
def session_scope():
    """
    データベース接続のセッション
    """
    session = Session()
    session.expire_on_commit = False
    try:
        lock.acquire()
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        lock.release()

def init_db():
    Base.metadata.create_all(bind=engine)

