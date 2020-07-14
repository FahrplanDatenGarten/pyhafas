import abc

from pyhafas.fptf import Leg


class TripRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_trip_request(self, trip_id: str) -> dict:
        pass

    @abc.abstractmethod
    def parse_trip_request(self, response: str) -> Leg:
        pass
