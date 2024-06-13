import datetime

from pyhafas import HafasClient
from pyhafas.profile import KVBProfile
from pyhafas.types.fptf import Journey


def test_kvb_journey_request():
    client = HafasClient(KVBProfile())
    journeys = client.journeys(
        destination="900000687",
        origin="900000008",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )

    journey = client.journey(
        journey=journeys[0].id
    )
    assert isinstance(journey, Journey)
