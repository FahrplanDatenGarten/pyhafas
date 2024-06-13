import datetime

from pyhafas import HafasClient
from pyhafas.profile import VVVProfile
from pyhafas.types.fptf import Journey


def test_vvv_journey_request():
    client = HafasClient(VVVProfile())
    journeys = client.journeys(
        destination="480045200",
        origin="480058500",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
    journey = client.journey(journey=journeys[0].id)
    assert isinstance(journey, Journey)
