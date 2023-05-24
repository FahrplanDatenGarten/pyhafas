import datetime
import os

from pyhafas.profile.kvb import KVBProfile
from pyhafas.types.fptf import Station, StationBoardLeg

from tests.types import PyTestHafasResponse


def test_kvb_departures_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/departures_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_station_board_legs = [StationBoardLeg(
        id='1|119823|0|1|24052023',
        name='609',
        direction='Bonn Brüser Berg Hardthöhe/Südwache',
        station=Station(
            id='300068712',
            lid='A=1@O=Bonn Hbf@X=7099420@Y=50731810@U=1@L=300068712@',
            name='Bonn Hbf',
            latitude=50.731810,
            longitude=7.099420),
        date_time=KVBProfile().timezone.localize(datetime.datetime(2023, 5, 24, 15, 57)),
        cancelled=False,
        delay=datetime.timedelta(
            seconds=600),
        platform='D2')]
    assert KVBProfile().parse_station_board_request(
        hafas_response, "d") == correct_station_board_legs
