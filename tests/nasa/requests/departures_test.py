import datetime

from pyhafas import HafasClient
from pyhafas.profile import NASAProfile


def test_nasa_departures_request():
    client = HafasClient(NASAProfile())
    departures = client.departures(
        station="7482",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures
