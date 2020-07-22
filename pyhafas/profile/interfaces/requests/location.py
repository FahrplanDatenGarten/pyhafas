import abc
from typing import List

from pyhafas.types.fptf import Station
from pyhafas.types.hafas_response import HafasResponse


class LocationRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_location_request(self, term: str):
        pass

    @abc.abstractmethod
    def parse_location_request(self, data: HafasResponse) -> List[Station]:
        pass
