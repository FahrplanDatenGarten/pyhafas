import datetime

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.parse_date_time import \
    ParseDateTimeHelperInterface


class BaseParseDateTimeHelper(ParseDateTimeHelperInterface):
    def parse_datetime(
            self: ProfileInterface,
            time_string: str,
            date: datetime.date) -> datetime.datetime:
        """
        Parses the time format HaFAS returns and combines it with a date

        :param time_string: Time string sent by HaFAS (multiple formats are supported. One example: 234000)
        :param date: Start day of the leg/journey
        :return: Parsed date and time as datetime object
        """
        try:
            hour = int(time_string[-6:-4])
            minute = int(time_string[-4:-2])
            second = int(time_string[-2:])
        except ValueError:
            raise ValueError(
                'Time string "{}" has wrong format'.format(time_string))

        dateOffset = int(time_string[:2]) if len(time_string) > 6 else 0
        return datetime.datetime(
            date.year,
            date.month,
            date.day,
            hour,
            minute,
            second) + datetime.timedelta(days=dateOffset)

    def parse_timedelta(
            self: ProfileInterface,
            time_string: str) -> datetime.timedelta:
        """
        Parses the time HaFAS returns as timedelta object

        Example use case is when HaFAS returns a duration of a leg
        :param time_string: Time string sent by HaFAS (example for format is: 033200)
        :return: Parsed time as timedelta object
        """
        try:
            hours = int(time_string[:2])
            minutes = int(time_string[2:-2])
            seconds = int(time_string[-2:])
        except ValueError:
            raise ValueError(
                'Time string "{}" has wrong format'.format(time_string))

        return datetime.timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds)

    def parse_date(self: ProfileInterface, date_string: str) -> datetime.date:
        """
        Parses the date HaFAS returns

        :param date_string: Date sent by HaFAS
        :return: Parsed date object
        """
        dt = datetime.datetime.strptime(date_string, '%Y%m%d')
        return dt.date()
