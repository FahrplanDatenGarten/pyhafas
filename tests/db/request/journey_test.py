import datetime
import pytest

from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey


@pytest.mark.skip()
def test_db_journey_request():
    profile = DBProfile()
    client = HafasClient(profile)
    journeys = client.journeys(
        destination="8011306",
        origin="8011160",
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys

    journey = client.journey(journey=journeys[0].id)
    assert isinstance(journey, Journey)
