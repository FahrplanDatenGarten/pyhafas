from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseJourneyRequest
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class OEBBJourneyRequest(BaseJourneyRequest, JourneyRequestInterface):
    """
    Class for the OEBB Journeys requests, because the id of the journey is in jny['recon']['ctx'] instead of jny['ctxRecon']
    """

    def format_journey_request(self: ProfileInterface, journey: Journey) -> dict:
        """
        Creates the HaFAS ( Adapted for NASA ) request for refreshing journey details

        :param journey: Id of the journey (ctxRecon)
        :return: Request for HaFAS ( NASA-Adapted )
        """
        return {"req": {"outReconL": [{"ctx": journey.id}]}, "meth": "Reconstruction"}

    def parse_journey_request(self: ProfileInterface, data: HafasResponse) -> Journey:
        """
        Parses the HaFAS response for a journey request ( Adapted for NASA )

        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        date = self.parse_date(data.res["outConL"][0]["date"])
        # todo: parse more data
        return Journey(
            data.res["outConL"][0]["recon"]["ctx"],
            date=date,
            duration=self.parse_timedelta(data.res["outConL"][0]["dur"]),
            legs=self.parse_legs(data.res["outConL"][0], data.common, date),
        )
