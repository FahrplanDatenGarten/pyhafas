import abc
import datetime


class ParseDateTimeHelperInterface(abc.ABC):
    @abc.abstractmethod
    def parse_datetime(
            self,
            time_string: str,
            date: datetime.date) -> datetime.datetime:
        pass

    @abc.abstractmethod
    def parse_timedelta(self, time_string: str) -> datetime.timedelta:
        pass

    @abc.abstractmethod
    def parse_date(self, date_string: str) -> datetime.date:
        pass
