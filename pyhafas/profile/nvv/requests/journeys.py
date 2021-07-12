from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.journeys import JourneysRequestInterface
from pyhafas.profile.base import BaseJourneysRequest
from pyhafas.types.hafas_response import HafasResponse


class NVVJourneysRequest(BaseJourneysRequest, JourneysRequestInterface):
    def parse_journeys_request(self:ProfileInterface, data: HafasResponse):
        for jny in data.res["outConL"]:
            jny["ctxRecon"] = ""

        return super().parse_journeys_request(data)
        