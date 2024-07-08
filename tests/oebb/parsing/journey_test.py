import datetime
import os

from pyhafas.profile import OEBBProfile
from pyhafas.types.fptf import Journey, Leg, Mode, Station, Stopover, Remark

from tests.types import PyTestHafasResponse


def test_oebb_journey_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/journey_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_journey = Journey(
        id="¶HKI¶T$A=1@O=Neunkirchen NÖ Bahnhof@L=8101277@a=128@$A=1@O=Wr.Neustadt Hbf@L=8100516@a=128@$202312252214$202312252225$CJX 9   $$1$$$$$$¶KRCC¶#VE#1#MRTF#",
        date=datetime.date(2023, 12, 25),
        duration=datetime.timedelta(seconds=660),
        legs=[
            Leg(
                id="2|#VN#1#ST#1703147972#PI#3#ZI#361277#TA#2#DA#251223#1S#8100027#1T#2155#LS#8100236#LT#2322#PU#181#RT#1#CA#CJX#ZE#9#ZB#CJX 9   #PC#4#FR#8100027#FT#2155#TO#8100236#TT#2322#",
                origin=Station(
                    id="8101277",
                    lid="A=1@O=Neunkirchen NÖ Bahnhof@X=16085100@Y=47731615@U=181@L=8101277@",
                    name="Neunkirchen NÖ Bahnhof",
                    latitude=47.731615,
                    longitude=16.085100,
                ),
                destination=Station(
                    id="8100516",
                    lid="A=1@O=Wr.Neustadt Hbf@X=16233656@Y=47811080@U=181@L=8100516@",
                    name="Wr.Neustadt Hbf",
                    latitude=47.81108,
                    longitude=16.233656,
                ),
                departure=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 25, 22, 14)
                ),
                arrival=OEBBProfile().timezone.localize(
                    datetime.datetime(2023, 12, 25, 22, 25)
                ),
                mode=Mode.TRAIN,
                name="CJX 9 (Zug-Nr. 2968)",
                cancelled=False,
                distance=None,
                departure_delay=datetime.timedelta(0),
                departure_platform="2",
                arrival_delay=datetime.timedelta(0),
                arrival_platform="2B-C",
                stopovers=[
                    Stopover(
                        stop=Station(
                            id="8101277",
                            lid="A=1@O=Neunkirchen NÖ Bahnhof@X=16085100@Y=47731615@U=181@L=8101277@",
                            name="Neunkirchen NÖ Bahnhof",
                            latitude=47.731615,
                            longitude=16.085100,
                        ),
                        cancelled=False,
                        arrival=None,
                        arrival_delay=None,
                        arrival_platform=None,
                        departure=OEBBProfile().timezone.localize(
                            datetime.datetime(2023, 12, 25, 22, 14)
                        ),
                        departure_delay=datetime.timedelta(0),
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
                            datetime.datetime(2023, 12, 25, 22, 18)
                        ),
                        arrival_delay=datetime.timedelta(0),
                        arrival_platform="2",
                        departure=OEBBProfile().timezone.localize(
                            datetime.datetime(2023, 12, 25, 22, 18)
                        ),
                        departure_delay=datetime.timedelta(0),
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
                            datetime.datetime(2023, 12, 25, 22, 25)
                        ),
                        arrival_delay=datetime.timedelta(0),
                        arrival_platform="2B-C",
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
        ],
    )
    assert OEBBProfile().parse_journey_request(hafas_response) == correct_journey
