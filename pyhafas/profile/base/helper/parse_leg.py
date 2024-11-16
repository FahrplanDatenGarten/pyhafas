import datetime
from typing import List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.parse_leg import ParseLegHelperInterface
from pyhafas.types.fptf import Leg, Mode, Stopover, Line, Operator


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
        if jny_type == "WALK" or jny_type == "TRSF":
            return Leg(
                id=gis['ctx'],
                origin=leg_origin,
                destination=leg_destination,
                departure=self.parse_datetime(departure['dTimeS'], date),
                arrival=self.parse_datetime(arrival['aTimeS'], date),
                line=Line("", mode=Mode.WALKING),
                distance=gis.get('dist') if gis is not None else None
            )
        else:
            leg_stopovers: List[Stopover] = []
            if 'stopL' in journey:
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
                                stopover.get('dPlatfS', stopover.get('dPltfR', stopover.get('dPltfS', {})).get('txt'))),
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
                                stopover.get('aPlatfS', stopover.get('aPltfR', stopover.get('aPltfS', {})).get('txt'))),
                            remarks=[self.parse_remark(common['remL'][msg['remX']], common)
                                     for msg in stopover.get('msgL', []) if msg.get('remX') is not None]
                        ))

            prodL = common['prodL'][journey['prodX']]

            leg_line = Line(
                id=str(prodL['name']).lower().replace(' ', '-'),
                name=prodL['name'],
                public=True,
                mode=Mode.TRAIN
            )

            if 'prodCtx' in prodL:
                prodCtx = prodL['prodCtx']

                leg_line.fahrtNr = prodCtx['num'] if prodCtx and 'num' in prodCtx else None
                leg_line.adminCode = prodCtx['admin'] if prodCtx and 'admin' in prodCtx else None
                leg_line.productName = str(prodCtx['catOut']).strip() if prodCtx and 'catOut' in prodCtx else None
                leg_line.addName = str(prodCtx['addName']).strip() if prodCtx and 'addName' in prodCtx else None

            if 'opL' in common and 'oprX' in prodL:
                opL = common['opL'][prodL['oprX']]

                leg_operator = Operator(
                    id=str(opL['name']).lower().replace(' ', '-'),
                    name=opL['name']
                )

                leg_line.operator = leg_operator

            if 'cls' in prodL:
                byBitmask = {}
                for availableProducts, bitmasks in self.availableProducts.items():
                    for bitmask in bitmasks:
                        byBitmask[bitmask] = availableProducts

                leg_line.product = byBitmask[prodL['cls']]

            return Leg(
                id=journey['jid'],
                line=leg_line,
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
                    departure.get('dPlatfS', departure.get('dPltfR', departure.get('dPltfS', {})).get('txt'))),
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
                    arrival.get('aPlatfS', arrival.get('aPltfR', arrival.get('aPltfS', {})).get('txt'))),
                stopovers=leg_stopovers,
                remarks=[self.parse_remark(common['remL'][msg['remX']], common)
                         for msg in journey.get('msgL', {}) if msg.get('remX') is not None])

    def parse_legs(
            self: ProfileInterface,
            jny: dict,
            common: dict,
            date: datetime.date) -> List[Leg]:
        """
        Parses Legs (when multiple available)

        :param jny: Journeys object returned by HaFAS (contains secL list)
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
