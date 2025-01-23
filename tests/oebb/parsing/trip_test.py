import datetime
import os

from pyhafas.profile import OEBBProfile
from pyhafas.types.fptf import Leg, Mode, Station, Stopover, Remark

from tests.types import PyTestHafasResponse

import json

def test_oebb_trips_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/trip_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_trip = Leg(
        id="2|#VN#1#ST#1703147972#PI#3#ZI#361076#TA#0#DA#261223#1S#8100027#1T#525#LS#8103000#LT#638#PU#181#RT#1#CA#CJX#ZE#9#ZB#CJX 9   #PC#4#FR#8100027#FT#525#TO#8103000#TT#638#",
        origin=Station(
            id="8100027",
            lid="A=1@O=Payerbach-Reichenau Bahnhof@X=15863012@Y=47696054@U=181@L=8100027@",
            name="Payerbach-Reichenau Bahnhof",
            latitude=47.696054,
            longitude=15.863012,
        ),
        destination=Station(
            id="8103000",
            lid="A=1@O=Wien Hbf@X=16377114@Y=48185103@U=181@L=8103000@",
            name="Wien Hbf",
            latitude=48.185103,
            longitude=16.377114,
        ),
        departure=OEBBProfile().timezone.localize(
            datetime.datetime(2023, 12, 26, 5, 25)
        ),
        arrival=OEBBProfile().timezone.localize(datetime.datetime(2023, 12, 26, 6, 38)),
        mode=Mode.TRAIN,
        name="CJX 9 (Zug-Nr. 2902)",
        cancelled=False,
        distance=None,
        departure_delay=None,
        departure_platform="1A",
        arrival_delay=None,
        arrival_platform="11A-B",
        stopovers=[
            Stopover(
                stop=Station(
                    id="8100027",
                    lid="A=1@O=Payerbach-Reichenau Bahnhof@X=15863012@Y=47696054@U=181@L=8100027@",
                    name="Payerbach-Reichenau Bahnhof",
                    latitude=47.696054,
                    longitude=15.863012,
                ),
                cancelled=False,
                arrival=None,
                arrival_delay=None,
                arrival_platform=None,
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 25)
                ),
                departure_delay=None,
                departure_platform="1A",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8100587",
                    lid="A=1@O=Schlöglmühl Bahnhof@X=15914314@Y=47682525@U=181@L=8100587@",
                    name="Schlöglmühl Bahnhof",
                    latitude=47.682525,
                    longitude=15.914314,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 29)
                ),
                arrival_delay=None,
                arrival_platform="1",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 30)
                ),
                departure_delay=None,
                departure_platform="1",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8100026",
                    lid="A=1@O=Gloggnitz Bahnhof@X=15945902@Y=47677698@U=181@L=8100026@",
                    name="Gloggnitz Bahnhof",
                    latitude=47.677698,
                    longitude=15.945902,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 33)
                ),
                arrival_delay=None,
                arrival_platform="1",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 34)
                ),
                departure_delay=None,
                departure_platform="1",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8101390",
                    lid="A=1@O=Pottschach Bahnhof@X=16006264@Y=47697132@U=181@L=8101390@",
                    name="Pottschach Bahnhof",
                    latitude=47.697132,
                    longitude=16.006264,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 37)
                ),
                arrival_delay=None,
                arrival_platform="1",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 37)
                ),
                departure_delay=None,
                departure_platform="1",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8101661",
                    lid="A=1@O=Ternitz Bahnhof@X=16033205@Y=47713529@U=181@L=8101661@",
                    name="Ternitz Bahnhof",
                    latitude=47.713529,
                    longitude=16.033205,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 40)
                ),
                arrival_delay=None,
                arrival_platform="3",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 40)
                ),
                departure_delay=None,
                departure_platform="3",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8101277",
                    lid="A=1@O=Neunkirchen NÖ Bahnhof@X=16085100@Y=47731615@U=181@L=8101277@",
                    name="Neunkirchen NÖ Bahnhof",
                    latitude=47.731615,
                    longitude=16.085100,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 43)
                ),
                arrival_delay=None,
                arrival_platform="2",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 44)
                ),
                departure_delay=None,
                departure_platform="2",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8101489",
                    lid="A=1@O=St.Egyden am Steinfeld Bahnhof@X=16146748@Y=47760992@U=181@L=8101489@",
                    name="St.Egyden am Steinfeld Bahnhof",
                    latitude=47.760992,
                    longitude=16.146748,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 47)
                ),
                arrival_delay=None,
                arrival_platform="2",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 48)
                ),
                departure_delay=None,
                departure_platform="2",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    id="8100516",
                    lid="A=1@O=Wr.Neustadt Hbf@X=16233656@Y=47811080@U=181@L=8100516@",
                    name="Wr.Neustadt Hbf",
                    latitude=47.81108,
                    longitude=16.233656,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 5, 54)
                ),
                arrival_delay=None,
                arrival_platform="3B-C",
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 6, 0)
                ),
                departure_delay=None,
                departure_platform="3B-C",
                remarks=[],
            ),
            Stopover(
                stop=Station(
                    name="Baden b.Wien Bahnhof",
                    lid="A=1@O=Baden b.Wien Bahnhof@X=16242780@Y=48004051@U=181@L=8100025@",
                    id="8100025",
                    latitude=48.004051,
                    longitude=16.242780,
                ),
                cancelled=False,
                arrival=None,
                arrival_delay=None,
                arrival_platform=None,
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 6, 12)
                ),
                departure_delay=None,
                departure_platform="2",
                remarks=[
                    Remark(
                        remark_type="R",
                        code="text.realtime.stop.exit.disabled",
                        subject=None,
                        text="Hält nur zum Einsteigen",
                        priority=None,
                        trip_id=None,
                    )
                ],
            ),
            Stopover(
                stop=Station(
                    id="8100514",
                    lid="A=1@O=Wien Meidling Bahnhof@X=16333733@Y=48174585@U=181@L=8100514@",
                    name="Wien Meidling Bahnhof",
                    latitude=48.174585,
                    longitude=16.333733,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 6, 31)
                ),
                arrival_delay=None,
                arrival_platform="6",
                departure=None,
                departure_delay=None,
                departure_platform=None,
                remarks=[
                    Remark(
                        remark_type="R",
                        code="text.realtime.stop.entry.disabled",
                        subject=None,
                        text="Hält nur zum Aussteigen",
                        priority=None,
                        trip_id=None,
                    )
                ],
            ),
            Stopover(
                stop=Station(
                    id="8103000",
                    lid="A=1@O=Wien Hbf@X=16377114@Y=48185103@U=181@L=8103000@",
                    name="Wien Hbf",
                    latitude=48.185103,
                    longitude=16.377114,
                ),
                cancelled=False,
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 26, 6, 38)
                ),
                arrival_delay=None,
                arrival_platform="11A-B",
                departure=None,
                departure_delay=None,
                departure_platform=None,
                remarks=[],
            ),
        ],
        remarks=[
            Remark(
                remark_type="A",
                code="OB",
                subject=None,
                text="Niederflurfahrzeug",
                priority=0,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="RO",
                subject=None,
                text="Rollstuhlstellplatz",
                priority=150,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="OA",
                subject=None,
                text="Rollstuhlstellplatz - Voranmeldung unter +43 5 1717",
                priority=150,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="EF",
                subject=None,
                text="Fahrzeuggebundene Einstiegshilfe",
                priority=150,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="OC",
                subject=None,
                text="rollstuhltaugliches WC",
                priority=150,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="FK",
                subject=None,
                text="Fahrradmitnahme begrenzt möglich",
                priority=250,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="K2",
                subject=None,
                text="nur 2. Klasse",
                priority=300,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="SB",
                subject=None,
                text="Zustieg im Nahverkehr (REX, R, CJX, S-Bahn) nur mit gültiger Fahrkarte",
                priority=350,
                trip_id=None,
            ),
            Remark(
                remark_type="A",
                code="WV",
                priority=710,
                subject=None,
                text="WLAN verfügbar",
                trip_id=None,
            ),
        ],
    )
    assert OEBBProfile().parse_trip_request(hafas_response) == correct_trip
