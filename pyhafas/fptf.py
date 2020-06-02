import datetime
from typing import List


class Station:
    def __init__(self, id: str or int, **kwargs):
        self.id = id
        self.name: str = kwargs.get('name')
        self.latitude: float = kwargs.get('latitude')
        self.longitude: float = kwargs.get('longitude')

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Journey:
    def __init__(self, id: str or int, **kwargs):
        self.id = id
        self.date: datetime.date = kwargs.get('date')
        self.duration: datetime.timedelta = kwargs.get('duration')
        self.legs: List[Leg] = kwargs.get('legs')

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Leg:
    def __init__(self, **kwargs):
        self.origin: Station = kwargs.get('origin')
        self.mode: str = kwargs.get('mode', 'train')
        self.cancelled: bool = kwargs.get('cancelled', False)
        self.destination: Station = kwargs.get('destination')
        self.departure: datetime.datetime = kwargs.get('departure')
        self.departure_delay: datetime.timedelta = kwargs.get('departure_delay', None)
        self.departure_platform: str = kwargs.get('departure_platform', None)
        self.arrival: datetime.datetime = kwargs.get('arrival')
        self.arrival_delay: datetime.timedelta = kwargs.get('arrival_delay', None)
        self.arrival_platform: str = kwargs.get('arrival_platform', None)
        self.stopovers: List[Stopover] = kwargs.get('stopovers', None)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Stopover:
    def __init__(self, **kwargs):
        self.stop: Station = kwargs.get('stop')
        self.cancelled: bool = kwargs.get('cancelled', False)
        self.arrival: datetime.datetime = kwargs.get('arrival', None)
        self.arrival_delay: datetime.timedelta = kwargs.get('arrival_delay', None)
        self.arrival_platform: str = kwargs.get('arrival_platform', None)
        self.departure: datetime.datetime = kwargs.get('departure', None)
        self.departure_delay: datetime.timedelta = kwargs.get('departure_delay', None)
        self.departure_platform: str = kwargs.get('departure_platform', None)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
