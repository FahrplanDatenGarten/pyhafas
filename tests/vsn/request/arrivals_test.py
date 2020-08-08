import datetime

from pyhafas import HafasClient
from pyhafas.profile import VSNProfile


def test_vsn_arrivals_request():
    client = HafasClient(VSNProfile())
    arrivals = client.arrivals(
        station="009033817",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert arrivals
