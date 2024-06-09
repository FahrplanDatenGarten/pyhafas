import abc
from typing import List

from pyhafas.types.fptf import Station
from pyhafas.types.hafas_response import HafasResponse
from pyhafas.types.nearby import LatLng


class NearbyRequestInterface(abc.ABC):
    @abc.abstractmethod
    def format_nearby_request(self,
                              location: LatLng,
                              max_walking_distance: int,
                              min_walking_distance: int,
                              products: dict[str, bool],
                              get_pois: bool,
                              get_stops: bool,
                              max_locations: int) -> dict:
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
        pass

    @abc.abstractmethod
    def parse_nearby_response(self, data: HafasResponse) -> List[Station]:
        pass
