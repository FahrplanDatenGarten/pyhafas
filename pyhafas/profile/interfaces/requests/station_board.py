import abc
import datetime
from typing import Dict, List, Optional

from pyhafas.types.fptf import Station, StationBoardLeg
from pyhafas.types.hafas_response import HafasResponse
from pyhafas.types.station_board_request import StationBoardRequestType


class StationBoardRequestInterface(abc.ABC):
    def format_station_board_request(
            self,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_trips: int,
            duration: int,
            products: Dict[str, bool],
            direction: Optional[Station]
    ) -> dict:
        """
        Creates the HaFAS request for Station Board (departure/arrival)

        :param station: Station to get departures/arrivals for
        :param request_type: ARRIVAL or DEPARTURE
        :param date: Date and time to get departures/arrival for
        :param max_trips: Maximum number of trips that can be returned
        :param products: Allowed products (a product is a mean of transport like ICE,IC)
        :param duration: Time in which trips are searched
        :param direction: Direction (end) station of the train. If none, filter will not be applied
        :return: Request body for HaFAS
        """
        pass

    def parse_station_board_request(
            self,
            data: HafasResponse,
            departure_arrival_prefix: str) -> List[StationBoardLeg]:
        """
        Parses the HaFAS data for a station board request

        :param data: Formatted HaFAS response
        :param departure_arrival_prefix: Prefix for specifying whether its for arrival or departure
        :return: List of StationBoardLeg objects
        """
        pass
