from pyhafas import HafasClient
from pyhafas.profile import KVBProfile


def test_kvb_locations_request():
    client = HafasClient(KVBProfile())
    locations = client.locations(term="Bonn Hbf")
    assert len(locations) >= 1
