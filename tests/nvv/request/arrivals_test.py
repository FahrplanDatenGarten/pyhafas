import datetime

from pyhafas import HafasClient
from pyhafas.profile import NVVProfile


def test_kvb_arrivals_request():
    client = HafasClient(NVVProfile())
    arrivals = client.arrivals(
        station="2200001",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert arrivals


