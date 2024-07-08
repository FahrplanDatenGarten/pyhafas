from pyhafas import HafasClient
from pyhafas.profile import OEBBProfile


def test_oebb_locations_request():
    client = HafasClient(OEBBProfile())
    locations = client.locations(term="Wien Hbf")
    assert len(locations) >= 1
