import datetime

from pyhafas import HafasClient
from pyhafas.profile import VVVProfile


def test_vvv_journeys_request():
    client = HafasClient(VVVProfile())
    journeys = client.journeys(
        destination="900006625",
        origin="480074302",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
