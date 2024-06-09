from pyhafas import HafasClient
from pyhafas.profile import VSNProfile
from pyhafas.types.nearby import LatLng
from tests.distance import calculate_distance_in_meters


def test_vsn_nearby_request():
    pos = LatLng(51.536403, 9.927406)
    client = HafasClient(VSNProfile())
    stations = client.nearby(pos)
    assert stations
    assert calculate_distance_in_meters(pos.latitude, pos.longitude, stations[0].latitude, stations[0].longitude) < 200
