import abc

from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class JourneyRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_journey_request(self, journey: Journey) -> dict:
        pass

    @abc.abstractmethod
    def parse_journey_request(self, data: HafasResponse) -> Journey:
        pass
