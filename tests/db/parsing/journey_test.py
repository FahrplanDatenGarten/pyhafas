import datetime
import os

from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey, Leg, Mode, Station, Stopover

from tests.types import PyTestHafasResponse


def test_db_journey_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/journey_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_journey = Journey(
        id='¶HKI¶T$A=1@O=Siegburg/Bonn@L=8005556@a=128@$A=1@O=Troisdorf@L=8000135@a=128@$202008081507$202008081512$S     19$$1$$$',
        date=datetime.date(2020, 8, 8),
        duration=datetime.timedelta(seconds=300),
        legs=[Leg(
            id='1|227361|0|80|8082020',
            origin=Station(
                id='8005556',
                name='Siegburg/Bonn',
                latitude=50.793916,
                longitude=7.203029),
            destination=Station(
                id='8000135',
                name='Troisdorf',
                latitude=50.813926,
                longitude=7.150892),
            departure=datetime.datetime(2020, 8, 8, 15, 7),
            arrival=datetime.datetime(2020, 8, 8, 15, 12),
            mode=Mode.TRAIN,
            name='S 19',
            cancelled=False, distance=None,
            departure_delay=datetime.timedelta(seconds=240),
            departure_platform='1',
            arrival_delay=datetime.timedelta(seconds=240),
            arrival_platform='1',
            stopovers=[Stopover(
                stop=Station(
                    id='8005556',
                    name='Siegburg/Bonn',
                    latitude=50.793916,
                    longitude=7.203029
                ),
                cancelled=False,
                arrival=None,
                arrival_delay=None,
                arrival_platform=None,
                departure=datetime.datetime(2020, 8, 8, 15, 7),
                departure_delay=datetime.timedelta(seconds=240),
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8000135',
                    name='Troisdorf',
                    latitude=50.813926,
                    longitude=7.150892
                ),
                cancelled=False,
                arrival=datetime.datetime(2020, 8, 8, 15, 12),
                arrival_delay=datetime.timedelta(seconds=240),
                arrival_platform='1',
                departure=None,
                departure_delay=None,
                departure_platform=None
            )
            ],
        )]
    )
    assert DBProfile().parse_journey_request(hafas_response) == correct_journey
