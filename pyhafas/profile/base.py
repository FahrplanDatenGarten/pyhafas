from __future__ import annotations

import datetime
import json
from enum import Enum
from hashlib import md5
from typing import Dict, List, Tuple

import requests

from pyhafas.fptf import Mode, Stopover
from ..fptf import Journey, Leg, Station


class Profile:
    baseUrl: str = ""
    defaultUserAgent: str = 'pyhafas'

    addMicMac: bool = False
    addChecksum: bool = False
    salt: str = ""

    locale: str = 'de-DE'
    timezone: str = 'Europe/Berlin'

    requestBody: dict = {}

    available_products: dict = []
    default_products: List[str] = []

    def __init__(self, ua=defaultUserAgent):
        self.userAgent = ua

    def url_formatter(self, data: str) -> str:
        url = self.baseUrl

        if self.addChecksum or self.addMicMac:
            parameters = []
            if self.addChecksum:
                parameters.append(
                    'checksum={}'.format(
                        self.calculate_checksum(data)))
            if self.addMicMac:
                parameters.append(
                    'mic={}&mac={}'.format(
                        *self.calculate_mic_mac(data)))
            url += '?{}'.format('&'.join(parameters))

        return url

    def request(self, body):
        data = {
            'svcReqL': [body]
        }
        data.update(self.requestBody)
        data = json.dumps(data)

        req = requests.post(
            self.url_formatter(data),
            data=data,
            headers={
                'User-Agent': self.userAgent,
                'Content-Type': 'application/json'})
        return req

    def calculate_checksum(self, data: str) -> str:
        return md5((data + self.salt).encode('utf-8')).hexdigest()

    def calculate_mic_mac(self, data: str) -> Tuple[str, str]:
        mic = md5(data.encode('utf-8')).hexdigest()
        mac = self.calculate_checksum(mic)
        return mic, mac

    def format_station_board_request(
            self,
            station: Station,
            request_type: StationBoardRequestType,
            date: datetime.datetime,
            max_journeys: int,
            duration: int,
            products: Dict[str, bool]
    ) -> dict:
        # TODO: More options
        return {
            'req': {
                'type': request_type.value,
                'stbLoc': {
                    'lid': 'A=1@L={}@'.format(station.id)
                },
                'maxJny': max_journeys,
                'date': date.strftime("%Y%m%d"),
                'time': date.strftime("%H%M%S"),
                'dur': duration,
                'jnyFltrL': [
                    self.format_products_filter(products)
                ],
            },
            'meth': 'StationBoard'
        }

    def format_trip_request(self, trip_id: str) -> dict:
        return {
            'req': {
                'jid': trip_id
            },
            'meth': 'JourneyDetails'
        }

    def format_journey_request(self, journey: Journey) -> dict:
        return {
            'req': {
                'ctxRecon': journey.id
            },
            'meth': 'Reconstruction'
        }

    def format_journeys_request(
            self,
            origin: Station,
            destination: Station,
            via: List[Station],
            date: datetime.datetime,
            min_change_time: int,
            max_changes: int,
            products: Dict[str, bool]
    ) -> dict:
        # TODO: find out, what commented-out values mean and implement options
        return {
            'req': {
                'arrLocL': [{
                    'type': 'S',
                    'lid': 'A=1@L={}@'.format(destination.id)
                }],
                'viaLocL': [{
                    'loc': {
                        'type': 'S',
                        'lid': 'A=1@L={}@'.format(via_station.id)
                    }
                } for via_station in via],
                'depLocL': [{
                    'type': 'S',
                    'lid': 'A=1@L={}@'.format(origin.id)
                }],
                'outDate': date.strftime("%Y%m%d"),
                'outTime': date.strftime("%H%M%S"),
                'jnyFltrL': [
                    self.format_products_filter(products)
                ],
                'minChgTime': min_change_time,
                'maxChg': max_changes,
                # 'getPasslist': False,
                # 'gisFltrL': [],
                # 'getTariff': False,
                # 'ushrp': True,
                # 'getPT': True,
                # 'getIV': False,
                # 'getPolyline': False,
                # 'numF': 1,
                # 'outFrwd': True,
                # 'trfReq': {
                #    'jnyCl': 2,
                #    'cType': 'PK',
                #    'tvlrProf': [{
                #        'type': 'E',
                #        'redtnCard': 4
                #    }]
                # }
            },
            # 'cfg': {
            #    'polyEnc': 'GPA',
            #    'rtMode': 'HYBRID'
            # },
            'meth': 'TripSearch'
        }

    def format_location_request(
            self,
            term: str):
        return {
            "req": {
                "input": {
                    "field": "S",
                    "loc": {
                        "name": term,
                        "type": "S"
                    }
                }
            },
            "meth": "LocMatch"
        }

    def format_products_filter(self, requested_products: dict) -> dict:
        products = self.default_products
        for requested_product in requested_products:
            if requested_products[requested_product]:
                try:
                    products.index(requested_product)
                except ValueError:
                    products.append(requested_product)

            elif not requested_products[requested_product]:
                try:
                    products.pop(products.index(requested_product))
                except ValueError:
                    pass
        bitmask_sum = 0
        for product in products:
            try:
                for product_bitmask in self.available_products[product]:
                    bitmask_sum += product_bitmask
            except KeyError:
                raise Exception()
        return {
            'type': 'PROD',
            'mode': 'INC',
            'value': str(bitmask_sum)
        }

    def parse_time(self, time_string: str, date: datetime.date) -> datetime.datetime:
        hour = int(time_string[-6:-4])
        minute = int(time_string[-4:-2])
        second = int(time_string[-2:])

        dateOffset = int(time_string[:2]) if len(time_string) > 6 else 0
        return datetime.datetime(
            date.year,
            date.month,
            date.day,
            hour,
            minute,
            second) + datetime.timedelta(days=dateOffset)

    def parse_timedelta(self, time_string: str) -> datetime.timedelta:
        hours = int(time_string[:2])
        minutes = int(time_string[2:-2])
        seconds = int(time_string[-2:])

        return datetime.timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds)

    def parse_date(self, date_string: str) -> datetime.date:
        dt = datetime.datetime.strptime(date_string, '%Y%m%d')
        return dt.date()

    def parse_station_board_request(self, response: str) -> List[Leg]:
        data = json.loads(response)
        legs = []
        if data['svcResL'][0]['err'] != 'OK':
            raise Exception()
        for raw_leg in data['svcResL'][0]['res']['jnyL']:
            leg = self.parse_leg(
                raw_leg,
                data['svcResL'][0]['res']['common'],
                raw_leg['stopL'][0],
                raw_leg['stopL'][-1],
                self.parse_date(raw_leg['date']),
                "JNY"
            )
            legs.append(leg)

        return legs

    def parse_lid(self, lid: str) -> dict:
        parsedLid = {}
        for lidElementGroup in lid.split("@"):
            if lidElementGroup:
                parsedLid[lidElementGroup.split(
                    "=")[0]] = lidElementGroup.split("=")[1]
        return parsedLid

    def parse_lid_to_station(
            self,
            lid: str,
            name: str = "",
            latitude: int = 0,
            longitude: int = 0) -> Station:
        parsedLid = self.parse_lid(lid)
        if latitude == 0 and longitude == 0 and parsedLid['X'] and parsedLid['Y']:
            latitude = int(int(parsedLid['Y']) / 1000000)
            longitude = int(int(parsedLid['X']) / 1000000)

        return Station(
            id=parsedLid['L'],
            name=name or parsedLid['O'],
            latitude=latitude,
            longitude=longitude
        )

    def parse_leg(
            self,
            journey: dict,
            common: dict,
            departure: dict,
            arrival: dict,
            date: datetime.date,
            jny_type: str,
            gis=None) -> Leg:
        leg_origin = self.parse_lid_to_station(
            common['locL'][departure['locX']]['lid'])
        leg_destination = self.parse_lid_to_station(
            common['locL'][arrival['locX']]['lid'])
        if jny_type == "WALK":
            return Leg(
                id=gis['ctx'],
                origin=leg_origin,
                destination=leg_destination,
                departure=self.parse_time(departure['dTimeS'], date),
                arrival=self.parse_time(arrival['aTimeS'], date),
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
                        departure=self.parse_time(
                            stopover.get('dTimeS'),
                            date) if stopover.get('dTimeS') is not None else None,
                        departureDelay=self.parse_time(
                            stopover['dTimeR'],
                            date) - self.parse_time(
                            stopover['dTimeS'],
                            date) if stopover.get('dTimeR') is not None else None,
                        departurePlatform=stopover.get(
                            'dPlatfR',
                            stopover.get('dPlatfS')),
                        arrival=self.parse_time(
                            stopover['aTimeS'],
                            date) if stopover.get('aTimeS') is not None else None,
                        arrivalDelay=self.parse_time(
                            stopover['aTimeR'],
                            date) - self.parse_time(
                            stopover['aTimeS'],
                            date) if stopover.get('aTimeR') is not None else None,
                        arrivalPlatform=stopover.get(
                            'aPlatfR',
                            stopover.get('aPlatfS')),
                    ))
            return Leg(
                id=journey['jid'],
                name=common['prodL'][journey['prodX']]['name'],
                origin=leg_origin,
                destination=leg_destination,
                cancelled=bool(arrival.get('aCncl', False)),
                departure=self.parse_time(
                    departure['dTimeS'],
                    date),
                departureDelay=self.parse_time(
                    departure['dTimeR'],
                    date) - self.parse_time(
                    departure['dTimeS'],
                    date) if departure.get('dTimeR') is not None else None,
                departurePlatform=departure.get(
                    'dPlatfR',
                    departure.get('dPlatfS')),
                arrival=self.parse_time(
                    arrival['aTimeS'],
                    date),
                arrivalDelay=self.parse_time(
                    arrival['aTimeR'],
                    date) - self.parse_time(
                    arrival['aTimeS'],
                    date) if arrival.get('aTimeR') is not None else None,
                arrivalPlatform=arrival.get(
                    'aPlatfR',
                    arrival.get('aPlatfS')),
                stopovers=leg_stopovers)

    def parse_legs(self, jny: dict, common: dict, date: datetime.date) -> List[Leg]:
        legs: List[Leg] = []

        for leg in jny['secL']:
            legs.append(self.parse_leg(leg.get('jny', None), common, leg['dep'], leg['arr'], date, leg['type'], leg.get('gis')))

        return legs

    def parse_location_request(self, response: str) -> List[Station]:
        data = json.loads(response)
        stations = []
        for stn in data['svcResL'][0]['res']['match']['locL']:
            latitude: int = 0
            longitude: int = 0
            if stn['crd']:
                latitude = stn['crd']['y'] / 1000000
                longitude = stn['crd']['x'] / 1000000
            stations.append(
                self.parse_lid_to_station(
                    stn['lid'],
                    stn['name'],
                    latitude,
                    longitude))
        return stations

    def parse_trip_request(self, response: str) -> Leg:
        data = json.loads(response)

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise Exception()
        return self.parse_leg(
            data['svcResL'][0]['res']['journey'],
            data['svcResL'][0]['res']['common'],
            data['svcResL'][0]['res']['journey']['stopL'][0],
            data['svcResL'][0]['res']['journey']['stopL'][-1],
            self.parse_date(data['svcResL'][0]['res']['journey']['date']),
            "JNY"
        )

    def parse_journey_request(self, response: str) -> Journey:
        data = json.loads(response)

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise Exception()
        date = self.parse_date(data['svcResL'][0]['res']['outConL'][0]['date'])
        return Journey(
            data['svcResL'][0]['res']['outConL'][0]['ctxRecon'],
            date=date,
            duration=self.parse_timedelta(data['svcResL'][0]['res']['outConL'][0]['dur']),
            legs=self.parse_legs(data['svcResL'][0]['res']['outConL'][0], data['svcResL'][0]['res']['common'], date))

    def parse_journeys_request(self, response: str) -> List[Journey]:
        data = json.loads(response)
        journeys = []

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise Exception()

        for jny in data['svcResL'][0]['res']['outConL']:
            # TODO: Add more data
            date = self.parse_date(jny['date'])
            journeys.append(Journey(
                jny['ctxRecon'],
                date=date,
                duration=self.parse_timedelta(jny['dur']),
                legs=self.parse_legs(jny, data['svcResL'][0]['res']['common'], date)
            ))
        return journeys


class StationBoardRequestType(Enum):
    DEPARTURE = 'DEP'
    ARRIVAL = 'ARR'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
