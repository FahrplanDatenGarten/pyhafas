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
        """
        Calculates the HaFAS Checksum of the request required for some HaFAS profiles

        :param data: Data of the request
        :return: Checksum for HaFAS
        """
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
        """
        Creates the HaFAS request for Station Board (departure/arrival)

        :param station: Station to get departures/arrivals for
        :param request_type: ARRIVAL or DEPARTURE
        :param date: Date and time to get departures/arrival for
        :param max_journeys: Maximum number of trips that can be returned
        :param products: Allowed products (e.g. ICE,IC)
        :param duration: Time in which trips are searched
        :return: Request for HaFAS
        """
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
        """
        Creates the HaFAS request for refreshing journey details

        :param trip_id: Id of the trip/leg
        :return: Request for HaFAS
        """
        return {
            'req': {
                'jid': trip_id
            },
            'meth': 'JourneyDetails'
        }

    def format_journey_request(self, journey: Journey) -> dict:
        """
        Creates the HaFAS request for refreshing journey details

        :param journey: Id of the journey (ctxRecon)
        :return: Request for HaFAS
        """
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
        """
        Creates the HaFAS request for journeys

        :param origin: Origin station
        :param destination: Destionation station
        :param via: Via stations, maybe empty list)
        :param date: Date and time to search journeys for
        :param min_change_time: Minimum time for changes at stations
        :param max_changes: Maximum number of changes
        :param products: Allowed products (e.g. ICE,IC)
        :return: Request for HaFAS
        """
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
        """
        Creates the HaFAS request for location search.

        :param term: Search term
        :return: Request for HaFAS
        """
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
        """
        Create the products filter given to HaFAS

        :param requested_products: Mapping of Products to whether it's enabled or disabled
        :return:
        """
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

    def parse_datetime(self, time_string: str, date: datetime.date) -> datetime.datetime:
        """
        Parses time HaFAS sends back

        :param time_string: Time string given by HaFAS
        :param date: date object
        :return: datetime object with parsed date and time
        """
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
        """
        Parses time HaFAS sends back as timedelta

        :param time_string: Time string given by HaFAS
        :return: timedelta object with parsed time
        """
        hours = int(time_string[:2])
        minutes = int(time_string[2:-2])
        seconds = int(time_string[-2:])

        return datetime.timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds)

    def parse_date(self, date_string: str) -> datetime.date:
        """
        Parses date HaFAS sends back

        :param date_string: Date string given by HaFAS
        :return: date object with parsed date
        """
        dt = datetime.datetime.strptime(date_string, '%Y%m%d')
        return dt.date()

    def parse_lid(self, lid: str) -> dict:
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
            self,
            lid: str,
            name: str = "",
            latitude: int = 0,
            longitude: int = 0) -> Station:
        """
        Parses the LID given by HaFAS to a station object

        :param lid: Location identifier (given by HaFAS)
        :param name: Station name (optional, if not given, LID is used)
        :param latitude: Latitude of the station (optional, if not given, LID is used)
        :param longitude: Longitude of the station (optional, if not given, LID is used)
        :return: Station object
        """
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
                        departureDelay=self.parse_datetime(
                            stopover['dTimeR'],
                            date) - self.parse_datetime(
                            stopover['dTimeS'],
                            date) if stopover.get('dTimeR') is not None else None,
                        departurePlatform=stopover.get(
                            'dPlatfR',
                            stopover.get('dPlatfS')),
                        arrival=self.parse_datetime(
                            stopover['aTimeS'],
                            date) if stopover.get('aTimeS') is not None else None,
                        arrivalDelay=self.parse_datetime(
                            stopover['aTimeR'],
                            date) - self.parse_datetime(
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
                departure=self.parse_datetime(
                    departure['dTimeS'],
                    date),
                departureDelay=self.parse_datetime(
                    departure['dTimeR'],
                    date) - self.parse_datetime(
                    departure['dTimeS'],
                    date) if departure.get('dTimeR') is not None else None,
                departurePlatform=departure.get(
                    'dPlatfR',
                    departure.get('dPlatfS')),
                arrival=self.parse_datetime(
                    arrival['aTimeS'],
                    date),
                arrivalDelay=self.parse_datetime(
                    arrival['aTimeR'],
                    date) - self.parse_datetime(
                    arrival['aTimeS'],
                    date) if arrival.get('aTimeR') is not None else None,
                arrivalPlatform=arrival.get(
                    'aPlatfR',
                    arrival.get('aPlatfS')),
                stopovers=leg_stopovers)

    def parse_legs(self, jny: dict, common: dict, date: datetime.date) -> List[Leg]:
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
                self.parse_leg(leg.get('jny', None), common, leg['dep'], leg['arr'], date, leg['type'], leg.get('gis')))

        return legs

    def parse_station_board_request(self, response: str) -> List[Leg]:
        """
        Parses the HaFAS response for the station board request

        :param response: HaFAS response
        :return: List of journey objects
        """
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
                self.parse_date(raw_leg['date'])
            )
            legs.append(leg)

        return legs

    def parse_location_request(self, response: str) -> List[Station]:
        """
        Parses the HaFAS response for the location request

        :param response: HaFAS response
        :return: List of Station objects
        """
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
        """
        Parses the HaFAS response for trip request

        :param response: HaFAS response
        :return: Leg objects
        """
        data = json.loads(response)

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise Exception()
        return self.parse_leg(
            data['svcResL'][0]['res']['journey'],
            data['svcResL'][0]['res']['common'],
            data['svcResL'][0]['res']['journey']['stopL'][0],
            data['svcResL'][0]['res']['journey']['stopL'][-1],
            self.parse_date(data['svcResL'][0]['res']['journey']['date'])
        )

    def parse_journey_request(self, response: str) -> Journey:
        """
        Parses the HaFAS response for journeys request

        :param response: HaFAS response
        :return: List of Journey objects
        """
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
        """
        Parses the HaFAS response for journeys request

        :param response: HaFAS response
        :return: List of Journey objects
        """
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
