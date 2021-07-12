import abc
from typing import List

from pyhafas.types.fptf import Station
from pyhafas.types.hafas_response import HafasResponse


class LocationRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_location_request(self, term: str, rtype: str = 'S'):
        """
        Creates the HaFAS request body for a location search request.

        :param term: Search term
        :param rtype: Result types. One of ['S' for stations, 'ALL' for addresses and stations]
        :return: Request body for HaFAS
        """
        pass

    @abc.abstractmethod
    def parse_location_request(self, data: HafasResponse) -> List[Station]:
        """
        Parses the HaFAS response for a location request

        :param data: Formatted HaFAS response
        :return: List of Station objects
        """
        pass
