import datetime
from typing import Dict, List, Optional, Union

from pyhafas.profile import ProfileInterface
from pyhafas.types.fptf import Journey, Leg, Station, StationBoardLeg
from pyhafas.types.station_board_request import StationBoardRequestType


class HafasClient:
    """
    The interface between the user's program and pyHaFAS internal code.

    :param profile: `Profile` to be used
    :param ua: (optional, not recommended to change) The user-agent which will be sent to HaFAS. By default "pyhafas", but is often overwritten by profile to emulate the app.
    :param debug: (optional) Whether debug mode should be enabled. Defaults to False.
    """

    def __init__(
            self,
            profile: ProfileInterface,
            ua: str = "pyhafas",
            debug: bool = False):
        self.profile = profile
        self.useragent = ua
        self.debug = debug

    def departures(
            self,
            station: Union[Station, str],
            date: datetime.datetime,
            max_trips: int = -1,
            duration: int = -1,
            products: Dict[str, bool] = {},
            direction: Optional[Union[Station, str]] = None) -> List[StationBoardLeg]:
        """
        Returns departing trips at the specified station

        To get detailed information on the trip use the `trip` method with the id

        :param station: FPTF `Station` object or ID of station
        :param date: Date and Time when to search
        :param max_trips: (optional) Maximum number of trips to be returned. Default is "whatever HaFAS wants"
        :param duration: (optional) Minutes after `date` in which is search is made. Default is "whatever HaFAS wants"
        :param products: (optional) Dict of product name(s) and whether it should be enabled or not. Modifies the default products specified in the profile.
        :param direction: (optional) Direction (end) station of the vehicle. Default is any direction station is allowed
        :return: List of FPTF `StationBoardLeg` objects with departing trips
        """
        if not isinstance(station, Station):
            station = Station(id=station)

        if not isinstance(direction, Station) and direction is not None:
            direction = Station(id=direction)

        date = self.profile.transform_datetime_parameter_timezone(date)

        body = self.profile.format_station_board_request(
            station,
            StationBoardRequestType.DEPARTURE,
            date,
            max_trips,
            duration,
            products,
            direction
        )
        res = self.profile.request(body)

        return self.profile.parse_station_board_request(res, "d")

    def arrivals(
            self,
            station: Union[Station, str],
            date: datetime.datetime,
            max_trips: int = -1,
            duration: int = -1,
            products: Dict[str, bool] = {},
            direction: Optional[Union[Station, str]] = None) -> List[StationBoardLeg]:
        """
        Returns arriving trips at the specified station

        To get detailed information on the trip use the `trip` method with the id

        :param station: FPTF `Station` object or ID of station
        :param date: Date and Time when to search
        :param max_trips: (optional) Maximum number of trips to be returned. Default is "whatever HaFAS wants"
        :param duration: (optional) Minutes after `date` in which is search is made. Default is "whatever HaFAS wants"
        :param products: (optional) Dict of product name(s) and whether it should be enabled or not. Modifies the default products specified in the profile.
        :param direction: (optional) Direction (end) station of the vehicle. Default is any direction station is allowed
        :return: List of FPTF `StationBoardLeg` objects with arriving trips
        """
        if not isinstance(station, Station):
            station = Station(id=station)

        if not isinstance(direction, Station) and direction is not None:
            direction = Station(id=direction)

        date = self.profile.transform_datetime_parameter_timezone(date)

        body = self.profile.format_station_board_request(
            station,
            StationBoardRequestType.ARRIVAL,
            date,
            max_trips,
            duration,
            products,
            direction
        )
        res = self.profile.request(body)

        return self.profile.parse_station_board_request(res, "a")

    def journeys(
            self,
            origin: Union[Station, str],
            destination: Union[Station, str],
            date: datetime.datetime,
            via: List[Union[Station, str]] = [],
            min_change_time: int = 0,
            max_changes: int = -1,
            products: Dict[str, bool] = {},
            max_journeys: int = -1
    ) -> List[Journey]:
        """
        Returns possible journeys between two destinations

        Possible journeys between two destinations are calculated by HaFAS and returned. It's also possible to add multiple via stations.

        :param origin: FPTF `Station` object or ID of origin/starting station
        :param destination: FPTF `Station` object or ID of destination/ending station
        :param date: Date and Time when to search
        :param via: (optional) List of via stations. The route is calculated via all of these stations in the order of the list. The stations have to be a FPTF `Station` object or the ID of the station. The default is no via stations.
        :param min_change_time: (optional) Minimum transfer/change time at each station. Default is the default that HaFAS specifies internal.
        :param max_changes: (optional) Maximum number of changes. Default is unlimited.
        :param products: (optional) Dict of product name(s) and whether it should be enabled or not. Modifies the default products specified in the profile.
        :param max_journeys: (optional) Maximum number of returned journeys. Default is the default that HaFAS specifies internal.
        :return: List of FPTF `Journey` objects
        """
        if not isinstance(origin, Station):
            origin = Station(origin)
        if not isinstance(destination, Station):
            destination = Station(destination)
        for via_station in via:
            if not isinstance(via_station, Station):
                via[via.index(via_station)] = Station(via_station)

        date = self.profile.transform_datetime_parameter_timezone(date)

        body = self.profile.format_journeys_request(
            origin,
            destination,
            via,
            date,
            min_change_time,
            max_changes,
            products,
            max_journeys
        )
        res = self.profile.request(body)

        return self.profile.parse_journeys_request(res)

    def journeys_from_leg(
            self,
            origin: Leg,
            destination: Union[Station, str],
            via: List[Union[Station, str]] = [],
            min_change_time: int = 0,
            max_changes: int = -1,
            products: Dict[str, bool] = {},
    ) -> List[Journey]:
        """
        Returns possible journeys from a leg to a destination

        Possible journeys between two destinations are calculated by HaFAS and returned. It's also possible to add multiple via stations.

        :param origin: FPTF `Leg` object from where to search
        :param destination: FPTF `Station` object or ID of destination/ending station
        :param via: (optional) List of via stations. The route is calculated via all of these stations in the order of the list. The stations have to be a FPTF `Station` object or the ID of the station. The default is no via stations.
        :param min_change_time: (optional) Minimum transfer/change time at each station. Default is the default that HaFAS specifies internal.
        :param max_changes: (optional) Maximum number of changes. Default is unlimited.
        :param products: (optional) Dict of product name(s) and whether it should be enabled or not. Modifies the default products specified in the profile.
        :return: List of FPTF `Journey` objects
        """
        if not isinstance(destination, Station):
            destination = Station(destination)
        for via_station in via:
            if not isinstance(via_station, Station):
                via[via.index(via_station)] = Station(via_station)

        body = self.profile.format_search_from_leg_request(
            origin,
            destination,
            via,
            min_change_time,
            max_changes,
            products
        )
        res = self.profile.request(body)

        return self.profile.parse_journeys_request(res)

    def journey(self, journey: Union[Journey, str]) -> Journey:
        """
        Returns information about a specific journey by its ID

        Useful if you want to refresh the data of the trip, e.g. the real-time data.

        :param journey: FPTF `Journey` object or journey ID
        :return: FPTF `Journey` object with current/updated information
        """
        if not isinstance(journey, Journey):
            journey = Journey(journey)

        body = self.profile.format_journey_request(journey)
        res = self.profile.request(body)

        return self.profile.parse_journey_request(res)

    def locations(self, term: str, rtype: str = 'S') -> List[Station]:
        """
        Returns stations (and addresses) that are searched with the provided term

        The further forward the station is in the list, the higher the similarity to the search term.

        :param term: Search term
        :param rtype: Result types. One of ['S' for stations only, 'ALL' for addresses and stations]
        :return: List of FPTF `Station` objects
        """
        body = self.profile.format_location_request(term, rtype)
        res = self.profile.request(body)

        return self.profile.parse_location_request(res)

    def trip(self, id: str) -> Leg:
        """
        Returns detailed information about a trip based on its ID

        :param id: ID of the trip
        :return: Detailed trip information as FPTF `Leg` object
        """
        body = self.profile.format_trip_request(id)
        res = self.profile.request(body)

        return self.profile.parse_trip_request(res)

    def stop(self, stop):
        """
        Not implemented yet.
        """
        raise NotImplementedError

    def nearby(self, location):
        """
        Not implemented yet.
        """
        raise NotImplementedError

    def radar(self, north, west, south, east):
        """
        Not implemented yet.
        """
        raise NotImplementedError
