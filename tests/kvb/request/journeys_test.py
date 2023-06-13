import datetime

from pyhafas import HafasClient
from pyhafas.profile import VSNProfile


def test_vsn_journeys_request():
    client = HafasClient(VSNProfile())
    journeys = client.journeys(
        destination="009033817",
        origin="009054997",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
