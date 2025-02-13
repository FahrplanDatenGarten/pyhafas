from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseParseLidHelper
from pyhafas.types.fptf import Station


class GVHParseLidHelper(BaseParseLidHelper):
    def parse_lid(self: ProfileInterface, lid: str) -> dict:
        """
        Converts the LID given by HaFAS

        This implementation only returns the LID inside a dict
        because GVH doesn't have normal HaFAS IDs but only HAMM IDs.

        :param lid: Location identifier (given by HaFAS)
        :return: Dict wrapping the given LID
        """
        return {"lid": lid}

    def parse_lid_to_station(
            self: ProfileInterface,
            lid: str,
            name: str = "",
            latitude: float = 0,
            longitude: float = 0) -> Station:
        """
        Parses the LID given by HaFAS to a station object

        :param lid: Location identifier (given by HaFAS)
        :param name: Station name (optional, if not given, empty string is used)
        :param latitude: Latitude of the station (optional, if not given, 0 is used)
        :param longitude: Longitude of the station (optional, if not given, 0 is used)
        :return: Parsed LID as station object
        """
        return Station(
            id=lid,
            lid=lid,
            name=name,
            latitude=latitude,
            longitude=longitude
        )
