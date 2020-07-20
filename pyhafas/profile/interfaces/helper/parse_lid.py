import abc

from pyhafas.types.fptf import Station


class ParseLidHelperInterface(abc.ABC):
    @abc.abstractmethod
    def parse_lid(self, lid: str) -> dict:
        pass

    @abc.abstractmethod
    def parse_lid_to_station(
            self,
            lid: str,
            name: str = "",
            latitude: int = 0,
            longitude: int = 0) -> Station:
        pass
