
from datetime import datetime, timezone, timedelta
from dateutil import tz

class NaiveError(Exception):
    def __init__(self, message="datatime should not be naive"):
        self.message = message

    def __str__(self):
        return self.message

def is_naive(dt: datetime) -> bool:
    """datetimeがナイーブか確認
    naiveとは、timezoneを持たないdatetimeオブジェクト
    utcoffset()はNoneをかえす
    """
    return dt.tzinfo is None or dt.utcoffset() is None


def utc_now() -> datetime:
    """utcのdatetimeを取得
    """
    return datetime.now().replace(tzinfo=timezone.utc)

def local_datetime(*args, **kwargs) -> datetime:
    """localのtimezoneを持つdatetimeを取得
    """
    return datetime(*args, **kwargs).replace(tzinfo=tz.tzlocal())

def utc_to_local(dt: datetime) -> datetime:
    """utcに対して時差の補正をして、timezoneを変更して、datetimeを返す
    """
    if is_naive(dt):
        raise NaiveError()
    return dt.astimezone(tz.tzlocal())








