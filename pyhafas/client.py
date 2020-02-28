from __future__ import annotations
from typing import Awaitable, Dict, List, Optional, Tuple, Union, Any, TYPE_CHECKING

from .fptf import Journey, Station
from .profile import DBProfile, Profile, StationBoardRequestType

class HafasClient:
    def __init__(
            self,
            profile: Profile = DBProfile(),
            ua: str = "pyhafas",
            debug: bool = False):

        self.profile = profile
        self.useragent = ua
        self.debug = debug

    def departures(self, station: Station or str):
        if isinstance(station, str):
            station = Station(station)

        body = self.profile.formatStationBoardRequest(
            station, StationBoardRequestType.DEPARTURE)
        res = self.profile.request(body)

        return self.profile.parseStationBoardRequest(res.text)

    def arrivals(self, station: Station or str):
        if isinstance(station, str):
            station = Station(station)

        body = self.profile.formatStationBoardRequest(
            station, StationBoardRequestType.ARRIVAL)
        res = self.profile.request(body)

        return self.profile.parseStationBoardRequest(res.text)

    def journeys(
            self,
            origin: Station or str,
            destination: Station or str) -> List[Journey]:
        if isinstance(origin, str):
            origin = Station(origin)
        if isinstance(destination, str):
            destination = Station(destination)

        body = self.profile.formatJourneysRequest(origin, destination)
        res = self.profile.request(body)

        return self.profile.parseJourneysRequest(res.text)

    def journey(self, journey: Journey or str) -> Journey:
        if isinstance(journey, str):
            journey = Journey(journey)

        body = self.profile.formatJourneyRequest(journey)
        res = self.profile.request(body)

        return self.profile.parseJourneyRequest(res.text)

    def locations(self, term):
        pass

    def stop(self, stop):
        pass

    def nearby(self, location):
        pass

    def trip(self, id, name):
        pass

    def radar(self, north, west, south, east):
        pass
