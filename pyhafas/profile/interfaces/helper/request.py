import abc
from typing import Tuple

from pyhafas.types.hafas_response import HafasResponse


class RequestHelperInterface(abc.ABC):
    @abc.abstractmethod
    def calculate_checksum(self, data: str) -> str:
        """
        Calculates the checksum of the request (required for most profiles)

        :param data: Complete body as string
        :return: Checksum for the request
        """
        pass

    @abc.abstractmethod
    def calculate_mic_mac(self, data: str) -> Tuple[str, str]:
        """
        Calculates the mic-mac for the request (required for some profiles)

        :param data: Complete body as string
        :return: Mic and mac to be sent to HaFAS
        """
        pass

    @abc.abstractmethod
    def url_formatter(self, data: str) -> str:
        """
        Formats the URL for HaFAS (adds the checksum or mic-mac)

        :param data: Complete body as string
        :return: Request-URL (maybe with checksum or mic-mac)
        """
        pass

    @abc.abstractmethod
    def request(self, body) -> HafasResponse:
        """
        Sends the request and does a basic parsing of the response and error handling

        :param body: Reqeust body as dict (without the `requestBody` of the profile)
        :return: HafasRespone object or Exception when HaFAS response returns an error
        """
        pass
