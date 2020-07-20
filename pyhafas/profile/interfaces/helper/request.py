import abc
from typing import Tuple

from pyhafas.types.hafas_response import HafasResponse


class RequestHelperInterface(abc.ABC):
    @abc.abstractmethod
    def calculate_checksum(self, data: str) -> str:
        pass

    @abc.abstractmethod
    def calculate_mic_mac(self, data: str) -> Tuple[str, str]:
        pass

    @abc.abstractmethod
    def url_formatter(self, data: str) -> str:
        pass

    @abc.abstractmethod
    def request(self, body) -> HafasResponse:
        pass
