import datetime

from pyhafas import HafasClient
from pyhafas.profile import NVVProfile


def test_nvv_journeys_request():
    client = HafasClient(NVVProfile())
    journeys = client.journeys(
        destination="2202508",
        origin="2200001",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
