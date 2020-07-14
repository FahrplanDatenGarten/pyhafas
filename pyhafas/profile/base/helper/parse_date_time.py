import datetime

from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.parse_date_time import \
    ParseDateTimeHelperInterface


class BaseParseDateTimeHelper(ParseDateTimeHelperInterface):
    def parse_datetime(
            self: ProfileInterface,
            time_string: str,
            date: datetime.date) -> datetime.datetime:
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
        dt = datetime.datetime.strptime(date_string, '%Y%m%d')
        return dt.date()
