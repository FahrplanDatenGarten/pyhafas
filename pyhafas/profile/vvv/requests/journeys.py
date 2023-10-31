from typing import List

from pyhafas.profile.base import BaseJourneysRequest
from pyhafas.profile.interfaces.requests.journeys import JourneysRequestInterface
from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class VVVJourneysRequest(BaseJourneysRequest, JourneysRequestInterface):
    def parse_journeys_request(self, data: HafasResponse) -> List[Journey]:
        journeys = []

        for jny in data.res['outConL']:
            date = self.parse_date(jny['date'])

            # skip all 'TRSF' type journeys (propably better handling should be implemented)
            jny['secL'] = [s for s in jny['secL'] if s['type'] != 'TRSF']

            journeys.append(
                Journey(
                    jny['recon']['ctx'], date=date, duration=self.parse_timedelta(
                        jny['dur']), legs=self.parse_legs(
                        jny, data.common, date)))
        return journeys