import datetime
import os

from pyhafas.profile.vsn import VSNProfile
from pyhafas.types.fptf import Station, StationBoardLeg

from tests.types import PyTestHafasResponse


def test_vsn_departures_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/departures_raw.json", "r", encoding="utf8")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_station_board_legs = [StationBoardLeg(
        id='1|265947|0|80|1082020',
        name='IC 2315',
        direction='Frankfurt(Main) Hbf',
        station=Station(
            id='8000050',
            lid='A=1@O=Bremen Hbf@X=8813833@Y=53083478@U=80@L=8000050@',
            name='Bremen Hbf',
            latitude=53.083478,
            longitude=8.813833),
        date_time=VSNProfile().timezone.localize(datetime.datetime(2020, 8, 1, 17, 44)),
        cancelled=False,
        delay=datetime.timedelta(
            seconds=3480),
        platform='8')]
    assert VSNProfile().parse_station_board_request(
        hafas_response, "d") == correct_station_board_legs
