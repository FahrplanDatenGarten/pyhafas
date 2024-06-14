import datetime

from pyhafas import HafasClient
from pyhafas.profile import OEBBProfile


def test_oebb_departures_request():
    client = HafasClient(OEBBProfile())
    departures = client.departures(
        station="8101277", date=datetime.datetime.now(), max_trips=2
    )
    assert len(departures) <= 2
