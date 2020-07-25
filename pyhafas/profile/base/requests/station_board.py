import datetime
from typing import Dict, List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.station_board import \
    StationBoardRequestInterface
from pyhafas.types.fptf import Leg, Station, StationBoardRequestType
from pyhafas.types.hafas_response import HafasResponse


class BaseStationBoardRequest(StationBoardRequestInterface):
    def format_station_board_request(
            self: ProfileInterface,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_trips: int,
            duration: int,
            products: Dict[str, bool]
    ) -> dict:
        """
        Creates the HaFAS request for Station Board (departure/arrival)

        :param station: Station to get departures/arrivals for
        :param request_type: ARRIVAL or DEPARTURE
        :param date: Date and time to get departures/arrival for
        :param max_trips: Maximum number of trips that can be returned
        :param products: Allowed products (e.g. ICE,IC)
        :param duration: Time in which trips are searched
        :return: Request for HaFAS
        """
        # TODO: More options
        return {
            'req': {
                'type': request_type.value,
                'stbLoc': {
                    'lid': 'A=1@L={}@'.format(station.id)
                },
                'maxJny': max_trips,
                'date': date.strftime("%Y%m%d"),
                'time': date.strftime("%H%M%S"),
                'dur': duration,
                'jnyFltrL': [
                    self.format_products_filter(products)
                ],
            },
            'meth': 'StationBoard'
        }

    def parse_station_board_request(
            self: ProfileInterface,
            data: HafasResponse) -> List[Leg]:
        """
        Parses the HaFAS data for the station board request

        :param data: Formatted HaFAS response
        :return: List of journey objects
        """
        legs = []
        try:
            for raw_leg in data.res['jnyL']:
                leg = self.parse_leg(
                    raw_leg,
                    data.res['common'],
                    raw_leg['stopL'][0],
                    raw_leg['stopL'][-1],
                    self.parse_date(raw_leg['date'])
                )
                legs.append(leg)
        except KeyError:
            pass

        return legs
