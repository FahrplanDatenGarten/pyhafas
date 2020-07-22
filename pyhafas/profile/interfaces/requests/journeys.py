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
            products: Dict[str, bool]
    ) -> dict:
        pass

    @abc.abstractmethod
    def parse_journeys_request(self, data: HafasResponse) -> List[Journey]:
        pass
