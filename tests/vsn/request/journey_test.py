from pyhafas import HafasClient
from pyhafas.profile import VSNProfile
from pyhafas.types.fptf import Journey
import datetime


def test_vsn_journey_request():
    client = HafasClient(VSNProfile())
    journeys = client.journeys(
        destination="9068991",
        origin="9033817",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )

    journey = client.journey(
        journey=journeys[0].id
    )
    assert isinstance(journey, Journey)
