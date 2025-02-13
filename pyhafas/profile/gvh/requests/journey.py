from io import UnsupportedOperation

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseJourneyRequest
from pyhafas.profile.gvh.helper.station_names import find
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class GVHJourneyRequest(BaseJourneyRequest):
    def format_journey_request(
            self: ProfileInterface,
            journey: Journey) -> dict:
        """
        Creates the HAFAS / HAMM request for refreshing journey details
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

        # station details
        station_name_by_lid = dict()
        for loc in data.common['locL']:
            station_name_by_lid[loc['lid']] = loc['name']

        journey = Journey(data.res['outConL'][0]['recon']['ctx'], date=date,
                          duration=self.parse_timedelta(data.res['outConL'][0]['dur']),
                          legs=self.parse_legs(data.res['outConL'][0], data.common, date))
        for leg in journey.legs:
            leg.origin.name = find(station_name_by_lid, leg.origin.lid, leg.origin.id)
            leg.destination.name = find(station_name_by_lid, leg.destination.lid, leg.destination.id)
            for stopover in leg.stopovers:
                stopover.stop.name = find(station_name_by_lid, stopover.stop.lid, stopover.stop.id)
        return journey
