import datetime

from pyhafas import HafasClient
from pyhafas.profile import KVBProfile


def test_kvb_arrivals_request():
    client = HafasClient(KVBProfile())
    arrivals = client.arrivals(
        station="300068712",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert arrivals
