import datetime

from pyhafas import HafasClient
from pyhafas.profile import VVVProfile


def test_vvv_arrivals_request():
    client = HafasClient(VVVProfile())
    arrivals = client.arrivals(
        station="480063000",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert arrivals


