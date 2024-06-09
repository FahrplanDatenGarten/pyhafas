from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.nearby import LatLng
from tests.distance import calculate_distance_in_meters


def test_db_nearby_request():
    pos = LatLng(52.523765, 13.369948)
    client = HafasClient(DBProfile())
    stations = client.nearby(pos)
    assert stations
    assert calculate_distance_in_meters(pos.latitude, pos.longitude, stations[0].latitude, stations[0].longitude) < 200
