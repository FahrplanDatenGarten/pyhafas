import abc

from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class JourneyRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_journey_request(self, journey: Journey) -> dict:
        """
        Creates the HaFAS request body for a journey request

        :param journey: Id of the journey (ctxRecon)
        :return: Request body for HaFAS
        """
        pass

    @abc.abstractmethod
    def parse_journey_request(self, data: HafasResponse) -> Journey:
        """
        Parses the HaFAS response for a journey request

        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        pass
