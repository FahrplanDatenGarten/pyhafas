import datetime
import os

from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey, Leg, Mode, Station, Stopover

from tests.types import PyTestHafasResponse


def test_db_journeys_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/journeys_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_journeys = [Journey(
        id='¶HKI¶T$A=1@O=Siegburg/Bonn@L=8005556@a=128@$A=1@O=Troisdorf@L=8000135@a=128@$202008061207$202008061212$S     19$$1$$$',
        date=datetime.date(2020, 8, 6),
        duration=datetime.timedelta(seconds=300),
        legs=[Leg(
            id='1|226393|0|80|6082020',
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
            departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 6, 12, 7)),
            arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 6, 12, 12)),
            mode=Mode.TRAIN,
            name='S 19',
            cancelled=False,
            distance=None,
            departure_delay=None,
            departure_platform='1',
            arrival_delay=datetime.timedelta(0),
            arrival_platform='1',
            stopovers=[Stopover(
                stop=Station(
                    id='8005556',
                    name='Siegburg/Bonn',
                    latitude=50.793916,
                    longitude=7.203029),
                cancelled=False,
                arrival=None,
                arrival_delay=None,
                arrival_platform=None,
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 6, 12, 7)),
                departure_delay=None,
                departure_platform='1'),
                Stopover(
                    stop=Station(
                        id='8000135',
                        name='Troisdorf',
                        latitude=50.813926,
                        longitude=7.150892),
                    cancelled=False,
                    arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 6, 12, 12)),
                    arrival_delay=datetime.timedelta(0),
                    arrival_platform='1',
                    departure=None,
                    departure_delay=None,
                    departure_platform=None
            )
            ]
        )]
    )]
    assert DBProfile().parse_journeys_request(hafas_response) == correct_journeys
