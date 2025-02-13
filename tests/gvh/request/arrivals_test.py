import datetime

from pyhafas import HafasClient
from pyhafas.profile.gvh import GVHProfile


def test_gvh_arrivals_request():
    client = HafasClient(GVHProfile())

    # Lister Platz
    arrivals_lister_platz = client.arrivals(
        station="de:03241:2021",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert arrivals_lister_platz and len(arrivals_lister_platz) >= 1

    # Hauptbahnhof
    arrivals_hauptbahnhof = client.arrivals(
        station="de:03241:31",
        date=datetime.datetime.now(),
        max_trips=5
    )
    assert arrivals_hauptbahnhof and len(arrivals_hauptbahnhof) >= 1
