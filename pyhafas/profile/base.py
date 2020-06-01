from __future__ import annotations

import datetime
import json
from enum import Enum
from hashlib import md5
from typing import Dict, List

import requests

from ..fptf import Journey, Station


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
            date: datetime.datetime
    ) -> Dict:
        # TODO: find out, what commented-out values mean and implement options
        return {
            'req': {
                'arrLocL': [{
                    'type': 'S',
                    'lid': 'A=1@L={}@'.format(destination.id)
                }],
                # 'viaLocL': None,
                'depLocL': [{
                    'type': 'S',
                    'lid': 'A=1@L={}@'.format(origin.id)
                }],
                'outDate': date.strftime("%Y%m%d"),
                'outTime': date.strftime("%H%M%S"),
                # 'jnyFltrL': [{
                #    'type': 'PROD',
                #    'mode': 'INC',
                #    'value': '1023'
                # }],
                # 'maxChg': -1,
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
        hour = int(timeString[:2])
        minute = int(timeString[2:-2])
        second = int(timeString[-2:])

        dateOffset = 0

        while (hour) - (24 * dateOffset) >= 24:
            dateOffset += 1

        return datetime.datetime(
            date.year,
            date.month,
            date.day,
            hour,
            minute,
            second)

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

    def parseLocationRequest(self, response: str) -> List[Station]:
        data = json.loads(response)
        stations = []
        for stn in data['svcResL'][0]['res']['match']['locL']:
            parsedLid = self.parseLid(lid=stn['lid'])
            latitude: int
            longitude: int
            if stn['crd']:
                latitude = stn['crd']['y'] / 1000000
                longitude = stn['crd']['x'] / 1000000
            elif parsedLid['X'] and parsedLid['Y']:
                latitude = parsedLid['Y'] / 1000000
                longitude = parsedLid['X'] / 1000000

            station = Station(
                id=stn['extId'],
                name=stn['name'],
                latitude=latitude,
                longitude=longitude)
            stations.append(station)
        return stations

    def parseJourneyRequest(self, response: str) -> Journey:
        pass

    def parseJourneysRequest(self, response: str) -> List[Journey]:
        data = json.loads(response)
        journeys = []

        if data.get('err') or data['svcResL'][0]['err'] != 'OK':
            raise Exception()

        for jny in data['svcResL'][0]['res']['outConL']:
            journeys.append(Journey(
                jny['ctxRecon'],
                date=self.parseDate(jny['date']),
                duration=self.parseTimedelta(jny['dur'])
            ))
            # TODO: Add more data

        return journeys


class StationBoardRequestType(Enum):
    DEPARTURE = 'DEP'
    ARRIVAL = 'ARR'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
