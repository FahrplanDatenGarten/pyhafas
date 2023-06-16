import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile

client = HafasClient(DBProfile(), debug=True)

origin = 8096009
destinations = [
    8011160,
    8010060,
    8000050,
    8000019,
    8071993,
    8000351,
    8005197,
    8000096,
    8010073,
    8010093,
    8011471,
    8013479,
    8013483,
    8010215,
    8013487,
    8012666,
    8010327,
    597502,
    8011044,
    8010016,
    8010139,
    8010153,
    8012963,
    8012585,
    8010241,
    8012617,
    8010304,
    8010033,
    8010324,
    8010338,
    8010381,
    8010392,
    8096022,
    8001235,
    8000310,
    8003992,
    8004004,
    8000323,
    8005247,
    182006,
    968306,
]


for destination in destinations:
    journey = client.journeys(  # type: ignore
        origin=origin,
        destination=destination,
        date=datetime.datetime.now(),
        max_journeys=1,
        products={
            "long_distance_express": False,
            "long_distance": False,
            "ferry": False,
            "bus": False,
            "suburban": False,
            "subway": False,
        },
    )
    print(journey)
