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
        self.destination: Station = kwargs.get('destination')
        self.departure: datetime.datetime = kwargs.get('departure')
        self.arrival: datetime.datetime = kwargs.get('arrival')

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
