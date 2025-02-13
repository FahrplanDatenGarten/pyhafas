import datetime
from typing import Dict, Optional, List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseStationBoardRequest
from pyhafas.types.fptf import Station, StationBoardLeg
from pyhafas.types.hafas_response import HafasResponse
from pyhafas.types.station_board_request import StationBoardRequestType


class GVHStationBoardRequest(BaseStationBoardRequest):
    def format_station_board_request(
            self: ProfileInterface,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_trips: int,
            duration: int,
            products: Dict[str, bool],
            direction: Optional[Station]
    ) -> dict:
        """
        Creates the HaFAS request for a station board request (departure/arrival)

        :param station: Station to get departures/arrivals for
        :param request_type: ARRIVAL or DEPARTURE
        :param date: Date and time to get departures/arrival for
        :param max_trips: Maximum number of trips that can be returned
        :param products: Allowed products (e.g. ICE,IC)
        :param duration: Time in which trips are searched
        :param direction: Direction (end) station of the train. If none, filter will not be applied
        :return: Request body for HaFAS
        """
        return {
            'req': {
                'type': request_type.value,
                'stbLoc': {
                    'lid': station.lid if station.lid else station.id
                },
                'dirLoc': {
                    'lid': direction.lid if direction.lid else direction.id
                } if direction is not None else None,
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
            data: HafasResponse,
            departure_arrival_prefix: str) -> List[StationBoardLeg]:
        """
        Parses the HaFAS data for a station board request

        :param data: Formatted HaFAS response
        :param departure_arrival_prefix: Prefix for specifying whether its for arrival or departure (either "a" or "d")
        :return: List of StationBoardLeg objects
        """
        legs = []
        if not data.res.get('jnyL', False):
            return legs
        else:
            for raw_leg in data.res['jnyL']:
                date = self.parse_date(raw_leg['date'])

                try:
                    platform = raw_leg['stbStop'][departure_arrival_prefix + 'PltfR']['txt'] if \
                        raw_leg['stbStop'].get(departure_arrival_prefix + 'PltfR') is not None else \
                        raw_leg['stbStop'][departure_arrival_prefix + 'PltfS']['txt']
                except KeyError:
                    platform = raw_leg['stbStop'].get(
                        departure_arrival_prefix + 'PlatfR',
                        raw_leg['stbStop'].get(
                            departure_arrival_prefix + 'PlatfS',
                            None))

                legs.append(StationBoardLeg(
                    id=raw_leg['jid'],
                    name=data.common['prodL'][raw_leg['prodX']]['name'],
                    direction=raw_leg.get('dirTxt'),
                    date_time=self.parse_datetime(
                        raw_leg['stbStop'][departure_arrival_prefix + 'TimeS'],
                        date
                    ),
                    station=self.parse_lid_to_station(data.common['locL'][raw_leg['stbStop']['locX']]['lid'],
                                                      name=data.common['locL'][raw_leg['stbStop']['locX']]['name']),
                    platform=platform,
                    delay=self.parse_datetime(
                        raw_leg['stbStop'][departure_arrival_prefix + 'TimeR'],
                        date) - self.parse_datetime(
                        raw_leg['stbStop'][departure_arrival_prefix + 'TimeS'],
                        date) if raw_leg['stbStop'].get(departure_arrival_prefix + 'TimeR') is not None else None,
                    cancelled=bool(raw_leg['stbStop'].get(departure_arrival_prefix + 'Cncl', False))
                ))
            return legs
