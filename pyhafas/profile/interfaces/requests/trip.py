import abc

from pyhafas.types.fptf import Leg
from pyhafas.types.hafas_response import HafasResponse


class TripRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_trip_request(self, trip_id: str) -> dict:
        pass

    @abc.abstractmethod
    def parse_trip_request(self, data: HafasResponse) -> Leg:
        pass
