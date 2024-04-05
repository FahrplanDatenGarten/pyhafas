from typing import List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.requests.nearby import NearbyRequestInterface
from pyhafas.types.fptf import Station
from pyhafas.types.hafas_response import HafasResponse
from pyhafas.types.nearby import LatLng


class BaseNearbyRequest(NearbyRequestInterface):
    def format_nearby_request(
            self: ProfileInterface,
            location: LatLng,
            max_walking_distance: int,
            min_walking_distance: int,
            products: dict[str, bool],
            get_pois: bool,
            get_stops: bool,
            max_locations: int,
    ) -> dict:
        """
        Creates the HaFAS request body for a nearby request.

        :param location: LatLng object containing latitude and longitude
        :param max_walking_distance: Maximum walking distance in meters
        :param min_walking_distance: Minimum walking distance in meters
        :param products: Dictionary of product names to products
        :param get_pois: If true, returns pois
        :param get_stops: If true, returns stops instead of locations
        :param max_locations: Maximum number of locations to return
        :return: Request body for HaFAS
        """
        return {
            "cfg": {
                "polyEnc": "GPA"
            },
            "meth": "LocGeoPos",
            "req": {
                "ring": {
                    "cCrd": {
                        "x": location.longitude_e6,
                        "y": location.latitude_e6,
                    },
                    "maxDist": max_walking_distance,
                    "minDist": min_walking_distance,
                },
                "locFltrL": [
                    self.format_products_filter(products)
                ],
                "getPOIs": get_pois,
                "getStops": get_stops,
                "maxLoc": max_locations

            }
        }

    def parse_nearby_response(self: ProfileInterface, data: HafasResponse) -> List[Station]:
        stations = []

        for station in data.res["locL"]:
            try:
                latitude: float = station['crd']['y'] / 1E6
                longitude: float = station['crd']['x'] / 1E6
            except KeyError:
                latitude: float = 0
                longitude: float = 0
            stations.append(
                self.parse_lid_to_station(
                    station['lid'],
                    station['name'],
                    latitude,
                    longitude))

        return stations
