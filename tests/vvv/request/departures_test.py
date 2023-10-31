import datetime

from pyhafas import HafasClient
from pyhafas.profile import VVVProfile


def test_vvv_departures_request():
    client = HafasClient(VVVProfile())
    departures = client.departures(
        station="480063000",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures
