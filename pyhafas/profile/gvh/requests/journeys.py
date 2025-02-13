import datetime
from typing import Dict, List, Union

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseJourneysRequest
from pyhafas.profile.gvh.helper.station_names import find
from pyhafas.profile.interfaces.requests.journeys import \
    JourneysRequestInterface
from pyhafas.types.fptf import Journey, Station, Leg
from pyhafas.types.hafas_response import HafasResponse


class GVHJourneysRequest(BaseJourneysRequest):
    def format_journeys_request(
            self: ProfileInterface,
            origin: Station,
            destination: Station,
            via: List[Station],
            date: datetime.datetime,
            min_change_time: int,
            max_changes: int,
            products: Dict[str, bool],
            max_journeys: int
    ) -> dict:
        """
        Creates the HaFAS request body for a journeys request

        :param origin: Origin station
        :param destination: Destionation station
        :param via: Via stations, maybe empty list)
        :param date: Date and time to search journeys for
        :param min_change_time: Minimum transfer/change time at each station
        :param max_changes: Maximum number of changes
        :param products: Allowed products (a product is a mean of transport like ICE,IC)
        :param max_journeys: Maximum number of returned journeys
        :return: Request body for HaFAS
        """
        return {
            'req': {
                'arrLocL': [{
                    'lid': destination.lid if destination.lid else destination.id
                }],
                'viaLocL': [{
                    'loc': {
                        'lid': via_station.lid if via_station.lid else via_station.id
                    }
                } for via_station in via],
                'depLocL': [{
                    'lid': origin.lid if origin.lid else origin.id
                }],
                'outDate': date.strftime("%Y%m%d"),
                'outTime': date.strftime("%H%M%S"),
                'jnyFltrL': [
                    self.format_products_filter(products)
                ],
                'minChgTime': min_change_time,
                'maxChg': max_changes,
                'numF': max_journeys,
            },
            'meth': 'TripSearch'
        }

    def format_search_from_leg_request(
            self: ProfileInterface,
            origin: Leg,
            destination: Station,
            via: List[Station],
            min_change_time: int,
            max_changes: int,
            products: Dict[str, bool],
    ) -> dict:
        """
        Creates the HaFAS request body for a journeys request

        :param origin: Origin leg
        :param destination: Destionation station
        :param via: Via stations, maybe empty list)
        :param min_change_time: Minimum transfer/change time at each station
        :param max_changes: Maximum number of changes
        :param products: Allowed products (a product is a mean of transport like ICE,IC)
        :return: Request body for HaFAS
        """
        return {
            'req': {
                'arrLocL': [{
                    'lid': destination.lid if destination.lid else destination.id
                }],
                'viaLocL': [{
                    'loc': {
                        'lid': via_station.lid if via_station.lid else via_station.id
                    }
                } for via_station in via],
                'locData': {
                    'loc': {
                        'lid': origin.lid if origin.lid else origin.id
                    },
                    'type': 'DEP',
                    'date': origin.departure.strftime("%Y%m%d"),
                    'time': origin.departure.strftime("%H%M%S")
                },
                'jnyFltrL': [
                    self.format_products_filter(products)
                ],
                'minChgTime': min_change_time,
                'maxChg': max_changes,
                'jid': origin.id,
                'sotMode': 'JI'
            },
            'meth': 'SearchOnTrip'
        }

    def parse_journeys_request(
            self: ProfileInterface,
            data: HafasResponse) -> List[Journey]:
        """
        Parses the HaFAS response for a journeys request

        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        journeys = []

        # station details
        station_name_by_lid = dict()
        for loc in data.common['locL']:
            station_name_by_lid[loc['lid']] = loc['name']

        # journeys
        for jny in data.res['outConL']:
            date = self.parse_date(jny['date'])
            journey = Journey(jny['recon']['ctx'], date=date, duration=self.parse_timedelta(jny['dur']),
                              legs=self.parse_legs(jny, data.common, date))
            for leg in journey.legs:
                leg.origin.name = find(station_name_by_lid, leg.origin.lid, leg.origin.id)
                leg.destination.name = find(station_name_by_lid, leg.destination.lid, leg.destination.id)
                for stopover in leg.stopovers:
                    stopover.stop.name = find(station_name_by_lid, stopover.stop.lid, stopover.stop.id)
            journeys.append(journey)
        return journeys
