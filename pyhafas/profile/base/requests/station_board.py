import datetime
import json
from typing import Dict, List

from pyhafas.exceptions import GeneralHafasError
from pyhafas.fptf import Leg, Station, StationBoardRequestType
from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.station_board import \
    StationBoardRequestInterface


class BaseStationBoardRequest(StationBoardRequestInterface):
    def format_station_board_request(
            self: ProfileInterface,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_journeys: int,
            duration: int,
            products: Dict[str, bool]
    ) -> dict:
        """
        Creates the HaFAS request for Station Board (departure/arrival)

        :param station: Station to get departures/arrivals for
        :param request_type: ARRIVAL or DEPARTURE
        :param date: Date and time to get departures/arrival for
        :param max_journeys: Maximum number of trips that can be returned
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
                'maxJny': max_journeys,
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
            response: str) -> List[Leg]:
        """
        Parses the HaFAS response for the station board request

        :param response: HaFAS response
        :return: List of journey objects
        """
        data = json.loads(response)
        if data['svcResL'][0]['err'] != 'OK':
            raise GeneralHafasError(
                "HaFAS returned general error: " +
                data['svcResL'][0].get(
                    'errTxt',
                    ""))
        legs = []
        try:
            for raw_leg in data['svcResL'][0]['res']['jnyL']:
                leg = self.parse_leg(
                    raw_leg,
                    data['svcResL'][0]['res']['common'],
                    raw_leg['stopL'][0],
                    raw_leg['stopL'][-1],
                    self.parse_date(raw_leg['date'])
                )
                legs.append(leg)
        except KeyError:
            pass

        return legs
