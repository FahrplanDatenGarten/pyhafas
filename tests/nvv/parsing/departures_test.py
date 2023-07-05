import datetime
import os

from pyhafas.profile import NVVProfile
from pyhafas.types.fptf import Station, StationBoardLeg

from tests.types import PyTestHafasResponse


def test_nvv_departures_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/departures_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_station_board_legs = [StationBoardLeg(
        id='2|#VN#1#ST#1688407889#PI#0#ZI#16504#TA#2#DA#50723#1S#2200012#1T#808#LS#2203069#LT#854#PU#80#RT#1#CA#T#ZE#5#ZB#Tram 5  #PC#5#FR#2200012#FT#808#TO#2203069#TT#854#',
        name='Tram 5',
        direction='Baunatal',
        station=Station(
            id='2200048',
            lid='A=1@O=Kassel Keilsbergstraße@X=9455942@Y=51279199@U=80@L=2200048@',
            name='Kassel Keilsbergstraße',
            latitude=51.279199,
            longitude=9.455942),
        date_time=NVVProfile().timezone.localize(datetime.datetime(2023, 7, 5, 8, 37)),
        cancelled=False,
        delay=datetime.timedelta(
            seconds=0))]
    assert NVVProfile().parse_station_board_request(
        hafas_response, "d") == correct_station_board_legs
