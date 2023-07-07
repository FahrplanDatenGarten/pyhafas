from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseJourneyRequest
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class KVBJourneyRequest(BaseJourneyRequest, JourneyRequestInterface):
    def format_journey_request(
            self: ProfileInterface,
            journey: Journey) -> dict:
        """
        Creates the HAFAS (KVB-deployment) request for refreshing journey details
        :param journey: Id of the journey (ctxRecon)
        :return: Request for HAFAS (KVB-deployment)
        """
        return {
            'req': {
                'outReconL': [{
                    'ctx': journey.id
                }]
            },
            'meth': 'Reconstruction'
        }

    def parse_journey_request(self: ProfileInterface, data: HafasResponse) -> Journey:
        """
        Parses the HaFAS response for a journey request
        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        date = self.parse_date(data.res['outConL'][0]['date'])
        return Journey(
            data.res['outConL'][0]['recon']['ctx'],
            date=date,
            duration=self.parse_timedelta(
                data.res['outConL'][0]['dur']),
            legs=self.parse_legs(
                data.res['outConL'][0],
                data.common,
                date))
