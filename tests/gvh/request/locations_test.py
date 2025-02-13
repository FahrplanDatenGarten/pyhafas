from pyhafas import HafasClient
from pyhafas.profile.gvh import GVHProfile


def test_gvh_locations_request():
    client = HafasClient(GVHProfile())

    locations_lister_platz = client.locations(term="Lister Platz")
    assert len(locations_lister_platz) >= 1

    locations_hauptbahnhof = client.locations(term="Hannover Hauptbahnhof")
    assert len(locations_hauptbahnhof) >= 1

    locations_aegi = client.locations(term="Aegidientorplatz")
    assert len(locations_aegi) >= 1
