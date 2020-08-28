import datetime
import os

from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Leg, Mode, Station, Stopover

from tests.types import PyTestHafasResponse


def test_db_trips_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/trip_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_trip = Leg(
        id='1|227083|0|80|5082020',
        origin=Station(
            id='8002753',
            name='Hennef(Sieg)',
            latitude=50.773331,
            longitude=7.284588),
        destination=Station(
            id='8000084',
            name='Düren',
            latitude=50.809513,
            longitude=6.482454
        ),
        departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 2)),
        arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 17)),
        mode=Mode.TRAIN,
        name='S 19',
        cancelled=False,
        distance=None,
        departure_delay=None,
        departure_platform='2',
        arrival_delay=None,
        arrival_platform='5',
        stopovers=[
            Stopover(
                stop=Station(
                    id='8002753',
                    name='Hennef(Sieg)',
                    latitude=50.773331,
                    longitude=7.284588
                ),
                cancelled=False,
                arrival=None,
                arrival_delay=None,
                arrival_platform=None,
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 2)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8005556',
                    name='Siegburg/Bonn',
                    latitude=50.793916,
                    longitude=7.203029
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 6)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 7)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8000135',
                    name='Troisdorf',
                    latitude=50.813926,
                    longitude=7.150892
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 12)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 13)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8005629',
                    name='Spich',
                    latitude=50.826727,
                    longitude=7.114917
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 15)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 16)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8004873',
                    name='Porz-Wahn',
                    latitude=50.858135,
                    longitude=7.079266
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 19)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 19)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8003330',
                    name='Köln/Bonn Flughafen',
                    latitude=50.8789,
                    longitude=7.119304
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 23)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 24)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8003358',
                    name='Köln Frankfurter Straße',
                    latitude=50.915217,
                    longitude=7.051264
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 29)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 29)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8003320',
                    name='Köln Trimbornstr',
                    latitude=50.935856,
                    longitude=6.996736),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 34)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 34)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8083368',
                    name='Köln Messe/Deutz Gl. 9-10',
                    latitude=50.941303,
                    longitude=6.97464),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 36)),
                arrival_delay=None,
                arrival_platform='10',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 37)),
                departure_delay=None,
                departure_platform='10'
            ), Stopover(
                stop=Station(
                    id='8000207',
                    name='Köln Hbf',
                    latitude=50.943029,
                    longitude=6.95873
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 39)),
                arrival_delay=None,
                arrival_platform='11 B-C',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 40)),
                departure_delay=None,
                departure_platform='11 B-C'
            ), Stopover(
                stop=Station(
                    id='8003392',
                    name='Köln Hansaring',
                    latitude=50.949133,
                    longitude=6.952563
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 42)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 42)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8000208',
                    name='Köln-Ehrenfeld',
                    latitude=50.951533,
                    longitude=6.91728),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 45)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 46)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8003375',
                    name='Köln-Müngersdorf Technologiepark',
                    latitude=50.948396,
                    longitude=6.8882
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 48)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 49)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8003732',
                    name='Lövenich',
                    latitude=50.94293,
                    longitude=6.834436
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 51)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 52)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8003383',
                    name='Köln-Weiden West',
                    latitude=50.940899,
                    longitude=6.815136
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 53)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 54)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8002389',
                    name='Frechen-Königsdorf',
                    latitude=50.936503,
                    longitude=6.777849
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 56)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 12, 57)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8000178',
                    name='Horrem',
                    latitude=50.91625,
                    longitude=6.713495
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 0)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 1)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8005575',
                    name='Sindorf',
                    latitude=50.903711,
                    longitude=6.681107
                ), cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 3)),
                arrival_delay=None,
                arrival_platform='1',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 3)),
                departure_delay=None,
                departure_platform='1'
            ), Stopover(
                stop=Station(
                    id='8001264',
                    name='Buir',
                    latitude=50.862405,
                    longitude=6.574513
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 9)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 10)),
                departure_delay=None,
                departure_platform='2'
            ), Stopover(
                stop=Station(
                    id='8003990',
                    name='Merzenich',
                    latitude=50.840031,
                    longitude=6.518051
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 13)),
                arrival_delay=None,
                arrival_platform='2',
                departure=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 13)),
                departure_delay=None,
                departure_platform='2'
            ),
            Stopover(
                stop=Station(
                    id='8000084',
                    name='Düren',
                    latitude=50.809513,
                    longitude=6.482454
                ),
                cancelled=False,
                arrival=DBProfile().timezone.localize(datetime.datetime(2020, 8, 5, 13, 17)),
                arrival_delay=None,
                arrival_platform='5',
                departure=None,
                departure_delay=None,
                departure_platform=None
            )
        ]
    )
    assert DBProfile().parse_trip_request(hafas_response) == correct_trip
