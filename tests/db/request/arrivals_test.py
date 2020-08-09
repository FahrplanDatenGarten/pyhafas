import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile


def test_db_departures_request():
    client = HafasClient(DBProfile())
    arrivals = client.arrivals(
        station="8011160",
        date=datetime.datetime.now(),
        max_trips=2
    )
    assert len(arrivals) <= 2
