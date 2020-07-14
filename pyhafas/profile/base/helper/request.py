import json
from hashlib import md5
from typing import Tuple

import requests

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.request import RequestHelperInterface


class BaseRequestHelper(RequestHelperInterface):
    def calculate_checksum(self: ProfileInterface, data: str) -> str:
        return md5((data + self.salt).encode('utf-8')).hexdigest()

    def calculate_mic_mac(
            self: ProfileInterface,
            data: str) -> Tuple[str, str]:
        mic = md5(data.encode('utf-8')).hexdigest()
        mac = self.calculate_checksum(mic)
        return mic, mac

    def url_formatter(self: ProfileInterface, data: str) -> str:
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

    def request(self: ProfileInterface, body) -> requests.Response:
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
