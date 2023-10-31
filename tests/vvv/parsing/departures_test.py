import datetime
import os

from pyhafas.profile import VVVProfile
from pyhafas.types.fptf import Station, StationBoardLeg

from tests.types import PyTestHafasResponse


def test_vvv_departures_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/departures_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_station_board_legs = [StationBoardLeg(
        id='2|#VN#1#ST#1698712882#PI#0#ZI#257543#TA#0#DA#11123#1S#480077901#1T#832#LS#480057101#LT#926#PU#81#RT#1#CA#V00#ZE#177#ZB#     177#PC#6#FR#480077901#FT#832#TO#480057101#TT#926#',
        name='Landbus 177',
        direction='Dornbirn Bahnhof',
        station=Station(
            id='480077901',
            lid='A=1@O=Ebnit Heumöser@X=9742491@Y=47345429@U=81@L=480077901@i=A×at:48:779:0:1@',
            name='Ebnit Heumöser',
            latitude=47.345429,
            longitude=9.742491),
        date_time=VVVProfile().timezone.localize(datetime.datetime(2023, 11, 1, 8, 32)),
        cancelled=False,
        delay=None)]
    assert VVVProfile().parse_station_board_request(
        hafas_response, "d") == correct_station_board_legs
