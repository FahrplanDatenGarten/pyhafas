from __future__ import annotations

import json
from enum import Enum
from hashlib import md5

import requests

from ..station import Station


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
            "svcReqL": [body]
        }
        data.update(self.requestBody)
        data = json.dumps(data)

        req = requests.post(
            self.urlFormatter(data),
            data=data,
            headers={
                "User-Agent": self.userAgent,
                "Content-Type": "application/json"})
        return req

    def calculateChecksum(self, data):
        to_hash = data + self.salt
        to_hash = to_hash.encode("utf-8")
        return md5(to_hash).hexdigest()

    def calculateMicMac(self, data):
        mic = md5(data.encode("utf-8")).hexdigest()
        mac = md5((mic + self.salt).encode("utf-8")).hexdigest()
        return mic, mac

    @staticmethod
    def formatStationBoardRequest(
            station: Station,
            request_type: StationBoardRequestType):
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


class StationBoardRequestType(Enum):
    DEPARTURE = 'DEP'
    ARRIVAL = 'ARR'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
