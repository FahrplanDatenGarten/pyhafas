import datetime

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.date_time import DateTimeHelperInterface


class BaseDateTimeHelper(DateTimeHelperInterface):
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
        return self.timezone.localize(datetime.datetime(
            date.year,
            date.month,
            date.day,
            hour,
            minute,
            second) + datetime.timedelta(days=dateOffset))

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

    def transform_datetime_parameter_timezone(
            self: ProfileInterface,
            date_time: datetime.datetime) -> datetime.datetime:
        """
        Transfers datetime parameters incoming by the user to the profile timezone

        :param date_time: datetime parameter incoming by user. Can be timezone aware or unaware
        :return: Timezone aware datetime object in profile timezone
        """
        if date_time.tzinfo is not None and date_time.tzinfo.utcoffset(
                date_time) is not None:
            return date_time.astimezone(self.timezone)
        else:
            return self.timezone.localize(date_time)
