import abc
import datetime
from typing import Dict, List

from pyhafas.types.fptf import Journey, Station
from pyhafas.types.hafas_response import HafasResponse


class JourneysRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_journeys_request(
            self,
            origin: Station,
            destination: Station,
            via: List[Station],
            date: datetime.datetime,
            min_change_time: int,
            max_changes: int,
            products: Dict[str, bool],
            max_journeys: int
    ) -> dict:
        """
        Creates the HaFAS request body for a journeys request

        :param origin: Origin station
        :param destination: Destionation station
        :param via: Via stations, maybe empty list)
        :param date: Date and time to search journeys for
        :param min_change_time: Minimum transfer/change time at each station
        :param max_changes: Maximum number of changes
        :param products: Allowed products (a product is a mean of transport like ICE,IC)
        :param max_journeys: Maximum number of returned journeys
        :return: Request body for HaFAS
        """
        pass

    @abc.abstractmethod
    def parse_journeys_request(self, data: HafasResponse) -> List[Journey]:
        """
        Parses the HaFAS response for a journeys request

        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        pass
