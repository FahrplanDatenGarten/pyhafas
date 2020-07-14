import json

from pyhafas.exceptions import GeneralHafasError
from pyhafas.fptf import Journey
from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface


class BaseJourneyRequest(JourneyRequestInterface):
    def format_journey_request(
            self: ProfileInterface,
            journey: Journey) -> dict:
        """
        Creates the HaFAS request for refreshing journey details

        :param journey: Id of the journey (ctxRecon)
        :return: Request for HaFAS
        """
        return {
            'req': {
                'ctxRecon': journey.id
            },
            'meth': 'Reconstruction'
        }

    def parse_journey_request(
            self: ProfileInterface,
            response: str) -> Journey:
        """
        Parses the HaFAS response for journeys request

        :param response: HaFAS response
        :return: List of Journey objects
        """
        data = json.loads(response)

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise GeneralHafasError(
                "HaFAS returned general error: " +
                data['svcResL'][0].get(
                    'errTxt',
                    ""))
        date = self.parse_date(data['svcResL'][0]['res']['outConL'][0]['date'])
        return Journey(
            data['svcResL'][0]['res']['outConL'][0]['ctxRecon'],
            date=date,
            duration=self.parse_timedelta(
                data['svcResL'][0]['res']['outConL'][0]['dur']),
            legs=self.parse_legs(
                data['svcResL'][0]['res']['outConL'][0],
                data['svcResL'][0]['res']['common'],
                date))
