import datetime

from pyhafas import HafasClient
from pyhafas.profile import NVVProfile


def test_kvb_departures_request():
    client = HafasClient(NVVProfile())
    departures = client.departures(
        station="2200001",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures
