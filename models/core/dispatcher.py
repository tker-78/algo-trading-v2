
from typing import cast, Any, Awaitable, Callable, Dict, Generator, List, Optional, Set, Tuple
import abc
import asyncio
import contextlib
import dataclasses
import datetime
import heapq
import logging
import platform
import signal

from . import dt, event, helpers

logger = logging.getLogger(__name__)
EventHandler = Callable[[event.Event], Awaitable[Any]]
IdleHandler = Callable[[], Awaitable[Any]]
SchedulerJob = Callable[[], Awaitable[Any]]

@dataclasses.dataclass
class EventDispatch:
    event: event.Event
    handlers: List[EventHandler]

@dataclasses.dataclass(order=True)
class ScheduleJob:
    when: datetime.datetime
    job: SchedulerJob = dataclasses.field(compare=False)



