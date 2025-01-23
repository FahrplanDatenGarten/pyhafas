import datetime
import os

from pyhafas.profile import OEBBProfile
from pyhafas.types.fptf import Station, StationBoardLeg

from tests.types import PyTestHafasResponse


def test_oebb_departures_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/departures_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_station_board_legs = [
        StationBoardLeg(
            id="2|#VN#1#ST#1703147972#PI#3#ZI#361303#TA#0#DA#241223#1S#8100027#1T#2255#LS#8100236#LT#10022#PU#181#RT#1#CA#CJX#ZE#9#ZB#CJX 9   #PC#4#FR#8100027#FT#2255#TO#8100236#TT#10022#",
            name="CJX 9 (Zug-Nr. 2972)",
            direction="Wien Floridsdorf Bahnhof",
            station=Station(
                id="8101277",
                lid="A=1@O=Neunkirchen N\u00d6 Bahnhof@X=16085100@Y=47731615@U=181@L=8101277@",
                name="Neunkirchen N\u00d6 Bahnhof",
                latitude=47.731615,
                longitude=16.085100,
            ),
            date_time=OEBBProfile().timezone.localize(
                datetime.datetime(2023, 12, 24, 23, 14)
            ),
            cancelled=False,
            delay=datetime.timedelta(seconds=0),
            platform="2",
        )
    ]

    assert (
        OEBBProfile().parse_station_board_request(hafas_response, "d")
        == correct_station_board_legs
    )
