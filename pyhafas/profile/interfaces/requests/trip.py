import abc

from pyhafas.types.fptf import Leg
from pyhafas.types.hafas_response import HafasResponse


class TripRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_trip_request(self, trip_id: str) -> dict:
        """
        Creates the HaFAS request for a trip request

        :param trip_id: Id of the trip/leg
        :return: Request body for HaFAS
        """
        pass

    @abc.abstractmethod
    def parse_trip_request(self, data: HafasResponse) -> Leg:
        """
        Parses the HaFAS data for a trip request

        :param data: Formatted HaFAS response
        :return: Leg objects
        """
        pass
