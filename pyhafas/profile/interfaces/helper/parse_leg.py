import abc
import datetime
from typing import List

from pyhafas.fptf import Leg


class ParseLegHelperInterface(abc.ABC):
    @abc.abstractmethod
    def parse_leg(
            self,
            journey: dict,
            common: dict,
            departure: dict,
            arrival: dict,
            date: datetime.date,
            jny_type: str = "JNY",
            gis=None) -> Leg:
        pass

    @abc.abstractmethod
    def parse_legs(
            self,
            jny: dict,
            common: dict,
            date: datetime.date) -> List[Leg]:
        pass
