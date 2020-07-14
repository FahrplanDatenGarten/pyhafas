import abc

from pyhafas.fptf import Journey


class JourneyRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_journey_request(self, journey: Journey) -> dict:
        pass

    @abc.abstractmethod
    def parse_journey_request(self, response: str) -> Journey:
        pass
