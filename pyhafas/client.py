from __future__ import annotations

import datetime
from typing import List

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

    def departures(
            self,
            station,
            date: datetime.datetime,
            max_journeys: int = -1):
        if not isinstance(station, Station):
            station = Station(station)

        body = self.profile.format_station_board_request(
            station,
            StationBoardRequestType.DEPARTURE,
            date,
            max_journeys
        )
        res = self.profile.request(body)

        return self.profile.parse_station_board_request(res.text)

    def arrivals(
            self,
            station,
            date: datetime.datetime,
            max_journeys: int = -1):
        if not isinstance(station, Station):
            station = Station(station)

        body = self.profile.format_station_board_request(
            station,
            StationBoardRequestType.ARRIVAL,
            date,
            max_journeys
        )
        res = self.profile.request(body)

        return self.profile.parse_station_board_request(res.text)

    def journeys(
            self,
            origin,
            destination,
            date: datetime.datetime,
            via: List = [],
            min_change_time: int = 0,
            max_changes: int = -1,
            products: Dict[str, bool] = {}
    ) -> List[Journey]:
        if not isinstance(origin, Station):
            origin = Station(origin)
        if not isinstance(destination, Station):
            destination = Station(destination)
        for via_station in via:
            if not isinstance(via_station, Station):
                via[via.index(via_station)] = Station(via_station)

        body = self.profile.format_journeys_request(
            origin,
            destination,
            via,
            date,
            min_change_time,
            max_changes,
            products
        )
        res = self.profile.request(body)

        return self.profile.parse_journeys_request(res.text)

    def journey(self, journey) -> Journey:
        if not isinstance(journey, Station):
            journey = Journey(journey)

        body = self.profile.format_journey_request(journey)
        res = self.profile.request(body)

        return self.profile.parse_journey_request(res.text)

    def locations(self, term: str) -> List[Station]:
        body = self.profile.format_location_request(term)
        res = self.profile.request(body)

        return self.profile.parse_location_request(res.text)

    def stop(self, stop):
        pass

    def nearby(self, location):
        pass

    def trip(self, id, name):
        pass

    def radar(self, north, west, south, east):
        pass
