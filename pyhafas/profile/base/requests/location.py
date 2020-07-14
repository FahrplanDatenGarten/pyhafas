import json
from typing import List

from pyhafas.exceptions import GeneralHafasError
from pyhafas.fptf import Station
from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces import LocationRequestInterface


class BaseLocationRequest(LocationRequestInterface):
    def format_location_request(self: ProfileInterface, term: str):
        """
        Creates the HaFAS request for location search.

        :param term: Search term
        :return: Request for HaFAS
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
            response: str) -> List[Station]:
        """
        Parses the HaFAS response for the location request

        :param response: HaFAS response
        :return: List of Station objects
        """
        data = json.loads(response)
        if data['svcResL'][0]['err'] != 'OK':
            raise GeneralHafasError(
                "HaFAS returned general error: " +
                data['svcResL'][0].get(
                    'errTxt',
                    ""))
        stations = []
        for stn in data['svcResL'][0]['res']['match']['locL']:
            try:
                latitude: int = stn['crd']['y'] / 1000000
                longitude: int = stn['crd']['x'] / 1000000
            except KeyError:
                latitude: int = 0
                longitude: int = 0
            stations.append(
                self.parse_lid_to_station(
                    stn['lid'],
                    stn['name'],
                    latitude,
                    longitude))
        return stations
