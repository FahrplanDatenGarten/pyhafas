import abc

from pyhafas.types.fptf import Station


class ParseLidHelperInterface(abc.ABC):
    @abc.abstractmethod
    def parse_lid(self, lid: str) -> dict:
        """
        Converts the LID given by HaFAS. Splits the LID in multiple elements

        :param lid: Location identifier (given by HaFAS)
        :return: Dict of the elements of the dict
        """
        pass

    @abc.abstractmethod
    def parse_lid_to_station(
            self,
            lid: str,
            name: str = "",
            latitude: int = 0,
            longitude: int = 0) -> Station:
        """
        Parses the LID given by HaFAS to a station object

        :param lid: Location identifier (given by HaFAS)
        :param name: Station name (optional)
        :param latitude: Latitude of the station (optional)
        :param longitude: Longitude of the station (optional)
        :return: Parsed LID as station object
        """
        pass
