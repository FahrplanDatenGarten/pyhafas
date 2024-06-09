from pyhafas import HafasClient
from pyhafas.profile import VVVProfile
from pyhafas.types.nearby import LatLng
from tests.distance import calculate_distance_in_meters


def test_vvv_nearby_request():
    pos = LatLng(47.272502, 9.638032)
    client = HafasClient(VVVProfile())
    stations = client.nearby(pos)
    assert stations
    assert calculate_distance_in_meters(pos.latitude, pos.longitude, stations[0].latitude, stations[0].longitude) < 200
