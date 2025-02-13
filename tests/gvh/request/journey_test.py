import datetime
from typing import List

from pyhafas import HafasClient
from pyhafas.profile.gvh import GVHProfile
from pyhafas.types.fptf import Journey


def test_gvh_journey_request():
    client = HafasClient(GVHProfile())
    journeys = client.journeys(
        origin="de:03241:31",  # Hauptbahnhof
        destination="de:03241:2021",  # Lister Platz
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    )

    assert isinstance(journeys, List)
    assert len(journeys) >= 1
    assert len(journeys[0].legs) >= 1
    assert journeys[0].legs[0].origin.name
    assert journeys[0].legs[0].destination.name
    for stopover in journeys[0].legs[0].stopovers:
        assert stopover.stop.name

    journey = client.journey(
        journey=journeys[0].id
    )
    assert isinstance(journey, Journey)
    assert journey.legs[0].origin.name
    assert journey.legs[0].destination.name
    for stopover in journey.legs[0].stopovers:
        assert stopover.stop.name