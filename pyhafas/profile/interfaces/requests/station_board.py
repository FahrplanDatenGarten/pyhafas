import abc
import datetime
from typing import Dict, List

from pyhafas.types.fptf import Leg, Station, StationBoardRequestType
from pyhafas.types.hafas_response import HafasResponse


class StationBoardRequestInterface(abc.ABC):
    def format_station_board_request(
            self,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_journeys: int,
            duration: int,
            products: Dict[str, bool]
    ) -> dict:
        pass

    def parse_station_board_request(self, data: HafasResponse) -> List[Leg]:
        pass
