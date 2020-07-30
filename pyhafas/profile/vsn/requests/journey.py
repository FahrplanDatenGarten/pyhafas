from pyhafas.profile.base import BaseJourneyRequest
from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.types.fptf import Journey


class VSNJourneyRequest(BaseJourneyRequest, JourneyRequestInterface):
    def format_journey_request(
            self: ProfileInterface,
            journey: Journey) -> dict:
        """
        Creates the HaFAS (VSN-deployment) request for refreshing journey details

        :param journey: Id of the journey (ctxRecon)
        :return: Request for HaFAS (VSN-deployment)
        """
        return {
            'req': {
                'outReconL': [{
                    'ctx': journey.id
                }]
            },
            'meth': 'Reconstruction'
        }
