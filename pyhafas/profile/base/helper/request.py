import json
from hashlib import md5
from typing import Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base.mappings.error_codes import BaseErrorCodesMapping
from pyhafas.profile.interfaces.helper.request import RequestHelperInterface
from pyhafas.types.hafas_response import HafasResponse


class BaseRequestHelper(RequestHelperInterface):
    request_session = requests.session()

    def calculate_checksum(self: ProfileInterface, data: str) -> str:
        """
        Calculates the checksum of the request (required for most profiles)

        :param data: Complete body as string
        :return: Checksum for the request
        """
        return md5((data + self.salt).encode('utf-8')).hexdigest()

    def calculate_mic_mac(
            self: ProfileInterface,
            data: str) -> Tuple[str, str]:
        """
        Calculates the mic-mac for the request (required for some profiles)

        :param data: Complete body as string
        :return: Mic and mac to be sent to HaFAS
        """
        mic = md5(data.encode('utf-8')).hexdigest()
        mac = self.calculate_checksum(mic)
        return mic, mac

    def url_formatter(self: ProfileInterface, data: str) -> str:
        """
        Formats the URL for HaFAS (adds the checksum or mic-mac)

        :param data: Complete body as string
        :return: Request-URL (maybe with checksum or mic-mac)
        """
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

    def activate_retry(self: ProfileInterface) -> None:
        self.request_session = requests.Session()

        retries = 4
        backoff_factor = 0.3

        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
        )

        adapter = HTTPAdapter(max_retries=retry)
        self.request_session.mount("http://", adapter)
        self.request_session.mount("https://", adapter)

    def request(self: ProfileInterface, body) -> HafasResponse:
        """
        Sends the request and does a basic parsing of the response and error handling

        :param body: Reqeust body as dict (without the `requestBody` of the profile)
        :return: HafasRespone object or Exception when HaFAS response returns an error
        """
        data = {
            'svcReqL': [body]
        }
        data.update(self.requestBody)
        data = json.dumps(data)

        res = self.request_session.post(
            self.url_formatter(data),
            data=data,
            headers={
                'User-Agent': self.userAgent,
                'Content-Type': 'application/json'})
        return HafasResponse(res, BaseErrorCodesMapping)
