import abc
import datetime
from typing import List

from pyhafas.types.fptf import Leg


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
        """
        Parses Leg HaFAS returns into Leg object

        :param journey: Journey object given back by HaFAS (Data of the Leg to parse)
        :param common:  Common object given back by HaFAS
        :param departure: Departure object given back by HaFAS
        :param arrival: Arrival object given back by HaFAS
        :param date: Parsed date of Journey (Departing date)
        :param jny_type: HaFAS Journey type
        :param gis: GIS object given back by HaFAS.
        :return: Parsed Leg object
        """
        pass

    @abc.abstractmethod
    def parse_legs(
            self,
            jny: dict,
            common: dict,
            date: datetime.date) -> List[Leg]:
        """
        Parses Legs (when multiple available)

        :param jny: Journeys object returned by HaFAS
        :param common: Common object returned by HaFAS
        :param date: Parsed date of Journey (Departing date)
        :return: Parsed List of Leg objects
        """
        pass
