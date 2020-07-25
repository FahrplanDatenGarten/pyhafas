import datetime
from typing import List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.parse_leg import ParseLegHelperInterface
from pyhafas.types.fptf import Leg, Mode, Stopover


class BaseParseLegHelper(ParseLegHelperInterface):
    def parse_leg(
            self: ProfileInterface,
            journey: dict,
            common: dict,
            departure: dict,
            arrival: dict,
            date: datetime.date,
            jny_type: str = "JNY",
            gis=None) -> Leg:
        """
        Parses Leg HaFAS returns into Leg object

        Different Types of HaFAS responses can be parsed into a leg object with the multiple variables

        :param journey: Journey object given back by HaFAS (Data of the Leg to parse)
        :param common:  Common object given back by HaFAS
        :param departure: Departure object given back by HaFAS
        :param arrival: Arrival object given back by HaFAS
        :param date: Parsed date of Journey (Departing date)
        :param jny_type: HaFAS Journey type
        :param gis: GIS object given back by HaFAS. Currently only used by "WALK" journey type.
        :return: Parsed Leg object
        """
        leg_origin = self.parse_lid_to_station(
            common['locL'][departure['locX']]['lid'])
        leg_destination = self.parse_lid_to_station(
            common['locL'][arrival['locX']]['lid'])
        if jny_type == "WALK":
            return Leg(
                id=gis['ctx'],
                origin=leg_origin,
                destination=leg_destination,
                departure=self.parse_datetime(departure['dTimeS'], date),
                arrival=self.parse_datetime(arrival['aTimeS'], date),
                mode=Mode.WALKING,
                name=None,
                distance=gis['dist'] if gis is not None else None
            )
        else:
            leg_stopovers: List[Stopover] = []
            for stopover in journey['stopL']:
                leg_stopovers.append(
                    Stopover(
                        stop=self.parse_lid_to_station(
                            common['locL'][stopover['locX']]['lid']
                        ),
                        cancelled=bool(
                            stopover.get(
                                'dCncl',
                                stopover.get(
                                    'aCncl',
                                    False
                                ))),
                        departure=self.parse_datetime(
                            stopover.get('dTimeS'),
                            date) if stopover.get('dTimeS') is not None else None,
                        departure_delay=self.parse_datetime(
                            stopover['dTimeR'],
                            date) - self.parse_datetime(
                            stopover['dTimeS'],
                            date) if stopover.get('dTimeR') is not None else None,
                        departure_platform=stopover.get(
                            'dPlatfR',
                            stopover.get('dPlatfS')),
                        arrival=self.parse_datetime(
                            stopover['aTimeS'],
                            date) if stopover.get('aTimeS') is not None else None,
                        arrival_delay=self.parse_datetime(
                            stopover['aTimeR'],
                            date) - self.parse_datetime(
                            stopover['aTimeS'],
                            date) if stopover.get('aTimeR') is not None else None,
                        arrival_platform=stopover.get(
                            'aPlatfR',
                            stopover.get('aPlatfS')),
                    ))
            return Leg(
                id=journey['jid'],
                name=common['prodL'][journey['prodX']]['name'],
                origin=leg_origin,
                destination=leg_destination,
                cancelled=bool(arrival.get('aCncl', False)),
                departure=self.parse_datetime(
                    departure['dTimeS'],
                    date),
                departure_delay=self.parse_datetime(
                    departure['dTimeR'],
                    date) - self.parse_datetime(
                    departure['dTimeS'],
                    date) if departure.get('dTimeR') is not None else None,
                departure_platform=departure.get(
                    'dPlatfR',
                    departure.get('dPlatfS')),
                arrival=self.parse_datetime(
                    arrival['aTimeS'],
                    date),
                arrival_delay=self.parse_datetime(
                    arrival['aTimeR'],
                    date) - self.parse_datetime(
                    arrival['aTimeS'],
                    date) if arrival.get('aTimeR') is not None else None,
                arrival_platform=arrival.get(
                    'aPlatfR',
                    arrival.get('aPlatfS')),
                stopovers=leg_stopovers)

    def parse_legs(
            self: ProfileInterface,
            jny: dict,
            common: dict,
            date: datetime.date) -> List[Leg]:
        """
        Parses Legs (when multiple available)

        :param jny: Journies object returned by HaFAS (contains secL list)
        :param common: Common object returned by HaFAS
        :param date: Parsed date of Journey (Departing date)
        :return: Parsed List of Leg objects
        """
        legs: List[Leg] = []

        for leg in jny['secL']:
            legs.append(
                self.parse_leg(
                    leg.get(
                        'jny',
                        None),
                    common,
                    leg['dep'],
                    leg['arr'],
                    date,
                    leg['type'],
                    leg.get('gis')))

        return legs
