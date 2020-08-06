from typing import List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces import LocationRequestInterface
from pyhafas.types.fptf import Station
from pyhafas.types.hafas_response import HafasResponse


class BaseLocationRequest(LocationRequestInterface):
    def format_location_request(self: ProfileInterface, term: str):
        """
        Creates the HaFAS request body for a location search request.

        :param term: Search term
        :return: Request body for HaFAS
        """
        return {
            "req": {
                "input": {
                    "field": "S",
                    "loc": {
                        "name": term,
                        "type": "S"
                    }
                }
            },
            "meth": "LocMatch"
        }

    def parse_location_request(
            self: ProfileInterface,
            data: HafasResponse) -> List[Station]:
        """
        Parses the HaFAS response for a location request

        :param data: Formatted HaFAS response
        :return: List of Station objects
        """
        stations = []
        for stn in data.res['match']['locL']:
            try:
                latitude: float = stn['crd']['y'] / 1000000
                longitude: float = stn['crd']['x'] / 1000000
            except KeyError:
                latitude: float = 0
                longitude: float = 0
            stations.append(
                self.parse_lid_to_station(
                    stn['lid'],
                    stn['name'],
                    latitude,
                    longitude))
        return stations
