import datetime

from pyhafas import HafasClient
from pyhafas.profile import KVBProfile


def test_kvb_departures_request():
    client = HafasClient(KVBProfile())
    departures = client.departures(
        station="300068712",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures
