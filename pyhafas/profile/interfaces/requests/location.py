import abc
from typing import List

from pyhafas.fptf import Station


class LocationRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_location_request(self, term: str):
        pass

    @abc.abstractmethod
    def parse_location_request(self, response: str) -> List[Station]:
        pass
