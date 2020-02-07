from __future__ import annotations

from typing import List

from .journey import Journey
from .profile import DBProfile, Profile, StationBoardRequestType
from .station import Station


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

        return res.text  # TODO: Add parser function

    def arrivals(self, station: Station or str):
        pass

    def journeys(
            self,
            origin: Station or str,
            destination: Station or str) -> List[Journey]:
        pass

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
