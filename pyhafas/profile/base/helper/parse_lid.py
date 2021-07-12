from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.parse_lid import ParseLidHelperInterface
from pyhafas.types.fptf import Station


class BaseParseLidHelper(ParseLidHelperInterface):
    def parse_lid(self: ProfileInterface, lid: str) -> dict:
        """
        Converts the LID given by HaFAS

        Splits the LID (e.g. A=1@O=Siegburg/Bonn) in multiple elements (e.g. A=1 and O=Siegburg/Bonn).
        These are converted into a dict where the part before the equal sign is the key and the part after the value.

        :param lid: Location identifier (given by HaFAS)
        :return: Dict of the elements of the dict
        """
        parsedLid = {}
        for lidElementGroup in lid.split("@"):
            if lidElementGroup:
                parsedLid[lidElementGroup.split(
                    "=")[0]] = lidElementGroup.split("=")[1]
        return parsedLid

    def parse_lid_to_station(
            self: ProfileInterface,
            lid: str,
            name: str = "",
            latitude: float = 0,
            longitude: float = 0) -> Station:
        """
        Parses the LID given by HaFAS to a station object

        :param lid: Location identifier (given by HaFAS)
        :param name: Station name (optional, if not given, LID is used)
        :param latitude: Latitude of the station (optional, if not given, LID is used)
        :param longitude: Longitude of the station (optional, if not given, LID is used)
        :return: Parsed LID as station object
        """
        parsedLid = self.parse_lid(lid)
        if latitude == 0 and longitude == 0 and parsedLid['X'] and parsedLid['Y']:
            latitude = float(float(parsedLid['Y']) / 1000000)
            longitude = float(float(parsedLid['X']) / 1000000)

        return Station(
            id=parsedLid['L'],
            lid=lid,
            name=name or parsedLid['O'],
            latitude=latitude,
            longitude=longitude
        )
