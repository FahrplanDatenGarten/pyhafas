import datetime
import os

from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Station, StationBoardLeg

from tests.types import PyTestHafasResponse


def test_db_departures_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/departures_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_station_board_legs = [StationBoardLeg(
        id='1|200921|0|80|5082020',
        name='IC 2055',
        direction='Stralsund Hbf',
        station=Station(
            id='8098160',
            lid='A=1@O=Berlin Hbf (tief)@X=13369549@Y=52525589@U=80@L=8098160@',
            name='Berlin Hbf (tief)',
            latitude=52.525589,
            longitude=13.369549),
        date_time=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 18, 16)),
        cancelled=False,
        delay=datetime.timedelta(
            seconds=0),
        platform='6')]
    assert DBProfile().parse_station_board_request(
        hafas_response, "d") == correct_station_board_legs
