import datetime

from pyhafas import HafasClient
from pyhafas.profile.gvh import GVHProfile
from pyhafas.types.fptf import Station


def test_gvh_departures_request():
    client = HafasClient(GVHProfile())

    # Lister Platz
    departures_lister_platz = client.departures(
        station="de:03241:2021",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures_lister_platz and len(departures_lister_platz) >= 1

    # Hauptbahnhof
    departures_hauptbahnhof = client.departures(
        station="de:03241:31",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert departures_hauptbahnhof and len(departures_hauptbahnhof) >= 1
