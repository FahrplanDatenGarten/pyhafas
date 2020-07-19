import abc
from typing import Tuple


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
    def request(self, body) -> dict:
        pass

    @abc.abstractmethod
    def format_response(self, data: dict) -> dict:
        pass
