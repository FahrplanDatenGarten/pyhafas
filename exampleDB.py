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
]


for destination in destinations:
    journey = client.journeys(  # type: ignore
        origin=origin,
        destination=destination,
        date=datetime.datetime.now(),
        max_journeys=1,
    )
    print(journey)
