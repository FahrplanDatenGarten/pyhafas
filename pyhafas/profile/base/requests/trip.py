import json

from pyhafas.exceptions import GeneralHafasError
from pyhafas.fptf import Leg
from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.trip import TripRequestInterface


class BaseTripRequest(TripRequestInterface):
    def format_trip_request(self: ProfileInterface, trip_id: str) -> dict:
        """
        Creates the HaFAS request for refreshing journey details

        :param trip_id: Id of the trip/leg
        :return: Request for HaFAS
        """
        return {
            'req': {
                'jid': trip_id
            },
            'meth': 'JourneyDetails'
        }

    def parse_trip_request(self: ProfileInterface, data: dict) -> Leg:
        """
        Parses the HaFAS data for trip request

        :param data: Formatted HaFAS response
        :return: Leg objects
        """
        return self.parse_leg(
            data['res']['journey'],
            data['common'],
            data['res']['journey']['stopL'][0],
            data['res']['journey']['stopL'][-1],
            self.parse_date(data['res']['journey']['date'])
        )
