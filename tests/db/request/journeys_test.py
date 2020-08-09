import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile


def test_db_journeys_request():
    client = HafasClient(DBProfile())
    journeys = client.journeys(
        destination="8000135",
        origin="8005556",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
