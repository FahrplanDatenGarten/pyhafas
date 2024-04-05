from pyhafas import HafasClient
from pyhafas.profile import NASAProfile
from pyhafas.types.nearby import LatLng
from tests.distance import calculate_distance_in_meters


def test_nasa_nearby_request():
    pos = LatLng(52.131019, 11.622818)
    client = HafasClient(NASAProfile())
    stations = client.nearby(pos)
    assert stations
    assert calculate_distance_in_meters(pos.latitude, pos.longitude, stations[0].latitude, stations[0].longitude) < 200
