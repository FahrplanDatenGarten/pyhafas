from __future__ import annotations

import datetime
import json
from enum import Enum
from hashlib import md5
from typing import Dict, List

import requests
from pyhafas.fptf import Stopover

from ..fptf import Journey, Station, Leg


class Profile:
    baseUrl: str = None
    defaultUserAgent: str = 'pyhafas'

    addMicMac: bool = False
    addChecksum: bool = False
    salt: str = None

    locale: str = 'de-DE'
    timezone: str = 'Europe/Berlin'

    requestBody: dict = {}

    def __init__(self, ua=defaultUserAgent):
        self.userAgent = ua

    def urlFormatter(self, data):
        url = self.baseUrl

        if self.addChecksum or self.addMicMac:
            parameters = []
            if self.addChecksum:
                parameters.append(
                    'checksum={}'.format(
                        self.calculateChecksum(data)))
            if self.addMicMac:
                parameters.append(
                    'mic={}&mac={}'.format(
                        *self.calculateMicMac(data)))
            url += '?{}'.format('&'.join(parameters))

        return url

    def request(self, body):
        data = {
            'svcReqL': [body]
        }
        data.update(self.requestBody)
        data = json.dumps(data)

        req = requests.post(
            self.urlFormatter(data),
            data=data,
            headers={
                'User-Agent': self.userAgent,
                'Content-Type': 'application/json'})
        return req

        req = requests.post(
            self.urlFormatter(data),
            data=data,
            headers={
                'User-Agent': self.userAgent,
                'Content-Type': 'application/json'})
        return req

    def calculateChecksum(self, data):
        return md5((data + self.salt).encode('utf-8')).hexdigest()

    def calculateMicMac(self, data):
        mic = md5(data.encode('utf-8')).hexdigest()
        mac = self.calculateChecksum(mic)
        return mic, mac

    def formatStationBoardRequest(
            self,
            station: Station,
            request_type: StationBoardRequestType) -> Dict:
        return {
            'req': {
                'type': request_type.value,
                'stbLoc': {
                    'lid': 'A=1@L={}@'.format(station.id)
                },
                'dur': 1,
            },
            'meth': 'StationBoard'
        }

    def formatJourneyRequest(self, journey: Journey) -> Dict:
        return {
            'req': {
                'ctxRecon': journey.id
            },
            'meth': 'Reconstruction'
        }

    def formatJourneysRequest(
            self,
            origin: Station,
            destination: Station,
            via: List[Station],
            date: datetime.datetime,
            min_change_time: int,
            max_changes: int
    ) -> Dict:
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
                'minChgTime': min_change_time,
                'maxChg': max_changes,
                # 'jnyFltrL': [{
                #    'type': 'PROD',
                #    'mode': 'INC',
                #    'value': '1023'
                # }],
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

    def formatLocationRequest(
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

    def parseTime(self, timeString, date) -> datetime.datetime:
        hour = int(timeString[-6:-4])
        minute = int(timeString[-4:-2])
        second = int(timeString[-2:])

        dateOffset = int(timeString[:2]) if len(timeString) > 6 else 0
        return datetime.datetime(
            date.year,
            date.month,
            date.day,
            hour,
            minute,
            second) + datetime.timedelta(days=dateOffset)

    def parseTimedelta(self, timeString) -> datetime.timedelta:
        hours = int(timeString[:2])
        minutes = int(timeString[2:-2])
        seconds = int(timeString[-2:])

        return datetime.timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds)

    def parseDate(self, dateString) -> datetime.date:
        dt = datetime.datetime.strptime(dateString, '%Y%m%d')
        return dt.date()

    def parseStationBoardRequest(self, response: str) -> List[Journey]:
        data = json.loads(response)
        journeys = []

        if data.get('err') != 'OK' or data['svcResL'][0]['err'] != 'OK':
            raise Exception()

        for jny in data['svcResL'][0]['res']['jnyL']:
            journey = Journey(jny['jid'])
            journey.date = self.parseDate(jny['date'])
            # TODO: Add more data
            # ...
            # ...
            journeys.append(journey)

        return journeys

    def parseLid(self, lid: str) -> Dict:
        parsedLid = {}
        for lidElementGroup in lid.split("@"):
            if lidElementGroup:
                parsedLid[lidElementGroup.split(
                    "=")[0]] = lidElementGroup.split("=")[1]
        return parsedLid

    def parseLidToStation(self, lid: str, name: str = "", latitude=0, longitude=0) -> Station:
        parsedLid = self.parseLid(lid)
        if latitude == 0 and longitude == 0 and parsedLid['X'] and parsedLid['Y']:
            latitude = int(parsedLid['Y']) / 1000000
            longitude = int(parsedLid['X']) / 1000000

        return Station(
            id=parsedLid['L'],
            name=name or parsedLid['O'],
            latitude=latitude,
            longitude=longitude
        )

    def parseLocationRequest(self, response: str) -> List[Station]:
        data = json.loads(response)
        stations = []
        for stn in data['svcResL'][0]['res']['match']['locL']:
            latitude: int = 0
            longitude: int = 0
            if stn['crd']:
                latitude = stn['crd']['y'] / 1000000
                longitude = stn['crd']['x'] / 1000000
            stations.append(self.parseLidToStation(stn['lid'], stn['name'], latitude, longitude))
        return stations

    def parseJourneyRequest(self, response: str) -> Journey:
        pass

    def parseJourneysRequest(self, response: str) -> List[Journey]:
        data = json.loads(response)
        journeys = []

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise Exception()

        for jny in data['svcResL'][0]['res']['outConL']:
            legs: List[Leg] = []
            # TODO: Add more data
            for leg in jny['secL']:
                leg_origin = self.parseLidToStation(data['svcResL'][0]['res']['common']['locL'][leg['dep']['locX']]['lid'])
                leg_destination = self.parseLidToStation(data['svcResL'][0]['res']['common']['locL'][leg['arr']['locX']]['lid'])
                if leg['type'] == "WALK":
                    legs.append(Leg(
                        origin=leg_origin,
                        destination=leg_destination,
                        departure=self.parseTime(leg['dep']['dTimeS'], self.parseDate(jny['date'])),
                        arrival=self.parseTime(leg['arr']['aTimeS'], self.parseDate(jny['date'])),
                        mode="walking"
                    ))
                else:
                    leg_stopovers: List[Stopover] = []
                    for stopover in leg['jny']['stopL']:
                        leg_stopovers.append(Stopover(
                            stop=self.parseLidToStation(data['svcResL'][0]['res']['common']['locL'][stopover['locX']]['lid']),
                            cancelled=bool(stopover.get('dCncl', stopover.get('aCncl', False))),
                            departure=self.parseTime(stopover.get('dTimeS'), self.parseDate(jny['date'])) if stopover.get('dTimeS') is not None else None,
                            departure_delay=self.parseTime(stopover['dTimeR'], self.parseDate(jny['date'])) - self.parseTime(stopover['dTimeS'], self.parseDate(jny['date'])) if stopover.get('dTimeR') is not None else None,
                            departure_platform=stopover.get('dPlatfR', stopover.get('dPlatfS')),
                            arrival=self.parseTime(stopover['aTimeS'], self.parseDate(jny['date'])) if stopover.get('aTimeS') is not None else None,
                            arrival_delay=self.parseTime(stopover['aTimeR'], self.parseDate(jny['date'])) - self.parseTime(stopover['aTimeS'], self.parseDate(jny['date'])) if stopover.get('aTimeR') is not None else None,
                            arrival_platform=stopover.get('aPlatfR', stopover.get('aPlatfS')),
                        ))
                    legs.append(Leg(
                        origin=leg_origin,
                        destination=leg_destination,
                        cancelled=bool(leg['arr'].get('aCncl', False)),
                        departure=self.parseTime(leg['dep']['dTimeS'], self.parseDate(jny['date'])),
                        departure_delay=self.parseTime(leg['dep']['dTimeR'], self.parseDate(jny['date'])) - self.parseTime(leg['dep']['dTimeS'], self.parseDate(jny['date'])) if leg['dep'].get('dTimeR') is not None else None,
                        departure_platform=leg['dep'].get('dPlatfR', leg['dep'].get('dPlatfS')),
                        arrival=self.parseTime(leg['arr']['aTimeS'], self.parseDate(jny['date'])),
                        arrival_delay=self.parseTime(leg['arr']['aTimeR'], self.parseDate(jny['date'])) - self.parseTime(leg['arr']['aTimeS'], self.parseDate(jny['date'])) if leg['arr'].get('aTimeR') is not None else None,
                        arrival_platform=leg['arr'].get('aPlatfR', leg['arr'].get('aPlatfS')),
                        stopovers=leg_stopovers
                    ))
            journeys.append(Journey(
                jny['ctxRecon'],
                date=self.parseDate(jny['date']),
                duration=self.parseTimedelta(jny['dur']),
                legs=legs
            ))
        return journeys


class StationBoardRequestType(Enum):
    DEPARTURE = 'DEP'
    ARRIVAL = 'ARR'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
