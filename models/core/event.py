
from typing import List, Optional
import abc
from datetime import datetime

from . import dt

class Producer(object):
    """
    producersのためのベースクラス。
    初期化処理には非同期処理を用いる。
    これは、...
    """

    async def initialize(self):
        """override"""
        pass

    async def main(self):
        """override"""
        pass

    async def finalize(self):
        """override"""
        pass



class Event(object):
    """
    eventsのためのベースクラス。
    """
    def __init__(self, when: datetime):
        assert not dt.is_naive(when), f'{when} should have timezone information set'

        self.when: datetime = when




class EventSource(metaclass=abc.ABCMeta):
    def __init__(self, producer: Optional[Producer] = None):
        self.producer = producer

    @abc.abstractmethod
    def pop(self) -> Optional[Event]:
        raise NotImplementedError()



class FifoQueueEventSource(EventSource):
    def __init__(self, producer: Optional[Producer] = None, events: List[Event] = []):
        super().__init__(producer)
        self._queue: List[Event] = []
        self._queue.extend(events)

    def push(self, event: Event):
        self._queue.append(event)

    def pop(self) -> Optional[Event]:
        ret = None
        if self._queue:
            ret = self._queue.pop(0)
        return ret


