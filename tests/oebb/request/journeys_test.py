import datetime

from pyhafas import HafasClient
from pyhafas.profile import OEBBProfile
from pyhafas.types.fptf import Journey


def test_oebb_journeys_request():
    client = HafasClient(OEBBProfile())
    journeys = client.journeys(
        origin="8101277",
        destination="8101489",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1,
        max_journeys=1,
    )
    assert isinstance(journeys[0], Journey)
