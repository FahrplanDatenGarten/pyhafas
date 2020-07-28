from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class BaseJourneyRequest(JourneyRequestInterface):
    def format_journey_request(
            self: ProfileInterface,
            journey: Journey) -> dict:
        """
        Creates the HaFAS request body for a journey request

        :param journey: Id of the journey (ctxRecon)
        :return: Request body for HaFAS
        """
        return {
            'req': {
                'ctxRecon': journey.id
            },
            'meth': 'Reconstruction'
        }

    def parse_journey_request(
            self: ProfileInterface,
            data: HafasResponse) -> Journey:
        """
        Parses the HaFAS response for a journey request

        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        date = self.parse_date(data.res['outConL'][0]['date'])
        return Journey(
            data.res['outConL'][0]['ctxRecon'],
            date=date,
            duration=self.parse_timedelta(
                data.res['outConL'][0]['dur']),
            legs=self.parse_legs(
                data.res['outConL'][0],
                data.common,
                date))
