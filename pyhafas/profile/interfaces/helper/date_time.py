import abc
import datetime


class DateTimeHelperInterface(abc.ABC):
    @abc.abstractmethod
    def parse_datetime(
            self,
            time_string: str,
            date: datetime.date) -> datetime.datetime:
        """
        Parses the time format HaFAS returns and combines it with a date

        :param time_string: Time string sent by HaFAS
        :param date: Start day of the leg/journey
        :return: Parsed date and time as datetime object
        """
        pass

    @abc.abstractmethod
    def parse_timedelta(self, time_string: str) -> datetime.timedelta:
        """
        Parses the time HaFAS returns as timedelta object

        Example use case is when HaFAS returns a duration of a leg
        :param time_string: Time string sent by HaFAS
        :return: Parsed time as timedelta object
        """
        pass

    @abc.abstractmethod
    def parse_date(self, date_string: str) -> datetime.date:
        """
        Parses the date HaFAS returns

        :param date_string: Date returned from HaFAS
        :return: Parsed date object
        """
        pass

    @abc.abstractmethod
    def transform_datetime_parameter_timezone(
            self,
            date_time: datetime.datetime) -> datetime.datetime:
        """
        Transfers datetime parameters incoming by the user to the profile timezone

        :param date_time: datetime parameter incoming by user. Can be timezone aware or unaware
        :return: Timezone aware datetime object in profile timezone
        """
        pass
