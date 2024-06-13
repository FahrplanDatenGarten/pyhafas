import datetime

from pyhafas import HafasClient
from pyhafas.profile import NASAProfile
from pyhafas.types.fptf import Journey


# Test journey request with NASA profile
def test_nasa_journey_request():
    profile = NASAProfile()
    client = HafasClient(profile)
    journeys = client.journeys(
        origin='90053',
        destination='5232',
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys
    journey = client.journey(journey=journeys[0].id)
    assert isinstance(journey, Journey)
