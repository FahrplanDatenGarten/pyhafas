import datetime

from pyhafas import HafasClient
from pyhafas.profile import OEBBProfile


def test_oebb_arrivals_request():
    client = HafasClient(OEBBProfile())
    arrivals = client.arrivals(
        station="8101277", date=datetime.datetime.now(), max_trips=2
    )
    assert len(arrivals) <= 2
