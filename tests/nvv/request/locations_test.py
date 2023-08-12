from pyhafas import HafasClient
from pyhafas.profile import NVVProfile


def test_kvb_locations_request():
    client = HafasClient(NVVProfile())
    locations = client.locations(term="Kassel Hbf")
    assert len(locations) >= 1
