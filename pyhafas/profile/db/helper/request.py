import json

import requests

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base.helper.request import BaseRequestHelper
from pyhafas.profile.base.mappings.error_codes import BaseErrorCodesMapping
from pyhafas.types.hafas_response import HafasResponse
from tenacity import (
    retry,
    retry_if_exception_type,
    wait_exponential,
    stop_after_attempt,
)


class DBRequestHelper(BaseRequestHelper):
    tenacity_multiplier = 20
    tenacity_retry_attempts = 4

    @retry(
        wait=wait_exponential(multiplier=tenacity_multiplier),
        stop=stop_after_attempt(tenacity_retry_attempts),
        retry=retry_if_exception_type(requests.ConnectionError),
    )
    def request(self: ProfileInterface, body) -> HafasResponse:
        """
        Sends the request and does a basic parsing of the response and error handling

        :param body: Reqeust body as dict (without the `requestBody` of the profile)
        :return: HafasRespone object or Exception when HaFAS response returns an error
        """
        data = {"svcReqL": [body]}
        data.update(self.requestBody)
        data = json.dumps(data)

        print("Requesting")
        res = requests.post(
            self.url_formatter(data),
            data=data,
            headers={"User-Agent": self.userAgent, "Content-Type": "application/json"},
        )
        return HafasResponse(res, BaseErrorCodesMapping)
