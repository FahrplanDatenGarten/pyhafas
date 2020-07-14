import abc
import datetime
from typing import Dict, List

from pyhafas.fptf import Journey, Station


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
    def parse_journeys_request(self, response: str) -> List[Journey]:
        pass
