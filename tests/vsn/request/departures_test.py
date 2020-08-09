import datetime

from pyhafas import HafasClient
from pyhafas.profile import VSNProfile


def test_vsn_departures_request():
    client = HafasClient(VSNProfile())
    departures = client.departures(
        station="009033817",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures
