from pyhafas import HafasClient
from pyhafas.profile import VSNProfile


def test_vsn_locations_request():
    client = HafasClient(VSNProfile())
    locations = client.locations(term="Göttingen Bahnhof/ZOB")
    assert len(locations) >= 1
