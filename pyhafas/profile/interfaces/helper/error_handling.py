import abc
from enum import Enum


class ErrorCodesMappingInterface(Enum):
    default: Exception


class ErrorHandlingHelperInterface(abc.ABC):
    @abc.abstractmethod
    def check_for_errors(self, data: dict):
        pass
