import datetime

from pyhafas import HafasClient
from pyhafas.profile import KVBProfile


def test_kvb_journeys_request():
    client = HafasClient(KVBProfile())
    journeys = client.journeys(
        destination="900000687",
        origin="900000008",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys

def test_kvb_journeys_local_request():
    client = HafasClient(KVBProfile())
    journeys = client.journeys(
        destination="900000001",
        origin="900000039",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
