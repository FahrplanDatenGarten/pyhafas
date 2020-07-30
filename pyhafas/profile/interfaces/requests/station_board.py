import abc
import datetime
from typing import Dict, List

from pyhafas.types.station_board_request import StationBoardRequestType
from pyhafas.types.fptf import Leg, Station
from pyhafas.types.hafas_response import HafasResponse


class StationBoardRequestInterface(abc.ABC):
    def format_station_board_request(
            self,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_trips: int,
            duration: int,
            products: Dict[str, bool]
    ) -> dict:
        """
        Creates the HaFAS request for Station Board (departure/arrival)

        :param station: Station to get departures/arrivals for
        :param request_type: ARRIVAL or DEPARTURE
        :param date: Date and time to get departures/arrival for
        :param max_trips: Maximum number of trips that can be returned
        :param products: Allowed products (a product is a mean of transport like ICE,IC)
        :param duration: Time in which trips are searched
        :return: Request body for HaFAS
        """
        pass

    def parse_station_board_request(self, data: HafasResponse) -> List[Leg]:
        """
        Parses the HaFAS data for a station board request

        :param data: Formatted HaFAS response
        :return: List of journey objects
        """
        pass
