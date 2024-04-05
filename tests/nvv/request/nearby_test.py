from pyhafas import HafasClient
from pyhafas.profile import NVVProfile
from pyhafas.types.nearby import LatLng
from tests.distance import calculate_distance_in_meters


def test_nvv_nearby_request():
    pos = LatLng(51.317862, 9.490816)
    client = HafasClient(NVVProfile())
    stations = client.nearby(pos)
    assert stations
    assert calculate_distance_in_meters(pos.latitude, pos.longitude, stations[0].latitude, stations[0].longitude) < 200
