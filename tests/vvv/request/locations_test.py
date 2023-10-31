from pyhafas import HafasClient
from pyhafas.profile import VVVProfile


def test_vvv_locations_request():
    client = HafasClient(VVVProfile())
    locations = client.locations(term="Rankweil Bifangstr.")
    assert len(locations) >= 1
