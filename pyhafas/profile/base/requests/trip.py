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

    def parse_trip_request(self: ProfileInterface, response: str) -> Leg:
        """
        Parses the HaFAS response for trip request

        :param self:
        :param response: HaFAS response
        :return: Leg objects
        """
        data = json.loads(response)
        if data['svcResL'][0]['err'] != 'OK':
            raise GeneralHafasError(
                "HaFAS returned general error: " +
                data['svcResL'][0].get(
                    'errTxt',
                    ""))
        return self.parse_leg(
            data['svcResL'][0]['res']['journey'],
            data['svcResL'][0]['res']['common'],
            data['svcResL'][0]['res']['journey']['stopL'][0],
            data['svcResL'][0]['res']['journey']['stopL'][-1],
            self.parse_date(data['svcResL'][0]['res']['journey']['date'])
        )
